import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_json("user_study.json")

df = df[['user_id', 'minutes']].groupby('user_id').sum()



fig = plt.figure()

ax = fig.add_subplot(1,1,1)

ax.set_title("StudyData")

ax.set_xlabel("User ID")

ax.set_ylabel("Study Time")

ax.plot(df)

fig.show()
