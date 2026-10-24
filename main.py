#coding:utf8

import numpy as np
import pandas as pd
import scipy
import scipy.stats
import matplotlib.pyplot as plt

#https://docs.scipy.org/doc/scipy/reference/stats.html

dist_names = ['norm', 'beta', 'gamma', 'pareto', 't', 'lognorm', 'invgamma', 'invgauss',  'loggamma', 'alpha', 'chi', 'chi2', 'bradford', 'burr', 'burr12', 'cauchy', 'dweibull', 'erlang', 'expon', 'exponnorm', 'exponweib', 'exponpow', 'f', 'genpareto', 'gausshyper', 'gibrat', 'gompertz', 'gumbel_r', 'pareto', 'pearson3', 'powerlaw', 'triang', 'weibull_min', 'weibull_max', 'bernoulli', 'betabinom', 'betanbinom', 'binom', 'geom', 'hypergeom', 'logser', 'nbinom', 'poisson', 'poisson_binom', 'randint', 'zipf', 'zipfian']

print(dist_names)

# Question 1
print("Question 1")

#Loi de Dirac
plt.stem([0], [1])
plt.title("Loi de Dirac en 0")
plt.savefig("img/loi_Dirac.png")
plt.show()

#Loi uniforme discrète
x = np.arange(1, 11)
plt.stem(x, scipy.stats.randint.pmf(x, 1, 11))
plt.title("Loi uniforme discrète sur {1, ..., 10}")
plt.savefig("img/loi_uniforme_discrete.png")
plt.show()

#Loi binomiale
plt.stem(range(11), scipy.stats.binom.pmf(range(11), 10, 0.5))
plt.title("Loi binomiale B(10, 0.5)")
plt.savefig("img/loi_binomiale.png")
plt.show()

#Loi de poisson
x = np.arange(0, 15)
plt.plot(x, scipy.stats.poisson.pmf(x, mu=5), 'o-')
plt.savefig("img/loi_poisson.png")
plt.show()

#Loi de Zipf-Mandelbrot
x = np.arange(1, 21)
p = 1 / (x + 1)**1.5
p /= p.sum()
plt.stem(x, p)
plt.title("Loi de Zipf-Mandelbrot")
plt.savefig("img/loi_zipf_mandelbrot.png")
plt.show()

#Loi de Poisson Variables continues
x = np.arange(16)
plt.plot(np.linspace(0, 15, 300), np.interp(np.linspace(0, 15, 300), x, scipy.stats.poisson.pmf(x, 5)))
plt.savefig("img/loi_poisson_interpolee.png")
plt.show()

#Loi normale
x = np.linspace(-4, 4, 300)
plt.plot(x, scipy.stats.norm.pdf(x, 0, 1))
plt.title("Loi normale N(0, 1)")
plt.savefig("img/loi_normale.png")
plt.show()

#Loi log-normale
x = np.linspace(0.01, 5, 300)
plt.plot(x, scipy.stats.lognorm.pdf(x, s=0.5))
plt.title("Loi log-normale")
plt.savefig("img/loi_log_normale.png")
plt.show()

#Loi uniforme
x = np.linspace(-1, 2, 300)
plt.plot(x, scipy.stats.uniform.pdf(x, loc=0, scale=1))
plt.title("Loi uniforme U(0, 1)")
plt.savefig("img/loi_uniforme.png")
plt.show()

#Loi du χ2
x = np.linspace(0, 20, 300)
plt.plot(x, scipy.stats.chi2.pdf(x, df=5))
plt.title("Loi du χ² (5 degrés de liberté)")
plt.savefig("img/loi_chi2.png")
plt.show()

#Loi de Pareto
x = np.linspace(1, 10, 300)
plt.plot(x, scipy.stats.pareto.pdf(x, b=3))
plt.title("Loi de Pareto")
plt.savefig("img/loi_pareto.png")
plt.show()

# Question 2
print("Question 2")
distributions = {
    "Binomiale": scipy.stats.binom(10, 0.5),
    "Uniforme discrète": scipy.stats.randint(1, 11),
    "Zipf-Mandelbrot": None,
    "Poisson": scipy.stats.poisson(5),
    "Normale": scipy.stats.norm(0, 1),
    "Log-normale": scipy.stats.lognorm(s=0.5),
    "Uniforme": scipy.stats.uniform(0, 1),
    "Khi-deux": scipy.stats.chi2(df=5),
    "Pareto": scipy.stats.pareto(b=3)
}
print(distributions)
for nom, loi in distributions.items():
    if loi is not None:
        print(f"{nom}: moyenne = {loi.mean():.4f}, écart-type = {loi.std():.4f}")

