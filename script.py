# ===============================================================================
# MOUSE STEERING SCRIPT FOR F1 & SIM-RACING
# Developed by Emanuel (sousa7tz) - Systems Development Student
# ===============================================================================
# Use this script to steer with your mouse via vJoy.
# Adjust sensitivity in-game using the Mouse Wheel for better control.

import winsound

if starting:
    enabled = False
    
    # Starting sensitivity value
    sensitivity = 1.5 
    standard_sensitivity = sensitivity 

    x = 0
    vJoy[0].x = 0

# TOGGLE CONTROL: Press 'C' to enable/disable steering
if keyboard.getPressed(Key.C):
    enabled = not enabled
    if enabled:
        winsound.Beep(1000, 150) # Activation tone
    else:
        winsound.Beep(400, 150)  # Deactivation tone
    
# DYNAMIC SENSITIVITY: Scroll UP to increase / Scroll DOWN to decrease
if mouse.wheel > 0:
    sensitivity += 0.1
    winsound.Beep(1300, 20)
    mouse.wheel = 0 
    
if mouse.wheel < 0:
    sensitivity -= 0.1
    winsound.Beep(800, 20)
    mouse.wheel = 0 
    
# RESET SENSITIVITY: Click Middle Mouse Button to return to default
if mouse.middleButton:
    sensitivity = standard_sensitivity
    winsound.Beep(600, 100)
    
if enabled:
    # Steering calculations
    x += mouse.deltaX * sensitivity

    # Axis limits to prevent overflow
    if x > 16384: x = 16384
    if x < -16384: x = -16384

    vJoy[0].x = x
else:
    # Centers the wheel when steering is disabled
    x = 0
    vJoy[0].x = 0

# Monitoring values in FreePIE console
diagnostics.watch(vJoy[0].x)
diagnostics.watch(sensitivity)