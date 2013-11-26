import unittest
from zac import Point, go


class ZacTest(unittest.TestCase):
    """
    test for go method
    """

    def test_point(self):
        self.assertEqual(Point(0, 0).path, [])

    def test_go(self):
        """
        test go method
        """
        route = [(p.x, p.y) for p in go(10, Point(0, 0), Point(9, 9)).path]
        self.assertEqual(route, [(1, 2), (2, 4), (3, 6),
                                 (5, 7), (7, 8), (9, 9)])

unittest.main()
