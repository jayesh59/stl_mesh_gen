#!/usr/bin/python

from stl import mesh
from numpy import concatenate
from base.squared import _build
from utils.render import meshrender



def build_cuboid(l, b, h, finishing):
    
    vertex = [0, 0, 0]
    p2 = [l, 0, 0]
    p3 = [0, b, 0]
    p4 = [0, 0, h]
    p5 = [l, 0, h]
    p6 = [0, b, h]
    p7 = [l, b, 0]
    p8 = [l, b, h]

    # base   - XY::LB
    data_basemesh = _build(vertex, p2, p3, p7, finishing)
    # ceil   - XY::LB
    data_topmesh = data_basemesh.copy()
    data_topmesh['vectors'] += [ 0, 0, h]
    #=============================================================
    # frontal - XZ::LH
    data_frontsidemesh = _build(vertex, p2, p4 ,p5, finishing)
    # rear   - XZ::LH
    data_rearsidemesh = data_frontsidemesh.copy()
    data_rearsidemesh['vectors'] += [ 0, b, 0]
    #=============================================================
    # leftside - YZ::BH
    data_leftsidemesh = _build(vertex, p3, p4 ,p6, finishing)
    # rightside   - YZ::BH
    data_rightsidemesh = data_leftsidemesh.copy()
    data_rightsidemesh['vectors'] += [ l, 0, 0]
    #=============================================================
    meshdata = [ data_basemesh, data_topmesh,
                data_frontsidemesh, data_rearsidemesh,
                data_leftsidemesh, data_rightsidemesh]#
                
    data = concatenate( meshdata)
    return data
    
if __name__ == "__main__":
    
    onemesh = build_cuboid(1, 2, 3 , 32)
    #onemesh = buildsquare([ 0, 0, 0], [ 6, 6, 0], 64)
    meshes = [mesh.Mesh(onemesh)]
    meshrender( meshes, 0)
