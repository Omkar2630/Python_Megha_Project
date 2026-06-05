# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# data = {
#     "Month": ["Jan", "Feb", "Mar", "Apr"],
#     "Sales": [100, 15, 20, 180]
# }

# df = pd.DataFrame(data)

# sns.lineplot(x="Month", y="Sales", data=df)

# plt.title("Monthly Sales")
# plt.xlabel("Month")
# plt.ylabel("Sales")
# plt.show()



# import matplotlib.pyplot as plt
# import seaborn as sns 

# x = [1,2,3,4]
# y = [10,20,15,25]

# plt.plot(x, y)

# plt.title("Simple Graph")
# plt.xlabel("X Values")
# plt.ylabel("Y Values")

# plt.show()

import matplotlib.pyplot as plt

import numpy as np

categories =["I&V","SW","SoftCloud"]
values = np.array([29,25,30])
colors = ["red","yellow","blue"]
plt.pie(values, labels=categories,
        autopct="%1.1f%%")

plt.show()