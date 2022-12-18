import geometry as gmt

class Chair:
    def __init__ (self, length, width, height):
        self.length=length
        self.width=width
        self.height=height
        
        self.vertices_3D=[
            [0,0,0],
            [length,0,0],
            [length,width,0],
            [0,width,0],
            [0,0,height],
            [length,0,height],
            [length,width,height],
            [0,width,height]]
        
        self.edges_3D=[
            [0,1],
            [1,2],
            [2,3],
            [3,0],
            [4,5],
            [5,6],
            [6,7],
            [7,4],
            [0,4],
            [1,5],
            [2,6],
            [3,7]]
        
        self.faces_3D=[
            [0,1,2,3],
            [4,5,6,7],
            [0,1,5,4],
            [1,2,6,5],
            [2,3,7,6],
            [3,0,4,7]]
        
        self.vertices_2D=[
            [0,0,0],
            [length,0,0],
            [length,width,0],
            [0,width,0]]
        
        self.edges_2D=[
            [0,1],
            [1,2],
            [2,3],
            [3,0]]
        
        self.faces_2D=[
            [0,1,2,3]]

class Table:
    top_h=.05
    leg_w=.05
    def __init__ (self, length, width, height):
        leg=[]
        leg.append(gmt.Box(leg_w, leg_w, height-top_h))
        leg.append(gmt.obj_move(leg[0], [length-leg_w, 0, 0]))
        leg.append(gmt.obj_move(leg[0], [length-leg_w, width-leg_w, 0]))
        leg.append(gmt.obj_move(leg[0], [length-leg_w, 0, 0]))
        top=gmt.Box(length, width, top_h)
        top=gmt.obj_move(top,[0, 0, height-top_h])
#print(top.vertices)