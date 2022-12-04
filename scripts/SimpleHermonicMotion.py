from typing import List

import PySimpleGUI as sg
from PySimpleGUI import Text


def openWindow(layout, ):
    sg.theme('DarkAmber')
    window = sg.Window("Second Window", layout, modal=True)
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
            break

    window.close()


def main():
    sg.theme("DarkAmber")
    layout = [
        [sg.Text("This is some text for a test")],
        [sg.Button("Exit"), sg.Button("New Window", key="-NewWindow-")]
    ]

    window = sg.Window("Test", layout)
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
            break
        if event == "-NewWindow-":
            layoutTemp = [
                [sg.Text("Test V2")]
            ]
            openWindow(layoutTemp)


if __name__ == "__main__":
    main()
