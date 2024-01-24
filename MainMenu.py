# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 22:11:06 2022

This is an ongoing project, plans are to include a GUI and maybe other
calculations to use this as a superscript for physics calculations

@author: dskmgmt
"""
# Importing Libraries and other scripts
import PySimpleGUI as sg
from scripts import ProjectileMotion as projMot
from scripts import EngineeringPhysics as engPhys

if __name__ == "__main__":
    sg.theme('DarkAmber')  # Defining the theme of the window

    layout = [
        [sg.Text('Physics Calculation Multi-Tool')],
        [sg.Button('Projectile Motion')], [sg.Button('Simple Harmonic Motion', key='-SHM-')],
        [sg.Button('Engineering Physics', key='-EngPhys-')],
        [sg.Button('Ok'), sg.Button('Exit')]
    ]

    window = sg.Window('Select What Script',
                       layout, )

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
            break

        if event == 'Projectile Motion':
            projMot.main()
        elif event == '-SHM-':
            print('It worked')
        elif event == '-EngPhys-':
            engPhys.main()


    window.Close()
