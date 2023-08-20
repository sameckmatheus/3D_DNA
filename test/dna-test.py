import numpy as np
from Bio.PDB import PDBParser
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Defininfo as conts para visualização (janela/camera)
WINDOW_TITLE = "DNA Humano"
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FOV = 45
NEAR = 1
FAR = 50
CAMERA_POS = (0, 0, -15)
CAMERA_TARGET = (0, 0, 0)
CAMERA_UP = (0, 1, 0)

