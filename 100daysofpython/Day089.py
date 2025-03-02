'''
Day 89: Generate fractals
Write a program to generate fractals.
'''

import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(width, height, zoom=1, x_offset=0, y_offset=0, max_iter=100):
    x = np.linspace(-2.5/zoom +zoom + x_offset, 1.5/zoom + x_offset, width)
    y = np.linspace(-2/zoom + y_offset, 2/zoom + y_offset, height)
    X,Y = np.meshgrid(x, y)
    C = X +1j * Y

    Z = np.zeros_like(C, dtype=np.complex128)
    mandelbrot_set = np.zeros(C.shape, dtype=np.uint8)

    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        Z[mask] = Z[mask] ** 2 + C[mask]
        mandelbrot_set[mask] = i

    return mandelbrot_set

def plor_mandelbrot():
    width, height = 800,600
    fractal = mandelbrot(width, height, zoom=1, max_iter=200)


    plt.figure(figsize=(10,7))
    plt.imshow(fractal, cmap="inferno", extent=[-2.5,1.5,-2,2])
    plt.colorbar(label='Iterations')
    plt.title("Mandelbrot Set")
    plt.xlabel("Real Axis")
    plt.ylabel("Imaginary Axis")
    plt.show()


if __name__ == "__main__":
    plor_mandelbrot()