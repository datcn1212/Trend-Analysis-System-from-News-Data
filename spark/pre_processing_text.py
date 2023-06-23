from pyvi import ViTokenizer, ViPosTagger, ViUtils
import re

def preprocessing(text):
    # text = re.sub(r'[.,!%?\-={}\(\)]', '', text)
    tags = ViPosTagger.postagging(ViTokenizer.tokenize(text))
    token = tags[0]
    tagg = tags[1]
    kw = []
    for i in range(len(tagg)):
        if tagg[i].startswith('N') or tagg[i].startswith('Np') or tagg[i].startswith('V') or tagg[i].startswith('A'):
            kw.append(token[i])
    return ' '.join(kw)