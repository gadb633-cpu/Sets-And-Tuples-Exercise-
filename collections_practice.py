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

