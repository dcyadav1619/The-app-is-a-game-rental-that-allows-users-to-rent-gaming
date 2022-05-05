import operations
import json
from json import JSONDecodeError

print("Welcome to Game Rental App")
while(1):
    print("Press: ")
    print("1. Register as Seller")
    print("2. Register as Gamer")
    print("3. Login as Seller")
    print("4. Login as Gamer")
    print("5. Exit")
    in1=int(input())
    if in1==1:
        print("Enter Email ID")
        Email_ID=input()
        print("Enter Username")
        Username=input()
        print("Enter Password")
        Password=input()
        print("Enter Contact Number")
        Contact_Number=input()
        try:
            f=open('Sellers.json','r')
            content=json.load(f)
            if Username in str(content):
                print("Username already exists !!")
                continue
        except JSONDecodeError:
            pass
        if "@admin.com" not in Email_ID or (len(Email_ID)*len(Username)*len(Password)*len(Contact_Number))==0 or len(str(Contact_Number))!=10 or len(Password)<=4:
            print("Please Enter Valid Data !!")
            continue
        else:
            operations.Register('seller','Gamers.json','Sellers.json',Email_ID,Username,Password,Contact_Number)
            print("Registered Successully as Seller")
            continue
    elif in1==2:
        print("Enter Email ID")
        Email_ID=input()
        print("Enter Username")
        Username=input()
        print("Enter Password")
        Password=input()
        print("Enter Contact Number")
        Contact_Number=input()
        if ".com" not in Email_ID or (len(Email_ID)*len(Username)*len(Password)*len(Contact_Number))==0 or len(Contact_Number)!=10 or len(Password)<=4:
            print("Please Enter Valid Data")
            continue
        else:
            operations.Register('gamer','Gamers.json','Sellers.json',Email_ID,Username,Password,Contact_Number)
            print("Registered Successully as Gamer")
            continue
    elif in1==3:
        print("Enter Username")
        Username=input()
        print("Enter Password")
        Password=input()
        ch=operations.Login('seller','Gamers.json','Sellers.json',Username,Password)
        if ch==True:
            f=open('Sellers.json','r')
            content=json.load(f)
            user_details=[]
            for i in range(len(content)):
                if content[i]["Username"]==Username:
                    user_details=content[i]
                    break
            print("Welcome "+str(Username))
            while(1):
                print("Press: ")
                print("1. Create Product")
                print("2. Update Product")
                print("3. View all created Products")
                print("4. View Product Details by ID")
                print("5. View User Profile")
                print("6. Logout")
                in2=int(input())
                if in2==1:
                    Product_id=operations.AutoGenerate_ProductID()
                    print("Product ID generated is "+str(Product_id))
                    print("Enter Product Name")
                    Product_Name=input()
                    print("Enter Product Type")
                    Product_type=input()
                    print("Enter Price per Day")
                    Price_per_day=int(input())
                    print("Enter Total Stock Available")
                    total_stock=int(input())
                    if len(Product_Name)*len(Product_type)==0 or Price_per_day<=0 or total_stock<=0:
                        print("Please enter valid data !!")
                        continue
                    operations.Create_Product(Username,'Products.json',Product_id,Product_Name,Product_type,Price_per_day,total_stock)
                    print("Product Created Successfully")
                elif in2==2:
                    print("Enter Product ID")
                    Product_id=input()
                    print("Enter Detail to be updated(Product Title | Product Type | Price Per Day | Total Stock Available)")
                    Detail_to_be_updated=input()
                    print("Enter Updated detail")
                    Updated_detail=input()
                    ch=operations.Update_Product(Username,'Products.json',Product_id,Detail_to_be_updated,Updated_detail)
                    if ch==True:
                        print("Product updated successfully !!")
                    else:
                        print("Product not updated !!")
                elif in2==3:
                    details=operations.Fetch_all_Products_created_by_seller(Username,'Products.json')
                    if len(details)==0:
                        print("No Products Created !!")
                    else:
                        for i in range(len(details)):
                            print("Product ID: "+str(details[i]["Product ID"]))
                            print("Product Title: "+str(details[i]["Product Title"]))
                            print("Product Type: "+str(details[i]["Product Type"]))
                            print("Price Per Day: "+str(details[i]["Price Per Day"]))
                            print("Total Stock Available: "+str(details[i]["Total Stock Available"]))
                            print('\n')
                elif in2==4:
                    print("Enter Product ID")
                    Product_Id=input()
                    details=operations.Fetch_Product_By_ID('Products.json',Product_Id)
                    if len(details)==0:
                        print("Invalid ID")
                    else:
                         for i in range(len(details)):
                            print("Product Title: "+str(details[i]["Product Title"]))
                            print("Product Type: "+str(details[i]["Product Type"]))
                            print("Price Per Day: "+str(details[i]["Price Per Day"]))
                            print("Total Stock Available: "+str(details[i]["Total Stock Available"]))
                            print('\n')
                         continue
                elif in2==5:
                    print("Enter Username")
                    usrnm=input()
                    details=operations.View_User_Details('Gamers.json',usrnm)
                    if len(details)==0:
                        print("Invalid Username")
                    else:
                        for i in range(len(details)):
                            print("Email: "+str(details[i]["Email"]))
                            print("Contact Number: "+str(details[i]["Contact Number"]))
                            print("Wishlist: "+str(details[i]["Wishlist"]))
                            print("Cart: ")
                            cart=details[i]["Cart"]
                            for j in range(len(cart)):
                                print("  Product ID: "+str(cart[j]["Product ID"]))
                                print("  Quantity: "+str(cart[j]["Quantity"]))
                                print("  Price Per Day: "+str(cart[j]["Price"]))
                                print("  Booking Start Date: "+str(cart[j]["Booking Start Date"]))
                                print("  Booking End Date: "+str(cart[j]["Booking End Date"]))
                                print('\n')
                            print('\n')
                        continue
                elif in2==6:
                    break
                else:
                    print("Please Enter valid input")
        else:
            print("Invalid Credentials !!")
    elif in1==4:
        print("Enter Username")
        Username=input()
        print("Enter Password")
        Password=input()
        ch=operations.Login('gamer','Gamers.json','Sellers.json',Username,Password)
        if ch==True:
            print("Welcome "+str(Username))
            in3=1
            while(in3!=7):
                print("Press: ")
                print("1. View all Product")
                print("2. Manage wishlist")
                print("3. Manage cart")
                print("4. Place order")
                print("5. Update Profile")
                print("6. View Orders")
                print("7. Logout")
                in3=int(input())
                if in3==1:
                    l=operations.Fetch_all_products('Products.json')
                    if len(l)==0:
                        print("No Products created !!")
                    else:
                        for i in range(len(l)):
                            print("Product ID: "+str(l[i]["Product ID"]))
                            print("Product Title: "+str(l[i]["Product Title"]))
                            print("Product Type: "+str(l[i]["Product Type"]))
                            print("Price Per Day: "+str(l[i]["Price Per Day"]))
                            print("Total Stock Available: "+str(l[i]["Total Stock Available"]))
                            print('\n')
                        continue
                elif in3==2:
                    print("Press: ")
                    print("1. Add item to wishlist")
                    print("2. Remove Item from wishlist")
                    in31=int(input())
                    if in31==1:
                        print("Enter Product ID")
                        Product_Id=input()
                        f=open('Products.json','r')
                        try:
                            content=json.load(f)
                        except JSONDecodeError:
                            print("No products created !!")
                            continue
                        if Product_Id not in str(content):
                            print("Please Enter Valid Product ID")
                            continue
                        else:
                            ch=operations.Add_item_to_wishlist(Username,Product_Id,'Gamers.json')
                            if ch==True:
                                print("Added item successfully !!")
                                continue
                            else:
                                print("Cannot add item !!")
                                continue
                    if in31==2:
                        print("Enter Product ID")
                        Product_Id=input()
                        f=open('Products.json','r')
                        try:
                            content=json.load(f)
                        except JSONDecodeError:
                            print("No products created !!")
                            continue
                        if Product_Id not in str(content):
                            print("Please Enter Valid Product ID")
                            continue
                        else:
                            ch=operations.Remove_item_from_wishlist(Username,Product_Id,'Gamers.json')
                            if ch==True:
                                print("Removed item successfully !!")
                                continue
                            else:
                                print("Cannot remove item !!")
                                continue
                    else:
                        print("Please Enter Valid choice")
                elif in3==3:
                    print("Press: ")
                    print("1. Add item to cart")
                    print("2. Remove Item from cart")
                    print("3. View Cart")
                    in31=int(input())
                    if in31==1:
                        print("Enter Product ID")
                        Product_Id=input()
                        print("Enter Quantity")
                        Quantity=int(input())
                        print("Enter Booking Start Date (YYYY-MM-DD)")
                        Booking_start_date=input()
                        print("Enter Booking End Date (YYYY-MM-DD)")
                        Booking_end_date=input()
                        f=open('Products.json','r')
                        try:
                            content=json.load(f)
                            f.close()
                        except JSONDecodeError:
                            print("No products created !!")
                            f.close()
                            continue
                        if Product_Id not in str(content):
                            print("Please Enter Valid Product ID")
                            continue
                        can_add=operations.Add_item_to_cart(Username,Product_Id,Quantity,'Gamers.json',Booking_start_date,Booking_end_date,'Products.json')
                        f.close()
                        if can_add==True:
                            print("Added item successfully !!")
                            continue
                        else:
                            print("Cannot add item to cart !!")
                            continue
                    if in31==2:
                        print("Enter Product ID")
                        Product_Id=input()
                        f=open('Products.json','r')
                        try:
                            content=json.load(f)
                            f.close()
                        except JSONDecodeError:
                            print("No products created !!")
                            f.close()
                            continue
                        if Product_Id not in str(content):
                            print("Please Enter Valid Product ID")
                            continue
                        can_remove=operations.Remove_item_from_cart(Username,Product_Id,'Gamers.json')
                        if can_remove==True:
                            print("Item removed successfully from cart !!")
                        else:
                            print("Cannot remove item")
                    elif in31==3:
                        cart=operations.View_Cart(Username,'Gamers.json')
                        if len(cart)==0:
                            print("Cart Empty !!")
                        else:
                            for i in range(len(cart)):
                                print("Product ID: "+str(cart[i]["Product ID"]))
                                print("Quantity: "+str(cart[i]["Quantity"]))
                                print("Price Per Day: "+str(cart[i]["Price"]))
                                print("Booking Start Date: "+str(cart[i]["Booking Start Date"]))
                                print("Booking End Date: "+str(cart[i]["Booking End Date"]))
                                print('\n')
                    else:
                        print("Please Enter Valid choice")
                elif in3==4:
                    Order_id=operations.AutoGenerate_OrderID()
                    print("Order ID genrated is "+str(Order_id))
                    order_placed=operations.Place_order(Username,'Gamers.json',Order_id,'Orders.json','Products.json')
                    if order_placed==True:
                        print("Order Placed Successfully with Order ID "+str(Order_id))
                    else:
                        print("Order Unsuccessful !!")
                elif in3==5:
                    print("Enter Detail to be updated ( Email | Password | Contact Number )")
                    Detail_to_be_updated=input()
                    print("Enter Updated detail")
                    Updated_detail=input()
                    upd=operations.Update_User('Gamers.json',Username,Detail_to_be_updated,Updated_detail)
                    if upd==True:
                        print("Profile Updated successfully !!")
                    else:
                        print("Cannot Update Profile !!")
                elif in3==6:
                    orders=operations.Fetch_all_orders('Orders.json',Username)
                    if len(orders)==0:
                        print("No orders placed !!")
                    else:
                        for i in range(len(orders)):
                            print("Order ID: "+str(orders[i]["Order ID"]))
                            print("Items: ")
                            cart=orders[i]["Items"]
                            for j in range(len(cart)):
                                print("  Product ID: "+str(cart[j]["Product ID"]))
                                print("  Quantity: "+str(cart[j]["Quantity"]))
                                print("  Price Per Day: "+str(cart[j]["Price"]))
                                print("  Booking Start Date: "+str(cart[j]["Booking Start Date"]))
                                print("  Booking End Date: "+str(cart[j]["Booking End Date"]))
                                print('\n')
                            print("Total Cost: "+str(orders[i]["Total Cost"]))
                elif in3==7:
                    break
                else:
                    print("Please Enter Valid choice")
        else:
            print("Invalid Credentials !!")
    elif in1==5:
        break
    else:
        print("Please Enter Valid choice")                    