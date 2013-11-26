#!/usr/bin/env python
# encoding: utf-8

"""
Author: zac 
"""

import sys
import getopt

class Point(object):

    def __init__(self, x, y, path= []):
        """
        Point object for knight_move

        :x: point x
        :y: point y
        :step: current step
        :returns: Point object

        """
        self.x = int(x)
        self.y = int(y)
        self.path = path

def go(n, start_point, end_point):
    
    n = int(n)
    board = [[0 for tmp_y in xrange(n)] for tmp_x in xrange(n)]
    routes = [start_point]
    rules = ((1, 2), (2, 1),(1, -2), (2, -1),(-1, -2), (-2, -1), (-2, 1), (-1, 2))
    while routes:
        bre_point = routes.pop(0)
        if bre_point.x == end_point.x and bre_point.y == end_point.y:
            return bre_point

        for step in rules:
            next_point = Point(bre_point.x + step[0], bre_point.y + step[1], [])
            if (0 <= next_point.x < n and 0 <= next_point.y < n and not board[next_point.y][next_point.x]):
                next_point.path = bre_point.path + [next_point]
                routes.append(next_point)
                board[next_point.y][next_point.x] = 1
                print board

if __name__ == '__main__':
    try:
        opts = getopt.getopt(sys.argv[1:], "n:x:y:")[0]
    except getopt.GetoptError:
        print "you input in a worng way , the good Example: python zac.py -n 10 -x 6 -y 5 "
        sys.exit(1)

    for opt, value in opts:
        if opt == "-n":
            n = int(value)
        elif opt == "-x":
            x = int(value)
        elif opt == "-y":
            y = int(value)

    result = go(n, Point(x, y), Point(n - 1, n - 1))
    if result:
        for point in result.path:
            print "({0.x},{0.y})".format(point)
    else:
        print "no way!"
