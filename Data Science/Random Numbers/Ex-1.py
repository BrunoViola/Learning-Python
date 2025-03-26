import numpy as np

print(np.random.rand())

np.random.seed(123)
print(np.random.rand())
print(np.random.rand())

np.random.seed()
print(np.random.randint(0,2))