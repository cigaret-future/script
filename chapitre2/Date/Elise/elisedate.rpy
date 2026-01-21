define clara = Character('Clara', color="#ff7f7f")


label elisedate:


    scene elisestreet

    "A weird tension settles between us."
    "She finally breaks the silence."
    elise "So, what do you think of Sarah?"
    name "Hm, she's nice."
    name "I like her even though I don't know her that much."
    name "She has this kind of aura that makes you feel reassured."
    scene elisestreet2
    elise "Yeah..."
    elise "I understand why people would have this impression."
    name "She seems like she can be trusted, like an older sister."
    elise "That's just because she's a bit older."
    elise "It doesn't mean that she is more mature than you. Or me, for that matter."

    name "Yeah, I guess."
    "We walk through the streets for a few minutes."
    name "Is it far? You said it was close."
    elise "Yeah, we're almost there, don't worry."
    elise "Jeez, stop whining."
    name "My legs are tired."
    elise "Do you want these books or not?"

    scene elisestreet3
    "We arrive in front of a tall building."
    elise "It's here."
    "We enter the building and take the elevator."
    scene elevator
    "A silence sets between us."

    elise "I hope my roommate is not there."
    name "Oh, you have a roommate?"
    elise "Yeah, but she's not here often."
    name "I won't stay long."
    elise "No, it's ok, don't worry."
    name "Ok."
    scene entering
    "We enter her apartment."
    elise "Welcome to my place."
    scene eliseappartment
    "Elise's flat is small but cute."
    "I guess it's because she is close to the city center."
    name "Nice place."

    elise "Do you want something to drink?"
    elise "I have a beer if you want."
    name "I'd love a beer!"
    elise "Got it."
    scene sittingeric
    "I sit on the couch and look around."
    "I am not sure if I should ask her about the books right away."
    scene take a beer
    elise "Here, I don't have rooibos, sorry."
    name "No worries."
    scene so pose
    name "So..."
    elise "Yeah?"
    name "The books?"
    elise "Oh, right."
    elise "They are in my room."
    elise "Wait here."
    scene gogetbook
    "She goes to her room."
    "I have a weird feeling, but it's not unpleasant."
    ""
    "I don't know if I am really interested in her books."
    "I hear her rummaging through her things."
    "She comes back with a few books in her arms."
    elise "Here you go."
    name "Wow."
    scene readingwithelise
    "Elise sits on the couch with me, and we start to talk about the books."
    "She shows me the artist she prefers."
    "Suddenly, the door opens."
    scene enteringcolloc
    clara "Hello."
    clara "Oh, we have a guest."
    scene collocchatting2
    clara "I am Clara, nice to meet you."
    name "[name], same here."
    clara "What are you guys doing?"
    elise "I am giving away some books."

    clara "Oh right, the books..."
    clara "I don't think I've seen you before."
    name "Yeah, I am new here."
    name "I am Sarah's neighbor."
    clara "Oh right, I see."
    "Clara looks at the books."
    scene collocchatting
    clara "Are you getting rid of this one?"

    clara "I like it."
    elise "You can keep it if you put it in your room."
    clara "Mmh."
    name "Are you sure I can take them?"
    name "They are really nice."
    elise "Yeah! I am telling you, I need space in my room."
    name "I don't know if I will be able to carry them all."
    elise "You can pick some and come back later."
    name "Yeah, I guess."
    elise "You can come back whenever you want."
    clara "We can help you carry them if you want."
    clara "I could say hi to Sarah on the way."
    elise "Well."
    elise "You can drink your beer, [name]. You are not in a hurry, are you?"
    clara "Can I have a beer too?"
    scene closeupelise
    elise "No, you can't."
    clara "Why not?"
    elise "Because you have been naughty."
    clara "Oh no!"
    elise "Don't you have some stuff to do?"
    scene collocchatting3
    clara "Oh, I get it. I'll let you two enjoy your book club."
    elise "Finally, I thought I would have to be rude."
    scene collocleaving
    clara "Bye, guys!"
    elise "Bye, Clara!"

    elise "Let's move to my room, it's more chill."

    elise "And we won't be bothered by my roommate."
    "I'm not entirely sure how her roommate was bothering us, but I nod and follow her."
    "We enter her small bedroom, which feels more like an extension of the living room than a separate room."
    scene elisegettingbook with dissolve
    elise "Take a look at this."
    "She puts a large book on the bed."
    scene lookingbookroom
    name "Wow... this is special."
    elise "Yeah, just like you."
    name "Haha, stop it."
    "I flip through the pages absentmindedly."
    "I can feel Elise's gaze on me."
    "Suddenly, my phone buzzes."
    "It's a text from Sarah."
    s_nvl "Hey, are you at your apartment?"
    n_nvl "No, I'm out. Do you need something?"
    s_nvl "Oh, okay. No, don't worry. It was nice seeing you."
    s_nvl "I just wanted to see you real quick, but it can wait."
    n_nvl "I'll be back soon, I think."
    s_nvl "Alright, have a nice day :)"
    scene focuselise2
    elise "You and Sarah are texting?"
    name "I guess we are."
    name "How long have you known her?"
    elise "About a year and a half."
    name "What do you think of her?"
    scene focuselise3
    elise "Why do you ask?"
    name "Because you asked me earlier."
    elise "Well, she's nice. She's a good listener."
    elise "She's just..."
    name "What?"
    elise "Nothing."
    name "Okay..."
    elise "She's just not good at her job."
    name "Oh."
    name "And you think you would be better, I suppose?"
    scene focuselise2 with dissolve
    elise "Did you sleep together with Sarah?"
    name "What? No?!"
    elise "That's what I thought."
    name "Why do you ask?"

    elise "You know why."
    name "No, I don't."
    elise "You're not very good at this, are you?"
    name "At what?"
    elise "At pretending."
    name "I don't know what you're talking about."
    elise "You are so annoying..."
    scene focuselise with dissolve
    elise "I know you want me."
    elise "You can't deny it."
    name "I mean..."
    elise "Can't you tell I'm dying to fuck you?"
    name 'What?'
    elise "You try to play smart with me."
    elise "But deep down, I know you want me to fuck you silly."
    elise "Don't you?"

    menu:
        "Yes...":
            jump kiss_elise
        "What are you talking about?":
            jump step_back

    label kiss_elise:

        elise "Finally..."
        jump eliseassault

        # Continue the scene for kissing Elise

    label step_back:
        elise 'Admit it.'
        elise "You want me to put you into your place."

        menu:
            "I guess I am attracted to you too":
                name "Maybe we could go on a date first?"
                jump eliseassault
            "I am sorry, I am not interested":
                jump elisebackdown
        # Continue the scene for stepping back


    label elisebackdown:
        scene black
        elise "Oh."
        elise "That's awkward."
        name "I guess I should go then."
        elise "Yeah, I think so too."
        scene ericleaving
        "I get up and leave the apartment."
        jump map3


    label eliseassault:
        scene firstassault
        "Elise pounces on me, slamming me onto the bed."
        elise "You're really just a little whore."
        scene assault2
        elise "I'm tired of you pretending otherwise."
        elise "You won't even try to fight back."

        scene assault25
        elise "I know you want this."
        scene assault43
        elise "See? You're not even attempting to stop me."
        elise "I stripped you bare, and you just lay there, totally unbothered."
        elise "You little slut."
        scene assault5
        elise "Come here, I am gonna give you what you deserve."
        name "Hey, stop! Your roommate is next door."

        scene assault7
        name "Your dick is so..."
        name "Mmmph..."
        elise "Yeah, that's it."

        scene assault8
        elise "Your mouth serves a better purpose like this."
        scene assault12

        "Her cock was already glistening with pre-cum."
        "As soon as her cock slides past my lips, I feel my reservations melting away."
        elise "Yes, you like this, don't you?"
        name "Mmhmmph..."
        scene assault116
        elise "I knew you would be obedient."
        elise "Suck it!"
        elise "That's it."
        elise "Your tongue feels so good."

        scene assault117
        elise "Oh fuck..."
        elise "..."
        elise "Wait, stop, I can't cum in your mouth now."
        scene assault9
        elise "I want to have your ass first."
        elise "Turn around."
        scene black
        "Elise takes her clothes off, grabs my ass, and starts fucking me."

        scene elisevideo with Dissolve(2.0)
        $ renpy.pause(3, hard=True)

        name "Oh fuck!!!"
        name "Your dick..."
        name "Is..."
        name "So..."
        name "Nice."
        elise "Shut up."
        elise "Just take it."
        elise "Mh."
        elise "Take it."
        elise "I am gonna turn you into my slut."
        "I try to focus on my breathing."
        "But Elise is fucking me so hard."
        "I can't help but moan."
        show colloclistening with dissolve
        "Her roommate is probably hearing us."
        hide colloclistening with dissolve
        "But I am not sure I want Elise to slow down."
        elise "I'm going to ruin you for anyone else."
        elise "You won't be able to enjoy anything but my dick."
        elise "I'm gonna fill you up."
        "She starts moving again quickly, pumping in and out."
        "The wet, slapping sounds of the intense fucking echo in the room along with my heavy breathing and cries of pleasure."
        elise "Oh yeah."
        play sound spank volume 1

        if gender == "male":
            elise "You have been a naughty boy."
        elif gender == "fem":
            elise "You have been a naughty girl."
        elise "Trying to play innocent with me."
        elise "Trying to pretend you are..."
        elise "Interested..."
        elise "In my books..."
        play sound spank volume 1
        elise "When you just want your hole to be filled."
        elise "Like a little whore."
        elise "Say it."
        menu:
            "I am a little whore":
                name "I am a little... whore!"
                name "Please... fuck me."
                "Elise's enthusiasm escalates as she witnesses me capitulating to her authority, eager to claim me completely."
                "Impaling me on her shaft with increasing force and speed."

            "No!":
                elise "Don't worry."
                elise "At the end of this, you will be begging for more."

        "She fucks me like an animal."
        "Making me lose track of time."
        "At a certain point, Elise's pace quickens, becoming more frantic and urgent."
        "Her hips snapping forward with increased velocity."
        elise "Take it."
        elise "Oooh."
        elise "I am gonna cum..."
        scene final4
        elise "Fuuuckk....!!"
        "With one last hard thrust, Elise pushes all the way inside me, pressing against my deepest parts."
        "She stays buried deep as her cock throbs and jumps, getting ready to explode."
        scene test
        elise "Fuuuuck, take it all!"
        "Her hips jerking erratically as spurt after spurt of heavy jizz pumps into my spasming hole."

        "My stomach begins to swell slightly from the sheer volume of her release, my body struggling to contain the massive load."
        scene final2
        "Elise pulls out of my hole, a river of pearly white cum immediately beginning to leak out and trickle down on the bed."

        elise "You took my cock so well, like you were made for it."

        scene final7
        name "It was... so good."
        elise "We should probably get dressed and cleaned up."
        name "Can I take a shower?"
        elise "Nope."
        elise "I want you to carry my scent with you when you return home."

        scene black
        "As we both dress, the reality of the intense encounter starts to sink in."
        scene goingout2
        elise "Don't think I'm done with you yet."
        scene black
        "As I take the elevator, I feel a mix of confusion and arousal in my gut."
        "Elise's cum is dripping down my boxers."
        "I want to get fucked by her again."
        $ sarah_relation_status_text = "You can ask your new date to meet you by going to the coffee shop and buying a coffee."

        $ elise_sdate_done = True
        jump map3

    label elise_sdate:
        scene ericaskingagain
        elise "Well, well."
        name "Hi, Elise..."
        elise "What do you want?"
        elise "Say it."
        menu:
            "Please fuck me":
                jump elise_fuck
            "About those books...":
                jump elise_refuse

    label elise_refuse:
        scene black
        play sound "music/doorhome"
        ""
        "..."
        jump map3

    label elise_fuck:
        scene ericaskingagain
        elise "Finally."
        elise "Get in."
        scene black
        name "Elise... I..."
        play sound spank volume 1
        elise "Shut up."

        "Elise pushes me into her room."

        "She takes my clothes off, grabs my ass, and starts fucking me."

        scene elisevideo with Dissolve(2.0)
        show black
        $ renpy.pause(3, hard=True)
        hide black
        name "Oh fuck!!!"
        name "Your dick..."
        name "Is..."
        name "So..."
        name "Nice."
        elise "Shut up."
        elise "Just take it."
        elise "Mh."
        elise "Take it."
        elise "I am gonna turn you into my cumslut."
        "I try to focus on my breathing."
        "But Elise is fucking me so hard."
        "I can't help but moan."
        show colloclistening with dissolve
        "Her roommate is probably hearing us."
        hide colloclistening with dissolve
        "But I am not sure I want Elise to slow down."
        elise "I'm going to ruin you for anyone else."
        name "Ooooh fuck."
        name "I love you."
        elise "You won't be able to enjoy anything but my dick."
        elise "I'm gonna fill you up."
        "She starts moving again quickly, pumping in and out, chasing her climax."
        "The wet, slapping sounds of the intense fucking echo in the room along with my heavy breathing and cries of pleasure."

        "She fucks me like an animal."

        scene final4
        elise "Fuuuckk....!!"
        "With one last hard thrust, Elise pushes all the way inside me, pressing against my deepest parts."
        "She stays buried deep as her cock throbs and jumps, getting ready to explode."
        scene test
        elise "Fuuuuck, take it all!"
        "Her hips jerking erratically as spurt after spurt of heavy jizz pumps into my spasming hole."

        "My stomach begins to swell slightly from the sheer volume of her release, my body struggling to contain the massive load."
        scene final2
        "Elise pulls out of my hole, a river of pearly white cum immediately beginning to leak out and trickle down on the bed."
        elise "You took my cock so well, like you were made for it."

        scene final7
        name "It was... so good."
        elise "We should probably get dressed and cleaned up."
        name "Can I take a shower?"
        elise "Nope."

        scene black
        "As we both dress, the reality of the intense encounter starts to sink in."
        scene goingout2
        elise "Don't think I'm done with you yet."
        scene black
        "As I take the elevator, I feel a mix of confusion and arousal in my gut."
        "Elise's cum is dripping down my boxers."
        $ elise_sagain_done = True
        $ sarah_relation_status_text = "You can ask your new date to meet you by going to the coffee shop and buying a coffee."
        "I want to get fucked by Elise again."
        jump map3

