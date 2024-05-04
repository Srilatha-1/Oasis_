Height=float(input("Enter the height in cm:"))
Weight=float(input("enter the weight in kg:"))

BMI = weight/(height/100)**2
print("Your Body Mass Index is :",BMI)
if BMI<=18.5:
      print("OOPS! You are underweight:")
elif BMI<=25.0:
      print("Awesome! You are healthy:")
elif BMI<=40.0:
      print("You are over weight:")
else:
      print("you are obese:")
