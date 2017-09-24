#Created by : Sidney Kang
#Created on : 24 Sept. 2017
#Created for : ICS3UR
# Daily Assignment - Unit1-04
# This program calculates the circumference of a circle in cm with the radius given by the user

import ui

def calculate_circumference_touch_up_inside(sender):
    #This calculates the circumference of the circle in cm
    
    # constants
    Pi = 3.14
    
    #input
    radius = float(view['input_of_radius_textbox'].text)
    
    #process
    circumference = 2.0*Pi*radius
    
    #output
    view['circumference_label'].text = "Circumference = "+str(circumference)+" cm"

view = ui.load_view()
view.present('full_screen')
