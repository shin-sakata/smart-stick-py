import math
import matplotlib.pyplot as plt

def normalize_joystick(value):
    normalized_value = (value - 128) / 128
    logarithmic_value = math.copysign(math.log(abs(normalized_value) + 1, 2), normalized_value)
    return logarithmic_value

if __name__ == "__main__":
    # グラフ用のデータを生成する
    x_values = list(range(0, 256))
    y_values = [normalize_joystick(x) for x in x_values]
    # グラフを描画する
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, linewidth=2)
    plt.title("Joystick Response Curve (Logarithmic)")
    plt.xlabel("Input Value (0-255)")
    plt.ylabel("Output Value (-1 to 1)")
    plt.grid(True)
    plt.xlim(0, 255)
    plt.ylim(-1, 1)
    plt.xticks([0, 64, 128, 192, 255])
    plt.yticks([-1, -0.5, 0, 0.5, 1])
    plt.show()
