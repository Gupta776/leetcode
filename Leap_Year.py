#Write a function to determine if a given year is a leap year or not.

def leap_year_validation(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
        
year = 2024
if leap_year_validation(year):
    print(f"{year} - leap year") 
else:
    print(f"{year} - not a leap year.")
