# ジェネレータ関数
def generator(max):
    print('ジェネレータ作成')
    for n in range(max):
        try:
            x = yield n 
            print('x = {}'. format(x))
            print('yeild実行')
        except ValueError as e:
            print('throwを実行しました')

gen = generator(10)
next(gen)
gen.send(100)
# 例外をスローする
#gen.throw(ValueError('Invaild Error'))
# クローズ
gen.close()

# クローズしているので、ジェネレータ関数は実行されない
next(gen)