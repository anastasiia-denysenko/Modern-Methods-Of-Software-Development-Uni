import sort
import matplotlib.pyplot as plt
from numpy import pi, sin, arctan
m = random.sample(range(-1000, 1000), 10)
quick_sort(m, 0, len(m)-1)
def f(m):
    return arctan(m)+(sin(m)**2)/pi
plt.plot(m, f(m))
plt.show()
