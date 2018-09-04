# class practice
# a nut has attributes: a name, price, size ('S' or 'L')
class Nuts:
    count = 0 #count how many nuts objects are created by the user.
    def __init__(self, name, size, price, quantity):
        Nuts.count += 1 #increment count by 1 for every object created
        self.name = name
        self.size = size
        self.price = price
        self.quantity = quantity

        # tell user the object is initialized
        print("Chosen nut is initialized!")

# what can be the methods for our nut class?
# play with it and improvise

    def inform(self):
        print("This nut is called: {}".format(self.name))
        print("{}\'s size is: {}".format(self.name, self.size))
        print("{} is priced at {} and its size is: {}".format(self.name, self.price, self.size))
        print("Available quantity for {}: {}".format(self.name, self.quantity))

    def inv_checker(self, qty_bought):
        if qty_bought > self.quantity:
            print("We don\'t have that many {} at the moment.".format(self.name))
            print("Sorry for the inconvenience")
        else:
            self.quantity = self.quantity - qty_bought
        print("Now you have {} {}\'s left.".format(self.quantity, self.name))

    def change_Size(self, new_size):
        print("The size for {} was {}. It is being updated to its new size.".format(self.name, self.size))
        self.size = new_size
        print("now the size is {}".format(self.size))

almond = Nuts('Almond', 'L', 8.99, 24)

almond = almond.change_Size('M')

# create a new instance from Nuts class
# cashew = Nuts('')



# print(almond.size)
# cashew = Nuts('Cashew', 'S', 6.49, 18)
# print(Nuts.count) # check how many instances exist.
# print(almond.price)
# print(almond.quantity)

# print(almond.inv_checker(22))
# print(almond.quantity)




# write a function that

# almond = Nuts('Almond', 'L', 8.99, 24)
# almond.inform()
# print(almond)
# print(type(almond))




    # def remove_from_inventory(self, item):
    #     count -= 1 #to decrease count by 1 for removed item
    #
    # def create_inventory(self, inv):
    #     # create a dictionary to count the items



"""
Time module test will be run on this test.py file
Main purpose: enchancing programming skills
Questions: How to convert messy time to a more structured data
"""

#converting timestamps
"""
import time

my_time = time.time()
my_structured_time = time.gmtime(my_time)
my_hour = my_structured_time.tm_hour
my_month = my_structured_time.tm_mon
print(my_time)
print(my_structured_time)
print(my_hour)
print(my_month)
"""
#datetime class
# import datetime

# current_time = datetime.datetime.utcnow()
# structured_year = current_time.year
# current_month = current_time.month
# today = current_time.day
#print(structured_year)
#print(current_month)

# diff  = datetime.timedelta(days=1)
# future = today + diff
# past = today - diff
# print(future)
# print(past)

# aday = datetime.datetime(year=2020, month=11, day=5)
# prettier_day = aday.strftime("%b %d, %Y")
# print(prettier_day)
