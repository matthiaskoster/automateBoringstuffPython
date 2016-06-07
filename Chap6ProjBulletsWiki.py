#! /usr/bin/env python3

# Bullets to Wiki Markup Chap. 6
# Copies text from clipboard, adds a star to each line, pastes to clipboard.

import pyperclip

text = pyperclip.paste()

# TODO: Iterate lines and add star

pyperclip.copy(text)
