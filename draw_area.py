from turtle_draw import BrachioGraphTurtle
bgt = BrachioGraphTurtle(
    inner_arm=7.8, shoulder_centre_angle=-55, shoulder_sweep=170,
    outer_arm=8,  elbow_centre_angle=90, elbow_sweep=170,
    window_size=800
)
bgt.draw_grid()
bgt.draw_outline()
bgt.draw_arcs()
bgt.draw_arms()
input("Press Enter to continue...")
