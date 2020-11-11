#! python
# mouseTrackerpy - prints current position of mouse cursor to the screen
# update: it also get info about color of current pixel in RGB
# XI 2020 Arnold Cytrowski

import pyautogui
print('Press Ctrl+C to finish the program')

try:
    while True:
        x, y = pyautogui.position()
        pixel_color = pyautogui.screenshot().getpixel((x,y))
        position_str = f'X: {str(x).rjust(4)}, Y: {str(y).rjust(4)} RGB: ({str(pixel_color[0]).rjust(3)}, {str(pixel_color[1]).rjust(3)}, {str(pixel_color[2]).rjust(3)})'
        print(position_str, end='')
        print('\b' * len(position_str), end='', flush=True)
except KeyboardInterrupt:
    print('\nAnd it\'s done')
