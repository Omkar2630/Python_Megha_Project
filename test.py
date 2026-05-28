import pandas as pd


data = [10, 20, 30, 40]

s = pd.Series(data)

print(s)


data = {
    "Name": ["Om", "Raj", "Amit"],
    "Age": [22, 23, 24]
}

df = pd.DataFrame(data)

print(df)


df = pd.read_excel("testcases.xlsx")

print(df)

pass_count = len(df[df["Result"] == "PASS"])

print("Total PASS:", pass_count)

