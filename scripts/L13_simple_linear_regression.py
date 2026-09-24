from scipy import stats

x = np.r_[22, 18, 30, 16, 25, 20, 10, 14]
y = np.r_[18.4, 19.2, 14.5, 19.0, 16.6, 17.7, 24.4, 21.0]

result = stats.linregress(x, y)

print(f'slope        = {result.slope:.4f}')
print(f'intercept    = {result.intercept:.4f}')
print(f'rvalue       = {result.rvalue:.4f}')
print(f'pvalue       = {result.pvalue:.4g}')
print(f'stderr       = {result.stderr:.4f}')

fig, ax = plt.subplots()
ax.scatter(x, y)
y_hat = result.intercept + result.slope * x
ax.plot(x, y_hat, color='red')
ax.set_xlabel('Training time (hrs)')
ax.set_ylabel('Project completion time (hrs)')
fig.set_size_inches(3,3)
fig.tight_layout()
