import cmath
import imageio
import cv2
import numpy as np
from math import log, ceil
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt


def omega(p, q):
    return cmath.exp((2.0 * cmath.pi * 1j * q) / p)


def pad(lst):
    k = 0

    while 2**k < len(lst):
        k += 1
    return np.concatenate((lst, ([0] * (2 ** k - len(lst)))))


def fft(x):
    n = len(x)

    if n == 1:
        return x

    Feven, Fodd = fft(x[0::2]), fft(x[1::2])
    combined = [0] * n

    for m in range(int(n/2)):
        combined[m] = Feven[m] + omega(n, -m) * Fodd[m]
        combined[int(m + n/2)] = Feven[m] - omega(n, -m) * Fodd[m]

    return combined


def ifft(X):
    x = fft([x.conjugate() for x in X])
    return [x.conjugate()/len(X) for x in x]


def pad2(x):
    m, n = np.shape(x)
    M, N = 2 ** int(ceil(log(m, 2))), 2 ** int(ceil(log(n, 2)))
    F = np.zeros((M, N), dtype=x.dtype)
    F[0:m, 0:n] = x
    return F, m, n


def fft2(f):
    f, m, n = pad2(f)
    return np.transpose(fft(np.transpose(fft(f)))), m, n


def ifft2(F, m, n):
    f, M, N = fft2(np.conj(F))
    f = np.matrix(np.real(np.conj(f)))/(M*N)
    return f[0:m, 0:n]


def plot_spectrum(im_fft):
    plt.imshow(np.abs(im_fft), norm=LogNorm(vmin=5), cmap=plt.cm.gray)
    plt.colorbar()


im = imageio.imread('thumb.tif')
# gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# fourier = fft2(gray)

fourier = fft2(im)

# fourier_scaled = fourier[0].copy()
#
# fourier_scaled *= 255.0 / fourier[0].max()
#
# real_fourier = np.abs(fourier_scaled.real.astype(int))
#
# imageio.imwrite('fourier.tif', real_fourier)

plot_spectrum(fourier[0])
plt.show()

i_fourier = ifft2(fourier[0], im.shape[0], im.shape[1])

plt.figure()
plt.imshow(i_fourier, plt.cm.gray)
plt.title('Reconstructed Image')
plt.show()
