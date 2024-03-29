from pre_processing_text import preprocessing2
from rank_bm25 import BM25Okapi
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import numpy as np


class ExtractKeywordBM25:
    def __init__(self) -> None:
        self.vocab = []

    def set_vocab(self, vocab):
        self.vocab = vocab

    def pre_processing(self, text):
        return preprocessing2(text) # list of tokens

    def extract_kw(self, dict, num_kw):
        text = dict["Title"] + dict["Description"] + dict["Body"]
        text = self.pre_processing(text)
        

def preprocess_text(text):
    stemmer = SnowballStemmer("english")
    stop_words = set(stopwords.words("english"))
    tokens = word_tokenize(text.lower())
    tokens = [stemmer.stem(token) for token in tokens if token.isalnum()]
    tokens = [token for token in tokens if token not in stop_words]
    return tokens


text = """Trung tâm TP Huế hơn 20 km, các xã Quảng Ngạn, Quảng Công (huyện Quảng Điền) có 12 km bờ biển với nhiều bãi tắm đẹp, như: Tân Mỹ, Cương Giáng, Tân Thành, theo cổng thông tin điện tử tỉnh Thừa Thiên Huế. Không nổi tiếng và đông đúc như Thuận An (TP Huế) hay Vinh Thanh (huyện Phú Vang), bãi biển Tân Thành (xã Quảng Công, huyện Quảng Điền) mang vẻ đẹp của sự hoang sơ, yên bình. Ngoài nước biển trong xanh và bãi cát vàng, Tân Thành còn có những con ngõ nhỏ dẫn ra biển với hai hàng phi lao xanh lãng mạn và cả những món ăn dân dã của người dân địa phương ở chợ Cồn Gai. Cách trung tâm TP Huế hơn 20 km, các xã Quảng Ngạn, Quảng Công (huyện Quảng Điền) có 12 km bờ biển với nhiều bãi tắm đẹp, như: Tân Mỹ, Cương Giáng, Tân Thành, theo cổng thông tin điện tử tỉnh Thừa Thiên Huế. Không nổi tiếng và đông đúc như Thuận An (TP Huế) hay Vinh Thanh (huyện Phú Vang), bãi biển Tân Thành (xã Quảng Công, huyện Quảng Điền) mang vẻ đẹp của sự hoang sơ, yên bình. Ngoài nước biển trong xanh và bãi cát vàng, Tân Thành còn có những con ngõ nhỏ dẫn ra biển với hai hàng phi lao xanh lãng mạn và cả những món ăn dân dã của người dân địa phương ở chợ Cồn Gai. Sống ở thị xã Hương Trà (Thừa Thiên - Huế) nhưng đến 23/6, Hoàng Thế Lập (20 tuổi) mới đến bãi biển Tân Thành ở xã Quảng Công lần đầu tiên.  Ông Nguyễn Trình, công tác tại Đoàn xã Quảng Công, cho biết xã sở hữu đường bờ biển dài với điểm nhấn là hai bãi tắm Cương Gián và Tân Thành. Bãi tắm Cương Gián được chọn làm điểm đến vào dịp hè của nhiều du khách ở Huế và ngoại tỉnh. Cương Gián đang được đầu tư phát triển du lịch, một số khu nghỉ dưỡng bắt đầu đi vào hoạt động. Bãi biển Tân Thành vẫn còn khá hoang sơ và chủ yếu phục vụ dân địa phương. Sống ở thị xã Hương Trà (Thừa Thiên - Huế) nhưng đến 23/6, Hoàng Thế Lập (20 tuổi) mới đến bãi biển Tân Thành ở xã Quảng Công lần đầu tiên.  Ông Nguyễn Trình, công tác tại Đoàn xã Quảng Công, cho biết xã sở hữu đường bờ biển dài với điểm nhấn là hai bãi tắm Cương Gián và Tân Thành. Bãi tắm Cương Gián được chọn làm điểm đến vào dịp hè của nhiều du khách ở Huế và ngoại tỉnh. Cương Gián đang được đầu tư phát triển du lịch, một số khu nghỉ dưỡng bắt đầu đi vào hoạt động. Bãi biển Tân Thành vẫn còn khá hoang sơ và chủ yếu phục vụ dân địa phương. Thôn Tân Thành nằm trên trục đường trung tâm xã, nối liền phá Tam Giang với biển. Đường đến đây dễ đi, có thể di chuyển bằng xe máy hoặc ôtô theo hướng dẫn của ứng dụng chỉ đường. Cầu Tam Giang, dân địa phương thường gọi là cầu Ca Cút, được thông xe vào năm 2010 giúp quãng đường di chuyển từ TP Huế đến Quảng Công ngắn lại. Từ cầu Ca Cút, du khách đi thẳng theo trục đường 49B sẽ đến điểm đầu tiên của Quảng Công là chợ Cồn Gai, ông Trình cho biết thêm. "Hoàng hôn trên Cầu Tam Giang cũng là một khung cảnh đẹp đáng để thưởng thức, khi những vệt nắng cuối ngày rải lên mặt sông lấp lánh", Lập chia sẻ. Thôn Tân Thành nằm trên trục đường trung tâm xã, nối liền phá Tam Giang với biển. Đường đến đây dễ đi, có thể di chuyển bằng xe máy hoặc ôtô theo hướng dẫn của ứng dụng chỉ đường. Cầu Tam Giang, dân địa phương thường gọi là cầu Ca Cút, được thông xe vào năm 2010 giúp quãng đường di chuyển từ TP Huế đến Quảng Công ngắn lại. Từ cầu Ca Cút, du khách đi thẳng theo trục đường 49B sẽ đến điểm đầu tiên của Quảng Công là chợ Cồn Gai, ông Trình cho biết thêm. "Hoàng hôn trên Cầu Tam Giang cũng là một khung cảnh đẹp đáng để thưởng thức, khi những vệt nắng cuối ngày rải lên mặt sông lấp lánh", Lập chia sẻ. Trước khi ra đến biển, Lập đã bị ấn tượng bởi những con ngõ đi xuyên qua xóm, làng dẫn ra biển. Nhờ những rặng phi lao xanh, con đường thêm phần thơ mộng và thanh bình. Hình ảnh những đứa trẻ chạy nhảy, nô đùa trên đường xóm khiến Lập nhớ về tuổi thơ của mình, vui vẻ và không lo nghĩ. Trước khi ra đến biển, Lập đã bị ấn tượng bởi những con ngõ đi xuyên qua xóm, làng dẫn ra biển. Nhờ những rặng phi lao xanh, con đường thêm phần thơ mộng và thanh bình. Hình ảnh những đứa trẻ chạy nhảy, nô đùa trên đường xóm khiến Lập nhớ về tuổi thơ của mình, vui vẻ và không lo nghĩ. Ra đến biển, điều đầu tiên Lập nhìn thấy là nước biển xanh ở phía xa và những con thuyền nhỏ của người dân nằm im lìm trên bãi cát. Không đông đúc, không ồn ào, cũng không có những resort, khách sạn, hàng quán bày bán trên bãi biển. Lập có thể nghe rõ tiếng sóng vỗ ì oạp vào bờ và tiếng gió thổi qua những ngọn phi lao. "Như một bản nhạc du dương của đại dương", Lập nói. Ra đến biển, điều đầu tiên Lập nhìn thấy là nước biển xanh ở phía xa và những con thuyền nhỏ của người dân nằm im lìm trên bãi cát. Không đông đúc, không ồn ào, cũng không có những resort, khách sạn, hàng quán bày bán trên bãi biển. Lập có thể nghe rõ tiếng sóng vỗ ì oạp vào bờ và tiếng gió thổi qua những ngọn phi lao. "Như một bản nhạc du dương của đại dương", Lập nói. Lập đến biển vào khoảng 16h30, trời vẫn còn nắng gắt nhưng đã có một số người dân ra biển, ngồi dưới những bóng cây để trò chuyện, hóng gió. Những đứa trẻ chạy nhảy, nô đùa theo từng đợt sóng dội về bờ. Bãi cát tại đây dài và thoải, nước biển xanh và sạch, an toàn cho tắm biển. Lập đến biển vào khoảng 16h30, trời vẫn còn nắng gắt nhưng đã có một số người dân ra biển, ngồi dưới những bóng cây để trò chuyện, hóng gió. Những đứa trẻ chạy nhảy, nô đùa theo từng đợt sóng dội về bờ. Bãi cát tại đây dài và thoải, nước biển xanh và sạch, an toàn cho tắm biển. Không có khách du lịch, bãi biển chủ yếu là nơi nghỉ ngơi, thư giãn của người dân địa phương sau một ngày làm việc. Thi thoảng, lại có vài chiếc thuyền của người dân từ xa cập bờ trước khi hoàng hôn buông xuống. "Chỉ là những hình ảnh quen thuộc nhưng khi kết hợp lại tạo thành bức tranh bình yên đến nao lòng. Tôi cứ ngồi mãi ở đó ngắm cảnh mà không nỡ về", Lập chia sẻ. Không có khách du lịch, bãi biển chủ yếu là nơi nghỉ ngơi, thư giãn của người dân địa phương sau một ngày làm việc. Thi thoảng, lại có vài chiếc thuyền của người dân từ xa cập bờ trước khi hoàng hôn buông xuống. "Chỉ là những hình ảnh quen thuộc nhưng khi kết hợp lại tạo thành bức tranh bình yên đến nao lòng. Tôi cứ ngồi mãi ở đó ngắm cảnh mà không nỡ về", Lập chia sẻ. Nằm dọc bãi biển, cách khoảng 300 m là khu vực nhà dân. Du khách sẽ bắt gặp những khoảnh khắc người dân dắt trâu, bò đi dọc bãi biển trở về nhà.  Ông Trình cho biết thêm, du khách có thể tắm biển và cắm trại miễn phí, an toàn. Tuy nhiên, do không có cơ sở kinh doanh dịch vụ cắm trại, du khách nên chuẩn bị kỹ đồ dùng, dụng cụ cần thiết. Về ẩm thực, có một số hàng quán nằm trong khu dân cư để du khách thưởng thức. Du khách cũng có thể di chuyển đến chợ Cồn Gai mua các loại thủy, hải sản của đầm phá Tam Giang như cá trích, cá chình, cá vược, cá mú, cá bống với giá cả phải chăng để tổ chức tiệc nướng trên bãi biển. Lưu ý dọn dẹp sạch sẽ trước khi ra về. Du khách cũng có thể lưu trú tại một số homestay, khu nghỉ dưỡng ở bãi biển Cương Giáng cùng ở xã Quảng Điền, cách biển Tân Thành khoảng 5 km. Nằm dọc bãi biển, cách khoảng 300 m là khu vực nhà dân. Du khách sẽ bắt gặp những khoảnh khắc người dân dắt trâu, bò đi dọc bãi biển trở về nhà.  Ông Trình cho biết thêm, du khách có thể tắm biển và cắm trại miễn phí, an toàn. Tuy nhiên, do không có cơ sở kinh doanh dịch vụ cắm trại, du khách nên chuẩn bị kỹ đồ dùng, dụng cụ cần thiết. Về ẩm thực, có một số hàng quán nằm trong khu dân cư để du khách thưởng thức. Du khách cũng có thể di chuyển đến chợ Cồn Gai mua các loại thủy, hải sản của đầm phá Tam Giang như cá trích, cá chình, cá vược, cá mú, cá bống với giá cả phải chăng để tổ chức tiệc nướng trên bãi biển. Lưu ý dọn dẹp sạch sẽ trước khi ra về. Du khách cũng có thể lưu trú tại một số homestay, khu nghỉ dưỡng ở bãi biển Cương Giáng cùng ở xã Quảng Điền, cách biển Tân Thành khoảng 5 km. Gần biển Quảng Công còn có biển Hải Dương, rừng ngập mặn Rú Chá, phá Tam Giang. Xa hơn một chút có biển Thuận An, một trong những bãi biển nổi tiếng nhất tại Huế để du khách tham quan. Khung cảnh trên đường về cũng đẹp không kém với những đầm, phá, những đàn trâu thong dong gặm cỏ. Dù chưa có những dịch vụ du lịch, vui chơi đúng nghĩa cho du khách phương xa, Tân Thành vẫn là một điểm đến dành cho những người yêu thích sự yên bình, muốn được thư giãn, nghỉ ngơi. "Khung cảnh thanh bình, màu xanh dịu mắt của biển ở đây có thể giúp mọi người được chữa lành. Nhưng khi đến đây, hy vọng mọi người sẽ không phá vỡ khung cảnh yên tĩnh ở đó. Đi nhẹ nói khẽ và không để lại gì ngoài những dấu chân", Lập chia sẻ. Gần biển Quảng Công còn có biển Hải Dương, rừng ngập mặn Rú Chá, phá Tam Giang. Xa hơn một chút có biển Thuận An, một trong những bãi biển nổi tiếng nhất tại Huế để du khách tham quan. Khung cảnh trên đường về cũng đẹp không kém với những đầm, phá, những đàn trâu thong dong gặm cỏ. Dù chưa có những dịch vụ du lịch, vui chơi đúng nghĩa cho du khách phương xa, Tân Thành vẫn là một điểm đến dành cho những người yêu thích sự yên bình, muốn được thư giãn, nghỉ ngơi. "Khung cảnh thanh bình, màu xanh dịu mắt của biển ở đây có thể giúp mọi người được chữa lành. Nhưng khi đến đây, hy vọng mọi người sẽ không phá vỡ khung cảnh yên tĩnh ở đó. Đi nhẹ nói khẽ và không để lại gì ngoài những dấu chân", Lập chia sẻ."""
# vocab = [text]
tokens = preprocessing2(text)
# tokens = preprocess_text(text)
# print(tokens)
# Create a BM25 model
bm25 = BM25Okapi([tokens])

# Get BM25 scores for each term in the document
doc_scores = [bm25.get_scores(token) for token in tokens]
print(doc_scores)

# Sort the terms based on BM25 scores and extract top keywords
top_keyword_indices = sorted(range(len(doc_scores)), key=lambda i: doc_scores[i], reverse=True)[:5]
top_keywords = [tokens[i] for i in top_keyword_indices]

print("Top Keywords:", top_keywords)


# corpus = [
#     "Hello there good man!",
#     "It is quite windy in London",
#     "How is the weather today?"
# ]

# tokenized_corpus = [doc.split(" ") for doc in corpus]

# bm25 = BM25Okapi(tokenized_corpus)

# query = ""
# tokenized_query = query.split(" ")

# doc_scores = bm25.get_scores(tokenized_query)

# print(doc_scores)