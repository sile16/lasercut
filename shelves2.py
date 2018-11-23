#p3 size 791mm x 384mm
#sculpteo 940mm x 590

import svgwrite

#Adobe Illustrator
#72 ppi, 
mm = 72 / 25.4

#manufacturer = "sculpteo"
manufacturer = "ponoko"
node_radius_ratio = 11
node_length = 7

if manufacturer == "sculpteo":
    join_width = 6.1
    color_width = 41
    color_height = 96.475
    panel_width = 940
    panel_height = 590
    shelf_width = 939
    depth = 160
    riser_height = 290

elif manufacturer == "ponoko":
    join_width = 5.9
    color_width = 41
    color_height = 96.475
    panel_width = 791
    panel_height = 384
    shelf_width = 790
    depth = 160
    riser_height = 290
   
stroke_width="0.01"
dwg = svgwrite.Drawing('shelf_po_v4_3.svg',size=('2267.72','1116.85'),viewBox="0 0 2267.72 1116.85",profile="tiny")
current_group = dwg.add(dwg.g(id="Design_Template"))
current_group.add(dwg.rect((0,0),(2267.72,1116.85),fill=svgwrite.rgb(246,146,30)))
current_group.add(dwg.rect((5*mm,5*mm),(2239.37,1088.5),fill=svgwrite.rgb(255,255,255)))

#current_group = dwg.add(dwg.g(id="design", stroke=svgwrite.rgb(0, 0, 255),stroke_width=stroke_width,fill='none')
current_group = dwg.add(dwg.g(id="ADD_your_design_here", stroke=svgwrite.rgb(0, 0, 255),stroke_width=stroke_width,fill='none'))

def addArc(p0, p1, ratio):
    """ Adds an arc that bulges to the right as it moves from p0 to p1 """
    args = {'x0':p0[0]*mm+5*mm, 
        'y0':p0[1]*mm+5*mm, 
        'xradius':mm*1/ratio, 
        'yradius':mm*1, 
        'ellipseRotation':0, #has no effect for circles
        'x1':(p1[0]-p0[0])*mm, 
        'y1':(p1[1]-p0[1])*mm}
    current_group.add(dwg.path(d="M %(x0)f,%(y0)f a %(xradius)f,%(yradius)f %(ellipseRotation)f 0,0 %(x1)f,%(y1)f"%args,
             fill="none", 
             stroke=svgwrite.rgb(0, 0, 255), stroke_width=stroke_width
            ))

def line(start,end):
    rx1 = round(start[0]*mm+5*mm,3)
    ry1 = round(start[1]*mm+5*mm,3)
    rx2 = round(end[0]*mm+5*mm,3)
    ry2 = round(end[1]*mm+5*mm,3)
    current_group.add(dwg.line((rx1, ry1), (rx2, ry2)))

def slot(x,y,top=True):
    if top:
        line((x-join_width/2, y), (x-join_width/2, y+depth/2))
    #break in 3 section
    join_length = depth/2

    y1 = round(join_length / 3, 2) + y
    y2 = round(2 * join_length / 3, 2) + y
    y3 = join_length + y 

    #down the right 
    current_x = x+join_width/2
    
    line((current_x, y), (current_x, y1 - node_length/2))
    addArc((current_x, y1 - node_length/2),(current_x, y1 + node_length/2),node_radius_ratio)
    line( (current_x, y1 + node_length/2),(current_x, y2 - node_length/2))
    addArc((current_x, y2 - node_length/2),(current_x, y2 + node_length/2),node_radius_ratio)
    line( (current_x, y2 + node_length/2), (current_x, y3))

    #bottom
    line( (x+join_width/2, y3),(x-join_width/2, y3))

    #up the left
    current_x = x-join_width/2
    line((current_x, y3),(current_x, y2 + node_length/2))
    addArc((current_x, y2 + node_length/2),(current_x, y2 - node_length/2),node_radius_ratio)
    line((current_x, y2 - node_length/2), (current_x, y1 + node_length/2))
    addArc((current_x, y1 + node_length/2),(current_x, y1 - node_length/2),node_radius_ratio)
    line( (current_x, y1 - node_length/2),(current_x, y))


def shelf(x,y,top=True,bottom=True,left=True,right=True):
    if top:
        line((x, y), (x+shelf_width, y))
    if left:
        line((x, y), (x, y+depth))
    curr_pos=0
    for incr in range(0,int(shelf_width/(color_width+join_width))):
        curr_pos+=color_width+join_width
        slot(curr_pos,y,top=False)
    if right:
        line((x+shelf_width, y), (x+shelf_width, y+depth))
    if bottom:
        line((x+shelf_width, y+depth), (x, y+depth))
    
    
def riser(x,y,top=True,bottom=True,left=True,right=True):
    if top:
        line((x, y), (x+riser_height, y))
    if left:
        line((x, y), (x, y+depth))
    if bottom:
        line((x, y+depth), (x+riser_height, y+depth))
    if right:
        line((x+riser_height, y), (x+riser_height, y+depth))
    slot(x+128.63,y,top=False)

if manufacturer  == "sculpteo":

    shelf(0,0,top=False,left=False,right=False)
    shelf(0,depth,top=False,left=False,right=False)
    riser(0*riser_height,depth*2,top=False,bottom=False,left=False)
    riser(1*riser_height,depth*2,top=False,bottom=False,left=False)
    riser(2*riser_height,depth*2,top=False,bottom=False,left=False)

elif manufacturer == "ponoko":
    shelf(0,0,top=False,left=False,right=False)
    riser(0*riser_height,depth*1,top=False,bottom=False,left=False)
    riser(1*riser_height,depth*1,top=False,bottom=False,left=False)
    riser(2*riser_height,depth*1,top=False,bottom=False,left=False,right=False)
    line((0,depth*2),(shelf_width,2*depth))
    line((0,0),(shelf_width,0))
    line((shelf_width,0),(shelf_width,2*depth))
    line((0,0),(0,2*depth))

    

#dwg.add(dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(0, 0, 255),stroke_width="0.01"))
#dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))
dwg.save()


