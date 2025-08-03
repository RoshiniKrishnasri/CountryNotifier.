from countryinfo import CountryInfo

# Ask user to enter the country name
country_name = input("Enter the name of the country: ")
a = CountryInfo(country_name)

# Alternate spellings
info_1 = a.alt_spellings()
print("Alternate Spellings:", info_1)

# Capital
info_2 = a.capital()
print("Capital:", info_2)

# Languages
info_3 = a.languages()
print("Languages:", info_3)

# Timezones
info_4 = a.timezones()
print("Time Zones:", info_4)

# Currency
info_5 = a.currencies()
print("Currency:", info_5)

# Area
info_6 = a.area()
print("Area:", info_6)

# Borders
info_7 = a.borders()
print("Borders:", info_7)

# Calling code
info_8 = a.calling_codes()
print("Calling Code:", info_8)

# Wikipedia link
info_9 = a.wiki()
print("Wikipedia Link:", info_9)

# All info
info_10 = a.info()
print("\n--- Complete Country Info ---")
for key, value in info_10.items():
    print(f"{key} : {value}")

