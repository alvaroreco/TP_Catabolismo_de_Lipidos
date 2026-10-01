from scipy.integrate import solve_ivp

from model.ode_system import derivatives


def run_simulation(
        y0,
        params,
        tmax=200):

    result = solve_ivp(

        derivatives,

        (0, tmax),

        y0,

        args=(params,),

        dense_output=True,

        method="LSODA"
    )

    return result