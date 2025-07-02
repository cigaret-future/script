label zoeyconv_direction:
    if drink_count > 10: 
        "I walk over to Zoey and Axel, my vision blurring."
        scene black
        "Someone bumps into me and I fall to the ground."
        
    elif zoey_vestibul_asked == True:
        jump zoeysscene
    elif zoeyaxelconv_count == 0:
        jump zoeyconv
    elif zoeyaxelconv_count == 1:
        jump axzoeyconv2
    elif zoeyaxelconv_count == 2:
        jump axzoeyconv3

label zoeyconv:
    # show zoeyparty at Position(xalign=0.65, yalign=0.99) with dissolve
    # show axel1 at Position(xalign=0.35, yalign=0.99) with dissolve
    scene livingroomarrowflou
    show zoeyparty with dissolve
    name "Hey Zoey"
    zoey "Hey, are you ready for the party?"
    zoey "I was afraid you wouldn't come."
    zoey "Here, have a beer."
    "Zoey hands me a beer."
    "I take the beer and open it."
    "I take a few sips"
    show text "Your mind blurs slightly." at Move((0.5, 0.6), (0.5, 0.5), 10.0)
    pause 5.0
    hide text with dissolve
    
    zoey "You know, I'm really glad you came."
    name "Yeah, I'm happy to be here too."
    zoey "I had to do a bit of persuading to get the girl who lives here to let us have the party."
    zoey "But hey, she seems to be having fun too."
    name "Ah, that's cool. Honestly, I didn't really know what to expect coming here."
    zoey "Don't worry, there are lots of parties here. People are used to meeting strangers."
    zoey "Everyone is generally pretty nice here."
    name "That's good then, I hope I'll have fun."
    zoey "Of course you will!"
    zoey "Do you want me to introduce you to Axel?"
    name "Yeah sure"
    zoey "Hey, Axel come here!"
    hide zoeyparty with dissolve
    
    show axel1 with dissolve
    "Zoey moves away and goes to talk to someone sitting on the couch."
    axel "What's up?"
    axel "Hi, nice to meet you!"
    name "Same here, I'm [name]."
    axel "So, Zoey told me you're new in town."
    axel "How are you finding it so far?"
    name "It's been good, I guess. I'm still getting used to everything."
    axel "ok cool!"
    axel "..."
    axel "I'm sorry, I'm not very good at small talk."
    axel "Usually, I'm at home listening to music."
    name "Well, I thought I was the only one not used to this kind of party."
    axel "Welcome to the club then!"
    axel "How did you meet Zoey?"
    name "She helped me on my first day."
    axel "That doesn't surprise me about her."
    name "And then, with Hugo, they invited me to a party."
    name "ahah I was like, 'wow thanks'"
    axel "Oh wow, that was quick."
    axel "It's true that it's important to make friends quickly at university."
    axel "Luckily some people know how to make the first move."
    axel "Otherwise we'd often be alone in our corner."
    name "Yes, that's true."
    name "Long live extroverts!"
    axel "ahah, cheers"
    axel "Without them, the rest of us would be hermits."
    name "Cheers!"
    hide axel1 with dissolve
    show zoeyparty at Position(xalign=0.65, yalign=0.99) with dissolve
    show axel1 at Position(xalign=0.35, yalign=0.99) with dissolve
    zoey "Are you talking about me?"
    axel "Yes, we were talking about you Zoey."
    zoey "In a good way I hope?"
    axel "We were saying we really like extroverted people like you."
    zoey "Hehe, I'm here for you my little freaks."
    zoey "I get it, I'm a bit of a freak in my own way too."
    axel "A social freak."
    zoey "Exactly."
    zoey "I know how to make you shine."
    "Zoey gives me a wink and warmly strokes my shoulder."
    axel "Zoey the projector."
    zoey "That's kind of it, yeah."
    zoey "I could really be a talent agent."
    zoey "I know how to make people stand out."
    axel "Whoa, I don't know if that's a good idea."
    "Those two seem to get along well, and to have known each other for a long time."
    "Zoey whispers in my ear"
    zoey "don't go too far"
    hide zoeyparty with dissolve
    hide axel1 with dissolve
    $ zoeyaxelconv_count += 1
    jump livingroom


