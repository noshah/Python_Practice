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


print(rw.x_values[-1], rw.y_values[-1])
print(rw.x_values1[-1], rw.y_values1[-1])
print(rw.x_values2[-1], rw.y_values2[-1])
print(rw.x_values3[-1], rw.y_values3[-1])
print(rw.x_values4[-1], rw.y_values4[-1])
print(f'first graph x axis : {rw.x_values}, \nfirst graph y axis : {rw.y_values}')
print(f'second graph x axis : {rw.x_values1}, \nsecond graph y axis : {rw.y_values1}')
print(f'third graph x axis : {rw.x_values2}, \nthird graph y axis : {rw.y_values2}')
print(f'fourth graph x axis : {rw.x_values3}, \nfourth graph y axis : {rw.y_values3}')
print(f'fifth graph x axis : {rw.x_values4}, \nfifth graph y axis : {rw.y_values4}')
print(f'sixth graph x axis : {rw.x_values5}, \nsixth graph y axis : {rw.y_values5}')



print(f'\n\n len of x- axixs:{rw.y_values3[int(len(rw.y_values3)/2)]}')

print(rw.y_values3[2500])


print('\n\n\n\nnew')
print(f'tenth graph x axis : {rw.x_values10}, \nsixth graph y axis : {rw.y_values10}')
print(f'what i want:')
print(f'start: {rw.x_values9[0], rw.y_values9[0]}')
print(f'end: {rw.x_values9[-1], rw.y_values9[-1]}')

print(f'the answer is:')

print(f'start: {rw.x_values10[0], rw.y_values10[0]}')
print(f'end: {rw.x_values10[-1], rw.y_values10[-1]}')
print(f'start: {rw.x_values9[int(len(rw.x_values9)/2)], rw.y_values9[int(len(rw.y_values9)/2)]}')
