#!/usr/bin/env python3

import i3ipc 

i3 = i3ipc.Connection()
focused = i3.get_tree().find_focused()
windows = focused.workspace().leaves()

if (len(windows)>1):
  largest_size=0
  for w in windows:
    w_size = w.rect.height*w.rect.width
    if (w.focused is False and w_size>largest_size):
      largest = w
      largest_size=w_size
  i3.command("mark focused")
  largest.command("focus")
  i3.command("swap container with mark focused")
  i3.command("unmark focused")