label axzoeyconv2:
    scene livingroomarrowflou
    show zoeyparty at Position(xalign=0.65, yalign=0.99) with dissolve
    
    zoey "Hey [name], your glass is empty, right?"
    zoey "Do you want me to get you a beer?"
    name "Sure, thanks Zoey."
    zoey "Don't move."
    hide zoeyparty with dissolve
    "Zoey heads to the kitchen, calling out to a few people on the way."
    show axel1 at Position(xalign=0.35, yalign=0.99) with dissolve
    axel "Zoey really seems to like you, [name]."
    name "Yeah, I feel a bit spoiled."
    axel "You can. There are a lot of people who'd like her attention."
    axel "I feel like she's in a very affectionate phase right now."
    axel "She seems to want to take care of you."
    name "Ahaha, what do you mean?"
    axel "It's just that..."
    axel "Never mind."
    name "How did you meet her?"
    axel "We started university at the same time, and met in a lecture hall."
    axel "I think she was the first person I talked to here."
    axel "We hit it off right away, and started seeing each other regularly."
    axel "Actually, we dated for a while."
    name "Oh really?"
    axel "Yeah, but it was a long time ago."
    axel "Well, three years."
    name "Did you stay together long?"
    axel "No, not long, but we stayed good friends."
    axel "As you can see."
    name "Yeah, you seem close."
    axel "Yeah, but don't worry about me, if she flirts with you, I won't mind."
    name "Oh ok, thanks, but I don't think she's flirting with me."
    axel "ahah you're cute"
    "Zoey comes back with a beer, she got herself a drink too."
    show zoeyparty at Position(xalign=0.65, yalign=0.99) with dissolve
    zoey "Here you go, a beer for my favorite little freak."
    name "Thanks."
    "I take the beer and open it."
    "I take a few sips"
    show text "Your mind blurs slightly." at Move((0.5, 0.6), (0.5, 0.5), 10.0)
    pause 5.0
    hide text with dissolve
    $ drink_count += 1
    $ drink_count += 1
    axel "And me?"
    zoey "What about you?"
    axel "You didn't get me anything?"
    zoey "But you didn't ask!"
    axel "Yes I did, I asked you to get me a beer."
    zoey "Oh, liar!"
    axel "I swear on [name]'s head that I asked you for a beer."
    name "Hey!"
    zoey "She's terrible!"
    "Zoey slips behind me and puts her hand on my lower back."
    zoey "We agree she didn't ask me, right [name]?"
    name "Uuuh, I don't remember."
    zoey "Ah, there you go!"
    axel "He didn't say no, he said he didn't remember."
    zoey "Yes, that means it didn't happen."
    zoey "You agree with me, right [name]?"
    "She runs her hand over my butt."
    name "Uuuh, yeah, sure."
    axel "Jeez... [name], you should've backed me up."
    zoey "Yeah, yeah, I saw right through your game."
    zoey "Trying to gaslight me."
    zoey "So, don't you want to dance a bit instead of talking nonsense?"
    axel "I don't know who put on the music, I think it's a girl, but I don't know her name."
    zoey "Don't you want to go ask her, [name]?"
    zoey "So we can dance a bit."
    axel "She's a blonde with a blue t-shirt."
    name "Ok, I'll go see."
    zoey "Thanks, love."
    "Zoey gives me a little slap on the butt."
    $ zoeyaxelconv_count += 1
    $ zoeyasketfor_music = True
    jump livingroom


