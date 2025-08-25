age=int(input("what is your age?\n"))
years_remaining=90-age
months_remaining=years_remaining*12
weeks_remaining=years_remaining*52
days_remaining=years_remaining*365
print(f"you have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left")