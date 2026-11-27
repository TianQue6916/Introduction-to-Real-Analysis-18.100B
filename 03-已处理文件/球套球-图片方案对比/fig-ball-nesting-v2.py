"""球套球对比图 v2：图内只留符号与数字，解释全部交给 md 图注。
布局一律用 offset points 相对定位，不用绝对坐标硬摆。
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc
import os

plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'serif'
plt.rcParams['axes.unicode_minus'] = False

R, Yc, Z = 1.0, 0.5, 1.3
RHO_STD = 0.5
RHO_SQ = np.sqrt(0.75)          # 0.8660254


def setup(ax, title):
    ax.set_xlim(-1.30, 1.60)
    ax.set_ylim(-1.42, 1.18)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(title, fontsize=15, pad=10)


def dot(ax, xy, label, dy, dx=0, ha='center'):
    ax.plot([xy[0]], [xy[1]], 'o', ms=6.5, color='black', zorder=6)
    ax.annotate(label, xy, xytext=(dx, dy), textcoords='offset points',
                ha=ha, va='top' if dy < 0 else 'bottom',
                fontsize=14, zorder=7)


def frame(ax):
    ax.add_patch(Circle((0, 0), R, fill=False, ls=(0, (5, 3)), lw=1.8, ec='black', zorder=3))
    ax.plot([R, R], [-1.28, 1.08], ls=':', lw=0.9, color='0.45', zorder=2)


def ruler(ax, x0, x1, label, fs=13):
    y = -1.14
    ax.plot([x0, x1], [y, y], color='black', lw=3.2, solid_capstyle='butt', zorder=6)
    for xx in (x0, x1):
        ax.plot([xx, xx], [y - 0.055, y + 0.055], color='black', lw=1.3, zorder=6)
    ax.annotate(label, ((x0 + x1) / 2, y), xytext=(0, -8), textcoords='offset points',
                ha='center', va='top', fontsize=fs, zorder=7,
                bbox=dict(fc='white', ec='none', pad=1.2))


fig, axes = plt.subplots(1, 2, figsize=(9.8, 4.7), dpi=220)

# ---------------- 左 ----------------
ax = axes[0]
setup(ax, r'$d=|x-y|$')
frame(ax)
ax.add_patch(Circle((Yc, 0), RHO_STD, fc='0.62', ec='black', lw=1.8, alpha=0.25, zorder=2))
dot(ax, (0, 0), '$x$', -2, dx=-9, ha='right')
dot(ax, (Yc, 0), '$y$', -9)
ruler(ax, Yc, Yc + RHO_STD, r'$r-d=0.5$')

# ---------------- 右 ----------------
ax = axes[1]
setup(ax, r'$d=(x-y)^2$')
frame(ax)
ax.add_patch(Circle((Yc, 0), RHO_SQ, fc='0.62', ec='black', lw=1.8, alpha=0.25, zorder=2))
ax.add_patch(Arc((Yc, 0), 2 * RHO_SQ, 2 * RHO_SQ, theta1=-54.7, theta2=54.7,
                 color='black', lw=2.6, zorder=4))
dot(ax, (0, 0), '$x$', -2, dx=-9, ha='right')
dot(ax, (Yc, 0), '$y$', -9)
ax.plot([Z], [0], 'o', mfc='white', mec='black', mew=2.0, ms=8.5, zorder=6)
ax.annotate('$z$', (Z, 0), xytext=(0, 9), textcoords='offset points',
            ha='center', va='bottom', fontsize=14, zorder=7)
ruler(ax, Yc, Yc + RHO_SQ, r'$r-d=0.866$')
# 探出量
ax.annotate('', xy=(R, 0.62), xytext=(Yc + RHO_SQ, 0.62),
            arrowprops=dict(arrowstyle='<->', lw=1.2, color='black', shrinkA=0, shrinkB=0))
ax.annotate(r'$0.366$', ((R + Yc + RHO_SQ) / 2, 0.62), xytext=(0, 5),
            textcoords='offset points', ha='center', va='bottom', fontsize=11, zorder=7)

plt.subplots_adjust(wspace=0.06)
out = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(out, 'fig-ball-nesting-v2.png')
fig.savefig(p, bbox_inches='tight', facecolor='white')
print('saved:', p, os.path.getsize(p), 'bytes')
print('check: rho_std=%.4f  rho_sq=%.4f  right_edge=%.6f  overshoot=%.6f  z_in_small=%s  z_out_big=%s'
      % (RHO_STD, RHO_SQ, Yc + RHO_SQ, Yc + RHO_SQ - R,
         abs(Z - Yc) < RHO_SQ, abs(Z) > R))
