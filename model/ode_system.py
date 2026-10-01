import numpy as np

from model.species import (
    N_SPECIES,
    SPECIES
)

from model.modules.beta_oxidation import (
    beta_oxidation_step
)

from model.modules.krebs import (
    krebs_step
)

from model.modules.etc import (
    etc_step
)

from model.modules.mdh import (
    mdh_step
)

from model.modules.ketones import (
    ketone_step
)

from model.modules.etf import (
    etf_step
)



def derivatives(
        t,
        y,
        p):

    dydt = np.zeros(
        N_SPECIES
    )

    # =====================================
    # β-OXIDACION
    # =====================================

    flux = beta_oxidation_step(
        y,
        p,
        dydt
    )

    if p["ferricyanide"]:
        dydt[
            SPECIES["ferricyanide_signal"]
        ] = flux
    else:
        dydt[
            SPECIES["ferricyanide_signal"]
        ] = 0
    # =====================================
    # KREBS
    # =====================================

    krebs_step(
        y,
        p,
        dydt
    )

    # =====================================
    # MDH
    # =====================================

    mdh_step(
        y,
        p,
        dydt
    )

    # =====================================
    # ACAC <-> BHB
    # =====================================

    ketone_step(
        y,
        p,
        dydt
    )

    # =====================================
    # ETC
    # =====================================

    etc_step(
        y,
        p,
        dydt
    )
    
    # =====================================
    # ETF
    # =====================================

    etf_step(
        y,
        p,
        dydt
    )

    return dydt