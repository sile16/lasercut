#p3 size 791mm x 384mm
#sculpteo 940mm x 590


import svgwrite



join_width = 5.9

color_width = 41
color_height = 96.475

panel_width = 940
panel_height = 590

shelf_width = 939
depth = 160

dwg = svgwrite.Drawing('risers.svg',size=(791,384))
stroke_width="0.01"

riser_height = 290


def slot(x,y):
    dwg.add(dwg.line((x-join_width/2, y), (x-join_width/2, y+depth/2), stroke=svgwrite.rgb(0, 0, 255),stroke_width=stroke_width))
    dwg.add(dwg.line((x+join_width/2, y), (x+join_width/2, y+depth/2), stroke=svgwrite.rgb(0, 0, 255),stroke_width=stroke_width))
    dwg.add(dwg.line((x-join_width/2, y+depth/2), (x+join_width/2, y+depth/2), stroke=svgwrite.rgb(0, 0, 255),stroke_width=stroke_width))

def shelf(x,y):
    #top
    dwg.add(dwg.line((x, y), (x+shelf_width, y), stroke=svgwrite.rgb(0, 0, 255),stroke_width=stroke_width))
    #left
    dwg.add(dwg.line((x, y), (x, y+depth), stroke=svgwrite.rgb(0, 0, 255),stroke_width=stroke_width))
    curr_pos=0
    for incr in range(0,int(shelf_width/color_width)):
        curr_pos+=color_width
        slot(curr_pos,y)
    
def riser(x,y):
    #top
    dwg.add(dwg.line((x, y), (x+riser_height, y), stroke=svgwrite.rgb(0, 0, 255),stroke_width=stroke_width))
    #left
    dwg.add(dwg.line((x, y), (x, y+depth), stroke=svgwrite.rgb(0, 0, 255),stroke_width=stroke_width))
    #bottom line
    dwg.add(dwg.line((x, y+depth), (x+riser_height, y+depth), stroke=svgwrite.rgb(0, 0, 255),stroke_width=stroke_width))
    #verticle right
    dwg.add(dwg.line((x+riser_height, y), (x+riser_height, y+depth), stroke=svgwrite.rgb(0, 0, 255),stroke_width=stroke_width))
    slot(x+128.63,y)


for num_riser in range(0,int(panel_width/riser_height)):
    riser(num_riser*riser_height,0)

for num_riser in range(0,int(panel_width/riser_height)):
    riser(num_riser*riser_height,depth)

for num_riser in range(0,int(panel_width/riser_height)):
    riser(num_riser*riser_height,depth*2)


#dwg.add(dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(0, 0, 255),stroke_width="0.01"))
#dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))
dwg.save()


