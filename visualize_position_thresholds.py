"""
Main module

This will help me visualize tolerances for hand position for the Playground Express Bike Glove.
"""
from numpy import arange, array
import matplotlib.pyplot as plt

# use plot(), fill(), and/or scatter()
# time_matrix = arange(0, 11, .05) (start, end, increment)

# Resting hand is X, Y = 0, Z = 9
# Left turn is X = 9, Y, Z = 0
# Right turn is X = 0, Y = 9, Z = 0
# xyz = brg
#
# drop rest 1: -7.5, -4, 5
# drop rest 2: -3, -2, 9
# left turn 1: -9, 0, 0
# left turn 2: -6, 6, 0
# test tolerance +/- 2.0
#
# for the plot, x, y and z are separate lines where t is the x-axis and the x, y or z value represented on the y-axis
# 5 plots: drop rest 1, drop rest 2, left 1, left 2, right
#
drop_rest_1_m = array([-7.5, -4, 5])
drop_rest_2_m = array([-3, -2, 9])
left_turn_1_m = array([-9, 0, 0])
left_turn_2_m = array([-6, 6, 0])
right_turn_m = array([0, 9, 0])
time_matrix = arange(0, 51, 1)  # (start, end, increment)


def tolerance(value):
    return [value - 2, value + 2.5, 0.5]  # test tolerance +/- 2.0


drop_rest_1_tolerance = array(
    [[arange(*tolerance(drop_rest_1_m[0]))],
     [arange(*tolerance(drop_rest_1_m[1]))],
     [arange(*tolerance(drop_rest_1_m[2]))]]
)

drop_rest_2_tolerance = array(
    [[arange(*tolerance(drop_rest_2_m[0]))],
     [arange(*tolerance(drop_rest_2_m[1]))],
     [arange(*tolerance(drop_rest_2_m[2]))]]
)

left_turn_1_tolerance = array(
    [[arange(*tolerance(left_turn_1_m[0]))],
     [arange(*tolerance(left_turn_1_m[1]))],
     [arange(*tolerance(left_turn_1_m[2]))]]
)

left_turn_2_tolerance = array(
    [[arange(*tolerance(left_turn_2_m[0]))],
     [arange(*tolerance(left_turn_2_m[1]))],
     [arange(*tolerance(left_turn_2_m[2]))]]
)

right_turn_tolerance = array(
    [[arange(*tolerance(right_turn_m[0]))],
     [arange(*tolerance(right_turn_m[1]))],
     [arange(*tolerance(right_turn_m[2]))]]
)

drop_rest_1_plot =  # enumerate?

print('test')
