__author__ = 'Scratso'

#####################
# VARIABLE DECLARES #
#####################

gameName = "PythianRealms"
gameYear = "2016"

tilesizex = 32
tilesizey = 32
mapwidth = 100
mapheight = 100
mapz = 15

realms = 2

playerz = 4

oldtiles = []

zaxis = 0
place = False
pickup = False
changedz = []

change = False
debug = False

invshow = False
shopshow = False

activeoverlay = True

selectednpc = None

coins = 1000  # 1000 coins to start, and per boost

global screen_image
screen_image = None

global playerHP
playerHP = 100

# visible map sizes. There is always hidden map.
vmapwidth = round(75 / (tilesizex / 16))
vmapheight = round(40 / (tilesizey / 16))
