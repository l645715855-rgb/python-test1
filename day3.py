"""命令行通讯录"""
contact = {"小张":122,"小林":110,"小钟":119,"小汪":120}

while True:
    choice = input("\n1.查询 2.添加 3.删除 4.退出")

    if choice == "1":
        name =input("姓名：")
        if name in contact:
            print("电话是：",contact[name])
        else:
            print("查无此人")  
    elif choice == "2":
        name =input("姓名：")
        tem =input("电话：")
        contact[name] = tem
        print("添加成功")
    elif choice == "3" :
        name =input("姓名：")
        del contact[name]
        # contact.pop(name, None) 第二种删除方式
        print("删除成功")
    elif choice == "4":
        break
    else:
        print("请重新输入")