label axzoeyconv3:
    scene livingroomarrowflou
    show zoeyparty at Position(xalign=0.65, yalign=0.99) with dissolve
    show axel1 at Position(xalign=0.35, yalign=0.99) with dissolve
    name "Alright, I found the girl."
    name "She told me she disconnected."
    axel "Yeah, her music really wasn't great."
    axel "I mean who listen to Modulär these days"
    zoey "We're going to change that."
    zoey "I feel like moving a bit."
    axel "Hey, put on Velvet Pulse"
    zoey "No, I wanted to put on Rhythm."
    axel "Ugh... aren't you tired of always playing that?"
    zoey "Never!"
    scene dancing
    zoey "There we go, now we're talking."
    "Zoey starts dancing near me."
    zoey "Come on, Axel, move that body!"
    axel "No way, I'll just watch you dance."
    axel "Besides, this isn't really my kind of music."
    zoey "Pff, you're no fun."
    scene dancingzoey
    zoey "Come on, [name], dance with me."
    name "Uh, I don't really know how to dance."
    zoey "Just move your hips, it's easy."
    scene dancing3
    "Zoey grabs my waist and starts moving her hips with mine."
    axel "Hahaha."
    "I feel a bit silly, but Zoey is so confident."
    "She steps back a little so I don't feel too awkward."
    "I let myself go and start moving with her."
    zoey "That's it!"
    scene dancingup
    "Other people join in and start dancing with us."
    axel "Woohoo!"
    "Zoey takes the chance to get closer and wraps her arm around my waist again."
    zoey "See? It's not so hard."
    name "You're definitely the life of the party."
    zoey "You have no idea."
    scene dancingcloserzoey
    "Zoey slides her hands down to my butt and pulls me against her."
    "I can feel her body pressed up against me."
    scene dancingcloserzoey6
    name "Whoa, what are you doing?"
    zoey "Don't you want to have a little fun?"
    name "Yeah, of course."
    zoey "Just relax and go with it."
    name "It's just that..."
    scene dancingcloserzoey
    zoey "Just move that cute little butt."
    zoey "Yeah, that's it."
    "I can't seem to resist her."
    "My body just follows her lead, almost without thinking."
    scene dancingcloserzoey6
    "I try to keep a bit of control, even as her hands squeeze my hips."
    "Part of me feels embarrassed for giving in so easily."
    "But I don't really want to stop her."
    scene dancingcloserzoey2
    "Zoey dances sensually close to me, giving me playful little slaps now and then."
    scene dancingcloserzoey5
    "I feel a bit shy."
    "But honestly, I like it."
    "Axel is probably laughing at me, but I don't really care."


    "We dance for three songs, and after a while, Zoey pulls me closer."
    zoey "Come on, let's go see Axel."
    "Zoey heads over to the couch and sits down."
    "Since there's no room left, she gestures to me."
    zoey "Come on, sit on my lap."
    scene dancingcloserzoey7
    name "Uh, okay."
    "I feel a bit shy, but we seem close now, so it doesn't feel as weird."
    axel "Hey, you two look like you're having fun."
    zoey "We were just dancing."
    axel "Yeah, I noticed."
    zoey "Don't you want to dance too?"
    axel "Nah, not really in the mood."
    zoey "You don't want to dance to my music."
    axel "That's not it..."
    zoey "Yeah, right..."
    zoey "You just wanted to put on your little indie music to show off."
    axel "Shut up."
    name "It's another way to flirt."
    zoey "I can already see her trying to impress the freshmen."
    axel "Pff, that's not my style at all."
    axel "Don't listen to her, [name]."
    zoey "Yeah, yeah, you think I don't see you?"
    zoey ""
    axel "Well, sometimes it helps to have good taste."
    zoey "Haha."
    zoey "Don't you want to dance then?"
    axel "I'd dance, but only if I get to pick the music."
    zoey "Oh wow"
    axel "It's fine, everyone is dancing to your music anyway."
    axel "You two really got the party going."
    zoey "Someone had to get things started."
    zoey "I didn't want to spend the whole night gossiping."
    axel "Yeah, you prefer to give people something to gossip about."
    zoey "Can't argue with that."
    "While we're talking, Zoey discreetly strokes the inside of my thigh."
    axel "Careful [name], Zoey's good at sweeping you off your feet before you even realize it."
    if gender == "male":
        zoey "Yeah, I think he likes it."
        zoey "Right, [name]? You like it?"
        name "Uh, yeah, it feels nice."
        zoey "See?"
    elif gender == "fem":
        zoey "Yeah, I think she likes it."
        zoey "Right, [name]? You like it?"
        name "Uh, yeah, it feels nice."
        zoey "See?"
    zoey "You look like a little kitten who loves being petted."
    zoey "Do you want me to make you purr?"
    name "Uh, what do you mean?"
    "Zoey leans in close to my ear."
    zoey "We could go upstairs to the bedroom."
    name "I don't know, I'd rather stay here a bit longer and enjoy the party."
    "Zoey presses her hand between my legs."
    "I don't really know what to say."
    "Especially with Axel sitting right there."
    "I'm not sure how to react."
    name "I think I'm going to get myself a drink."
    zoey "Don't go too far."
    "I slip out of Zoey's grasp and stand up."
    "I feel like I'm getting a bit of control back."
    $ zoeyaxelconv_count += 1
    
    jump kitchenparty
   
    

