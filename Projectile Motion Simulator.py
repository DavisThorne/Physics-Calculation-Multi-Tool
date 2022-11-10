# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 22:11:06 2022

This is an ongoing project, plans are to include a GUI and maybe other 
calculations to use this as a superscript for physics calculations

@author: dskmgmt
"""
import numpy as np
import matplotlib.pyplot as plt


def inputGathering():
    try:
        M = float(input("Enter the projectiles mass in kg\n>>> "))
        g = float(input("Enter the affects of gravity (Earth = 9.81)\n>>> "))
        V = float(input("Enter the projectiles initial velocity in m/s\n>>> "))
        ang = float(input("Enter the initial angle of the projectile\n>>> "))
        Cd = float(input("Enter the drag coefficient\n>>> "))
        dt = float(input("Enter the time increment for each measurement in seconds\n>>> "))

    except KeyboardInterrupt:
        print("interrupted")

    except:
        print("Please enter valid values")
        inputGathering()

    return calculations(M, g, V, ang, Cd, dt)


def calculations(M, g, V, ang, Cd, dt):
    t = [0]  # list to keep track of time
    vx = [V * np.cos(ang / 180 * np.pi)]  # list for velocity x and y components
    vy = [V * np.sin(ang / 180 * np.pi)]
    x = [0]  # list for x and y position
    y = [0]

    # Drag force
    drag = Cd * V ** 2  # drag force

    # Acceleration components
    ax = [-(drag * np.cos(ang / 180 * np.pi)) / M]
    ay = [-g - (drag * np.sin(ang / 180 * np.pi) / M)]

    # Use Euler method to update variables
    counter = 0
    while y[counter] >= 0:  # Check that the last value of y is >= 0
        t.append(t[counter] + dt)  # increment by dt and add to the list of time

        # Update velocity
        vx.append(vx[counter] + dt * ax[counter])  # Update the velocity
        vy.append(vy[counter] + dt * ay[counter])

        # Update position
        x.append(x[counter] + dt * vx[counter])
        y.append(y[counter] + dt * vy[counter])

        # With the new velocity calculate the drag force and update acceleration
        vel = np.sqrt(vx[counter + 1] ** 2 + vy[counter + 1] ** 2)  # magnitude of velocity
        drag = Cd * vel ** 2  # drag force
        ax.append(-(drag * np.cos(ang / 180 * np.pi)) / M)
        ay.append(-g - (drag * np.sin(ang / 180 * np.pi) / M))

        # Increment the counter by 1
        counter = counter + 1

    plt.plot(x, y, 'r-')
    plt.ylabel("Vertical Displacement (m)")
    plt.xlabel("Horizontal Displacement (m)")
    plt.show()

    # The last value of x should give the range of the projectile approximately.

    print("Total x-displacement of projectile is {:3.1f}m".format(x[counter]))
    print("Total y-displacement of projectile is {:3.1f}m".format(y[counter]))


inputGathering()
