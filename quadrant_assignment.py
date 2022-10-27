#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Oct 2022
# This program identifies which quadrant the coordinate is in

import math


def main():
    # this function identifies which quadrant the coordinate is in

    # input
    user_input_x = int(
        input("Enter the x value of a coordinate (positive or negative): ")
    )
    print("")
    user_input_y = int(
        input("Enter the y value of a coordinate (positive or negative): ")
    )
    print("")

    # process
    if (user_input_x > 0) & (user_input_y > 0):
        print("These coordinates are in quadrant 1.".format(user_input_x, user_input_y))
    elif (user_input_x < 0) & (user_input_y > 0):
        print("These coordinates are in quadrant 2.".format(user_input_x, user_input_y))
    elif (user_input_x < 0) & (user_input_y < 0):
        print("These coordinates are in quadrant 3.".format(user_input_x, user_input_y))
    elif (user_input_x > 0) & (user_input_y < 0):
        print("These coordinates are in quadrant 4.".format(user_input_x, user_input_y))

        print("\nDone.")


if __name__ == "__main__":
    main()
