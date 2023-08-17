import numpy as np
from Bio.PDB import PDBParser
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def load_dna_strcture(pdb_file):
  paser = PDBParser(quit=true)
  structure = paser.get_structure('DNA', pdb_file)
  model = structure[0]
  return model

# Inicializando a janela OpenGL
def draw_dna_model(model):
  glutInit()
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutCreateWindow("Representação do DNA humano")

  # Inicializando a renderização da janela
  def render():
    glClear(GL_COLOR_BUFFER_CLEAR)
    glRotatef(1, 3, 1, 1)

    glLineWidth(2.0)
    glBegin(GL_LINES)
    for chain in model.get_chains():
      for residue in chain:
        for atom in residue:
          if atom.get_name() == "p":
            x, y, z = atom.get_coord()
            glVertex3f(x, y, z)
    glEnd()
    glFlush()