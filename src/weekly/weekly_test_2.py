# P6RDCN
import math
import src.utils.helper as helper


# 1. feladat
class LaplaceDistribution:

    def __init__(self, rand, loc, scale):
        self.rand = rand
        self.loc = loc
        self.scale = scale

    def pdf(self, x):
        return 1 / (2 * self.scale) * math.exp(-math.fabs(x - self.loc)/self.scale)

    def cdf(self, x):
        return 0.5 + 0.5 * helper.sign(x - self.loc) * (1 - math.exp(-(math.fabs(x - self.loc)) / self.scale))

    def ppf(self, p):
        if p < 0 or p > 1:
            raise Exception("Invalid probability")
        return self.loc - self.scale * helper.sign(p - 0.5) * math.log((1 - 2 * math.fabs(p - 0.5)), math.e)

    def gen_rand(self):
        return self.ppf(self.rand.random())

    def mean(self):
        return self.loc

    def variance(self):
        return 2 * self.scale ** 2

    def skewness(self):
        return 0

    def ex_kurtosis(self):
        return 3

    def mvsk(self):
        return [self.mean(), self.variance(), self.skewness(), self.ex_kurtosis()]


# 2. feladat
class ParetoDistribution:

    def __init__(self, rand, scale, shape):
        self.rand = rand
        self.scale = scale
        self.shape = shape

    def pdf(self, x):
        return (self.shape * self.scale ** self.shape) / (x ** (self.shape + 1))

    def cdf(self, x):
        return 1 - (self.scale / x) ** self.shape

    def ppf(self, p):
        if p < 0 or p > 1:
            raise Exception("Invalid probability")
        return self.scale * (1 - p) ** (- 1 / self.shape)

    def gen_rand(self):
        return self.ppf(self.rand.random())

    def mean(self):
        if self.shape <= 1:
            return math.inf
        else:
            return (self.shape * self.scale) / (self.shape - 1)

    def variance(self):
        if self.shape <= 1:
            raise Exception("Moment undefined")
        else:
            if self.shape <= 2:
                return math.inf
            else:
                return (self.scale ** 2 * self.shape) / ((self.shape - 1) ** 2 * (self.shape - 2))

    def skewness(self):
        if self.shape <= 3:
            raise Exception("Moment undefined")
        else:
            return (2 * (1 + self.shape) / (self.shape - 3)) * math.sqrt((self.shape - 2) / self.shape)

    def ex_kurtosis(self):
        if self.shape <= 4:
            raise Exception("Moment undefined")
        else:
            return (6 * (self.shape ** 3 + self.shape ** 2 - 6 * self.shape - 2)) / (self.shape * (self.shape - 3) * (self.shape - 4))

    def mvsk(self):
        return [self.mean(), self.variance(), self.skewness(), self.ex_kurtosis()]