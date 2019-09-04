print("Electricity bill estimator 2.0")
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

# cents_per_kwh = float(input("Enter cents per kwh: "))
choice_of_tarrif_rate = input("Which tariff? 11 or 31: ")

if choice_of_tarrif_rate == 11:
    choice_of_tarrif_rate = TARIFF_11
else:
    choice_of_tarrif_rate = TARIFF_31

daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
estimated_bill = choice_of_tarrif_rate * daily_use * billing_days
print("Estimated bill: {:,.2f}".format(estimated_bill))
