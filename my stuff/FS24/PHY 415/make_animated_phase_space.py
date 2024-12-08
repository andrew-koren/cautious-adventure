from matplotlib.animation import PillowWriter
import matplotlib.pyplot as plt
import numpy as np
from numpy import cos, pi
from scipy.integrate import solve_ivp

print('wowza')
fig = plt.figure()


# The Physics

def duffing(t, p0, params):
    x, v = p0
    alpha, beta, delta, gamma, omega = params
    dx = v
    dv = -delta * v - alpha * x - beta * x**3 + gamma * cos(omega * t)
    return dx, dv

alpha = -1
beta = 1
delta = 1
gamma = 5
omega = 1.2

parameters = [alpha, beta, delta, gamma, omega]

# make quiver plot

def generate_phase_space(x_lim, v_lim, grid_size, parameters, t):

    x = np.linspace(x_lim[0], x_lim[1], grid_size)
    v = np.linspace(v_lim[0], v_lim[1], grid_size)
    
    X, V = np.meshgrid(x, v)
    
    dX, dV = duffing(t, (X,V), parameters)
    
    return X, V, dX, dV

x_lim = (-3, 3)
v_lim = (-5, 5)
grid_size = 20

X, V, dX, dV = generate_phase_space(x_lim, v_lim, grid_size, parameters, 0)

field1 = plt.streamplot(X, V, dX, dV) #streamplot should have lower framerate, a bit overwhelming
#field1 = plt.quiver(X, V, dX, dV)


# creating the animation

metadata = dict(title='Movie', artist='AndrewKoren')
writer = PillowWriter(fps=15, metadata=metadata) # can make fps based on dt to make 1 second = 1 second

data = []

initial_condition = [1, 0]
end = 20
dt = 0.1

tspan = np.arange(0, end, dt)
solution = solve_ivp(duffing, (0, end), initial_condition, t_eval = tspan, args=[parameters])

with writer.saving(fig, 'duffing1.gif', 100):
    for i, tval in enumerate(tspan):
        
        X, V, dX, dV = generate_phase_space(x_lim, v_lim, grid_size, parameters, tval)
        plt.title(f't = {tval*omega/(2*np.pi):.2f} periods')
        plt.xlabel('position')
        plt.ylabel('velocity')

        plt.streamplot(X, V, dX, dV, color='blue') # can use streamplot instead, but more complicated
        #field1.set_UVC(dX, dV) # change where arrows point

        plt.plot(solution.y[0][:i+1], solution.y[1][:i+1], color='red') #draws 
        writer.grab_frame()
        plt.cla() # deletes old plots, use with plt.streamplot
