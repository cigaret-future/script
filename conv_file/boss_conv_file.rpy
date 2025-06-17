label boss:
    if boss_conv_done == True:
        scene elisesarahcafe
        "I already talked to her."
        jump cafedirection
    elif boss_conv_done == False:

        scene elisesarahcafe
        show neutral3 with dissolve
        elo "Hey, what's up?"
        name "I'm just passing by."
        elo "Cool, you come here often?"
        name "Yeah, I like this place."
        elo "How's the service?"
        name "It's nice, it feels like a familiar place."
        name "And the coffee is good."
        elo "Excellent."
        name "Why do you ask?"
        show bosssmile with dissolve
        hide neutral3 with dissolve
        elo "Oh, because I run the place."
        name "Really?"
        elo "Yeah, I own 3 bars in this city."
        name "That's impressive."
        name "How do you manage that?"
        elo "It's a lot of work."
        elo "But I love it."
        elo "I am a workaholic, ahah."
        elo "But I'm working on it."
        name "How do you do it?"
        show neutral3 with dissolve
        hide bosssmile with dissolve
        elo "I have a great team."
        elo "I try to delegate as much as possible."
        elo "And a lot of sport."
        show bosslaugh with dissolve
        hide neutral3 with dissolve
        elo "Loooot of sport."
        name "I see."
        name "That seems like a good balance."
        name "I can't see myself running a business at all."
        name "Managing my life is already a lot."
        show neutral3 with dissolve
        hide bosslaugh with dissolve
        elo "It's not for everyone, that's for sure."
        elo "I also couldn't imagine being in this position when I was younger."
        elo "But now I'm here."
        elo "I have two young children, a wife, and some businesses to run."
        name "Wow."
        elo "Yeah, it's a lot, ahah."
        name "I can't imagine."
        elo "I'm Elodie, by the way."
        name "I'm [name]."
        elo "Nice to meet you."
        elo "I hope you enjoy your time here."
        elo "I'll see you around."
        name "Alright."
        hide neutral3 with dissolve
        $ boss_conv_done = True
        jump cafedirection