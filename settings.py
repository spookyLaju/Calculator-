
# app size 
APP_SIZE = (400,600)
MAIN_ROWS = 7 
MAIN_COLUMN = 4 

# Text 

FONT = 'Helvetica'
OUTPUT_FONT_SIZE = 70
NORMAL_FONT_SIZE =  30 

STYLING = {
    'gap': 0.5 , 
    'corner_radius': 0
}

NUM_POSITIONS ={
    '.': {'col': 2, 'row': 6, 'span':1},
       0: {'col': 0, 'row': 6, 'span':2},
       1: {'col': 0, 'row': 5, 'span':1},
       2: {'col': 1, 'row': 5, 'span':1},
       3: {'col': 2, 'row': 5, 'span':1},
       4: {'col': 0, 'row': 4, 'span':1},
       5: {'col': 1, 'row': 4, 'span':1},
       6: {'col': 2, 'row': 4, 'span':1},
       7: {'col': 0, 'row': 3, 'span':1},
       8: {'col': 1, 'row': 3, 'span':1},
       9: {'col': 2, 'row': 3, 'span':1},
}


MATH_POSITIONS = {
    '/':{'col': 2, 'row':3, 'charater':'/', 'operator': '/'},
     '+' :{'col': 3, 'row':5, 'charater':'+', 'operator': '+'},
     '-' :{'col': 3, 'row':4, 'charater':'-', 'operator': '-'},
     '*' :{'col': 3, 'row':3, 'charater':'*', 'operator': '*'},
     '=' :{'col': 3, 'row':6, 'charater':'=', 'operator': '='},
}

OPERATORS = {
    'clear': {'col': 0, 'row':2, 'text': 'C'},
    'bracket':{'col': 1, 'row':2, 'text': '()'}, 
    'percent': {'col': 2, 'row':2, 'text': '%'},
}


TITLE_BAR_HEX_COLORS = {
    'dark': '0x00000000',
    'light': '0x00EEEEEE'
}

BLACK = '#000000'
WHITE = '#EEEEEE'
