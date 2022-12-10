##Connecting to the database
import mysql.connector

mydb = mysql.connector.connect(host="localhost", username="ht22_2_group_42", passwd="pwd_42", database="ht22_2_project_group_42")

mycursor = mydb.cursor()

ProdID = input('Enter the Product ID to search the discount : ')
mycursor.execute("SELECT MAX(ProductID) FROM tbl_product")

for i in mycursor:
    Max_ProdID = i[0]

if int(ProdID) > int(Max_ProdID):
    print("Invalid Product ID, Try Again.")
else:
    mycursor.execute("SELECT DiscountPercentage FROM tbl_product WHERE ProductID = " + ProdID + ";")
    for i in mycursor:
        if i[0] == 0:
            print("There's no discount on the product at the moment.")

            reply = input('DO you want to ADD the discount on this product ? Y/N : ')

            if reply == 'Y' or reply == 'y':
                discount_price = input('Provide the discount price in numbers : ')
                mycursor.execute(
                    "UPDATE tbl_product SET DiscountPercentage = " + discount_price + " WHERE ProductID =" + ProdID + ";")
                print("Price Updated!.")
                mycursor.execute("Select DiscountPercentage FROM tbl_product where ProductID = " + ProdID + ";")
                for i in mycursor:
                    print(str(i[0]))
            elif reply == 'N' or reply == 'n':
                print("User don't wish to update the discount price of the product.")
            else:
                print("Invalid Input.")
        else:
            print(str(i[0]) + "%")
            reply = input('Do you want to update the discount on this product ? Y/N : ')
            if reply == 'Y' or reply == 'y':
                discount_price = input('Provide the discount price in numbers : ')
                mycursor.execute("UPDATE tbl_product SET DiscountPercentage = " + discount_price + " WHERE ProductID =" + ProdID + ";")
                print("Price Updated!.")
                mycursor.execute("Select DiscountPercentage FROM tbl_product WHERE ProductID = " + ProdID + ";")
                for i in mycursor:
                    print(str(i[0]))
            elif reply == 'N' or reply == 'n':
                print("User don't wish to update the discount price of the product.")
            else:
                print("Invalid Input.")

mydb.commit()
mydb.close()