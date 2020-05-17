import numpy as np
import matplotlib.pyplot as plt

from matdie import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()
width = 0.35
men_std = [0, 3, 4, 1, 2]
# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for roll_num in range(50_0000)]
print(results)
print(len(results))

max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]
print(frequencies)

# Visualize the results.
x_values = list(range(2, max_result+1))

fig, ax = plt.subplots()

ax.bar(x_values, frequencies, width)

ax.tick_params(axis='both', which='major', labelsize=14)

ax.set_title("Results of rolling a both D6 500000 times", fontsize=30)
ax.set_xlabel("Result", fontsize=14)
ax.set_ylabel("Frequncy of Result", fontsize=14)
ax.get_xaxis().set_visible(True)
ax.get_yaxis().set_visible(True)
plt.show()