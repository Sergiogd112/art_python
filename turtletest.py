#!/usr/bin/python
'''    Spectral Harmonographs   Copyright 2014 Alan Richmond (Tuxar.uk)

    Trace of 4 decaying sine waves, 2 per axis (x & y)(i.e. 2-pendula), with rainbow colour.
    I did this in Java some decades ago (Encyclogram; I no longer have the source), this
    version is in Python, with PyGame.
    It randomly generates a sequence of harmonographs. It's fast, and can be set to go
    much faster (or slower) if you want.
    Tip: set the display window to fullscreen. On KDE Ubuntu right-click on the title bar,
    select More Actions -> Fullscreen
'''
import random as r
import sys
import pygame
from math import pi, sin, cos, exp
from pygame.locals import *
print("Quit: q key, Screenshot: spacebar")

#                        EDIT THESE:
'''
width, height = 1280, 720       # YouTube HD
width, height = 1920, 1080      # my left monitor
width, height = 1280, 1024      # my right monitor
width, height = 1680, 1050      # Lucy's monitor
width, height = 1200, 800
'''
width, height = 2560, 1440      # YT channel art
dd = 0.99995                  # decay factor
dt = 0.02                     # time increment
speed = 200                   # yes, speed
hui = 57 * 2                    # Hue increment
hue, sat, val, aaa = 0, 100, 100, 0
sd = 0.005                    # frequency spread (from integer)
mx = 4                        # max range for amplitudes & frequencies
print("Hit SPACE to save")


def check_event():
    global save
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            save = True
            print("Saving when finished...")


def scale(length):
    while True:
        a1, a2 = r.randint(-mx, mx), r.randint(-mx, mx)
        max = abs(a1) + abs(a2)
        if max > 0:
            break
    return a1, a2, length / (2 * max)


steps = 0
pygame.init()
pygame.event.set_allowed([QUIT, KEYDOWN])
screen = pygame.display.set_mode((width, height), DOUBLEBUF)
screen.set_alpha(None)
fg = pygame.Color(0, 0, 0, 0)
# fg=(0,0,0)
# fg = (255, 255, 255)
save = True
while True:
    #   Amplitudes & scales
    ax1, ax2, xscale = scale(width)
    ay1, ay2, yscale = scale(height)
    fx1, fx2 = r.randint(1, mx) + r.gauss(0,
                                          sd), r.randint(1, mx) + r.gauss(0, sd)
    fy1, fy2 = r.randint(1, mx) + r.gauss(0,
                                          sd), r.randint(1, mx) + r.gauss(0, sd)
    px1, px2 = r.uniform(0, 2 * pi), r.uniform(0, 2 * pi)
    py1, py2 = r.uniform(0, 2 * pi), r.uniform(0, 2 * pi)
    print(ax1, ax2, ay1, ay2)
    print(fx1, fx2, fy1, fy2)
    print(px1, px2, py1, py2)

    dec = 1.0
    t = 0.0                       # angle for sin
    first = True
    while dec > 0.015:
                                # calculate next x,y point along line
        x = xscale * dec * (ax1 * sin(t * fx1 + px1) +
                            ax2 * sin(t * fx2 + px2)) + width / 2
        y = yscale * dec * (ay1 * sin(t * fy1 + py1) +
                            ay2 * sin(t * fy2 + py2)) + height / 2
        dec *= dd                 # decay
        if not first:           # ignore any complaint about prev_x,y being undefined
            fg.hsva = (hue, sat, val, aaa)
            hue = (hue + dt * hui) % 360      # cycle hue
            pygame.draw.aaline(screen, fg, (x, y), (prev_x, prev_y), 1)
        else:
            first = False

        prev_x = x              # save x,y for next line segment start
        prev_y = y
        if steps % speed == 0:
            pygame.display.update()
        steps += 1
        t += dt                   # increment angle for sin
        check_event()

    if save:                    # parameters are encoded into filename
        pars = 'shg-{0}_{1}-{2}_{3}-{4}_{5}'.format(
            ax1, ax2, fx1, fx2, px1, px2)
        pygame.image.save(screen, pars + '.jpg')
        print("Saved as " + pars + '.jpg')
        save = True

    screen.fill((0, 0, 0))
#    screen.fill((255,255,255))
