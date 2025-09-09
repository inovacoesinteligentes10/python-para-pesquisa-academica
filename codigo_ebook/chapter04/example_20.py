# -*- coding: utf-8 -*-
"""
Código extraído do Capítulo 4
Seção: Bootstrap: Estimando Distribuições
Linha original no arquivo LaTeX: 772

Este código foi extraído automaticamente do arquivo chapter4.tex
"""
import numpy as np
import matplotlib.pyplot as plt


print("\nEXEMPLO 3: DIFERENCA ENTRE MEDIAS")
print("=" * 30)
grupo1 = np.random.normal(50, 10, 30)
grupo2 = np.random.normal(55, 12, 25)

# Bootstrap para diferenca entre grupos (versao simplificada)
def bootstrap_grupos(grupo1, grupo2, n_bootstrap=10000):
    """Bootstrap especifico para diferenca entre grupos"""
    diffs = []
    for _ in range(n_bootstrap):
        boot_g1 = resample(grupo1)
        boot_g2 = resample(grupo2)
        diff = np.mean(boot_g1) - np.mean(boot_g2)
        diffs.append(diff)
    return np.array(diffs)

diffs_boot = bootstrap_grupos(grupo1, grupo2)
diff_original = np.mean(grupo1) - np.mean(grupo2)

print(f"Diferenca original: {diff_original:.3f}")
print(f"IC 95% bootstrap: [{np.percentile(diffs_boot, 2.5):.3f}, {np.percentile(diffs_boot, 97.5):.3f}]")

# Visualizar distribuicao das diferencas
plt.figure(figsize=(8, 5))
plt.hist(diffs_boot, bins=50, alpha=0.7, density=True)
plt.axvline(diff_original, color='red', linestyle='--', label=f'Diferenca observada: {diff_original:.3f}')
plt.axvline(np.percentile(diffs_boot, 2.5), color='green', linestyle='--', alpha=0.7)
plt.axvline(np.percentile(diffs_boot, 97.5), color='green', linestyle='--', alpha=0.7, label='IC 95%')
plt.xlabel('Diferenca entre Medias')
plt.ylabel('Densidade')
plt.title('Bootstrap: Diferenca entre Grupos')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("temp_plot.png", bbox_inches="tight")
plt.close()  # plt.show() substituído para execução não-interativa
