import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]


plt.style.use('seaborn')
# we can also use multiple styple in our graph.
# And the result are mindbogling.
# plt.style.use('seaborn-dark')
# plt.style.use('dark_background')


fig, ax = plt.subplots()
# fis, ay = plt.subplots()
# ax.scatter(25, 25)
# ax.scatter(3, 3, s=300)
ax.scatter(input_values, squares)
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axis.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
# ax.tick_params(axis='x', labelsize=14)
ax.tick_params(axis='both', labelsize=14)
# ax.plot(ds)
# ay.plot(squares)

plt.show()
