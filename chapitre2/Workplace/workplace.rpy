label workplace:
    if workday_done == False:
        if work_count == 0:
            jump workplace1
        elif work_count == 1:
            jump workplace2
        elif work_count == 2:
            jump workplace3
        elif work_count == 3:
            jump workplace4
        elif work_count >= 4:
            jump workplace5
    else: 
        "You already worked today, you should go home."
        jump map3

    label workplace1:
        scene upview
        $ work_count += 1
        "I arrive at a coffee shop, people are lining up to order, and baristas are busy behind the counter."
        "It's a slightly different atmosphere from the coffee shop near my house, but it doesn't seem too bad."
        "I try to spot the boss, but I don't see her."
        "I should ask at the counter if she's here."
        "I approach the counter."
        scene upviewblur with dissolve
        show jenny with dissolve
       
        jen "Hey there."
        name "Hi, I'm looking for the boss."
        jen "That's me, I'm Jenny."
        name "Oh, okay, nice to meet you. I am [name]."
      
        show jenny3 with dissolve
        hide jenny with dissolve
        
        jen "Nah, I'm just kidding. Why do you want to see the boss?"
        name "She offered me a job here."
        jen "Ah, okay, I'll let her know you're here."
        "Jenny walks away and heads towards the back of the coffee shop."
        "I wait for a few minutes, and she comes back."
        jen "She's coming. You can wait on the side."
        name "Thanks."
        hide jenny3 with dissolve
        scene upview with dissolve
        "I stand near the counter on the side."
        "It's not exactly what I imagined, but it should be fine."
        "After a few minutes, the boss comes out of a room in the back and approaches me, staring at me."
        show bossview
        elod "Hey, are you the new recruit?"
        name "Hello, I'm ready to work. When do I start?"
        elod "Perfect, you can start right now if you want."
        elod "That way, you can see if it suits you."
        name "Don't I need to sign a contract first?"
        elod "Yes, but this will allow you to get to know your colleagues."
        name "Well... okay, I don't mind."
        elod "Great, I'll get you an outfit."
        elod "You'll see, it's very dynamic here."
        elod "I'll be right back."
        "She walks away and comes back with a t-shirt and pants."
        elod "Here, put this on."
        name "Here?"
        elod "No, come to the storage room."
        scene changing2
        "She takes me to a room at the back of the coffee shop."
        "She shows me a room with boxes and clothes."
        "I put on the uniform and leave the room."
        elod "Great, it suits you very well."
        name "Cool."
        scene upviewblur with dissolve
        "I head to the counter and start watching Jenny work."
        
        "After a few hours, I start to get the hang of it."
        show jenny with dissolve
        jen "Do you want me to show you how to make a coffee?"
        name "Okay..."
        jen "Look, you just put the coffee here,"
        jen "then press here, and you're good to go."
        "The day goes by slowly."
        jen "Okay, my shift is over."
        jen "I think we can leave now."
        hide jenny with dissolve
        "I leave the coffee shop with Jenny, and we part ways."
        $ money += 200
        $ work_status_text = "I can go work at the coffeeshop if I need money."
        $ workday_done = True
        show text "+200$" at Move((0.5, 0.6), (0.5, 0.5), 10.0)
        hide text with dissolve
        jump map3

    label workplace2:
        scene upview
        $ work_count += 1
        $ workday_done = True
        "Second day at the coffee shop."
        "The place feels more familiar now."
        show jenny with dissolve
        jen "Back again, [name]."
        name "Yeah, ready for today."
        show jenny3 with dissolve 
        hide jenny with dissolve
        jen "Cool. Today’s the fun part: the latte machine."
        jen "It’s a bit more of a hassle than just pressing a button."

        scene upviewblur with dissolve
        hide jenny3 with dissolve
        "Jenny takes me over to a tall, stainless steel machine with a glowing touchscreen. It looks expensive — and slightly intimidating."
        "She pokes a few buttons and the machine comes to life with a low hum."

        show jennyoccupied with dissolve
        jen "This thing? Fully automatic, costs more than my car."
        jen "It grinds the beans fresh, tamps the grounds, does the shot. All without us doing much."
        jen "Well... when it feels like cooperating."

        name "Looks complicated..."
        jen "It is, but luckily it's smarter than both of us. Mostly."
        show jennyamusedlookstraight with dissolve
        hide jennyoccupied with dissolve
        "She grabs a metal pitcher and walks over to the steam wand."

        jen "Now the milk part. Pour it cold. Always cold."
        jen "Then steam it, just under the surface so it pulls in a bit of air. You’re going for that smooth microfoam, not a bubble bath."

        "She demonstrates with practiced, slightly impatient movements. The wand hisses as the milk swirls."

        jen "Cut it off around 65 to 70 degrees. Hotter than that and it tastes like regret."
        jen "Then just pour it in, milk first, then foam. Try not to dump it like soup."

        name "This is... more delicate than I expected."

        jen "Yeah, it’s weirdly technical for something people chug on their commute."
        hide jennyamusedlookstraight with dissolve

        "I give it a try. The milk comes out uneven, my pour’s a mess, and I nearly burn my hand."

        "Jenny sighs but adjusts my grip without making a big deal about it."

        "I spend most of the shift practicing. Steam, pour, repeat."

        "By closing, I can pull a decent shot and my latte only looks *slightly* like a chemistry experiment gone wrong."

        show jennyflirty with dissolve
        hide jennyamusedlookstraight with dissolve
        jen "Not bad. You only destroyed, what, four pitchers of milk?"
        name "Progress, right?"
        jen "Sure, if you consider turning milk into soup progress."
        hide jennyflirty with dissolve
        "The afternoon brings its usual steady flow of customers."
        "Students with laptops, business meetings, people just wanting a break."
        scene black with dissolve
        window hide
        pause
        scene coffeworkempty with dissolve
        "As the day winds down, I help with the closing routine and head out."
        show jenny2 with dissolve
        jen "Alright you were pretty useless today.. but you tried."
        name "Hey, aren’t you supposed to be training me?"
        jen "I am training you."
        jen "You just don't pay attention"
        name "I am paying attention!"
        jen "Sure you are."
        jen "I’ll see you tomorrow rookie."
        
        hide jenny with dissolve
        scene upview with dissolve
        $ money += 200
        show text "+200$" at Move((0.5, 0.6), (0.5, 0.5), 10.0)
        hide text with dissolve
        jump map3

    label workplace3:
        scene coffeworkempty
        $ work_count += 1
        $ workday_done = True
        "I walk into the coffeeshop, Jenny isn’t at the counter."
        "She must be in the restroom, probably."
        scene corridor with dissolve
        "I open the locker room door."
        scene jennychanging1 with dissolve
        "Jenny’s there, in the middle of changing."
        "Her bottoms are lowered, and I catch a glimpse of her sex pressed against her panties."
        scene jennychanging2 with dissolve
        jen "Hey [name], sorry, I won’t be long."
        "I quickly look away, feeling a bit embarrassed."
        scene corridor with dissolve
        "Jenny finishes changing and steps out of the locker room."
        show jenny3 with dissolve
        jen "Don’t make that face. Never seen a futa before?"
        name "No, it’s just... unexpected."
        "Third day. The routine is becoming clearer."
        show jennyoccupied with dissolve
        hide jenny3 with dissolve
        jen "Heads up, [name]. Big crowd expected today."
        jen "Office meeting next door."
        name "Understood."
        jen "Time to learn rush management."
        jen "Keep the flow steady."
        
        hide jennyoccupied with dissolve
        scene upviewblur with dissolve
       
        "Customers start flooding in."
        "I work the counter while Jenny handles the more complex orders."
        "The afternoon passes in controlled chaos."
        "As the day winds down, I help with the closing routine and head out."
        scene black with dissolve
        window hide
        pause
        scene coffeworkempty with dissolve
        show jennyflirty with dissolve
        jen "Good job today."
        name "Thanks, Jenny. I think I’m getting the hang of it."
        jen "Yeah maybe seeing me naked gave you motivation.."
        jen "Is that it?"
        name "What are you talking about?"
        jen "Ahah pretend you didn't see anything."
        name "Anyway, see you later..."
        
        hide jennyflirty with dissolve
        scene black with fade
        $ money += 200
        show text "+200$" at Move((0.5, 0.6), (0.5, 0.5), 10.0)
        hide text with dissolve
        jump map3

    

    label workplace4:
            scene coffeworkempty  
            $ work_count += 1  
            $ workday_done = True  
            "Fourth day at the coffee shop."  
            "Today seems quieter than usual."  

            show jenny with dissolve  
            jen "Morning, [name]. Looks like it's going to be a slow one today."
            jen "It's only you and me.."
            name "That's fine by me. Maybe I can practicing my latte art."  
            show jennyannoyed with dissolve
            hide jenny with dissolve
             
            jen "You don't have to try to be the perfect employee"  

            name "What do you mean?"  

            show jenny3 with dissolve  
            hide jennyannoyed with dissolve  

            jen "I mean, look around. We have like no customers total."  
            jen "And you're over there polishing the espresso machine like it's going to cure cancer."  

            name "I just want to do a good job..."  

            jen "Yeah, I can tell. It's actually kind of annoying."  
            jen "Most people would be happy to take it easy on a day like this."  

            "Jenny walks over to the counter and leans against it, watching me with a faint smirk."  
            show jennyflirty with dissolve
            hide jenny3 with dissolve
            jen "You know what? Since you're so eager to work..."  
            jen "How about you organize those boxes under the counter?"  
            jen "They've been a mess for weeks."  

            name "Sure, no problem."  

            jen "Of course it's no problem for you."  

            scene jennyworking
            "I crouch down and start pulling out the boxes from under the counter"
            "They're filled with coffee supplies, napkins, and random coffee shop stuff."  
            "Some of them are pretty heavy."  
            jen "Make sure you stack them properly. Heavy ones at the bottom."  
            jen "And try not to make it look like a tornado hit the place."  

            name "Got it."  

            "I focus on rearranging the boxes, my back slightly turned to Jenny."
            scene jennyworking2
            "As I shift a particularly bulky carton, I hear a soft rustle of fabric."  
            "A smell hits my nostrils, rich and musky."
            scene jennyworking2ericunder  
            "I turn around and see her penis pulled out."  
            scene jennyworking2ericunder3
            
            jen "You’re… distracted, [name]."
            "Her voice is low, teasing." 
            scene jennyworking2ericundercloseup
            jen "Something catching your eye?"
            scene jennyworking2ericundercloseup3 with dissolve
            window hide
            pause
            scene jennyworking2ericundercloseup with dissolve
            window hide
            pause
            scene jennyworking2ericundercloseup3 with dissolve
            "I step closer, hesitantly."
           
            jen "Come on, don’t you want to be really useful?"
            jen "I’m sure it’s part of your contract to be nice to your colleagues."
            "I take the risk and move even nearer."
            scene black
            "Jenny grabs my head and presses my face against her cock."
            scene jennyangleup2
           
            "She guides her length into my mouth and begins rolling her hips against the counter."
            jen "Oh fuck..."
            scene jennyangleup1
            
            scene jennyangleup2 with dissolve
            $ renpy.pause(0.5, hard = True)
            scene jennyangleup3 with dissolve
            $ renpy.pause(0.5, hard = True)
            scene jennyangleup2 with dissolve
            $ renpy.pause(0.5, hard = True)
            scene jennyangleup1 with dissolve
            window hide
            pause
            scene jennyangleup2 with dissolve
            window hide
            pause
            scene jennyangleup3 with dissolve
            window hide
            pause
            scene jennyangleup2 with dissolve
            window hide
            pause
            scene jennyangleup1 with dissolve
            window hide
            pause
            scene jennyfaceangle with dissolve
            jen "I think we’re gonna be a bit behind schedule..."
            scene jennyfaceangle2 with dissolve
            jen "But since I’m here to train you,"
            scene jennyfaceangle with dissolve
            jen "I guess we can take our time."
            scene jennyfaceangle2 with dissolve
            jen "And call it on-the-job training."
            scene jennyfaceangle with dissolve
            "I nod, my mouth still full"
            scene jennyangleup2 with dissolve
            window hide
            pause
            scene jennyangleup3 with dissolve
            window hide
            pause
            scene jennyangleup2 with dissolve
            window hide
            pause
            scene jennyangleup1 with dissolve
            window hide
            pause
            scene jennyangleup2 with dissolve
            window hide
            pause
            scene jennyangleup3 with dissolve
            window hide
            pause
            scene jennyangleup2 with dissolve
            window hide
            pause
            scene jennyangleup1 with dissolve
            window hide
            pause
            jen "You do have a looot to learn..."
            scene black with dissolve
            "She make me suck her dick for long minutes."  
            "It feels like I’m still working, but my job has changed a bit..."  

            scene jennypose24 with dissolve  
            jen "Fuck, your mouth is so tight."  

            scene jennypose25 with dissolve  
            jen "I feel like I’m fucking a pussy..."  

            scene jennypose24 with dissolve  
            jen "It’s so warm and wet..."  

            scene jennypose25 with dissolve  
            jen "Hey, if you suck me nicely, I’ll ask the boss for a raise..."  
            scene jennypose24 with dissolve  
            jen "It’s not like you’re the first one to get ‘special training.’"  
            scene jennypose25 with dissolve
            window hide 
            pause
            scene jennypose24 with dissolve
            window hide 
            pause
            scene jennypose25 with dissolve
            window hide 
            pause
            scene jennypose24 with dissolve
            window hide 
            pause
            scene jennypose1 with dissolve
            name "I just hope no customers show up yet..."
            jen "It's still early, so you'll have some time to learn from me for a bit."
            scene jennypose2 with dissolve
            window hide 
            pause
            scene jennypose1 with dissolve
            window hide 
            pause
            scene jennypose2 with dissolve
            window hide 
            pause
            scene jennypose1 with dissolve
            window hide 
            pause
            scene jennypose2 with dissolve
            window hide 
            pause
            scene jennypose1 with dissolve
            window hide 
            pause
            scene jennypose2 with dissolve
            window hide 
            pause
            scene jennypose1 with dissolve
            window hide 
            pause
            scene jennypose24 with dissolve
            window hide 
            pause
            scene jennypose25 with dissolve
            window hide 
            pause
            scene jennypose26 with dissolve
            window hide 
            pause
            scene jennypose25 with dissolve
            window hide 
            pause
            scene jennypose24 with dissolve
            window hide 
            pause
            scene jennypose25 with dissolve
            window hide 
            pause
            scene jennypose26 with dissolve
            window hide 
            pause
            scene jennypose25 with dissolve
            window hide 
            pause
            scene jennypose24 with dissolve
            window hide 
            pause
            scene jennypose1 with dissolve
            window hide 
            pause
            scene jennypose2 with dissolve
            window hide 
            pause
            scene jennypose1 with dissolve
            window hide 
            pause
            jen "I see that you are eager to improve."  
            jen "Little slut.."
            scene jennypose2 with dissolve
            window hide 
            pause
            scene jennypose1 with dissolve
            window hide 
            pause
            scene jennypose2 with dissolve
            window hide 
            pause
            scene jennypose1 with dissolve
            window hide 
            pause
            scene jennypose2 with dissolve
            window hide 
            pause
            scene black with dissolve
          
            "After what feels like forever working his length with her mouth, Jenny grows restless..."


            scene jennypose22 with dissolve
            window hide 
            pause
            scene jennypose21 with dissolve
            window hide 
            pause
            scene jennypose22 with dissolve
            window hide 
            pause
            scene jennypose21 with dissolve
            window hide 
            pause
            scene jennypose22 with dissolve
            window hide 
            pause
            scene jennypose21 with dissolve
            window hide 
            pause
            scene jennypose31 with dissolve
            window hide 
            pause
            scene jennypose32 with dissolve
            window hide 
            pause
            scene jennypose33 with dissolve
            window hide 
            pause
            scene jennypose32 with dissolve
            window hide 
            pause
            scene jennypose31 with dissolve
            window hide 
            pause
            scene jennypose32 with dissolve
            window hide 
            pause
            scene jennypose33 with dissolve
            window hide 
            pause
            scene jennypose32 with dissolve
            window hide 
            pause
            scene jennypose31 with dissolve
            window hide 
            pause
            scene jennypose34 with dissolve
            window hide 
            pause
            scene endfacejenny with dissolve
            jen "Oh fuuck.."
            scene endfacejenny3 with dissolve
            jen "I am gonna unload in your mouth.. "
            scene endfacejenny with dissolve
            window hide 
            pause
            scene endfacejenny3 with dissolve
            window hide 
            pause
            scene jennypose34 with dissolve
            jen "Yeah, just like that.."
            jen "Gag on it.."
            scene jennypose32 with dissolve
            window hide 
            pause
            scene jennypose34 with dissolve
            window hide 
            pause
            scene jennypose32 with dissolve
            window hide 
            pause
            scene jennypose34 with dissolve
            window hide 
            pause
            scene jennypose32 with dissolve
            window hide 
            pause
            scene jennypose34 with dissolve
            window hide 
            pause
            scene jennypose32 with dissolve
            window hide 
            pause
            scene jennypose34 with dissolve
            window hide 
            pause
            scene jennypose32 with dissolve
            window hide 
            pause
            scene endfacejenny3 with dissolve
            jen "I am close.."
            scene endfacejenny with dissolve
            window hide 
            pause
            scene endfacejenny3 with dissolve
            window hide 
            pause
            scene endfacejenny with dissolve
            window hide 
            pause
            scene endfacejenny3 with dissolve
            window hide 
            pause
            scene endfacejenny4 with dissolve
            jen "Yeeees.."
            jen "Fuck..."
            window hide 
            pause
            scene black with dissolve
            window hide 
            pause
            scene endshotjenny with dissolve
            jen "..."
            jen "That was... so good.."
            jen "I think you'll enjoy working here."
            
            scene coffeworkempty
            "Customers begin trickling in."
            "I wipe my mouth, careful not to stain my shirt."

            
            show jenny2 with dissolve
            jen "Come on let's get to work!"
            scene upview with fade
            "The day goes by normally..."
            "...except I keep tasting Jenny's cum in my mouth all afternoon."
            scene black with fade
            window hide
            pause
            scene coffeworkempty
            show jennyflirty with dissolve
            jen "You seemed... motivated today."
            jen "Hope you liked the taste of my dick."
            jen "Because I’m nowhere near done with you."
            jen "Later."


            $ money += 200  
            show text "+200$" at Move((0.5, 0.6), (0.5, 0.5), 10.0)  
            hide text with dissolve  
            jump map3  





    label workplace5:
        $ workday_done = True
        scene upview
        "Another day at the coffee shop."
        "By now, the routine has become second nature."
        
        show jenny with dissolve
        jen "Morning, [name]. Ready for another shift?"
        name "Yeah, let's do this."
        
        scene upviewblur with dissolve
        hide jenny with dissolve
        
        "The day starts with the usual morning rush."
        "Regulars come in, order their usual drinks, and head off to work."
        
        
        "The hours pass smoothly."
        "I handle orders, make drinks, and chat with customers."
        "Nothing particularly eventful happens, but that's not necessarily a bad thing."
        
        "The afternoon brings its usual steady flow of customers."
        "Students with laptops, business meetings, people just wanting a break."
        "As the day winds down, I help with the closing routine and head out."
        "But Jenny blocks the door with her arm"
        show jenny3 with dissolve
        jen "Oh no no no. where do you think you're going, rookie?"
        name "My shift's over! Checklist's done."
        show jenny2 with dissolve
        hide jenny3 with dissolve
        jen "Mmh, forgot one item... my equipment needs polishing."
        "Jenny lock the door and guids me toward the counter"
        hide jenny2 with dissolve
        scene black with fade
        window hide
        pause

        scene jennyangleup1
        
        scene jennyangleup2 with dissolve
        $ renpy.pause(0.5, hard = True)
        scene jennyangleup3 with dissolve
        $ renpy.pause(0.5, hard = True)
        scene jennyangleup2 with dissolve
        $ renpy.pause(0.5, hard = True)
        scene jennyangleup1 with dissolve
        window hide
        pause
        scene jennyangleup2 with dissolve
        window hide
        pause
        scene jennyangleup3 with dissolve
        window hide
        pause
        scene jennyangleup2 with dissolve
        window hide
        pause
        scene jennyangleup1 with dissolve
        window hide
        pause
        scene jennyfaceangle with dissolve
        jen "I think we’re gonna be late on closing..."
        scene jennyfaceangle2 with dissolve
        jen "But since I’m here to train you,"
        scene jennyfaceangle with dissolve
        jen "I guess we can take our time."
        scene jennyfaceangle2 with dissolve
        jen "And call it on-the-job training."
        scene jennyfaceangle with dissolve
        "I nod, my mouth still full"
        scene jennyangleup2 with dissolve
        window hide
        pause
        scene jennyangleup3 with dissolve
        window hide
        pause
        scene jennyangleup2 with dissolve
        window hide
        pause
        scene jennyangleup1 with dissolve
        window hide
        pause
        scene jennyangleup2 with dissolve
        window hide
        pause
        scene jennyangleup3 with dissolve
        window hide
        pause
        scene jennyangleup2 with dissolve
        window hide
        pause
        scene jennyangleup1 with dissolve
        window hide
        pause
        jen "You do have a looot to learn..."
        scene black with dissolve
        "She made me suck her dick for long minutes."  
        "It feels like I’m still working, but my job has changed a bit..."  

        scene jennypose24 with dissolve  
        jen "Fuck, your mouth is so tight."  

        scene jennypose25 with dissolve  
        jen "I feel like I’m fucking a pussy..."  

        scene jennypose24 with dissolve  
        jen "It’s so warm and wet..."  

        scene jennypose25 with dissolve  
        jen "Hey, if you suck me nicely, I’ll ask the boss for a raise..."  
        scene jennypose24 with dissolve  
        jen "It’s not like you’re the first one to get ‘special training.’"  
        scene jennypose25 with dissolve
        window hide 
        pause
        scene jennypose24 with dissolve
        window hide 
        pause
        scene jennypose25 with dissolve
        window hide 
        pause
        scene jennypose24 with dissolve
        window hide 
        pause
        scene jennypose1 with dissolve
        
        scene jennypose2 with dissolve
        window hide 
        pause
        scene jennypose1 with dissolve
        window hide 
        pause
        scene jennypose2 with dissolve
        window hide 
        pause
        scene jennypose1 with dissolve
        window hide 
        pause
        scene jennypose2 with dissolve
        window hide 
        pause
        scene jennypose1 with dissolve
        window hide 
        pause
        scene jennypose2 with dissolve
        window hide 
        pause
        scene jennypose1 with dissolve
        window hide 
        pause
        scene jennypose24 with dissolve
        window hide 
        pause
        scene jennypose25 with dissolve
        window hide 
        pause
        scene jennypose26 with dissolve
        window hide 
        pause
        scene jennypose25 with dissolve
        window hide 
        pause
        scene jennypose24 with dissolve
        window hide 
        pause
        scene jennypose25 with dissolve
        window hide 
        pause
        scene jennypose26 with dissolve
        window hide 
        pause
        scene jennypose25 with dissolve
        window hide 
        pause
        scene jennypose24 with dissolve
        window hide 
        pause
        scene jennypose1 with dissolve
        window hide 
        pause
        scene jennypose2 with dissolve
        window hide 
        pause
        scene jennypose1 with dissolve
        window hide 
        pause
        scene jennypose2 with dissolve
        window hide 
        pause
        scene jennypose1 with dissolve
        window hide 
        pause
        scene jennypose2 with dissolve
        window hide 
        pause
        scene jennypose1 with dissolve
        window hide 
        pause
        scene jennypose2 with dissolve
        window hide 
        pause
        scene black with dissolve
        
        "After what feels like forever working his length with her mouth, Jenny grows restless..."


        scene jennypose22 with dissolve
        window hide 
        pause
        scene jennypose21 with dissolve
        window hide 
        pause
        scene jennypose22 with dissolve
        window hide 
        pause
        scene jennypose21 with dissolve
        window hide 
        pause
        scene jennypose22 with dissolve
        window hide 
        pause
        scene jennypose21 with dissolve
        window hide 
        pause
        scene jennypose31 with dissolve
        window hide 
        pause
        scene jennypose32 with dissolve
        window hide 
        pause
        scene jennypose33 with dissolve
        window hide 
        pause
        scene jennypose32 with dissolve
        window hide 
        pause
        scene jennypose31 with dissolve
        window hide 
        pause
        scene jennypose32 with dissolve
        window hide 
        pause
        scene jennypose33 with dissolve
        window hide 
        pause
        scene jennypose32 with dissolve
        window hide 
        pause
        scene jennypose31 with dissolve
        window hide 
        pause
        scene jennypose34 with dissolve
        window hide 
        pause
        scene endfacejenny with dissolve
        window hide 
        pause
        scene endfacejenny3 with dissolve
        window hide 
        pause
        scene endfacejenny with dissolve
        window hide 
        pause
        scene endfacejenny3 with dissolve
        window hide 
        pause
        scene jennypose34 with dissolve
        window hide 
        pause
        scene jennypose32 with dissolve
        window hide 
        pause
        scene jennypose34 with dissolve
        window hide 
        pause
        scene jennypose32 with dissolve
        window hide 
        pause
        scene jennypose34 with dissolve
        window hide 
        pause
        scene jennypose32 with dissolve
        window hide 
        pause
        scene jennypose34 with dissolve
        window hide 
        pause
        scene jennypose32 with dissolve
        window hide 
        pause
        scene jennypose34 with dissolve
        window hide 
        pause
        scene jennypose32 with dissolve
        window hide 
        pause
        scene endfacejenny3 with dissolve
        window hide 
        pause
        scene endfacejenny with dissolve
        window hide 
        pause
        scene endfacejenny3 with dissolve
        window hide 
        pause
        scene endfacejenny with dissolve
        window hide 
        pause
        scene endfacejenny3 with dissolve
        window hide 
        pause
        scene endfacejenny4 with dissolve
        window hide 
        pause
        window hide 
        pause
        scene black with dissolve
        window hide 
        pause
        scene endshotjenny with dissolve
        jen "..."
        jen "That was... so good.."
        jen "Here, I think you deserve a raise"
        "She tosses some cash on the table."
        $ money += 250
        $ workday_done = True
        show text "+250$" at Move((0.5, 0.6), (0.5, 0.5), 10.0)
        hide text with dissolve
        jen "See you later"
        scene black with fade
        window hide
        pause
        jump map3