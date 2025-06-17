define olia = Character('Olivia', color="#c8c8c8")
label rentdue:
    if rentdue_meet_count == 0:
        jump rentdue1
    elif rentdue_meet_count == 1:
        jump rentdue2

label rentdue1:


    scene home00
    "Someone is knocking on the door."
    "I quickly get dressed and open the door."
    "Fuck... It's my landlord."
    scene rentasking
    if gender == "male":
        olia "Hi, Mr. Smith."
    elif gender == "fem":
        olia "Hi, Mrs. Smith."
    olia "I just wanted to check if you've settled into your new home."
    name "Oh yes, thanks for stopping by. Yes, everything is going well. I was able to meet my neighbors, and I'm happy with everything."
    olia "Great, that's just great. I don't know if someone told you, but I live just next to your building, and I like to stop by and check in on my tenants."
    name "I don't think I have any issue with that."
    scene rentasking2
    olia "And I take this opportunity to come and collect the rent..."
    name "Oh."
    olia "Yeah, I started doing that after a bad experience with a tenant I had."
    olia "I hope that's not an issue for you."
    name "No, not at all, of course."
    name "I'll make the transfer right away."
    scene rentasking3
    if gender == "male":
        olia "Thank you so much, Mr. Smith."
    elif gender == "fem":
        olia "Thank you so much, Mrs. Smith."
    olia "I'll see you next week."
    name "Alright, bye."
    if money < 700:
        $ money += 0
    elif money >= 700:
        $ money -= 700
        show text "-700$" at Move((0.5, 0.6), (0.5, 0.5), 2.0) 
        hide text with dissolve
    $ rentdue_meet_count += 1
    show screen homescreen4
    call screen homescreen4

    label rentdue2: 
        scene home00
        "Someone is knocking on the door."
        "I quickly get dressed and open the door."
        "Fuck... It's my landlord."
        scene rentasking
        if gender == "male":
            olia "Hello, Mr. Smith."
        elif gender == "fem":
            olia "Hello, Mrs. Smith."
        name "Hi..."
        olia "I hope I am not waking you up."
        name "Nooo, I was getting ready to go."
        olia "Great, so about the rent..."
        if money < 700:
            name "I am not sure I will be able to pay the rent this week."
            olia "Well, well, we'll have to find an arrangement then."
            scene black
            
            "This part is still in development ;)"
            jump map3
        else:
            name "I'll make the transfer right away."
            scene rentasking3
            if gender == "male":
                olia "Thank you so much, Mr. Smith."
            elif gender == "fem":
                olia "Thank you so much, Mrs. Smith."
            olia "I'll see you next week."
            name "Alright, bye."
            $ money -= 700
            show text "-700$" at Move((0.5, 0.6), (0.5, 0.5), 2.0) 
            hide text with dissolve 
            hide text with dissolve
            
            show screen homescreen4
            call screen homescreen4
