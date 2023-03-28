
###########################################
####        ฟังก์ชั่นเพิ่มของเข้าสต๊อก        ####
##########################################

def add_to_database_stock(how_many_items):
    stock_database=open("database_for_stock.txt", "a")
    for count in range(0,how_many_items):
        password_items=check_repeat_key()
        items_name=str(input("กรุณากรอกชื่อสินค้า : "))
        count_items=str(input("กรุณากรอกจำนวนสินค้า : "))
        price_items=str(input("กรุณากรอกราคาสินค้า : "))
        if password_items.isdigit() == True and items_name.isalpha() == True and count_items.isdigit() == True and price_items.isdigit() == True :
            print("เพิ่มสินค้าเสร็จสิ้น")
            stock_database.write(password_items+","+count_items+","+price_items+","+items_name+"\n")
        else :
            print("เพิ่มสินค้าไม่สำเร็จ")
    stock_database.close()

##########################################
####        ฟังก์ชั่นเช็คของในสต๊อก        ####
#########################################

def check_database_stock():
    read_database_stock=open("database_for_stock.txt","r")
    while True:
        check_stock=read_database_stock.readline()
        if check_stock=="":
            break
        check_second=check_stock.split(",")
        x_check=len(check_second[3])
        free_space=""
        for x in range(0,x_check-1):
            free_space+=check_second[3][x]
        check_second[3]=free_space
        Dic_for_stock1={check_second[0]:[check_second[1],check_second[3]]}
        print(Dic_for_stock1)
    read_database_stock.close()

################################################
####        ฟังก์ชั่นเช็คการซ้ำของรหัสสินค้า        ####
###############################################

def check_repeat_key():
    read_database_stock=open("database_for_stock.txt","r")
    Dict_for_check_repeat={}
    for n in read_database_stock:
        split_data=n.split(",")
        name_split=split_data[3].split("\n")
        Dict_for_check_repeat[split_data[0]]=split_data[1],split_data[2],name_split[0]
    print("คำเตือน! กรุณากรอกรหัสสินค้าที่ไม่ซ้ำกับรหัสสินค้าที่เคยมีอยู่แล้ว")
    while True:
        password_items=str(input("กรุณากรอกรหัสสินค้า : "))
        if password_items in Dict_for_check_repeat.keys():
            print("กรุณาตรวจสอบรหัสสินค้าอีกรอบ")
        else:
            return password_items

#########################################
####        ฟังก์ชั่นลบข้อมูลสินค้า        ####
########################################

def delete_password_items():
    list_for_update = []
    password_list = []
    read_database = open("database_for_stock.txt", "r")
    for line in read_database:
        list_for_update.append(line)
    read_database.close()
    how_many_delete = int(input("ต้องการลบข้อมูลสินค้ากี่ตัว : "))
    for n in range(0,how_many_delete):
        password_list.append(str(input("รหัสสินค้าที่ต้องการลบข้อมูล : ")))
    data_index=0
    max_len=len(list_for_update)
    while data_index!=max_len:
        id_key,count,price,name=list_for_update[data_index].split(',')
        if id_key in password_list:
            list_for_update.remove(list_for_update[data_index])
            data_index=0
            max_len-=1
        data_index+=1
    write_database = open("database_for_stock.txt", "w")
    for line in list_for_update:
        write_database.write(line)
    write_database.close()

    
    
    
