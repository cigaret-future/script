label stacymelanieconv:
    
    if drink_count >= 5 and stacybourreconv_done == False:
        jump stacyconvbourre1
    elif drink_count >= 5 and stacybourreconv_done == True:
        jump stacyconvbourre2
    elif stacydate_over == True:
        jump stacymelanie5
    elif zoeyasketfor_music == True and music_changed == False:
        jump stacyaskformusic
    elif stacymelanieconv_count == 0:
        jump stacymelanie1
    elif stacymelanieconv_count == 1:
        jump stacymelanie2
    elif stacymelanieconv_count == 2:
        jump stacymelanie3
    elif stacymelanieconv_count == 3:
        jump stacymelanie4


    label stacymelanie1:    
       
        if sebastianjen_date_started == True or sebastianjen_date_done == True:
            scene kitchenarrownojenblur
        else: 
            scene kitchenarrow
            scene kitchenarrowflou with dissolve 
        show tracy2 with dissolve
        show tracy2 at right:
            xalign 0.8
        show designergirl15 with dissolve:
            xalign 0.2
            yalign 0.99
        $ stacymelanieconv_count += 1
        "I walk up to two girls deep in conversation."
        tra "Crazy, I never thought a student could have an apartment here."
        tra "This isn’t really the kind of neighborhood where you run into students, right?"
        show designgirl007 with dissolve:
            xalign 0.2
            yalign 0.99
        hide designergirl15 with dissolve
        mela "The girl’s loaded, didn’t you know?"
        mela "I know who she is—her parents are super rich, engineers or something like that."
        mela "Honestly, half the people at uni are like her."
        mela "Rich kids everywhere..."
        tra "And what about me, do I look like a rich kid to you?"
        show designgirl010 with dissolve:
            xalign 0.2
            yalign 0.99
        hide designergirl15 with dissolve
        mela "You? Haha. Maybe halfway."
        mela "Let’s just say you’re not a lost cause."
        
        show tracy3 at right with dissolve:
            xalign 0.8
        hide tracy2 with dissolve
        tra "Good to know you’ve got me all figured out."

        hide stacyv2
        hide stacyv2 with dissolve
        hide designer4
        hide designer4 with dissolve
        jump kitchenparty 
        
    label stacymelanie2:
            if sebastianjen_date_started == True or sebastianjen_date_done == True:
                scene kitchenarrownojenblur
            else: 
                scene kitchenarrow
                scene kitchenarrowflou with dissolve  
            show tracy2 with dissolve
            show tracy2 at right:
                xalign 0.8
            show designergirl15 with dissolve:
                xalign 0.2
                yalign 0.99
            $ stacymelanieconv_count += 1
            mela "Hey, are you eavesdropping on us?"
            name "Me? No, I mean, I was just kind of listening in a bit."
            mela "Oh really? And you think it’s normal to listen in on two girls talking?"
            name "Sorry, I didn’t mean to bother you."
            show designgirl009 with dissolve:
                xalign 0.2
                yalign 0.99
            hide designergirl15 with dissolve
            mela "Relax, I’m just messing with you."
            mela "Did you come here alone?"
            name "I know Hugo and Zoey, but yeah, I came by myself."
            name "I like meeting new people, getting to know them."
            name "But I don’t really know anyone here, so I’m never sure how to start a conversation."
            mela "So you just stand next to people and listen in?"
            name "Yeah, well, I’m new here."
            tra "Go easy on him, it’s not easy when you don’t know anyone."
            tra "Besides, sometimes it’s nice to just listen."
            tra "I do that a lot at the coffee shop."
            mela "That sounds boring."
            name "You don’t like listening?"
            mela "I’d rather talk."
            tra "Yeah, you’re definitely not the listening type."
            
            show designgirl007 with dissolve:
                xalign 0.2
                yalign 0.99
            hide designgirl009 with dissolve
            mela "I mean, I like listening to music, but not to people."
            mela "You’re all so boring, wanting to just listen."
            mela "It’s like those people who say:"
            mela "'If you can sit in silence with someone, it means they’re the right person.'"
            mela "No way, when I’m dating, I’m like: talk!"
            show designer004 with dissolve:
                xalign 0.2
                yalign 0.99
            hide designgirl007 with dissolve
            mela "What’s the point otherwise?"
            mela "We’re not just going to stare at each other in silence for hours."
            show tracy3 with dissolve:
                xalign 0.8
            hide tracy2 with dissolve
            tra "That’s actually oppressive."
            show designgirl011 with dissolve:
                xalign 0.2
                yalign 0.99
            hide designer004 with dissolve
            tra "What if the person doesn’t feel like talking?"
            tra "Maybe they’re just searching for the right words."
            tra "We are not all equal when it comes to language."
            mela "What?"
            tra "It's scientifically proven nowadays."
            show designgirl009 with dissolve:
                xalign 0.2
                yalign 0.99
            hide designgirl011 with dissolve
            mela "It's probably a theory made by people who had no conversation skills."
            mela "Anyway, I’m going to grab a beer, do you want one?"
            tra "Yeah, sure."
            mela "Here you go"
            jump kitchenparty

    label stacymelanie3:
        if sebastianjen_date_started == True or sebastianjen_date_done == True:
            scene kitchenarrownojenblur
        else: 
            scene kitchenarrow
            scene kitchenarrowflou with dissolve 
        show tracy2 with dissolve
        show tracy2 at right:
            xalign 0.8
        show designergirl15 with dissolve:
            xalign 0.2
            yalign 0.99
        $ stacymelanieconv_count += 1
        mela "You’re taking this way too seriously."
        tra "No, I’m sure she really felt something real."
        mela "Oh, come on, not that again."
        mela "Hey you, make yourself useful."
        mela "Do you think polyamorous relationships can actually work?"
        name "Uh, I guess... in theory, yeah."
        mela "In theory, sure."
        mela "But reality tends to be messier."
        tra "That’s not what I mean. What I’m really asking is: can you be in love with more than one person at once?"
        mela "That’s the same thing."
        tra "No, it's not. Being in love and being in a relationship are two different things."
        name "I think... yeah, you can love more than one person. But it’s never the same kind of love."
        mela "How convenient."
        tra "I actually agree. Love shifts depending on the person—it’s not a fixed recipe."
        mela "Sounds like something people say when they don’t want to pick a side."
        tra "Or when they finally stop pretending everything fits into neat little boxes."
        mela "So now exclusivity is just a social myth?"
        name "Yes, it's a choice we make, even though we could experiment something else."
        tra "Exactly. It’s not natural, it’s something people agree on."
        tra "We weren't born to be nourished by the love of just one person."
        mela "Funny, coming from someone who pouts when they don’t get a goodnight text."
        tra "You're mean when you know you're wrong."
        tra "I never said I was free from all forms of relationships."
        mela "Okay, but at some point, you have to choose. We live in this society, we can't just do whatever we want."
        name "That’s... actually a good point."
        tra "Don’t support her in her need to stick to old-fashioned ideas."
        mela "He knows I'm right."
        mela "He's just being honest."
        name "I admit, I'm sometimes skeptical about open relationships."
        name "But as long as no one is forced into it, I don't see the problem."
        mela "That's all I'm saying: I'm still waiting to see a happy polyamorous person."
        tra "I know plenty who are."
        mela "Really? I’d love to meet them."
        tra "But if I introduce them to you, you’ll just try to dissect their lives to prove you’re right."
        mela "Of course I will."
        
        mela "So back to the main question: if you were in love with two people, what would you do?"
        mela "Tell us what you would do, [name]."
        name "I don’t know... try to be honest, I guess."
        mela "You would choose."
        name "Yes, eventually."
        mela "Eventually..."
        name "Yeah, it takes time to choose."
        mela "Ahaha."
        tra "I'm not necessarily against making choices."
        tra "But sometimes, not choosing is also a choice."
        mela "Whoa, shh, you're confusing us now."
        mela "We were getting close to the revealed truth."
        mela "From the mouth of [name]."
        mela "[name] said, polyamorous people are just delaying the moment to decide."
        name "No, I didn't say that..."
        mela "Thanks for your honesty."
        tra "Let it go [name], she just wants to be right."
        tra "I understood your position and I accept it."
        mela "You're so cute when you act all comprehensive."
        "Melany moves closer to Tracy and whispers in her ear."
        "Tracy blushes and laughs nervously."
        
        jump kitchenparty

        label stacymelanie4:
            if sebastianjen_date_started == True or sebastianjen_date_done == True:
                scene kitchenarrownojenblur
            else: 
                scene kitchenarrow
                scene kitchenarrowflou with dissolve
            show tracy2 with dissolve
            show tracy2 at right:
                xalign 0.8
            show designergirl15 with dissolve:
                xalign 0.2
                yalign 0.99
            $ stacymelanieconv_count += 1
            "Melany walks away to talk to someone else."
            hide designergirl15 with dissolve
            tra "So, are you enjoying the party?"
            name "It's okay."
            tra "I see you going back and forth, you look like you're looking for someone."
            name "Not really, I don't know many people here."
            tra "You can stay with us if you want."
            name "Thanks, I don't want to bother you."
            tra "Don't worry."
            tra "We don't mind."
            tra "The more, the merrier."
            tra "I think Melany likes you."
            name "You think so?"
            tra "Yes, of course."
            tra "You'd know if it wasn't the case."
            tra "You seem like a chill person."
            name "Yeah, people tell me that sometimes."
            name "How did you and Melany meet?"
            tra "Some friends introduced us."
            tra "She helped me come out of my shell..."
            name "I see."
            show designergirl15 with dissolve:
                xalign 0.2
                yalign 0.99
            mela "Fucking bourgeois.."
            name "what's up?"
            mela "I was talking to this guy about an exhibition I saw.."
            mela "and he was like 'oh yes, this artist is so problematic, because the representation of violence ... blah, blah blah...'"
            mela "I'm like, why do you like art if you are going to be so judgmental?"
            tra "Actually, having a relationship with art means taking a position about it."
            tra "It's inevitable."
            tra "But it goes further than 'I like it or I don't like it.'"
            mela "yeah whatever, I just want to enjoy the art without having to think about it."
            tra "But you can't enjoy without thinking about it."
            mela "omg shut up, drink something."
            tra "I don't want to drink."
            tra "Don't you want to do something else than drinking."
            mela "What do you want to do?"
            tra "I don't know, something out of the ordinary."
            mela "OMG you are going to depress me, I can feel it."
            mela "I'll leave you two talking about art."
            hide designergirl15 with dissolve
               
            "Melanie walks away and goes to the living room."
            tra "She's really weird."
            name "It's ok... I feel like I should leave you two."
            tra "No! Don't worry."
            tra "I enjoy your presence."
            name "I enjoy yours too."
            tra "It's a bit lousy here don't you think?"
            tra "Do you want to go somewhere else?"
            name "Like where?"
            tra "I don't know, maybe we can go upstairs?"
            name "Oh ok why not."
            jump tracyupstairnoisabelle

        label stacymelanie5:
            if sebastianjen_date_started == True or sebastianjen_date_done == True:
                    scene kitchenarrownojenblur
            else: 
                scene kitchenarrow
                scene kitchenarrowflou with dissolve
            show tracy2 with dissolve
            show tracy2 at right:
                xalign 0.8
            show designergirl15 with dissolve:
                xalign 0.2
                yalign 0.99
            mela "Hey what's up?"
            name "I was just wondering around."
            mela "You are exploring huh?"
            mela "Be careful not to venture too far."
            mela "I think we should go Tracy.."
            tra "Yeah.."
            mela "See you"
            name "Oh ok.. bye"
            tra "Bye"
            "Tracy gives me one last look and leaves with Melanie"
            "What the fuck was that?"
            $ tracymelaniedate_done = True
        jump kitchenparty

   



    label stacyaskformusic:
        if sebastianjen_date_started == True:
            scene kitchenarrownomelblur
        else:
            scene kitchenarrow
            scene kitchenarrowflou with dissolve 
        show tracy2 with dissolve
        show tracy2 at right:
            xalign 0.8
        show designergirl15 with dissolve:
            xalign 0.2
            yalign 0.99
        name "Hey, was it one of you who put your music on the speakers?"
       
        mela "Yeah, why do you ask?"
        mela "Do you want to change it?"
        name "No, it's really cool. I just wanted to know who the artist was."
        mela "Modulär."
        mela "I discovered them at a festival."
        name "It's pretty unique."
        mela "It brings back memories—those nights in tents after the concerts..."
        mela "It's wild, I've become so bourgeois."
        tra "Alright, we get it, you're a rebel."
        tra "Do you really miss being in the mud, sleeping in a tent, and waking up with frozen feet?"
        
        name "Can I play you something? I think you'll like it."
        name "It's kind of the same vibe."
        mela "What is it?"
        name "It's in my playlist, I found it recently. Can you disconnect your phone?"
        mela "Okay..."
        name "You'll see, you're going to love it."
        "Why do I always get myself into trouble like this?"
        $ music_changed = True
        jump kitchenparty

    label stacyconvbourre:
        label stacyconvbourre1:
            if sebastianjen_date_started == True:
                scene kitchenarrownomelblur
            else:
                scene kitchenarrow
                scene kitchenarrowflou with dissolve 
                show tracy2 with dissolve
                name "Do you think people choose their favorite dish, or does the dish choose them?"
                tra "Hmm. You mean like astrology?"
                name "Exactly. For me, it's risotto. It appeared to me in a dream."
                tra "I love risotto, it's such a comforting dish ahah..."
                name "I took it as a sign. Since then, I order it everywhere. Even in Japanese restaurants."
                tra "And does it work?"
                name "No. But I still have hope. Sometimes you have to force destiny a little."
                tra "I see."
                $ stacybourreconv_done = True
                jump kitchenparty
            label stacyconvbourre2:
                scene kitchenarrow
                scene kitchenarrowflou with dissolve 
                show tracy2 at right:
                    xalign 0.8
                show designergirl15 with dissolve:
                    xalign 0.2
                    yalign 0.99
                name "Hey, do you know where I can find a bathroom?"
                tra "Yeah, it's upstairs"
                name "thanks"
                show designgirl009 with dissolve:
                    xalign 0.2
                    yalign 0.99
                hide designergirl15 with dissolve

                mela "Wouhouuu, let's party right?"
                
                jump kitchenparty


    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// TRIO CONV
    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    label trioaskformusic:
        if stacydate_activated == True or tracymelaniedate_done == True:
                scene kitchenarrownomelblur
        else:
                scene kitchenarrow
                scene kitchenarrowflou with dissolve 
        
        show jennifer062 at left with dissolve:
            xalign 0.3
            zoom 0.94
        show bruno061 at center with dissolve:
            xalign 0.5
            zoom 1.02
        show elodie063 at right with dissolve:
            xalign 0.7
            zoom 0.98
        if tracymelaniedate_done == True or stacydate_activated == True:
            name "Hey, was it one of you who put your music on the speakers?"
        
            elo "Yeah, we finally got control of the music."
            bru "It was playing some weird stuff before."
            name "Can I play you something? I think you'll like it."
            name "It's kind of the same vibe."
            jeni "What is it?"
            name "It's in my playlist, I found it recently. Can you disconnect your phone?"
            elo "Sure, let's hear it."
            name "You'll see, you're going to love it."
            "Why do I always get myself into trouble like this?"
            $ music_changed = True
            $ trio_musicasked = True
            jump kitchenparty

        else:
            
            name "Hey, was it one of you who put your music on the speakers?"
            jeni "Uh, no?"
            elo "Nah it's not us."
            bru "I like the vibe, though."
            $ trio_musicasked = True
            jump kitchenparty

