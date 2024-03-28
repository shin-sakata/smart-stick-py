from time import perf_counter
from dualshock4 import interpretDS4
import vgamepad as vg
from response_curve import normalize_joystick

# start_time = 0

counter = 0 # 1000hz で動作させている場合、1000回の処理で 1 秒間になる
gamepad = vg.VX360Gamepad()

def handler(data):
    ds4 = interpretDS4(data)
    global counter
    # global counter
    # global start_time
    # if counter == 0:
    #     start_time = perf_counter()
    update_xbox_controller(ds4)
    counter += 1
    if counter == 1000:
        counter = 0
    # if counter == 1000:
    #     end_time = perf_counter()
    #     execution_time = end_time - start_time
    #     # 平均実行時間を ms で表示
    #     print(f"Average execution time: {execution_time / 1000 * 1000} ms")
    #     counter = 0
    

def update_xbox_controller(ds4):
    global counter
    global gamepad

    # D-Padの状態を更新
    if ds4['dpad']['up']:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)

    if ds4['dpad']['down']:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)

    if ds4['dpad']['left']:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)

    if ds4['dpad']['right']:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)

    # ボタンの状態を更新
    if ds4['buttons']['cross']:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)

    if ds4['buttons']['circle']:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)

    if ds4['buttons']['square']:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)

    if ds4['buttons']['triangle']:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)

    if ds4['buttons']['l1']:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)

    if ds4['buttons']['r1']:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)

    if ds4['buttons']['l3']:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)

    if ds4['buttons']['r3']:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)

    if ds4['buttons']['options']:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)

    if ds4['buttons']['share'] or ds4['buttons']['touchpad']:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)

    if ds4['buttons']['ps']:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE)

    gamepad.left_joystick_float(x_value_float=(ds4['sticks']['left']['x'] - 128) / 128, y_value_float=-(ds4['sticks']['left']['y'] - 128) / 128)
    gamepad.right_joystick_float(x_value_float=(ds4['sticks']['right']['x'] - 128) / 128, y_value_float=-(ds4['sticks']['right']['y'] - 128) / 128)

    gamepad.left_trigger_float(value_float=ds4['triggers']['l2'] / 255)
    gamepad.right_trigger_float(value_float=ds4['triggers']['r2'] / 255)

    # 変更を適用
    gamepad.update()
