name1 = "yoki"
height_m1 = 2     # Here are the varibles "1, 2 and 3" the buliding blocks of the code we go back to these multiple times over the course of the code
weight_kg1 = 90

name2 = "yoki sister" 
height_m2 = 1.8          # I want to calculate the bmi and calculate if sommeone is overweight
weight_kg2 = 70

name3 = "sam"
height_m3 = 2.5
weight_kg3 = 160


def bmi_calculator(name, height_m, weight_kg):  # This function took 3 arguments "name, height in meter, and weight in kilo grams"
    bmi = weight_kg / (height_m ** 2)    # This means: body mass index = weright in kilo grams divided by height in meters squared 2" so for yoki we do "90 / 2 square root of 2 which is 4 = 22.5"
    print("bmi: ")   # This is what is typed in the console "bmi:" since this is in "" is will be typed out as a string
    print(bmi)       # Then under the "bmi:" the actually "bmi" is typed which for yoki is 22.5
    if bmi < 25:     
        return name + " is not overweight "
    else:
        return name + " is overweight "


result1 = bmi_calculator(name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)


print(result1)
print(result2)
print(result3)