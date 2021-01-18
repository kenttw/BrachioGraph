servo_1_angle_pws = [[-90.0, 2494],
                     [-72.0, 2294],
                     [-54.0, 2094],
                     [-36.0, 1884],
                     [-18.0, 1654],
                     [0,1433],
                     [18.0, 1223],
                     [36.0, 1033],
                     [54.0, 853],
                     [54.0, 853],
                     [72.0, 679],
                     [90.0, 504], ]

servo_2_angle_pws = [[-90.0, 2438],
                     [-72.0, 2238],
                     [-54.0, 2048],
                     [-36.0, 1849],
                     [-18.0, 1633],
                     [0.0, 1423],
                     [18, 1223],
                     [36, 1033],
                     [54, 833],
                     [72, 633],
                     [90, 500], ]

bounds = [-8, 3, 8, 13]


from brachiograph import BrachioGraph

bg = BrachioGraph(

    inner_arm=7.8,
    outer_arm=8,
    # servo_1_centre=1433,  # shoulder motor centre pulse-width
    # servo_2_centre=1423,  # elbow motor centre pulse-width
    servo_1_angle_pws=servo_1_angle_pws,  # pulse-widths for various angles
    servo_2_angle_pws=servo_2_angle_pws,
    servo_1_degree_ms=10,  # milliseconds pulse-widthx` per degree
    servo_2_degree_ms=10,  # reversed for the mounting of the elbow servo
    arm_1_centre=-55, # 如果有給　servo_1_angle_pws　這個參數沒有作用
    arm_2_centre=90,
    # hysteresis_correction_1=0,  # hardware error compensation
    # hysteresis_correction_2=0,
    bounds=bounds,  # the maximum rectangular drawing area
    wait=.05,
    virtual_mode=False,
    pw_up=500,  # pulse-widths for pen up/down
    pw_down=1500,
    servo1_pin=0,
    servo2_pin=1,

)