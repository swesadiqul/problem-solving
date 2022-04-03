##calculate your bmi
##by@sadiqul islam

name = str(input("Enter the name here:"))
height_m =int(input("Enter the height_m here:"))
weight_kg =int(input("Enter the weight_kg here:"))

bmi=weight_kg/(height_m ** 2)
print("bmi:")
print(bmi)
if bmi<25:
    print(name)
    print("is not overweight")
    print("It's a good position.")
else:
    if bmi ==25:
        print(name)
        print("is not overweight but as soon as posible you should diode control.")
    else:
        print(name)
        print("""is overweight.It's a very big problem for health.Now you should diode control.
              On the other hand I think that,You should take physical exercise everyday since in the morning and afternoon.""")

