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

x_time = arange(1, 10, 1)  # (start, end, increment)
y_time = arange(11, 20, 1)
z_time = arange(21, 30, 1)
#all_time = array([x_time, y_time, z_time])
all_time = array([x_time, x_time, x_time])
#all_time = array(arange(1, 33, 1))
other_time = array([y_time, y_time, y_time])


def tolerance(value):
    return [value - 2, value + 2.5, 0.5]  # test tolerance +/- 2.0


drop_rest_1_tolerance = array(
    [arange(*tolerance(drop_rest_1_m[0])),
     arange(*tolerance(drop_rest_1_m[1])),
     arange(*tolerance(drop_rest_1_m[2]))]
)

drop_rest_2_tolerance = array(
    [arange(*tolerance(drop_rest_2_m[0])),
     arange(*tolerance(drop_rest_2_m[1])),
     arange(*tolerance(drop_rest_2_m[2]))]
)

left_turn_1_tolerance = array(
    [arange(*tolerance(left_turn_1_m[0])),
     arange(*tolerance(left_turn_1_m[1])),
     arange(*tolerance(left_turn_1_m[2]))]
)

left_turn_2_tolerance = array(
    [arange(*tolerance(left_turn_2_m[0])),
     arange(*tolerance(left_turn_2_m[1])),
     arange(*tolerance(left_turn_2_m[2]))]
)

right_turn_tolerance = array(
    [arange(*tolerance(right_turn_m[0])),
     arange(*tolerance(right_turn_m[1])),
     arange(*tolerance(right_turn_m[2]))]
)

drop_rest_1_plot = array([[j,k] for i in range(len(all_time)) for j in all_time[i] for k in drop_rest_1_tolerance[i]])

drop_rest_2_plot = array([[j,k] for i in range(len(all_time)) for j in other_time[i] for k in drop_rest_2_tolerance[i]])

# left_turn_1_plot = array([[j,k] for i in range(len(all_time)) for j in all_time[i] for k in left_turn_1_tolerance[i]])
#
# left_turn_2_plot = array([[j,k] for i in range(len(all_time)) for j in all_time[i] for k in left_turn_2_tolerance[i]])
#
# right_turn_plot = array([[j,k] for i in range(len(all_time)) for j in all_time[i] for k in right_turn_tolerance[i]])

#all_plot = array([drop_rest_1_plot, drop_rest_2_plot, left_turn_1_plot, left_turn_2_plot, right_turn_plot])

print("test plot")
plt.scatter(drop_rest_1_plot[:,0], drop_rest_1_plot[:,1])
#plt.scatter(drop_rest_2_plot[:,0], drop_rest_2_plot[:,1])
print("goodbye")