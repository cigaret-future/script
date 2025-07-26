label zoeydate:

    if zoeydate_count == 0:
        jump zoeydate1
    
    elif zoey_date_done == True:
        jump zoeyfinal
    elif zoeydate_count == 1:
        jump zoeydate2
    elif zoeydate_count == 2:
        jump zoeydate3
    
    



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
        show zoeysurprise with dissolve
        hide zoeysmile with dissolve
        zoey "On the contrary, I feel like it gives me perspective."
        name "That's well put."
        zoey "No really, I feel like I understand people from up there."
        zoey "It's like I can feel what they want."
        name "Like a god?"
        show zoeysmile with dissolve
        hide zoeysurprise with dissolve
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
        show zoeydesire with dissolve
        hide zoeysmile with dissolve
        zoey "He's a pretty ambiguous god."
        zoey "He kind of transgresses gender norms."
        name "I didn't know that."
        zoey "Yes you do, ahah"
        "I blush a little."

        name "Anyway... I should get going."
        name "I am late for.. my class of ... mythology."
        show zoeysmilecorridor2 with dissolve
        hide zoeydesire with dissolve
        zoey "Sure, I should probably get going too."
        zoey "Oh by the way what's your name?"
        name "I am [name] and you?"
        zoey "Zoey."
        zoey "I have your number, but I didn't know what name to put."
        name "You have my number?"
        zoey "Yeah Hugo gave it to me."
        if gender == "male":
            zoey "I just wrote 'cut new guy'"
        elif gender == "fem":
            zoey "I just wrote 'cute new girl'"
        name "ahah ok.. now you have the right name"
        zoey "Yes I will change it"
        name "See you later"
        zoey "Bye [name]."
        hide zoeysmilecorridor2 with dissolve
        "She gives me a playful wave and walks off."
        "I feel a bit invaded by the fact that she knows my number."
        "But she doesn't seems like a bad person."
        $  zoeydate_count += 1
        jump gardenuni_start2


    label zoeydate2:
        scene zoeycorridorblur
        show zoeysmile with dissolve
        
        zoey "Hello, [name]." 
        name "Hi Zoey."
        zoey "How are you doing?" 
        name "Pretty good, just finished some work I needed to do."
        zoey "That's good. Now you can take some time to relax."
        zoey "It's important to rest sometimes."
        name "I know, but..."
        name "I'm not great at managing my time, honestly."
        name "When I try to focus, other thoughts always seem to... distract me." 
        name "It makes everything feel scattered."
        zoey "I understand that completely." 
        name "Sometimes I just wish I had more time for myself."
        show zoeysmilecorridor2 with dissolve
        hide zoeysmile with dissolve
        zoey "You're a free spirit, aren't you?" 
        zoey "I feel the same way, actually."
        zoey "Even with all the freedom I have..."
        zoey "...I still find myself wanting more."
        zoey "But I've been thinking, sometimes commitment is important too."
        name "What do you mean by that?"
        zoey "Well... choosing someone, or something, and really committing to it."
        zoey "Relationships, for example." 
        name "Oh, I see."
        zoey "Don't get me wrong, I value my freedom..." 
        zoey "But I do wonder what it would be like to have someone special."
        zoey "Someone to share moments with." 
        name "That makes sense."
        zoey "Wht I'm trying to say is..." 
        zoey "Maybe true freedom doesn't require being alone."
        name "Yeah but you're not necessarily alone."
        name "You can still grow, change..."
        zoey "Ah, I see, you're that type."
        zoey "The restless kind who's always moving."
        zoey "But someday, you'll meet someone who changes your perspective." 
        name "Yeah... I can't really imagine that."
        zoey "Heh, they'll just need to know how to... press the right buttons." 
        zoey "Then you might surprise yourself." 
        name "Maybe..."
        name "But I don't think that will happen anytime soon."
        name "I really enjoy being independent right now."
        name "Maybe when I'm older."
        zoey "It might happen sooner than you think."
        zoey "Who knows?"
        name "Yeah, who knows?"
        name "well it was cool talking to you.. I'll try to enjoy my free time"
        name "See you Zoey!"
        zoey "alright see you later [name]."
        $ zoeydate_count += 1
        hide zoeysmilecorridor2 with dissolve
        "She gives me a playful wave and walks off."

        jump gardenuni_start2

    label zoeydate3:

        scene zoeycorridorblur
        show zoeysmile with dissolve

        zoey "Hey [name]!"
        name "Hi Zoey!"
        zoey "So about the party..."
        zoey "It's tonight?"
        zoey "Are you up for it?"
        name "Yeah why not.."
        zoey "Yaaay!"
        zoey "Great!"
        show zoeydesire with dissolve
        hide zoeysmile with dissolve
        zoey "By the way.."
        zoey "You are really cute in that outfit."
        zoey "It really shows off your figure"
        name "Thanks.."
        show zoeykiss with dissolve
        hide zoeydesire with dissolve
        zoey "see you tonight!"
        hide zoeykiss with dissolve
        "She gives me a playful wave and walks off."
        $ party_started = True
        jump gardenuni_start2
    label zoeyfinal:
        scene zoeycorridorblur
        show zoeysmile with dissolve

        zoey "Oh, look who's back..."
        name "Hi Zoey."
        show zoeysmilecorridor2 with dissolve
        hide zoeysmile with dissolve
        zoey "You seem... different today."
        name "Different how?"
        zoey "I don't know... you look like you're searching for something."

        name "Last night was..."
        zoey "Intense?"
        name "Yeah, something like that."
        show zoeydesire with dissolve
        hide zoeysmilecorridor2 with dissolve
        zoey "You know, I can see it in your eyes."
        zoey "That restless spirit you talked about before..."
        zoey "It's still there, but it's... focused now."
        name "Focused on what?"
        zoey "You tell me."
        name "I... I can't stop thinking about you."
        name "About last night."
        zoey "Mmm, is that so?"
        show zoeysurprise with dissolve
        hide zoeydesire with dissolve
        zoey "Remember when you said you valued your independence?"
        zoey "That you couldn't imagine giving it up for someone?"
        name "I remember."
        zoey "And now?"
        name "I'm not so sure."
        name "I think I need you, Zoey."
        zoey "Need me? That's a strong word."
        name "I know, but... I can't help it."
        show zoeysmile with dissolve
        hide zoeykiss with dissolve
        zoey "Well i am not gonna make you wait"
        zoey "Come on."
        name "Where are we going?"
        zoey "My place. We need to talk about this properly."
        scene black with fade
        "She takes my hand and leads me through the campus."
        "I follow without hesitation, even though part of me knows this changes everything."
        "We walk through the street to her place."
        "She opens the door and make me enter."
        zoey "Welcome to my humble abode."
        scene zoeyopendoor with dissolve
        name "I came here thinking I'd just say hi, but..."
        zoey "You know what this means, don't you?"
        name "What?"
        zoey "You're mine now, [name]."
        name "Is that what you wanted all along?"
        zoey "Maybe..."
        window hide
        $ renpy.pause(1, hard=True)

        scene zoeyclosedoor with dissolve


        "As she closes the door behind her, she approaches and start undressing."
        "I realize there's no going back."
        "Whatever this relationship becomes, I'm completely under her spell."
        "And honestly... I don't mind."
        scene black with fade
        $ renpy.pause(1, hard=True)
        scene endscreenzoey2 with fade
        $ renpy.pause(1, hard=True)
        scene endscreenzoey with dissolve
        $ renpy.pause(4, hard=True)
        
        