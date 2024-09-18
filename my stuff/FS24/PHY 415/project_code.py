# I don't know what im doing
import numpy as np

def generate_grid(xrange, yrange, points):
    '''
    Creates a points*points grid across xrange and yrange. spaceing will shrink/stretch if not square
    '''

    xarray = np.linspace(xrange[0],xrange[1], points)
    yarray = np.linspace(yrange[0],yrange[1], points)
    return np.meshgrid(xarray,yarray)


def generate_phase_space(diff_eq_func, params, xrange, yrange, grid_size):
    X, V = generate_grid(xrange, yrange, grid_size)
    dx, dv = diff_eq_func(X, V, params)

    return X, V, dx, dv    
