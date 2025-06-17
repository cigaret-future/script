label sarahdate1:
    $ day_not_over = True
    scene cafesarah
    if sarahcafe_conv1_done == True:
        "I should let her read her book, we'll see each other later."
        show screen cafescreen_sarah
        call screen cafescreen_sarah
    
    else: 
        "I see Sarah sitting at a table. I should go say hello to her."
    
    show sarahnobackpack with dissolve
    sar "Hey you! Did you think I wouldn't see you?"

    name "Hey Sarah. I don't see you here often."

    sar "Yeah... unlike many people, I have to work on-site. I have a day off today."

    name "What exactly do you do?"

    sar "I'm the manager of a small team at a communications firm. It's not thrilling, but it pays well."

    name "I see."
    
    show sarahinvite2 with dissolve
    hide sarahnobackpack with dissolve 
    
    sar "Hey, do you want to sit and have a coffee with me?"

    name "Sure! I've already had two, but I can make room for more."

    sar "I'm buying, come on."

    name "Oh no, don't worry."

    show sarahinvite4 with dissolve 
    hide sarahinvite2 with dissolve
    
    sar "No, I insist. I know what it's like being a student. You need money to eat proper meals."

    name "Well, if you insist."

    sar "It makes me happy, go ahead and order something."

    name "Okay, I'll be right back."

    hide sarahinvite4 with dissolve
    "I go order a large latte and sit down across from Sarah."

    name "So, it's your day off, right?"
    show sarahtired with dissolve
    sar "Yeah, finally. I've been working non-stop for three weeks. I needed a break."
    
    name "Is your job tough?"

    sar "Yes... I feel like the mother of four kids. I have to constantly keep an eye on them."

    name "Oh right, you're a manager. I always thought managers were cold, tyrannical, and psychopathic, but you don't seem to fit that description."
    show sarahneutral with dissolve
    hide sarahtired with dissolve
    
    sar "Haha, thanks. I guess you'd have to ask my colleagues."

    name "I'm sure they appreciate you. You seem like a responsible leader."
    show sarahjoking with dissolve
    hide sarahneutral with dissolve
    
    sar "Exactly. I have power, but I use it wisely. I'm an enlightened dictator."

    name "Haha, wow. The mask comes off."

    sar "I am the light in the darkness."

    sar "No, but seriously, it's a real challenge to lead people without being a jerk."

    name "I bet. It almost seems impossible."
    show sarahneutral with dissolve
    hide sarahjoking with dissolve
    
    sar "Well, yeah, sometimes I think I am a bit of a jerk. But it's often the circumstances. The people above me put pressure on me, and it trickles down."
    if sarah_pissedconv_done == True:
        name "Yeah, I experienced that."
        show sarahcrossed with dissolve
        hide sarahneutral with dissolve
        
        sar "Oh my god, I was so pissed that night. I was ready to come down to your place and give you a piece of my mind."

        name "Good thing I turned the volume down."

        sar "Yes, otherwise I would have been on your back all night."

        name "Jeez, what a pain in the ass."
        show sarahlaugh with dissolve
        hide sarahcrossed with dissolve
        
        sar "Haha, you can't imagine."

        name "..."

        sar "You are funny."
        hide sarahlaugh with dissolve
    elif sarah_pissed == False:
        
        name "I guess yeah"
    show sarahneutral2 with dissolve 
    hide sarahneutral with dissolve
    
    name ""
    name "There aren't many folks in our building, it seems."

    sar "Yeah, it's a small building."

    sar "Have you met Sacha?"

    if sacha_count >= 1: 
        name "Yes, he's the only one I've met besides you."
    else: 
        name "No, not yet."

    sar "He's a good guy. But he might ask to borrow stuff from you."

    name "Oh really?"

    sar "Yes, it seems like he doesn't have anything at his place."

    sar "Actually, that's how we became friends. One evening he came to my door. It must have been around 10 PM. He asked if I had a blender."

    name "A blender?"

    sar "Yes, he wanted to make soup. At 10 PM..."

    name "And you gave it to him?"
    define fastdissolve = Dissolve(0.5)
    hide sarahneutral2 
    show sarahcrossed2 
    
    sar "Yep... never saw it again."

    name "He sounds funny. A guy making soups inspires trust."

    sar "That's true."

    sar "Anyway, I'm going to finish this coffee and try to do something else with my day than just drink coffee here."

    name "What's wrong with that?"

    name "That's what I would do if I had time."

    sar "Yeah, I know it's tempting. But I promised myself I would do something interesting on my day off."

    name "Like what?"

    sar "I don't know yet, but I'm going to think about it very seriously."

    name "I see, well have a good reflection then."
    $ sarahcafe_conv1_done = True
    sar "See you around, neighbor."
    hide sarahcrossed2 with dissolve
    $ sarah_conv_done = True
    $ sarah_relation_status_text = "I should go to sleep, I'll see Sarah later."
    $ sarah_pissed = False

    show screen cafescreen_sarah
    call screen cafescreen_sarah

label sarahnotdate:
    scene cafesarah
    show sarahnobackpack
    sar "Hey, didn't I see you somewhere?"

    name "I'm not sure."

    sar "Well, enjoy your day."

    name "You too."
    "Did I already meet her?"
    $ sarah_relation_exist = True
    $ sarah_relation_status_text = "It seems I could meet new people in the stairs of my building."
    show screen cafescreen_sarah
    call screen cafescreen_sarah
