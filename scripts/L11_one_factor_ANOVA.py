# L11_ANOVA_one_factor.py ---
#
# Filename: L11_ANOVA_one_factor.py
# Description:
# Author: Subhasis Ray
# Created: Thu Sep  3 10:36:22 2026 (+0530)
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
stats.f_oneway(business.mid, stem.mid, hass.mid, nan_policy='omit')

#
# L11_ANOVA_one_factor.py ends here
