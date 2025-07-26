label boss:
    if boss_conv_done == True:
        scene elisesarahcafe
        "I already talked to her."
        jump cafedirection
    elif boss_textconv_done == True:
        scene elisesarahcafe
        show neutral3 with dissolve
        elod "Hey, [name]."
        name "Hey, Elodie."
        elod "How's your day going?"
        name "It's been good, just finished my shift."
        elod "Do you like working here?"
        name "Yeah, sure.."
        elod "That's great to hear."
        $ boss_conv_done = True
        jump cafedirection
       
        
    elif boss_conv_done == False:

        scene elisesarahcafe
        show neutral3 with dissolve
        elod "Hey, what's up?"
        name "I'm just passing by."
        elod "Cool, you come here often?"
        name "Yeah, I like this place."
        elod "How's the service?"
        name "It's nice, it feels like a familiar place."
        name "And the coffee is good."
        elod "Excellent."
        name "Why do you ask?"
        show bosssmile with dissolve
        hide neutral3 with dissolve
        elod "Oh, because I run the place."
        name "Really?"
        elod "Yeah, I own 3 bars in this city."
        name "That's impressive."
        name "How do you manage that?"
        elod "It's a lot of work."
        elod "But I love it."
        elod "I am a workaholic, ahah."
        elod "But I'm working on it."
        name "How do you do it?"
        show neutral3 with dissolve
        hide bosssmile with dissolve
        elod "I have a great team."
        elod "I try to delegate as much as possible."
        elod "And a lot of sport."
        show bosslaugh with dissolve
        hide neutral3 with dissolve
        elod "Loooot of sport."
        name "I see."
        name "That seems like a good balance."
        name "I can't see myself running a business at all."
        name "Managing my life is already a lot."
        show neutral3 with dissolve
        hide bosslaugh with dissolve
        elod "It's not for everyone, that's for sure."
        elod "I also couldn't imagine being in this position when I was younger."
        elod "But now I'm here."
        elod "I have two young children, a wife, and some businesses to run."
        name "Wow."
        elod "Yeah, it's a lot, ahah."
        name "I can't imagine."
        elod "I'm Elodie, by the way."
        name "I'm [name]."
        elod "Nice to meet you."
        elod "I hope you enjoy your time here."
        elod "I'll see you around."
        name "Alright."
        hide neutral3 with dissolve
        $ boss_conv_done = True
        jump cafedirection