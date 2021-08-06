import numpy as np
def convolution(f,g):
    size = len(f) + len(g) - 1
    size = 1 << (size - 1).bit_length()
    f = np.fft.rfft(f,size)
    g = np.fft.rfft(g,size)
    f *= g
    f = np.fft.irfft(f,size)
    return np.rint(f).astype(np.int64)

s = input()
t = input()
n = len(s)
m = len(t)

s1 = np.array(list(map(int,s)))
s2 = 1 - s1
t1 = np.array(list(map(int,reversed(t))))
t2 = 1 - t1

a = convolution(s1,t2) + convolution(s2,t1)
print(np.min(a[m-1:n]))