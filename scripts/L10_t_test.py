# L10_t_test.py ---
#
# Filename: L10_t_test.py
# Description:
# Author: Subhasis Ray
# Created: Tue Sep  1 10:44:08 2026 (+0530)
#

# Code:
#%% imports
import numpy as np
import pandas as pd
from scipy import stats

import matplotlib.pyplot as plt
#%% Load data
df = pd.read_csv('../data/salaries_by_college_major.csv').dropna()

df.rename(columns={
    'Undergraduate Major': 'major',
    'Starting Median Salary': 'starting',
    'Mid-Career Median Salary': 'mid',
    'Mid-Career 10th Percentile Salary': 'mid10',
    'Mid-Career 90th Percentile Salary': 'mid90'},
          inplace=True)
print('After sanitization\n', df)

#%% Extract Business and STEM
print(df.Group == 'Business')

business = df[df.Group == 'Business']
stem = df[df.Group == 'STEM']
print('#' * 20, '\n', business, '=' * 20, '\n', stem)
#%%
bs = business.starting
ss = stem.starting
print(len(bs))
print(len(ss))
stats.ttest_ind(bs, ss, alternative='less')
print('mean bs', bs.mean(), 'mean stem', ss.mean())

stats.ttest_ind(business.mid, stem.mid, alternative='less')

#%%
import seaborn as sns

sns.catplot(data=df, kind='bar', x='Group', y='mid', errorbar='sd')
# df.plot(x='Group', y='mid', yerr='StdDev', kind='bar')
plt.show()
#
# L10_t_test.py ends here
