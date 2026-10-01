import numpy as np

from model.species import SPECIES
from model.species import CHAINS


def beta_oxidation_step(
        y,
        p,
        dydt):

    FAD = y[SPECIES["fad"]]
    NAD = y[SPECIES["nad"]]
    NADH = y[SPECIES["nadh"]]

    redox_factor = (
        NAD
        /
        (
            NAD
            + NADH
            + 1e-9
        )
    )

    flux = 0

    for chain in CHAINS:

        acyl = SPECIES[f"acylcoa_C{chain}"]

        enoyl = SPECIES[f"enoyl_C{chain}"]

        hydroxy = SPECIES[f"hydroxy_C{chain}"]

        keto = SPECIES[f"keto_C{chain}"]

        acyl_conc = y[acyl]

        enoyl_conc = y[enoyl]

        hydroxy_conc = y[hydroxy]

        keto_conc = y[keto]

        v_acad = (

            p["k_acad"]
            * acyl_conc
            * FAD

            *

            (
                0.01
                + redox_factor
            )

        )


        v_ech = (
            p["k_ech"]
            * enoyl_conc
        )

        v_had = (
            p["k_had"]
            * hydroxy_conc
            * NAD
        )

        v_kat = (
            p["k_kat"]
            * keto_conc
        )

        flux += v_acad

        dydt[acyl] -= v_acad

        dydt[enoyl] += v_acad
        dydt[enoyl] -= v_ech

        dydt[hydroxy] += v_ech
        dydt[hydroxy] -= v_had

        dydt[keto] += v_had
        dydt[keto] -= v_kat

        dydt[SPECIES["fad"]] -= v_acad
        dydt[SPECIES["fadh2"]] += v_acad

        dydt[SPECIES["nad"]] -= v_had
        dydt[SPECIES["nadh"]] += v_had

        dydt[SPECIES["acetylcoa"]] += v_kat

        next_chain = chain - 2

        if next_chain >= 4:

            next_acyl = SPECIES[
                f"acylcoa_C{next_chain}"
            ]

            dydt[next_acyl] += v_kat

        else:

            dydt[SPECIES["acetylcoa"]] += v_kat

    return flux