import pymysql
from ExtraCost import ExtraCost
from Vehicle import Vehicle
from Sale import Sale
import datetime

x = Vehicle(2114, "Car", "ABCDEFG4567345684", 2012, "Toyota", "Camry", "Red", "Sedan", "12345678", 4, 75000, "MO",
            "Wholesale", 20000, "2015-10-15", "Rayan")
y = Vehicle(2117, "Car", "ABCDEFG4567346756", 2010, "Honda", "Accord", "Black", "Sedan", "87654321", 4, 100000, "MO",
            "Wholesale", 15000, "2013-11-12", "Dani")
z = Vehicle(2116, "Car", "ABCDEFG4567343452", 2008, "Nissan", "Altima", "Silver", "Sedan", "98765432", 4, 80000, "MO",
            "Wholesale",10000, "2013-08-11", "Aleeza")

x1 = ExtraCost('2017-01-25', 'Airbag', 2000, "Ebay")
y1 = ExtraCost('2021-04-15', "Headlight", 10000, "O'Reileys")
z1 = ExtraCost('2014-12-15', "Bumper", 5000, "Autozone")

x2 = Sale(10000, 1000, 500, datetime.date(2020, 4, 17))
y2 = Sale(20000, 2000, 1000, datetime.date(2021, 3, 21))
z2 = Sale(15000, 1000, 1000, datetime.date(2019, 5, 5))

# Code below establishes a connection with mySQL
db = pymysql.connect(
    host="localhost",
    user="root",
    passwd="Froggy24!",
    database="car_lot"
)

# mycursor is what is used to interact with the code
mycursor = db.cursor()



# An object of type Vehicle is passed in and is added to the Vehicle table in mySQL
def add_transaction(x):
    mycursor.execute("INSERT INTO Vehicle (StockNum, Category, Vin, CarYear, Make, Model, Color, Style, PrevTitleNum,"
                     "NumCylinders, Mileage, PrevState, TypeofPurchase, PurchasePrice, DatePurchased,"
                     "CustomerName, CostofRepairs, TotalCost) VALUES(%s,%s,%s,%s,%s,"
                     "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (x.get_stock_num(), x.get_category(),
                    x.get_vin(), x.get_year(), x.get_make(), x.get_model(), x.get_color(), x.get_style(),
                    x.get_prev_title_num(), x.get_num_cylinders(), x.get_mileage(), x.get_prev_state(),
                    x.get_typeofpurchase(), x.get_purchase_price(), x.get_date_purchased(),
                    x.get_customer_name(),x.get_cost_of_repairs(), x.get_total_cost()))
    db.commit()
"""
add_transaction(x)
add_transaction(y)
add_transaction(z)
"""


def add_sale(x, y):
    mycursor.execute("INSERT INTO Sale (CarID, SellingPrice, CashDown, AmountFinanced, PaymentRate, SoldDate, "
                     "FirstPaymentDate, FinalPaymentDate, FinalPaymentAmount) Values(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                     (y, x.get_selling_price(), x.get_cash_down(), x.get_amount_financed(), x.get_payment_rate(), x.get_sold_date(),
                      x.get_first_payment_date(), x.get_final_payment_date(), x.get_final_payment_amt()))
    db.commit()
    query = "UPDATE Vehicle SET DateSold = %s, SoldAmount = %s, active = %s WHERE CarID = %s"
    mycursor.execute(query, (x.get_sold_date(), x.get_selling_price(), "inactive", y))
    db.commit()
"""
add_sale(x2, 16)
add_sale(y2, 17)
add_sale(z2, 18)
"""



