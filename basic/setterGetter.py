# setter getter
class Human:

    def __init__ (self, name, age):
        self.__name = name
        self.age = age

    @property
    def name(self): # getter
        print('getter nameが呼ばれました')
        return self.__name
        
    @property
    def age(self): #getter
        print('getter ageが呼ばれました')
        return self.__age
    
    @name.setter
    def name(self, name):
        print('setter nameが呼ばれました')
        self.__name = name

    @age.setter
    def age(self, age):
        print('setter ageが呼ばれました')
        if age < 0:
            print('0以上の年齢を設定してください')
            return
        self.__age = age

# 名前と年齢を格納
human = Human('sakuma', 27)
# 値を取得
print(human.name)

# 0未満の値の時は、格納せずに処理を返す
#human.age = -100
