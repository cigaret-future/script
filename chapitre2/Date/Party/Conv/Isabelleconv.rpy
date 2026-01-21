

label isabelleconv:
    default isabelleconvbourre_done = False

    if isabelle_date_done == True:
        jump isabelleconv5
    elif isabelle_proposal_refused == True:
        jump isabellesecondchance
    elif drink_count >= 5 and isabelleconvbourre_done == False:
        jump isabelleconvbourre1
    elif drink_count >= 5 and isabelleconvbourre_done == True:
        jump isabelleconvbourre2


    elif isabelleconv_count == 0:
        jump isabelleconv1 
    elif isabelleconv_count == 1:
        jump isabelleconv2
    elif isabelleconv_count == 2:
        jump isabelleconv3
    elif isabelleconv_count == 3:
        jump isabelleconv3b
    elif isabelleconv_count == 4:
        jump isabelleconv4


    label isabelleconvbourre1:
        scene vestibulearrowflou
        show test044 with dissolve
        show hugolaugh at right:
            xalign 0.7
        "The alcool is starting to have it's effect on me.."
        name "I'm so happy to be here."
        name "Everyone around me seems so nice."
        hug "Yeah, it's true, it's pretty cool."
        isa "You really like to party, I can tell."
        isa "I've seen you shaking your butt for a while now."
        

        isa "He really looks like someone who wants to let loose."
        hug "Go all out, [name], you only live once, right?"
       
        
        name "YAAAAS! Tonight, I'm a party tornado!"
        hug "Hahaha, [name] is on fire."
        show hugopartydrunk at right with dissolve:
            xalign 0.7
        
        hide hugolaugh with dissolve
        hug "It's time to ceeeeelebraaate!"
        show isabellegossip with dissolve
        hide test044 with dissolve
        isa "Come on Hug, you're not that drunk...."
        isa "I know you. Stop pretending"
        isa "Don't start acting all bro"
        show hugolaughsorry2 at right with dissolve:
            xalign 0.7
        hide hugopartydrunk with dissolve

        hug "I know, but [name] inspires me. I think I'm going to put my good resolutions aside for tonight."
        isa "Wow, it didn't take much for you."
        show isabellelaugh4 with dissolve
        hide isabellegossip with dissolve
        
        isa "All it takes is a drunk [name] for you to let loose?"
        hug "Haha, look at him, he looks like he drank a whole barrel of beer."
        name "Come on guys, I'm not that drunk."
        name "I'm just a little warm, that's all."
        isa "You are so drunk, [name]."
        hug "Come on, stop patronizing him."
        hug "I'm going to get a drink."
        isa "Get me a drink too, pour me some gin."
        hug "Of course, baby."
        isa "Don't call me baby."
        "Hugo goes to the kitchen to get drinks."
        hide hugolaughsorry2 with dissolve
        if stacymelanieconv_count < 1 or stacymelanieconv_count > 2:
            hide hugov2 with dissolve
            show isabelleteasing with dissolve
            hide isabellelaugh4 with dissolve
            "Isabelle looks at me and smiles."
            isa "So, [name], are you having fun?"
            name "a lot!"
            isa "You know what? I think you've unlocked some kind of party beast mode."
            name "Party beast mode? I like that!"
            name "Rawr! I'm the party beast!"
            
            "I make exaggerated claw gestures."
            hug "Oh no, we've awakened a beast!"
            isa "A very intoxicated beast who thinks he's intimidating."
            name "I'm not intimidating, I'm... magnificent!"
            name "Like a party unicorn!"
            isa "From beast to unicorn in mere seconds, quite the transformation."
            hug "A party unicorn who struggles to stay upright."
            name "Unicorns don't need to stay upright, they glide!"
            "I attempt to demonstrate gliding by walking on my tiptoes, nearly losing my balance."
            isa "Oh my goodness, you're going to injure yourself."
            isa "Come here, party unicorn, before you tumble and damage your horn."
            "Isabelle grabs my arm to steady me."
            name "My horn is unbreakable!"
            hug "Your horn is saturated with alcohol"
            isa "Speaking of poor choices, perhaps we should relocate this discussion somewhere he can fly."
            name "Fly? I like the sound of that."
            hug "Let's go!"
            "We head toward the living room, Isabelle holding me by the waist, pretending to support me."
            "She takes the opportunity to slip a hand under my shirt."
            scene hugodancingalone
            "Hugo starts dancing by himself."
            isa "Yeah, go Hugo!"
            isa "Look at him."
            isa "He's as drunk as you."
            scene hugodancingalone2 with dissolve
            name "Yeah, but he's not as magical as me."
            isa "I know."
            isa "Let me see just how magical you are."
            scene ericdansingisabelle with dissolve
            "Isabelle takes me by the waist and begins dancing with me."
            "The three of us start dancing wildly together."
            "The others join us after a moment."
            "A crowd forms around us."
            "Isabelle presses closer and closer to me."
            "I can feel the warmth radiating from her body."
            isa "You're really getting into it..."
            isa "I never would have guessed you had these moves."
            name "I'm full of surprises."
            isa "That you are."
            isa "My little party unicorn."
            hug "Hey, quit the flirting and dance with me!"
            isa "Go find your own dance partner."
            isa "Haha, such a third wheel."
            isa "I'm keeping this one to myself."
            name "Since when did I become your personal property?"
            isa "Just for tonight."
           
            "Isabelle leans in and kisses me softly."
            "I catch a hint of her desire in the air."
            "I can tell she wants me."
            "We keep dancing, our bodies pressed close."
            "Every now and then, Isabelle brings a drink to my lips."
            "The alcohol is starting to hit me."
            scene ericdansingisabelle3
            "Isabelle slides behind me, her hips moving against mine."
            "The alcohol makes me feel bold, uninhibited."
            "I move with her, matching her rhythm."
            scene isabellebumping4 with dissolve
            window hide 
            pause
            scene isabellebumping3 with dissolve
            window hide 
            pause
            scene isabellebumping4 with dissolve
            window hide 
            pause
            scene isabellebumping3 with dissolve
            window hide 
            pause
            isa "You know, I have a penis."
            name "Yeah, I kind of figured."
            isa "I need to tell you something.."
            scene isabellewhispering
            "She moves closer to my ear."
            "Her breath on my neck makes me shiver"   
            isa "There is this things i wanted to do for a while."
            if gender == "male":
                isa "I've always fantasized about having a guy go down on me at a party."
            
            elif gender == "fem":
                isa "I've always fantasized about having a girl go down on me at a party."
        
            "I listen to her silently, holding my breath"  
            if gender == "male":
                isa "Especially if I don't know him very well."
            elif gender == "fem":
                isa "Especially if I don't know her very well."
            isa "You know what I mean?"
            name "Uh yeah, I think so."
            scene isabellewhispering
           
            isa "You know, like feeling someone's mouth on my dick."
            isa "Right after he was just talking to me a few minutes ago, saying boring things."
            isa "Telling me what he did this summer."
            isa "Or what kind of music he likes to listen to."
            "While speaking, Isabelle continues to move against me."
            "Pressing closer and closer to me" 
            isa "Want to find somewhere quieter?"
            isa "Just the two of us?"
            name "Yes... That would be nice."
            scene livingroomarrowflou
            "Isabelle takes me by the waist and we slip away from the crowd."
            "We go upstairs."
            isa "Haha, watch out not to fall."
            isa "Come on. Let's try to be discreet."
            "We arrive upstairs."
            "Isabelle leads me into the toilet."
            scene firsteric3
            isa "Finally alone."
            name "The toilet? Seriously?"
            "I groan, but the protest dies in my throat as she slams the door shut behind us, caging me in."

            if gender == "male":
                isa "Good boys get beds."
            elif gender == "fem":
                isa "Good girls get beds."
            isa "But you?"
            isa "I want to make you filthy."
            
            $ isabelledanse_done = True
            jump isabelledate
            


        
        hide hugov2 with dissolve
        show isabelleteasing with dissolve
        hide test044 with dissolve
        "Hugo walks away to the kitchen, laughing"
        isa "I can't believe you're this drunk already."
        isa "You really wanted to party, huh?"
        name "Yeah, I mean, I never really had the chance to party where I used to live."
        isa "Too bad I'm not in college anymore, I would have loved to party with you."
        hug "Hey guys, come get your drinks"
        isa "He is calling us?"
        name "We are coming"
        "We find ourselves in the kitchen, chatting with the people there."
        "The atmosphere is cool and relaxed."
        "Talking with people makes me feel less numb from the alcohol."

        "I feel more connected to the moment."

        scene kitchenpartyisafinale
       
      

 
        tra "This music instantly takes me back to the past."
        tra "I remember such specific things when I listen to it."
        tra "It's weird."
        name "Like what?"
        tra "Like silly things, like what position I was in when I heard the song."
        tra "Or whether I was having a good day or not."
        tra "It's weird, right?"
        isa "A little, but at the same time I think I get it."
        isa "I really get that with smells."
        name "Yeah, me too, I think."
        name "I read somewhere that smells and sounds leave a much stronger impression on us than visuals."
       
        tra "Yeah, I think I read that too."
        tra "It's because hearing and smell are directly connected to the limbic system."
        name "Wow, really?"
        name "So they're kind of more primitive senses?"
        tra "Exactly."
        $ isabelle_balconyparty_done = True
        tra "They're deeply connected to our instincts."
        tra "And now, they're also strongly linked to our emotions."
        name "That's really interesting."
        name "I love learning about how the brain works."
        name "I was pretty good at biology, I always found this stuff fascinating."
        tra "Yeah, it really feels like you're getting closer to the mysteries of life."
        isa "The mysteries of life..."
        isa "Yeah..."
        isa "Well, the mysteries of life aren't that complicated, we're all here to reproduce."
        isa "At some point, you have to stop overthinking it."
        tra "That's kind of a weird way to see it..."
        tra "Do you want to have kids?"
        isa "Me? No, not at all."
        isa "I love my independence too much."
        tra "Me too, I'm not ready to have kids."
        isa "But I like the idea of being able to have them if I want."
        name "Like, at any moment, you want to be able to reproduce."
        isa "Exactly. haha"
        isa "Even now."
        "Isabelle gives me a knowing look."
        tra "I think I get it."
        hug "Hey, have you seen that show, it's like a reality TV show where they just party all the time?"
        hug "What's it called again?"
        hug "It's something like 'temptations room' or something like that."
        tra "'Temptation room?' haha what is that?"
        name "'Temptations rules'?"
        hug "Yeah, that's it, and they're always playing games."
        isa "I can totally see you on that show."
        hug "Yeah, I'd totally fit in. Party, games, drama... that's my thing."
        tra "It's so weird to be filmed all the time."
        name "I think some people actually get excited by that."
        hug "I wouldn't mind it."
        name "See? Hugo would like that."
        hug "Also, I'd do it for the money."
        hug "If I got paid for that, I'd do it every day."
        tra "I don't understand how you can be so comfortable with that."
        isa "You don't get it? He just wants people to see him having sex, he's an exhibitionist!"
        isa "He loves it when people look at him."
        hug "Exactly."
        isa "Haha, look, he's proud of himself, he thinks it's a compliment."
        "The evening goes on quietly, we chat while drinking."
        "..."


        scene balconyparty
        "After a while, we end up on the balcony, singing along to a song."
        "Isabelle often grabs me by the waist, trying to make me dance with her."
        
        isa "Hey, this balcony is great, isn't it?" 
        name "Yeah, it's nice."
        isa "You look like you're ready for anything."
        isa "Do you have your eye on someone?"
        name "No, I'm just enjoying the moment"
        isa "Liar, I'm sure you're in hunter mode right now."
        isa "You're looking for someone to take home."
        name "Are you talking about yourself?"
        isa "ahahah"
        isa "I'm not really in the mood to bring someone home tonight."
        isa "I have other ideas."
        name "Like what?"
        isa "You'll see."
        name "Are you going to try to hit on me?"
        isa "Pff... you're not that great."
        name "Oh really?"
        isa "ahah, I'm kidding."
        isa "You're cute."
        isa "You have a nice butt"
        name "Thanks, I guess."
        isa "Don't you have a girlfriend?"
        name "Yeah, well, it's complicated."
        name "She lives in my old town."
        name "We talk from time to time by message."
        isa "That's complicated."
        isa "Aren't you afraid she'll cheat on you?"
        name "No, strangely enough."
        isa "Maybe you'll be the one to cheat on her, haha."
        name "We'll see."
        isa "ahahah."
        tra "What are you two talking about?"
        isa "Nothing, nothing, we were just talking about relationships."
        hug "Hey Isabelle, do you remember the guy who used to play piano at college?"
        isa "What?.."
        hug "I think he lives across the street, look."
        isa "Are you spying on people now?"
        "Isabelle joins Hugo."
        scene balconyparty2flou with dissolve
        show tracy3 with dissolve
        "Tracy comes closer to me"
        tra "Do you know Isabelle?"
        name "No, we just met."
        tra "Ah, okay!"
        tra "Usually I have trouble meeting new people, but you all seem nice."
        name "Same, the alcohol helps a bit."
        tra "Yeah, I can see that."
        tra "You look pretty relaxed."
        name "I feel a bit like I'm in a fridge."
        name "But a warm fridge."
        tra "Like in a saucepan?"
        name "Exactly, like someone is slowly cooking me."
        tra "Haha, I hope this person is a good cook."
        name "I have to be careful not to let myself get too cooked."
        tra "Yeah, it's not good when it's overcooked."
        name "I think he's a little drunk."
        tra "Do you want to drink some water?"
        name "I think I'm okay, haha."
        tra "I'm a little drunk too."
        tra "I hope I won't say too many stupid things."
        
        name "Don't worry. You are not stupid."
        tra "Thanks."
        "Isabelle comes back to me, taking me by the waist again"
        isa "Hey, can i tell you something?"
        name "Of course, what's up?"
        isa "You know, I have a penis."
        name "Yeah, I kind of figured."

        if gender == "male":
            isa "I've always fantasized about having a guy go down on me at a party."
           
        elif gender == "fem":
            isa "I've always fantasized about having a girl go down on me at a party."
       
        name "okay?"
        if gender == "male":
            isa "Especially if I don't know him very well."
        elif gender == "fem":
            isa "Especially if I don't know her very well."
        isa "You know what I mean?"
        name "Uh yeah, I think so."
        "She moves closer to me and whispers in my ear."
        isa "You know, like feeling someone's mouth on my dick."
        isa "Right after he was just talking to me a few minutes ago, saying boring things."
        isa "Telling me what he did this summer."
        isa "Or what kind of music he likes to listen to."
        $ isabelle_fantasme_told = True
        name "You mean I'm boring you?"
        isa "No you are amazing."
        name "I know."
        isa "Hey, you're not supposed to say that."
        
        "Hugo starts mocking the neighbors who ask him to be quieter."
        hug "Hey, you shut up, we're having a party here!"
        hug "If you don't like it, go to bed!"
        isa "omg Hugo shut up hahaha"
        isa "We won't be able to come back here after this."
        hug "He started it! He told me to 'shut up'!"
        isa "I hope she didn't hear us."
        "Isabelle glances into the kitchen."
        hug "Don't worry, she's probably too busy with her boyfriend."
        isa "I think she heard you."
        name "I'm going to go check."
        tra "Yeah, I'll come with you."
        tra "I'm good at talking sense into people."
        name "Okay, let's go."
        scene livingroomarrowflou
        "We go back to the entrance. People seem to have heard Hugo but are taking it pretty lightly."
        name "I don't see her."
        tra "Maybe she went upstairs?"
        name "Yeah, come on, let's go see."
        "We head upstairs."
        "Some people have gathered on the first floor."
        name "Well, I think it looks fine."
        name "We'd hear her, I think."
        tra "You're right."
        tra "Come on, let's go into the bedroom to check."
        scene tracyroom
        "We arrive in the bedroom, the light is on but no one is there."
        name "Wow, do you think this is her room?"
        tra "It's her parents' room, isn't it?"
        name "Oh, her parents live with her?"
        tra "I think so, Melanie told me she lives with her parents."
        name "Oh yeah, look, there are pictures of them."
        scene tracyroom2
        tra "Hey, don't look at that, it's too weird."
        name "No, look, they seem nice."
        name "They went to Egypt, obviously."
        tra "I feel like I'm in someone else's memories."
        name "They're cute."
        name "And that's the girl who invited us."
        tra "Yeah, she seems less nice than her parents."
        name "Maybe she's adopted."
        tra "Haha, don't say that, that's mean."
        name "But it's true, she doesn't seem to have the same personality as them at all."
        name "You don't get to choose your kids."
        tra "That's true."
        tra "But you can choose your friends."
        "We keep looking at the photo"
        name "So, are you dating Melanie?"
        tra "What? No, not at all..."
        name "It's just that you two seem close."
        "Tracy looks uncomfortable"
        tra "Ah, no, we're just friends..."
        name "Close friends?"
        tra "Yeah, let's say that."
        tra "Close friends..."
        tra "But I'm not in love with her."
        tra "Well..."
        name "Oh, so you're really close close friends then."
        name "Haha, I didn't get that."
        tra "Yeah well, it's complicated."
        name "You don't have to tell me if you don't want to."
        tra "No, it's fine, it's just that sometimes I feel like she doesn't understand me."
        tra "We're very different."
        tra "You probably noticed that."
        name "Yeah, but that's also what's nice about it."
        tra "Yeah, that's true..."
        tra "But sometimes I wish she was a bit more like you... uh, I mean like me."
        tra "Well, you know what I mean."
        name "Haha, yeah, I get it, don't worry."
        "Suddenly Tracy turns to me and looks me straight in the eyes."
        "She moves closer to me and kisses me."
        scene kisseric
        "I'm surprised, but I don't pull away."
        "I feel her soft lips against mine, and I let myself get carried away by the moment."
        "Tracy pulls back and looks at me, a shy smile on her lips."
        scene kisseric2
        tra "Sorry, I just wanted to kiss you."
        name "Oh, uh, no problem."
        tra "It's the alcohol."
        tra "I'm not usually like this."
        name "What do you mean, not usually like this?"
        tra "ahah, you know."
        scene kisseric
        "Tracy kisses me again."
        tra "I'm so drunk ahah"
        name "It's okay."
        "I don't mind."
        "As she kisses me, I feel a pain in my lower belly."
        "Like a pressure being released."
        "Suddenly, I really need to pee..."
        "Wtf..."
        name "Wait, I need to go to the toilet, can you wait for me here?"
        tra "Oh sure, go ahead."
        tra "Don't worry."
        scene corridorscreenfloutracy
        "I leave the bedroom and go straight into the toilet next door."
        scene ericpeeing
        "I realize that I'm a bit drunk too."
        "Maybe I should have waited?"
        "No, I would have needed to go anyway."
        "I'm not sure why she kissed me."
        "It was a bit weird, but oh well."
        "She seems like a cool person."
        "I just hope it won't cause any drama with Melanie."
        "Oh well."
        scene isabelleintercept
        "As I come out, I bump right into Isabelle."
         
        isa "Hey, what are you doing?"
        name "Nothing, I was just peeing."
        isa "So, is the owner mad?"
        name "No, not at all."
        name "We didn't run into her after all."
        isa "Oh, and you stayed here?"
        name "Yeah..."
        isa "What are you two up to?"
        name "Nothing, nothing."
        "Isabelle looks me straight in the eyes, without saying anything."
        name "What?"
        isa "Are you two together or what?"
        name "What are you talking about?"
        "Isabelle tries to push me into the bathroom"
        menu: 
            "Resist and go back to the bedroom.":
                $ isabelle_proposal_refused = True
                jump tracydate
            "Let her do it (I know where this is going)":
                
                jump isabelledate

            
 



   







        # isa "Yeah, I stopped drinking whatever people hand me here. I like to know what I'm getting into."
        # name "Seems like you've got everything under control."
        # isa "More or less. Like right now, I'm thinking I'm wasting my time talking in this noisy room... when there's a much quieter one in the back. Like... really quiet."
        # name "Oh yeah? Quiet like... you want to talk philosophy or...?"
        # isa "No. I was thinking more... just the two of us. If you're up for it."
        # name "Yeah, well... yeah, I'd like that. Should I follow you?"
        # isa "Cool."

        # "You start walking toward the hallway."

        # "Off-screen voice" "Hey Isa! Jules is looking for his charger — have you seen it?"
        # isa "No. He asks me that at every party. Tell him to buy a real phone."
        # name "Seems like you're used to dealing with drunk people."
        # isa "Yeah, but tonight I've got something else on my mind. You coming?"
        # name "Yeah... yeah, I'm coming."

    label isabelleconv2:
        scene vestibulearrowflou
        show test044 with dissolve
        show hugov2 at right:
            xalign 0.7
        isa "hey [name], you look like you're having a good time."
        name "Yeah, I am."
        show hugoplanningsomething at right with dissolve:
            xalign 0.7
        hide hugov2 with dissolve
        hug "Do you think I have a shot with Abby?"
        name "I don't know who that is."
        show isabellegossip with dissolve
        hide test044 with dissolve
        isa "She's a girl who looks a lot like him."
        isa "And no, he doesn't have a chance with her."
        isa "I already told you, you two would look like brother and sister."
        isa "It would be weird."
        hug "Yeah but she is hot."
        isa "She is, but that's not the point."
        hug "But isn't it the dream to date your own clone?"
        isa "No, not at all."
        name "I think it's hot."
        hide hugoplanningsomething
        show hugov2 at right with dissolve:
            xalign 0.7
         
        hug "Yeah you get it [name]."
        hug "It's the best thing to do."
        show isabelleneutral2 with dissolve
        hide isabellegossip with dissolve
        isa "You guys are weird."
        show hugorealizingsomething at right with dissolve:
            xalign 0.7
        hide hugov2 with dissolve
        hug "It's not weird, wouldn't you want to date your clone?"
        isa "No..."
        show isabellegossip with dissolve
        hide isabelleneutral2 with dissolve
        isa "I mean, maybe if we lived on an island..."
        isa "No I just pictured it, it would be weird."
        show hugopowerfull at right with dissolve:
            xalign 0.8
        hide hugorealizingsomething with dissolve
        hug "Wait are you saying that dating your twin on an island is weird?"
        show isabelleteasing with dissolve
        hide isabellegossip with dissolve

        isa "Yes that's what i am saying Hugo.."
        hug "Wooww..."
        hug "you are so close minded..."
        hug "It might even be oppressive for some people"
        hug "Have you think about twins that date each other?"
        show isabellesmug with dissolve
        hide isabelleteasing with dissolve
        isa "I am not saying this should be illegal."
        hug "I am going to make a post on twitter about this."
        hug "To say how close minded you are."
        isa "shut up, i am not."
        isa "Do your post, i don't care."
        hug "I will..."
        show hugorealizingsomething at right with dissolve:
            xalign 0.8
        
        hide hugopowerfull with dissolve 
        hug "'Isabelle thinks that twins that dated eachother should be in prison'"
        isa "Why not tortured will you at it."
        hug "'And tortured'"
        isa "Sure"
        name "You guys are funny."
        
        isa "Should'nt we be dancing instead of talking non sense?"
        show hugolookingtowardthelivingroom at right with dissolve:
            xalign 0.8
        hide hugorealizingsomething with dissolve
        hug "Yeah that's true."
        hug "But i feel like drinking a bit more before."
        show isabelleteasing with dissolve
        hide isabellesmug with dissolve
        
        isa "Yeah, me too."
        hug "Hey [name], if you want to grab a beer there are some in the kitchen."
        $ isabelleconv_count += 1
        jump vestibule
       

    label isabelleconv3:
        scene vestibulearrowflou
        
        show hugov2 at right with dissolve:
            xalign 0.7
        show isabellesmile with dissolve
        hide test044 with dissolve
        hug "So [name], what kind of people are you looking for here?"
        name "I don't know, I guess I'm just looking to meet new people."
        hug "Yeah, but do you have a type?"
        name "hmm."
        name "I guess I like... confident people."
        hug "Confident people, huh?"
        show isabelleteasing with dissolve
        hide isabellesmile with dissolve
        isa "So you like people who know what they want and go for it?"
        name "Yeah that's it."
        isa "Well then, you're in luck.."
        show hugolookintatthesky at right with dissolve:
            xalign 0.7
        hide hugov2 with dissolve
        hug "Yeah, you're in luck, because I'm the most confident person I know."
        hug "Never met someone as confident as me."

        name "ahahah I think you know I am not gonna date you."
        show hugoplanningsomething at right with dissolve:
            xalign 0.7
        hide hugolookintatthesky with dissolve
        hug "Why not?"
        hug "Like I said, most confident person in the room."
        name "I'd rather we just be friends, Hugo."
        show hugolaughsorry at right with dissolve:
            xalign 0.7
        hide hugoplanningsomething with dissolve
        hug "Friends? That's it huh?"
        name "Sorry Hugo.."
        show hugolaughsorry2 at right with dissolve:
            xalign 0.7
        hide hugolaughsorry with dissolve
        hug "Ouch."
        hug "I thought we had something special."
        hug "You are really breaking my heart here."
        hug "I thought we were going to be the new power couple of the century."
        show isabellelaugh4 with dissolve
        hide isabelleteasing with dissolve
        isa "You are not his type."
        isa "He likes people who are more... how can I put it... less weird."
        hug "Like you?"
        show isabelleneutral3 with dissolve
        hide isabellelaugh4 with dissolve
        isa "I mean, I am weird too in some ways."
        name "We are all weird in our own way."
        isa "But I think I am weird in a good way."
        show isabelleteasing with dissolve
        hide isabelleneutral3 with dissolve
        isa "If you know me enough, it can become enjoyable."
        show hugorealizingsomething at right with dissolve:
            xalign 0.7
        hide hugolaughsorry2 with dissolve
        hug "wow that sounds interesting."
        hug "You're hiding things from me, Isa."
        isa "If only you knew..."
        isa "Maybe [name] will discover them tonight."
        show hugolaugh at right with dissolve:
            xalign 0.7
        hide hugorealizingsomething with dissolve
        hug "Oh oh..."
        hug "You are in trouble."
        name "ahah I don't mind."
        $ isabelleconv_count += 1
        jump vestibule
    
    label isabelleconv3b:
        scene vestibulearrowflou
        "I approach Isabelle and Hugo, but Isabelle steps forward and takes me aside."
        "Hugo looks at me with an amused look."
        "Then he walks away to the kitchen, leaving us alone."

        show test044 with dissolve
        "Isabelle steps closer, close enough that I can smell her perfume."
        isa "Don't mind Hugo.. he is just..."
        isa "He is just in a mood to joke about everything."
        name "Yeah, he's funny"
        isa "yes.. "
        isa "So you are new here in this city.. "
        name "Yeah, I just moved here."
        name "It's a bit overwhelming, I'm not gonna lie."
        name "I'm trying to find my bearings"
        isa "Yeah life in the city can be intense."
        isa "All these people..."
        isa "When I arrived here, I thought the same thing"
        name "and people have a very fluid way of approaching relationships."
        isa "Yes"
        isa "But you get used to it quickly."
        isa "It's a matter of rhythm."
        name "Yeah, rhythm I see"
        isa "You have to be with people who put you in the rhythm."
        isa "And then it all flows by itself."
        name "Yeah, for now I feel like I have acquaintances that are a bit scattered."
        isa "It can be just one person too.."
        isa "You know, sometimes all it takes is a somewhat revealing moment."
        isa "And you integrate the rhythm."
        isa "Just let you go.."
        show isabelleteasing with dissolve
        hide test044 with dissolve
        isa "I'll show you if you want."
        name "You're going to show me?"
        isa "Yes"
        name "What are you going to show me?.."
        isa "ahahah.."
        isa "You are asking too many questions"
        "She lightly touches my arm while speaking."
        isa "Let's just say I'd like to get to know you better."
        "Her hand lingers on my arm a moment longer than necessary."
        name "What do you want to know?"
        isa "Things.."   
        isa "You have decide to making this hard on me do you?"
        name "ahahah.. sorry"
        show isabellesmile with dissolve
        hide isabelleteasing with dissolve
        isa "Don't be sorry, just let me take the lead."
        
        show hugov2 at right with dissolve:
            xalign 0.7
        hug "Hey guys, what are you talking about?"
        "Hugo comes back from the kitchen with a drink in hand."
        "Isabelle steps back a little from me and glances at Hugo"
        show isalookleft with dissolve
        hide isabellesmile with dissolve
        $ isabelleconv_count += 1
        isa "oh you know.. just a nice chill conversation between the two of us.."
        isa "..that you just interrupted."
        jump vestibule



    label isabelleconv4: 
        scene vestibulearrow
        scene vestibulearrowflou with dissolve 
        show test044 with dissolve

        show hugoserious at right with dissolve:
            xalign 0.7
        isa "Maybe we should play a game or something?"
        hug "A game? Do you have other boring ideas like that?"
        name "What kind of game?"
        show hugorealizingsomething at right with dissolve:
            xalign 0.7
        hide hugoserious with dissolve
        
        hug "Like a card game?"
        show hugounsure at right with dissolve:
            xalign 0.7
        hide hugorealizingsomething with dissolve
        hug "I suck at card games."
        isa "I don't know, maybe like we gives each other a challenge?"
        show hugorealizingsomething at right with dissolve:
            xalign 0.7
        hide hugounsure with dissolve
        hug "Like missions?"
        show isabellelaugh3 with dissolve
        hide test044 with dissolve
        isa "Like you asking the girl living here if she want to party with us."
        hug "Oh wow, that would be so awkard."
        show hugoserious at right with dissolve:
            xalign 0.7
        hide hugorealizingsomething with dissolve

        isa "Come on, we know it's just for the game."
        name "Don't worry Hugo, We know you are cooler than her."
        hug "..."
        show hugolaugh at right with dissolve:
            xalign 0.7
        hide hugoserious with dissolve
        
        hug "But like, what do I say to her?"
        hug "'Hi, do you want to party with us?'"
        hug "'Hi do you want to play card games with us?'"
        isa "whatever, we don't care, tell her we're so happy to be here"  
        isa "and that we hope to spend some time with her."
        show hugoserious at right with dissolve:
            xalign 0.7
        hide hugolaugh with dissolve

        hug "That's boring.."
        hug "Maybe I should just ask her how her daddy got so rich..."
        isa "Or that you want to form the power couple of the century with her."
        show hugolookingtowardthelivingroom at right with dissolve:
            xalign 0.7
        hide hugoserious with dissolve
        
        hug "ok fuck it... i'll find something when i'll be in front of her"
        hug "She might even accept."
        hug "Wish me good luck."
        "Hugo walks away toward his mission."
        hide hugolookingtowardthelivingroom with dissolve
        
        show isabelleteasing with dissolve
        hide isabellelaugh3 with dissolve
        
        isa "Finally, he's gone"
        
        name "You wanted to get rid of him?"
        isa "Not really, but I wanted to talk to you alone for a moment."
        name "About what?"
        isa "Nothing specific... I just like getting to know people better."
        isa "And you seem interesting."
        name "Thanks, I guess."
        isa "You're pretty cute when you're modest like that."
        name "I'm not being modest, I just don't know what to say."
        show isabellelaugh4 with dissolve
        hide isabelleteasing with dissolve
        isa "See? That's exactly what I mean."
        isa "Most guys would already be trying to impress me or something."
        name "Should I be trying to impress you?"
        show isabellegossip with dissolve
        hide isabellelaugh4 with dissolve
        isa "Only if you want to."
        isa "But I'm curious... what would you do to impress me?"
        
        menu:
            "I'd tell you about my hobbies":
                name "I'd probably tell you about my hobbies or something."
                isa "Boring. Next."
                name "Hey, you asked!"
                isa "I know, but I was hoping for something more... creative."
            
            "I'd show you my dance moves":
                name "I'd show you my incredible dance moves."
                isa "Oh really? Let me see them then."
                name "Right here? Right now?"
                isa "Why not?"
                "I do a few awkward dance moves."
                isa "Haha, okay, that's... something."
                name "Not impressed?"
                isa "It's endearing, let's say that."
            
            "I wouldn't try to impress you":
                name "Honestly? I wouldn't try to impress you."
                show isabellesmile with dissolve
                hide isabellegossip with dissolve
                isa "Oh? And why is that?"
                name "Because if you're interested, you'll figure it out on your own."
                name "And if you're not, trying to force it won't help."
                isa "Hmm... that's actually pretty smart."
                isa "I like that approach."
        
        show hugolaughsorry2 at right:
            xalign 0.7
        with dissolve
        
        hug "Mission accomplished!"
        name "Already? That was fast."
        hug "I mean she just said that she was having fun and that she would join us later."
        hug "It wasn't too weird."
        hug "She was actually kinda happy that I asked her."
        isa "See? We told you that you were the cooler guy in here."
        isa "What did you ask her?"
        hug "I just said 'Nice party, I hope you'll make us visit your palace.'"
        hug "She wanted to know if we were having fun."
        isa "And what did you tell her?"
        hug "That we were having a blast, obviously."
        hug "And I may have mentioned that we were thinking of playing some party games."
        isa "Did she seem interested?"
        hug "She said she'd join us if we found something fun to do."
        name "So what now? Your turn to give us a challenge?"
        show hugoplanningsomething at right with dissolve:
            xalign 0.7
        hide hugolaughsorry2 with dissolve
        hug "Yep"
        hug "Let me think..."
        hug "Isa... "
        show isabellegossip with dissolve
        hide isabellesmile with dissolve
        isa "Oh boy"
        hug "I dare you to go flirt with that guy over there."
        isa "the guy by the window?"
        hug "Yeah, the one with the blue shirt."
        show isabelleneutral2 with dissolve
        hide isabellegossip with dissolve
        isa "That's too easy."
        show hugolaugh2 at right with dissolve:
            xalign 0.7
        hide hugoplanningsomething with dissolve
        hug "Look at her, 'too easy'.."
        hug "Bring back his number."
        isa "What is this? A pickup artist competition?"
        isa "You watch too much youtube.."
        show hugolaughsorry2 at right with dissolve:
            xalign 0.7
        hide hugolaugh2 with dissolve
        hug "Just do it instead if talking."
        isa "Okay, okay, I'll do it."
        show isabellegossip with dissolve
        hide isabelleneutral2 with dissolve
        isa "Fuck... Why did I propose this stupid game.."
        hide isabellegossip with dissolve
        "Isabelle walks away toward her mission"
        hug "Look at her go..."
        name "Do you think she'll actually get his number?"
        show hugolaughsorry at right with dissolve:
            xalign 0.7
        hide hugolaughsorry2 with dissolve
        hug "Honestly? She probably could."
        hug "I mean, she's not bad looking."
        hug "Right?"
        name "Yeah, definitely."
        show hugov2 at right with dissolve:
            xalign 0.7
        hide hugolaughsorry
        hug "Would you date her?"
        name "Me? Yeah, why not."
        hug "Haha, you two would make a cute couple."
        name "Maybe I should ask her out..."
        hug "Dude... If she doesn't make a move on you first, I'd be impressed."
        hug "Unless she manages to snag that guy instead."
        name "What are they doing over there?"
        hug "They're telling each other their life stories."
        hug "Looks like they're hitting it off."
        hug "Maybe she'll actually pull this off."
        hug "Oh, she's coming back."
        name "So, did you get it?"
        show isabelleneutral2 with dissolve
        
        isa "Not even close."
        isa "I completely froze the moment I walked up to him."
        isa "I almost cried."
        show hugopowerfull at right with dissolve:
            xalign 0.8
        hide hugov2
        hug "What? You cried?"
        isa "Just kidding - he gave me his number."
        show hugounsure at right with dissolve:
            xalign 0.8
        hide hugopowerfull with dissolve
        hug "What? No way."
        hug "What is it then?"
        isa "You think I memorized it? I put it in my phone, dummy."
        hug "Show us."
        isa "Geez, fine, look."
        isa "See? 'James - nice guy'"
        hug "I bet you already had that number."
        isa "..."
        isa "Go ask him yourself then."
        hug "Okay, okay, I believe you... for now."
        hug "We'll verify this later."
        show hugorealizingsomething at right with dissolve:
            xalign 0.8
        hide hugounsure with dissolve

        isa "So it's my turn now."
        isa "[name]..."
        isa "To keep with the awkward encounters theme..."
        isa "You're going to go talk to that girl over there."
        name "Which girl?"
        isa "The one in the red sweater by the stairs."
        show hugolookingtowardthelivingroom at right with dissolve:
            xalign 0.8
        hide hugorealizingsomething with dissolve
        name "Her?"
        if estelle_firstconv_done == True:
            name "I know her."
            hug "Really?"
            name "Yeah it's Estelle, we're in the same class."
            name "Don't know her that well though."
        isa "You're going to ask her to dance with you."
        show hugoserious at right with dissolve:
            xalign 0.8
        hide hugolookingtowardthelivingroom
        hug "Wow, that's brutal..."
        name "..."
        name "This is soooo awkward."
        name "I can't.."
        show isabellelaugh3 with dissolve
        hide isabelleneutral2 with dissolve
        isa "Come on, we don't actually expect you to dance with her."
        hug "Plus this music really sucks..."
        hug "Makes it even more awkward..."
        isa "We just want to see you try."
        name "That's kind of cruel."
        show hugolaugh at right with dissolve:
            xalign 0.8
        hide hugoserious with dissolve
        hug "Yeah, I agree with him."
        hug "That may be a bit much.."
        isa "Come on, it's just for fun. You can always tell her afterwards that it was just a dare."
        name "Ok... I guess I have to do it."
        isa "Yep."
        isa "Come on, show us your charming skills."
        hug "Good luck."
        "I walk over to the girl in the red sweater."
        scene livingroomarrowflou
        show esther12 with dissolve
        if estelle_firstconv_done == True:
            name "Hey Estelle, how's it going?"
            est "Oh... it's you."
            name "Just saying hi. Are you having fun?"
            est "Yeah sure, I feel like you have something to say.. "
            name "..."
        else:
            name "Hey!"
            est "what's up?"
            name "Just saying hi. Are you having fun?"
            est "Yeah sure, I feel like you have something to say.. "
            name "..."
            "I gather my courage."
            menu:
                "Don't you think this music makes you want to dance?":
                    name "Don't you think this music makes you want to dance?"
                    show esther15 with dissolve
                    hide esther12 with dissolve
                    est "What?"
                    name "The music.. don't you think it's..."
                    name "nevermind"
                    est "Do I look like someone who would dance to this garbage?"
                    name "Come on, it could be fun. Just one song."
                    est "Fun? You have a weird definition of fun."
                    
                    hide esther15 with dissolve
                    

                
                "Would you like to dance with me?":
                    show esther15 with dissolve
                    hide esther12 with dissolve
                    name "Would you like to dance with me?"
                    est "Dance with you?"
                    est "No, I am ok."
                    est "Thanks for asking."
                    name "You're welcome."
                    hide esther15 with dissolve
                
                "Fair maiden, might I humbly beseech thee to honor me with thy gracious presence upon the dance floor?":
                    name "Fair maiden, might I humbly beseech thee to honor me with thy gracious presence upon the dance floor?"
                    show esther15 with dissolve
                    hide esther12 with dissolve
                    est "What did you just say?"
                    name "Uh... what I said?"
                    name "You know, asking you to dance."
                    est "Wow, you really are something..."
                    show estherparty with dissolve
                    hide esther15 with dissolve
                    est "It's almost... charming."
                    name "So, would you like to dance with me?"
                    show esther15 with dissolve
                    hide estherparty with dissolve
                    est "Are you insane? Just the two of us here?"
                    
                    est "Well..."
                    est "If other people start dancing, maybe I'll consider honoring your invitation."
                    name "Oh ok, i'll take that."
                    name "thanks"
                    name "We'll catch up later then."
                    est "See you later, fair maiden."
                    hide esther15 with dissolve

            scene vestibulearrowflou with dissolve
            "I go back to Hugo and Isabelle"
            show hugolaugh at right with dissolve:
                xalign 0.7
            show isabellelaugh4 with dissolve

                
            name "She said yes.."
            hug "Really?"
            name "Yeah, it's just that she wants other people to dance first."
            name "But after she'll dance with me."
            hug "ahahah."
            isa "We saw her reaction from here."
            isa "You are not gonna make us believe that she said yes."
            name "No, I swear."
            isa "Anyway, we got what we wanted."
            hug "It was really funny [name]"
            hug "thanks for that."
            hug "But you pulled it off! Respect."
            isa "Yeah, I didn't think you would actually do it."
            isa "But you did."
            isa "Cheers!"

            show isabellelaugh4 with dissolve
            hide isabelleteasing with dissolve

            isa "Well, mission accomplished. What should we do next?"
            hug "Hey let's drink, what else?"

            show isabelleneutral3 with dissolve
            hide isabellelaugh4 with dissolve

            isa "I guess it's all what left to do."
            hug "Lets grab some beer"
            scene black with dissolve
            "We crack open a couple of beers in the kitchen and talk for a while."
            "As we talk, I keep drinking without really noticing."
            "After a while, I start to feel a little tipsy."
            $ drink_count = 5
            $ isabelleconv_count += 1
            jump isabelleconvbourre1

    label isabelleconv5:
        scene vestibulearrow
        scene vestibulearrowflou with dissolve 
        "I join Isabelle and Hugo in the vestibule."
        show test044 with dissolve
        
           
        "Isabelle immediately approaches me."
        "She takes me by the waist."
        isa "That was fun, wasn't it?"
        name "Yeah, i loved it."
        isa "You took it like a champ."
        name "Thanks..."
        hide test044 with dissolve
        menu : 
            "End the party here":
                scene black
                "We continue talking with Hugo and Isabelle for a while."
                "Then feeling tired, I decide to go home."
                jump partyending
            "Continue":
                jump vestibule
       
        
       

    label isabelleconv1:  
            $ isabelleconv_count += 1
            scene vestibulearrow
            scene vestibulearrowflou with dissolve 
            show test044 with dissolve
            
            show hugov2 at right:
                xalign 0.7
            
            hug "Hey, you made it!"
            name "Yeah, I finally left my cave, haha."
            hug "It's funny seeing you here."

            hug "Oh, and this is Isabelle."
            hug "Isabelle, this is [name], the nerd I told you about."
            show isabellesmile with dissolve
            hide test044 with dissolve
            isa "Hi, nice to meet you."
            name "Nice to meet you too."
            name "I'm not really a nerd, but I'll let it slide."
            hug "That's exactly what a nerd would say."
            isa "Don't worry, when he's not at a party, he's glued to his computer."
            hug "Yeah, yeah. Anyway, glad you could come."
            name "Thanks, it's cool of you to invite me."
            hug "No problem, it's actually thanks to Zoey. She knows the girl who lives here."
            hug "At first she wasn't sure, but Zoey convinced her."
            hug "I'm not supposed to say this, but whatever."
            hug "She told her you were her date."
            show isabellelaugh4 with dissolve
            hide isabellesmile with dissolve

            isa "Haha, really?"
            name "Oh... okay."
            show isabelleneutral3 with dissolve
            hide isabellelaugh4 with dissolve

            isa "That's kind of cute."
            isa "You look a bit embarrassed."
            isa "Does it bother you if people think you're her date?"
            name "No, not really. I mean, I guess not. I'm not sure what it means."
            isa "You don't know what a 'date' is?"
            name "No, I mean, unless she has something planned."
            show isabelleteasing with dissolve
            hide isabelleneutral3 with dissolve
            isa "I'm just teasing you."
            isa "But knowing her, yeah, she probably has something in mind."
            hug "Yeah, I don't know if she really wants people to think she came with a date, but whatever."
            hug "It just limits her options."
            name "Haha, true."
            name "So it's nice of her, I guess."
            hug "Yeah, she's a good person overall."
            show isabellegossip with dissolve
            hide isabelleteasing with dissolve
            isa "An angel."
            name "Feels like I'm missing something here."
            hug "A saint, even."
            isa "You'll see, you'll love her, [name]."
            hug "Haha."
            hug "She's in the living room if you want to say hi."
            isa "Yeah, but don't go too far, or I'll be stuck talking to this geek all night."
            hug "Shut up, let's go get a drink."

            show isabelleneutral3 with dissolve
            hide isabellegossip with dissolve
            jump kitchenparty

    label isabellesecondchance:
        
            scene vestibulearrow
            scene vestibulearrowflou with dissolve 
            show test044 with dissolve
            "Approaching Isabelle and Hugo, Isabelle takes me aside."
            isa "Hey, don't you want to dance instead of running around?"
            isa "You look like you need to let off some steam."
            show hugov2 at right:
                xalign 0.7
            hug "Come on let's go!"
            "We head toward the living room, Isabelle holding me by the waist, pretending to support me."
            "She takes the opportunity to slip a hand under my shirt."
            scene hugodancingalone
            "Hugo starts dancing by himself."
            isa "Yeah, go Hugo!"
            isa "Look at him."
            isa "He's as drunk as you."
            scene hugodancingalone2 with dissolve
            name "Yeah, but he's not as magical as me."
            isa "I know."
            isa "Let me see just how magical you are."
            scene ericdansingisabelle with dissolve
            "Isabelle takes me by the waist and begins dancing with me."
            "The three of us start dancing wildly together."
            "The others join us after a moment."
            "A crowd forms around us."
            "Isabelle presses closer and closer to me."
            "I can feel the warmth radiating from her body."
            isa "You're really getting into it..."
            isa "I never would have guessed you had these moves."
            name "I'm full of surprises."
            isa "That you are."
            isa "My little party unicorn."
            hug "Hey, quit the flirting and dance with me!"
            isa "Go find your own dance partner."
            isa "Haha, such a third wheel."
            isa "I'm keeping this one to myself."
            name "Since when did I become your personal property?"
            isa "Just for tonight."
           
            "Isabelle leans in and kisses me softly."
            "I catch a hint of her desire in the air."
            "I can tell she wants me."
            "We keep dancing, our bodies pressed close."
            "Every now and then, Isabelle brings a drink to my lips."
            "The alcohol is starting to hit me."
            scene ericdansingisabelle3
            "Isabelle slides behind me, her hips moving against mine."
            "The alcohol makes me feel bold, uninhibited."
            "I move with her, matching her rhythm."
            scene isabellebumping4 with dissolve
            window hide 
            pause
            scene isabellebumping3 with dissolve
            window hide 
            pause
            scene isabellebumping4 with dissolve
            window hide 
            pause
            scene isabellebumping3 with dissolve
            window hide 
            pause
            
            isa "I need to tell you something.."
            scene isabellewhispering
            "She moves closer to my ear."
            "Her breath on my neck makes me shiver"   
            
            if gender == "male":
                isa "You know this things i told you earlier about a guy going down on me at a party."
            
            elif gender == "fem":
                isa "You know this things i told you earlier about a guy going down on me at a party."
        
            "I listen to her silently, holding my breath"  
           
            
            scene isabellewhispering
            isa "I think you might be exactly what I've been waiting for." 
            "While speaking, Isabelle continues to move against me."
            "Pressing closer and closer to me" 
            isa "Want to find somewhere quieter?"
            isa "Just the two of us?"
            name "Yes... That would be nice."
            scene livingroomarrowflou
            "Isabelle takes me by the waist and we slip away from the crowd."
            "We go upstairs."
            isa "Haha, watch out not to fall."
            isa "Come on. Let's try to be discreet."
            "We arrive upstairs."
            "Isabelle leads me into the toilet."
            scene firsteric3
            isa "Finally alone."
            name "The toilet? Seriously?"
            "I groan, but the protest dies in my throat as she slams the door shut behind us, caging me in."

            if gender == "male":
                isa "Good boys get beds."
            elif gender == "fem":
                isa "Good girls get beds."
            isa "But you?"
            isa "I want to make you filthy."
            
            
            $ isabelledanse_done = True
            jump isabelledate