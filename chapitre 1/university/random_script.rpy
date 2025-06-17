label randompeople:
    scene uniempty
    "these peoples seems to chill"
    "i should probably go to my class before i am late"
    show screen uniscreenempty

    call screen uniscreenempty


define sam = Character('Samuel', color="#a8f9ff") 
define elisa = Character('Elisa', color="#80a1fc") 

label randompeople2:
    if linda_conv_done == True:
        scene unilindaout
    elif linda_conv_done == False:
        scene uni1
    
    sam "You know, I think I might need a break."
    elisa "My brain is starting to fry."
    sam "I could use a breather too."
    elisa "Maybe we should grab some snacks or go for a walk or something."

    if day == 0:
        if linda_conv_done == True:
            show screen uniscreenlindaout

            call screen uniscreenlindaout

        elif linda_conv_done == False:
            show screen uniscreen
            call screen uniscreen
    else: 
        show screen uniscreen2
        call screen uniscreen2  