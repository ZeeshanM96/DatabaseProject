import mysql.connector

mydb = mysql.connector.connect(host="localhost", username="ht22_2_group_42", passwd="pwd_42", database="ht22_2_project_group_42")

mycursor = mydb.cursor()

DeptID = input('Enter the Deptartment ID : ')
mycursor.execute("SELECT MAX(DepartmentID) FROM tbl_department")

for i in mycursor:
    Max_DeptID = i[0]


if int(DeptID) > int(Max_DeptID):
    print("Invalid Deptartment ID, Try Again.")
else:
    mycursor.execute("SELECT COUNT(*) FROM tbl_department WHERE ManagedBy = " + DeptID + ";")
    data = mycursor.fetchall()

    if data[0][0] == 0:
        mycursor.execute("SELECT ProductID, ProductTitle, (RetailPriceWithoutTax - (RetailPriceWithoutTax * (DiscountPercentage/100))) AS RetailPriceAfterDiscount FROM tbl_product WHERE DepartmentID =" + DeptID + ";")
    else:
        mycursor.execute("SELECT DepartmentTitle, DepartmentDescription FROM tbl_department where ManagedBy = " + DeptID + ";")

    for i in mycursor.fetchall():
        print(i)

mydb.commit()
mydb.close()


