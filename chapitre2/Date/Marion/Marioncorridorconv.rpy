label Marionconv:
    if day % 2 == 0 and Jenny_end_done == False and zoey_uni_conv_done == False:
        scene zoeycorridorblur with dissolve
    else:
        scene corridorrealistblur with dissolve
        if marion_conv_count == 0:
            label marion_articlerequested:
                
                show marionserious1 with dissolve

                "I'm walking through the hallway, when I see Mrs. Gillberg approaching."

                mar "[name] Smith?"

                "I freeze for a second before turning around."

                name "Oh! Good afternoon, Mrs. Gillberg."

                mar "Perfect, I was just thinking I needed to email you."
                mar "Since you came to see me about your thesis topic, I want us to set up something concrete."

                show marionserious2 with dissolve
                hide marionserious1 with dissolve

                mar "Before we go any further with your dissertation, I need to know if you can write."
                mar "Not just essays for class, but something that could eventually be published."

                name "Published...?"
                name "You mean, like, a real article?"

                mar "Exactly."
                mar "I want you to write a short article based on your thesis idea."
                mar "Something clear, well-argued."
                mar "Think about how you present your research question, your sources, and one or two case studies."

                name "O-okay. How long should it be?"

                mar "Nothing enormous. Around ten pages."
                mar "The point is to see if you can communicate your research, not to bury yourself in footnotes."
                mar "If it’s good, we might even think about polishing it for a journal later."

                "This suddenly feels very real."

                name "And when do you need it?"

                mar "Soon."
                mar "Let’s say in a few weeks. I’ll send you an email with the exact deadline and a few guidelines."
                
                name "Alright. I’ll do my best."
                show marionsmileandwalkingaway with dissolve
                hide marionserious2 with dissolve
                mar "Good. I’m counting on you."
                mar "I have to run to another meeting, but don’t let this drag on, alright?"

                name "Yes, Mrs. Gillberg. Thank you."

                hide marionsmileandwalkingaway with dissolve
                window hide
                pause

                "I swallow hard. An article."
                "I really need to start working on this."

                $ marion_conv_count += 1
                $ corridorconv_done = True  
            jump gardenuni_start2



        elif marion_conv_count == 1:
            
            show marionneutral2 with dissolve
                
            mar "Hello!"
            name "Good afternoon!"
            mar "How's your work going?"
            name "Yes, it's going well!"
            mar "Don't forget that article we talked about."
            mar "If you're having trouble focusing, you can always go to the library."
            mar "It's much better for concentration!"
            mar "I'm actually going there myself to work on something, you can come with me if you like."
            menu:
                "Sure, that sounds good.":
                    
                    show marionsmileandwalkingaway with dissolve
                    hide marionneutral2 with dissolve
                    mar "Great! Let's go then."
                    mar "That way I can show you some interesting resources."
                    name "Thanks, Mrs. Gillberg."
                    window hide
                    pause
                    "We head to the library together."
                    $ marion_conv_count += 1
                    $ corridorconv_done = True

                    jump Marion_librarydate

                "No, thank you. I need to do something else right now.":

                    mar "Of course, I understand."
            show marionneutral with dissolve
            hide marionneutral2 with dissolve
            mar "I can't get any work done in my office."
            mar "It's just too quiet, I need the background noise."
            name "Thanks, I'll keep that in mind."
                
            mar "Alright, hang in there!"
            hide marionneutral with dissolve
            window hide
            pause
            "I seriously need to buckle down and work on this article."

            $ marion_conv_count += 1
            $ corridorconv_done = True  
            jump gardenuni_start2



        elif marion_conv_count == 2:
            
            show marionworry2 with dissolve
                
            mar "Hey, how's it going?"
            name "Good, I'm just passing by."
            mar "I see. If you need help with the article, don't hesitate to let me know."
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



        elif marion_conv_count == 3:
        
            show marionwaling with dissolve

            mar "Hey, I see you hanging around the hallways all the time."
            mar "Hope you're actually getting some work done on that article…"
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
            mar "Anyway, I gotta run... meeting with a student."
            hide marionwaling3 with dissolve
                
            window hide
            pause
            "She continues on her way with a hurried step."
            $ marion_conv_count += 1
            $ corridorconv_done = True  
            jump gardenuni_start2


        else:
            
            show marionworry2 with dissolve
            "Mrs. Gillberg passes by, buried in a stack of folders."
            "She gives me a brief nod before disappearing around the corner."
            hide marionworry2 with dissolve
            
            jump gardenuni_start2


    label othercorridor_conv:
        if renpy.random.randint(1, 4) >= 3:
            $ corridorconv_done = True
            jump emma_corridor_sequence
        else:
        
            
            if day % 2 == 0 and Jenny_end_done == False and zoey_uni_conv_done == False:           
                show screen corridor_zoey
                call screen corridor_zoey
            show screen corridor_standard
            call screen corridor_standard


