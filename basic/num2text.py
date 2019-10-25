"""
Chương trình chuyển một số có 3 chữ số thành phát âm tiếng Việt
 - Đầu vào : số tự nhiên trong phạm vi từ 0 đến 999
 - Đầu ra : phát âm tiếng Việt của số đó
"""

bangso = ['không', 'một', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín']

def convert2digits(x):
    if x < 10:
        return bangso[x]

    chuc = x // 10
    donvi = x % 10
    
    text = (bangso[chuc] + ' mươi') if chuc > 1 else 'mười'    

    if donvi > 0:
        text += ' '

        if donvi == 5:
            text += 'lăm'

        elif donvi == 1 and chuc > 1:
            text += 'mốt'

        else:
            text += bangso[donvi]

    return text

def convert3digits(x):
    if x < 100:
        return convert2digits(x)

    tram = x // 100
    chuc = (x//10) % 10
    donvi = x % 10
 
    text = bangso[tram] + ' trăm'

    if chuc > 0:
        text += ' ' + convert2digits(x%100)

    elif donvi > 0:
        text += ' lẻ ' + bangso[donvi]

    return text

print(convert3digits(105))
