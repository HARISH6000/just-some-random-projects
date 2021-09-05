def bmi(h, w):
    bmi = w/((h/100)**2)
    print("your BMI is", bmi)

#h1 = int(input("Enter your height in meter:"))
#w1 = int(input("Enter your weight in kg:"))
h1 = int(input("Enter your height in cm:"))
w1 = int(input("Enter your weight in kg:"))

bmi(h1, w1)
