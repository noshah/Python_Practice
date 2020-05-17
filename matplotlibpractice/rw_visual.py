import matplotlib.pyplot as plt

from random_walk import RandonWalk

flags =True

# Keep making new walks, as long as the program is active.
while flags:
    # Make a random walk.
    rw = RandonWalk()
    # rw.get_step()
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6))


    point_numbers = range(rw.num_points)

    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolors='none', s=8)
    # ax.plot(rw.x_values, rw.y_values, linewidth=2, c='lightblue')
    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # remove the axes.
    ax.get_xaxis().set_visible(True)
    ax.get_yaxis().set_visible(True)
    # print(rw.x_values)

    plt.show()


    while True:
        keep_running = input("Make another walk? (y/n):")
        if keep_running == 'y':
            break
        elif keep_running == 'n':
            flags = False
            break
        else:
            print("please, enter y/n.".upper())