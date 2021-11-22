counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1]=="Denver":
    print(counties[1])

#What is the temperature?
temperature = int(input("What is the temperature outside?"))
if temperature > 80:
    print("Turn the AC On")
else:
    print("Open the windows.")

#What is the score?
grade = int(input("What is your grade?"))

#Determine the grade.
if grade >=90:
    print("Your grade is an 'A'")
else:
    if grade >=80:
        print("Your grade is a 'B'")
    else:
        if grade >=70:
            print("Your grade is a 'C'")
        else:
            if grade >=60:
                print("Your grade is a 'D'")
            else:
                print("Your grade is an 'F'")

#What is your score?

score = int(input('What is your score?'))

#Determine the grade

if score >=90:
    print("Your grade is an 'A'")
elif score >=80:
    print("Your grade is a 'B'")
elif score >=70:
    print("Your grade is a 'C'")
elif score >=60:
    print("Your grade is a 'D'")
else:
    print("Your grade is an 'F'")

#Membership
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

#AND statement
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

#Or Statement
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Neither Arapahoe nor El Paso is not in the list of counties.")

for county in counties:
    print(county)

counties_dict = {'Arapahoe': 422829, 'Denver': 463353, 'Jeffersion': 432438}
for county in counties_dict.keys():
    print(county)

for county in counties_dict.values():
    print(county)

for county in counties_dict:
    print(counties_dict[county])
    