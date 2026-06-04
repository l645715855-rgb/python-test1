#day5.py —— OO版通讯录

class Contact:
    """单个联系人"""
    
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone

    def show(self):
        """返回联系人信息"""
        return f"{self.name}:{self.phone}"
    
class AddressBook:
    """通讯录（管理多个联系人）"""
    version = "1.0" #类属性，所有通讯录共享版本号

    def __init__(self):
        self.contacts = []
    
    def add(self,name,phone):
        """添加联系人"""
        c = Contact(name,phone)
        self.contacts.append(c)
        print("添加成功")

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
        print("1. 添加  2. 查询  3. 删除  4. 显示全部  5. 退出")
        choice = input("请选择：")

        if choice == "1":
            name = input("姓名：")
            phone = input("电话：")
            if AddressBook.is_valid_phone(phone):
                book.add(name,phone)
            else:
                print("手机号格式不对，需要11位数字")
        elif choice == "2":
            name = input("姓名：")
            book.query(name)
        elif choice == "3":
            book.delete(input("姓名："))
        elif choice == "4":
            book.show_all()
        elif choice == "5":
            print("再见！")
            break
        else:
            print("无效选择")

if __name__ == "__main__":
    main()