#  Cho 2 văn bản. Viết hàm tìm danh sách từ chung nhau của 2 văn bản

def get_word_set(st):
    return set(st.split())
    
def get_common_words(st1, st2):
    words1 = get_word_set(st1)
    words2 = get_word_set(st2)
    return words1.intersection(words2)
    
st1 = "nhiệt độ ở thủ đô Hà Nội ngày mai là 20-25 độ C"
st2 = "nhiệt độ ở TP.HCM hôm này là 30-35 độ C"

common_words = get_common_words(st1, st2)
print(common_words)