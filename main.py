from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
polygons = []
transform = new_matrix()

# add_polygon(polygons, 0, 0, 0, 100, 100, 0, 200, 200, 0)
# add_polygon(polygons, 0, 0, 0, 100, 100, 100, 200, 200, 200)
# draw_polygons(polygons, screen, color)
# display(screen)
parse_file( 'script', edges, polygons, transform, screen, color )