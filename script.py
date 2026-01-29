# this script handles basic steering input. if you want more precision like linearity of direction
# or deadzones, set this in-game, generally simulation games have this on settings :)

if starting:
    enabled = False
    # sensitivity setting
    sensitivity = 1.5 # !!! you can set your sensitivity here. !!!
    # I M P O R T A N T: if you are getting issues for set the axis on the game, just up the sensitivity, like 1000
    # and reset after.
    
    x = 0
    vJoy[0].x = 16384

# key 'C' toggles on/off the control
if keyboard.getPressed(Key.C): # !!! you can change the toggle key here !!!
    enabled = not enabled
    # lock the mouse to the screen to prevent in-game issues
    mouse.pointerLock = enabled

if enabled:
    # steering logic: x axis movement only for now
    # to add other functions like gas/brake, enable the axes in vJoy Config and map them here.
    x += mouse.deltaX * sensitivity
    
    # vjoy limits (preventing value overflow)
    if x > 16384: x = 16384
    if x < -16384: x = -16384
    
    # mapping: direction value + center = precise position
    vJoy[0].x = x + 16384
else:
    # recenter the wheel when disabled
    x = 0
    vJoy[0].x = 16384

# debug for the freepie console (just if you want to see the sensi, bugs, etc.)
diagnostics.watch(vJoy[0].x)