from plotly.graph_objs import Bar, Layout
from plotly import offline

from threedie import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = [die_1.roll() + die_2.roll() + die_3.roll() for num in range(10_00_00)]
print(results)
print(len(results))

max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequncies = [results.count(value) for value in range(3, max_result+1)]
print(frequncies)
print(len(frequncies))

x_values = list(range(3, max_result+1))
data = [Bar(x=x_values, y=frequncies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequncy of Result'}
my_layout = Layout(title='Results of rolling thrice time D6 dice 100000 times', xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_d6.html')





