cost = int(input("Enter the cost of the laptop: "))
allowance =20000
sf = 0.1
r = 0.5
months = 1
monthly_savings = allowance*sf
def calculate_months(cost,allowance,monthly_savings,r,months):
    while True:
        intrest = monthly_savings * r
        monthly_savings += intrest
        months += 1
        if (monthly_savings >= cost):
            break
    return months



print(calculate_months(cost,allowance,monthly_savings,r,months))
print(monthly_savings-cost)
