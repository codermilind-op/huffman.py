

class ExpenseTracker:
    #class attribute
    expense_version_tracker=0.1
    def __init__(self,track_category,original_balance,budget):
        #instance/object Attributes
        self.tracking_category=track_category
        self.original_balance=original_balance
        self.tracker_budget=budget
        #instance method
    def get_original_balance(self):
        return self.original_balance
    def check_balance(self,limit=1000):
        if self.tracker_budget>=limit:
            return True
        else:
            return "Your opening balance is less than limit"
    @staticmethod
    def convert_amount(amount):
            return float(amount)
    @classmethod
    def get_attributes_fromstring(cls,diary_entry:str):
        tracking_category,opening_balance,tracker_budget=diary_entry.split(" ")
        return ExpenseTracker(tracking_category.capitalize(),
                             cls.convert_amount(opening_balance),
                             cls.convert_amount(tracker_budget))
ClassObject=ExpenseTracker.get_attributes_fromstring("shopping 100 5000")
ClassObject.__dict__