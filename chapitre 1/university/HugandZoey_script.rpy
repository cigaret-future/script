define hug = Character('Hugo', color="#7b9ce2") 
define zoey = Character('Zoey', color="#a9f080") 
label HugandZoeyStart: 
    scene corridor10
    
    if linda_1st_conv_done == True:
        "I wander in the corridor until I arrive in front of the administration, on the 1st floor."
        show hugopose11 at left:
            xalign 0.3
        
        hug "So, did you find what you were looking for?"
        
        name "Yeah, Linda suggested I go see Mrs. Gillsberg."

        hug "She knows her stuff."

        name "Definitely, she even offered to help me with my thesis topic."

        hug "Seriously?"

        name "I think so."
        
        show zoeypose04 at right:
            xalign 0.7
            
        zoey "That doesn't sound like her."

        hug "Yeah, she'll probably charge you for it but hasn't told you yet."

        name "You think?"

        hide hugopose11
        show hugopose08 at left:
            xalign 0.3
        hug "That's what she told me when I asked for her class notes."

        name "Man, I hope she doesn't, I'm broke."

        name "She seemed nice though."

        hug "Yeah, she is... how to say it..."
        hide zoeypose04
        show zoeypose07 at right:
            xalign 0.7
            
        zoey "She's quite a character."

        hug "That's putting it mildly."

        name "Well, I hope she can help me. I'm still not sure about my topic."
        hide hugopose11
        show hugopose10 at left:
            xalign 0.3
        hug "Oh man, I need to get on that too."

        hide zoeypose04
        show zoeypose03 at right: 
            xalign 0.7
        zoey "Come on, Hugo... you still haven't found one yet." 

        hide hugopose10
        show hugopose09 at left:
            xalign 0.3

        hug "I am working on it, okay! I have too many ideas."

        zoey "Yeah, right... you're just lazy."
        
        zoey "That's what you get for spending your summer at festivals instead of working."

        name "I thought you needed a topic to start a master's program."

        zoey "Hugo has a way of getting on the professors' good side, right?"

        hide hugopose09
        show hugopose08 at left:
            xalign 0.3

        hug "They believe in my talent."

        zoey "Sure, your talent for getting wasted."

        hug "Hey, I'm a serious student too! I just like to have fun."

        hide zoeypose03
        show zoeypose01 at right:
            xalign 0.7
        hug "Talking about fun, give me your phone number. If there's a party, I'll let you know."

        name "Oh, ok, thanks. That's nice of you."

        hug "No problem."

        hide zoeypose01
        show zoeypose11 at right:
            xalign 0.7
        "Zoey winks at me."

        name "Okay. Let's stay in touch."

        name "Oh, by the way, do you know where Mrs. Gillsberg's office is?"
        hug "Yeah, it's on the 6th floor. It's an office with a large window."
        $ zoey_first_conv_done = True
        name "Thanks, see you."

        jump marion_1st_meet
    elif linda_1st_conv_done == False: 
        "I wander in the corridor, looking for a brunette with a black sweater."
        "Hugo is there with a friend of his."
        "Maybe I should ask him where I can find Linda."
        show hugopose07 at left:
            xalign 0.3
        name "Hey, have you seen Linda? I couldn't find her in the amphitheater."

        hug "No, I haven't seen her. Maybe she's in the library. She's always there."

        name "Thanks, I'll go check there."
        hide hugopose07
        jump gardenuni_start