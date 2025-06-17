default rav = Character('Chloe', color="#b493e7")

label raverconv:
    # "thanks for playing the demo, if you want to unlock this content please consider supporting the game on patreon"
    # jump map3
    scene raverstone
    "This girl seems to be wasted."

    "She probably didn't sleep all night. She smells like whisky and sweat. Ah, youth."
    "I should probably check on her."
    scene cafeblur with dissolve
    show chloestone with dissolve
    rav "Bl...rg..."

    name "Are you okay?"

    rav "My... head..."

    rav "Ghh..."

    rav "I need... coffee, please..."

    name "Maybe start with some water."

    rav "Water first, then coffee."

    name "I'll be right back."
    hide chloestone with dissolve
    scene raverstone with dissolve
    "I go to the counter."

    name "Hey, can you give her a coffee and a large glass of water? I'll pay for it."
    show barmaidpissed with dissolve
    lau "Sure, but looking at her, a stomach pump might be more appropriate."

    name "I am surprised you even let her in here."

    name "You are not as cold as you seem."

    lau "I have a heart, you know. Plus, she makes everyone else feel a lot better about their own hangovers."

    name "You should add a 'special hangover' drink to your menu."
    hide barmaidpissed
    show barmaidsmile
    lau "Yeah, I could add some liquor to their coffee, that would do the trick. Thanks for the idea."

    name "That's not what I meant..."

    lau "What? I can't hear you over the coffee machine."
    hide barmaidsmile with dissolve
    name "Never mind."

    "I go back to sit with the wasted girl."

    scene cafeblur with dissolve
    show chloestone with dissolve
    rav "Please... water."

    name "It's on its way."

    "The barmaid brings the water and the coffee."
    lau "Here, make sure she doesn't vomit on the floor, please."
    show text "-3$" at Move((0.5, 0.6), (0.5, 0.5), 2.0) 
    hide text with dissolve
    $ money -= 3 
    name "I'll do my best."
    name "Here, drink this."
    show chloevoid with dissolve
    hide chloestone with dissolve
    rav "Thanks."
    rav "It feels good."
    rav "My brain feels like mush."
    show chloe awake with dissolve
    hide chloevoid with dissolve
    rav "How the hell did I end up here?"

    name "I don't know, you were there when I arrived."

    rav "I feel like I have been hit by a truck."

    name "I bet. I hope it was worth it."
    show chloethinking with dissolve
    hide chloe awake with dissolve
    rav "For the first part, it was."
    name "What happened?"
    show chloe awake with dissolve
    hide chloethinking with dissolve
    rav "How would I know?"
    name "..."
    rav "Please don't question my life choices right now. I am not in a position to argue."
    show chloerealising with dissolve 
    hide chloe awake with dissolve
    rav "..."
    rav "I know... I am a mess."

    name "Don't worry about it."
    name "Just enjoy your coffee."
    name "You will feel better."

    show chloelook with dissolve
    hide chloerealising with dissolve
    rav "I am Chloe."
    name "[name]."
    name "Nice to meet you."
    rav "Thanks for the water and coffee. People are not usually that nice."
    name "No problem."
    name "I guess I am not used to seeing people looking like dead bodies in the morning."

    show chloesmile with dissolve
    hide chloelook with dissolve
    rav "That explains it."
    rav "You are not from around here."
    name "Yeah, I moved in not long ago."
    rav "Welcome to this beautiful city."
    rav "It doesn't look like it, but it's actually worth the pain."
    name "I'll take your word for it."
    rav "I am not really what you would call a reliable source."
    rav "But if you want to try it for yourself, I know a few places to visit."
    rav "If you want to have fun."
    name "Why not."
    rav "I don't usually do this, but you seem trustworthy."
    rav "I'll give you my number."
    rav "Send me a text if you want to go out."
    name "Oh, ok, thanks."
    rav "I am gonna go now. I am probably still drunk, and I am not entirely sure what I am doing."
    hide chloesmile with dissolve
    if gender == "male":
        rav "Thanks for the coffee, man."
    elif gender == "fem":
        rav "Thanks for the coffee"
    name "No problem."
    name "Be safe."
    "She leaves the café, staggering."
    $ raver_first_conv_done = True
    $ raver_not_over = True

    jump map3