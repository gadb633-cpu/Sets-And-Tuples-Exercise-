# part 1
# 1
tags = {"python","bash","git","python"}
print(tags)
print(len(tags))
# 2
tags.add("linux")
print(tags)
# 3
tags.discard("bash")
print(tags)
tags.discard("banana")
print(tags)
# 4
a = {1,2,3}
b = {3,4,5}
print(a | b)
print(a & b)
diff_a = a - b
diff_b = b - a
print(diff_a)
print(diff_b)
# 5
print("git" in tags)
# 6
point = (10,20)
print(point)
print(point[0],point[1])
# 7
# point[0]= 99
# print(point)
# typeerror
# 8
rgb = (255,128,0)
r = rgb[0]
g = rgb[1]
b = rgb[2]
print(r)
print(g)
print(b)
# 9
coords = (1,2,3,2,1)
coords2 = coords.count(2)
print(coords2)
print(coords[0:3])
