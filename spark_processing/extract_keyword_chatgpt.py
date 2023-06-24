import openai
import time
import re
from pre_processing_text import preprocessing

openai.api_key = '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'

class ExtractKeywordChatGPT:

    def __init__(self):
        self.messages = [
            {"role": "system", "content": "professional assistant that extract keywords from text"},
        ]

    def pre_processing(self, text):
        return preprocessing(text)
    
    def extract_kw(self, dict, num_kw):
        text = dict["Title"] + dict["Description"] + dict["Body"][:200]
        # text = dict["Title"] + dict["Description"] 
        text = self.pre_processing(text)
        text = f"Trích xuất {num_kw} keywords quan trọng nhất từ đoạn văn sau, chú ý kết quả trả về chỉ bao gồm 5 keywords đó và ngăn cách bởi dấu phẩy: " + text
        self.messages.append(
            {"role": "user", "content": text},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.messages
        )
        reply = chat.choices[0].message.content       
        self.messages.append({"role": "assistant", "content": reply})  
        
        # remove '.' from answer if exists and replace '_' by ' '
        reply = re.sub(r'[.]', '', reply).replace('_', ' ') 

        reply_lst = reply.split(", ")
        time.sleep(5)
        return reply_lst
