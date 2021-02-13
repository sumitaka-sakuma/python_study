
fruit = ('apple', 'banana', 'melon')
print(fruit)
print(fruit[1])

#エラー
#fruit[1] = 'grape'

fruit = fruit + ('grape',)
print(fruit)

# リストをタプルに変換
list_fruit = ['apple', 'banana']
fruit = tuple(list_fruit)
print(fruit)

# 数の取得
print(fruit.count('apple'))
# 何番目の要素か
print(fruit.index('banana'))

# キー
pos = (135, 35)
countries = {pos: 'Japan'}
# キーから値を取得
print(countries.get((135, 35)))
