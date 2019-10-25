"""
Chương trình tính điểm trung bình của một lớp học
 - Đầu vào : File csv, mỗi hàng chứa thông tin điểm của một học sinh
   Mỗi hàng có các cột sau, ngăn cách bởi dầu phảy :
     + Họ tên
     + Điểm hệ số 1
     + Điểm hệ số 2
     + Điểm hệ số 3
  - Đầu ra: File csv, mỗi hàng giống như file csv đầu vào, nhưng có thêm cột điểm trung bình ở cuối
"""

ds_lop = []

fi = open('diem_trungbinh_input.csv', encoding='utf-8')
for line in fi:
    hoten, diemhs1, diemhs2, diemhs3 = line.split(',')
    diemhs1 = int(diemhs1)
    diemhs2 = int(diemhs2)
    diemhs3 = int(diemhs3)
    diem_tb = (diemhs1 + 2*diemhs2 + 3*diemhs3) / 6.0
    ds_lop.append((hoten, diemhs1, diemhs2, diemhs3, diem_tb))

fi.close()

fo = open('diem_trungbinh_output.csv', 'wt', encoding='utf-8')
for hocsinh in ds_lop:
    hoten, diemhs1, diemhs2, diemhs3, diem_tb = hocsinh    
    line = '{}, {}, {}, {}, {: 1.1f}'.format(
    		hoten, diemhs1, diemhs2, diemhs3, diem_tb)
    
    fo.write(line + '\n')

fo.close()
