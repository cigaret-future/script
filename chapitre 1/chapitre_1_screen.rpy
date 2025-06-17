screen cafescreen:
    frame:
        imagemap:
            ground "cafe2.jpg"
            hover "cafe2hover.jpg"
            hotspot (2089, 345, 466, 640) action Jump("map2")
            hotspot (1635, 536, 194, 306) action Jump("Mila1")
            hotspot (1858, 752, 337, 685) action Jump("Barmaid2")
            hotspot (1047, 592, 153, 337) action Jump("lisa_conv_direction")

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
                    



# screen animated_text:
#     text "-100$":
#         font "fonts/Poppins-Regular.ttf"
#         color "#fff"
#         size 50
#         xpos 0.5
#         ypos 1.0
#         xanchor 0.5
#         yanchor 0.5


#         # L'animation fade-in
#         alpha 0.0
#         linear 2.0 alpha 1.0


    