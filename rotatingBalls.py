# -*- coding: cp1251 -*-
# Імпортуємо всю бібліотеку.
from visual import *


class Ball:
    def __init__(self, pos, trail = True):
        self.ball = sphere(pos = pos, make_trail = trail)
        self.main()

    def main(self):
        # Швидкість м'яча по координатах x, y та z.
        xSpeed = -10
        ySpeed = -5
        zSpeed = -7
        while 1:
            rate(25)
            self.ball.pos.x += xSpeed
            self.ball.pos.y += ySpeed
            self.ball.pos.z += zSpeed
            if self.ball.pos.x < -100 or self.ball.pos.x > 100:
                xSpeed = -xSpeed
            if self.ball.pos.y < -100 or self.ball.pos.y > 100:
                ySpeed = -ySpeed
            if self.ball.pos.z < -100 or self.ball.pos.z > 100:
                zSpeed = -zSpeed


for i in range(3):
    Ball(vector(i * 2, i * 2, i * 2))
