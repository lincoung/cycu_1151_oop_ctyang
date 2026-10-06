import matplotlib.pyplot as plt
import math 
import numpy as np

def func1(x):
    """Return a list of y values using y = sin(x)."""
    y = []
    for value in x:
        y.append(math.sin(value))
    return y


def draw(x, y):
    """Plot matching lists of x and y values."""
    if len(x) != len(y):
        raise ValueError("x and y must have the same length")

    plt.figure()
    plt.plot(x, y, marker=".")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    points=np.linspace(-3,3,50)
    x = points  # Generate x values
    y = func1(x)
    print(y)
    draw(x, y)
    