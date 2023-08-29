import openai
import time
import re
from pre_processing_text import preprocessing

openai.api_key = '...'
#datcn-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


class ExtractKeywordChatGPT:

    def __init__(self):
        self.messages = [
            {"role": "system", "content": "professional assistant that extract keywords from text"},
        ]

    def pre_processing(self, text):
        return preprocessing(text)
    
    def extract_kw(self, dict, num_kw):
        text = dict["Title"] + dict["Description"] + dict["Body"]
        text = self.pre_processing(text)
        text = f"Trích xuất {num_kw} keywords quan trọng nhất từ đoạn văn sau, chú ý kết quả trả về chỉ bao gồm {num_kw} keywords đó và ngăn cách bởi dấu phẩy: " + text
        self.messages = [{"role": "user", "content": text}]
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.messages
        )
        reply = chat.choices[0].message.content       
        # self.messages.append({"role": "assistant", "content": reply})  
        
        reply = re.sub(r'[.]', '', reply)

        reply_lst = reply.split(", ")
        a = min(5, len(reply_lst))
        time.sleep(5)
        return reply_lst[:a]

