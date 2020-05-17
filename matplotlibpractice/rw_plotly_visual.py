from plotly import *
from plotly import offline

from randomwalk_plotly import RandomWalk

rw = RandomWalk()
rw.fill_walk()

flag = True

while flag:
    # loop is running until flag is false.

    data = [graph_objs.Scatter(x=rw.x_values, y=rw.y_values)]

    x_axis_config = {'title': 'x-axis'}
    y_axis_config = {'title': 'y-axis'}


    my_layout = graph_objs.Layout(title='Random Walk through 5000 points.',
                       xaxis=x_axis_config, yaxis=y_axis_config)

    offline.plot({'data': data, 'layout': my_layout}, filename='random_walk_5000.html')

    while True:
        keep_running = input('do want to restart the graph y/n: ')
        if keep_running == 'y':
            break
        elif keep_running == 'n':
            flag = False
            break
        else:
            print('Please, Enter y/n.'.upper())




