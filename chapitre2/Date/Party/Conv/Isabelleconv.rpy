label isabelleconv:
    default isabelleconvbourre_done = False


    if drink_count >= 5 and isabelleconvbourre_done == False:
        jump isabelleconvbourre1
    elif drink_count >= 5 and isabelleconvbourre_done == True:
        jump isabelleconvbourre2


    elif isabelleconv_count == 0:
        jump isabelleconv1 
    elif isabelleconv_count == 1:
        jump isabelleconv2


    label isabelleconvbourre1:
        scene vestibulearrowflou
        show test044 with dissolve
        show hugov2 at right:
            xalign 0.7
        name "I'm so happy to be here."
        name "Everyone around me seems so nice."
        hug "Yeah, it's true, it's pretty cool."
        isa "You really like to party, I can tell."
        isa "I've seen you shaking your butt for a while now."
        

        isa "He really looks like someone who wants to let loose."
        hug "Go all out, [name], you only live once, right?"
       
        
        name "YAAAAS! Tonight, I'm a party tornado!"
        hug "Hahaha, [name] is on fire."
        hug "It's time to ceeeeelebraaate!"
        isa "Come on Hug, you're not that drunk."
        hug "I know, but [name] inspires me. I think I'm going to put my good resolutions aside for tonight."
        isa "Wow, it didn't take much for you."
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
        
        hide hugov2 with dissolve
        show isabelleteasing with dissolve
        hide test044 with dissolve
        "Hugo walks away to the kitchen, laughing"
        isa "I can't believe you're this drunk already."
        isa "You really wanted to party, huh?"
        name "Yeah, I mean, I never really had the chance to party where I used to live."
        isa "Too bad I'm not in college anymore, I would have loved to party with you."
        hug "Hey guys, venez chercher vos verres"
        isa "He is calling us?"
        name "We are coming"
        "We find ourselves in the kitchen, chatting with the people there."
        "The atmosphere is cool and relaxed."
        "Talking with people makes me feel less numb from the alcohol."

        

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
        
        isa "Hey, you're feeling good here, aren't you?"
        name "Yeah, it's nice."
        isa "You look like you're ready for anything."
        name ""
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
        tra ""
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
        hug "Hey, if you want a beer, help yourself in the kitchen"
        jump vestibule
        $ isabelleconv_count =+1

    label isabelleconv1:  
            $ isabelleconv_count =+ 1
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
            
            menu:
                "go with isabelle":
                    jump isabelledate
                "Leave them":
                    jump vestibule
  