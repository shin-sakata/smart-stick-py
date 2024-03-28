import math
import matplotlib.pyplot as plt

def normalize_joystick(value, scale=2):
    value = max(0, min(value, 255))
    normalized_value = (value - 128) / 128 * scale
    logarithmic_value = math.copysign(math.log(abs(normalized_value) + 1), normalized_value)
    return logarithmic_value / math.log(scale + 1)

if __name__ == "__main__":
    scales = [0.5, 1, 1.5, 2]
    x_values = list(range(0, 256))

    plt.figure(figsize=(8, 6))
    for scale in scales:
        y_values = [normalize_joystick(x, scale=scale) for x in x_values]
        plt.plot(x_values, y_values, linewidth=2, label=f'scale={scale}')

    plt.title("Joystick Response Curves with Different Scales")
    plt.xlabel("Input Value (0-255)")
    plt.ylabel("Output Value (-1 to 1)")
    plt.grid(True)
    plt.xlim(0, 255)
    plt.ylim(-1, 1)
    plt.xticks([0, 64, 128, 192, 255])
    plt.yticks([-1, -0.5, 0, 0.5, 1])
    plt.legend()
    plt.show()
