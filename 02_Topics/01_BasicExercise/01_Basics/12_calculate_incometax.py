"""
Exercise 12: Calculate income tax
Calculate income tax for the given income by adhering to the rules below

Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20
Expected Output:

For example, suppose the income is 45000, and the income tax payable is

10000*0% + 10000*10%  + 25000*20% = $6000.
"""

income = 45000
tax_payable = 0
print("Given income", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    # no tax on first 10,000
    x = income - 10000
    # 10% tax
    tax_payable = x * 10 / 100
else:
    # first 10,000
    tax_payable = 0

    # next 10,000 10% tax
    tax_payable = 10000 * 10 / 100

    # remaining 20%tax
    tax_payable += (income - 20000) * 20 / 100

print("Total tax to pay is", tax_payable)