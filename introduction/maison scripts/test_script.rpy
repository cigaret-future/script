label cantsleep:
    scene ericawake2
    if linda_1st_conv_done == True and marion_1st_conv_done == True:
        scene sleeping3e
        jump newdaystart    
    else:
        "i can't sleep now"
        show screen homescreen3 with dissolve

        call screen homescreen3

label map2:
    play music "music/skyline.mp3" fadein 1 volume 0.5 loop
    
    show map1 

    "I go out in the street"
    show screen minicarte2 
    call screen minicarte2

 
