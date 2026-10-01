import streamlit as st

from model.parameters import (
    HEPATIC_PARAMETERS,
    CARDIAC_PARAMETERS
)

from model.simulation import (
    run_simulation
)

from ui_utils import (
    build_initial_conditions
)

from analysis.summary import (
    simulation_summary
)

from analysis.flux import (
    beta_flux
)

from graphics.plotting import (
    plot_carbon_flux,
    plot_nad,
    plot_fad,
    plot_atp,
    plot_acetylcoa,
    plot_oaa_malate,
    plot_ketones,
    plot_beta_flux,
    plot_ferricyanide
)


# =====================================================
# PORTADA
# =====================================================

st.image(
    "assets/Mitocondria_experimental.png",
    use_container_width=True
)

st.title(
    "Gemelo Digital de la β‑Oxidación Mitocondrial"
)

st.caption(
    "Comprenda el catabolismo lipídico como un sistema integrado mediante la articulación de experimentación real y simulación digital."
)

st.divider()

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.header(
    "Configuración experimental"
)

tissue = st.sidebar.selectbox(
    "Tejido",
    [
        "Hígado",
        "Corazón"
    ]
)

rotenone = st.sidebar.checkbox(
    "Rotenona"
)

ferricyanide = st.sidebar.checkbox(
    "Añadir ferricianuro experimental",
    value=True
)

fatty_acids = {
    "Palmítico (C16:0)": 16,
    "Mirístico (C14:0)": 14,
    "Láurico (C12:0)": 12,
    "Cáprico (C10:0)": 10,
    "Caprílico (C8:0)": 8,
    "Caproico (C6:0)": 6,
    "Butírico (C4:0)": 4
}

selected_fa = st.sidebar.selectbox(
    "Ácido graso",
    list(fatty_acids.keys())
)

chain = fatty_acids[selected_fa]

substrate = st.sidebar.number_input(
    "Moleculas de sustrato",
    value=50.0,
    min_value=0.0
)

oaa = st.sidebar.number_input(
    "Oxalacetato",
    value=0.0,
    min_value=0.0
)

acac = st.sidebar.number_input(
    "Acetoacetato",
    value=0.0,
    min_value=0.0
)

bhb = st.sidebar.number_input(
    "β-Hidroxibutirato",
    value=0.0,
    min_value=0.0
)

tmax = st.sidebar.slider(
    "Tiempo de simulación",
    50,
    5000,
    500
)

plots = st.sidebar.multiselect(
    "Mostrar gráficos",
    [
        "Carbono",
        "NAD",
        "FAD",
        "ATP",
        "AcetylCoA",
        "OAA/Malato",
        "Cetonas",
        "Flujo β",
        "Ferricianuro"
    ],
    default=[
        "Carbono",
	"ATP"
    ]
)

# =====================================================
# PARAMETROS
# =====================================================

if tissue == "Hígado":

    params = HEPATIC_PARAMETERS.copy()

else:

    params = CARDIAC_PARAMETERS.copy()

params["rotenone"] = rotenone
params["ferricyanide"] = ferricyanide

# =====================================================
# SIMULAR
# =====================================================

if st.button(
    "Simular"
):

    y0 = build_initial_conditions(

        chain_length=chain,

        substrate_conc=substrate,

        oaa=oaa,

        acac=acac,

        bhb=bhb

    )

    result = run_simulation(

        y0,

        params,

        tmax=tmax

    )

    # =====================================
    # Ferricianuro (para obtener vqs)
    # =====================================

    ferri_output = plot_ferricyanide(
        result
    )

    if ferri_output is not None:

        fig_ferri = ferri_output[0]

        vqs = ferri_output[1]

    else:

        fig_ferri = None

        vqs = None

    # =====================================
    # TABLA
    # =====================================

    st.header(
        "Resumen"
    )

    table = simulation_summary(
        result,
        y0,
        vqs
    )

    st.dataframe(
        table,
        use_container_width=True
    )

    # =====================================
    # FLUJO BETA
    # =====================================

    flux = beta_flux(
        result
    )

    # =====================================
    # GRAFICOS
    # =====================================

    st.header(
        "Gráficos"
    )

    if "Carbono" in plots:

        fig,_ = plot_carbon_flux(
            result
        )

        st.pyplot(fig)

    if "NAD" in plots:

        fig,_ = plot_nad(
            result
        )

        st.pyplot(fig)

    if "FAD" in plots:

        fig,_ = plot_fad(
            result
        )

        st.pyplot(fig)

    if "ATP" in plots:

        fig,_ = plot_atp(
            result
        )

        st.pyplot(fig)

    if "AcetylCoA" in plots:

        fig,_ = plot_acetylcoa(
            result
        )

        st.pyplot(fig)

    if "OAA/Malato" in plots:

        fig,_ = plot_oaa_malate(
            result
        )

        st.pyplot(fig)

    if "Cetonas" in plots:

        fig,_ = plot_ketones(
            result
        )

        st.pyplot(fig)

    if "Flujo β" in plots:

        fig,_ = plot_beta_flux(
            result,
            flux
        )

        st.pyplot(fig)

    if "Ferricianuro" in plots:

        if fig_ferri is not None:

            st.pyplot(
                fig_ferri
            )