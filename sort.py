points = [[1, 80], [3, 250], [5, 150], [8, 220], [9, 90]]

x_coords = [x for x, y in points]
x_coords.sort()
#print(x_coords)
widest=0
for i in range(len(x_coords)-1):
    k=x_coords[i+1]-x_coords[i]
    if k>widest:
        widest=k
print(widest)