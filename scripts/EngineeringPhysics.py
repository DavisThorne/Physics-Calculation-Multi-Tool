import PySimpleGUI as sg

class RuntimeValues:
    def __init__(self):
        self.torque = 0

def openWindow(layout):
    sg.theme('DarkAmber')
    window = sg.Window("Second Window", layout, modal=True)
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
            break

    window.close()

def main():
    sg.theme('DarkAmber')

    layout = [
        [sg.Text('Select a calculation')],
        [sg.Button('Torque Calculator', key='-Torque-')],
        [sg.Button('Exit')]
    ]

    window = sg.Window('Stress and Strain Calculator', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == '-Torque-':
            torqueCalc()


def torqueCalc():
    sg.theme('DarkAmber')
    layout = [
        [sg.Text('Enter the force applied'), sg.InputText(key='-force-')],
        [sg.Text('Enter the distance from the pivot point'), sg.InputText(key='-distance-')],
        [sg.Button('Calculate'), sg.Button('Exit')]
    ]
    window = sg.Window('Torque Calculator', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == 'Calculate':
            try:
                force = float(values['-force-'])
                distance = float(values['-distance-'])
            except TypeError:
                print('Invalid input')
            else:
                torque = force * distance
                RuntimeValues.torque = torque
                layout = [
                    [sg.Text('The torque is: ' + str(torque))],
                    [sg.Button('Exit')]
                ]
                openWindow(layout, )
                break