from random import choice


class FirstLetterWalk:
    """A class to genrate random walks."""
    def __init__(self, num_points=5000, num_points_extra=10000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        self.num_points_extra = num_points_extra
        self.increase_points = 20

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

        self.first_line()
        self.second_line()
        self.third_line()
        self.fourth_line()




    def first_line(self):
        """calculation for plotting points"""

        # Decide which direction to go and how far to go in that direction.
        x_direction = [0]
        x_distance = [0]
        self.x_step = x_direction[-1] * x_distance[-1]

        y_direction = [2]
        y_distance = [2]
        self.y_step = y_direction[-1] * y_distance[-1]

    def second_line(self):
        """calculation for plotting points"""

        # Decide which direction to go and how far to go in that direction.
        x_direction = [0.01]
        x_distance = [1]
        self.x_step = x_direction[-1] * x_distance[-1]

        y_direction = [2]
        y_distance = [2]
        self.y_step = y_direction[-1] * y_distance[-1]

    def third_line(self):
        """calculation for plotting points"""

        # Decide which direction to go and how far to go in that direction.
        x_direction = [0]
        x_distance = [0]
        self.x_step = x_direction[-1] * x_distance[-1]

        y_direction = [2]
        y_distance = [2]
        self.y_step = y_direction[-1] * y_distance[-1]

    def fourth_line(self):
        """calculation for plotting points"""

        # Decide which direction to go and how far to go in that direction.
        x_direction = [0.01]
        x_distance = [1]
        self.x_step = x_direction[-1] * x_distance[-1]

        y_direction = [0]
        y_distance = [0]
        self.y_step = y_direction[-1] * y_distance[-1]


    def draw_character(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.y_values) < self.num_points:

            self.first_line()
            # Reject moves that go nowhere.
            if self.x_step == 0 and self.y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + self.x_step
            y = self.y_values[-1] + self.y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def second_character_draw(self):
        """Calculate all the points in the walk."""
        self.x_values1 = [self.x_values[-1]]
        self.y_values1 = [self.y_values[-1]]
        # Keep taking steps until the walk reaches the desired length.
        while len(self.y_values1) < self.num_points:

            self.second_line()
            # Reject moves that go nowhere.
            if self.x_step == 0 and self.y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values1[-1] + self.x_step
            y = self.y_values1[-1] - self.y_step

            self.x_values1.append(x)
            self.y_values1.append(y)

    def third_character_draw(self):
        """Calculate all the points in the walk."""
        self.x_values2 = [self.x_values1[-1]]
        self.y_values2 = [self.y_values1[-1]]
        # Keep taking steps until the walk reaches the desired length.
        while len(self.y_values2) < self.num_points:

            self.third_line()
            # Reject moves that go nowhere.
            if self.x_step == 0 and self.y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values2[-1] + self.x_step
            y = self.y_values2[-1] + self.y_step

            self.x_values2.append(x)
            self.y_values2.append(y)

    def fourth_character_draw(self):
        """Calculate all the points in the walk."""
        self.x_values3 = [self.x_values2[0] + self.increase_points]
        self.y_values3 = [0]
        # Keep taking steps until the walk reaches the desired length.
        while len(self.y_values3) < self.num_points:

            self.second_line()
            # Reject moves that go nowhere.
            if self.x_step == 0 and self.y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values3[-1] + self.x_step

            y = self.y_values3[-1] + self.y_step

            self.x_values3.append(x)
            self.y_values3.append(y)

    def fifth_character_draw(self):
        """Calculate all the points in the walk."""
        self.x_values4 = [self.x_values3[-1]]
        self.y_values4 = [self.y_values3[-1]]
        # Keep taking steps until the walk reaches the desired length.
        while len(self.y_values4) < self.num_points:

            self.second_line()
            # Reject moves that go nowhere.
            if self.x_step == 0 and self.y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values4[-1] + self.x_step

            y = self.y_values4[-1] - self.y_step

            self.x_values4.append(x)
            self.y_values4.append(y)

    def sixth_character_draw(self):
        """Calculate all the points in the walk."""
        self.x_values5 = [self.x_values3[int(len(self.x_values3)/2)]]
        self.y_values5 = [self.y_values3[int(len(self.y_values3)/2)]]
        # Keep taking steps until the walk reaches the desired length.
        while len(self.y_values5) < self.num_points:

            self.fourth_line()
            # Reject moves that go nowhere.
            if self.x_step == 0 and self.y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values5[-1] + self.x_step

            y = self.y_values5[-1] + self.y_step

            self.x_values5.append(x)
            self.y_values5.append(y)

    def seventh_character_draw(self):
        """Calculate all the points in the walk."""
        self.x_values6 = [self.x_values4[-1] + self.increase_points]
        self.y_values6 = [0]
        # Keep taking steps until the walk reaches the desired length.
        while len(self.y_values6) < self.num_points:

            self.first_line()
            # Reject moves that go nowhere.
            if self.x_step == 0 and self.y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values6[-1] + self.x_step

            y = self.y_values6[-1] + self.y_step

            self.x_values6.append(x)
            self.y_values6.append(y)

    def eight_character_draw(self):
        """Calculate all the points in the walk."""
        self.x_values7 = [self.x_values6[-1]]
        self.y_values7 = [self.y_values6[-1]]
        # Keep taking steps until the walk reaches the desired length.
        while len(self.y_values7) < self.num_points:

            self.second_line()
            # Reject moves that go nowhere.
            if self.x_step == 0 and self.y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values7[-1] + self.x_step

            y = self.y_values7[-1] - self.y_step

            self.x_values7.append(x)
            self.y_values7.append(y)

    def ninth_character_draw(self):
        """Calculate all the points in the walk."""
        self.x_values8 = [self.x_values7[-1]]
        self.y_values8 = [self.y_values7[-1]]
        # Keep taking steps until the walk reaches the desired length.
        while len(self.y_values8) < self.num_points:

            self.first_line()
            # Reject moves that go nowhere.
            if self.x_step == 0 and self.y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values8[-1] + self.x_step

            y = self.y_values8[-1] + self.y_step

            self.x_values8.append(x)
            self.y_values8.append(y)

    def tenth_character_draw(self):
        """Calculate all the points in the walk."""
        self.x_values9 = [self.x_values8[0] + self.increase_points]
        self.y_values9 = [self.y_values8[0]]
        # Keep taking steps until the walk reaches the desired length.
        while len(self.y_values9) < self.num_points:

            self.first_line()
            # Reject moves that go nowhere.
            if self.x_step == 0 and self.y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values9[-1] + self.x_step

            y = self.y_values9[-1] + self.y_step

            self.x_values9.append(x)
            self.y_values9.append(y)


    def eleventh_character_draw(self):
        """Calculate all the points in the walk."""
        self.x_values10 = [259.95999999994467, 285, 301, 310, 298, 287.5, 259.95999999994467]
        self.y_values10 = [0, 1517, 4140, 9998, 14799, 18203, 19996]









