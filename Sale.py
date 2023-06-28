import re
from datetime import date
from dateutil.relativedelta import relativedelta
from ExtraCost import ExtraCost
from Vehicle import Vehicle

import math

class Sale:
    # All initialized variables in Sale represent different characteristics
    # of the associated sale
    def __init__(self, selling_price, cash_down, payment_rate, sold_date):
        self.selling_price = selling_price
        self.cash_down = cash_down
        self.payment_rate = payment_rate
        self.sold_date = sold_date

# If the selling price is an integer then return
    def get_selling_price(self):
        if isinstance(self.selling_price, int):
            return self.selling_price
        else:
            return "ERROR"

# If the cash down is an integer then return
    def get_cash_down(self):
        if isinstance(self.cash_down, int):
            return self.cash_down
        else:
            return "ERROR"

# Calculate the amount financed by finding the difference between selling price and cash down
    def get_amount_financed(self):
        return self.selling_price - self.cash_down

# If the payment rate is an integer then return
    def get_payment_rate(self):
        if isinstance(self.payment_rate, int):
            return self.payment_rate
        else:
            return "ERROR"

# If the sold date is a datetime object then return
    def get_sold_date(self):
        if isinstance(self.sold_date, date):
            return self.sold_date
        else:
            return "ERROR"

# Return the sold date incremented by a month
    def get_first_payment_date(self):
        self.sold_date += relativedelta(months=1)
        return self.sold_date

# Calculate the final payment date by calculating the number of payments and then
# incrementing the months by this number
    def get_final_payment_date(self):
        num_payments = math.ceil(self.get_amount_financed()/self.payment_rate)
        self.sold_date += relativedelta(months=num_payments)
        return self.sold_date

# Since the final payment will likely be uneven, the remainder of the amount financed
# divided by the payment rate will be the final payment
    def get_final_payment_amt(self):
        remainder = self.get_amount_financed() % self.payment_rate
        return remainder

"""
x = Sale(10000, 1000, 500, date(2020, 4, 17))


print(x.get_selling_price())
print(x.get_cash_down())
print(x.get_amount_financed())
print(x.get_sold_date())
print(x.get_first_payment_date())
print(x.get_final_payment_date())
print(x.get_final_payment_amt())

"""
