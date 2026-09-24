
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


import pandas as pd
data =[10,20,30,40,50]
s=pd.Series(data)
print(s)


import pandas as pd
data =[100,50,80,60]
fruits=["Apple","Banana","Mango","Orange"]
s=pd.Series(data,index=fruits)
print(s)




import pandas as pd
data = {
"Name":["Rahul","priya","Aman"],
"Age":[20,21,19],
"Marks":[85,92,78]

}
df =pd.DataFrame(data)
print(df)



#1.Number of rows and columns
print(df.shape)

#2.Column names
print(df.columns)

#3.Data types
print(df.dtypes)

#4.First 2 rows
print(df.head(2))


import pandas as pd
df = pd.DataFrame({
 "Name":["Rahul","priya","Aman"],
 "Age":[20,21,19],
"Marks":[85,92,78]
})

df["Marks"]