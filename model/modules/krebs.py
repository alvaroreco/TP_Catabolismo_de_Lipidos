from model.species import SPECIES


def krebs_step(
        y,
        p,
        dydt):

    acetyl = y[SPECIES["acetylcoa"]]

    NAD = y[SPECIES["nad"]]

    NADH = y[SPECIES["nadh"]]

    FAD = y[SPECIES["fad"]]

    malate = y[SPECIES["malate"]]

    redox_ratio = (
        NADH /
        (
            NADH + NAD + 1e-9
        )
    )

    acetyl_factor = (
        1
        +
        0.05 * malate
    )

    v_krebs = (

        p["k_krebs"]
        * acetyl
        * acetyl_factor
        * NAD
        * FAD
        * (1 - redox_ratio)

    )

    dydt[SPECIES["acetylcoa"]] -= v_krebs

    dydt[SPECIES["nad"]] -= (
        3 * v_krebs
    )

    dydt[SPECIES["fad"]] -= (
        1 * v_krebs
    )

    dydt[SPECIES["nadh"]] += (
        3 * v_krebs
    )

    dydt[SPECIES["fadh2"]] += (
        1 * v_krebs
    )

    dydt[SPECIES["atp"]] += (
        1 * v_krebs
    )