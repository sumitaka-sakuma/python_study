# ジェネレータ関数
def generator(max):
    print('ジェネレータ作成')
    for n in range(max):
        yield n 
        print('yeild実行')

gen = generator(10)

for x in gen:
    print('x = {}'. format(x))