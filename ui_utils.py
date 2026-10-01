import numpy as np

from model.species import (
    SPECIES,
    N_SPECIES
)


def build_initial_conditions(
        chain_length,
        substrate_conc,
        oaa,
        acac,
        bhb):

    y0 = np.zeros(
        N_SPECIES
    )

    y0[
        SPECIES[
            f"acylcoa_C{chain_length}"
        ]
    ] = substrate_conc

    y0[
        SPECIES["nad"]
    ] = 100

    y0[
        SPECIES["fad"]
    ] = 100

    y0[
        SPECIES["oxaloacetate"]
    ] = oaa

    y0[
        SPECIES["acetoacetate"]
    ] = acac

    y0[
        SPECIES["bhb"]
    ] = bhb

    return y0