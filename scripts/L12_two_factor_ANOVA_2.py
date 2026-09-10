# L11_ANOVA_one_factor.py ---
#
# Filename: L12_two_factor_ANOVA_2.py
# Description:
# Author: Subhasis Ray
# Created: Thu Sep  8 10:36:22 2026 (+0530)
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

#%% Extract groups
business = df[df.Group == 'Business']
stem =  df[df.Group == 'STEM']
hass =  df[df.Group == 'HASS']

#%%
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

new_data = []
for row in df.itertuples():
    new_data.append((row.Group, row.starting, 0))
    new_data.append((row.Group, row.mid, 1))

new_data = pd.DataFrame(new_data, columns=['group', 'salary', 'level'])

#%%
formula = 'salary ~ C(group) + C(level) + C(group)*C(level)'
res = ols(formula, new_data).fit()
# print(res.summary())
# print('&' * 70)
print(anova_lm(res))
#
# L12_two_factor_ANOVA_2.pt ends here
