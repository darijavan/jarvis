from typing import List


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Jarvis:
    @staticmethod
    def orientation(p: Point, q: Point, r: Point):
        val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2

    @staticmethod
    def envconvex(points: List[Point]):
        n = len(points)

        if n < 3:
            return
        env = []
        l = 0
        for i in range(1, n):
            if(points[i].x < points[l].x):
                l = i
        p = l
        while True:
            env.append(points[p])
            q = (p + 1) % n

            for i in range(1, n):
                if Jarvis.orientation(points[p], points[i], points[q]) == 2:
                    q = i
            p = q
            if p == l:
                break
        for temp in env:
            print("(", temp.x, ", ", temp.y, ")")
