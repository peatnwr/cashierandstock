###########################################################################################
##########                    Cashier and Stock [Version 1.0]                    ##########
##########                         Updated on 03/11/2562                         ##########
###########################################################################################

import os
from func_cashier import cashier
from func_database_stock import add_to_database_stock,check_database_stock,delete_password_items
while True:
    os.system("cls")
    print("ตำแหน่งหน้าที่การงาน")
    print("1.)Cashier")
    print("2.)Stock checker")
    print("3.)Exit Program")
    status=input("กรุณากรอกตำแหน่งงานของคุณ : ")
    status.lower()
    if status!="cash" and status!="cashier" and status!="stock" and status!="stocker" and status!="stock checker" and status!="1" and status!="2" and status!="3":
        print("กรุณากรอกตำแหน่งงานของท่านให้ถูกต้อง")
    elif status=="3":
        os.system("cls")
        print("ขอบคุณที่เข้ามาใช้บริการโปรแกรมของพวกเรา")
        break
    while status=="cashier" or status=="cash" or status=="1":
        os.system("cls")
        cashier()
        work_question=input("ต้องการทำงานต่อไหม (yes or no) : ")
        work_question.lower()
        if work_question!="yes" and work_question!="no":
            print("กรุณากรอกให้ถูกต้อง")
            break
        else:
            if work_question=="yes":
                pass
            else:
                break
    while status=="stock checker" or status=="stock" or status=="stocker" or status=="2":
        os.system("cls")
        question_ac=input("คุณต้องการจะเพิ่มสินค้าหรือลบสินค้าและเช็คสินค้าภายในร้าน (add or delete or check) : ")
        question_ac.lower()
        if question_ac!="add" and question_ac!="check" and question_ac!="delete":
            print("กรุณากรอกข้อมูลให้ถูกต้อง")
            continue
        else:
            if question_ac=="add":
                os.system("cls")
                how_many_items=int(input("คุณต้องการเพิ่มสินค้ากี่ชนิด : "))
                add_to_database_stock(how_many_items)
            elif question_ac=="check":
                os.system("cls")
                check_database_stock()
            elif question_ac=="delete":
                check_database_stock()
                delete_password_items()
        print("หากกรอกคำถามข้างต้นไม่ถูกต้อง คุณจะไม่สามารถออกจากระบบปฏิบัติการ Stock Checker ได้")
        work_question=input("คุณต้องการทำงานต่อไหม (yes or no) : ")
        work_question.lower()
        if work_question!="yes" and work_question!="no":
            print("กรุณากรอกให้ถูกต้อง")
            continue
        else:
            if work_question=="yes":
                pass
            else:
                break
