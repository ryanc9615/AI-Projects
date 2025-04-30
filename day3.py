import numpy as np
import pandas as pd

df = pd.DataFrame({
    "Category": ["A", "B", "C", "D", "E", "F"],
    "Amount": [15000, 20000, 4000, 6000, 7000, 10000],
    "Quarter": [1, 3, 3, 2, 1, 4]
})

## Needs review if amount is greater than 10000
is_large = np.where(df["Amount"] > 10000, "Needs Review", "OK")
# Assign the mask to a new column called "Status"
df.loc[:,"Status"] = is_large

print(df)

# Summarise the data
summary = df.groupby("Status").agg({
    "Amount": ["count", "sum"]
})
print(summary)