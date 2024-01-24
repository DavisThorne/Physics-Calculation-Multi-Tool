import PySimpleGUI as sg


def openWindow(layout, ):
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
        [sg.Text('Temp')],
        [sg.Button('Calculate'), sg.Button('Exit')]
    ]

    window = sg.Window('Stress and Strain Calculator', layout, )
    plt = 0

    calcLoop(window, plt, )


def calcLoop(window, plt, ):
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or 'Exit':
            break
        if event == 'Calculate':
            layout = [
                [sg.Text('Calculations Complete')],
                [sg.Button('Exit')]

            ]
            openWindow(layout, )



    window.close()


if __name__ == '__main__':
    main()
