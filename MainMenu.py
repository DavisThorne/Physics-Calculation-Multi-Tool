# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 22:11:06 2022

This is an ongoing project, plans are to include a GUI and maybe other
calculations to use this as a superscript for physics calculations

@author: dskmgmt
"""
# Importing Libraries and other scripts
import PySimpleGUI as sg
import ProjectileMotion as projMot

sg.theme('DarkAmber')  # Defining the theme of the window

layout = [
    [sg.Text('Physics Calculation Multi-Tool')],
    [sg.Button('Projectile Motion')],
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

window.Close()
