from model.species import SPECIES
from model.species import CHAINS


def beta_flux(result):

    flux = []

    for i in range(len(result.t)):

        total = 0

        for chain in CHAINS:

            idx = SPECIES[
                f"acylcoa_C{chain}"
            ]

            total += result.y[idx][i]

        flux.append(total)

    return flux