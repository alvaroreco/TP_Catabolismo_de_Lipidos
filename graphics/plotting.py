import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import AutoMinorLocator

from model.species import SPECIES


def setup_axis(ax):

    ax.spines['top'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)

    ax.tick_params(
        axis='both',
        labelsize=16,
        pad=10
    )

    ax.xaxis.set_minor_locator(
        AutoMinorLocator(2)
    )

    ax.yaxis.set_minor_locator(
        AutoMinorLocator(2)
    )

    ax.tick_params(
        axis='both',
        which='major',
        direction='in',
        length=6,
        width=1.5
    )

    ax.tick_params(
        axis='both',
        which='minor',
        direction='in',
        length=3,
        width=1.5
    )

    ax.set_xlabel(
        "Tiempo",
        fontsize=20
    )

    ax.set_ylabel(
        "Concentración",
        fontsize=20
    )


# ======================================================
# GENERICO
# ======================================================

def plot_species(
        result,
        indices,
        labels,
        title):

    fig, ax = plt.subplots(
        figsize=(10,7)
    )

    setup_axis(ax)

    colors = plt.cm.viridis(
        np.linspace(
            0,
            1,
            len(indices)
        )
    )

    for i, idx in enumerate(indices):

        ax.plot(
            result.t,
            result.y[idx],
            linewidth=2,
            color=colors[i],
            label=labels[i]
        )

    ax.set_title(
        title,
        fontsize=20
    )

    ax.legend()

    plt.tight_layout()

    return fig, ax


# ======================================================
# FLUJO DE CARBONO
# ======================================================

def plot_carbon_flux(result):

    chains = [16,14,12,10,8,6,4]

    indices = [
        SPECIES[f"acylcoa_C{c}"]
        for c in chains
    ]

    labels = [
        f"C{c}"
        for c in chains
    ]

    return plot_species(
        result,
        indices,
        labels,
        "Flujo de carbono"
    )


# ======================================================
# NAD
# ======================================================

def plot_nad(result):

    return plot_species(

        result,

        [
            SPECIES["nad"],
            SPECIES["nadh"]
        ],

        [
            "NAD+",
            "NADH"
        ],

        "Estado Redox NAD"
    )


# ======================================================
# FAD
# ======================================================

def plot_fad(result):

    return plot_species(

        result,

        [
            SPECIES["fad"],
            SPECIES["fadh2"]
        ],

        [
            "FAD",
            "FADH2"
        ],

        "Estado Redox FAD"
    )


# ======================================================
# ATP
# ======================================================

def plot_atp(result):

    return plot_species(

        result,

        [
            SPECIES["atp"]
        ],

        [
            "ATP"
        ],

        "ATP"
    )


# ======================================================
# ACETIL COA
# ======================================================

def plot_acetylcoa(result):

    return plot_species(

        result,

        [
            SPECIES["acetylcoa"]
        ],

        [
            "Acetyl-CoA"
        ],

        "Acetyl-CoA"
    )


# ======================================================
# OAA MALATO
# ======================================================

def plot_oaa_malate(result):

    return plot_species(

        result,

        [
            SPECIES["oxaloacetate"],
            SPECIES["malate"]
        ],

        [
            "OAA",
            "Malato"
        ],

        "Malato DH"
    )
    
def plot_ketones(result):

    return plot_species(

        result,

        [
            SPECIES["acetoacetate"],
            SPECIES["bhb"]
        ],

        [
            "AcAc",
            "βHB"
        ],

        "Cuerpos cetónicos"
    )

def plot_beta_flux(
        result,
        flux):

    fig, ax = plt.subplots(
        figsize=(10,7)
    )

    setup_axis(ax)

    ax.plot(
        result.t,
        flux,
        linewidth=3
    )

    ax.set_title(
        "Flujo β-oxidativo"
    )

    return fig, ax


def plot_ferricyanide(result):

    ferri = result.y[
        SPECIES["ferricyanide_signal"]
    ]

    t = result.t

    # =====================================
    # VELOCIDAD
    # =====================================

    velocity = np.gradient(
        ferri,
        t
    )

    velocity = np.convolve(
        velocity,
        np.ones(11)/11,
        mode="same"
    )

    # =====================================
    # BUSCAR EL INTERVALO MÁS LARGO
    # DONDE LA VELOCIDAD SEA CASI CONSTANTE
    # =====================================

    tolerance = 0.20

    best_start = None
    best_end = None

    best_duration = 0

    min_window = 20

    for i in range(
        int(0.05*len(t)),
        len(t)-min_window
    ):

        vref = np.mean(
            velocity[
                i:i+min_window
            ]
        )

        if vref <= 0:

            continue

        j = i + min_window

        while j < len(t):

            rel_error = abs(
                velocity[j]
                -
                vref
            ) / vref

            if rel_error > tolerance:

                break

            j += 1

        duration = (
            t[j-1]
            -
            t[i]
        )

        if duration > best_duration:

            best_duration = duration

            best_start = i

            best_end = j

    # =====================================
    # AJUSTE LINEAL
    # =====================================

    x = t[
        best_start:best_end
    ]

    y = ferri[
        best_start:best_end
    ]

    coef = np.polyfit(
        x,
        y,
        1
    )

    vqs = coef[0]

    # =====================================
    # FIGURA 1
    # =====================================

    fig1, ax1 = plt.subplots(
        figsize=(7,7)
    )

    setup_axis(ax1)

    ax1.plot(
        t,
        ferri,
        color="navy",
        lw=3,
        label="Ferricianuro reducido"
    )

    ax1.axvspan(
        x[0],
        x[-1],
        color="orange",
        alpha=0.20
    )

    fit_x = np.array(
        [
            0,
            x[-1]
        ]
    )

    fit_y = np.polyval(
        coef,
        fit_x
    )

    ax1.plot(
        fit_x,
        fit_y,
        "--",
        color="red",
        lw=3,
        label=f"v0={vqs:.4f}"
    )

    ax1.set_title(
        "Ferricianuro reducido",fontsize=16
    )

    ax1.legend(fontsize=16)

    print(
        "\nVelocidad incial:",
        round(vqs,5)
    )

    return (fig1,vqs)