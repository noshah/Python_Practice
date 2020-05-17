import matplotlib.pyplot as plt


x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
# this below style usefull for background of graph.
plt.style.use('seaborn')
# plt.style.use('seaborn-dark')
# plt.style.use('dark_background')
# this subplots funtion use for show blank graph.
fig, ax = plt.subplots()
# scatter show indiviual points.
# ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)
# Using a Colormap.
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes.
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

# show() funtion use for show all ploted graph or blank graph.
plt.savefig('squares_plot_1.png', bbox_inches='tight')
plt.show()
