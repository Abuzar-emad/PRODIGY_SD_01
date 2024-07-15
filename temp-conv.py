#("Temperature Conversion Program")



temp_value = float (input("Enter Temperature "))
orign_unit = input("Enter Mesasurement Unit ")

def cels_to_fah_and_kel(celsius):
    kelven = celsius + 273.15
    fahrenheit = (celsius * 9/5) +32
    print("Temperature in kelven = ",kelven)
    print("Temperature in fahrenheit = ",fahrenheit)

def fahr_to_cels_and_kel(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    kelven = (fahrenheit - 32) * 5/9+ 273.15
    print("Temperature in kelven = ",kelven)
    print("Temperature in celsius = ",celsius)

def kel_to_fah_and_cels(kelven):
    fahrenheit = (kelven - 273.15) * 9/5 + 32
    celsius = kelven - 273.15 
    print("Temperature in fahrenheit = ",fahrenheit)
    print("Temperature in celsius = ",celsius)



if orign_unit.lower() == "c":
    kel_fah = cels_to_fah_and_kel(temp_value)
elif orign_unit.lower() == "f":
    cels_kel = fahr_to_cels_and_kel(temp_value)
elif orign_unit.lower() == "k":
    fah_cels = kel_to_fah_and_cels(temp_value)
else :
    print("Pleace Enter c,f or k")
