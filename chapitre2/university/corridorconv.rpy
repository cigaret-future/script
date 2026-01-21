label corridor_randomconv:
    
    if renpy.random.randint(1, 2) == 1:
        jump Marionconv
    else:
        jump othercorridor_conv
    
    label Marionconv:
        if marion_conv_count == 0:
            scene corridorrealistblur with dissolve
            show marionneutral2 with dissolve
            
            mar "Hello!"
            name "Good afternoon!"
            mar "How's your work going?"
            name "Yes, it's going well!"
            mar "If you're having trouble focusing, you can always go to the library."
            mar "It's much better for concentration!"
            mar "I'm telling you this because I'm actually going there myself to read something."
            show marionneutral with dissolve
            hide marionneutral2 with dissolve
            mar "I can't get any work done in my office."
            mar "It's too quiet ahah."
            name "Thanks, I'll keep that in mind."
            
            mar "Alright, hang in there!"
            hide marionneutral with dissolve
            window hide
            pause
            "I seriously need to buckle down and work on this."

            $ marion_conv_count += 1
            $ corridorconv_done = True  
            jump gardenuni_start2
        elif marion_conv_count == 1:
            scene corridorrealistblur with dissolve
            show marionworry2 with dissolve
            
            mar "Hey, how's it going?"
            name "Good, I'm just passing by."
            mar "I see. If you need help, don't hesitate to let me know."
            mar "If I have time, we could talk."
            show marionworry3 with dissolve
            hide marionworry2 with dissolve
            mar "Though right now, I don't have any to spare."
            name "Everything's fine."
            show marionworry2 with dissolve
            hide marionworry3 with dissolve
            mar "That's good to hear."
            mar "I have to go, these meetings are never-ending..."
            hide marionworry2 with dissolve
            window hide
            "She seems a bit stressed."
            pause
            $ marion_conv_count += 1
            $ corridorconv_done = True  
            jump gardenuni_start2
        elif marion_conv_count == 2:
            scene corridorrealistblur with dissolve
            show marionwaling with dissolve

            mar "Hey, I see you hanging around the hallways all the time."
            mar "Hope you're actually getting some work done.."
            name "Yeah, yeah, I'm working."
            name "Just need to catch my breath."
            name "And..."
            name "Find some inspiration."
            mar "Ah, I get that."
            show marionwaling2 with dissolve
            hide marionwaling with dissolve
            mar "Inspiration really matters."
            mar "Especially in our line of work."
            mar "We're not machines, after all."
            show marionwaling3 with dissolve
            hide marionwaling2 with dissolve
            mar "Anyway, I gotta run.. meeting with a student."
            hide marionwaling3 with dissolve
            
            window hide
            pause
            "She continues on her way with a hurried step."
            $ corridorconv_done = True  
            jump gardenuni_start2
        else:
            scene corridorrealist
            show marioncrossingcorridor with dissolve
            
    label othercorridor_conv:
            "but nothing comes up.."
            "Maybe later."
            jump gardenuni_start2