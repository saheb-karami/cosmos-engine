# 🪐 Exoplanet Dataset

This directory contains tools and data for exploring confirmed exoplanets from NASA's Exoplanet Archive.

## Data Source

- **NASA Exoplanet Archive**: [exoplanetarchive.ipac.caltech.edu](https://exoplanetarchive.ipac.caltech.edu/)
- Last updated: 2025
- Format: CSV (downloadable from NASA)

## Key Columns

| Column | Description | Unit |
|--------|-------------|------|
| `pl_name` | Planet name | — |
| `hostname` | Host star name | — |
| `pl_rade` | Planet radius | Earth radii |
| `pl_masse` | Planet mass | Earth masses |
| `pl_eqt` | Equilibrium temperature | K |
| `pl_orbsmax` | Semi-major axis | AU |
| `pl_orbper` | Orbital period | days |
| `st_teff` | Star effective temperature | K |
| `st_mass` | Star mass | Solar masses |
| `st_rad` | Star radius | Solar radii |
| `sy_dist` | System distance | parsecs |

## Notable Exoplanets

| Planet | Host Star | Radius (Earth) | Temp (K) | Discovered |
|--------|-----------|----------------|----------|------------|
| Proxima Centauri b | Proxima Centauri | ~1.1 | 234 | 2016 |
| TRAPPIST-1e | TRAPPIST-1 | 0.92 | 251 | 2017 |
| Kepler-452b | Kepler-452 | 1.63 | 265 | 2015 |
| Kepler-186f | Kepler-186 | 1.17 | 188 | 2014 |
| K2-18b | K2-18 | 2.61 | 265 | 2015 |

## Usage

```python
import pandas as pd

df = pd.read_csv('datasets/exoplanets/exoplanets.csv')

# Find potentially habitable planets
habitable = df[
    (df['pl_rade'] < 2.0) &
    (df['pl_eqt'] > 200) &
    (df['pl_eqt'] < 320)
]
print(f"Potentially habitable: {len(habitable)}")
```
