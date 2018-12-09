import cocos
import pyglet
from pyglet import image
        
        
#run right --------------------------------------------------  
img_r = image.load('res/animation/run/adventurer-run3-sword-Sheet.png')
img_grid_r = image.ImageGrid(img_r, 1, 6, item_width=50, item_height=37 )
anim_r = image.Animation.from_image_sequence(img_grid_r[0:], 0.1, loop=True)
# ----------------------------------------------------------
        
#attack1
img_a1 = pyglet.image.load('res/animation/attack1/attack1sheet.png')
img_grid_a1 = pyglet.image.ImageGrid(img_a1, 6, 1, item_width=50, item_height=37 )

anim_a1 = pyglet.image.Animation.from_image_sequence(img_grid_a1[::-1], 0.05, loop=False)
#------------------------------------------------------------------

#attack2
img_a2 = image.load('res/animation/attack2/attack2sheet.png')
img_grid_a2 = image.ImageGrid(img_a2, 6, 1, item_width=50, item_height=37)
anim_a2 = image.Animation.from_image_sequence(img_grid_a2[::-1], 0.1, loop=True)
#------------------------------------------------------------------

#attack3
img_a3 = image.load('res/animation/attack3/attack3sheet.png')
img_grid_a3 = image.ImageGrid(img_a3, 6, 1, item_width=50, item_height=37)
anim_a3 = image.Animation.from_image_sequence(img_grid_a3[::-1], 0.1, loop=True)
#-------------------------------------------------------------------

# idle
img_i = image.load('res/animation/idle/idlesheet.png')
img_grid_i = image.ImageGrid(img_i, 1, 4, item_width=50, item_height=37 )

anim_i = image.Animation.from_image_sequence(img_grid_i[0:], 0.3, loop=True)

#_-----------------------------------------------------------------

# jump
img_j = image.load('res/animation/jump/jumpsheet.png')
img_grid_j = image.ImageGrid(img_j, 1, 4, item_width=50, item_height=37)

anim_j = image.Animation.from_image_sequence(img_grid_j[0:], 0.2, loop=True)

#------------------------------------------------------------------

# block
img_b = image.load('res/animation/block/blocksheet.png')
img_grid_b = image.ImageGrid(img_b, 3, 1, item_width=50, item_height=37)

anim_b = image.Animation.from_image_sequence(img_grid_b[0:], 0.3, loop=True)

#------------------------------------------------------------------