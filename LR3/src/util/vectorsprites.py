import pygame
import sys
import os
import math
import random
from math import *
from .vector2d import *
from .geometry import *


class VectorSprite:

    def __init__(self, position, heading, pointlist, angle=0, color=(255, 255, 255)):
        self.position = position
        self.heading = heading
        self.angle = angle
        self.vAngle = 0
        self.pointlist = pointlist
        self.color = color
        self.ttl = 25

    def rotate_and_transform(self):
        new_point_list = [self.rotate_point(point) for point in self.pointlist]
        self.transformed_point_list = [
            self.translate_point(point) for point in new_point_list]

    def draw(self):
        self.rotate_and_transform()
        return self.transformed_point_list

    def translate_point(self, point):
        newPoint = [point[0] + self.position.x, point[1] + self.position.y]
        return newPoint

    def move(self):
        self.position.x = self.position.x + self.heading.x
        self.position.y = self.position.y + self.heading.y
        self.angle = self.angle + self.vAngle

    def rotate_point(self, point):
        new_point = []
        cosVal = math.cos(radians(self.angle))
        sinVal = math.sin(radians(self.angle))
        new_point.append(point[0] * cosVal + point[1] * sinVal)
        new_point.append(point[1] * cosVal - point[0] * sinVal)

        new_point = [int(point) for point in new_point]
        return new_point

    def scale(self, point, scale):
        new_point = [point[0] * scale, point[1] * scale]
        new_point = [int(point) for point in new_point]
        return new_point

    def collides_with(self, target):
        if self.boundingRect.colliderect(target.boundingRect):
            return True
        else:
            return False

    def check_polygon_collision(self, target):
        for i in range(0, len(self.transformed_point_list)):
            for j in range(0, len(target.transformed_point_list)):
                p1 = self.transformed_point_list[i - 1]
                p2 = self.transformed_point_list[i]
                p3 = target.transformed_point_list[j - 1]
                p4 = target.transformed_point_list[j]
                p = calculate_intersect_point(p1, p2, p3, p4)
                if p != None:
                    return p

        return None


class Point(VectorSprite):

    pointlist = [(0, 0), (1, 1), (1, 0), (0, 1)]

    def __init__(self, position, heading, stage):
        VectorSprite.__init__(self, position, heading, self.pointlist)
        self.stage = stage
        self.ttl = 30

    def move(self):
        self.ttl -= 1
        if self.ttl <= 0:
            self.stage.remove_sprite(self)

        VectorSprite.move(self)
