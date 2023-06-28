from ExtraCost import ExtraCost
import re


class Vehicle(ExtraCost):
    # Each of the initialized variables represents a different characteristic of a certain vehicle
    # while the repairs variable is meant to be populated as parts are ordered
    def __init__(self, stock_num, category, vin, year, make, model, color, style, prev_title_num,
                 num_cylinders, mileage, prev_state, typeofpurchase, purchase_price,
                 date_purchased, customer_name, repairs=None, comments=None):
        self.stock_num = stock_num
        self.category = category
        self.vin = vin
        self.year = year
        self.make = make
        self.model = model
        self.color = color
        self.style = style
        self.prev_title_num = prev_title_num
        self.num_cylinders = num_cylinders
        self.mileage = mileage
        self.prev_state = prev_state
        self.typeofpurchase = typeofpurchase
        self.purchase_price = purchase_price
        self.date_purchased = date_purchased
        self.customer_name = customer_name
        self.repairs = [] if repairs is None else repairs
        self.comments = comments

    # The function add_cost appends an ExtraCost object to the list of repairs as parts are ordered
    def add_cost(self, cost):
        if isinstance(cost, ExtraCost):
            self.repairs.append(cost)

    # Returns the stock_num if it is both and integer and has 4 digits
    def get_stock_num(self):
        if isinstance(self.stock_num, int) and len(str(self.stock_num)) == 4:
            return self.stock_num
        else:
            return "ERROR"

    # Returns the car category if it is a valid input
    def get_category(self):
        if self.category == "Car" or self.category == "Cars" or self.category == "Sports Utility" or self.category == "Trucks" or self.category == "Van" or self.category == "Vans":
            return self.category
        else:
            return "ERROR"

    # Returns the vin if it is both a string and length of 17
    def get_vin(self):
        if isinstance(self.vin, str) and len(self.vin) == 17:
            return self.vin
        else:
            return "ERROR"

    # Returns the car year if it is both an integer and has 4 digits
    def get_year(self):
        if isinstance(self.year, int) and len(str(self.year)) == 4:
            return self.year
        else:
            return "ERROR"

    # Returns the make of the car if it is a string
    def get_make(self):
        if isinstance(self.make, str):
            return self.make
        else:
            return "ERROR"

    # Returns the model of the car if it is a string
    def get_model(self):
        if isinstance(self.model, str):
            return self.model
        else:
            return "ERROR"

    # Returns the color of the car if it is a string
    def get_color(self):
        if isinstance(self.color, str):
            return self.color
        else:
            return "ERROR"

    # Returns the style of the car if it is a string
    def get_style(self):
        if isinstance(self.style, str):
            return self.style
        else:
            return "ERROR"

    # Returns the number of cylinders if the value is an int
    def get_num_cylinders(self):
        if isinstance(self.num_cylinders, int):
            return self.num_cylinders
        else:
            return "ERROR"

    # Returns the mileage of a car if the value is an int
    def get_mileage(self):
        if isinstance(self.mileage, int):
            return self.mileage
        else:
            return "ERROR"

    # Returns the prev_title_num of a car if it is a string and has length of 8
    def get_prev_title_num(self):
        if isinstance(self.prev_title_num, str) and len(self.prev_title_num) == 8:
            return self.prev_title_num
        else:
            return "ERROR"

    # Returns the previous state if the value is a string
    def get_prev_state(self):
        if isinstance(self.prev_state, str):
            return self.prev_state
        else:
            return "ERROR"

    # Returns the type of purchase if Wholesale or Retail is passed in
    def get_typeofpurchase(self):
        if self.typeofpurchase == "Wholesale" or self.typeofpurchase == "Retail":
            return self.typeofpurchase
        else:
            return "ERROR"

    # Returns the purchase price if the value is an int
    def get_purchase_price(self):
        if isinstance(self.purchase_price, int):
            return self.purchase_price
        else:
            return "ERROR"

    # Loops through the repairs array and sums the cost of repairs
    def get_cost_of_repairs(self):
        cost_of_repairs = 0
        for cost in self.repairs:
            cost_of_repairs += cost.get_amount()
        return cost_of_repairs

    # Adds the cost of repairs to the purchase price to yield total cost
    def get_total_cost(self):
        total_cost = self.purchase_price
        total_cost += self.get_cost_of_repairs();
        return total_cost

    # Returns the date purchased if the value is in the correct format
    def get_date_purchased(self):
        pattern = r"^\d{4}-\d{2}-\d{2}$"  # Regular expression pattern for "YYYY-MM-DD"
        if re.match(pattern, self.date_purchased):
            return self.date_purchased
        else:
            return "ERROR"

    # Returns the customer name if the value is a string
    def get_customer_name(self):
        if isinstance(self.customer_name, str):
            return self.customer_name

    # Returns the comments if the value is a string
    def get_comments(self):
        if isinstance(self.comments, str):
            return self.comments
        else:
            return "ERROR"