label kitchenzoeyconv:
        $ zoey_vestibul_asked == True
        scene vestibulearrowflou
        "As I leave the kitchen, I bump into Zoey waiting for me."
        zoey "Hey [name], I was looking for you."
        zoey "Feels like you're always keeping an eye on me."
        zoey "Maybe I should do the same."
        zoey "From now on, I'll just watch you."
        name "I have no idea what you're talking about."
        zoey "..."
        zoey "Ugh, I can't keep a straight face."
        zoey "You're just too cute."
        zoey "I just want to..."
        hug "Hey, what's up, guys?"
        hug "Who picked this music?"
        zoey "No idea, why?"
        hug "It's so basic."
        zoey "Hey, screw you."
        hug "Wait, was it you?"
        zoey "I just wanted to dance, and everyone loved my playlist."
        zoey "I set the mood."
        hug "Wow, I can't decide if I should apologize or just judge you."
        zoey "Why not both?"
        hug "I think I'll just judge you."
        hug "Come on, admit it wasn't that great, [name]."
        name "It was alright, I guess."
        zoey "Yeah, yeah, you looked like you were having fun dancing earlier."
        "Zoey gives me a playful slap on the butt."
        name "I was just trying not to hurt your feelings."
        zoey "Oh, you little brat."
        hug "See, you really do have terrible taste."
        hug "Alright, I'm going to see if I can find someone who knows if there's a projector here."
        zoey "You seriously want to watch a movie?"
        zoey "Don't even think about setting up in the bedroom."
        hug "Hey, leave me alone, it wasn't my idea."
        hug "I'll go ask Stephanie."


        name "Is he really going to watch a movie?"
        zoey "He's all over the place, that guy."
        name "He seems pretty funny."
        zoey "I'm funny too, you know."
        zoey "Hey, do you want to come upstairs with me?"
        name "Upstairs?"
        zoey "Yeah, I want to chill for a bit."
        name "I don't know, I was just starting to enjoy the party."
        zoey "Oh come on, don't be like that."
        zoey "Come upstairs with me."
        zoey "I want to show you something."
        name "What is it?"
        zoey "You'll see, it's a surprise."
        menu:
            "Go upstairs with Zoey":
                zoey "I knew you couldn't resist."
                "Zoey takes my hand and leads me to the stairs."
                "I follow her, a little nervous but also excited."
                jump zoeysscene
            "Maybe later":
                zoey "Alright, I'll wait for you. Don't take too long!"
                "I watch Zoey head back to the living room, and I take a moment to compose myself."
                jump livingroom
    


   
