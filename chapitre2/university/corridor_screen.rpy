
label corridor: 
    if emma_date_started == False:
        if day % 2 == 0:
            show screen corridor_zoey
            call screen corridor_zoey
        
        scene corridorrealist
        "I wonder in the corridor, looking for something interesting to do,"
        "but nothing comes up."
        "Maybe later."
        jump gardenuni_start2
    elif emma_date_started == True and emma_date_done == False:
        show screen corridor_emma
        call screen corridor_emma
    else:
        scene corridorrealist
        "I wander in the corridor, looking for something interesting to do,"
        "but nothing comes up."
        "Maybe later."
        jump gardenuni_start2

screen corridor_emma:
    frame:
        imagemap:
            ground "corridorrealist2.png"
            hover "corridorrealist2hover.png"
            hotspot (1429, 519, 187, 548) action Jump("emmadate")
            hotspot (1929, 307, 604, 1077) action Jump("gardenuni_start2")
            


screen corridor_zoey:
    frame:
        imagemap:
            ground "université/corridorzoeyphone.png"
            hover "université/corridorzoeyphone.png"
            hotspot (1429, 519, 187, 548) action Jump("partydate")
            hotspot (1929, 307, 604, 1077) action Jump("gardenuni_start2")
            



