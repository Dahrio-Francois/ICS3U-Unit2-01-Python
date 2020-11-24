#!/usr/bin/env python3

# Created by: Dahrio
# Created on: November 2020
# This program calculates the area and perimeter of a circle
#     With radius of 15mm

import math


def main():
    # this function calculates area and perimeter
    print("If a circle has the radius of 15mm")
    print("")
    print("Area is {}mm^2".format(math.pi*15**2))
    print("Perimeter is {}mm".format(2*math.pi*15))


if __name__ == "__main__":
    main()
