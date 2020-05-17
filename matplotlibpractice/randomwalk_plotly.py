from random import choice

class RandomWalk:
    """in the class we are trying to get x and y co-ordinates."""
    def __init__(self, num_points=5000):
        """we define some useful attribute throught code."""
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]


    def get_step(self):
        """in this method we do some calculation for x and y co-ordinates."""
        # first calculation for x-axis.
        x_direction = choice([-1, 1])
        x_distance = choice([0, 1, 2, 3, 4])
        self.x_step = x_direction * x_distance

        # second calculation for y-axis.
        y_direction = choice([-1, 1])
        y_distance = choice([0, 1, 2, 3, 4])
        self.y_step = y_direction * y_distance

    def fill_walk(self):
        """we get the the co-ordeinates."""
        while len(self.x_values) < self.num_points:

            self.get_step()

            #check the points if it is then continue the loop.
            if self.x_step == 0 and self.y_step == 0:
                continue

            # now we get the co-ordinates.
            x = self.x_values[-1] + self.x_step
            y = self.y_values[-1] + self.y_step

            self.x_values.append(x)
            self.y_values.append(y)








