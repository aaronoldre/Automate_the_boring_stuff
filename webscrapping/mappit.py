import webbrowser
import sys
import pyperclip

sys.argv # ['mappit.py', '870', 'Valencia', 'St.']

# Check if command line arguments were passed
if len(sys.argv) > 1:
    # ['mappit.py', '870', 'Valencia', 'St.'] - > '870 Valencia St.'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)
