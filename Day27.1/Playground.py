
# Unlimited arguments:
def add (*args):
    user_sum = 0
    for n in args:
        user_sum += n

# print(add(2,10,29))

# KeyWord arguments

def calculate(n,**kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2,add=3,multiply=5)

class Car:
    def __init__(self,**kw):
        self.make = kw.get("make") # .get avoids errors if the kw is not defined when the function is called
        self.model = kw.get("model")


my_car = Car(make="Nissan")
print(my_car.model)











