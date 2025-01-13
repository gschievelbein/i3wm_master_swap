# i3wm_master_swap

Quick script to swap the focused window to the largest window in the same screen (i3wm/sway).


Just bind it to a key combination in your config:

* bindsym  <binding> exec $XDG_CONFIG_HOME/i3/scripts/swapper.py
  
Use it with https://github.com/gschievelbein/stacki3 for a simple master/stack layout :)
  
# Requirements
* i3ipc-python
