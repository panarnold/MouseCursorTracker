#! python
# mouseTrackerpy - prints current position of mouse cursor to the screen
# XI 2020 Arnold Cytrowski

import pyautogui
print('Press Ctrl+C to finish the program')

try:
    while True:
        x, y = pyautogui.position()
        position_str = f'X: {str(x).rjust(4)}, Y: {str(y).rjust(4)}'
        print(position_str, end='')
        print('\b' * len(position_str), end='', flush=True)
except KeyboardInterrupt:
    print('\nAnd it\'s done')
