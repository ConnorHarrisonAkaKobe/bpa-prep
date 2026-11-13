# Name: Connor Harrison
# Date: 11/11/26
# Program: Step 2 - Variables and Input
# Description: a program that prints a weekly pay stub with taxes taken out, plus yearly totals.

# Input: the employee name, hourly pay rate, and hours worked this week
employee_name = input("Employee Name: ")
rate = float(input("Hourly Pay: "))
hours = float(input("Hours worked: "))

# Constant
FEDERAL_TAX_RATE = 0.10
STATE_TAX_RATE = 0.035
SOCIAL_SECURITY_RATE = 0.062
MEDICARE_RATE = 0.0145
WEEKS_PER_YEAR = 52

# Processing: Calculating pay and tax
gross_pay = rate * hours
federal_tax = gross_pay * FEDERAL_TAX_RATE
state_tax = gross_pay * STATE_TAX_RATE
social_tax = gross_pay * SOCIAL_SECURITY_RATE
medicare_tax = gross_pay * MEDICARE_RATE
total_taken_out = federal_tax + state_tax + social_tax + medicare_tax
net_pay = gross_pay - total_taken_out
percent_kept = net_pay / gross_pay * 100
yearly_gross = gross_pay * WEEKS_PER_YEAR
yearly_net = net_pay * WEEKS_PER_YEAR

# Output: yearly payment added together
print()
print("Employee name:", employee_name)
print(f"Hourly pay rate: {rate:.2f}")
print("Hours worked this week:", hours)
print()
print("=" * 32)
print("PAY STUB:", employee_name)
print("=" * 32)
print("Hours worked:     ", hours)
print(f"Hourly rate:       ${rate:.2f}")
print(f"Gross pay:        ${gross_pay:.2f}")
print("-" * 32)
print(f"Federal tax (10%): ${federal_tax:.2f}")
print(f"State tax (3.5%): ${state_tax:.2f}")
print(f"Social Security: ${social_tax:.2f}")
print(f"Medicare:       ${medicare_tax:.2f}")
print(f"Total taken out: ${total_taken_out:.2f}")
print("-" * 32)
print(f"NET PAY:         ${net_pay:.2f}")
print("=" * 32)
print(f"You keep {percent_kept:.1f}% of what you earn.")
print(f"Yearly gross: ${yearly_gross:.2f}")
print(f"Yearly net:   ${yearly_net:.2f}")
