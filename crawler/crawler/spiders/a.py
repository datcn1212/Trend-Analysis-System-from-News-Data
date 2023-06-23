# import spacy

# # Load English tokenizer, tagger, parser and NER
# nlp = spacy.load("en_core_web_sm")

# text = ("When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him  seriously.")
# doc = nlp(text)

# # Analyze syntax
# print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
# print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# # Find named entities, phrases and concepts
# for entity in doc.ents:
#     print(entity.text, entity.label_)



# import spacy
# import pytextrank
# # example text
# text = "When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him  seriously."
# # load a spaCy model, depending on language, scale, etc.
# nlp = spacy.load("en_core_web_sm")
# # add PyTextRank to the spaCy pipeline
# nlp.add_pipe("textrank")
# doc = nlp(text)
# # examine the top-ranked phrases in the document
# for phrase in doc._.phrases[:6]:
#     print(phrase.text)


# from keybert import KeyBERT
doc = """Ngày 2/11, ông Nguyễn Minh Huy, Giám đốc Ban Quản lý dự án đầu tư xây dựng các công trình giao thông Đà Nẵng (cơ quan tổ chức lập quy hoạch), cho biết đã hoàn tất lấy ý kiến cộng đồng khu dân cư về đồ án điều chỉnh quy hoạch phân khu sân bay, tỷ lệ 1/2.000. Theo Quyết định điều chỉnh quy hoạch chung TP Đà Nẵng đến năm 2030, tầm nhìn 2045 được Chính phủ phê duyệt năm 2021, phân khu sân bay thuộc vùng lõi xanh, giới hạn bởi các tuyến đường Cách Mạng Tháng Tám, Trường Chinh, Điện Biên Phủ, Nguyễn Tri Phương, Nguyễn Hữu Thọ. Phạm vi nghiên cứu quy hoạch gần 1.327 ha, dân số khoảng 104.000, bao gồm khu vực cảng hàng không quốc tế Đà Nẵng, diện tích hơn 741 ha; còn lại là diện tích các phường Hòa Cường Bắc, Hòa Thuận Tây (quận Hải Châu); Thạc Gián, Chính Gián, Hòa Khê, An Khê (quận Thanh Khê); Khuê Trung, Hòa Thọ Đông, Hòa Phát (quận Cẩm Lệ). Đại diện Công ty cổ phần Viện Quy hoạch đô thị và nông thôn Quảng Nam (đơn vị tư vấn) giải thích mô hình đô thị sân bay là lấy sân bay làm trung tâm, các khu nhà ở, công trình thương mại, dịch vụ và khu chức năng đô thị khác được bố trí xung quanh. Với định hướng như vậy, phân khu sân bay được chia làm bốn khu vực. Trong đó, khu vực 1 (nằm ở vị trí trung tâm, ký hiệu SB) là cảng hàng không quốc tế, nội địa. Cảng sẽ được mở rộng thêm một đường băng để sẵn sàng phục vụ 30 triệu lượt khách/năm, mở thêm cửa hướng ra đường Trường Chinh với hệ thống hạ tầng dịch vụ, logistics kèm theo. Khu vực 2, diện tích đất hơn 112 ha, dân số hơn 12.000, gồm các ô đất tiếp giáp đường Nguyễn Tri Phương, Nguyễn Hữu Thọ, định hướng phát triển thương mại dịch vụ, khu vực miễn thuế, đáp ứng cho nhu cầu của hành khách sân bay và người dân TP Nẵng nói chung. Khu vực 3 rộng 130 ha, dân số gần 20.000, gồm các ô đất tiếp giáp đường Cách Mạng Tháng Tám, sẽ được nâng cấp, bổ sung hệ thống hạ tầng kỹ thuật và các tiện ích đô thị. Thành phố từng bước đưa cơ sở công nghiệp, tiểu thủ công nghiệp, kho xen lẫn khu dân cư gây ô nhiễm môi trường ở nơi này ra các khu, cụm công nghiệp tập trung, chuyển đổi chức năng đất phục vụ phát triển đô thị. Khu vực 4 rộng hơn 305 ha, dân số hơn 45.000, gồm các ô đất tiếp giáp với đường Điện Biên Phủ và Trường Chinh (quốc lộ 1A), sẽ được chỉnh trang, tái thiết, nâng cấp bổ sung hệ thống hạ tầng kỹ thuật và các tiện ích đô thị phục vụ nhu cầu của người dân. trục đông tây kết nối tuyến Điện Biên Phủ ở phía bắc, tuyến ngầm Trưng Nữ Vương quy hoạch mới đi qua sân bay nối Lê Trọng Tấn, kết hợp với tuyến tàu điện ngầm, tuyến Lê Đại Hành và Cách Mạng Tháng Tám. Còn trục bắc nam là tuyến đường Trường Chinh ở phía tây và tuyến Nguyễn Tri Phương, Nguyễn Hữu Thọ ở phía đông. Ngoài ra, thành phố còn có các trục giao thông quan trọng hình thành cấu trúc đô thị như tuyến Ông Ích Đường, Hà Tông Quyền, Nguyễn Phước Tần, Tôn Thất Thuyết... ở phía nam; tuyến Hà Huy Tập, Huỳnh Ngọc Huệ... ở phía bắc. Quy hoạch này cũng nhằm tăng cường kết nối đô thị sân bay với phân khu ven sông Hàn và bờ đông, khu lõi xanh; phân khu ven vịnh Đà Nẵng và khu đổi mới sáng tạo; kết nối các tuyến giao thông công cộng và tuyến đường sắt đô thị. Nhà ga sân bay là công trình điểm nhấn quan trọng của phân khu. Ngoài ra, đơn vị tư vấn đề xuất xây dựng các công trình công cộng thương mại dịch vụ tại các nút giao quan trọng, cửa ngõ ra vào sân bay, để tạo điểm nhấn và đảm bảo các chức năng thương mại dịch vụ, bệnh viện, công cộng...  đơn vị tư vấn cho biết khu vực quy hoạch có hơn 50% là diện tích nằm trong sân bay, khu quân sự nên việc ngầm hóa là cần thiết. Diện tích ngầm sẽ được bố trí tại lô đất thương mại dịch vụ, công cộng, bệnh viện. Toàn bộ đất thương mại dịch vụ và công trình công cộng sẽ được bố trí bãi xe ngầm, tăng diện tích cảnh quan cây xanh trên bề mặt. Các bệnh viện cũng được khuyến cáo có bãi đỗ xe ngầm nhằm tối ưu hóa không gian sử dụng và ngăn cách với khu dân cư bên ngoài khi cần cách ly vì dịch bệnh. Độ sâu không gian ngầm có thể chia làm 3 lớp. Lớp 0-5 m phục vụ xây dựng hạ tầng kỹ thuật ngầm như lối vào tầng hầm, hầm đi bộ; 5-15 m xây công trình công cộng, bãi đỗ xe đảm bảo chỉ tiêu 4 m2/người; trên 15 m xây các công trình hạ tầng kỹ thuật. Hệ thống điện cũng nên ưu tiên ngầm hóa. Theo ông Nguyễn Minh Huy, điều chỉnh quy hoạch phân khu sân bay không chỉ nhằm khai thác tiềm năng của sân bay quốc tế Đà Nẵng mà còn đảm bảo khớp nối đồng bộ các quy hoạch, dự án, phát triển không gian đô thị hài hòa giữa hiện trạng và khu vực đề xuất xây dựng mới; cân đối lợi ích kinh tế của cộng đồng với các đơn vị, tổ chức có liên quan. "Quy hoạch và xây dựng hầm chui xuyên qua sân bay là nội dung nằm trong Quyết định điều chỉnh quy hoạch chung TP Đà Nẵng đến năm 2030, tầm nhìn đến năm 2045. Bộ Giao thông Vận tải đã ủng hộ, là tiền đề để thực hiện dù ý tưởng này đã được nhiều người đề xuất từ hơn chục năm trước", ông Huy nói. Tuy nhiên, quỹ đất ở tại đô thị, đất công trình dịch vụ - công cộng, đất cây xanh công cộng và đất hạ tầng kỹ thuật đô thị không còn nhiều do hầu hết đã có dân cư sinh sống, không có đất làm khu đô thị sân bay mới. Vì thế, ông Huy cho rằng không có nhiều đột phá khi quy hoạch phân khu này. Theo lộ trình, đồ án sẽ được lấy ý kiến các quận huyện. Hội Liên hiệp khoa học kỹ thuật thành phố tổ chức hội nghị lấy ý kiến chuyên gia, tổ chức hội thảo phản biện trước khi trình đồ án tới UBND TP Đà Nẵng để thẩm định và phê duyệt. Theo Quyết định điều chỉnh quy hoạch chung TP Đà Nẵng đến năm 2030, tầm nhìn đến năm 2045, toàn thành phố tổ chức thành 12 phân khu. Ngoài phân khu sân bay, còn có các phân khu ven sông Hàn và bờ đông; phân khu ven vịnh Đà Nẵng; phân khu cảng biển Liên Chiểu; phân khu công nghệ cao..."""
# kw_model = KeyBERT()
# keywords = kw_model.extract_keywords(doc)
# print(keywords)


from rake_nltk import Rake
import nltk
nltk.download('stopwords')
nltk.download('punkt')
r = Rake()
my_text = "When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him  seriously."
r.extract_keywords_from_text(doc)
keywordList           = []
rankedList            = r.get_ranked_phrases_with_scores()
for keyword in rankedList:
  keyword_updated       = keyword[1].split()
  keyword_updated_string    = " ".join(keyword_updated[:2])
  keywordList.append(keyword_updated_string)
print(keywordList)
