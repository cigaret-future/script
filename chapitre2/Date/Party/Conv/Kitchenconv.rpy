label stacymelanieconv:
    if drink_count >= 5 and stacybourreconv_done == False:
        jump stacyconvbourre1
    elif drink_count >= 5 and stacybourreconv_done == True:
        jump stacyconvbourre2

    elif zoeyasketfor_music == True:
        jump stacyaskformusic
    elif stacymelanieconv_count == 0:
        jump stacymelanie1
    elif stacymelanieconv_count == 1:
        jump stacymelanie2


    label stacymelanie1:    
        $ stacymelanieconv_count =+ 1
        if sebastianjen_date_started == True:
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
            if sebastianjen_date_started == True:
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
            $ stacymelanieconv_count =+ 1
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
            tra "I do that a lot at the café."
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

        label stacymelanie3:
            if sebastianjen_date_started == True:
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
            $ stacymelanieconv_count =+ 1
            mela "You’re taking this way too seriously."
            tracy "No, I’m sure she really felt something real."
            mela "Oh, come on, not that again."
            mela "Hey you, make yourself useful."
            mela "Do you think polyamorous relationships can actually work?"
            name "Uh, I guess... in theory, yeah."
            mela "In theory, sure."
            mela "But reality tends to be messier."
            tracy "That’s not what I mean. What I’m really asking is: can you be in love with more than one person at once?"
            mela "That’s the same thing."
            tracy "No, it's not. Being in love and being in a relationship are two different things."
            name "I think... yeah, you can love more than one person. But it’s never the same kind of love."
            mela "How convenient."
            tracy "I actually agree. Love shifts depending on the person—it’s not a fixed recipe."
            mela "Sounds like something people say when they don’t want to pick a side."
            tracy "Or when they finally stop pretending everything fits into neat little boxes."
            mela "So now exclusivity is just a social myth?"
            name "Yes, it's a choice we make, even though we could experiment something else."
            tracy "Exactly. It’s not natural, it’s something people agree on."
            tracy "We weren't born to be nourished by the love of just one person."
            mela "Funny, coming from someone who pouts when they don’t get a goodnight text."
            tracy "You're mean when you know you're wrong."
            tracy "I never said I was free from all forms of relationships."
            mela "Okay, but at some point, you have to choose. We live in this society, we can't just do whatever we want."
            name "That’s... actually a good point."
            tracy "Don’t support her in her need to stick to old-fashioned ideas."
            mela "He knows I'm right."
            mela "He's just being honest."
            name "I admit, I'm sometimes skeptical about open relationships."
            name "But as long as no one is forced into it, I don't see the problem."
            mela "That's all I'm saying: I'm still waiting to see a happy polyamorous person."
            tracy "I know plenty who are."
            mela "Really? I’d love to meet them."
            tracy "But if I introduce them to you, you’ll just try to dissect their lives to prove you’re right."
            mela "Of course I will."
            
            mela "So back to the main question: if you were in love with two people, what would you do?"
            mela "Tell us what you would do, [name]."
            name "I don’t know... try to be honest, I guess."
            mela "You would choose."
            name "Oui eventuellement."
            mela "Eventually..."
            name "Yeah, it takes time to choose."
            mela "Ahaha."
            tracy "I'm not necessarily against making choices."
            tracy "But sometimes, not choosing is also a choice."
            mela "Whoa, shh, you're confusing us now."
            mela "We were getting close to the revealed truth."
            mela "From the mouth of [name]."
            mela "[name] said, polyamorous people are just delaying the moment to decide."
            name "No, I didn't say that..."
            mela "Thanks for your honesty."
            tracy "Let it go [name], she just wants to be right."
            tracy "I understood your position and I accept it."
            mela "You're so cute when you act all comprehensive."
            "Melany moves closer to Tracy and whispers in her ear."
            "Tracy blushes and laughs nervously."
            jump kitchenparty

        label stacymelanie4:
            if sebastianjen_date_started == True:
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
            $ stacymelanieconv_count =+ 1
            "Melany walks away to talk to someone else."
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
            tra "She helped me come out of my shell."
            tra "Juste "
            

        # menu:
        #     "Yes":
        #         name "Yes, please."
        #         mela "Okay, I’ll be right back."
        #         show designgirl010 with dissolve:
        #             xalign 0.2
        #             yalign 0.99
        #         hide designgirl009 with dissolve
        #     "No":
        #         name "No, thanks."
        #         mela "as you want"
        #         show designgirl010 with dissolve:
        #             xalign 0.2
        #             yalign 0.99
        #         hide designgirl009 with dissolve
        # show designgirl010 with dissolve:
        #     xalign 0.2
        #     yalign 0.99
        # hide designgirl011 with dissolve
        # mela "Speaking of talking, t'a pas l'air d'être un grand parleur toi non plus."
        # name "qui ça moi?"
        


        # tra "You’re gonna call me that forever now?"
        # mela "I mean, if the shoe fits."
        # tra "You don't even know me."
        # mela "I know enough."
        # tra "No. You know the version of me you made up in your head."
        # mela "Defensive much?"
        # tra "Maybe. Maybe because... maybe because I don't like what you think of me."

        # show designgirl011 with dissolve:
        #     xalign 0.2
        #     yalign 0.99
        # hide designgirl010 with dissolve

        # mela "Then show me I'm wrong."

        # "I step closer. There's a tension now, heavy and real."

        # tra "Maybe I will."
        # tra "But maybe you’ll have to stop judging first."

        # "Mela tilts her head, studying me like I’m a riddle she’s not sure she wants to solve."

        # show mela_blush at left with dissolve:
        #     xalign 0.2
        # hide designgirl011 with dissolve

        # mela "Maybe... I like judging you."
        # mela "It's fun watching you get all serious."

        # tra "And maybe I like it when you look at me like that."

        # "Mela's smile falters for a second. A crack. She catches it fast, but I saw it."

        # show tracy5 at right with dissolve:
        #     xalign 0.8
        # hide tracy3 with dissolve

        # mela "Careful, Tra."
        # mela "You’re dangerously close to being interesting."

        # tra "Good. Because you’re dangerously close to being wrong about me."

        # "A beat. A slow, electric silence."

        # mela "We'll see."

        # "I sit next to her. Close enough to touch, but I don't. Not yet."

        # tra "Yeah. We will."

        # "Neither of us says anything more. The night folds around us, thick and humming."


        # jump kitchenparty

    label stacyaskformusic:
        if stacydate_activated == True:
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
        tra "Uh, no?"
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
        
        name "Je peux mettre quelque c"
        name "Can I play you something? I think you'll like it."
        name "It's kind of the same vibe."
        mela "What is it?"
        name "It's in my playlist, I found it recently. Can you disconnect your phone?"
        mela "Okay..."
        name "You'll see, you're going to love it."
        "Why do I always get myself into trouble like this?"
        jump kitchenparty

    label stacyconvbourre:
        label stacyconvbourre1:
            if stacydate_activated == True:
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
        if stacydate_activated == True:
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

        name "Hey, was it one of you who put your music on the speakers?"
        jeni "Uh, no?"
        elo "Nah it's not us."
        bru "I like the vibe, though."
        $ trio_musicasked = True
        jump kitchenparty

label trioconv:
    if trio_musicasked == True and trio_musicasked == False:
        jump trioaskformusic
    elif drink_count >= 5 and drink_count <= 10:
        jump trioconvbourre1
    elif drink_count >= 10:
        jump trioconvbourre2
    elif trioconv_count == 0:
        jump trioconv1
    elif trioconv_count == 1:
        jump trioconv2









    label trioconvbourre1:
        if stacydate_activated == True:
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
        "I approach the group of friends."
        


    label trioconv1:

        if stacydate_activated == True:
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
        jump kitchenparty

    label trioconv2:
        scene kitchenarrowflou
        
        show jennifer062 at left with dissolve:
            xalign 0.3
            zoom 0.94
        show bruno061 at center with dissolve:
            xalign 0.5
            zoom 1.02
        show elodie063 at right with dissolve:
            xalign 0.7
            zoom 0.98