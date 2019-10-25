block_points = set()
N = 10

with open('grid.txt') as f:
    line = f.readline()
    point1, point2 = line.strip().split('|')
    x1, y1 = point1.split(',')
    x2, y2 = point2.split(',')
    
    start_point = (int(x1), int(y1))
    end_point = (int(x2), int(y2))
    
    for line in f:
        x, y = line.strip().split(',')
        block_points.add((int(x), int(y)))
        
def find_shortest_path(point1, point2):    
    if point1 == point2:
        return [point1]
    
    block_points.add(point1)
    
    next_paths = []
    
    for i, j in [(-1, 0), (1, 0), (0,-1), (0,1)]:
        x, y = point1[0] + i, point1[1] + j
        
        if x >= 0 and x < N and y >= 0 and y <= N and (x,y) not in block_points:
            next_path = find_shortest_path((x,y), end_point)
            
            if next_path:
                next_paths.append(next_path)
        
    if len(next_paths) > 0:
            
        next_paths = sorted(next_paths, key=lambda x : len(x))
            
        block_points.remove(point1)
        
        return [point1] + next_paths[0]
    
path = find_shortest_path(start_point, end_point)
print(path)   
