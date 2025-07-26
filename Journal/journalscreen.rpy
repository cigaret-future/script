
label journalscreen:
    scene map1blur
    
    show screen journalopen with Dissolve(0.1)

    call screen journalopen


screen journalopen:
    
    # frame:
    #         align (0.5, 0.5)  # Centre le screen au milieu de l'écran
    #         xysize (1732, 1329)
    window:
        background "journalopen.png"
        xysize (1732, 1329)
        xpos 0.5
        ypos 0.97
        # Center the window in the middle of the screen
        imagebutton:
            idle "croix.png"
            hover "croixhover.png"
            xalign 0.92
            yalign 0.07
            action [Hide("emma_window"), Hide("sarah_window"), Hide("linda_window"), Hide("camille_window"), Hide("chloe_window"), Hide("zoey_window"), Hide("work_window"), Jump("gobacktomap")]

        
        vbox:
            xalign 0.1  # Adjust the alignment to center horizontally
            yalign 0.3 # Adjust the alignment to center vertically
            spacing 10  # Add spacing between buttons
            text "Relationship journal":
                size 50
                color "#2b0606"
                font "fonts/Poppins-Regular.ttf"
                bold True
            

            
           
            textbutton "Work":
                action [Hide("emma_window"), Hide("sarah_window"), Hide("linda_window"), Hide("camille_window"), Hide("chloe_window"), Hide("zoey_window"), Show("work_window")]


            if classdateemma_count >= 1: 
                textbutton "Emma":
                    action [Hide("emma_window"), Hide("sarah_window"), Hide("linda_window"), Hide("camille_window"), Hide("chloe_window"), Hide("zoey_window"), Hide("work_window"), Show("emma_window")]

            if sarah_count >= 1 or sarah_relation_exist == True:
                if elise_sdate_done == True: 
                    textbutton "Elise":
                        action [Hide("emma_window"), Hide("sarah_window"), Hide("linda_window"), Hide("camille_window"), Hide("chloe_window"), Hide("zoey_window"), Hide("work_window"), Show("sarah_window")]
                else:
                    textbutton "Sarah":
                        action [Hide("emma_window"), Hide("sarah_window"), Hide("linda_window"), Hide("camille_window"), Hide("chloe_window"), Hide("zoey_window"), Hide("work_window"), Show("sarah_window")]

            if linda_1st_conv_done == True:
                textbutton "Linda":
                    action [Hide("emma_window"), Hide("sarah_window"), Hide("linda_window"), Hide("camille_window"), Hide("chloe_window"), Hide("zoey_window"), Hide("work_window"), Show("linda_window")]

            if classdatecamille_count >= 1:
                textbutton "Camille":
                    action [Hide("emma_window"), Hide("sarah_window"), Hide("linda_window"), Hide("camille_window"), Hide("chloe_window"), Hide("zoey_window"), Hide("work_window") Show("camille_window")]

            if raver_first_conv_done == True:
                textbutton "Chloe":
                    action [Hide("emma_window"), Hide("sarah_window"), Hide("linda_window"), Hide("camille_window"), Hide("chloe_window"), Hide("zoey_window"), Hide("work_window"), Show("chloe_window")]

            if zoey_first_conv_done == True:
                textbutton "Zoey":
                    action [Hide("emma_window"), Hide("sarah_window"), Hide("linda_window"), Hide("camille_window"), Hide("chloe_window"), Hide("zoey_window"), Hide("work_window"), Show("zoey_window")]

 


screen camille_window:
    frame:
        background None
        xysize (500, 600)
        xalign 0.7
        yalign 0.5
        vbox:
            text "Camille":
                size 40
                color "#2b0606"
                font "fonts/Poppins-Regular.ttf"
                bold True
                
            text camille_relation_status_text:
                size 30
                color "#2b0606"
                font "fonts/Poppins-Regular.ttf"
                xalign 0.5
              
