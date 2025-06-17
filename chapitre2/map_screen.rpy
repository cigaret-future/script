label map3:
    
    play music "music/skyline.mp3" fadein 1 volume 0.2 loop
    show screen minicarte3 with dissolve 
    call screen minicarte3 




screen minicarte3:
    frame:
        imagemap:
            idle "map1.jpg"
            ground "map1.jpg"

            imagebutton: 
                idle "journalicon.png"
                hover "journaliconhover.png"
                xalign 0.850
                yalign 0.040
                action Jump ("journalscreen")
            imagebutton:
                idle "sleepicon.png"
                hover "sleepiconhover.png"
                xalign 0.725
                yalign 0.355
                action Jump ("quickgotobed")    
            imagebutton:
                idle "pinpoint.png"
                hover "pinpointlight.png"
                xalign 0.6955
                yalign 0.355
                action Jump ("backhome")
            imagebutton:
                idle "pinpoint.png"
                hover "pinpointlight.png"
                xalign 0.7937
                yalign 0.525
                action Jump ("cafe1")
            imagebutton:
                idle "cartl.png"
                hover "cartlight.png"
                xalign 0.5715
                yalign 0.305
                action Jump ("shop")
            imagebutton:
                idle "pinpoint.png"
                hover "pinpointlight.png"
                xalign 0.106
                yalign 0.2629
                action Jump ("gardenuni2")
           
            if linda_invitation_sent == True:

                imagebutton:
                    idle "pinpoint.png"
                    hover "pinpointlight.png"
                    xalign 0.08
                    yalign 0.450
                    action Jump("lindadate5")
            if boss_textconv_done == True:
                imagebutton:
                    idle "workicon.png"
                    hover "workiconhover.png"
                    xalign 0.55
                    yalign 0.11
                    action Jump("workplace")


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
