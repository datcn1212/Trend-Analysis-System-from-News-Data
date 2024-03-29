import sparknlp
import pandas as pd
spark = sparknlp.start()

# Import the required modules and classes
from sparknlp.base import DocumentAssembler, Pipeline, LightPipeline
from sparknlp.annotator import (
    SentenceDetector,
    Tokenizer,
    YakeKeywordExtraction
)
import pyspark.sql.functions as F

# Step 1: Transforms raw texts to `document` annotation
document = DocumentAssembler() \
            .setInputCol("text") \
            .setOutputCol("document")

# Step 2: Sentence Detection
sentenceDetector = SentenceDetector() \
            .setInputCols("document") \
            .setOutputCol("sentence")

# Step 3: Tokenization
token = Tokenizer() \
            .setInputCols("sentence") \
            .setOutputCol("token") \
            .setContextChars(["(", ")", "?", "!", ".", ","])

# Step 4: Keyword Extraction
keywords = YakeKeywordExtraction() \
            .setInputCols("token") \
            .setOutputCol("keywords") \
            
# Define the pipeline
yake_pipeline = Pipeline(stages=[document, sentenceDetector, token, keywords])

# Create an empty dataframe
empty_df = spark.createDataFrame([['']]).toDF("text")

# Fit the dataframe to get the 
yake_Model = yake_pipeline.fit(empty_df)

light_model = LightPipeline(yake_Model)

text = '''
Tỷ phú người Áo Dietrich Mateschitz, nhà đồng sáng lập công ty nước tăng lực Red Bull, vừa qua đời ở tuổi 78.", "Body": "Thông tin được lãnh đạo đội đua Red Bull tại Austin, Texas (Mỹ) thông báo hôm 22/10. Chi tiết về nguyên nhân và nơi qua đời của ông chưa được nêu rõ. Ông Mateschitz sinh ngày 20/5/1944, là tỷ phú giàu nhất tại Áo, đứng thứ 71 trên thế giới theo xếp hạng của Forbes (tính đến lúc ông qua đời) với giá trị tài sản ròng ước tính 20,2 tỷ USD. Tỷ phú Mateschitz nổi tiếng với vai trò đồng sáng lập Red Bull cùng với doanh nhân Thái Lan Chaleo Yoovidhya. Cơ duyên bắt nguồn từ việc ông Mateschitz nhận thấy tiềm năng của loại thức uống năng lượng có tên Krating Daeng do ông Chaleo tạo ra. Họ bắt tay thành lập công ty vào năm 1984 để tìm đường đưa sản phẩm đến phương Tây. Sau khi hợp tác, ông Mateschitz đã nghiên cứu công thức của Krating Daeng trong ba năm để tiến hành một số điều chỉnh. Sau đó, công ty chính thức tung ra thị trường với tên gọi mới là Red Bull vào năm 1987 tại quê hương Áo. Dưới sự quản lý của Mateschitz, Red Bull nhanh chóng tăng thị phần của mình, đầu tiên là ở châu Âu, sau đó là Mỹ, nhờ các chiến dịch tiếp thị quảng bá các đặc tính kích thích của thức uống và các thỏa thuận tài trợ rộng rãi trong các môn đua xe thể thao, bóng đá, mạo hiểm và ngành công nghiệp âm nhạc. Không chỉ giúp nước tăng lực trở nên phổ biến trên toàn thế giới, Mateschitz còn xây dựng nên một đế chế thể thao, truyền thông, bất động sản và ẩm thực xung quanh thương hiệu này. Ông đã mở rộng đáng kể đầu tư vào thể thao, đặc biệt là đua xe thể thao và thể thao mạo hiểm. Hãng Red Bull của ông hiện điều hành các câu lạc bộ bóng đá, đội khúc côn cầu trên băng và đội đua F1. Tập đoàn này cũng có hợp đồng với hàng trăm vận động viên ở nhiều môn thể thao khác nhau và một chương trình phát triển tay đua chuyên sâu để đưa các tay đua đạt đến đẳng cấp hàng đầu. Mateschitz mua lại đội đua Jaguar Racing từ chủ sở hữu trước đó là Ford vào cuối năm 2004 và đổi tên thành Red Bull cho mùa giải 2005. Cuối năm đó, ông mua thêm đội Minardi và đổi tên thành Toro Rosso, sử dụng nó như một đội bồi dưỡng hạt giống cho Red Bull. Mohammed Ben Sulayem, Chủ tịch cơ quan quản lý thể thao môtô FIA, cho biết Mateschitz là một nhân vật tầm cỡ trong làng thể thao môtô. Chia sẻ với Sky Sports F1, Đội trưởng đội đua Red Bull Christian Horner cho biết nhiều người trong đội biết ơn vì những cơ hội mà ông đã mang lại, tầm nhìn của ông, sức mạnh của tính cách và không bao giờ sợ hãi để theo đuổi ước mơ. \"Đó là những gì ông ấy đã làm cho F1, chứng minh rằng bạn có thể tạo ra sự khác biệt\", ĐChristian Horner nói. Không chỉ lớn mạnh ở môn đua xe, công ty của tỷ phú Mateschitz còn điều hành các đội bóng đá ở các giải hàng đầu trên khắp Áo, Đức, Brazil và Mỹ. Họ khởi đầu bằng việc mua câu lạc bộ Áo SV Austria Salzburg vào năm 2005 và đổi tên thành Red Bull Salzburg. Đến 2009, tập đoàn của ông mua câu lạc bộ hạng năm SSV Markranstadt tại Đức và đổi tên thành RasenBallsport Leipzig và bồi dưỡng nó cho đến khi được thăng hạng lên Bundesliga vào năm 2016.  ( )"'''

light_result = light_model.fullAnnotate(text)[0]

keys_df = pd.DataFrame([(k.result, k.begin, k.end, k.metadata['score'],  k.metadata['sentence']) for k in light_result['keywords']],
                       columns = ['keywords','begin','end','score','sentence'])
keys_df['score'] = keys_df['score'].astype(float)


top_keywords = keys_df.drop_duplicates(subset='keywords').nlargest(10, 'score')

# Extract the keywords from the resulting DataFrame
top_keywords_list = top_keywords['keywords'].tolist()

print(top_keywords_list)

spark.stop()


