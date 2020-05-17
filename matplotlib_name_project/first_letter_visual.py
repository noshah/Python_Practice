import matplotlib.pyplot as plt

from first_letter import FirstLetterWalk



# Keep making new walks, as long as the program is active.
# Make a random walk.
rw = FirstLetterWalk()
# rw.get_step()
rw.draw_character()
rw.second_character_draw()
rw.third_character_draw()
rw.fourth_character_draw()
rw.fifth_character_draw()
rw.sixth_character_draw()
rw.seventh_character_draw()
rw.eight_character_draw()
rw.ninth_character_draw()
rw.tenth_character_draw()
rw.eleventh_character_draw()

plt.style.use('classic')
fig, ax = plt.subplots()


point_numbers = range(rw.num_points)
point_numbers_extra = range(rw.num_points_extra)



ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
           edgecolors='none', s=8)
# ax.plot(rw.x_values, rw.y_values, linewidth=2, c='lightblue')
# Emphasize the first and last points.
ax.scatter(0, 0, c='green', edgecolors='none', s=100)

# for second line.
ax.scatter(rw.x_values1, rw.y_values1, c=point_numbers, cmap=plt.cm.Blues,
           edgecolors='none', s=8)

# for third line.
ax.scatter(rw.x_values2, rw.y_values2, c=point_numbers, cmap=plt.cm.Blues,
           edgecolors='none', s=8)

# for fourth line.
ax.scatter(rw.x_values3, rw.y_values3, c=point_numbers, cmap=plt.cm.Blues,
           edgecolors='none', s=8)

# for fifth line.
ax.scatter(rw.x_values4, rw.y_values4, c=point_numbers, cmap=plt.cm.Blues,
           edgecolors='none', s=8)
# for sixth line.
ax.scatter(rw.x_values5, rw.y_values5, c=point_numbers, cmap=plt.cm.Blues,
           edgecolors='none', s=8)

# for seventh line.
ax.scatter(rw.x_values6, rw.y_values6, c=point_numbers, cmap=plt.cm.Blues,
           edgecolors='none', s=8)

# for eight line.
ax.scatter(rw.x_values7, rw.y_values7, c=point_numbers, cmap=plt.cm.Blues,
           edgecolors='none', s=8)

# for ninth line.
ax.scatter(rw.x_values8, rw.y_values8, c=point_numbers, cmap=plt.cm.Blues,
           edgecolors='none', s=8)

# for tenth line.
ax.scatter(rw.x_values9, rw.y_values9, c=point_numbers, cmap=plt.cm.Blues,
           edgecolors='none', s=8)

# for eleventh line.

ax.plot(rw.x_values10, rw.y_values10, c='blue', linewidth=5)
ax.scatter(rw.x_values10, rw.y_values10, c='red',
           edgecolors='none', s=100)

ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
ax.scatter(rw.x_values1[-1], rw.y_values1[-1], c='blue', edgecolors='none', s=100)
ax.scatter(rw.x_values2[-1], rw.y_values2[-1], c='orange', edgecolors='none', s=100)
ax.scatter(rw.x_values3[-1], rw.y_values3[-1], c='red', edgecolors='none', s=100)
ax.scatter(rw.x_values3[0], rw.y_values3[0], c='blue', edgecolors='none', s=100)
ax.scatter(rw.x_values4[-1], rw.y_values4[-1], c='orange', edgecolors='none', s=100)
ax.scatter(rw.x_values5[0], rw.y_values5[0], c='yellow', edgecolors='none', s=100)
ax.scatter(rw.x_values5[-1], rw.y_values5[-1], c='yellow', edgecolors='none', s=100)
ax.scatter(rw.x_values6[0], rw.y_values6[0], c='blue', edgecolors='none', s=100)
ax.scatter(rw.x_values6[-1], rw.y_values6[-1], c='orange', edgecolors='none', s=100)
ax.scatter(rw.x_values7[-1], rw.y_values7[-1], c='red', edgecolors='none', s=100)
ax.scatter(rw.x_values8[-1], rw.y_values8[-1], c='yellow', edgecolors='none', s=100)
ax.scatter(rw.x_values9[0], rw.y_values9[0], c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values9[-1], rw.y_values9[-1], c='yellow', edgecolors='none', s=100)


# remove the axes.
ax.get_xaxis().set_visible(True)
ax.get_yaxis().set_visible(True)


plt.show()

