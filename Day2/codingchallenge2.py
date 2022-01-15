
#height = float(input("enter your height in m: "))
#weight = float(input("enter your weight in kg: "))

#print("The bmi is "+weight/(height*height))
#    print("The bmi is "+weight/(height*height))
#    TypeError: can only concatenate str (not "float") to str



height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

print("The bmi is "+ str(weight/(height*height)))