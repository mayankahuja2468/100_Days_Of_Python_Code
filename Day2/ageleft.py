age=int(input("What is your current age?"))
age_left = 90-age
weeks_left = age_left*52
months_left = age_left*12
days_left=age_left*365.25

print(f"You have {days_left} days, {weeks_left} weeks, amd {months_left} months left")
