import numpy as np
import matplotlib.pyplot as plt
import math as m


def part1():
    # plot histogram of samples
    plt.figure(1)
    plt.hist(X, 70, density=True, color='m')
    plt.title("Gaussian Random Variable Sample Histogram")
    plt.xlabel("X Value")
    plt.ylabel("Frequency")

    # plot sample means vs n
    Mn = []
    n = []

    for i in range(N):
        n.append(i + 1)
        Mn.append(np.mean(X[0:i + 1]))

    plt.figure(2)
    plt.plot(n, Mn, color='m')
    plt.title("Gaussian Sample Means vs # Samples")
    plt.xlabel("n")
    plt.ylabel("Sample Mean")
    plt.show()


def part2():
    Un = np.random.uniform(-1, 1, N)
    Cn = []
    for i in Un:
        Cn.append(m.tan(m.pi * i))

    C100 = Cn[0:100]
    C1000 = Cn[0:1000]

    # plot n = 100
    plt.figure(1)
    plt.hist(C100, 100, density=True, color="b", range=(-5, 5))
    plt.title("Cauchy Random Variable Sample Histogram for n = 100")
    plt.xlabel("Cn")
    plt.ylabel("Frequency")

    # plot n = 1000
    plt.figure(2)
    plt.hist(C1000, 100, density=True, color="b", range=(-5, 5))
    plt.title("Cauchy Random Variable Sample Histogram for n = 1000")
    plt.xlabel("Cn")
    plt.ylabel("Frequency")

    # plot n = 10000
    plt.figure(3)
    plt.hist(Cn, 100, density=True, color="b", range=(-5, 5))
    plt.title("Cauchy Random Variable Sample Histogram for n = 10000")
    plt.xlabel("Cn")
    plt.ylabel("Frequency")

    n = []
    Cmean = []
    for i in range(N):
        n.append(i + 1)
        Cmean.append(np.mean(Cn[0:i + 1]))

    # plot sample means vs n
    plt.figure(4)
    plt.plot(n, Cmean, color="b")
    plt.title("Cauchy Sample Means vs # Samples")
    plt.xlabel("n")
    plt.ylabel("Sample Mean")
    plt.show()

    return

def part3():
    Y = np.random.normal(mu, sigma, 10000)
    Z = np.divide(X, Y)

    Z100 = Z[0:100]
    Z1000 = Z[0:1000]

    plt.figure(1)
    plt.hist(Z100, 100, density=True, color='orange', range=(-5, 5))
    plt.title("Quotient Cauchy Random Variable Sample Histogram for n = 100")
    plt.xlabel("Zn")
    plt.ylabel("Frequency")

    plt.figure(2)
    plt.hist(Z1000, 100, density=True, color='orange', range=(-5, 5))
    plt.title("Quotient Cauchy Random Variable Sample Histogram for n = 1000")
    plt.xlabel("Zn")
    plt.ylabel("Frequency")

    plt.figure(3)
    plt.hist(Z, 100, density=True, color='orange', range=(-5, 5))
    plt.title("Quotient Cauchy Random Variable Sample Histogram for n = 10000")
    plt.xlabel("Zn")
    plt.ylabel("Frequency")

    n = []
    Zmean = []
    for i in range(N):
        n.append(i + 1)
        Zmean.append(np.mean(Z[0:i + 1]))

    plt.figure(4)
    plt.plot(n, Zmean, color='orange')
    plt.title("Quotient Cauchy Sample Means vs # Samples")
    plt.xlabel("n")
    plt.ylabel("Sample Mean")
    plt.show()
    return


N = 10000 # for all parts
mu, sigma = 0, 1  # 0 mean, unit variance
X = np.random.normal(mu, sigma, 10000) # X to be used in both part 1 and part 3
part1()
part2()
part3()