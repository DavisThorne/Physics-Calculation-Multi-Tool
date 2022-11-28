import PySimpleGUI as sg

def openWindow(layout, ):
    sg.theme('DarkAmber')
    window = sg.Window("Second Window", layout, modal=True)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()


def main():
    pass


