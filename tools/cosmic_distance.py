"""
Cosmos Engine — Cosmic Distance Toolkit
=======================================
Tools for calculating cosmic distances using various
astronomical distance measurement methods.

Author: Saheb Karami
License: MIT
"""

import math

# Constants
C = 299_792_458          # Speed of light (m/s)
PARSEC = 3.0857e16        # 1 parsec in meters
LIGHT_YEAR = 9.4607e15    # 1 light-year in meters
AU = 1.496e11             # 1 AU in meters
H0 = 70                   # Hubble constant (km/s/Mpc)


class CosmicDistance:
    """Calculate cosmic distances using various methods."""

    def parallax_to_parsecs(self, parallax_mas: float) -> float:
        """Convert parallax angle (milliarcseconds) to distance in parsecs."""
        parallax_arcsec = parallax_mas / 1000
        if parallax_arcsec <= 0:
            return float('inf')
        return 1 / parallax_arcsec

    def parsecs_to_lightyears(self, parsecs: float) -> float:
        """Convert parsecs to light-years."""
        return parsecs * (PARSEC / LIGHT_YEAR)

    def parsecs_to_au(self, parsecs: float) -> float:
        """Convert parsecs to astronomical units."""
        return parsecs * (PARSEC / AU)

    def hubble_distance(self, redshift: float) -> float:
        """Calculate distance using Hubble's Law (for moderate redshift) in Mpc."""
        v = redshift * C / 1000  # velocity in km/s
        return v / H0

    def luminosity_distance(self, redshift: float) -> float:
        """Approximate luminosity distance for small redshifts in Mpc."""
        return self.hubble_distance(redshift) * (1 + redshift)

    def distance_modulus(self, distance_pc: float) -> float:
        """Calculate distance modulus: m - M = 5*log10(d) - 5."""
        return 5 * math.log10(distance_pc) - 5

    def absolute_magnitude(self, apparent_mag: float, distance_pc: float) -> float:
        """Calculate absolute magnitude from apparent magnitude."""
        return apparent_mag - self.distance_modulus(distance_pc)

    def light_travel_time(self, distance_ly: float) -> float:
        """Calculate light travel time in years."""
        return distance_ly


# Famous cosmic distances reference
FAMOUS_DISTANCES = {
    'Proxima Centauri':     {'distance_ly': 4.24,    'method': 'Parallax'},
    'Sirius':               {'distance_ly': 8.6,     'method': 'Parallax'},
    'Vega':                 {'distance_ly': 25.04,   'method': 'Parallax'},
    'Orion Nebula':         {'distance_ly': 1344,    'method': 'Parallax (cluster)'},
    'Galactic Center':      {'distance_ly': 26000,   'method': 'Stellar orbits'},
    'Andromeda Galaxy':     {'distance_ly': 2_537_000, 'method': 'Cepheids + TRGB'},
    'Virgo Cluster':        {'distance_ly': 53_000_000, 'method': 'Cepheids + SBF'},
    'Coma Cluster':         {'distance_ly': 321_000_000, 'method': 'Tully-Fisher'},
}


if __name__ == '__main__':
    cd = CosmicDistance()

    print("=" * 55)
    print("Cosmos Engine - Cosmic Distance Demo")
    print("=" * 55)

    p_proxima = 768.07  # mas (Gaia DR3)
    d_pc = cd.parallax_to_parsecs(p_proxima)
    d_ly = cd.parsecs_to_lightyears(d_pc)
    print(f"\nProxima Centauri:")
    print(f"   Parallax: {p_proxima} mas")
    print(f"   Distance: {d_pc:.2f} pc = {d_ly:.2f} ly")

    z = 0.01
    d_hubble = cd.hubble_distance(z)
    print(f"\nGalaxy at redshift z={z}:")
    print(f"   Hubble distance: {d_hubble:.1f} Mpc")

    d_andromeda_pc = 778_000
    dm = cd.distance_modulus(d_andromeda_pc)
    print(f"\nAndromeda Galaxy:")
    print(f"   Distance: {d_andromeda_pc:,} pc")
    print(f"   Distance modulus: {dm:.2f} mag")

    print(f"\nFamous Cosmic Distances:")
    print(f"   {'Object':<22} {'Distance (ly)':<18} {'Method':<25}")
    print(f"   {'-'*22} {'-'*18} {'-'*25}")
    for name, info in FAMOUS_DISTANCES.items():
        dist_str = f"{info['distance_ly']:,}"
        print(f"   {name:<22} {dist_str:<18} {info['method']:<25}")

    print("\n" + "=" * 55)
