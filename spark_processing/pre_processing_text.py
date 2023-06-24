from pyvi import ViTokenizer, ViPosTagger, ViUtils
import re

def get_stopwords_list(stop_file_path):
    with open(stop_file_path, 'r', encoding="utf-8") as f:
        stopwords = f.readlines()
        stop_set = set(m.strip() for m in stopwords)
        return list(frozenset(stop_set))

def preprocessing(text):
    # stopwords_lst = get_stopwords_list("vn_stopwords.txt")
    tags = ViPosTagger.postagging(ViTokenizer.tokenize(text))
    token = tags[0]
    tagg = tags[1]
    kw = []
    for i in range(len(tagg)):
        if tagg[i].startswith('N') or tagg[i].startswith('Np') or tagg[i].startswith('V') or tagg[i].startswith('A'):
            kw.append(token[i])
    return ' '.join(kw)