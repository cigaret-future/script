label estelleconv :
    label estelleconv_direction:

       
        
        if drink_count >= 5 and estellebourreconv_done == False:
            jump estelleconvbourre1
        elif drink_count >= 5 and estellebourreconv2_done == True:
            jump estelleconvbourre3
        elif drink_count >= 5 and estellebourreconv_done == True and estellepuke_done == False:
            jump estelleconvbourre2
        elif drink_count >= 5:
            jump estelleconvourre2
        
        

        
        elif estellepartyconv_count == 0:
            jump estelleconv1
        elif estellepartyconv_count == 1:
            jump estelleconv2
        else:
            scene livingroomarrow
            scene livingroomarrowflou with dissolve
            show estherparty with dissolve
            est "You seem like you want to get in some trouble"
            name "why do you say that?"
            est "I see you going back and forth throughout the party."
            est "You are looking for something i can tell."
            name "Maybe i am."
            jump livingroom

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
            

            $ estellebourreconv2_done = True
            $ estellebourreconv_done = True
            $ estellepartyconv_count += 1
            hide esther12 with dissolve
            jump livingroom
        
        label estelleconvbourre3:
            scene livingroomarrow
            scene livingroomarrowflou with dissolve  
            show estherparty with dissolve 
            est "Wow. You’re really pushing your limits tonight, huh?"  
            name "Nah, ‘m good. I can still… stand. Probably."  
            est "Mhmm You know, at this rate, you’ll either pass out on the floor, or worse, make a mess someone has to clean up."  
            "She leans in."  
            est "How about we find you something to sober up?"
            name "Like what? Water?"
            est "Lucky for you, I’ve got a much better idea."  

            scene black with dissolve
            window hide
            pause
           
            "Before you can protest, Estelle takes your arm and guides you toward the kitchen, her grip deceptively gentle but leaving no room for escape."  
            scene estelledrinkup  
            "She grabs a bottle of milk from the fridge, shaking it playfully."  
            est "Trust me, you’ll thank me later. A little milk, and poof, no more nausea. Easy, right?"  
            name "Wait, How milk is gonna help me. And I don’t wanna puke!"  

            est "You’re way past 'wanting' anything. This is 'needing'."  

            

            est "Come on. One big gulp, and it’ll all be over. Or… Do I have to hold your nose and pour it down your throat like a stubborn child?"  
            name "Ugh… fine. But this is your fault if I die."  
            est "Oh, don’t be dramatic"
            scene estelledrinkup1 with dissolve
            window hide
            pause            
            scene estelledrinkup4 with dissolve
            "She watches, delighted, as you chug."
            est "See? Not so bad, right?"
           
            name "Mmph... "
            scene estelledrinkup5 with dissolve
            est "Keep going, you're doing great!"
            window hide
            pause

            scene estelledrinkup2 with dissolve
            
            window hide
            pause
            scene estelledrinkup1 with dissolve
            window hide
            pause
            scene estelledrinkup8 with dissolve
            window hide
            pause
            scene estelledrinkup1 with dissolve
            window hide
            pause
            scene estelledrinkup3 with dissolve
            "I really don't feel good..."
            window hide
            pause

            scene estelledrinkup4 with dissolve
            est "Just a bit more, trust me!"
            "The milk feels heavy in your stomach."
            window hide
            pause

            scene estelledrinkup5 with dissolve
            "Your stomach starts to feel uncomfortably full."
            "Your vision starts to swim."
            window hide
            pause

            scene estelledrinkup2 with dissolve
            "I think I'm gonna be sick..."
            window hide
            pause
            scene estelledrinkup3 with dissolve
            
            window hide
            pause
            scene black with dissolve
            "Your legs feel unsteady. Estelle notices and quickly takes your arm."
            est "Let's get you to the bathroom, quickly."
            "Her tone has a hint of amusement in it."
            scene estellefaceview2 with dissolve
            est "are you okay?"
            name "I don't feel so good..."
            est "Yeah, you look pale."
            est "you'll feel better after.."
            "She hold my head down on the bowl."

            scene estelletoilet1 with dissolve
            
            window hide
            pause

            scene estelletoilet2 with dissolve
            "Estelle helps keep me steady as I lean over, but there's something playful in the way she holds me."
            est "Just let it out. You'll feel better after."
            "She seems to be enjoying this a little too much."
            scene estellefaceview3 with dissolve
            window hide
            pause
            est "There you go, just let it all out."
            scene estelletoilet2 with dissolve
            "You feel the contents of your stomach emptying into the toilet, and Estelle holds your hair back, her touch surprisingly gentle."
            scene estelletoilet1 with dissolve
            est "See? I told you the milk was a good idea"
            scene estelletoilet2 with dissolve
            window hide
            pause
            scene estelletoilet1 with dissolve
            window hide
            pause
            scene estelletoilet2 with dissolve
            window hide
            pause
            scene estelletoilet1 with dissolve
            window hide
            pause
            scene estelletoilet2 with dissolve
            window hide
            pause
            scene estelletoilet1 with dissolve
            window hide
            pause
            scene estelletoilet2 with dissolve
            window hide
            pause
            scene estelletoilet1 with dissolve
            window hide
            pause
            scene black with dissolve
            "After a while, you feel that your stomach is empty and you can get up."
            
            scene estellefaceview5 with dissolve
            name "..."
            name "I think... I think I'm done."
            scene estellefaceview3 with dissolve
            window hide
            pause
            est "Just stay like that for a bit, just in case.."
            "You feel a bit better, but your head is still spinning."
            est "I know it's not the best position.."
            est "But it's for the best."
            est "Besides.."
            est "You are pretty cute like that."
            name "what??.."
            scene estelleupview with dissolve
            est "Yeah you know.."
            est "All messy..."
            est "And vulnerable."
            est "It's kinda cute."
            name "I don't feel cute at all right now."
            est "You are.."
            est "You are just a bit drunk, that's all."
            scene black with dissolve
           
            "She helps you stand up slowly."
           
            est "You should drink some water, it will help you feel better."
            "You nod, appreciating her concern."
            $ estellepartyconv_count += 1
            $ drink_count = 0
            $ estellepuke_done = True
            jump upstairs
           
           

         
            jump livingroom
        label estellepukedoneconv:
            scene estellefaceview5 with dissolve
            est "Hey, you look better now."
            name "Yeah, I feel a bit better."
            name "Thanks for helping me."
            est "Anytime!"
            $ estellepartyconv_count += 1
            jump livingroom
        



    label estelleconv1:
        scene livingroomarrow
        scene livingroomarrowflou with dissolve
        show estherparty with dissolve
        if estelle_firstconv_done == True:
            est "Hey, you're here."
            name "Yeah, Zoey and Bruno invited me."
            est "Cool..."
        else:
            if estellepuke_done == True:
                est "You look better now."
                name "Yeah, I feel a bit better."
                name "Thanks for helping me."
                est "Anytime!"
                jump livingroom
            est "Hey, do I know you?"
            name "We must have crossed paths at college."
            est "Oh, okay. Well, I don't know you very well."
            est "We probably wouldn't have much to talk about, I think."
            est "No offense, I like people who have interesting story to tell."
            name "wow that's so rude"
            jump livingroom
        if estellepuke_done == True:
                est "You look better now."
                name "Yeah, I feel a bit better."
                name "Thanks for helping me."
                est "Anytime!"
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