label zoeysscene:
        scene dancingcloserzoey8
        "Zoey leads me upstairs, her hand firmly holding mine."
        scene goingroomzoey
        "We reach the top floor, passing a few people chatting in the hallway."
        "Zoey opens the door to a bedroom and pulls me inside."
        "Some people glance at us and laugh as we go in."
        scene discoverroom2
        zoey "So..."
        zoey "Finally alone."
        "Zoey closes the door behind us, leaving us in the softly lit room."
        scene discoverroom
        "Elle allumes la lumière"
        "The room is cozy, with a big bed in the center"
        scene roomzoeyasking
        zoey "I wanted to talk to you for a bit."
        zoey "I feel like you've been avoiding me tonight."
        zoey "And I wanted to clear the air between us."
        name "Avoiding you? No, not at all."
        zoey "Anyway, I know you're shy."
        zoey "But I have to admit something."
        "Zoey looks me straight in the eyes."
        zoey "I have a thing for shy people."
        zoey "Honestly, I've been picturing you with my cock in your mouth all night."
        name "Wait, what?"
        "Zoey grins, her eyes full of mischief."
        zoey "Come on, don't you want to help me make that fantasy come true?"
        name "What do you want me to do?"
        zoey "Just close your eyes and let yourself go."
        "Zoey steps closer, her presence overwhelming."
        "She lowers her pants, revealing her cock, already hard."
        scene roomzoeyasking2
        "There's a faint scent of sweat and sex in the air."
        "It fills my senses, and my heart starts racing."
        "I try not to show how flustered I am."
        zoey "See what you do to me?"
        zoey "Come on, baby."
        zoey "Get on your knees."
        scene startbjzoey1
        "With one hand, she gently pushes me down, making me kneel in front of her."
        "She holds my head and brings it closer to her cock."
        name "Fuck, it's so big."
        zoey "Yeah, you'll definitely feel it."
        zoey "Put it in your mouth."
        scene startbjzoey2
        "I let her guide me and wrap my lips around Zoey's tip."
        "A salty, musky taste fills my mouth."
        "I swirl my tongue gently around her head, tasting her precum."
        zoey "I knew you wanted this too."
        zoey "You look so cute with my cock in your mouth."
        zoey "It really suits you."
        scene startbjzoeyv24
        "Zoey presses my head onto her cock, gradually pushing her tip inside."
        scene startbjzoeyv23
        "Then deeper and deeper into my throat."
        scene startbjzoeyv24
        "She moves my head back and forth on her cock."
        scene startbjzoeyv23
        "Forcing me to relax my throat to take her in."
        zoey "Yeah, that's it."
        zoey "You're really made for this."
        zoey "I hope you can hold your breath."
        zoey "I want to go even deeper inside you."
        scene startbjzoeyv22
        "With a thrust of her hips, she pushes her penis even further down my throat."
        "Making me gag and drool suddenly."
        scene startbjzoeyv23
        zoey "Relax"
        zoey "Just enjoy"
        scene startbjzoeyv24
        "Bracing herself with her strong legs,"
        scene startbjzoeyv23
        "Zoey thrusts into my mouth as if it were just a toy,"
        scene startbjzoeyv22
        ""
        scene startbjzoeyv23
        ""
        scene startbjzoeyv24
        ""
        scene startbjzoeyv23
        "Making me feel strangely small."
        scene startbjzoeyv22
        "Her cock seem to fill my entire world."
        scene startbjzoeyv23 
        "With every thrust, I feel her taking more and more control over me."
        scene startbjzoeyv24
        "I'm completely giving in to her, letting her do whatever she wants."
        scene startbjzoeyv23
        "Even though I'm struggling to breathe, I keep taking her deep in my throat."
        scene startbjzoeyv21
        "After a while, I pull back to catch my breath."
        
        name "Damn..."
        name "Your cock..."
        name "feels so good..."
        zoey "I know."
        scene bjzoeyv2
        zoey "Come on, suck me a little more. Then I'll take you from behind."
        scene bjzoeyv22
        zoey "You're going to love it."
        scene bjzoeyv23
        ""




        zoey "Tu veux savoir ce que j'ai prévu pour toi ?"
        name "Uh, yeah, I guess."
        name "What is it?"
        zoey "Just a little something I like to do when I'm in the mood."
       
        zoey "I like to have a little fun with my friends."
        zoey "And I think you're going to like it too."
        "Zoey walks over to the bed and sits down, looking at me with a playful smile."
        zoey "Come here, [name]."
        "I walk over to her, feeling a mix of excitement and nervousness."
        zoey "Don't be shy, I promise you'll like it."
        "Zoey pats the bed next to her, inviting me to sit down."
        name "Okay, I'm here."
        zoey "Good."
        zoey "Now, I want you to relax and enjoy the moment."  
       




        jump zoeyscene
