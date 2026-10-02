import pandas as pd

from model.species import SPECIES


def simulation_summary(
        result,
        y0,
        vqs=None):

    return pd.DataFrame({

        "Variable":[

            "ATP generado",
            "AcetylCoA final",


            "NAD+",
            "NADH",

            "FAD",
            "FADH2",

            "Oxaloacetato",
            "Malato",

            "Acetoacetato",
            "β-Hidroxibutirato",
            "Ferricianuro final",
            "Velocidad de reducción de ferricianuro"

        ],

        "Valor":[

            result.y[
                SPECIES["atp"]
            ][-1],

            result.y[
                SPECIES["acetylcoa"]
            ][-1],



            result.y[
                SPECIES["nad"]
            ][-1],

            result.y[
                SPECIES["nadh"]
            ][-1],
            
            ferrocyanide_equivalent = (
                2.0 * nadh_final
            )
            result.y[
                SPECIES["fad"]
            ][-1],

            result.y[
                SPECIES["fadh2"]
            ][-1],

            result.y[
                SPECIES[
                    "oxaloacetate"
                ]
            ][-1],

            result.y[
                SPECIES["malate"]
            ][-1],

            result.y[
                SPECIES["acetoacetate"]
            ][-1],

            result.y[
                SPECIES["bhb"]
            ][-1],
            
            result.y[
                SPECIES[
                    "ferricyanide_signal"
                ]
            ][-1],
            
            vqs