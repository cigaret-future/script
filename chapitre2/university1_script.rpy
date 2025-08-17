label gardenuni2: 
    stop music fadeout 2.0
    stop sound fadeout 2.0
    play sound universitysound volume 1 loop
    scene garden1
    "I'm in the garden of the university."
    if day == 0:
        jump gardenuni_start
    else:
        jump gardenuni_start2


default unistart = "gardenuni"



label gardenuni_start2:
        stop background fadeout 2.0
        stop music fadeout 2.0
        stop sound fadeout 2.0
        play sound universitysound volume 1 loop
        scene garden1
 
        menu:
            "go to the classroom":
                stop sound fadeout 2.0
                jump classdirection
                "i don't have class right now"
                jump gardenuni_start2
                
            "go to the library":
                    stop sound fadeout 2.0
                    show screen uniscreen2

                    call screen uniscreen2


            "walk around the university":
                stop sound fadeout 2.0
                jump corridor 
                
                jump gardenuni_start2
            

            "return to the street":
                stop sound fadeout 2.0
                jump map3