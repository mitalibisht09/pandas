
import pandas as pd
print(pd.__version__)

import pandas as pd

# Dictionary se DataFrame banate hain
data = {
    "Name": ["Aman", "Priya", "Rohit", "Simran"],
    "Age": [21, 22, 20, 23],
    "City": ["Delhi", "Mumbai", "Pune", "Delhi"]
}

df = pd.DataFrame(data)

print(df)
print("\nColumns:", df.columns.tolist())
print("\naverage of age:", df["Age"].mean())
print("\nstudents lives in delhi:\n", df[df["City"] == "Delhi"])