import numpy as np
from scipy   import stats
data = np.array([ # Soil_1, Soil_2, Soil_3, Soil_4
      [[7.8, 9.1, 10.6], [11.2, 12.7, 13.3], [12.1, 12.5, 14.1], [9.1, 10.7, 12.6]],  # Strain 1
      [[8.0, 8.7, 10.0], [11.3, 12.9, 13.8], [13.8, 14.3, 15.4], [11.3, 12.7, 14.3]], # Strain 2
      [[15.3, 16.0, 17.6], [16.8, 18.3, 19.2], [17.9, 21.0, 20.7], [17.2, 18.3, 19.1]] # Strain 3
      ])
print('Data:\n', data)
print('Dimensions:', data.shape)

means_a = np.mean(data, axis=(1,2))
means_b = np.mean(data, axis=(0,2))
means_ab = np.mean(data, axis=2)
grand_mean = np.mean(data)
print(f'X_i..={means_a}\nX_.j.={means_b}\nX_..k={means_ab}\nX_...', grand_mean)

a, b, r = data.shape
ss_a = r * b * np.sum((means_a - grand_mean)**2)
ss_b = r * a * np.sum((means_b - grand_mean)**2)

# Convert `means_a` with shape (3,) to shape (3,4) by repeating it
#  as a column vector
# `means_a[:,np.newaxis]` first converts it into 3x1 2D vector,
# then `broadcast_to` tiles it to make `b` repeated columns
ma_stacked = np.broadcast_to(means_a[:, np.newaxis], (a, b))
# Convert `means_b` with shape (4,) to shape (3,4) by repeating it
#  as a row vector
# `means_b[np.newaxis,:]` first converts it into 1x4 2D vector,
# then `broadcast_to` tiles it to make `a` repeated rows
mb_stacked = np.broadcast_to(means_b[np.newaxis,:], (a, b))
mab_stacked = np.broadcast_to(means_ab[:,:,np.newaxis], (a, b, r))

ss_ab = r * np.sum(
    (means_ab - ma_stacked - mb_stacked + grand_mean)**2)
ss_e = np.sum((data - mab_stacked)**2)

ms_a = ss_a / (a - 1)
ms_b = ss_b / (b - 1)
ms_ab = ss_ab / ((a - 1) * (b - 1))
# Denominator dof - reused for all F stats
dfe = (a * b * r - a * b)
ms_e = ss_e / dfe

F_ab = ms_ab / ms_e
F_a = ms_a / ms_e
F_b = ms_b / ms_e

alpha = 0.05
F_crit_ab = stats.f.ppf(1 - alpha, (a - 1) * (b - 1), dfe)
F_crit_a = stats.f.ppf(1 - alpha, a - 1, dfe)
F_crit_b = stats.f.ppf(1 - alpha, b - 1, dfe)

p_ab = stats.f.sf(F_ab, (a - 1) * (b - 1), dfe)
p_a = stats.f.sf(F_a, a - 1, dfe)
p_b = stats.f.sf(F_b, b - 1, dfe)

print(f'Interaction: F={F_ab:.4f}, F_crit={F_crit_ab:.4f},'
      f' p={p_ab:.6f}, reject H0={F_ab >= F_crit_ab}')
print(f'Factor A:    F={F_a:.4f}, F_crit={F_crit_a:.4f},'
      f' p={p_a:.6f}, reject H0={F_a >= F_crit_a}')
print(f'Factor B:    F={F_b:.4f}, F_crit={F_crit_b:.4f},'
      f' p={p_b:.6f}, reject H0={F_b >= F_crit_b}')

import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

# Reshape the (a, b, r) array into long format: one row per observation
rows = [(f'strain_{i+1}', f'soil_{j+1}', data[i, j, k])
        for i in range(a) for j in range(b) for k in range(r)]
df = pd.DataFrame(rows, columns=['strain', 'soil', 'value'])
formula = 'value ~ C(strain) + C(soil) + C(strain):C(soil)'
model = ols(formula, data=df).fit()
print(anova_lm(model, typ=2))
