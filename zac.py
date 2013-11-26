#!/usr/bin/env python
# encoding: utf-8

"""
Author: zac
"""

import sys
import getopt


class Point(object):

    def __init__(self, x, y, path=[]):
        """
        x: point x
        y: point y
        path: the way go the point
        """
        self.x = int(x)
        self.y = int(y)
        self.path = path  # process


def go(n, start_point, end_point):
    n = int(n)
    # use to set where has been to
    matrix = [[0 for a in range(n)] for b in range(n)]
    routes = [start_point]
    rules = ((1, 2), (2, 1), (1, -2), (2, -1),
             (-1, -2), (-2, -1), (-2, 1), (-1, 2))  # go way
    #m = 0
    while routes:
        bre_point = routes.pop(0)  # get bre_point to test go to end_point
        if bre_point.x == end_point.x and bre_point.y == end_point.y:
            #print m
            return bre_point

        for step in rules:
            #m+= 1
            next_point = Point(bre_point.x + step[0],
                               bre_point.y + step[1], [])
            if (0 <= next_point.x < n and 0 <= next_point.y < n
                    and not matrix[next_point.x][next_point.y]):
                # if point in matrix and did not to go ,that is a odds
                next_point.path = bre_point.path + [next_point]
                routes.append(next_point)
                matrix[next_point.x][next_point.y] = 1  # set

if __name__ == '__main__':
    try:
        opts = getopt.getopt(sys.argv[1:], "n:x:y:")[0]
    except getopt.GetoptError:
        print "input worng,the good Example: python zac.py -n 10 -x 6 -y 5"
        sys.exit(1)

    for opt, value in opts:
        if opt == "-n":
            n = int(value)
            if n < 2:
                print "n must be greater than 2"
                sys.exit(1)
        elif opt == "-x":
            x = int(value)
            if x > n:
                print "x must be less than n"
                sys.exit(1)
        elif opt == "-y":
            y = int(value)
            if y > n:
                print "y must be less than y"
                sys.exit(1)

    result = go(n, Point(x, y), Point(n - 1, n - 1))
    if result:
        for point in result.path:
            print "({0.x},{0.y})".format(point)
    else:
        print "no way!"
