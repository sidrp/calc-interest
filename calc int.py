startAmt = simpleAmt = compAmt = float(input("Enter initial amount: "))
loanMonths = int(input("Enter Loan Duration In Months: "))
intPercent = float(input("Enter interest percentage: "))
# this will make an explanation of compound interest.
simpleInt = startAmt*(intPercent/100)
for i in range(0, loanMonths):
    compInterest = compAmt*(intPercent/100)
    simpleAmt = startAmt + (simpleInt*(i+1))
    compAmt = compAmt + compInterest
    print(f"Month: {i+1} Interest: {round(compInterest, 2)} Compound: {round(compAmt, 2)} Simple: {round(simpleAmt, 2)}")

print("\nInitial amount: $", round(startAmt, 2))
print(f"Compound amount after {loanMonths} months: ${round(compAmt, 2)}")
print(f"Simple amount after {loanMonths} months: ${round(simpleAmt, 2)}")
print("You are a rich person if you do this!")
    
