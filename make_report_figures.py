"""Draws the two schematic/analytic figures of the report: domain geometry (Fig. 1) and IDM fundamental diagram (Fig. 2).
Run:  python make_report_figures.py     -> writes fig_geometry.png and fig_fundamental_diagram.png"""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
plt.rcParams.update({"font.family": "serif", "font.size": 11})

# ---- Fig. 1: geometry
fig, ax = plt.subplots(figsize=(7.2, 2.8))
for i in range(3):
    ax.add_patch(Rectangle((0, i), 1500 if i == 0 else 3000, 0.6, fc="#d9d9d9", ec="k", lw=0.8))
for y, t in ((0.3, "lane 0 (ends at drop)"), (1.3, "lane 1"), (2.3, "lane 2")):
    ax.text(750, y, t, ha="center", va="center", fontsize=9)
ax.add_patch(Polygon([[1500, 0], [1500, 0.6], [1560, 0.3]], fc="r", ec="r"))
ax.plot([1500, 1500], [-0.4, 3.4], "r--", lw=1); ax.text(1510, 3.15, "lane drop, x = 1500 m", color="r", fontsize=9)
ax.plot([900, 1000], [-0.8, 0.0], "k-", lw=2.5)
ax.text(930, -1.0, "on-ramp (storage 15 veh)\nmerge at x = 1000 m", fontsize=8.5, ha="left", va="center")
for d in [250, 500, 750, 1000, 1250]:
    ax.plot([1500 - d], [3.0], "bv", ms=7); ax.text(1500 - d, 3.45, f"{d}", ha="center", fontsize=8.5, color="b")
ax.text(-40, 3.45, "d [m]:", ha="right", fontsize=8.5, color="b")
ax.annotate("", xy=(150, 1.3), xytext=(10, 1.3), arrowprops=dict(arrowstyle="->")); ax.text(0, -0.3, "Poisson arrivals", fontsize=8.5, va="top")
ax.annotate("", xy=(3000, 1.3), xytext=(2850, 1.3), arrowprops=dict(arrowstyle="->")); ax.text(2990, 0.5, "outflow", ha="right", fontsize=8.5)
ax.set_xlim(-160, 3060); ax.set_ylim(-1.5, 3.9); ax.set_xlabel("position x [m]"); ax.set_yticks([])
ax.spines[["left", "top", "right"]].set_visible(False)
plt.tight_layout(); plt.savefig("fig_geometry.png", dpi=200); plt.close()

# ---- Fig. 2: equilibrium IDM fundamental diagram
def cap(T, v0=120/3.6, s0=1, s1=10, d=4, l=4.5):
    v = np.linspace(0.1, v0 * 0.9999, 400)
    se = (s0 + s1 * np.sqrt(v / v0) + v * T) / np.sqrt(1 - (v / v0) ** d)
    rho = 1000 / (se + l); return rho, rho * v * 3.6
fig, ax = plt.subplots(figsize=(5.6, 3.6))
for T, c, n in ((1.2, "C0", "Human, T = 1.2 s"), (0.6, "C3", "AV, T = 0.6 s")):
    r, q = cap(T); ax.plot(r, q, c, lw=2, label=f"{n} (capacity {q.max():.0f} veh/h/lane)")
ax.set_xlim(0, 160); ax.set_xlabel("density [veh/km/lane]"); ax.set_ylabel("flow [veh/h/lane]"); ax.legend(fontsize=9); ax.grid(alpha=.3)
plt.tight_layout(); plt.savefig("fig_fundamental_diagram.png", dpi=200); plt.close()
print("wrote fig_geometry.png, fig_fundamental_diagram.png")
