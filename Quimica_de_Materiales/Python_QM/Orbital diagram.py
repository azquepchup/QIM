import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

out = '/home/azquepchup/IQM/Química de Materiales/Imagenes_QM'
os.makedirs(out, exist_ok=True)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

x = np.linspace(-4, 4, 1000)
d = 1.2
s = 1.0

psi_L = np.exp(-((x+d)**2)/(2*s**2))
psi_R = np.exp(-((x-d)**2)/(2*s**2))

# --- Enlazante ---
ax = axes[0]
psi_bond = psi_L + psi_R
# Normalizar para que el pico sea 1
psi_bond = psi_bond / psi_bond.max()

ax.fill_between(x, psi_bond, alpha=0.3, color='steelblue')
ax.plot(x, psi_bond, 'steelblue', linewidth=2)
ax.axhline(0, color='k', linewidth=0.8)

ax.plot([-d, d], [0, 0], 'ko', markersize=7, zorder=5)
ax.text(-d, -0.1, 'N$_1$', ha='center', fontsize=10)
ax.text( d, -0.1, 'N$_2$', ha='center', fontsize=10)
ax.axvline(-d, color='k', linewidth=0.5, linestyle='--', alpha=0.3)
ax.axvline( d, color='k', linewidth=0.5, linestyle='--', alpha=0.3)

ax.annotate('densidad alta\nentre núcleos',
            xy=(0, psi_bond[500]),
            xytext=(0, psi_bond[500] + 0.35),
            fontsize=9, ha='center',
            arrowprops=dict(arrowstyle='->', color='steelblue', lw=1.2))

ax.set_title('$\\sigma$ enlazante', fontsize=12)
ax.set_xlabel('Posición', fontsize=10)
ax.set_ylabel('Función de onda $\\psi$', fontsize=10)
ax.set_ylim(-0.2, 1.6)
ax.set_xlim(-4, 4)
ax.set_xticks([])
ax.set_yticks([])
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

# --- Antienlazante ---
ax = axes[1]
psi_anti = psi_L - psi_R
psi_anti = psi_anti / abs(psi_anti).max()

ax.fill_between(x, psi_anti, where=(psi_anti > 0), alpha=0.3, color='firebrick')
ax.fill_between(x, psi_anti, where=(psi_anti < 0), alpha=0.3, color='firebrick')
ax.plot(x, psi_anti, 'firebrick', linewidth=2)
ax.axhline(0, color='k', linewidth=0.8)

ax.plot([-d, d], [0, 0], 'ko', markersize=7, zorder=5)
ax.text(-d, -0.15, 'N$_1$', ha='center', fontsize=10)
ax.text( d, -0.15, 'N$_2$', ha='center', fontsize=10)
ax.axvline(-d, color='k', linewidth=0.5, linestyle='--', alpha=0.3)
ax.axvline( d, color='k', linewidth=0.5, linestyle='--', alpha=0.3)

# Nodo
ax.axvline(0, color='darkred', linewidth=1.5, linestyle=':', alpha=0.9)
ax.text(0.15, 0.6, 'nodo\n$\\psi=0$', fontsize=9, color='darkred')

ax.annotate('lóbulo\nexterno',
            xy=(-2.5, psi_anti[100]),
            xytext=(-3.3, 0.8),
            fontsize=9, ha='center',
            arrowprops=dict(arrowstyle='->', color='gray', lw=1))

ax.annotate('lóbulo\nexterno',
            xy=(2.5, psi_anti[900]),
            xytext=(3.3, -0.8),
            fontsize=9, ha='center',
            arrowprops=dict(arrowstyle='->', color='gray', lw=1))

ax.set_title('$\\sigma^*$ antienlazante', fontsize=12)
ax.set_xlabel('Posición', fontsize=10)
ax.set_ylabel('Función de onda $\\psi$', fontsize=10)
ax.set_ylim(-1.5, 1.5)
ax.set_xlim(-4, 4)
ax.set_xticks([])
ax.set_yticks([])
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.suptitle('Función de onda: enlazante vs antienlazante', fontsize=11, y=1.01)
plt.tight_layout()

outfile = os.path.join(out, 'orbitales_enlace.pdf')
plt.savefig(outfile, bbox_inches='tight', dpi=150)
plt.close()
print(f"Guardado: {outfile}")