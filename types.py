import typing as t

from pydantic import BaseModel


# TODO: think about scaling


class PlanetConfig(BaseModel):
    name: str
    vx: int  # initial speed on the x axis (m/s)
    vy: int  # initial speed on the y axis (m/s)
    radius: int  # in meters
    mass: int  # in kg
    color: t.List[int]  # [R, G, B]


class GameConfig(BaseModel):
    scale: float  # all distances will be divided on it (only for graphics)
    width: int = 1280  # window width
    height: int = 720  # window height
    fps: int = 30  # frames per second
    time_step: int = 60 * 60  # time skipped between two frames (in seconds)
    planets: t.List[PlanetConfig]  # planets list