label trioconv:
    if zoeyasketfor_music == True and trio_musicasked == False:
        jump trioaskformusic
    elif drink_count >= 5 :
        jump trioconvbourre1
    

    elif trioconv_count == 0:
        jump trioconv1
    elif trioconv_count == 1:
        jump trioconv2
    elif trioconv_count == 2 and sebastian_open == False:
        jump trioconv3
    

    elif sebastian_open == True and sebastian_mission_started == False:
        jump trioconv4
    elif sebastian_mission_started:
        jump trioconv5
    else: 
        jump trioconv3







    label trioconvbourre1:
        if stacydate_activated == True or tracymelaniedate_done == True:
            scene kitchenarrownomelblur
        else:
            scene kitchenarrow
            scene kitchenarrowflou with dissolve 
        
        show jennifer062 at left with dissolve:
            xalign 0.3
            zoom 0.94
        show bruno061 at center with dissolve:
            xalign 0.5
            zoom 1.02
        show elodie063 at right with dissolve:
            xalign 0.7
        if trioconv_count == 0:
            
            name "Hey, you three! I just wanted to say... this party is amazing!"
            jeni "Yeah, it’s pretty cool."
            bru "You look like you’re having a good time."
            name "I am! I’m just... enjoying the vibe, you know?"
            name "I feel like I can finally let loose and be myself!"
            elo "That’s great to hear."
            jeni "Just don’t overdo it, okay?"
            bru "Yeah, we don’t want you ending up in a corner talking to the fridge."
            name "No way! I’m here to have fun!"
            $ trioconv_count += 1
            jump kitchenparty
        else:
            name "Heeyyy, you three! I've been thinking... You're either my guardian angels or accomplices in my descent into hell. And I love it!"

            show elodie065 at right with dissolve:
                xalign 0.7
                zoom 0.98
            hide elodie063 with dissolve

            elo "Wow, you didn't waste any time, did you."

            bru "Yeah, he clearly skipped the 'moderation' phase."

            name "Moderation is for people who are afraid of... of blurry but fun memories!"

            show jennifer064 at left with dissolve:
                xalign 0.3
                zoom 0.94
            hide jennifer062 with dissolve

            jeni "You're off to a good start then."
            
            name "Listen, Jennifer. I have a theory. Exes are like cheap vodka... it hurts at first, but then you forget."
        
            elo "Where did that come from?"
            
            show bruno062 at center with dissolve:
                xalign 0.5
                zoom 1.02
            hide bruno061 with dissolve

            bru "That's the best bullshit I've heard all night."

        
            elo "Bruno, don't encourage him! Are you sure you don't need a glass of water?"

            name "Water? I am not a fish."

            jeni "Jen I think we just found your drinking buddy."

            bru "Cheers to that, then. Just... don't puke on my shoes."

            name "Cross my heart... "

            bru "Alright, ok. Maybe we'll find you a couch before you end up kissing a lamppost."
            name "A couch? No way! I want to dance! I want to feel the music in my bones!"
            name "This kitchen has the best acoustics! I can hear the music echoing in my soul!"
            elo "You should eat something.."
            
            jump kitchenparty



                
                # elo "You look a bit pale"
                # name "I am ok.. I just ate "
                # bru "Dude, you're swaying a little."
                # name "No, no... I'm perfectly... perfectly stable."
                # jeni "Maybe sit down for a minute?"
                # name "Sitting is for quitters! I'm having the best time ever!"
                # name "Did you know... did you know that this kitchen has AMAZING acoustics?"
                # "I start speaking louder than necessary."
                # name "Everything echoes! ECHO! ECHO!"
                # elo "Okay, maybe lower your voice a bit..."
                # name "But I love you guys! You're like... the best people I've met tonight!"
                # name "Actually, you're the best people I've met in my ENTIRE LIFE!"
                # bru "Alright, that's definitely the alcohol talking."
                # name "No way! I'm just... I'm just being honest for once!"
                # name "Usually I'm all... all nervous and stuff, but now I feel FREE!"
                # jeni "Maybe we should get you some water?"
                # name "Water? I am not a fish! I want to dance!"
                # name "Why isn't anyone dancing? This music is INCREDIBLE!"
                # "I start moving awkwardly to the beat."
      


    label trioconv1:

        if stacydate_activated == True or tracymelaniedate_done == True:
            scene kitchenarrownomelblur
        else:
            scene kitchenarrow
            scene kitchenarrowflou with dissolve 
        
        show jennifer062 at left with dissolve:
            xalign 0.3
            zoom 0.94
        show bruno061 at center with dissolve:
            xalign 0.5
            zoom 1.02
        show elodie063 at right with dissolve:
            xalign 0.7
            zoom 0.98
            


        "I approach a group with some familiar faces."
        name "Hi! You’re here too, this party is so cool."
        elo "Sup..."
        jeni "Hello!"
        bru "Hey, Hugo told me he invited you."
        name "This place is huge, do you know the person who lives here?"

        show elodie065 at right with dissolve:
            xalign 0.7
            zoom 0.98
        hide elodie063 with dissolve
        elo "No, but we’d like to ahah."
        bru "It’s always useful to have a rich friend."
        bru "But she’s probably not interested."
        name "Why?"
        elo "We’re not cool enough for her."
        jeni "We don’t know, we don’t really know her."
        jeni "We could go talk to her."
        bru "So we can get her disdain in our faces?"
        bru "Hell no."
        elo "Anyway, we prefer to observe."
        name "I see."
        jeni "So, are you enjoying yourself tonight?"
        name "I’m mostly just wandering around, trying to get a feel for the place."
        name "I’ve bumped into a few familiar faces, but I don’t know many people here. Just trying to blend in, you know?"
        elo "Well, if you’re up for it, Jennifer could use someone to vent to about her breakup."
        name "Oh, I’m sorry to hear that."
        bru "Don’t worry, Jennifer’s breakups are like seasons—there’s always another one around the corner."
        jeni "It’s fine, really. It’s not like I’m going to announce it to the whole party."
        elo "Come on, he seems like someone you can trust, don’t you think?"
        name "No pressure, though. If you don’t feel like talking about it, I totally get it."
        jeni "No, it’s okay. It’s not a big deal, it just happened recently."
        name "Were you together for a long time?"
        jeni "Not really. We only dated for about a week, but it just didn’t click."
        name "Ah, I see. So it wasn’t one of those long-term heartbreaks."
        jeni "Yeah, nothing like that..."
        bru "She’s just afraid of being alone, that’s all."
        bru "We’re here, don’t worry."
        if gender == "fem":
            elo "And I’m sure you’ll find a girl tonight to replace her."
        elif gender == "male":
            elo "And I’m sure you’ll find a guy tonight to replace him."
        jeni "You think?"
        if gender == "male":
            elo "Yes, just don’t ask him right away to be your boyfriend."
        elif gender == "fem":
            elo "Yes, just don’t ask her right away to be your girlfriend."
        bru "Yeah..."
        bru "And have a drink first."
        "Bruno hands her a beer."
        "She grabs it and takes a few sips."
        jeni "I need to drink more, otherwise I’ll be awkward."
        elo "Yes, take it easy though."
        elo "The last time you tried that technique, you almost threw up on your date."
        bru "Hey, do you want a beer [name]?"
        menu:
            "Yes":
                name "Ah yes, thank you."
                "I take the beer Bruno hands me and take a sip."
                $ drink_count += 1

                show text "Your mind blurs slightly." at Move((0.5, 0.6), (0.5, 0.5), 10.0)
                pause 5.0
                hide text with dissolve
                    
            "No thanks":
                name "I’m fine, thanks."
                bru "As you wish."

        bru "I hope people will want to dance at some point, I don’t want to have to make conversation all evening."

        "They keep talking while drinking."
        "I can try to keep wandering around and talking to people."
        $ trioconv_count += 1
        jump kitchenparty

    label trioconv2:
        scene kitchenarrowflou
        if stacydate_activated == True or tracymelaniedate_done == True:
            scene kitchenarrownomelblur
        else:
            scene kitchenarrow
            scene kitchenarrowflou with dissolve
        show jennifer062 at left with dissolve:
            xalign 0.3
            zoom 0.94
        show bruno061 at center with dissolve:
            xalign 0.5
            zoom 1.02
        show elodie063 at right with dissolve:
            xalign 0.7
            zoom 0.98
            

        "I walk back to the trio, who are now deeper into their drinks."

        elo "You're back"
        name "How's everyone doing?"

        show jennifer064 at left with dissolve:
            xalign 0.3
            zoom 0.94
        hide jennifer062 with dissolve

        jeni "Better! I think the alcohol is helping."
        bru "She's been practicing her pickup lines on us."
        jeni "They're not pickup lines! They're conversation starters."
        name "Like what?"
        elo "' Do you believe in love at first sight, or if she should walk by again.'"

        
        
        name "That's... actually not bad."
        jeni "See? Thank you!"

        elo "That's the least authentic thing you could tell someone"

        show elodie065 at right with dissolve:
            xalign 0.7
            zoom 0.98
        hide elodie063 with dissolve

        jeni "So [name], have you spotted anyone interesting tonight?"
        name "I'm still figuring everyone out. What about you guys?"
        bru "Bruno's been eyeing someone all night but won't admit it."
        bru "I have not."
        jeni "You totally have! The boy with the short hair in the livingroom."
        bru "Can we not do this right now?"
        elo "We're just saying, maybe you should go talk to him instead of hiding in the kitchen."
        name "Maybe he want to observe first."
        bru "Exactly! Finally, someone who gets it."
        jeni "But you can't observe forever. At some point you have to take action."
        elo "Jennifer's right. The worst that can happen is they say no."
        bru "Or they laugh at you. Or ignore you completely."
        name "True, but then at least you know where you stand."
        jeni "Exactly! And you can move on."

        $ trioconv_count += 1
        jump kitchenparty
        
    label trioconv3:
        if stacydate_activated == True or tracymelaniedate_done == True:
            scene kitchenarrownomelblur
        else:
            scene kitchenarrow
            scene kitchenarrowflou with dissolve

        show jennifer065 at left with dissolve:
            xalign 0.3
            zoom 0.94
        show bruno062 at center with dissolve:
            xalign 0.5
            zoom 1.02
        show elodie063 at right with dissolve:
            xalign 0.7
            zoom 0.98


        jeni "You know what? I'm tired of being single."
        jeni "Like, really tired. I see couples everywhere and I'm just... here."
        elo "Jennifer..."
        jeni "No, I'm serious! I want someone to text goodnight to. Someone who gets excited to see me."
        bru "You'll find someone."
        jeni "When though? I've been saying that for months."
        jeni "I keep going on these awful dates, and nothing ever clicks."
        name "Maybe you're trying too hard?"
        jeni "Maybe. But I don't want to end up alone, you know?"
        jeni "I see my friends in relationships, posting cute photos, planning trips together..."
        jeni "And I'm just... swiping through dating apps every night."
        elo "The right person will come along."
        jeni "But what if they don't? What if I'm just meant to be the friend who's always single?"
        bru "Don't think like that."
        jeni "I can't help it! Sometimes I wonder if there's something wrong with me."
        jeni "Like, why does everyone else make it look so easy?"
        name "Dating isn't easy for anyone."
        jeni "Maybe, but some people seem to find their person without even trying."
        jeni "I'm out here putting myself out there, going to parties like this..."
        jeni "Hoping maybe tonight will be different."
        elo "Well, you never know. Maybe tonight will be."
        jeni "You think? I mean, there are some cute people here..."
        jeni "Maybe I should be more direct. Just walk up to someone and see what happens."
        bru "That takes guts."
        name "Just be yourself."
        jeni "Yeah... maybe that's enough."

       
        jump kitchenparty
    
    label trioconv4:
        if stacydate_activated == True or tracymelaniedate_done == True:
            scene kitchenarrownomelblur
        else:
            scene kitchenarrow
            scene kitchenarrowflou with dissolve 
        
        show jennifer064 at left with dissolve:
            xalign 0.3
            zoom 0.94
        show bruno062 at center with dissolve:
            xalign 0.5
            zoom 1.02
        show elodie065 at right with dissolve:
            xalign 0.7
            zoom 0.98

        name "Hey guys, how are you holding up?"
        jeni "I'm still feeling a bit anxious about the whole dating thing."
        name "You know what? I'm pretty confident you're going to find someone tonight, Jennifer."
        elo "Oh really? What makes you so sure?"
        name "Well, I've been talking to people around here, and everyone seems genuinely interested in meeting new people and having a good time."
        name "The vibe is really relaxed and open, you know?"
        bru "Wait, seriously? People actually told you they're looking to meet someone?"
        name "Yeah, absolutely. There's definitely that energy in the air."
        jeni "Really? Who did you talk to?"
        name "Actually, there was this guy I met earlier on the balcony."
        name "We got to chatting, and he mentioned he's hoping to connect with someone tonight too."
        jeni "Wait, which guy? Can you point him out?"
        name "He should still be out there. Tall, short dark hair, wearing a blue shirt."
        show jenasking at left with dissolve:
            xalign 0.3
            zoom 0.94
        hide jennifer064 with dissolve
        jeni "Oh my god, I think I know who you mean! He's really cute."
        elo "Him? Really? I thought he looked kind of boring from here."
        jeni "Are you kidding? He has such a nice smile."
        name "I actually think you two might really hit it off. You seem to have similar personalities."
        jeni "You really think so?"
        name "Definitely. He seemed like a genuine, down-to-earth guy."
        jeni "Hmm..."
        jeni "Can you do me a huge favor?"
        name "What kind of favor?"
        jeni "Could you maybe go talk to him for me? Just to break the ice a little?"
        name "You want me to be your wingman?"
        jeni "Yes! You could just casually mention that I think he seems interesting and that I'd love to chat with him."
        name "I mean... I guess I could do that."
        bru "That's actually not a bad strategy."
        
        name "Alright, if you really want me to..."
        jeni "Yes! Please!"
        name "Okay, I'll go see what I can do."
        $ sebastian_mission_started = True
        $ trioconv_count += 1
        jump kitchenparty
        
