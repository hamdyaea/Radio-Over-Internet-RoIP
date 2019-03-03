#!/usr/bin/python3

# Developer : Hamdy Abou El Anein
# writed in python 3
# Read the readme to install the python 3 modules and dependencies


import sys
from easygui import *
import vlc

def energy1058():
    player = vlc.MediaPlayer("http://tachyon.shoutca.st:8590/stream")
    player.play()
    image = "./pictures/energy1058.jpg"
    msg = "You are listening the Energy 1058 radio"
    choices = ["Exit","Start menu"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Start menu":
        player.stop()
        start()
    else:
        sys.exit(0)

def fdlounge():
    player = vlc.MediaPlayer("http://listen.radionomy.com/fd-lounge-radio")
    player.play()
    image = "./pictures/fdlounge.jpg"
    msg = "You are listening FD lounge radio"
    choices = ["Exit","Start menu"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Start menu":
        player.stop()
        start()
    else:
        sys.exit(0)

def radiomosaique():
    player = vlc.MediaPlayer("http://radio.mosaiquefm.net:8000/mosalive")
    player.play()
    image = "./pictures/mosaique.jpg"
    msg = "You are listening Mosaique FM live"
    choices = ["Exit","Start menu"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Start menu":
        player.stop()
        start()
    else:
        sys.exit(0)

def nrjlounge():
    player = vlc.MediaPlayer("http://cdn.nrjaudio.fm/adwz1/fr/30049/mp3_128.mp3?origine=fluxradios")
    player.play()
    image = "./pictures/nrjlounge.jpg"
    msg = "You are listening to NRJ lounge radio"
    choices = ["Exit","Start menu"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Start menu":
        player.stop()
        start()
    else:
        sys.exit(0)


def abcpiano():
    player = vlc.MediaPlayer("http://listen.radionomy.com/abc-piano")
    player.play()
    image = "./pictures/abcpiano.jpg"
    msg = "You are listening ABC Piano live"
    choices = ["Exit","Start menu"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Start menu":
        player.stop()
        start()
    else:
        sys.exit(0)

def start():
    image = "./pictures/live.jpg"
    msg = "Click on the button to open a live web radio"
    choices = ["Mosaique FM","ABC Piano","NRJ Lounge","FD lounge radio","Energy 1058"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Mosaique FM":
        radiomosaique()
    elif reply == "ABC Piano":
        abcpiano()
    elif reply == "NRJ Lounge":
        nrjlounge()
    elif reply == "FD lounge radio":
        fdlounge()
    elif reply == "Energy 1058":
        energy1058()
    else:
        sys.exit(0)

start()

