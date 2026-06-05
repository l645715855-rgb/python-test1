# class Animal:
#     def __init__(self,name):
#         self.name = name 

#     def speak(self):
#         print(f"{self.name}发出声音")

# class Dog(Animal):
#     pass

# #最基本的继承
# dog = Dog("小梁")
# dog.speak()

# #方法重写（Override）
# class Dog1(Animal):
#     def speak(self):
#         print(f"{self.name}汪汪叫了两声")
# dog = Dog1("小梁")
# dog.speak()

# #super()调用父类方法
# class Dog2(Animal):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age = age 

#     def speak(self):
#         super().speak()
#         print(f"{self.name}汪了三声")

# dog = Dog2("小林",10)
# dog.speak()


# #多态（Polymorphism）不同的子类，调用同一个方法，表现不同：
# class Cat(Animal):
#     def speak(self):
#         print(f"{self.name}喵喵喵")

# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name}汪汪汪")

# animal = [Dog("小黄"),Cat("小红")]
# for i in animal:
#     i.speak()



#day5.py —— OO版通讯录

class Contact:
    """单个联系人"""
    
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
        self.type = 0

    def show(self):
        """返回联系人信息"""
        return f"{self.name}:{self.phone}"
    
    def add_points(self):
        pass
    

class VIPContact(Contact):
    def __init__(self, name, phone):
        super().__init__(name, phone)
        self.points = 0
        self.type = 1

    def show(self):
        """返回联系人信息"""
        return f"{self.name}:{self.phone}--积分：{self.points}"
    
    def add_points(self):
        self.points = self.points+1



    
class AddressBook:
    """通讯录（管理多个联系人）"""
    version = "1.0" #类属性，所有通讯录共享版本号

    def __init__(self):
        self.contacts = []
    
    def add(self,name,phone,is_vip = False):
        """添加联系人"""
        if is_vip == True:
            c = VIPContact(name,phone)
            self.contacts.append(c)
            print("添加成功为VIP用户")
        else :
            c = Contact(name,phone)
            self.contacts.append(c)
            print("添加成功为普通用户")

    def find(self,name):
        """查找联系人"""
        for c in self.contacts:
            if c.name == name:
                return c
        return None

    def query(self,name):
        """查询联系人"""
        c = self.find(name)
        if c:
            print(c.show())
        else:
            print("查无此人")

    def delete(self,name):
        """删除联系人"""
        c =self.find(name)
        if c:
            self.contacts.remove(c)
            print("删除成功")
        else:
            print("查无此人")

    # def delete(self, name):
    # for i, c in enumerate(self.contacts):   ###enumerate 告诉你i是号码牌，c是对象本身
    #     if c.name == name:
    #         self.contacts.pop(i)  # pop 接收位置 i
    #         print("✅ 删除成功")
    #         return
    # print("❌ 查无此人")

    def show_all(self):
        """显示所有联系人"""
        if not self.contacts:
            print("通讯录为空")
            return
        
        print("\n --- 所有联系人 ---")
        for c in self.contacts:
            print(c.show())

    def add_points(self,name):
        c = self.find(name)
        if c:
            c.add_points()
            if c.type == 1:
                print(f"给{name}加1分，当前积分{c.points}")
            if c.type == 0:
                print("普通用户没有积分")
        else:
            print("查无此人")            

        

    @classmethod
    def show_version(cls):
        """类方法：显示版本"""
        print(f"通讯录版本：{cls.version}")


    @staticmethod
    def is_valid_phone(phone):
        """静态方法：验证手机号格式"""
        return len(phone) == 11 and phone.isdigit()
    










def main():
    book = AddressBook()# 创建一本通讯录
    AddressBook.show_version()# 调用类方法

    while True:
        print("\n ========= 00版通讯录=====")
        print("1. 添加  2. 查询  3. 删除  4. 显示全部 5.加积分 6. 退出")
        choice = input("请选择：")

        if choice == "1":
            name = input("姓名：")
            
            vip_flag = None
            while True:
                is_vip = input("是不是VIP(y/n)")
                if is_vip == "y":
                    vip_flag = True
                    break
                elif is_vip == "n":
                    vip_flag = False
                    break
                else :
                    print("请重新输入")
            while True:
                phone = input("电话：")
                if AddressBook.is_valid_phone(phone):
                    book.add(name,phone,vip_flag)
                    break;
                else:
                    print("手机号格式不对，需要11位数字")
                    continue
            

        elif choice == "2":
            name = input("姓名：")
            book.query(name)
        elif choice == "3":
            book.delete(input("姓名："))
        elif choice == "4":
            book.show_all()
        elif choice == "5":
            book.add_points(input("姓名："))
        
        elif choice == "6":
            print("再见！")
            break
        else:
            print("无效选择")

if __name__ == "__main__":
    main()