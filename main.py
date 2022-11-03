#dimensions in mm
#cuboid - l,b,h
#cylinder - radius, height 
# enter 'c' to stop the program.

from stl import mesh
from cylinder import build_cylindricalmesh
from box import build_cuboid
from utils.save import meshlist2stl

def build_stl(dim):
    shape = 0
    if len(dim)==2:
        shape = 'cylinder'
        finishing = 20
        req_mesh = build_cylindricalmesh(dim[0], dim[1], finishing)
    else:
        shape = 'cuboid'
        finishing = 32
        req_mesh = build_cuboid(dim[0], dim[1], dim[2], finishing)

    meshes = [mesh.Mesh(req_mesh)]
    meshlist2stl(meshes, dim, shape)
    print('generated and saved')
    return 1

if __name__ == "__main__":
    dim = [0]
    print('Enter the dimension array')
    while(len(dim)>0):
        dim = input().split()
        if dim[0] == 'c':
            break
        else:
            for i in range(len(dim)):
                dim[i] = float(dim[i])
        
            build_stl(dim)