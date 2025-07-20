label zoeydate:

    if zoeydate_count == 0:
        jump zoeydate1
    elif zoeydate_count == 1:
        jump zoeydate2
    



    label zoeydate1:
        scene zoeycorridorblur
        show zoeysurprise with dissolve
        zoey "Hey you!"
        name "Hi!"
        show zoeysmile with dissolve
        hide zoeysurprise with dissolve
        zoey "I was looking for you."
        name "Oh, really? Why?"
        zoey "I was just curious about you. That's all."
        name "ok?"
        zoey "I feel like i want to know you better."
        zoey "I mean, you seem like a nice person."
        zoey "Sometimes I get this kind of feeling with people."
        zoey "You give off good energy."
        name "Thanks, you too."
        name "You also give off energy ahah."
        zoey "Oh really?"
        zoey "What kind of energy?"
        name "Well... I don't know how to describe it."
        name "You are... tall?"
        zoey "Ahahah, yeah I tend to look down on people."
        zoey "I mean not like a bad way."
        zoey "On the contrary, I feel like it gives me perspective."
        name "That's well put."
        zoey "No really, I feel like I understand people from up there."
        zoey "It's like I can feel what they want."
        name "Like a god?"
        zoey "Ahahah, no you silly."
        zoey "..."
        zoey "Well, some people might see it that way..."
        zoey "But no, I don't think I'm a god, don't worry."
        zoey "I'm way too scatterbrained for that."
        name "I see."
        zoey "Maybe... that god we learned about in mythology?"
        name "Aphrodite?"
        zoey "No, more like Dionysus."
        name "But he's a man."
        zoey "Yeah... well, you know... haha."
        zoey "He's a pretty ambiguous god."
        zoey "He kind of transgresses gender norms."
        name "I didn't know that."
        zoey "Yes you do, ahah"
        "I blush a little."
        name "Anyway... I should get going."
        name "I am late for.. my class of ... mythology."
        zoey "Sure, I should probably get going too."
        zoey "Oh by the way what's your name?"
        name "I am [name] and you?"
        zoey "Zoey."
        zoey "I have your number, but I didn't know what name to put."
        name "You have my number?"
        zoey "Yeah Hugo gave it to me."
        zoey "J'ai juste mis 'cute new guy'"
        name "ahah ok.. now you have the right name"
        zoey "Yes I will change it"
        name "See you later"
        zoey "Bye [name]."
        "She gives me a playful wave and walks off."
        "I feel a bit invaded by the fact that she knows my number."
        "But she doesn't seems like a bad person."
        $ zoeydate_count += 1
        jump gardenuni_start


    label zoeydate2:
        scene zoeycorridorblur
        show zoeysmile with dissolve
        zoey "I wanted to ask you something"
        name "Sure, what is it?"
        zoey "Do you want to come to a party with me?"
        name "A party?"
        zoey "Yeah you know, a place where people dance and have fun."
        name "Yeah I know what is a party."
        zoey "So, do you want to come?"
        zoey "Je ..."
        show zoeydesire with dissolve
        hide zoeysmile with dissolve
        zoey "You are really cute in that outfit."
        zoey "ça mets en valeur tes formes"
        name "Thanks"
        
        show zoeykiss with dissolve
        hide zoeydesire with dissolve
        
        zoey "No problem"
        jump partydate