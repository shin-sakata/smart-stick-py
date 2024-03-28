def interpretDS4(data):
    left_stick = {"x": data[1], "y": data[2]}
    right_stick = {"x": data[3], "y": data[4]}

    dpad_value = data[5] & 0b1111
    dpad = {
        "up": dpad_value in (7, 0, 1),
        "right": dpad_value in (1, 2, 3),
        "down": dpad_value in (3, 4, 5),
        "left": dpad_value in (5, 6, 7),
    }

    square = (data[5] & 0x10) != 0
    cross = (data[5] & 0x20) != 0
    circle = (data[5] & 0x40) != 0
    triangle = (data[5] & 0x80) != 0

    l1 = (data[6] & 0x01) != 0
    r1 = (data[6] & 0x02) != 0
    l2 = (data[6] & 0x04) != 0
    r2 = (data[6] & 0x08) != 0
    share = (data[6] & 0x10) != 0
    options = (data[6] & 0x20) != 0
    l3 = (data[6] & 0x40) != 0
    r3 = (data[6] & 0x80) != 0

    ps = (data[7] & 0x01) != 0
    touchpad = (data[7] & 0x02) != 0

    l2_trigger = data[8]
    r2_trigger = data[9]

    return {
        "sticks": {"left": left_stick, "right": right_stick},
        "dpad": dpad,
        "buttons": {
            "square": square,
            "cross": cross,
            "circle": circle,
            "triangle": triangle,
            "l1": l1,
            "r1": r1,
            "l2": l2,
            "r2": r2,
            "share": share,
            "options": options,
            "l3": l3,
            "r3": r3,
            "ps": ps,
            "touchpad": touchpad,
        },
        "triggers": {"l2": l2_trigger, "r2": r2_trigger},
    }
