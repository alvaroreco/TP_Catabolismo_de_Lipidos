from model.species import SPECIES


def etf_step(
        y,
        p,
        dydt):

    FADH2 = y[SPECIES["fadh2"]]

    v_etf = (
        p["k_etf"]
        * FADH2
    )

    dydt[SPECIES["fadh2"]] -= v_etf

    dydt[SPECIES["fad"]] += v_etf