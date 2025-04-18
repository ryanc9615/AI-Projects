import numpy as np
import pandas as pd
import time

# Sample: 12 months x 4 accounts
#data = [
    #["4000", "Revenue",     125000],
    #["5000", "COGS",        -83000],
    #["6100", "Rent",        -12000],
    #["7100", "Utilities",   -3500],
    #["8000", "Interest",    -900],
    #["4000", "Revenue",     131000],
    #["5000", "COGS",        -79000],
    #["6100", "Rent",        -12000],
    #["7100", "Utilities",   -3400],
    #["8000", "Interest",    -920]
#]

# df = pd.DataFrame(data, columns=["Account", "Description", "Amount"])
#df.to_csv("trial_balance.csv", index=False)

trial_balance = np.loadtxt("trial_balance.csv", delimiter=",", skiprows=1, usecols=2, dtype=float)

start = time.time()
total_debits = trial_balance[trial_balance < 0].sum()
total_credits = trial_balance[trial_balance > 0].sum()
net_income = trial_balance.sum()
end = time.time()

print("\nVectorized version:")
print("Total Debits:", total_debits)
print("Total Credits:", total_credits)
print("Net Income:", net_income)
print("Elapsed Time:", end - start, "seconds")

start = time.time()
debit = 0
credit = 0
for val in trial_balance:
    if val < 0:
        debit += val
    else:
        credit += val
net_income = credit + debit
end = time.time()

print("Loop version:")
print("Total Debits:", debit)
print("Total Credits:", credit)
print("Net Income:", net_income)
print("Elapsed Time:", end - start, "seconds")

