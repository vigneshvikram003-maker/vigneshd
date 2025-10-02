import pandas as avm
import matplotlib.pyplot as vicky
vk = avm.read_csv('gender_submission.csv')
print(vk.head())
Total_Pass = vk["Survived"].value_counts()
total = len(vk)
non_survivors = Total_Pass[0]  # Assuming 0 = non-survivor
perc = (non_survivors / total) * 100
print(f"Percentage of non-survivors is: {perc:.2f}%")
Total_Pass.plot(kind='bar', color=["blue", "green"])
vicky.xlabel("Survival Status (0 = No, 1 = Yes)")
vicky.ylabel("Number of People")
vicky.title("Survived Passengers in the Titanic Dataset")
vicky.xticks(rotation=0)
vicky.show()