
car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2021}
temp_car = {'country': 'Japan', 'prefecture': 'Aichi', 'model': 'カローラ'}

# 追加、更新
car.update(temp_car)
print(car)

value = car.popitem()
print(car)
print(value)

# keyから値を取得
value = car.pop('model')
print(car)
print(value)

# clear
car.clear()
# del
del car