x = 0
while x<=5:
    print(x)
    x= x+1

counties_tuple = ("Arapahoe", "Denver", "Jefferson")

counties_dict = {"Arapahoe":422829, "Denver":463353, "Jefferson":432438}

for county in counties_dict.keys():
    print(county)

for county in counties_dict:
    print(counties_dict[county])

for county, voters in counties_dict.items():
    print(county," county has", voters, "registered voters")
    
voting_date = [{"county":"Arapahoe", "registered voters":422829},
                {"county":"Denver", "registered voters": 463353},
                {"county":"Jefferson", "registered voters": 432438}]

for counties_dict in voting_date:
    print(counties_dict)

for i in range(len(voting_date)):
    print(voting_date[i])

for county_dict in voting_date:
    for value in county_dict.values():
        print(value)

for county,voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters")