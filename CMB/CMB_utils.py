
# Claudia Scóccola - marzo 2025 

import numpy as np
import matplotlib.pyplot as plt
import healpy as hp
import camb
from camb import model, initialpower



def check_mean_temperature(cmb_map):
    """Carga un mapa del CMB y muestra su temperatura media."""
    mean_temp = np.mean(cmb_map)
    print(f"Temperatura media del mapa: {mean_temp:.5f} mK")
    return mean_temp




# Sección 1: Carga y visualización de mapas del CMB

def plot_cmb_map(cmb_map):
    """Carga y visualiza un mapa del CMB desde el numpy array donde ya fue guardado."""
    hp.mollview(cmb_map, title='Mapa del CMB', unit='mK', cmap='coolwarm')
    print("Ajustar los valores min y max del display.")
    plt.show()

    

# Sección 2: Estadísticas básicas del mapa del CMB

def analyze_cmb_statistics(cmb_map):
    """Calcula la temperatura media y la desviación estándar del mapa."""
    mean_temp = np.mean(cmb_map)
    std_temp = np.std(cmb_map)
    print(f"Temperatura media: {mean_temp:.5f} mK")
    print(f"Desviación estándar: {std_temp:.5f} mK")

   


# Sección 3: Análisis del espectro angular de potencias

def compute_power_spectrum(cmb_map):
    """Calcula y visualiza el espectro de potencias del mapa CMB."""
    cl = hp.anafast(cmb_map)
    ell = np.arange(len(cl))
    plt.figure(figsize=(8, 5))
    plt.plot(ell, cl * ell * (ell + 1) / (2 * np.pi), label='C_l')
    plt.xlabel('$\ell$')
    plt.ylabel('$\ell(\ell+1)C_\ell / 2\pi$')
    plt.title('Espectro de Potencias TT')
    plt.legend()
    plt.show()
    return ell, cl


# Sección 4: Uso de CAMB para generar espectros teóricos

def generate_camb_spectrum(H0= 67.5,ombh2= 0.022,omch2= 0.122,ns= 0.965):
    """Genera el espectro de potencias con CAMB."""
    pars = camb.CAMBparams()
    pars.set_cosmology(H0=H0, ombh2=ombh2, omch2=omch2)
    pars.InitPower.set_params(ns=ns)
    print("Los parámetros cosmológicos utilizados son:")
    print("H0, ombh2, omch2, ns = ", H0, ombh2, omch2, ns )
    pars.set_for_lmax(2500, lens_potential_accuracy=0)
    results = camb.get_results(pars)
    powers = results.get_cmb_power_spectra(pars, CMB_unit='muK')
    tt = powers['total'][:, 0]
    ell = np.arange(len(tt))
    plt.plot(ell, tt, label='TT (Teórico)')
    plt.xlabel('$\ell$')
    plt.ylabel('$C_\ell$')
    plt.title('Espectro de Potencias TT - CAMB')
    plt.legend()
    plt.show()
    return ell, tt


    