label elisesachadate:
    scene cafeelisesachaeric11
    "We arrive at the place"
    sac "It's here"
    sac "I see Elise, she is on the corner"
    sac "Go ahead, I'll order."
    name "Get me a long coffee."
    sac "Got it."
    if camillelove_count >= 3:
        "I see a familiar face."
        "It's Camille."
        name "Hey! What are..."
        play sound "audio/music/spank.mp3" volume 1.0
        # "Camille passes by me and slaps me on the ass."
    
    scene cafeelisesachaeric14 with dissolve
    elise "hey [name]"
    "Elise gives me a seductive look"
    if camillelove_count >= 3:
        elise "I saw that girl slap your ass."
        elise "what was that?"
        name "Nevermind, she's someone from my class, she likes to tease me."
        elise "Looks like you're really enjoying college!"
    scene talkingsachaericelise with dissolve
    "Sacha is telling Elise about his problems at work."
    "Elise listens, but she seems a bit distracted."
    "She’s acting kind of strange."
    "I wonder what their relationship is like."
    
    scene cafeconv2 with dissolve
    "She seems more focused on trying to catch my eye"
    sac "I’m thinking of checking out the organic shop that just opened near me."
    sac "They seem cool, and I might be able to grab some unsold stuff."
    name "Yeah, sounds like a good idea."

    scene cafeconv2cut8 with dissolve
    elise "But I don’t get how that guy is running the place."
    elise "Can’t you talk to the owner and tell him this guy has no clue what he’s doing?"
    sac "Pfft, I’m pretty sure they’re either friends or family."
    elise "You should at least try. Who knows, maybe the owner would appreciate hearing his manager is a jerk."

    scene cafeconv2cut10 with dissolve
    "I feel Elise’s leg brushing against mine."
    "I wonder if she’s doing it on purpose."

    scene cafeconv2cut8 with dissolve
    elise "If I were you, I’d try to take advantage of the situation and aim for his position."
    sac "Yeah, I don’t think I want to manage that place."
    sac "They’re probably drowning in debt anyway."
    sac "And honestly, I’m not sure I’d want to work that much."

    scene cafeconv2cut16 with dissolve
    "As we continue talking, her foot keeps brushing against my leg."
    "It’s..."
    "Her cold toes touch my skin."
    "I feel a small knot in my stomach."

    scene cafeconv2cut14 with dissolve
    elise "And what’s that?"  
    name "What?"  
    name "Oh, that?"  
    name "It’s a photo book I picked up at the bookstore."  
    name "Not sure if it’ll actually help, but it looked interesting."  

    scene cafeconv2cut13 with dissolve  
    elise "Oh, for your thesis?"  
    elise "I’ve got some books like that at home."  
    elise "If you want to check them out."  
    name "Like that? What do you mean?"  
    elise "You know, fancy photography books."  
    elise "I think I have a few lying around."
    scene cafeconv2cut19 with dissolve
    elise "I can lend them to you if you’d like."  
    elise "I haven’t had much time to read them anyway."  
    elise "But you’ll have to come by my place to grab them."  
    elise "I’m not going to carry them around."  
    name "Sure... thanks. I’ll stop by sometime."  
    elise "Cool."  

    scene cafeconv2cut14 with dissolve
    elise "..."

    if gender == "male":
        sac "I’m showing him around the city a bit."
        elise "He doesn’t show it, but I’m sure he’s excited to explore."

    elif gender == "fem":
        sac "I’m showing her around the city a bit."
        elise "She doesn’t show it, but I’m sure she’s excited to explore."

    name "Yeah, I am!"
    scene cafeconv2cut13 with dissolve
    name "I’m just trying to adapt."
    name "There are so many things I don’t fully understand yet."

    scene cafeconv2cut14 with dissolve
    sac "You’ll get used to it."
    scene black with dissolve
    "We continue to talk for a while until"
    "Our conversation blends with that of the other people in the bar"
    "I am having a good time."
    scene standingupsachaelise
    sac "Well, I’m heading out."
    name "Me too"
    elise "alright i follow you guys"
    sac "I'm inviting you"
    name "Thanks"
    scene goinghomesachaeliseout
    elise "hey, you forgot your book"
    name "oh thanks"
    name "thanks for the coffee Sacha"
    sac "No problem, see you soon"
    name "see you"
    $ sarah_relation_status_text = "I should hang out to the coffee shop"
    $ sarahcafe_conv2_done = True
    $ sarah_cafe = False
    $ sarah_conv_done = True
    $ sacha_conv_done = True
    
    jump map3
    


    jump cafedirection






    #