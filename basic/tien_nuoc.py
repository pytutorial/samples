x = float(input('Tổng số mét khối nước tiêu thụ trong tháng: '))

bang_gia = [
    {'don_gia' : 5973, 'muc_tieu_thu' : 10 },
    {'don_gia' : 7052, 'muc_tieu_thu' : 20 },
    {'don_gia' : 8669, 'muc_tieu_thu' : 30 },
    {'don_gia' : 15929 }
]

so_tien = 0
i = 0
print('Số m3 \t Đơn giá \t Tiền')

so_met_da_tinh = 0

while so_met_da_tinh < x:
    don_gia = bang_gia[i]['don_gia']
    muc_tieu_thu = bang_gia[i].get('muc_tieu_thu')
    
    if muc_tieu_thu != None and muc_tieu_thu < x:
        khoi_luong = muc_tieu_thu - so_met_da_tinh
    else:
        khoi_luong = x - so_met_da_tinh
            
    print(f'{khoi_luong} \t {don_gia} \t {khoi_luong * don_gia}')
    
    so_tien += don_gia * khoi_luong    
    so_met_da_tinh += khoi_luong
    i += 1

print('Tổng tiền : ', so_tien)

    


