from model.species import SPECIES


def ketone_step(
        y,
        p,
        dydt):

    AcAc = y[SPECIES["acetoacetate"]]

    BHB = y[SPECIES["bhb"]]

    NAD = y[SPECIES["nad"]]

    NADH = y[SPECIES["nadh"]]

    # ==========================
    # BDH
    # ==========================

    v_bdh = (

        p["k_bdh_forward"]
        * AcAc
        * NADH

        -

        p["k_bdh_reverse"]
        * BHB
        * NAD

    )

    dydt[SPECIES["acetoacetate"]] -= v_bdh

    dydt[SPECIES["bhb"]] += v_bdh

    dydt[SPECIES["nad"]] += v_bdh

    dydt[SPECIES["nadh"]] -= v_bdh

    # ==========================
    # UTILIZACION DE AcAc
    # ==========================

    v_ketone_use = (

        p["k_ketone_use"]
        * AcAc

    )

    dydt[SPECIES["acetoacetate"]] -= v_ketone_use

    # 1 AcAc → 2 Acetil-CoA

    dydt[SPECIES["acetylcoa"]] += (

        2.0
        *
        v_ketone_use

    )