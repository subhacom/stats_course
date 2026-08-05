# L6_ci_unknown_variance.py ---
#
# Filename: L6_ci_unknown_variance.py
# Description:
# Author: Subhasis Ray
# Created: Wed Aug  5 22:14:53 2026 (+0530)
#

# Code:
#%% imports
import numpy as np
import pandas as pd
from scipy import stats

import matplotlib.pyplot as plt
#%% Load data
df = pd.read_csv('../data/salaries_by_college_major.csv').dropna()

#%% Brief look at the data
print('The dataframe content')
print('*' * 40)
print(df)

#%% Head and tail
print('The dataframe head')
print('-' * 40) # print 40 dashes to make a horizontal separator line
print(df.head())
print('The dataframe tail')
print('-' * 40)
print(df.tail())

#%% Column name sanitization
print('The dataframe columns')
print('-' * 40) # print 40 dashes to make a horizontal separator line
print(df.columns)
df.rename(columns={
    'Undergraduate Major': 'major',
    'Starting Median Salary': 'starting',
    'Mid-Career Median Salary': 'mid',
    'Mid-Career 10th Percentile Salary': 'mid10',
    'Mid-Career 90th Percentile Salary': 'mid90'},
          inplace=True)
print('After sanitization\n', df)
#%% Use mid-career median salary as population
pop = df.mid
# `na` (NaN) contaminates all calculations and comparisons with NaN
# always return False
pop.dropna(inplace=True)
mu_true = pop.mean()

#%% Random sampling - credit: Claude
rng = np.random.default_rng()
alpha = 0.05

def coverage(n, reps=1000):
    # ppf = percent point function, it is the inverse of cdf (cumulative distribution function)
    # cdf q = P(X < x), ppf(q) = x, quantile corresponding to the tail probability q
    z = stats.norm.ppf(1 - alpha/2)
    t = stats.t.ppf(1 - alpha/2, df=n-1)
    hit_z = hit_t = 0
    for _ in range(reps):
        sample = rng.choice(pop, size=n, replace=True)
        xbar = sample.mean()
        S = sample.std(ddof=1)
        se = S / np.sqrt(n)
        hit_z += abs(xbar - mu_true)  <= z * se
        hit_t += abs(xbar - mu_true)  <= t * se
    return hit_z / reps, hit_t / reps

ns = [5, 10, 20, 30, 100]

results = [coverage(n) for n in ns]
z_cov, t_cov = zip(*results)

#%% Plot coverage vs n
fig, ax = plt.subplots()
ax.plot(ns, z_cov, 'o-', label='naive z (plugging in S)')
ax.plot(ns, t_cov, 's-', label='t-distribution')
ax.axhline(0.95, color='k', linestyle='--', label='nominal 95%')
ax.set_xlabel('sample size n')
ax.set_ylabel('empirical coverage')
ax.legend()
plt.show()

#
# L6_ci_unknown_variance.py ends here
