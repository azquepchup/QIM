import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

out = '/home/azquepchup/IQM/Química de Materiales/Imagenes_QM'
os.makedirs(out, exist_ok=True)

def bezier(p0, p1, p2, p3, n=200):
    t = np.linspace(0, 1, n)
    x = (1-t)**3*p0[0] + 3*(1-t)**2*t*p1[0] + 3*(1-t)*t**2*p2[0] + t**3*p3[0]
    y = (1-t)**3*p0[1] + 3*(1-t)**2*t*p1[1] + 3*(1-t)*t**2*p2[1] + t**3*p3[1]
    return x, y

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

for i, (ax, exo) in enumerate(zip(axes, [True, False])):
    if exo:
        R, TS, P = (0.5, 0.55), (5.0, 1.00), (9.5, 0.15)
        dh = '$\\Delta H < 0$'
        title = '$S_N2$ — Exotérmica'
        ls = 'k-'
    else:
        R, TS, P = (0.5, 0.20), (5.0, 1.00), (9.5, 0.65)
        dh = '$\\Delta H > 0$'
        title = '$S_N2$ — Endotérmica'
        ls = 'k--'

    x0 = np.linspace(0.0, R[0], 20); y0 = np.full_like(x0, R[1])
    x1, y1 = bezier(R,  (2.0, R[1]),  (3.5, TS[1]), TS)
    x2, y2 = bezier(TS, (6.5, TS[1]), (8.0, P[1]),  P)
    x3 = np.linspace(P[0], 10.0, 20); y3 = np.full_like(x3, P[1])

    xs = np.concatenate([x0, x1, x2, x3])
    ys = np.concatenate([y0, y1, y2, y3])
    ax.plot(xs, ys, ls, linewidth=2.2)

    ax.text(R[0]-0.15,  R[1]+0.04,  'R', fontsize=12, fontweight='bold')
    ax.text(P[0]+0.15,  P[1]+0.04,  'P', fontsize=12, fontweight='bold')
    ax.text(TS[0], TS[1]+0.05, '$\\ddagger$', fontsize=14, ha='center')

    side = -1 if exo else 1
    ax.annotate('Estado de\ntransición',
                xy=TS, xytext=(TS[0]+side*1.8, TS[1]+0.12),
                fontsize=9, ha='center',
                arrowprops=dict(arrowstyle='->', color='gray', lw=1))

    ax.annotate('', xy=(TS[0], TS[1]), xytext=(TS[0], R[1]),
                arrowprops=dict(arrowstyle='<->', color='steelblue', lw=1.2))
    ax.text(TS[0]+0.2, (TS[1]+R[1])/2, '$E_a$', fontsize=10, color='steelblue')

    ax.annotate('', xy=(9.3, P[1]), xytext=(9.3, R[1]),
                arrowprops=dict(arrowstyle='<->', color='firebrick', lw=1.2))
    ax.text(9.55, (P[1]+R[1])/2, dh, fontsize=9, color='firebrick')

    ax.set_xlabel('Avance de reacción', fontsize=11)
    ax.set_ylabel('Energía', fontsize=11)
    ax.set_title(title, fontsize=12)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlim(0, 10); ax.set_ylim(0, 1.3)
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)

plt.tight_layout()
outfile = os.path.join(out, 'coordenada_SN2.pdf')
plt.savefig(outfile, bbox_inches='tight', dpi=150)
plt.close()
print(f"Guardado: {outfile}")