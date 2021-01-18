from my_brachiograph import bg

import time





def fit_and_transforme(lines,boounds):
    min_x = 100000000
    max_x = -100000000
    min_y = 100000000
    max_y = -100000000


    for sp in lines:
        for point in sp:
            x,y = point
            if x > max_x: max_x = x
            if y > max_y: max_y = y

            if x < min_x: min_x = x
            if y < min_y: min_y = y

    width = max_x - min_x
    height = max_y - min_y

    width_scale = (bounds[2] - bounds[0])/width
    height_scale = (bounds[3] - bounds[1])/height

    new_lines = []

    for sp in lines:
        temp = []
        for point in sp:
            x,y = point
            x = x*width_scale + bounds[0]
            y = y*height_scale + bounds[1]
            temp.append((x,y))
        new_lines.append(temp)
    return new_lines


from linedraw import *
bounds = [-5, 3, 5, 13]

bg.plot_file(filename='./boy3.json',bounds=bounds,interpolate=400)