# An object of type ExtraCost and the associated CarID is passed in and is added to the ExtraCost table in mySQL
# The cost of repairs and total cost variables in Vehicle are also updated as extra costs are added
def add_cost(x, y):
    mycursor.execute("INSERT INTO ExtraCost (CarID, DateofPurchase, Description, Amount, Vendor)"
                     "VALUES(%s, %s, %s, %s, %s )", (y, x.get_date_of_purchase(), x.get_description(),
                      x.get_amount(), x.get_vendor()))
    db.commit()
    query = "SELECT * FROM Vehicle WHERE CarID = %s"
    mycursor.execute(query, y)
    for i in mycursor:
        var1 = i[18] + x.get_amount()
        var2 = i[19] + x.get_amount()
    query = "UPDATE Vehicle SET CostOfRepairs = %s, TotalCost = %s WHERE CarID = %s"
    mycursor.execute(query, (var1, var2, y))
    db.commit()

"""
add_cost(x1, 16)
add_cost(y1, 16)
add_cost(z1, 16)
"""

# Helper function which is used for formatting purposed in each filter function
def helper_func(x):
    print("Stock Num: " + str(x[0]))
    print("Category: " + x[1])
    print("Vin: " + x[2])
    print("Car Year: " + str(x[3]))
    print("Car Make: " + x[4])
    print("Car Model: " + x[5])
    print("Car Color: " + x[6])
    print("Car Style: " + x[7])
    print("Previous Title Number: " + str(x[8]))
    print("Number of Cylinders: " + str(x[9]))
    print("Mileage: " + str(x[10]))
    print("Previous State: " + x[11])
    print("Type of Purchase: " + x[12])
    print("Purchase Price: " + str(x[13]))
    datepurchased = x[14].strftime('%Y-%m-%d')
    print("Date Purchased: " + datepurchased)
    datesold = x[15].strftime('%Y-%m-%d')
    print("Date Sold: " + datesold)
    print("Customer Name: " + x[16])
    print("Sold Amount: " + str(x[17]))
    print("Cost of Repairs: " + str(x[18]))
    print("Total Cost: " + str(x[19]))
    print("Car ID: " + str(x[20]))
    print("END CAR")

# Prints the current active vehicles from the Vehicle table
def active_list():
    query = "SELECT * FROM Vehicle WHERE active = 'active'"
    mycursor.execute(query)
    for x in mycursor:
        helper_func(x)

# Prints the current inactive vehicles from the Vehicle table
def inactive_list():
    query = "SELECT * FROM Vehicle WHERE active = 'inactive'"
    mycursor.execute(query)
    for x in mycursor:
        helper_func(x)

# Takes in a CarID as an input and returns a list of all of the associated repairs for that car
def repairs_list(x):
    query = "SELECT * FROM ExtraCost WHERE CarID = %s"
    mycursor.execute(query, x)
    for x in mycursor:
        print("Car ID: " + str(x[0]))
        datepurchased = x[1].strftime('%Y-%m-%d')
        print("Date of Purchase: " + datepurchased)
        print("Description: " + x[2])
        print("Cost: " + str(x[3]))
        print("Vendor: " + x[4])

# repairs_list(4)

# Takes in two integers and either Mileage, CarYear, PurchasePrice, or TotalCost as the column that is filtered
def range_filter(x, y, z):
    query = f"SELECT * FROM Vehicle WHERE {z} BETWEEN %s and %s ORDER BY {z} ASC"
    mycursor.execute(query, (x, y))
    for x in mycursor:
        helper_func(x)

# range_filter(70000, 90000, "Mileage")

# Takes in two dates and either DatePurchased or DateSold as the column that is filtered
def date_filter(x, y, z):
    query = f"SELECT * FROM Vehicle WHERE {z} >= %s AND {z} <= %s"
    mycursor.execute(query, (x, y))
    for x in mycursor:
        helper_func(x)

# date_filter("2014-01-01", "2016-01-01", "DatePurchased")

# Takes in the desired filter value and then either CustomerName, CarID, StockNum, Make, Model, Color, or Vin as the filtered column
def specific_filter(x, z):
    query = f"SELECT * FROM Vehicle WHERE {z} = %s"
    mycursor.execute(query, x)
    for x in mycursor:
        helper_func(x)

# specific_filter("2114", "StockNum")






