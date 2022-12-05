import pygame
from math import sin, cos, pi
import stargen
import pygame.freetype

pygame.init()

map_font = pygame.freetype.Font("Perfect DOS VGA 437.ttf", 22)

def map_gen():
    starmap = {}
    for column in range(0, 11):
        starmap[column] = {}
        for map_row in range(0, 22):
            starmap[column][map_row] = stargen.Star(column, map_row)
    return starmap

def draw_regular_polygon(surface, color, vertex_count,
						 radius, position, width):
    n, r = vertex_count, radius
    x, y = position
    pygame.draw.polygon(surface, color, [
        (x + r * cos(2 * pi * i / n),
		 y + r * sin(2 * pi * i / n))
        for i in range(n)
    ], width)


def star_renderer (starmap, map_column, map_row):
                if map_column % 2 != 0:
                    if starmap[map_column][map_row].startype == "@":
                        pygame.draw.circle(screen, (0, 255, 0), (80*map_column*1.5, 140*map_row-60), 20, 0)
                    elif starmap[map_column][map_row].startype == "0":
                        pygame.draw.circle(screen, (0, 255, 0), (80*map_column*1.5, 140*map_row-60), 20, 2)
                    else:
                        pass
                    map_font.render_to(screen, (80*map_column*1.5-30, 140*map_row-10), starmap[map_column][map_row].names, (0, 255, 0))
                    map_font.render_to(screen, (80*map_column*1.5, 140*map_row-120), starmap[map_column][map_row].starport, (0, 255, 0))
                    if starmap[map_column][map_row].gas_giant == "*":
                        pygame.draw.circle(screen, (0, 255, 0), (80*map_column*1.5+30, 140*map_row-100), 6, 0)
                    else:
                        pass
                if map_column % 2 == 0:
                    if starmap[map_column][map_row].startype == "@":
                        pygame.draw.circle(screen, (0, 255, 0), (80*map_column*1.5, 140*map_row+8), 20, 0)
                    elif starmap[map_column][map_row].startype == "0":
                        pygame.draw.circle(screen, (0, 255, 0), (80*map_column*1.5, 140*map_row+8), 20, 2)
                    else:
                        pass
                    map_font.render_to(screen, (80*map_column*1.5-30, 140*map_row+54), starmap[map_column][map_row].names, (0, 255, 0))
                    map_font.render_to(screen, (80*map_column*1.5, 140*map_row-50), starmap[map_column][map_row].starport, (0, 255, 0))
                    if starmap[map_column][map_row].gas_giant == "*":
                        pygame.draw.circle(screen, (0, 255, 0), (80*map_column*1.5+30, 140*map_row-30), 6, 0)
                    else:
                        pass



screen = pygame.display.set_mode([1080, 1520])

pygame.display.set_caption('Cepheus Subsector Map')

starmap = map_gen()

screen.fill((0, 0, 0))
map_row = 1
map_column = 1
for map_column in range (1, 9):
    if map_column % 2 != 0:
        for map_row in range (1, 11):
            draw_regular_polygon(screen, (0, 255, 0), 6, 80, (80*map_column*1.5, 140*map_row-60), 2)
            star_renderer(starmap, map_column, map_row)
    if map_column % 2 == 0:
        for map_row in range (1, 11):
            draw_regular_polygon(screen, (0, 255, 0), 6, 80, (80*map_column*1.5, 140*map_row+8), 2)
            star_renderer(starmap, map_column, map_row)

pygame.display.update()
pygame.image.save(screen, "starmap.jpeg")
pygame.quit()