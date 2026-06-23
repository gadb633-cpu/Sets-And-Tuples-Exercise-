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
# 10
list_1 = [1,2,3]
set_1 = {1,2,3}
tuple_1 = (1,2,3)
print(list)
print(set)
print(tuple)
# part 2
# 1
a = {1,2,3}
b = {3,4,5}
print(a.issubset(b))
print(b.issubset(a))
print(a.issuperset(b))
print(b.issuperset(a))
# 2
pairs = [(1,"a"),(2,"b"),(3,"c")]
print(pairs[1][1])
# 3
convert_list = [1,2,3,2,3,1]
convert_set = set(convert_list)
print(convert_set)
convert_set_to_list = list(convert_set)
print(convert_set_to_list)
# 4
set_a = {1,2,3,4}
set_b = {3,4,5,6}
result = set_a.symmetric_difference(set_b)
print(result)
# 5
list_g = [1,2,3]
set_g = {4,5,6}
tuple_g = (7,8,9)
# set_g.add(list_g)
# print(set_g)
#TypeError
set_g.add(tuple_g)
print(set_g)


