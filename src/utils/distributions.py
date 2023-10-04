import random
import math
import pyerf
import scipy
random.seed(42)


class UniformDistribution:
    def __init__(self, rand, a, b):
        self.rand = rand
        self.a = a
        self.b = b

    def pdf(self, x):
        if (x >= self.a) and (x <= self.b):
            return 1 / (self.b - self.a)
        else:
            return 0

    def cdf(self, x):
        if x < self.a:
            return 0
        elif x > self.b:
            return 1
        else:
            return (x - self.a) / (self.b - self.a)

    def ppf(self, p):
        if (p < 0) or (p > 1):
            raise Exception("Invalid probability")
        else:
            return p * (self.b - self.a) + self.a

    def gen_rand(self):
        return self.ppf(self.rand.random())

    def mean(self):
        return 0.5 * (self.a + self.b)

    def median(self):
        return 0.5 * (self.a + self.b)

    def variance(self):
        return 1 / 12 * (self.b - self.a) ** 2

    def skewness(self):
        return 0

    def ex_kurtosis(self):
        return -6 / 5

    def mvsk(self):
        return [self.mean(), self.variance(), self.skewness(), self.ex_kurtosis()]


class NormalDistribution:

    def __init__(self, rand, loc, scale):
        self.rand = rand
        self.loc = loc
        self.scale = scale

    def pdf(self, x):
        return (1 / (math.sqrt(self.scale) * math.sqrt(2 * math.pi))) * math.exp(
            -0.5 * ((x - self.loc) / math.sqrt(self.scale)) ** 2)

    def cdf(self, x):
        z = (x - self.loc) / (math.sqrt(self.scale) * math.sqrt(2))
        return 0.5 * (1 + pyerf.erf(z))

    def ppf(self, p):
        if p < 0 or p > 1:
            raise Exception("Invalid probability")
        z = pyerf.erfinv(2 * p - 1) * math.sqrt(2)
        return self.loc + z * math.sqrt(self.scale)

    def gen_rand(self):
        return self.ppf(self.rand.random())

    def mean(self):
        return self.loc

    def median(self):
        return self.loc

    def variance(self):
        return self.scale

    def skewness(self):
        return 0

    def ex_kurtosis(self):
        return 0

    def mvsk(self):
        return [self.mean(), self.variance(), self.skewness(), self.ex_kurtosis()]


class CauchyDistribution:

    def __init__(self, rand, loc, scale):
        self.rand = rand
        self.loc = loc
        self.scale = scale

    def pdf(self, x):
        return 1 / (math.pi * self.scale * (1 + ((x - self.loc) / self.scale) ** 2))

    def cdf(self, x):
        return 1 / math.pi * math.atan((x - self.loc) / self.scale) + 0.5

    def ppf(self, p):
        if p < 0 or p > 1:
            raise Exception("Invalid probability")
        else:
            return self.loc + self.scale * math.tan(math.pi * (p - 0.5))

    def gen_rand(self):
        return self.ppf(self.rand.random())

    def mean(self):
        raise Exception("Moments undefined")

    def median(self):
        return self.loc

    def variance(self):
        raise Exception("Moments undefined")

    def skewness(self):
        raise Exception("Moments undefined")

    def ex_kurtosis(self):
        raise Exception("Moments undefined")

    def mvsk(self):
        return [self.mean(), self.variance(), self.skewness(), self.ex_kurtosis()]


class LogisticDistribution:

    def __init__(self, rand, location, scale):
        self.rand = rand
        self.location = location
        self.scale = scale

    def pdf(self, x):
        return (math.e ** (-(x - self.location) / self.scale)) / (self.scale * (1 + math.e ** (-(x - self.location) / self.scale)) ** 2)

    def cdf(self, x):
        return 1 / (1 + math.e ** (-(x - self.location) / self.scale))

    def ppf(self, p):
        if p < 0 or p > 1:
            raise Exception("Invalid probability")
        else:
            return self.location + self.scale * math.log(p / (1 - p), math.e)

    def gen_rand(self):
        return self.ppf(self.rand.random())

    def mean(self):
        return self.location

    def variance(self):
        return self.scale ** 2 * math.pi ** 2 / 3

    def skewness(self):
        return 0

    def ex_kurtosis(self):
        return 6/5

    def mvsk(self):
        return [self.mean(), self.variance(), self.skewness(), self.ex_kurtosis()]


class ChiSquaredDistribution:

    def __init__(self, rand, dof):
        self.rand = rand
        self.dof = dof

    def pdf(self, x):
        if x < 0:
            return 0
        else:
            return (x ** (self.dof / 2 - 1) * math.e ** (-x / 2)) / (2 ** (self.dof / 2) * scipy.special.gamma(self.dof / 2))

    def cdf(self, x):
        if x < 0:
            return 0
        else:
            return scipy.special.gammainc(self.dof / 2, x / 2)

    def ppf(self, p):
        if p < 0 or p > 1:
            raise Exception("Invalid probability")
        else:
            return scipy.special.gammaincinv(self.dof / 2, p) * 2

    def gen_rand(self):
        return self.ppf(self.rand.random())

    def mean(self):
        return self.dof

    def variance(self):
        return self.dof * 2

    def skewness(self):
        return (8 / self.dof) ** 0.5

    def ex_kurtosis(self):
        return 12 / self.dof

    def mvsk(self):
        return [self.mean(), self.variance(), self.skewness(), self.ex_kurtosis()]