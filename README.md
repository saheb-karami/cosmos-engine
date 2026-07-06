<div align="center">

# 🌌 Cosmos Engine

### *A Data-Driven Laboratory for Exploring the Universe*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)

> *"The cosmos is within us. We are made of star-stuff. We are a way for the universe to know itself."*  
> — Carl Sagan

</div>

---

## 🔭 What is Cosmos Engine?

**Cosmos Engine** is an open-source data science laboratory for exploring the universe through code. We combine real astronomical datasets, physics simulations, and data visualization to make the cosmos accessible, understandable, and awe-inspiring.

From exoplanet hunting to black hole physics, from orbital mechanics to cosmic web visualization — this is where data meets the stars.

---

## 🗺️ Repository Structure

```
cosmos-engine/
│
├── 📁 datasets/           # Curated astronomical datasets
│   ├── exoplanets/         # NASA exoplanet archive data
│   ├── stars/              # Stellar catalogs (Hipparcos, Gaia)
│   └── blackholes/         # Black hole observations
│
├── 📁 tools/               # Python tools & utilities
│   ├── orbital_mechanics.py
│   ├── blackbody.py
│   └── cosmic_distance.py
│
├── 📁 simulations/         # Physics simulations
│   ├── n_body/             # N-body gravitational simulations
│   ├── orbits/             # Orbital mechanics simulator
│   └── cosmology/          # Universe expansion models
│
├── 📁 visualizations/      # Data visualizations
│   ├── star_maps/          # Interactive star charts
│   ├── exoplanet_plots/    # Exoplanet discovery trends
│   └── cosmic_web/         # Large-scale structure plots
│
├── 📁 catalogs/            # Object catalogs & references
│   ├── messier.md          # Messier object catalog
│   ├── ngc.md              # NGC catalog highlights
│   └── constellations.md   # Constellation guide
│
├── 📁 notebooks/           # Jupyter notebooks with analysis
│   ├── exoplanet_hunting.ipynb
│   ├── stellar_evolution.ipynb
│   └── cosmic_distances.ipynb
│
└── 📁 docs/                # Documentation & guides
    ├── getting_started.md
    └── data_sources.md
```

---

## 🚀 Featured Projects

| Project | Description | Status |
|---------|-------------|--------|
| 🪐 **Exoplanet Hunter** | Analyze NASA Kepler/TESS data to find exoplanets | 🟢 Active |
| 🕳️ **Black Hole Lab** | Simulate Schwarzschild & Kerr black holes | 🟡 In Progress |
| 🌟 **Stellar Lifecycle** | Model star formation, evolution, and death | 🟢 Active |
| 🛰️ **Orbital Playground** | Simulate orbits, transfers, and gravitational assists | 🟡 In Progress |
| 🕸️ **Cosmic Web** | Visualize the large-scale structure of the universe | 📋 Planned |
| 🌠 **Meteor Shower Predictor** | Analyze meteor shower data and predict peaks | 📋 Planned |

---

## 🌟 The Cosmic Scale

```
Scale of the Universe (logarithmic)

Human          | 10^0  m  | *
Earth          | 10^7  m  | **
Sun            | 10^9  m  | ***
Solar System   | 10^13 m  | ****
Light Year     | 10^16 m  | *****
Galaxy         | 10^21 m  | ******
Galaxy Cluster | 10^23 m  | *******
Observable Uni | 10^27 m  | ************************************
```

---

## 🛠️ Quick Start

### Installation

```bash
git clone https://github.com/saheb-karami/cosmos-engine.git
cd cosmos-engine
pip install -r requirements.txt
```

### Calculate orbital velocity

```python
from tools.orbital_mechanics import OrbitalMechanics

orb = OrbitalMechanics()

# ISS orbital velocity
v_iss = orb.circular_orbit_velocity(altitude_km=408, central_body='Earth')
print(f"ISS orbital velocity: {v_iss:.2f} km/s")
# Output: ISS orbital velocity: 7.67 km/s

# Geostationary orbit altitude
h_geo = orb.geostationary_altitude()
print(f"Geostationary altitude: {h_geo:,.0f} km")
# Output: Geostationary altitude: 35,786 km
```

---

## 📊 Key Numbers: Our Universe

| Quantity | Value | Scale |
|----------|-------|-------|
| Observable universe diameter | ~93 billion light-years | 8.8 × 10^26 m |
| Number of galaxies | ~2 trillion | 2 × 10^12 |
| Stars in our galaxy | ~100–400 billion | 10^11–10^12 |
| Exoplanets confirmed | 5,000+ (and counting) | — |
| Age of the universe | 13.8 billion years | 4.35 × 10^17 s |
| Speed of light | 299,792 km/s | 3 × 10^8 m/s |
| Hubble constant | ~70 km/s/Mpc | H0 ~ 70 |
| Dark matter fraction | ~27% of universe | — |
| Dark energy fraction | ~68% of universe | — |
| Ordinary matter | ~5% of universe | — |

---

## 🕳️ Black Holes: A Quick Dive

**Schwarzschild Radius** (event horizon):
```
R_s = 2GM / c^2

For the Sun:   R_s ~ 3 km    (if compressed to 3km, it becomes a black hole)
For the Earth: R_s ~ 9 mm    (if compressed to 9mm, it becomes a black hole)
For a human:   R_s ~ 10^-25 m (way smaller than a proton)
```

---

## 🪐 Orbital Mechanics Cheat Sheet

| Maneuver | Formula | Use Case |
|----------|---------|----------|
| Circular orbit velocity | v = sqrt(GM/r) | Stable orbit |
| Escape velocity | v = sqrt(2GM/r) | Leave gravity well |
| Hohmann transfer | dv = sqrt(GM/r1)(sqrt(2r2/(r1+r2)) - 1) | Transfer between orbits |
| Vis-viva equation | v^2 = GM(2/r - 1/a) | Any orbit, any point |
| Orbital period | T = 2*pi*sqrt(a^3/GM) | Time per orbit |

---

## 📚 Data Sources

| Source | Description | Link |
|--------|-------------|------|
| NASA Exoplanet Archive | Confirmed exoplanets | [archive.stsci.edu](https://exoplanetarchive.ipac.caltech.edu/) |
| Gaia Mission | 1.7 billion stars | [esa.int/gaia](https://www.cosmos.esa.int/web/gaia) |
| Hipparcos Catalog | 118,000 stars | [hipparcoscatalog.com](https://hipparcoscatalog.com/) |
| NASA ADS | Astronomy papers | [ui.adsabs.harvard.edu](https://ui.adsabs.harvard.edu/) |
| Sloan Digital Sky Survey | Galaxy survey | [sdss.org](https://www.sdss.org/) |
| ESA Euclid | Dark universe | [euclid.esa.int](https://www.euclid-ec.org/) |

---

## 🤝 Contributors

| Contributor | Role |
|-------------|------|
| [Saheb Karami](https://github.com/saheb-karami) | 🌌 Creator & Maintainer |
| [Sabi Karami](https://github.com/sabi-karami) | 🔭 Co-Maintainer |

---

## 📜 License

MIT License — see [LICENSE](LICENSE) file.

The universe is open source. 🌌

---

<div align="center">

**Made with curiosity and 🌠 by [Saheb Karami](https://github.com/saheb-karami) & [Sabi Karami](https://github.com/sabi-karami)**

*"Somewhere, something incredible is waiting to be known."* — Carl Sagan

⭐ **Star this repo if you love space!** ⭐

</div>
