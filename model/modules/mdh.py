from model.species import SPECIES


def mdh_step(
        y,
        p,
        dydt):

    OAA = y[SPECIES["oxaloacetate"]]

    Malate = y[SPECIES["malate"]]

    NAD = y[SPECIES["nad"]]

    NADH = y[SPECIES["nadh"]]

    v_mdh = (

        p["k_mdh_forward"]
        * OAA
        * NADH

        -

        p["k_mdh_reverse"]
        * Malate
        * NAD

    )

    dydt[SPECIES["oxaloacetate"]] -= v_mdh

    dydt[SPECIES["malate"]] += v_mdh

    dydt[SPECIES["nad"]] += v_mdh

    dydt[SPECIES["nadh"]] -= v_mdh