screen emma_window:
    frame:
        background None
        xysize (500, 600)
        xalign 0.7
        yalign 0.5
        vbox:
            text "Emma":
                size 40
                color "#2b0606"
                font "fonts/Poppins-Regular.ttf"
                bold True
                
            text emma_relation_status_text:
                size 30
                color "#2b0606"
                font "fonts/Poppins-Regular.ttf"
                xalign 0.5
            
screen linda_window:
    frame:
        background None
        xysize (500, 600)
        xalign 0.7
        yalign 0.5
        vbox:
            text "Linda":
                size 40
                color "#2b0606"
                font "fonts/Poppins-Regular.ttf"
                bold True
                
            text linda_relation_status_text:
                size 30
                color "#2b0606"
                font "fonts/Poppins-Regular.ttf"
                xalign 0.5
            
screen sarah_window: 
    frame:
        background None
        xysize (500, 600)
        xalign 0.7
        yalign 0.5
        vbox:

            if elise_sdate_done == True:
                text "Elise":
                    size 40
                    color "#2b0606"
                    font "fonts/Poppins-Regular.ttf"
                    bold True
            else:
                text "Sarah":
                    size 40
                    color "#2b0606"
                    font "fonts/Poppins-Regular.ttf"
                    bold True
            text sarah_relation_status_text:
                size 30
                color "#2b0606"
                font "fonts/Poppins-Regular.ttf"
                xalign 0.5
           
screen chloe_window: 
    frame:
        background None
        xysize (500, 600)
        xalign 0.7
        yalign 0.5
        vbox:
            text "Chloe":
                size 40
                color "#2b0606"
                font "fonts/Poppins-Regular.ttf"
                bold True
                
            text chloe_relation_status_text:
                size 30
                color "#2b0606"
                font "fonts/Poppins-Regular.ttf"
                xalign 0.5
           

screen zoey_window:
    frame:
        background None
        xysize (500, 600)
        xalign 0.7
        yalign 0.5
        vbox:
            text "Zoey":
                size 40
                color "#2b0606"
                font "fonts/Poppins-Regular.ttf"
                bold True
                
            text zoey_relation_status_text:
                size 30
                color "#2b0606"
                font "fonts/Poppins-Regular.ttf"
                xalign 0.5


screen work_window:
    frame:
        background None
        xysize (500, 600)
        xalign 0.7
        yalign 0.5
        vbox:
            text "Work":
                size 40
                color "#2b0606"
                font "fonts/Poppins-Regular.ttf"
                bold True
                
            text work_status_text:
                size 30
                color "#2b0606"
                font "fonts/Poppins-Regular.ttf"
                xalign 0.5



screen minicarte3journal:
    frame:
        imagemap:
            idle "map1.jpg"
            ground "map1.jpg"

            imagebutton: 
                idle "journalicon.png"
                hover "journaliconhover.png"
                xalign 0.850
                yalign 0.040
               
                
            imagebutton:
                idle "pinpoint.png"
                hover "pinpointlight.png"
                xalign 0.6955
                yalign 0.355
                
            imagebutton:
                idle "pinpoint.png"
                hover "pinpointlight.png"
                xalign 0.7937
                yalign 0.525
                
            imagebutton:
                idle "cartl.png"
                hover "cartlight.png"
                xalign 0.5715
                yalign 0.305
                
            imagebutton:
                idle "pinpoint.png"
                hover "pinpointlight.png"
                xalign 0.106
                yalign 0.2629
                
          



    frame:
        background "textbackground.png"  # Chemin de l'image pour le background du texte
        # Utilisation de padding pour ajuster l'espace autour du texte
        xpadding 10
        ypadding 10
        
        # Positionnement du texte et du frame
        xpos 2225
        ypos 50

        # Le texte lui-même
        text "[money]$":
            font "fonts/Poppins-Regular.ttf"
            color "#fff"
            size 35
            bold True
            anchor (-140, -30)


label gobacktomap:
    show screen minicarte3
    call screen minicarte3                       