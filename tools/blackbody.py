"""
Cosmos Engine — Blackbody Radiation Toolkit
============================================
Calculate blackbody radiation spectra using Planck's law.

Author: Saheb Karami
License: MIT
"""

import math
import numpy as np

# Physical constants
H = 6.62607015e-34   # Planck constant (J*s)
C = 299_792_458       # Speed of light (m/s)
KB = 1.380649e-23     # Boltzmann constant (J/K)


class Blackbody:
    """Calculate blackbody radiation properties."""

    def spectral_radiance(self, wavelength_m: float, temperature_k: float) -> float:
        """Planck's law: spectral radiance per unit wavelength."""
        wl = wavelength_m
        T = temperature_k
        exponent = (H * C) / (wl * KB * T)
        return (2 * H * C**2) / (wl**5) * 1 / (math.exp(exponent) - 1)

    def peak_wavelength(self, temperature_k: float) -> float:
        """Wien's displacement law: peak emission wavelength in meters."""
        b = 2.8977719e-3  # Wien's displacement constant (m*K)
        return b / temperature_k

    def total_power(self, temperature_k: float) -> float:
        """Stefan-Boltzmann law: total power radiated per unit area (W/m^2)."""
        sigma = 5.670374e-8  # Stefan-Boltzmann constant
        return sigma * temperature_k**4

    def luminosity(self, radius_m: float, temperature_k: float) -> float:
        """Calculate luminosity of a star (assuming blackbody) in Watts."""
        return 4 * math.pi * radius_m**2 * self.total_power(temperature_k)

    def spectrum(self, temperature_k: float, wl_min_nm: float = 100, wl_max_nm: float = 3000,
                 n_points: int = 500) -> tuple:
        """Generate a blackbody spectrum. Returns (wavelengths_nm, radiance_values)."""
        wavelengths = np.linspace(wl_min_nm, wl_max_nm, n_points) * 1e-9
        radiances = np.array([self.spectral_radiance(wl, temperature_k) for wl in wavelengths])
        return wavelengths * 1e9, radiances


# Stellar classification reference
STELLAR_CLASSES = {
    'O': {'temp_range': (30000, 50000), 'color': 'Blue', 'example': 'Zeta Ophiuchi'},
    'B': {'temp_range': (10000, 30000), 'color': 'Blue-white', 'example': 'Rigel'},
    'A': {'temp_range': (7500, 10000),  'color': 'White', 'example': 'Sirius A'},
    'F': {'temp_range': (6000, 7500),   'color': 'Yellow-white', 'example': 'Procyon'},
    'G': {'temp_range': (5200, 6000),   'color': 'Yellow', 'example': 'The Sun'},
    'K': {'temp_range': (3700, 5200),   'color': 'Orange', 'example': 'Arcturus'},
    'M': {'temp_range': (2400, 3700),   'color': 'Red', 'example': 'Betelgeuse'},
}


if __name__ == '__main__':
    bb = Blackbody()

    print("=" * 55)
    print("Cosmos Engine - Blackbody Radiation Demo")
    print("=" * 55)

    T_sun = 5778  # K
    peak_sun = bb.peak_wavelength(T_sun) * 1e9
    power_sun = bb.total_power(T_sun)
    lum_sun = bb.luminosity(6.9634e8, T_sun)

    print(f"\nThe Sun (T = {T_sun} K):")
    print(f"   Peak wavelength: {peak_sun:.1f} nm (green light)")
    print(f"   Surface power: {power_sun / 1e6:.1f} MW/m^2")
    print(f"   Luminosity: {lum_sun / 3.828e26:.2f} L_sun")

    T_betel = 3500
    peak_betel = bb.peak_wavelength(T_betel) * 1e9
    print(f"\nBetelgeuse (T = {T_betel} K):")
    print(f"   Peak wavelength: {peak_betel:.1f} nm (infrared/red)")

    print(f"\nStellar Classification:")
    print(f"   {'Class':<6} {'Temp (K)':<15} {'Color':<15} {'Example':<20}")
    print(f"   {'-'*6} {'-'*15} {'-'*15} {'-'*20}")
    for cls, info in STELLAR_CLASSES.items():
        temp_str = f"{info['temp_range'][0]:,}-{info['temp_range'][1]:,}"
        print(f"   {cls:<6} {temp_str:<15} {info['color']:<15} {info['example']:<20}")

    print("\n" + "=" * 55)
