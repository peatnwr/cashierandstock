####################################
####        ฟังก์ชั่นเงินทอน        ####
###################################

def changemoney(pay,sum_price):
    change=pay-sum_price
    print("\t","เงินทอน : ",change," บาท")

#############################################
####        ฟังก์ชั่นจำนวนธนบัตรที่ทอน        ####
############################################

def banknote(pay,sum_price):
    bn1000=bn500=bn100=bn50=bn20=bn10=bn5=bn1=bn050=bn025=0
    putprice=pay-sum_price
    while True :
        if putprice>=1000:
            putprice-=1000
            bn1000+=1
        elif putprice>=500:
            putprice-=500
            bn500+=1
        elif putprice>=100:
            putprice-=100
            bn100+=1
        elif putprice>=50:
            putprice-=50
            bn50+=1
        elif putprice>=20:
            putprice-=20
            bn20+=1
        elif putprice>=10:
            putprice-=10
            bn10+=1
        elif putprice>=5:
            putprice-=5
            bn5+=1
        elif putprice>=1:
            putprice-=1
            bn1+=1
        elif putprice>=0.50:
            putprice-=0.50
            bn050+=1
        elif putprice>=0.25:
            putprice-=0.25
            bn025+=1
        else:
            print("\t","ธนบัตร 1000 บาท :",bn1000," ใบ")
            print("\t","ธนบัตร 500 บาท : ",bn500," ใบ")
            print("\t","ธนบัตร 100 บาท :",bn100," ใบ")
            print("\t","ธนบัตร 50 บาท :",bn50," ใบ")
            print("\t","ธนบัตร 20 บาท : ",bn20," ใบ")
            print("\t","เหรียญ 10 บาท : ",bn10," ใบ")
            print("\t","เหรียญ 5 บาท : ",bn5," เหรียญ")
            print("\t","เหรียญ 1 บาท : ",bn1," เหรียญ")
            print("\t","เหรียญ 50 สตางค์ : ",bn050," เหรียญ")
            print("\t","เหรียญ 25 สตางค์ : ",bn025," เหรียญ")
            break

###########################################################
####        ฟังก์ชั่นเปลี่ยนจำนวนสินค้าหลังจากที่มีลูกค้าซื้อ        ####
###########################################################

def change_count_data(password_items,count_items):
    copy_text=""
    read_data=open("database_for_stock.txt","r")
    for line in read_data:
        password,count,price,name=line.split(",")
        if password==password_items:
            true_count=int(count)-int(count_items)
            copy_text+=str(password)+","+str(true_count)+","+str(price)+","+str(name)
        else:
            copy_text+=str(password)+","+str(count)+","+str(price)+","+str(name)
    read_data.close()
    write_data=open("database_for_stock.txt","w")
    write_data.write(copy_text)
    write_data.close()

########################################
####        ฟังก์ชั่นแคชเชียร์หลัก        ####
########################################

def cashier():
    sum_price=0
    Dict_for_update={}
    dict_for_check={}
    read_database=open("database_for_stock.txt","r")
    for line in read_database:
        split_data=line.split(",")
        dict_for_check[split_data[0]]=split_data[1],split_data[2],split_data[3]
    read_database.close()
    try:
        while True:
            password_items=str(input("รหัสสินค้า : "))
            if password_items=="":
                break
            elif not password_items in dict_for_check.keys():
                print("ไม่มีรหัสสินค้านี้อยู่")
                continue
            count_items=str(input("จำนวนสินค้าที่ลูกค้าซื้อ : "))
            if int(count_items)<=0:
                print("จำนวนสินค้าไม่ถูกต้อง")
                continue
            elif count_items=="":
                break
            read_data=open("database_for_stock.txt","r")
            for line in read_data:
                password,count,price,name=line.split(",")
                if password==password_items:
                    if int(count)>0:
                        summary=int(price)*int(count_items)
                        sum_price+=summary
                        Dict_for_update[password_items]=count_items
                    else:
                        print("สินค้าหมดชั่วคราว")
                        continue
            read_data.close()
            print("ราคา : ",summary)
            print("ราคาสุทธิ : ",sum_price)
        while True:
            pay=int(input("เงินที่ลูกค้าจ่ายมา : "))
            if pay<sum_price:
                print("Error :","คุณกรอกจำนวนเงินที่ลูกค้าจ่ายมาน้อยกว่าราคารวม กรุณาทำรายการใหม่")
                continue
            else:
                for n in Dict_for_update:
                    change_count_data(n,Dict_for_update[n])
                changemoney(pay,sum_price)
                banknote(pay,sum_price)
                break
    except:
        print("กรุณาทำรายการใหม่อีกรอบ")
        
        
        
            

    