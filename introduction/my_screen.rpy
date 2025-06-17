screen telephone: 
    text "This is a screen that will be displayed when the player is using the telephone."

screen cupoftea:
    imagebutton:
        xpos 190
        ypos 450
        idle "cupoftea.png"
        at custom_zoom
        action Jump("teadrinked")

transform custom_zoom:
    zoom 0.5


screen inventory: 
    hbox: 
        for i in player_inventory: 
            frame:
                xmargin 10
                ymargin 10

                add i.image size(100, 100)




screen homescreen3:
    frame:
        imagemap:
            ground "ericawake2.jpg"
            hover "ericawake2hover.png"
            hotspot (0, 1020, 1088, 414) action Jump("cantsleep")
            hotspot (2191, 248, 362, 1047) action Jump("map2")

screen hover_pinpoint():
    # L'image à afficher lorsque la zone est survolée
    add "pinpointlight.png" xalign 0.5 yalign 0.3

screen minicarte2:
                
                
                frame:
                   
                    imagemap:
                        idle"map1.jpg"
                        ground "map1.jpg"
                        imagebutton: 
                            idle "journalicon.png"
                            hover "journaliconhover.png"
                            xalign 0.850
                            yalign 0.040
                            action Jump ("journalscreen")
                        imagebutton:
                            idle "pinpoint.png"
                            hover "pinpointlight.png"
                            xalign 0.6955
                            yalign 0.355
                            action Jump ("back")
                        imagebutton:
                            idle "pinpoint.png"
                            hover "pinpointlight.png"
                            xalign 0.7937
                            yalign 0.525
                            action Jump ("cafe")
                        imagebutton:
                            idle "cartl.png"
                            hover "cartlight.png"
                            xalign 0.5715
                            yalign 0.305
                            action Jump ("nothing")
                        imagebutton:
                            idle "pinpoint.png"
                            hover "pinpointlight.png"
                            xalign 0.106
                            yalign 0.2629
                            action Jump ("gardenuni")

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



label back :
    show screen homescreen3
    call screen homescreen3
label nothing: 
    show map1
    "i have everything i need"
    jump map2  
