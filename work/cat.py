from work.animal import Animal

'''
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】
Catch mice
'''
class Cat(Animal):

    def __init__(self,name,color,age,gender):
        self.hair="短毛"
        super().__init__(name,color,age,gender)

    def catchMice(self):
         print(f"{self.name}会捉老鼠")

    def call(self):
         print("喵喵叫")


if __name__ =='__main__':
    mm=Cat("喵喵",'白色',1,'女')
    print(mm.name)
    print(mm.color)
    print(mm.age)
    print(mm.hair)
    print(mm.gender)
    mm.call()
    mm.catchMice()