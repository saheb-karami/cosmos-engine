"""
Cosmos Engine — Orbital Mechanics Toolkit
==========================================
Tools for calculating orbital velocities, transfer orbits,
and gravitational parameters.

Author: Saheb Karami
License: MIT
"""

import math

# Gravitational constant (m^3 kg^-1 s^-2)
G = 6.67430e-11

# Speed of light (m/s)
C = 299_792_458

# Astronomical unit (meters)
AU = 1.496e11

# Body parameters: (mass in kg, radius in km)
BODIES = {
    'Sun':     {'mass': 1.989e30, 'radius_km': 696_340},
    'Mercury': {'mass': 3.301e23, 'radius_km': 2_440},
    'Venus':   {'mass': 4.867e24, 'radius_km': 6_052},
    'Earth':   {'mass': 5.972e24, 'radius_km': 6_371},
    'Mars':    {'mass': 6.417e23, 'radius_km': 3_390},
    'Jupiter': {'mass': 1.898e27, 'radius_km': 69_911},
    'Saturn':  {'mass': 5.683e26, 'radius_km': 58_232},
    'Uranus':  {'mass': 8.681e25, 'radius_km': 25_362},
    'Neptune': {'mass': 1.024e26, 'radius_km': 24_622},
    'Moon':    {'mass': 7.342e22, 'radius_km': 1_737},
}


class OrbitalMechanics:
    """Calculate orbital mechanics for celestial bodies."""

    def circular_orbit_velocity(self, altitude_km: float, central_body: str = 'Earth') -> float:
        """Calculate circular orbital velocity in km/s."""
        body = BODIES[central_body]
        r = (body['radius_km'] + altitude_km) * 1000
        v = math.sqrt(G * body['mass'] / r)
        return v / 1000

    def escape_velocity(self, altitude_km: float = 0, central_body: str = 'Earth') -> float:
        """Calculate escape velocity in km/s."""
        body = BODIES[central_body]
        r = (body['radius_km'] + altitude_km) * 1000
        v = math.sqrt(2 * G * body['mass'] / r)
        return v / 1000

    def orbital_period(self, semi_major_axis_km: float, central_body: str = 'Earth') -> float:
        """Calculate orbital period in minutes using Kepler's third law."""
        body = BODIES[central_body]
        a = semi_major_axis_km * 1000
        T = 2 * math.pi * math.sqrt(a**3 / (G * body['mass']))
        return T / 60

    def geostationary_altitude(self) -> float:
        """Calculate geostationary orbit altitude for Earth in km."""
        earth = BODIES['Earth']
        T = 86164  # Earth's sidereal day in seconds
        a = (G * earth['mass'] * T**2 / (4 * math.pi**2)) ** (1/3)
        altitude = a / 1000 - earth['radius_km']
        return altitude

    def hohmann_transfer(self, r1_km: float, r2_km: float, central_body: str = 'Earth') -> dict:
        """Calculate Hohmann transfer orbit between two circular orbits."""
        body = BODIES[central_body]
        mu = G * body['mass']
        r1 = r1_km * 1000
        r2 = r2_km * 1000

        v1 = math.sqrt(mu / r1)
        v2 = math.sqrt(mu / r2)
        v_transfer_1 = math.sqrt(mu * (2/r1 - 2/(r1 + r2)))
        v_transfer_2 = math.sqrt(mu * (2/r2 - 2/(r1 + r2)))

        dv1 = abs(v_transfer_1 - v1)
        dv2 = abs(v2 - v_transfer_2)
        a_transfer = (r1 + r2) / 2
        T_transfer = math.pi * math.sqrt(a_transfer**3 / mu)

        return {
            'delta_v1_km_s': dv1 / 1000,
            'delta_v2_km_s': dv2 / 1000,
            'total_delta_v_km_s': (dv1 + dv2) / 1000,
            'transfer_time_hours': T_transfer / 3600,
        }

    def schwarzschild_radius(self, mass_kg: float) -> float:
        """Calculate Schwarzschild radius (event horizon) in meters."""
        return 2 * G * mass_kg / C**2


if __name__ == '__main__':
    orb = OrbitalMechanics()

    print("=" * 50)
    print("Cosmos Engine - Orbital Mechanics Demo")
    print("=" * 50)

    v_iss = orb.circular_orbit_velocity(408, 'Earth')
    print(f"\nISS orbital velocity: {v_iss:.2f} km/s")

    h_geo = orb.geostationary_altitude()
    print(f"Geostationary altitude: {h_geo:,.0f} km")

    v_esc = orb.escape_velocity(0, 'Earth')
    print(f"Earth escape velocity: {v_esc:.2f} km/s")

    r_leo = BODIES['Earth']['radius_km'] + 400
    r_geo = BODIES['Earth']['radius_km'] + h_geo
    transfer = orb.hohmann_transfer(r_leo, r_geo, 'Earth')
    print(f"LEO->GEO transfer: dv={transfer['total_delta_v_km_s']:.2f} km/s, "
          f"time={transfer['transfer_time_hours']:.1f} hours")

    r_s_sun = orb.schwarzschild_radius(BODIES['Sun']['mass'])
    print(f"Sun's Schwarzschild radius: {r_s_sun:.0f} m ({r_s_sun/1000:.1f} km)")

    r_s_earth = orb.schwarzschild_radius(BODIES['Earth']['mass'])
    print(f"Earth's Schwarzschild radius: {r_s_earth*1000:.2f} mm")

    print("\n" + "=" * 50)
