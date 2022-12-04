import PySimpleGUI as sg


def main():
    sg.theme('DarkAmber')

    layout = [
        [sg.Text('Temp')],
        [sg.Button('Exit')]
    ]

    window = sg.Window('Stress and Strain Calculator', layout, )
    plt = 0

    calcLoop(window, plt, )


def calcLoop(window, plt, ):
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or 'Exit':
            break


    window.close()


if __name__ == '__main__':
    main()
