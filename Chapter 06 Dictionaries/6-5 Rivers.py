rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'mississippi',
}

for river, loc in rivers.items():
    print(f"\nThe {river.title()} river is in {loc.title()}.")
print("\nThe following rivers are contained in the dictionary:")
for river in rivers.keys():
    print(f"{river.title()}")
print("\nThe following locations are contained in the dictionary:")
for loc in rivers.values():
    print(f"{loc.title()}")

###########################################################################################
# Answer:
# rivers = {
#     'nile': 'egypt',
#     'mississippi': 'united states',
#     'fraser': 'canada',
#     'kuskokwim': 'alaska',
#     'yangtze': 'china',
#     }

# for river, country in rivers.items():
#     print(f"The {river.title()} flows through {country.title()}.")

# print("\nThe following rivers are included in this data set:")
# for river in rivers.keys():
#     print(f"- {river.title()}")

# print("\nThe following countries are included in this data set:")
# for country in rivers.values():
#     print(f"- {country.title()}")
