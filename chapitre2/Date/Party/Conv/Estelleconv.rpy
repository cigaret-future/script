label estelleconv :
    label estelleconv_direction:

        if drink_count >= 10:
            jump estelleconvbourre3
        
        elif drink_count >= 5 and and drink_count < 10 and estellebourreconv_done == False:
            jump estelleconvbourre1
        elif drink_count >= 5 and drink_count < 10 and estellebourreconv_done == True:
            jump estelleconvbourre2
        


        elif estellepartyconv_count == 0:
            jump estelleconv1
        elif estellepartyconv_count == 1:
            jump estelleconv2
        
    label estelleconvbourre:
        label estelleconvbourre1:
            scene livingroomarrow
            scene livingroomarrowflou with dissolve
            show estherparty with dissolve
            name "You know you have the same eyes as my cat."
            est "Thanks, I guess?"
            name "No, it's a compliment! He's very mysterious. And a bit aggressive."
            est "What's his name?"
            name "Uh, I don't know."
            show esther15 with dissolve
            hide estherparty with dissolve
            est "You don't know your cat's name?"
            name "No, but I don't have a cat. But if I did, he'd have those eyes."
            est "..."
            name "Do you want to come to my place? He needs an eye model."
            est "No thanks."
            $ estellebourreconv_done = True
            $ estellepartyconv_count += 1
            jump livingroom
            
        label estelleconvbourre2:
            scene livingroomarrow
            scene livingroomarrowflou with dissolve
            show esther12 with dissolve
            est "Are you okay?"
            name "Sure, I just need to dance a little."
            name "Do you want to dance with me?"
            est "No thanks."
            est "Just so you know, if you faint, don't count on me to help you."
            name "Thanks, I knew I could count on you."
            $ estellebourreconv_done = True
            $ estellepartyconv_count += 1
            jump livingroom
        
        label estelleconvbourre3:
            scene livingroomarrow
            scene livingroomarrowflou with dissolve
            show estherparty with dissolve
            est "Don't you think you've had enough to drink?"
            name "No, as long as I can crawl, I'm fine."
            est "You know you can die from alcohol poisoning, right?"
            est "If you die, could you do it a bit further away, please."
            est "I don't want to be the one who has to call for help."
            "As I try to articulate a response, I feel myself losing balance and fall to the floor."
            "I wake up a few minutes later, lying on a bed."
            "The light is off, and I can hear music playing in the distance."
            "I try to get up, but my head is spinning and I feel nauseous."
            "I'd better stay lying down for a while."
            "I fall asleep again."
            "The next day, I wake up in an unfamiliar room."
            "It seems there's no one around."
            "I get up and leave the apartment."
            "Slowly, I recognize the place."
            "I stagger home, my head still heavy from the night before."
    
            jump livingroom

        



    label estelleconv1:
        scene livingroomarrow
        scene livingroomarrowflou with dissolve
        show estherparty with dissolve
        if estelle_firstconv_done == True:
            est "Hey, are you here?"
            name "Yeah, Zoey and Bruno invited me."
            est "Cool..."
        else:
            est "Hey, do I know you?"
            name "We must have crossed paths at college."
            est "Oh, okay. Well, I don't know you very well."
            est "We probably wouldn't have much to talk about, I think."
            est "No offense, I like people who have interesting story to tell."
            name "wow that's so rude"
            jump livingroom
        est "soo..."
        name "sooo..."
        name "Do you know a lot of people here?"
        est "Yeah, most of them."
        name "Oh, okay."
        est "This party is kind of lame, isn't it?"
        name "Yeah, totally... so lame."
        name "It's so lame that I came to talk to you."
        name "Can you imagine?"
        est "Do you think you're funny?"
        name "I was just trying to make conversation."
        est "Well, you don't have to try so hard."
        jump livingroom

        if estelle_spankconv_done == True:
            est "Hey, so are you looking for something in particular here?"
            name "What do you mean?"
            show estherhorny2 with dissolve
            hide estherparty with dissolve
            est "Well, you know..."
            est "Someone to put you in your place."
            name "What?"
            est "Well, you know, like Camille."
            est "Is that what you're looking for?"
            name "I don't see what you're talking about."
            est "Yeah, play innocent."
            est "I know your secret."
        hide estherparty
        
        jump livingroom