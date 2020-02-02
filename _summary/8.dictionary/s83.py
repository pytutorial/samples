# Cho một văn bản, in ra các từ trong văn bản kèm số lần xuất hiện của chúng theo thứ tự số lượng giảm dần

st = "một năm có ba trăm sáu mươi lăm hoặc ba trăm sáu mươi sáu ngày"

counts = {}

for word in st.split():
    counts[word] = counts.get(word, 0) + 1
    
items = sorted(counts.items(), key=lambda x: x[1], reverse=True)

for word, count in items:
    print(word, ':', count)