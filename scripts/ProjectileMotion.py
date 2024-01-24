import PySimpleGUI as sg
import matplotlib.pyplot as plt
import numpy as np


def openWindow(layout, ):
    sg.theme('DarkAmber')
    window = sg.Window("Second Window", layout, modal=True)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()


def main():
    sg.theme('DarkAmber')

    layout = [
        [sg.Text('Enter the mass of the object'), sg.InputText(key="-mass-")],
        [sg.Text('Enter the Velocity of the object'), sg.InputText(key="-velocity-")],
        [sg.Text('Enter the Initial angle of launch'), sg.InputText(key="-angle-")],
        [sg.Text('Enter the drag coefficient (0 for no drag)'), sg.InputText(key="-drag-")],
        [sg.Text('Enter the gravitational constant of your choosing'), sg.InputText(key="-gravity-")],
        [sg.Text('Enter the time interval of measurement'), sg.InputText(key="-dt-")],
        [sg.Button('Calculate'), sg.Button('Show Graph'), sg.Button('Close Graph'), sg.Button('Exit')]
    ]

    window = sg.Window('Projectile Motion Calculator', layout, )
    plt = 0

    calcLoop(window, plt)


def calcLoop(window, plt, ):
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks Close
            break
        elif event == 'Calculate':
            layout = [
                [sg.Text('Calculations Complete')],
                [sg.Button('Exit')]
            ]
            openWindow(layout, )

            try:
                M = float(values["-mass-"])
                V = float(values["-velocity-"])
                ang = float(values["-angle-"])
                Cd = float(values["-drag-"])
                g = float(values["-gravity-"])
                dt = float(values["-dt-"])

            except KeyboardInterrupt:
                print("interrupted")

            except TypeError:
                print("Please enter valid values")
                main()

            return calculations(M, g, V, ang, Cd, dt, window)

        elif event == 'Show Graph':
            plt.show()
        elif event == 'Close Graph':
            plt.close()
    window.close()


def calculations(M, g, V, ang, Cd, dt, window):
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
    # The last value of x should give the range of the projectile approximately.



    xDisplacement = ("Total x-displacement of projectile is {:3.1f}m".format(x[counter]))
    yDisplacement = ("Total y-displacement of projectile is {:3.1f}m".format(y[counter]))

    return calcLoop(window, plt, )
