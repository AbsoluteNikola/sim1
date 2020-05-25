import typing as t
import pygame


class Planet:
    def __init__(
            self,
            name: str,
            mass: int,
            radius: int,
            x: int = 0,
            y: int = 0,
            vx: int = 0,
            vy: int = 0,
            color=t.List[int],
            **kwargs
    ):
        self._name = name
        self._mass = mass
        self._radius = radius
        self._x = x
        self._y = y
        self._vx = vx
        self._vy = vy
        self._color = color

    def draw(self, surface):
        pygame.draw.circle(
            surface,
            self._color,
            (self._x, self._y),
            self._radius
        )

    def move(self, time_step: int, scale):
        self.x += self.vx * time_step / scale
        self.y += self.vy * time_step / scale

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def mass(self):
        return self._mass

    @property
    def radius(self):
        return self._radius

    @property
    def vx(self):
        return self._vx

    @vx.setter
    def vx(self, value):
        self._vx = value

    @property
    def vy(self):
        return self._vy

    @vy.setter
    def vy(self, value):
        self._vy = value

    @property
    def name(self):
        return self._name
