label vestibule:
    $ renpy.music.set_volume(1, delay=0.5, channel="background")
    if zoeyaxelconv_count >= 3 and  zoey_vestibul_asked == False:
        jump kitchenzoeyconv
    else: 
        show screen vestibulescreen
        call screen vestibulescreen

screen vestibulescreen:
    frame:
        if drink_count >= 5:
            imagemap:
                ground "party/blur/vestibulearrowandblur.png"
                hover "party/blur/vestibulearrowhoverandblur.png"
                hotspot (750, 337, 885, 1102) action Jump("isabelleconv")
                hotspot (84, 1073, 277, 283) action Jump("kitchenparty")
                hotspot (2212, 1062, 340, 308) action Jump("livingroom")
        else:
            imagemap:
                ground "party/vestibulearrow.png"
                hover "party/vestibulearrowhover.png"
                hotspot (750, 337, 885, 1102) action Jump("isabelleconv")
                hotspot (84, 1073, 277, 283) action Jump("kitchenparty")
                hotspot (2212, 1062, 340, 308) action Jump("livingroom")

label livingroom:
    $ renpy.music.set_volume(1, delay=0.5, channel="background")
    if drink_count >= 5 and renpy.random.randint(1, 3) == 1:
        scene ericbourredanse
        "I can't help but dance a little."
        "People around me laugh and cheer me on."
        "I feel like my body is more receptive to the music."
    
     
    show screen livingroomscreen
    call screen livingroomscreen

screen livingroomscreen:
    frame:
        if drink_count >= 5:
            imagemap:
                ground "party/blur/livingroomarrowandblur.png"
                hover "party/blur/Livingroomarrowhoverandblur.png"
                hotspot (1989, 1139, 570, 287) action Jump("vestibule")
                hotspot (1392, 329, 362, 743) action Jump("zoeyconv_direction")
                hotspot (503, 286, 272, 918) action Jump("estelleconv")
                hotspot (22, 1077, 435, 355) action Jump ('upstairs')
        else:
            imagemap:
                ground "party/livingroomarrow.png"
                hover "party/Livingroomarrowhover.png"
                hotspot (1989, 1139, 570, 287) action Jump("vestibule")
                hotspot (1392, 329, 362, 743) action Jump("zoeyconv_direction")
                hotspot (503, 286, 272, 918) action Jump("estelleconv")
                hotspot (22, 1077, 435, 355) action Jump ('upstairs')

label kitchenparty:
    stop music fadeout 0.5
    $ renpy.music.set_volume(0.5, delay=0.5, channel="background")
    if (stacydate_activated == True or tracymelaniedate_done == True) and (sebastianjen_date_started == True or sebastianjen_date_done == True):
        show screen kitchenpartynobody
        call screen kitchenpartynobody
        
    elif sebastianjen_date_started == True:
        show screen kitchenpartynojenscreen
        call screen kitchenpartynojenscreen
    elif stacydate_activated == True or tracymelaniedate_done == True:
        show screen kitchenpartynomelscreen
        call screen kitchenpartynomelscreen

    elif sebastianjen_date_started == True:
        show screen kitchenpartynojenscreen
        call screen kitchenpartynojenscreen
    else:
        show screen kitchenpartyscreen
        call screen kitchenpartyscreen

screen kitchenpartyscreen:
    frame:
        if drink_count >= 5:
            imagemap:
                ground "party/blur/kitchenarrowandblur.png"
                hover "party/blur/kitchenarrowwithbottleandblur.png"
                hotspot (1445, 193, 213, 434) action Jump("vestibule")
                hotspot (437, 474, 434, 716) action Jump("stacymelanieconv")
                hotspot (1836, 412, 387, 578) action Jump("trioconv")
                hotspot (23, 1143, 418, 270) action Jump("balcony")
                hotspot (1190, 676, 244, 224) action Jump("drinking")
        else:
            imagemap:
                ground "party/kitchenarrow.png"
                hover "party/kitchenarrowwithbottle.png"
                hotspot (1445, 193, 213, 434) action Jump("vestibule")
                hotspot (437, 474, 434, 716) action Jump("stacymelanieconv")
                hotspot (1836, 412, 387, 578) action Jump("trioconv")
                hotspot (23, 1143, 418, 270) action Jump("balcony")
                hotspot (1190, 676, 244, 224) action Jump("drinking")

