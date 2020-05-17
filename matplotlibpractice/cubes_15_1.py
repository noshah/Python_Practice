import matplotlib.pyplot as plt


x_values = range(1, 5001)
y_values = [num**3 for num in x_values]

plt.style.use('dark_background')
fig, ax = plt.subplots()

# ax.scatter(x_values, y_values, c=(1.0, 0, 0), s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Oranges, s=10)
ax.set_title('Cubes Numbers', fontsize=24)
ax.set_xlabel('Values', fontsize=14)
ax.set_ylabel('Cubes Values', fontsize=14)
# ax.axis([0, 7, 0, 240])

plt.show()