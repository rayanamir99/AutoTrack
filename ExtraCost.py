import re
class ExtraCost:
    # All initialized variables in ExtraCost represent different characteristics
    # of the associated purchased parts
    def __init__(self, date_of_purchase, description, amount, vendor):
        self.date_of_purchase = date_of_purchase
        self.description = description
        self.amount = amount
        self.vendor = vendor

# Returns the date of purchase if the value is in the correct format
    def get_date_of_purchase(self):
        pattern = r"^\d{4}-\d{2}-\d{2}$"  # Regular expression pattern for "YYYY-MM-DD"
        if re.match(pattern, self.date_of_purchase):
            return self.date_of_purchase
        else:
            return "ERROR"

# Returns the description of the ExtraCost if it is a string
    def get_description(self):
        if isinstance(self.description, str):
            return self.description
        else:
            return "ERROR"

# Returns the cost of the ExtraCost if it is an integer
    def get_amount(self):
        if isinstance(self.amount, int):
            return self.amount
        else:
            return "ERROR"

# Returns the vendor name if it is a string
    def get_vendor(self):
        if isinstance(self.vendor, str):
            return self.vendor
        else:
            return "ERROR"
