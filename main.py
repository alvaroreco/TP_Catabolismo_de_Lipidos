import numpy as np
import matplotlib.pyplot as plt
from model.simulation import run_simulation
from model.parameters import HEPATIC_PARAMETERS
from model.parameters import CARDIAC_PARAMETERS
from analysis.flux import beta_flux
from model.species import SPECIES
from model.species import N_SPECIES

from graphics.plotting import (
    plot_carbon_flux,
    plot_nad,
    plot_fad,
    plot_atp,
    plot_acetylcoa,
    plot_oaa_malate,
    plot_ketones,
    plot_beta_flux,
    plot_ferricyanide
)



CARDIAC_PARAMETERS["rotenone"] = True
# =====================================================
# CONDICIONES INICIALES
# =====================================================

y0 = np.zeros(
    N_SPECIES
)

# =====================================
# SUSTRATO
# =====================================

y0[SPECIES["acylcoa_C16"]] = 50

# =====================================
# COFACTORES
# =====================================

y0[SPECIES["nad"]] = 100

y0[SPECIES["fad"]] = 100

# =====================================
# ATP
# =====================================

y0[SPECIES["atp"]] = 0

# =====================================
# OAA
# =====================================

y0[SPECIES["oxaloacetate"]] = 0

y0[SPECIES["malate"]] = 0

# =====================================
# CUERPOS CETONICOS
# =====================================

y0[SPECIES["acetoacetate"]] = 0
y0[SPECIES["bhb"]] = 0

# =====================================================
# SIMULACION
# =====================================================

result = run_simulation(
    y0,
    CARDIAC_PARAMETERS,
    tmax=500
)


# =====================================================
# VALIDACIONES
# =====================================================

print("Solver OK:", result.success)

print("Shape:", result.y.shape)

print(
    "AcetylCoA final:",
    result.y[
        SPECIES["acetylcoa"]
    ][-1]
)

print(
    "ATP final:",
    result.y[
        SPECIES["atp"]
    ][-1]
)

print("rotenona",
    HEPATIC_PARAMETERS["rotenone"]
)

print("oxalacetato",
    result.y[
        SPECIES["oxaloacetate"]
    ][-1]
)

print("malato",
    result.y[
        SPECIES["malate"]
    ][-1]
)

print("acetoacetato",
    result.y[
        SPECIES["acetoacetate"]
    ][-1]
)

print("bhb",
    result.y[
        SPECIES["bhb"]
    ][-1]
)

consumo_C16 = (
    y0[SPECIES["acylcoa_C16"]]
    -
    result.y[
        SPECIES["acylcoa_C16"]
    ][-1]
)

print(
    "C16 consumido:",
    consumo_C16
)



print("\nCadenas finales:\n")



print(
"Ferricyanuro:",
result.y[
SPECIES["ferricyanide_signal"]
][-1]
)

for chain in [16,14,12,10,8,6,4]:

    idx = SPECIES[
        f"acylcoa_C{chain}"
    ]

    print(
        f"C{chain}:",
        result.y[idx][-1]
    )

print("NAD+:",
    result.y[SPECIES["nad"]][-1]
)

print("NADH:",
    result.y[SPECIES["nadh"]][-1]
)

print(
    "FAD:",
    result.y[
        SPECIES["fad"]
    ][-1]
)

print(
    "FADH2:",
    result.y[
        SPECIES["fadh2"]
    ][-1]
)


nad_pool = (
    result.y[SPECIES["nad"]]
    +
    result.y[SPECIES["nadh"]]
)

redox = (
    result.y[SPECIES["nadh"]]
    /
    nad_pool
)


redox_ratio = (

    result.y[SPECIES["nad"]]

    /

    (

        result.y[SPECIES["nad"]]

        +

        result.y[SPECIES["nadh"]]

    )

)

flux = beta_flux(result)

plot_carbon_flux(result)

plot_nad(result)

plot_fad(result)

plot_atp(result)

plot_acetylcoa(result)

plot_oaa_malate(result)

plot_ketones(result)

plot_beta_flux(
    result,
    flux
)



plt.show()

plt.figure()

plt.plot(
    result.t,
    redox_ratio
)

plt.title(
    "NAD/(NAD+NADH)"
)

plot_ferricyanide(
    result
)

plt.show()

