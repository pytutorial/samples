"""
Chương trình chuyển phát âm tiếng Việt của một số 3 chữ số sang giá trị số
 - Đầu vào : phát âm tiếng Việt của một số trong phạm vi 1 đến 999
 - Đầu ra : giá trị của số
"""

bang_so1 = {'một' : 1, 'hai' : 2, 'ba' : 3, 'bốn' : 4, 'năm' : 5, 'sáu' : 6, 'bảy' : 7, 'tám' : 8, 'chín' : 9, 'mười' : 10}
bang_so2 = {'một' : 1, 'hai' : 2, 'ba' : 3, 'bốn' : 4, 'lăm' : 5, 'sáu' : 6, 'bảy' : 7, 'tám' : 8, 'chín' : 9}
bang_so3 = {'mươi' : 0, 'mốt' : 1, 'hai' : 2, 'ba' : 3, 'bốn' : 4, 'tư' : 4, 'lăm' : 5, 'sáu' : 6, 'bảy' : 7, 'tám' : 8, 'chín' : 9}

def convert2digits(words):
    N = len(words)

    if N == 1:
        return bang_so1.get(words[0], -1)

    chuc, donvi = -1, -1

    if (N == 3 and words[1] == 'mươi') or N == 2:
        chuc = bang_so1.get(words[0], -1)
        donvi = bang_so3.get(words[-1], -1)

    if N == 2 and words[0] == 'mười':
        chuc = 1
        donvi = bang_so2.get(words[1], -1)

    if chuc >= 0 and donvi >= 0:
        return 10 * chuc + donvi
    
    return -1

def convert3digits(words):
    N = len(words)

    if N <= 1 or words[1] != 'trăm':
        return convert2digits(words)

    tram = bang_so1.get(words[0], -1)

    if N == 2 and tram >= 0:
        return 100*tram     
    
    if N == 4 and words[2] == 'lẻ':
        donvi = bang_so1.get(words[3], -1)

        if tram >= 0 and donvi >= 0:
            return 100*tram + donvi

    x = convert2digits(words[2:])

    if tram >= 0 and x >= 0:
        return 100*tram + x

    return -1        

def text2num(text):    
    return convert3digits(text.lower().split())

print(text2num('tám trăm năm mươi tư'))
