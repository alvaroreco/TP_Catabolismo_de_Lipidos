
from model.species import SPECIES


def etc_step(
        y,
        p,
        dydt):
    NADH = y[SPECIES["nadh"]]

    FADH2 = y[SPECIES["fadh2"]]

    if p["rotenone"]:

        v_etc_nadh = 0

        if p["ferricyanide"]:
            v_etc_fadh2 = 0
        else:
            v_etc_fadh2 = (
                p["k_etc_fadh2"]
                * FADH2
            )
    else:

        v_etc_nadh = (
            p["k_etc_nadh"]
            * NADH
        )

        if p["ferricyanide"]:
            v_etc_fadh2 = 0
        else:
            v_etc_fadh2 = (
                p["k_etc_fadh2"]
                * FADH2
            )

    dydt[SPECIES["nad"]] += v_etc_nadh
    dydt[SPECIES["nadh"]] -= v_etc_nadh

    dydt[SPECIES["fad"]] += v_etc_fadh2
    dydt[SPECIES["fadh2"]] -= v_etc_fadh2
    ATP_SCALING = 1.18

    dydt[SPECIES["atp"]] += ATP_SCALING * (
        2.5 * v_etc_nadh
        +
        1.5 * v_etc_fadh2
    )
