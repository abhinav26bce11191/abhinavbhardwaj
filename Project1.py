# ==========================================================
#              PHARMACY MANAGEMENT SYSTEM
# ==========================================================

import json
import os

# ----------------------------------------------------------
#  JSON DATABASE
# ----------------------------------------------------------
DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pharmacy_data.json")

medicines = []
ordered_drugs = []
employees = []
customers = []
cart = []          


def save_data():
    data = {
        "medicines": medicines,
        "ordered_drugs": ordered_drugs,
        "employees": employees,
        "customers": customers,
    }
    tmp_file = DB_FILE + ".tmp"
    try:
        with open(tmp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        os.replace(tmp_file, DB_FILE)
    except OSError as error:
        print("Warning: could not save data ->", error)


def load_data():
    if not os.path.exists(DB_FILE):
        return

    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        backup = DB_FILE + ".corrupt"
        os.replace(DB_FILE, backup)
        print("Warning: database file was damaged. Saved a copy as", backup)
        return
    except OSError as error:
        print("Warning: could not read data ->", error)
        return

    medicines[:] = data.get("medicines", [])
    ordered_drugs[:] = data.get("ordered_drugs", [])
    employees[:] = data.get("employees", [])
    customers[:] = data.get("customers", [])


load_data()


# ==========================================================
#                    ADD DRUGS
# ==========================================================

def add_drugs():

    print("\n==========================================")
    print("              ADD DRUGS")
    print("==========================================")

    while True:

        medicine = {}
        try:
            medicine["S_NO"] = int(input("Enter S_NO: "))
            medicine["Prescription_ID"] = int(input("Enter Prescription_ID: "))
            medicine["Batch_Number"] = int(input("Enter Batch_Number: "))
        except ValueError:
            print("Please enter valid data type........")
            continue
        medicine["Drug_Name"] = input("Enter Drug_Name: ")
        medicine["Company_Name"] = input("Enter Company_Name: ")
        medicine["Drug_Type"] = input("Enter Drug_Type: ")
        medicine["Uses"] = input("Enter Uses: ")
        try:
            medicine["Price"] = float(input("Enter Price: "))
            medicine["Stock"] = int(input("Enter Stock: "))
            if medicine["Price"] < 0 or medicine["Stock"] < 0:
                print("Price and Stock cannot be negative.")
                continue
        except ValueError:
            print("Please enter valid data type......")
            continue

        medicines.append(medicine)
        save_data()

        print("\nRow inserted successfully...")

        choice = input("\nDo you want to enter more records (y/n): ")

        if choice.lower() != "y":
            break


# ==========================================================
#                 ADD ORDERED DRUGS
# ==========================================================

def add_ordered_drugs():

    print("\n==========================================")
    print("           ADD ORDERED DRUGS")
    print("==========================================")

    order = {}
    try:
        order["Order_ID"] = int(input("Enter Order_ID: "))
        order["Drug_Name"] = input("Enter Drug_Name: ")
        order["Drug_Type"] = input("Enter Drug_Type: ")
        order["Ordered_quantity"] = int(input("Enter Ordered_quantity: "))
        order["Price"] = float(input("Enter Price: "))
        order["Customer_Name"] = input("Enter Customer_Name: ")
        order["Phone_no"] = input("Enter Phone_no: ")
        order["Address"] = input("Enter Address: ")
    except ValueError:
        print("Please enter valid data type........")
        return

    ordered_drugs.append(order)
    save_data()

    print("\nOrder record added successfully...")


# ==========================================================
#                    ORDERED DRUGS
# ==========================================================

def show_ordered_drugs():

    print("\n==========================================")
    print("             ORDERED DRUGS")
    print("==========================================")

    if len(ordered_drugs) == 0:
        print("No ordered drug records found.")
        return

    for order in ordered_drugs:

        print("\nOrder_ID:", order["Order_ID"])
        print("Drug_Name:", order["Drug_Name"])
        print("Drug_Type:", order["Drug_Type"])
        print("Ordered_quantity:", order["Ordered_quantity"])
        print("Price:", order["Price"])
        print("Customer_Name:", order["Customer_Name"])
        print("Phone_no:", order["Phone_no"])
        print("Address:", order["Address"])

        print("------------------------------------------")


# ==========================================================
#                     CHECK STOCK
# ==========================================================

def check_stock():

    print("\n==========================================")
    print("               CHECK STOCK")
    print("==========================================")

    if len(medicines) == 0:
        print("No medicine records found.")
        return

    for medicine in medicines:

        print("\nS_NO:", medicine["S_NO"])
        print("Drug_Name:", medicine["Drug_Name"])
        print("Batch_Number:", medicine["Batch_Number"])
        print("Stock:", medicine["Stock"])
        print("Price:", medicine["Price"])

        print("------------------------------------------")


# ==========================================================
#                   ADD EMPLOYEE
# ==========================================================

def add_employee():

    print("\n==========================================")
    print("              ADD EMPLOYEE")
    print("==========================================")

    employee = {}
    try:
        employee["Employee_ID"] = int(input("Enter Employee_ID: "))
        employee["Employee_Name"] = input("Enter Employee_Name: ")
        employee["Role"] = input("Enter Role: ")
        employee["Salary"] = float(input("Enter Salary: "))
        employee["Phone_no"] = input("Enter Phone_no: ")
        employee["Address"] = input("Enter Address: ")
    except ValueError:
        print("Please enter valid data type..........")
        return

    employees.append(employee)
    save_data()

    print("\nRow inserted successfully...")


# ==========================================================
#                    EMPLOYEE
# ==========================================================

def show_employee():

    print("\n==========================================")
    print("               EMPLOYEE")
    print("==========================================")

    if len(employees) == 0:
        print("No employee records found.")
        return

    for employee in employees:

        print("\nEmployee_ID:", employee["Employee_ID"])
        print("Employee_Name:", employee["Employee_Name"])
        print("Role:", employee["Role"])
        print("Salary:", employee["Salary"])
        print("Phone_no:", employee["Phone_no"])
        print("Address:", employee["Address"])

        print("------------------------------------------")


# ==========================================================
#                   ADD CUSTOMER
# ==========================================================

def add_customer():

    print("\n==========================================")
    print("              ADD CUSTOMER")
    print("==========================================")

    customer = {}
    try:
        customer["S_NO"] = int(input("Enter S_NO: "))
        customer["Customer_Name"] = input("Enter Customer_Name: ")
        customer["Phone_no"] = input("Enter Phone_no: ")
        customer["Address"] = input("Enter Address: ")
    except ValueError:
        print("Please enter valid data type........")
        return

    customers.append(customer)
    save_data()

    print("\nRow inserted successfully...")


# ==========================================================
#                     CUSTOMER
# ==========================================================

def show_customer():

    print("\n==========================================")
    print("                CUSTOMER")
    print("==========================================")

    if len(customers) == 0:
        print("No customer records found.")
        return

    for customer in customers:

        print("\nS_NO:", customer["S_NO"])
        print("Customer_Name:", customer["Customer_Name"])
        print("Phone_no:", customer["Phone_no"])
        print("Address:", customer["Address"])

        print("------------------------------------------")


# ==========================================================
#                 SEARCH MEDICINE
# ==========================================================

def search_medicine():

    print("\n==========================================")
    print("             SEARCH MEDICINE")
    print("==========================================")

    if len(medicines) == 0:
        print("No medicine available.")
        return

    name = input("Enter the Drug Name: ")

    found = False

    for medicine in medicines:

        if medicine["Drug_Name"].lower() == name.lower():

            print("\n_____ MEDICINE DETAILS _____")

            print("S_NO:", medicine["S_NO"])
            print("Prescription_ID:", medicine["Prescription_ID"])
            print("Batch_Number:", medicine["Batch_Number"])
            print("Drug_Name:", medicine["Drug_Name"])
            print("Company_Name:", medicine["Company_Name"])
            print("Drug_Type:", medicine["Drug_Type"])
            print("Uses:", medicine["Uses"])
            print("Price:", medicine["Price"])
            print("Stock:", medicine["Stock"])

            found = True
            break

    if found == False:
        print("\nMedicine not found.")

#===========================================================
#                  BROWSE MEDICINE
#===========================================================
def browse_medicine():
    while True:
        print("\n" + "="*45)
        print("                BROWSE MEDICINE")
        print("="*45)
         
        print("1. Veiw All Medicine")
        print("2. Browse By Company")
        print("3. Browse By Drug Type")
        print("4. Back")
        
        choice=input("Enter your choice: ")
        if choice == "1":
            if not medicines:
                print("No medicine available.")
            else:
                print("\n"+ "="*45)
                print("                 ALL MEDICINE")
                print("-"*70)
                for medicine in medicines:
                    print(
                        f"Medicine: {medicine['Drug_Name']} | "
                        f"Company: {medicine['Company_Name']} | "
                        f"Type: {medicine['Drug_Type']} | "
                        f"Price: ₹{medicine['Price']} | "
                        f"Stock: {medicine['Stock']}"
                    )

        elif choice == "2":
            company = input("\nEnter company name: ").lower()

            found = False

            for medicine in medicines:
                if company in medicine["Company_Name"].lower():
                    print(
                        f"\nMedicine: {medicine['Drug_Name']}"
                        f"\nCompany: {medicine['Company_Name']}"
                        f"\nType: {medicine['Drug_Type']}"
                        f"\nPrice: ₹{medicine['Price']}"
                        f"\nStock: {medicine['Stock']}"
                    )
                    found = True

            if not found:
                print("\nNo medicine found for this company.")

        elif choice == "3":
            drug_type = input("\nEnter drug type: ").lower()

            found = False

            for medicine in medicines:
                if drug_type in medicine["Drug_Type"].lower():
                    print(
                        f"\nMedicine: {medicine['Drug_Name']}"
                        f"\nCompany: {medicine['Company_Name']}"
                        f"\nType: {medicine['Drug_Type']}"
                        f"\nPrice: ₹{medicine['Price']}"
                        f"\nStock: {medicine['Stock']}"
                    )
                    found = True

            if not found:
                print("\nNo medicine found for this drug type.")

        elif choice == "4":
            break

        else:
            print("\nInvalid choice.")
#=================================================================
#                       VIEW MEDICINE DETAILS     
#=================================================================     
def view_medicine_details():
    name = input("\nEnter medicine name: ").lower()

    found = False

    for medicine in medicines:

        if medicine["Drug_Name"].lower() == name:

            print("\n" + "=" * 45)
            print("          MEDICINE DETAILS")
            print("=" * 45)

            print("S.No           :", medicine["S_NO"])
            print("Prescription ID:", medicine["Prescription_ID"])
            print("Batch Number   :", medicine["Batch_Number"])
            print("Drug Name      :", medicine["Drug_Name"])
            print("Company        :", medicine["Company_Name"])
            print("Drug Type      :", medicine["Drug_Type"])
            print("Uses           :", medicine["Uses"])
            print("Price          : ₹", medicine["Price"])
            print("Stock          :", medicine["Stock"])

            found = True
            break

    if not found:
        print("\nMedicine not found.")    
#======================================================
#                     SHOPPING CART
#======================================================
def shopping_cart():
    while True:

        print("\n" + "=" * 50)
        print("                 SHOPPING CART")
        print("=" * 50)

        if not cart:
            print("Your cart is empty.")
        else:
            total = 0

            print("\nMedicine              Qty       Price       Total")
            print("-" * 50)

            for item in cart:
                item_total = item["Quantity"] * item["Price"]
                total += item_total

                print(
                    f"{item['Drug_Name']:<20}"
                    f"{item['Quantity']:<10}"
                    f"₹{item['Price']:<10}"
                    f"₹{item_total}"
                )

            print("-" * 50)
            print("Total Amount: ₹", total)

        print("\n1. Add Medicine")
        print("2. Change Quantity")
        print("3. Remove Medicine")
        print("4. Continue Shopping")
        print("5. Checkout")
        print("6. Clear Cart")
        print("7. Back")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_to_cart()

        elif choice == "2":
            change_cart_quantity()

        elif choice == "3":
            remove_from_cart()

        elif choice == "4":
            continue

        elif choice == "5":
            checkout()

        elif choice == "6":
            cart.clear()
            print("\nCart cleared.")

        elif choice == "7":
            break

        else:
            print("\nInvalid choice.")
#==============================================
#                ADD TO CART
#==============================================
def add_to_cart():

    name = input("\nEnter medicine name: ").lower()

    for medicine in medicines:

        if medicine["Drug_Name"].lower() == name:

            try:
                quantity = int(input("Enter quantity: "))

                if quantity <= 0:
                    print("\nQuantity must be greater than 0.")
                    return

                already_in_cart = 0
                for item in cart:
                    if item["Drug_Name"].lower() == name:
                        already_in_cart = item["Quantity"]

                if already_in_cart + quantity > medicine["Stock"]:
                    print("\nNot enough stock available.")
                    return

                for item in cart:
                    if item["Drug_Name"].lower() == name:
                        item["Quantity"] += quantity
                        print("\nQuantity updated in cart.")
                        return

                cart_item = {
                    "Drug_Name": medicine["Drug_Name"],
                    "Drug_Type": medicine["Drug_Type"],
                    "Quantity": quantity,
                    "Price": float(medicine["Price"])
                }

                cart.append(cart_item)

                print("\nMedicine added to cart.")
                return

            except ValueError:
                print("\nPlease enter a valid quantity.")
                return

    print("\nMedicine not found.")
#===============================================
#              CHANGE CART QUANTITY
#===============================================
def change_cart_quantity():

    if not cart:
        print("\nYour cart is empty.")
        return

    name = input("\nEnter medicine name: ").lower()

    for item in cart:

        if item["Drug_Name"].lower() == name:

            try:
                quantity = int(input("Enter new quantity: "))

                if quantity <= 0:
                    print("\nQuantity must be greater than 0.")
                    return

                for medicine in medicines:
                    if medicine["Drug_Name"].lower() == name:

                        if quantity > medicine["Stock"]:
                            print("\nNot enough stock available.")
                            return

                        item["Quantity"] = quantity
                        print("\nCart quantity updated.")
                        return

            except ValueError:
                print("\nPlease enter a valid quantity.")
                return

    print("\nMedicine not found in cart.")
#=================================================
#                  REMOVE FROM CART
#================================================
def remove_from_cart():

    if not cart:
        print("\nYour cart is empty.")
        return

    name = input("\nEnter medicine name to remove: ").lower()

    for item in cart:

        if item["Drug_Name"].lower() == name:

            cart.remove(item)

            print("\nMedicine removed from cart.")
            return

    print("\nMedicine not found in cart.")
#=================================================
#                     CHECKOUT
#================================================
def checkout():

    if not cart:
        print("\nYour cart is empty.")
        return

    total = 0

    print("\n" + "=" * 55)
    print("                    BILL")
    print("=" * 55)

    for item in cart:

        item_total = item["Quantity"] * item["Price"]
        total += item_total

        print(
            f"{item['Drug_Name']} "
            f"x {item['Quantity']} "
            f"= ₹{item_total}"
        )

    print("-" * 55)
    print("Total Amount: ₹", total)

    confirm = input("\nConfirm purchase? (yes/no): ").lower()

    if confirm != "yes":
        print("\nPurchase cancelled.")
        return

    # Check stock again before completing purchase
    for item in cart:

        for medicine in medicines:

            if medicine["Drug_Name"].lower() == item["Drug_Name"].lower():

                if item["Quantity"] > medicine["Stock"]:
                    print(
                        f"\nNot enough stock for {medicine['Drug_Name']}."
                    )
                    return

    # Reduce stock and create orders
    for item in cart:

        for medicine in medicines:

            if medicine["Drug_Name"].lower() == item["Drug_Name"].lower():

                medicine["Stock"] -= item["Quantity"]

                order = {
                    "Order_ID": len(ordered_drugs) + 1,
                    "Drug_Name": item["Drug_Name"],
                    "Drug_Type": item["Drug_Type"],
                    "Ordered_quantity": item["Quantity"],
                    "Price": item["Price"],
                    "Customer_Name": "User",
                    "Phone_no": "",
                    "Address": ""
                }

                ordered_drugs.append(order)

                break

    save_data()

    print("\nPurchase successful.")
    print("Total Amount: ₹", total)

    cart.clear()

    print("Thank you for shopping with us.")
#====================================================
#                   USER ORDERS
#====================================================
def my_orders():

    print("\n" + "=" * 50)
    print("                  MY ORDERS")
    print("=" * 50)

    if not ordered_drugs:
        print("No orders found.")
        return

    for order in ordered_drugs:

        print("\nOrder ID       :", order["Order_ID"])
        print("Medicine       :", order["Drug_Name"])
        print("Drug Type      :", order["Drug_Type"])
        print("Quantity       :", order["Ordered_quantity"])
        print("Price          : ₹", order["Price"])
        print("Customer       :", order["Customer_Name"])

        print("-" * 50)
#=====================================================
#                 PURCHASE HISTORY
#=====================================================
def purchase_history():

    print("\n" + "=" * 50)
    print("              PURCHASE HISTORY")
    print("=" * 50)

    if not ordered_drugs:
        print("No purchase history available.")
        return

    total_spent = 0

    for order in ordered_drugs:

        amount = order["Ordered_quantity"] * order["Price"]
        total_spent += amount

        print(
            f"\nOrder ID : {order['Order_ID']}"
            f"\nMedicine : {order['Drug_Name']}"
            f"\nQuantity : {order['Ordered_quantity']}"
            f"\nAmount   : ₹{amount}"
        )

    print("\n" + "-" * 50)
    print("Total Purchase Amount: ₹", total_spent)
#====================================================
#                   USER PROFILE
#====================================================
def my_profile():

    print("\n" + "=" * 45)
    print("               MY PROFILE")
    print("=" * 45)

    print("1. View Profile")
    print("2. Update Profile")
    print("3. Back")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        view_my_profile()

    elif choice == "2":
        update_my_profile()

    elif choice == "3":
        return

    else:
        print("\nInvalid choice.")
def view_my_profile():

    if not customers:
        print("\nNo customer profile found.")
        return

    print("\n" + "=" * 45)
    print("             PROFILE DETAILS")
    print("=" * 45)

    customer = customers[-1]

    print("S.No        :", customer["S_NO"])
    print("Name        :", customer["Customer_Name"])
    print("Phone       :", customer["Phone_no"])
    print("Address     :", customer["Address"])
#====================================================
#                   UPDATE MY PROFILE
#====================================================
def update_my_profile():

    if not customers:
        print("\nNo customer profile found.")
        return

    customer = customers[-1]

    print("\nLeave input blank if you don't want to change it.")

    name = input("Enter new name: ")
    phone = input("Enter new phone number: ")
    address = input("Enter new address: ")

    if name:
        customer["Customer_Name"] = name

    if phone:
        customer["Phone_no"] = phone

    if address:
        customer["Address"] = address

    save_data()
    print("\nProfile updated successfully.")

# ==========================================================
#                   BUY MEDICINE
# ==========================================================

def buy_medicine():

    print("\n==========================================")
    print("              BUY MEDICINE")
    print("==========================================")

    if len(medicines) == 0:
        print("No medicine available.")
        return

    name = input("Enter Drug Name: ")

    found_medicine = None

    for medicine in medicines:

        if medicine["Drug_Name"].lower() == name.lower():
            found_medicine = medicine
            break

    if found_medicine is None:
        print("\nMedicine not found.")
        return

    print("\nMedicine Found")
    print("Drug Name:", found_medicine["Drug_Name"])
    print("Price:", found_medicine["Price"])
    print("Available Stock:", found_medicine["Stock"])

    try:
        quantity = int(input("Enter Quantity: "))
    except ValueError:
        print("\nPlease enter a valid quantity.")
        return

    if quantity <= 0:
        print("\nInvalid quantity.")
        return

    if quantity > found_medicine["Stock"]:
        print("\nSorry, insufficient stock.")
        return

    customer_name = input("Enter Customer Name: ")
    phone = input("Enter Phone_no: ")
    address = input("Enter Address: ")

    total_price = quantity * found_medicine["Price"]

    found_medicine["Stock"] -= quantity

    order = {}

    order["Order_ID"] = len(ordered_drugs) + 1
    order["Drug_Name"] = found_medicine["Drug_Name"]
    order["Drug_Type"] = found_medicine["Drug_Type"]
    order["Ordered_quantity"] = quantity
    order["Price"] = found_medicine["Price"]   # unit price (same as checkout)
    order["Customer_Name"] = customer_name
    order["Phone_no"] = phone
    order["Address"] = address

    ordered_drugs.append(order)
    save_data()

    print("\n==========================================")
    print("                BILL")
    print("==========================================")

    print("Order_ID:", order["Order_ID"])
    print("Drug_Name:", order["Drug_Name"])
    print("Quantity:", order["Ordered_quantity"])
    print("Price per unit:", found_medicine["Price"])
    print("Total Price:", total_price)

    print("------------------------------------------")
    print("Customer Name:", customer_name)
    print("Phone No:", phone)
    print("Address:", address)

    print("\n_____ THANK YOU FOR YOUR ORDER _____")


# ==========================================================
#                    ADMIN MENU
# ==========================================================

def admin_menu():

    while True:

        print("\n==========================================")
        print("                ADMIN MENU")
        print("==========================================")

        print("1. Add_Drugs")
        print("2. Add_Ordered_Drugs")
        print("3. Ordered_Drugs")
        print("4. Check_Stock")
        print("5. Add_Employee")
        print("6. Employee")
        print("7. Add_Customer")
        print("8. Customer")
        print("9. Exit")

        choice = input("\nEnter your choice :- ")

        if choice == "1":
            add_drugs()

        elif choice == "2":
            add_ordered_drugs()

        elif choice == "3":
            show_ordered_drugs()

        elif choice == "4":
            check_stock()

        elif choice == "5":
            add_employee()

        elif choice == "6":
            show_employee()

        elif choice == "7":
            add_customer()

        elif choice == "8":
            show_customer()

        elif choice == "9":
            print("\nThank you, Admin.")
            break

        else:
            print("\nInvalid choice. Please try again.")


# ==========================================================
#                     USER MENU
# ==========================================================

def user_menu():

    while True:

        print("\n==========================================")
        print("                 USER MENU")
        print("==========================================")

        print("1. Search_Medicine")
        print("2. Browse Medicine")
        print("3. View Medicine Details")
        print("4. Buy Medicine")
        print("5. Shopping Cart")
        print("6. My Orders")
        print("7. My Purchase History")
        print("8. My Profile")
        print("9. logout")

        choice = input("\nEnter Your Choice :- ")

        if choice == "1":
            search_medicine()

        elif choice == "2":
            browse_medicine()
        elif choice == "3":
            view_medicine_details()
        elif choice == "4":
            buy_medicine()
        elif choice == "5":
            shopping_cart()
        elif choice == "6":
            my_orders()
        elif choice == "7":
            purchase_history()
        elif choice == "8":
            my_profile()
        elif choice == "9":
            print("Logging out......")
            break

        else:
            print("\nInvalid choice. Please try again.")


# ==========================================================
#                     ADMIN LOGIN
# ==========================================================

def admin_login():

    print("\n==========================================")
    print("               ADMIN LOGIN")
    print("==========================================")

    username = input("Enter Admin Username: ")
    password = input("Enter Admin Password: ")

    # Sample login credentials
    if username == "Abhinav" and password == "Ab@123":

        print("\nLogin successful.")
        print("Welcome, Admin!")

        admin_menu()

    else:

        print("\nInvalid username or password.")


# ==========================================================
#                      USER LOGIN
# ==========================================================

def user_login():

    print("\n==========================================")
    print("                USER LOGIN")
    print("==========================================")

    username = input("Enter User Username: ")
    password = input("Enter User Password: ")

    # Sample login credentials
    if username == "user" and password == "1234":

        print("\nLogin successful.")
        print("Welcome, User!")

        user_menu()

    else:

        print("\nInvalid username or password.")


# ==========================================================
#                     MAIN PROGRAM
# ==========================================================

while True:

    print("\n")
    print("==========================================")
    print("        PHARMACY MANAGEMENT SYSTEM")
    print("==========================================")

    print("\n_____ WELCOME _____")

    print("\n1. ADMIN LOGIN")
    print("2. USER LOGIN")
    print("3. EXIT")

    choice = input("\nEnter Who Are You :- ")

    if choice == "1":

        admin_login()

    elif choice == "2":

        user_login()

    elif choice == "3":

        print("\n==========================================")
        print("       THANK YOU FOR USING THE SYSTEM")
        print("==========================================")

        break

    else:

        print("\nInvalid option. Please try again.")