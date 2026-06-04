# day4.py —— 模块化通讯录

def show_menu():
    print("\n===== 通讯录 =====")
    print("1. 查询联系人")
    print("2. 添加联系人")
    print("3. 删除联系人")
    print("4. 显示所有")
    print("5. 退出")


def query(contact):
    name = input("请输入名字")
    if name in contact:
        print(f'他的电话是{contact[name]}')
    else:
        print('查无此人')

def add(contact):
    name = input("请输入名字")
    phone = input("请输入电话")
    contact[name] = phone
    print("添加成功")

def delete(contact):
    name = input("请输入名字")
    del contact[name]
    print("删除成功")

def show_all(contact):
    if not contact :
        print('没有数据')
    else:
        for name,phone in contact.items():
            print(name,":",phone)

def main():
    contact={'小林':122,'小黄':110,'小绿':119}



    while True:
        show_menu()
        choice = input("请输入数字")
        if choice=="1":
            query(contact)
        elif choice == "2":
            add(contact)
        elif choice == "3":
            delete(contact)
        elif choice == "4":
            show_all(contact)
        elif choice == "5":
            print("欢迎下次使用")
            break
        else:
            print("请重新输入")

if __name__ == "__main__":
    main()