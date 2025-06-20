label vestibule:
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


label upstairs:
    show screen upstairspartyscreen
    call screen upstairspartyscreen

screen upstairspartyscreen:
    frame:
        imagemap:
            ground "party/corridorscreenarrow.png"
            hover "party/corridorscreenarrowhover.png"
            hotspot (62, 1117, 411, 317) action Jump("livingroom")
            hotspot (520, 236, 331, 720) action Jump("toiletparty")
            hotspot (1602, 115, 373, 1127) action Jump("partybathroom")
            

label balcony:
    show screen balconypary
    call screen balconypary

screen balconypary:
    frame:
        imagemap:
            ground "party/balconynobodyarrow.png"
            hover "party/balconynobodyarrowhover.png"
            hotspot (243, 209, 287, 1154) action Jump("kitchenparty")
            hotspot (1440, 209, 287, 1154) action Jump("sebastianconv")