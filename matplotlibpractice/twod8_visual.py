from plotly.graph_objs import Bar, Layout
from plotly import offline

from die_8 import Die

die_1 = Die()
die_2 = Die()

results = [die_1.roll() + die_2.roll() for num in range(100_000)]
print(results)

max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]
print(frequencies)

x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]


x_axis_config = {'title': 'Sum of both D8 rolling.', 'dtick': 1}
y_axis_config = {'title': 'Frequncy of Result'}

my_layout = Layout(title='Results of rolling both D8 100000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')