from mario import tri, frame_rate

import numpy as np
import matplotlib.pyplot as plt


xs = np.linspace(0, 2 * frame_rate / 440, 10_000)
ys = [tri(440)(x) for x in xs]

# plt.plot(xs, ys)


from mario import E5, e_freq

xs = np.linspace(0, frame_rate / e_freq, 10_000)
ys = [E5(x) for x in xs]

plt.plot(xs, ys)
