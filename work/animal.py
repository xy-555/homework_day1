#创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
class Animal:
    name="牛妞"
    color="brown"
    age=2
    gender='female'

#实例化的时候就会执行
    def __init__(self,name,color,age,gender):
        self.name=name
        self.color=color
        self.age=age
        self.gender=gender

    @classmethod
    def call(self):
        print("牛年到，祝大家牛气冲天、牛运亨通、牛财旺盛、牛福永恒")

    def run(self):
        print("running:"+"牛年旺")

#实例化这个类
# nn=Animal('牛妞','褐色',2,'女')
# print(f"大家好，我的名字是：{nn.name},颜色是：{nn.color},年龄是：{nn.age}岁，性别是：{nn.gender}。祝大家牛年大吉!")
# nn.call()
# nn.run()
# mm=Animal('喵喵','白色',1,'女')
# print(f"大家好，我的名字是：{mm.name},颜色是：{mm.color},年龄是：{mm.age}岁，性别是：{mm.gender}。祝大家牛年无忧无烦恼!")

#类直接访问方法，需要添加@classmethod装饰器变成类方法
# Animal.call()

if __name__ == '__main__':
    nn=Animal('牛妞','褐色',2,'女')
    print(f"大家好，我的名字是：{nn.name},颜色是：{nn.color},年龄是：{nn.age}岁，性别是：{nn.gender}。祝大家牛年大吉!")

    mm = Animal('喵喵', '白色', 1, '女')
    print(f"大家好，我的名字是：{mm.name},颜色是：{mm.color},年龄是：{mm.age}岁，性别是：{mm.gender}。祝大家牛年无忧无烦恼!")

