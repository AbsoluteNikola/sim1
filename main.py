import copy
import sys
import pygame
import decimal
import math

from config_types import *
from planet import Planet


def init_planets(game_config: GameConfig) -> t.List[Planet]:
    main_obj = None
    for planet_conf in game_config.planets:
        planet_conf.radius = planet_conf.radius / game_config.scale * planet_conf.scale
        if planet_conf.x is not None:
            main_obj = planet_conf
        else:
            planet_conf.dist /= game_config.scale

    if main_obj is None or main_obj.x is None or main_obj.y is None:
        raise RuntimeError("No main object with x and y coordinates")

    planets = [Planet(**main_obj.dict())]
    for planet_conf in game_config.planets:
        if planet_conf is main_obj:
            continue
        angle = planet_conf.angle / 180 * math.pi
        planet_conf.x = main_obj.x + planet_conf.dist * math.cos(angle)
        planet_conf.y = main_obj.y + planet_conf.dist * math.sin(angle)
        planets.append(Planet(**planet_conf.dict()))

    return planets


def calc_attraction(planet1: Planet, planet2: Planet, planet3: Planet, game_config: GameConfig) -> None:
    """Third planet should be a copy of one of the planets"""
    # TODO: serve collision
    G = 6.7e-11  # The gravitational constant G

    dx = planet1.x - planet2.x
    dy = planet1.y - planet2.y
    r = math.sqrt(dx ** 2 + dy ** 2) * game_config.scale
    f = G * (planet1.mass * planet2.mass) / (r**2)
    theta = math.atan2(dy, dx)
    fx = math.cos(theta) * f
    fy = math.sin(theta) * f
    planet3.vx += fx / planet2.mass * game_config.time_step
    planet3.vy += fy / planet2.mass * game_config.time_step


def run(surface: pygame.Surface, game_config: GameConfig):
    planets = init_planets(game_config)
    clock = pygame.time.Clock()
    while True:
        clock.tick(game_config.fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        surface.fill((0, 0, 0))
        next_gen = copy.deepcopy(planets)
        for p1 in planets:
            for p2, p3 in zip(planets, next_gen):
                if p1 is p2:
                    continue
                calc_attraction(p1, p2, p3, game_config)
        planets = next_gen

        for planet in planets:
            planet.move(game_config.time_step, game_config.scale)
            print(f"{planet.name} ({planet.x}, {planet.y})")
            planet.draw(surface)
        print('---')
        pygame.display.update()


def main():
    if len(sys.argv) < 2:
        print("First argument should be path to config")
        sys.exit(1)

    game_config = GameConfig.parse_file(sys.argv[1])
    game_config.time_step /= game_config.fps
    # decimal.getcontext().prec = 30
    pygame.init()

    surface = pygame.display.set_mode(
        (game_config.width, game_config.height)
    )
    run(surface, game_config)


if __name__ == '__main__':
    main()