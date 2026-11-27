"""G3：把「越界」画成函数图像。
rho(p) = 1 - 0.5^p 是平方族 d_p=|x-y|^p 下的剩余半径；
内圆右缘 = 0.5 + rho(p)，越过大圆边界 1 当且仅当 rho(p) > 0.5。
rho(1)=0.5 恰好在线上；rho(2)=0.75 越界 0.25（Euclid 半径 0.866，右缘 1.366）。
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = ['Microsoft YaHei', 'DejaVu Serif', 'serif']

p = np.linspace(0.55, 2.15, 400)
rho = 1 - 0.5 ** p

fig, ax = plt.subplots(figsize=(7.6, 4.9), dpi=220)
ax.plot(p, rho, color='black', lw=2.2, zorder=4, label=r'$\rho(p)=1-0.5^{\,p}$')
ax.axhline(0.5, color='0.45', lw=1.2, ls=(0, (5, 3)), zorder=2)
ax.axvline(1.0, color='0.45', lw=1.2, ls=(0, (5, 3)), zorder=2)

# 越界区
ax.fill_between(p, 0.5, rho, where=(p >= 1.0) & (rho >= 0.5),
                color='0.72', alpha=0.55, zorder=1, interpolate=True)

ax.plot([1.0], [0.5], 'o', ms=7, mfc='white', mec='black', mew=2, zorder=6)
ax.plot([2.0], [0.75], 'o', ms=7, color='black', zorder=6)

ax.annotate(r'$p=1$: $\rho=0.5$' + '\n刚好贴住', (1.0, 0.5),
            xytext=(14, -34), textcoords='offset points', fontsize=11.5,
            arrowprops=dict(arrowstyle='-', lw=0.9, color='0.35'), ha='left')
ax.annotate(r'$p=2$: $\rho=0.75$' + '\n右缘 $1.366$，越界 $0.366$', (2.0, 0.75),
            xytext=(-14, -66), textcoords='offset points', fontsize=11.5,
            arrowprops=dict(arrowstyle='-', lw=0.9, color='0.35'), ha='right')
ax.text(1.52, 0.60, '越界区\n' + r'$\rho>0.5$', fontsize=12, ha='center', color='0.2')

ax.set_xlim(0.55, 2.18)
ax.set_ylim(0.28, 0.86)
ax.set_xlabel(r'$p$  （$d_p=|x-y|^{\,p}$ 的指数）', fontsize=12.5)
ax.set_ylabel(r'剩余半径 $\rho$', fontsize=12.5)
ax.set_yticks([0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8])
ax.set_xticks([0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0])
ax.tick_params(labelsize=10.5)
for s in ('top', 'right'):
    ax.spines[s].set_visible(False)
ax.legend(loc='upper left', fontsize=11, frameon=False)

out = os.path.dirname(os.path.abspath(__file__))
pp = os.path.join(out, 'G3-function-plot.png')
fig.savefig(pp, bbox_inches='tight', facecolor='white')
print('saved', pp, os.path.getsize(pp))
for q in (1.0, 1.5, 2.0):
    r = 1 - 0.5 ** q
    print(f'  p={q}  rho={r:.4f}  right_edge={0.5+r:.4f}  over={max(0,0.5+r-1):.4f}')
