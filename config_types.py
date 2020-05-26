import typing as t

from pydantic import BaseModel


class PlanetConfig(BaseModel):
    name: str
    vx: int = 0  # initial speed on the x axis (m/s)
    vy: int = 0  # initial speed on the y axis (m/s)
    radius: int  # in meters
    mass: int  # in kg
    color: t.List[int]  # [R, G, B]
    scale: float  # radius wil be multiplied on it (only for rendering)
    draw_path: bool = False
    # coordinates on monitor, should be only on main obj in the system
    # all other objects calculates from range and angle to the main obj
    x: t.Optional[int] = None  # in pixels
    y: t.Optional[int] = None  # in pixels
    angle: t.Optional[float] = None  # in degrees [0, 360]
    dist: t.Optional[int] = None  # in meters


class GameConfig(BaseModel):
    scale: float  # all distances will be divided on it (only for graphics)
    width: int = 1280  # window width
    height: int = 720  # window height
    fps: int = 30  # frames per second
    time_step: int = 60 * 60  # time skipped between two seconds (in seconds)
    planets: t.List[PlanetConfig]  # planets list
