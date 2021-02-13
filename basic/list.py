# Initialize
list_a = [1,2,3,4,5,6,7,8,9,10]

# slice
list_b = list_a[1:10:3]
print(list_b)

# append
list_a.append('apple')
print(list_a)

# extend
list_a.extend(['banana', 'melon'])
print(list_a)

# Insert
list_a.insert(2, 'grape')
print(list_a)

# clear
#list_a.clear()
#print(list_a)

# remove
list_a.remove(10)
print(list_a)

# pop
value = list_a.pop()
print(list_a, value)

# count
print(list_a.count(1))

# index 
print(list_a.index(7))

# copy

# 参照渡しの場合
print(list_a)
list_b = list_a
list_b[0] = 'asdfg'
print(list_a)

# copyを使った場合
list_b = list_a.copy()
list_b[0] = 'qwert'
print(list_b)
print(list_a)