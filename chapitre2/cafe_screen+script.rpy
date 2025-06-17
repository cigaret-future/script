


label cafe1:
    if day == 2 and laura_count < 1:
       
        
        scene slep
        "Not many people in here..."
        show screen cafescreen2
       
        call screen cafescreen2
        
        
       

    elif day == 2 and laura_count >= 1:
        show screen cafescreen_laura_backtobed
        call screen cafescreen_laura_backtobed

    else:
        stop music 
        
        queue coffee_ambiance ["music/coffee.mp3"] volume 1.0 loop 
        jump cafedirection
       

        

   

label cafedirection:
    
    if day >= 3 and day % 2 != 0 and raver_first_conv_done == False:
        show screen cafescreen_raver
        call screen cafescreen_raver

    elif raver_not_over == True:
        show screen cafescreen_raverout
        call screen cafescreen_raverout

    elif day >= 4 and sarahcafe_conv1_done == False or day >= 4 and day_not_over == True:
        show screen cafescreen_sarah
        call screen cafescreen_sarah
    elif elise_cafe == True and elise_cafe_conv_done == False:
        show screen cafescreen_elise
        call screen cafescreen_elise
    elif sarah_cafe == True and sarahcafe_conv2_done == False:
        show screen cafescreen_sarah2
        call screen cafescreen_sarah2
    elif sarah_elise_cafe == True and sarah_elise_cafedate_done == False:
        show screen cafescreen_sarahelise
        call screen cafescreen_sarahelise
    else:
        show screen cafescreen1
        call screen cafescreen1




screen cafescreen2:
            frame:
                imagemap:
                    ground "slep.jpg"
                    hover "slephover.jpg"
                    hotspot (2089, 345, 466, 640) action Jump("exitcafe")
                    hotspot (210, 1003, 486, 389) action Jump("Barmaid3")
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

screen cafescreen1:
    frame:
        imagemap:
            ground "cafe2.jpg"
            hover "cafe2hover.jpg"
            hotspot (2088, 366, 348, 354) action Jump("exitcafe")
            hotspot (1622, 536, 200, 303) action Jump("Mila1")
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
                    
screen cafescreen_sleepylaura:
    frame:
        imagemap:
            ground "slep2.jpg"
            hover "slep2hover.jpg"
            hotspot (2089, 345, 466, 640) action Jump("exitcafe")
            hotspot (1461, 902, 532, 532) action Jump("Barmaid4")
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
                    
screen cafescreen_laura_backtobed:
    frame:
        imagemap:
            ground "slep3.jpg"
            hotspot (2089, 345, 466, 640) action Jump("exitcafe")
            hotspot (226, 1004, 463, 378) action Jump("Barmaid5")
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
                    
screen cafescreen_sarah:
    frame:
        imagemap:
            ground "cafesarah.jpg"
            hover "cafesarahhover.jpg"
            hotspot (2088, 366, 348, 354) action Jump("exitcafe")
            hotspot (1599, 513, 260, 347) action Jump("Mila1_sarahscreen")
            hotspot (1918, 806, 418, 610) action Jump("BarmaidSarah")
            hotspot (948, 470, 170, 317) action Jump("sarahdate")
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
                    
screen cafescreen_raver:
    frame:
        imagemap:
            ground "raverstone.jpg"
            hover "raverstonehover.jpg"
            hotspot (2089, 345, 466, 640) action Jump("exitcafe")
            
            hotspot (1195, 476, 207, 241) action Jump("raverconv")
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
                    
screen cafescreen_raverout:
    frame:
        imagemap:
            ground "raverstone2.jpg"
            hotspot (2089, 345, 466, 640) action Jump("exitcafe")
            
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

screen cafescreen_elise:
    frame:
        imagemap:
            ground "cafeelisefinal.jpg"
            hover "cafeelisefinalhover.jpg"
            hotspot (2177, 402, 206, 356) action Jump("exitcafe")
            hotspot (1635, 536, 194, 306) action Jump("Mila1")
            hotspot (1863, 746, 333, 690) action Jump("Barmaid2")
            hotspot (1050, 592, 141, 334) action Jump ("lisa_conv_direction")
            hotspot (585, 556, 134, 320) action Jump ("Elise")

           
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

screen cafescreen_sarah2:
    frame:
        imagemap:
            ground "cafesarah2.jpg"
            hover "cafeSarahhover2.jpg"
            hotspot (2089, 345, 466, 640) action Jump("exitcafe")
            hotspot (1622, 536, 200, 303) action Jump("Mila1")
            hotspot (1858, 752, 337, 685) action Jump("Barmaid2")
            hotspot (1047, 592, 153, 337) action Jump("lisa_conv_direction")
            hotspot (774, 497, 209, 345) action Jump ("sarahdate")
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

screen cafescreen_sarahelise:
    frame:
        imagemap:
            ground "cafe/elisesarahcafe.png"
            hover "cafe/elisesarahcafehover.png"
            hotspot (2089, 345, 466, 640) action Jump("exitcafe")
            hotspot (1461, 630, 195, 414) action Jump("boss")
            hotspot (1858, 752, 337, 685) action Jump("Barmaid2")
            hotspot (1047, 592, 153, 337) action Jump("lisa_conv_direction")
            hotspot (563, 535, 281, 384) action Jump ("sarahelisecafe")
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



label exitcafe: 
    stop music fadeout 2.0
    stop coffee_ambiance fadeout 2.0
    scene cafe2blur2
    if day == 0:
        jump map2
    else:
        jump map3




