import matplotlib.pyplot as plt


ages = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
plt.bar(range(len(ages)), ages)
plt.xlabel('Age Groups')
plt.ylabel('Number of People')
plt.title('Distribution of Ages in a Population')
plt.xticks(range(len(ages)), ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5', 'Group 6', 'Group 7', 'Group 8', 'Group 9', 'Group 10'])
plt.show()


