# window info
WINDOW_SIZE = (800,600)
FIELDS = (20,15)

# movement
START_POS = (5,int(FIELDS[1] / 2))
DIRECTIONS = {'left': [-1,0], 'right': [1,0], 'up': [0,-1], 'down': [0,1]}
REFRESH_SPEED = 250

# field limits 
LEFT_LIMIT = 0
TOP_LIMIT = 0
RIGHT_LIMIT = FIELDS[0]
BOTTOM_LIMIT = FIELDS[1]

# colors 
SNAKE_BODY_COLOR = '#8EF249'
SNAKE_HEAD_COLOR = '#71CC1D'
APPLE_COLOR = '#F9473E'