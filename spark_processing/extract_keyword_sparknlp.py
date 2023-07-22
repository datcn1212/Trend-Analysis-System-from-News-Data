# from rake_nltk import Rake
import sparknlp
import pandas as pd
from sparknlp.base import DocumentAssembler, Pipeline, LightPipeline
from sparknlp.annotator import (
    SentenceDetector,
    Tokenizer,
    YakeKeywordExtraction
)
import pyspark.sql.functions as F
from pre_processing_text import preprocessing


class ExtractKeywordSparkNLP:

    def __init__(self, spark):

        # self. rake = Rake()
        self.spark = spark

        self.document = DocumentAssembler() \
            .setInputCol("text") \
            .setOutputCol("document")
        
        self.sentenceDetector = SentenceDetector() \
            .setInputCols("document") \
            .setOutputCol("sentence")
        
        self.token = Tokenizer() \
            .setInputCols("sentence") \
            .setOutputCol("token") \
            .setContextChars(["(", ")", "?", "!", ".", ","])
        
        # keyword extraction
        self.keywords = YakeKeywordExtraction() \
            .setInputCols("token") \
            .setOutputCol("keywords") \
            
        self.yake_pipeline = Pipeline(stages=[self.document, self.sentenceDetector, self.token, self.keywords])
        self.empty_df = self.spark.createDataFrame([['']]).toDF("text")
        self.yake_Model = self.yake_pipeline.fit(self.empty_df)

        # main model
        self.light_model = LightPipeline(self.yake_Model)


    def pre_processing(self, text):
        return preprocessing(text)

    def extract_kw(self, dict, num_kw):
        text = dict["Title"] + dict["Description"] + dict["Body"]
        # text = self.pre_processing(text)

        light_result = self.light_model.fullAnnotate(text)[0]

        keys_df = pd.DataFrame([(k.result, k.metadata['score']) for k in light_result['keywords']],
                       columns = ['keywords', 'score'])
        keys_df['score'] = keys_df['score'].astype(float)

        top_keywords = keys_df.drop_duplicates(subset='keywords').nsmallest(num_kw, 'score')

        top_keywords_list = top_keywords['keywords'].tolist()

        return top_keywords_list    
