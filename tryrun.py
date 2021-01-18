from brachiograph import BrachioGraph
bg = BrachioGraph(
    inner_arm=9, outer_arm=9,
    bounds=(-8, 3, 8, 15),
    servo_1_centre=1695, servo_2_centre=1480
)
bg.grid_lines(interpolate=400, both=True)
