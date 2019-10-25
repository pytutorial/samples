"""
Chương trình đếm số lần xuất hiện các từ trong một câu
"""

text = 'Một năm có mười hai tháng, tháng hai có hai mươi tám ngày, các tháng còn lại có ba mươi hoặc ba mươi mốt ngày.'

text = text.lower()
for c in ['.', ',' , ':']:
    text = text.replace(c, ' ')

words_count = {}

for word in text.split():
    words_count[word] = words_count.get(word, 0) + 1

result = []
for (word, count) in words_count.items():
    result.append((count, word))

result = sorted(result, reverse=True)

for (count, word) in result:
    print(word , ' : ', count)

