label gardenuni2: 
    stop music fadeout 2.0
    scene garden1
    "I'm in the garden of the university."
    if day == 0:
        jump gardenuni_start
    else:
        jump gardenuni_start2


default unistart = "gardenuni"



label gardenuni_start2:
        stop music fadeout 2.0
        
        scene garden1
 
        menu:
            "go to the classroom":
                jump classdirection
                "i don't have class right now"
                jump gardenuni_start2
                
            "go to the library":
                    show screen uniscreen2

                    call screen uniscreen2


            "walk around the university":
                jump corridor
                
                jump gardenuni_start2
            

            "return to the street":
                show screen minicarte3

                call screen minicarte3