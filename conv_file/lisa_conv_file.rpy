
label lisa_conv_direction:
    if lisa_conv_done == True:
        jump lisa_not_available
    elif lisa_conv_done == False:
        jump lisa
label lisa_not_available:
    if elise_cafe == True and elise_cafe_conv_done == False:
            scene cafeelisefinal
    elif sarah_cafe == True and sarahcafe_conv2_done == False :
            scene cafesarah2
    elif sarah_elise_cafe == True and sarah_elise_cafedate_done == False:
        scene elisesarahcafe
    else: 
        scene cafe2
    "I already talk to her today"
    jump cafedirection

label lisa: 
    if elise_cafe == True and elise_cafe_conv_done == False:
        scene cafeelisefinal
    elif sarah_cafe == True and sarahcafe_conv2_done == False:
        scene cafesarah2
    elif sarah_elise_cafe == True and sarah_elise_cafedate_done == False:
        scene elisesarahcafe
    else: 
        scene cafe2

    if lisa_count == 0:
        jump lisa1
    elif lisa_count == 1:
        jump lisa2
    elif lisa_count == 2:
        jump lisa3
    elif lisa_count == 3:
        jump lisa4
    elif lisa_count >= 4:
        jump lisa5

label lisa1:
    show lisaneutral10 with dissolve
    lis "Hey, do you need something?"
    name "No, just looking."
    lis "Alright."
    hide lisaneutral10 with dissolve
    $ lisa_conv_done = True
    $ lisa_count += 1
    jump cafedirection

label lisa2:
    show lisaneutral10 with dissolve
    lis "Hey, I see you looking at me."
    name "No, it's just..."
    lis "Yes?"
    name "Nothing."
    lis "You're cute."
    lis "You're really good at flirting."
    $ lisa_conv_done = True
    hide lisaneutral10 with dissolve
    $ lisa_count += 1
    jump cafedirection

label lisa3:
    show lisatalking01 with dissolve
    lis "You should work out more."
    name "What?"
    lis "I'm just saying, you should work out more."
    lis "Your body would be more graceful."
    name "Ok?"
    lis "It's important to take care of yourself."
    name "Yeah, I just don't have the time."
    lis "You're just lazy, that's all."
    lis "I was a fitness coach. I can tell you that people who take care of themselves are happier."
    lis "It's a fact."
    name "I don't doubt it."
    lis "Not to mention the success with women you could have."
    name "Yeah, ok. I mean, not everyone is made for that."
    
    show lisatalking00 with dissolve
    hide lisatalking01 with dissolve
    lis "Oh, come on, you're just making excuses."
    lis "Everyone does that now: making excuses."
    name "Ok, I'll think about it."
    lis "You should. It's important."
    "I don't know what to say to that."
    hide lisaneutral10 with dissolve
    $ lisa_conv_done = True
    $ lisa_count += 1
    jump cafedirection

label lisa4:
    show lisaneutral10 with dissolve
    lis "Hey, you look good today."
    name "Thanks, you too."
    lis "I know."
    name "..."
    hide lisaneutral10 with dissolve
    $ lisa_conv_done = True
    $ lisa_count += 1
    jump cafedirection

label lisa5:
    show lisaneutral10 with dissolve
    name "Hey, what's up?"
    lis "Oh, hi. Have you been working out?"
    name "Huh? Of course, I have..."
    lis "Mmmh."
    lis "Don't rest on your laurels."
    lis "You're not there yet."
    name "..."
    name "I'm not sure what you mean."
    lis "You're not in shape."
    lis "How do you expect people to notice you if you don't put in the effort?"
    name "I'm trying to start slowly."
    name "You know, I don't want to hurt myself."
    lis "Yes, you're right. You have to be careful."
    lis "But don't hesitate to gradually increase the effort."
    lis "If it hurts, it means it's working."
    name "I'll keep that in mind."
    hide lisaneutral10 with dissolve
    $ lisa_conv_done = True
    $ lisa_count += 1
    jump cafedirection
 