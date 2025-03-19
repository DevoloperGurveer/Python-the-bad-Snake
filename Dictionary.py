country_code={'India':'0007',
              'Horses':'0069',
              'New Zaeland':'0010',
              'England':'00420'}
print("Country codefor India-")
print(country_code.get("India", "not found"))
print("Country code for Horses \-")
print(country_code.get("Horses", "not found"))
print("Country code for England-")
print(country_code.get("England", "not found"))
print("Country code for New Zaeland-")
print(country_code.get("New Zaeland", "not found"))