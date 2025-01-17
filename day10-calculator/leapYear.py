def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    check_4 = year % 4
    check_100 = year % 100
    check_400 = year % 400
    print(f"{check_4} {check_100} {check_400}")
    
    if check_4 == 0 and check_100 == 0 and check_400 == 0:
        return "Leap year"
    else:
        return "Non Leap year"
    #return f"{check_4} {check_100} {check_400}"
    
print(f"Year 2000 is a {is_leap_year(2000)}")
print(f"Year 2020 is a {is_leap_year(2020)}")
print(f"Year 2100 is a {is_leap_year(2100)}")

# https://www.gigacalculator.com/calculators/leap-year-calculator.php
# 2020 is a leap year

# Here the output shown is
# 0 0 0
# Year 2000 is a Leap year
# 0 20 20
# Year 2020 is a Non Leap year
# 0 0 100
# Year 2100 is a Non Leap year

# TODO: Fix issue - 2020 is a leap year, but showing it as non leap year


