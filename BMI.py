print("welcome to the BMI calculator")
weight=float(input("enter your weight in kg: \n"))
height=float(input("enter your height in cm: \n"))
BMI=weight/height**2*10000
print(f"your BMI is:{BMI}")