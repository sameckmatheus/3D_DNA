import numpy as np
from Bio.PDB import PDBParser
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Definindo as conts para visualização (janela/camera)
WINDOW_TITLE = "DNA Humano"
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FOV = 45
NEAR = 1
FAR = 50
CAMERA_POS = (0, 0, -15)
CAMERA_TARGET = (0, 0, 0)
CAMERA_UP = (0, 1, 0)

# Definindo uma função para carregar a estrutura do DNA a partir de um arquivo PDB
def load_dna_structure(pdb_file):
  parser = PDBParser(QUIET=True)
  structure = parser.get_structure('DNA', pdb_file)
  model = structure[0]
  return model

# Definindo uma função para desenhar a estrutura do DNA usando linhas
def draw_dna_model(model):
  glLineWidth(2.0)
  glBegin(GL_LINE)
  for chain in model.get_chains():
    for residue in chain:
      for atom in residue:
        if atom.get_name() == "p":
          x, y, z = atom.get_coord()
          glVertex3f(x, y, z)
  glEnd()