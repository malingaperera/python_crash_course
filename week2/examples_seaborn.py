import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")
print(type(flights))
print(flights.head())
sns.lineplot(data=flights, x="year", y="passengers", hue="month")
plt.show()
