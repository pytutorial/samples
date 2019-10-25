points = ['A', 'B', 'C', 'D']

distances = { 
           ('A', 'B') : 10,
           ('B', 'C') : 5,
           #('C', 'B') : 5,  # TODO : Bỏ comment dòng này và sửa chương trình để chạy đúng
           ('B', 'D') : 7,
           ('C', 'D') : 5
        }        

def find_shortest_path(p1, p2):
    if p1 == p2:                                                   # Nếu điểm đầu và điểm cuối trùng nhau
        return (0, p1)                                             # Đường đi ngắn nhất có độ dài bằng 0 và gồm chính điểm đó
    
    paths = []                                                     # Danh sách tất cả các đường có thể đi từ p1 đến p2
    
    for p in points:
        if (p1, p) in distances:                                   # Duyệt qua các địa điểm mà từ p1 có thể đi tới
            route_length, route = find_shortest_path(p, p2)        # Tìm đường ngắn nhất từ p đến p2
                        
            if route_length >= 0 :                                 # Nếu tồn tại đường đi từ p đến p2
                route_length += distances[(p1, p)]
                route = p1 + '->' + route
                paths.append((route_length, route))                # Thêm lộ trình (p1->p->p2) vào danh sách đường có thể đi
    
    if len(paths) > 0:                                             # Nếu có ít nhất 1 đường đi từ p1 đến p2
        paths = sorted(paths)                                      # Sắp xếp các con đường theo độ dài tăng dần
        return paths[0]                                            # Đường đi ngắn nhất là phần tử đầu của danh sách sau sắp xếp
    
    else:
        return (-1, '')                                            # Không tồn tại con đường nào để đi từ p1 đến p2
            
print(find_shortest_path('A', 'D'))
