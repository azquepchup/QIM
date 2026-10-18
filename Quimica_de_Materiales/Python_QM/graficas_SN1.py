import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

out = 'Química de Materiales/Imagenes_QM'
os.makedirs(out, exist_ok=True)

fig, ax = plt.subplots(figsize=(9, 5))

def bezier(p0, p1, p2, p3, n=100):
    t = np.linspace(0, 1, n)
    x = (1-t)**3*p0[0] + 3*(1-t)**2*t*p1[0] + 3*(1-t)*t**2*p2[0] + t**3*p3[0]
    y = (1-t)**3*p0[1] + 3*(1-t)**2*t*p1[1] + 3*(1-t)*t**2*p2[1] + t**3*p3[1]
    return x, y

R   = (0.5,  0.30)
TS1 = (3.0,  1.00)
I   = (5.5,  0.62)
TS2 = (7.5,  0.82)
P   = (9.5,  0.12)

x1, y1 = bezier(R,   (1.5, 0.50), (2.2, 1.00), TS1)
x2, y2 = bezier(TS1, (4.0, 0.95), (4.8, 0.62), I)
x3, y3 = bezier(I,   (6.2, 0.62), (6.8, 0.82), TS2)
x4, y4 = bezier(TS2, (8.5, 0.75), (9.0, 0.12), P)
x5 = np.linspace(P[0], 10.0, 20)
y5 = np.full_like(x5, P[1])

xs = np.concatenate([x1, x2, x3, x4, x5])
ys = np.concatenate([y1, y2, y3, y4, y5])

ax.plot(xs, ys, 'k-', linewidth=2.2)

ax.text(R[0]-0.15,  R[1]+0.04,  'R', fontsize=12, fontweight='bold')
ax.text(P[0]+0.15,  P[1]+0.04,  'P', fontsize=12, fontweight='bold')
ax.text(TS1[0], TS1[1]+0.05, '$\\ddagger$', fontsize=14, ha='center')
ax.text(TS2[0], TS2[1]+0.05, '$\\ddagger$', fontsize=14, ha='center')

ax.annotate('Ruptura\nheterolítica',
            xy=TS1, xytext=(TS1[0]-1.4, TS1[1]+0.15),
            fontsize=9, ha='center',
            arrowprops=dict(arrowstyle='->', color='gray', lw=1))
ax.annotate('Carbocatión\n(intermediario)',
            xy=I, xytext=(I[0]-2.0, I[1]-0.15),
            fontsize=9, ha='center',
            arrowprops=dict(arrowstyle='->', color='gray', lw=1))
ax.annotate('Formación\ndel enlace',
            xy=TS2, xytext=(TS2[0]+1.4, TS2[1]+0.15),
            fontsize=9, ha='center',
            arrowprops=dict(arrowstyle='->', color='gray', lw=1))

ax.annotate('', xy=(TS1[0], TS1[1]), xytext=(TS1[0], R[1]),
            arrowprops=dict(arrowstyle='<->', color='steelblue', lw=1.2))
ax.text(TS1[0]+0.2, (TS1[1]+R[1])/2, '$E_{a1}$', fontsize=10, color='steelblue')

ax.annotate('', xy=(TS2[0], TS2[1]), xytext=(TS2[0], I[1]),
            arrowprops=dict(arrowstyle='<->', color='steelblue', lw=1.2))
ax.text(TS2[0]+0.2, (TS2[1]+I[1])/2, '$E_{a2}$', fontsize=10, color='steelblue')

ax.annotate('', xy=(9.7, P[1]), xytext=(9.7, R[1]),
            arrowprops=dict(arrowstyle='<->', color='firebrick', lw=1.2))
ax.text(9.85, (P[1]+R[1])/2, '$\\Delta H$', fontsize=10, color='firebrick')

ax.set_xlabel('Avance de reacción', fontsize=11)
ax.set_ylabel('Energía', fontsize=11)
ax.set_title('Coordenada de reacción — $S_N1$', fontsize=12)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(0, 10)
ax.set_ylim(0, 1.3)
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
outfile = os.path.join(out, 'coordenada_SN1.pdf')
plt.savefig(outfile, bbox_inches='tight', dpi=150)
plt.close()
print(f"Guardado: {outfile}")