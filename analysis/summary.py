import pandas as pd

from model.species import SPECIES


def simulation_summary(
        result,
        y0,
        vqs=None):

    return pd.DataFrame({

        "Variable":[

            "ATP generado",
<<<<<<< HEAD
            "AcetylCoA final",

=======

            "Acetil-CoA final",
>>>>>>> 7e5bc0691118137cbc68df21476da6e813642abb

            "NAD+",

            "NADH",

            "Ferrocianuro equivalente",

            "FAD",

            "FADH2",

            "Oxalacetato",

            "Malato",

            "Acetoacetato",
<<<<<<< HEAD
            "β-Hidroxibutirato",
            "Ferricianuro final",
            "Velocidad de reducción de ferricianuro"
=======
>>>>>>> 7e5bc0691118137cbc68df21476da6e813642abb

            "β-Hidroxibutirato"
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
<<<<<<< HEAD
                2.0 * nadh_final
            )
=======
                2.0
                *
                result.y[
                    SPECIES["nadh"]
                ][-1]
)
>>>>>>> 7e5bc0691118137cbc68df21476da6e813642abb
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
<<<<<<< HEAD
            
            result.y[
                SPECIES[
                    "ferricyanide_signal"
                ]
            ][-1],
            
            vqs
=======

            vqs
            

        ]

    })
>>>>>>> 7e5bc0691118137cbc68df21476da6e813642abb
