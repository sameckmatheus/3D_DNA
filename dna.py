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