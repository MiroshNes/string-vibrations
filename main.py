# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()  # создаем фигуру и координатную ось

x = np.arange(0, np.pi, 0.01)
line, = ax.plot(x, np.sin(x))  # ссылка на данные графика


def animate(i):
    line.set_ydata(np.sin(x + i / 50))  # update the data.
    return line,

phasa = np.arange(0, 4*np.pi, 0.1)

ani = animation.FuncAnimation(
    fig, animate, frames=phasa, interval=20, blit=True, save_count=50)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# writer = animation.FFMpegWriter(
#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()