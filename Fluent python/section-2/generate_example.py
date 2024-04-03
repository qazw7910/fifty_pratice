import numpy as np
from time import perf_counter as pc

floats = np.random.rand(10000000)

np.savetxt('floats-10M-lines.txt', floats)