screen kitchenpartynojenscreen:
    frame:
        if drink_count >= 5:
            imagemap:
                ground "party/blur/kitchenarrownojenblur.png"
                hover "party/blur/kitchenarrownojenhoverblur.png"
                hotspot (1445, 193, 213, 434) action Jump("vestibule")
                hotspot (437, 474, 434, 716) action Jump("stacymelanieconv")
                hotspot (1190, 676, 244, 224) action Jump("drinking")
                hotspot (23, 1143, 418, 270) action Jump("balcony")
        else:
            imagemap:
                ground "party/kitchenarrownojen.png"
                hover "party/kitchenarrownojenhover.png"
                hotspot (1445, 193, 213, 434) action Jump("vestibule")
                hotspot (437, 474, 434, 716) action Jump("stacymelanieconv")
                hotspot (1190, 676, 244, 224) action Jump("drinking")
                hotspot (23, 1143, 418, 270) action Jump("balcony")



screen kitchenpartynobody:
    frame:
        if drink_count >= 5:
            imagemap:
                ground "party/kitchenarrownobodyblur.png"
                hover "party/kitchenarrownobodyblurhover.png"
                hotspot (1445, 193, 213, 434) action Jump("vestibule")
                
                hotspot (1836, 412, 387, 578) action Jump("trioconv")
                hotspot (23, 1143, 418, 270) action Jump("balcony")
                hotspot (1190, 676, 244, 224) action Jump("drinking")
        else:
            imagemap:
                ground "party/kitchenarrownobody.png"
                hover "party/kitchenarrownobodyhover.png"
                hotspot (1445, 193, 213, 434) action Jump("vestibule")
                
                hotspot (1836, 412, 387, 578) action Jump("trioconv")
                hotspot (23, 1143, 418, 270) action Jump("balcony")
                hotspot (1190, 676, 244, 224) action Jump("drinking")




screen kitchenpartynomelscreen:
    frame:
        if drink_count >= 5:
            imagemap:
                ground "party/blur/kitchenarrownomelblur.png"
                hover "party/blur/kitchenarrownomelhoverblur.png"
                hotspot (1445, 193, 213, 434) action Jump("vestibule")
                
                hotspot (1836, 412, 387, 578) action Jump("trioconv")
                hotspot (23, 1143, 418, 270) action Jump("balcony")
                hotspot (1190, 676, 244, 224) action Jump("drinking")
        else:
            imagemap:
                ground "party/kitchenarrownomel.png"
                hover "party/Kitchenarrownomelhover.png"
                hotspot (1445, 193, 213, 434) action Jump("vestibule")
                
                hotspot (1836, 412, 387, 578) action Jump("trioconv")
                hotspot (23, 1143, 418, 270) action Jump("balcony")
                hotspot (1190, 676, 244, 224) action Jump("drinking")




label upstairs:
    $ renpy.music.set_volume(0.5, delay=0.5, channel="background")
    if stacydate_activated == True:
        show screen upstairspartystactyscreen
        call screen upstairspartystactyscreen
    else:
        show screen upstairspartyscreen
        call screen upstairspartyscreen

screen upstairspartyscreen:
    frame:
        imagemap:
            ground "party/corridorscreenarrow.png"
            hover "party/corridorscreenarrowhover.png"
            hotspot (62, 1117, 411, 317) action Jump("livingroom")
            hotspot (520, 236, 331, 720) action Jump("toiletparty")
            hotspot (1580, 18, 408, 1273) action Jump("partybathroom")
            
screen upstairspartystactyscreen:
    frame:
        imagemap:
            ground "party/corridorscreenarrowtracy.png"
            hover "party/corridorscreenarrowtracyhover.png"
            hotspot (62, 1117, 411, 317) action Jump("livingroom")
            hotspot (520, 236, 331, 720) action Jump("toiletparty")
            hotspot (1580, 18, 408, 1273) action Jump("partybathroom")
            hotspot (540, 945, 293, 174) action Jump("tracydate2")




label balcony:
    $ renpy.music.set_volume(0.2, delay=0.5, channel="background")
    play music skylineparty volume 2 loop
    if sebastianjen_date_started == True:
        scene balconynobodyblur
        "There is no one I could talk to on the balcony."
        "I should go back inside."
        jump kitchenparty
    else:
        show screen balconypary
        call screen balconypary

screen balconypary:
    frame:
        if drink_count >= 5:
            imagemap:
                ground "party/blur/balconynobodyarrowblur.png"
                hover "party/blur/balconynobodyarrowhoversebblur.png"
                hotspot (243, 209, 287, 1154) action Jump("kitchenparty")
                hotspot (1214, 480, 381, 930) action Jump("sebastianconv")
        else:
            imagemap:
                ground "party/balconynobodyarrow.png"
                hover "party/balconynobodyarrowhoverseb.png"
                hotspot (243, 209, 287, 1154) action Jump("kitchenparty")
                hotspot (1214, 480, 381, 930) action Jump("sebastianconv")