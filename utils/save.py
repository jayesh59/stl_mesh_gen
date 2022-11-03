#!/usr/bin/python

from stl import mesh, stl
from numpy import concatenate

def meshlist2stl(mesh_list,dim,shape):
    
    justonemesh = mesh.Mesh( concatenate( [me.data for me in mesh_list]))
    justonemesh.save(f'./required_meshes/{shape}_{dim}.stl', mode= stl.Mode.ASCII)