label trioconv5:
    if stacydate_activated == True or tracymelaniedate_done == True:
            scene kitchenarrownomelblur
    else:
        scene kitchenarrow
        scene kitchenarrowflou with dissolve 
    
    show jenangst at left with dissolve:
        xalign 0.3
        zoom 0.94
    show bruno062 at center with dissolve:
        xalign 0.5
        zoom 1.02
    show elodie065 at right with dissolve:
        xalign 0.7
        zoom 0.98
    jeni "So what did he said?"
    if sebastian_asked_done == False:
        name "wait i didn't asked him yet."
        jeni "what are you wanting for??"
        jeni "Come on, I'll owe you one..."
        show brunolaugh at center with dissolve:
            xalign 0.5
            zoom 1.02
        hide bruno062 with dissolve
        bru "How are you going to thank him?"
        jeni "I don't know, i'll... i'll give him a hug?"
        hide brunolaugh with dissolve
        hide jenangst with dissolve
        hide elodie065 with dissolve
        jump kitchenparty
    elif sebastian_asked_done == True:
        name "He said he was interested, he'll wait for you in the livingroom."
        show jenasking at left with dissolve:
            xalign 0.3
            zoom 0.94
        hide jenangst with dissolve
        jeni "Really?"
        name "yep"
        elo "see we told you'd find someone."
        bru "You go jen!"
        jeni "Thanks guys!!"
        jeni "i'll go meet him."
        hide jenasking with dissolve
        elo "I am not sure this guy is the right one for her."
        bru "I don't know, he seems nice."
        bru "Well at least he is good looking."
        elo "Come on, let's move from here, we're not going to stay here all night."
        
        hide bruno062 with dissolve
       
        hide elodie065 with dissolve
        "I feel like I did a good deed."
        "Well, I think so."
        "Maybe it was a bit too easy."
        "I hope it works out for her."
        scene black with dissolve
        $ renpy.pause(2.0, hard = True)
        $ sebastianjen_date_started = True
        jump vestibule
        



