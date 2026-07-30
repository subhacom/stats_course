# binomial_to_gaussian_v2.py ---
#
# Filename: binomial_to_gaussian_v2.py
# Description:
# Author: Subhasis Ray
# Created: Mon Jul 27 11:04:37 2026 (+0530)
#

# Code:
import numpy as np
import matplotlib.pyplot as plt

# Given the same seed, the random number generator (RNG) reproduces
# the same sequence of random numbers. When it is `None`, the RNG uses
# system time and other parameters to seed the RNG, so that the
# sequence is different each time
seed = None
rng = np.random.default_rng(seed)


def bean_draw(N, p):
    """Draw `N` beans from a mix of red and white where the fraction of
    red beans is `p`.

    Here we use numpy random number related functions more efficiently.
    """
    # rng.choice(x, size, replace, p)
    # x - array possible outcomes to pick from
    # size - number of samples to pick
    # replace - whether to replace the element after picking
    # p - array of probabilities of each outcome
    return rng.choice([0, 1], size=N, replace=True, p=[1 - p, p])


def Bernoulli_sampling(n, N, p):
    """Run n experiments of N-draws where probability of success is p"""
    samples = []
    for ii in range(n):
        samples.append(bean_draw(N, p))

    sample_means = [np.mean(sample) for sample in samples]
    # `np.var(sample_array, ddof)` calculates variance where ddof
    # represents `delta degrees of freedom`. It computes variance as
    # `sum_squared_deviation / (N - ddof)`. By default it uses ddof=0,
    # for Bessel's correction, we specify ddof=1 so that var =
    # sum_squared_deviation / (N - 1).
    sample_variances = [np.var(sample, ddof=1) for sample in samples]
    mean_of_means = np.mean(sample_means)
    mean_of_vars = np.mean(sample_variances)
    var_of_means = np.var(sample_means, ddof=1)
    # Print some info
    print('*' * 30)
    print('Draws N=', N, 'p=', p, 'repeats n=', n)
    print('E(Xbar):', mean_of_means, 'Theoretical:', p)
    print('Var(Xbar):', var_of_means, 'Theoretical:', p * (1-p)/N)
    print('Mean of sample variances:', mean_of_vars, 'Theoretical:', p*(1-p))

    # Return the results as a dict
    return {'samples': samples,
            'sample_means': sample_means,
            'mean_of_means': mean_of_means,
            'var_of_means': var_of_means}
#%%

n = 30

N_small = 10
p = 0.5
ret_small = Bernoulli_sampling(n, N_small, p)

N_med = 30
ret_med = Bernoulli_sampling(n, N_med, p)

N_large = 100
ret_large = Bernoulli_sampling(n, N_large, p)

fig, axes = plt.subplots(nrows=3, ncols=1, sharex='all')


# Note: `bins=np.linspace(-0.5/N_small, 1+0.5/N_small, N_small+2)` to have one bean for every possible value
axes[0].hist(ret_small['sample_means'], density=True, bins=np.linspace(-0.5/N_small, 1+0.5/N_small, N_small+2))
axes[0].axvline(p - np.sqrt(p * (1-p)/N_small), color='red', alpha=0.5, label='mean +/- SD')
axes[0].axvline(p + np.sqrt(p * (1-p)/N_small), color='red', alpha=0.5)
axes[0].axvline(p, color='orange', alpha=0.5, label='mean')

axes[1].hist(ret_med['sample_means'], density=True, bins=np.linspace(-0.5/N_med, 1+0.5/N_med, N_med+2))
axes[1].axvline(p - np.sqrt(p * (1-p)/N_med), color='red', alpha=0.5, label='mean +/- SD')
axes[1].axvline(p + np.sqrt(p * (1-p)/N_med), color='red', alpha=0.5)
axes[1].axvline(p, color='orange', alpha=0.5, label='mean')

axes[2].hist(ret_large['sample_means'], density=True, bins=np.linspace(-0.5/N_large, 1+0.5/N_large, N_large+2))
axes[2].axvline(p - np.sqrt(p * (1 - p)/ N_large), color='red', alpha=0.5, label='mean +/- SD')
axes[2].axvline(p + np.sqrt(p * (1 - p)/ N_large), alpha=0.5, color='red')
axes[2].axvline(p, color='orange', alpha=0.5, label='mean')
for ax in axes:
    ax.legend()
plt.show()

#
# binomial_to_gaussian_v2.py ends here
