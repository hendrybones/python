planet=input("which planet are you from?")
print(planet)

def currency_converter(rate,euros):
    dollars=euros*rate
    return dollars
r=input("enter your rate")
e=input("enter your euros")
print(currency_converter(float(r),float(e)))
