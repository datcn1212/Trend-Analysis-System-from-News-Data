dict = {
    'Đời sống': 'doi_song',
    'Du lịch': 'du_lich',
    'Giải trí': 'giai_tri',
    'Giáo dục': 'giao_duc',
    'Khoa học': 'khoa_hoc',
    'Kinh doanh': 'kinh_doanh',
    'Pháp luật': 'phap_luat',
    'Sức khỏe': 'suc_khoe',
    'Thế giới': 'the_gioi',
    'Thể thao': 'the_thao',
    'Thời sự': 'thoi_su',
    'Bất động sản': 'bat_dong_san',
    'Số hóa': 'so-hoa'
}

dict2 = {
    'doi_song': 'Đời sống',
    'du_lich': 'Du lịch',
    'giai_tri': 'Giải trí',
    'giao_duc': 'Giáo dục',
    'khoa_hoc': 'Khoa học',
    'kinh_doanh': 'Kinh doanh',
    'phap_luat': 'Pháp luật',
    'suc_khoe': 'Sức khỏe',
    'the_gioi': 'Thế giới',
    'the_thao': 'Thể thao',
    'thoi_su': 'Thời sự',
    'other_topic': 'Khác'
}

def topic_vi_to_en(vi_topic):
    if vi_topic in dict.keys():
        return dict[vi_topic]
    return 'other_topic'

def topic_en_to_vi(en_topic):
    return dict2[en_topic]