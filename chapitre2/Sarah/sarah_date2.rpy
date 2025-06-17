define sal = Character('Salomon', color="#7b9ce2")
define cat = Character('Cat', color="#7b9ce2")
define elise = Character('Elise', color="#1b2b50")
define jay = Character('Jay', color="#00e8f8")

label sarahdate2:
    
    scene stairssarah
    "I close my door, making sure it's locked, and head downstairs."
    "A person is coming down the stairs."
    
    show sarahneutral
    sar "Hi, it's my day off and I have a few friends over. Do you want to join us?"

    menu: 
        "Sure, why not?": 
            sar "Great, see you there."
            hide sarahneutral
            
            jump afternoon_party
        "I'm not sure, I'm a bit tired.": 
            sar "No worries, maybe next time."
            hide sarahneutral
            $ day_until_new_date = 4
            jump map3

label afternoon_party:
    name "Oh, nice. Is it some kind of afternoon party?"

    sar "Yeah, that's the spirit. It's a tea party."

    name "Sounds fun. Give me a minute, I'm coming."

    sar "Great, see you there."
    scene climbing2

    "The door is open, letting a cat out."

    cat "Meow."
    scene miaow3
    name "Hi, kitty. That's a nice chonk."
    cat "Mew."
    scene miaow4
    elise "His name is Salomon."

    name "Salomon, that's nice. Hi, Salomon."

    sal "Mrlh?"

    scene headshotelise2
    elise "Come in. I'm Elise."

    name "[name], nice to meet you."

    scene 1test2

    elise "We were talking about you."

    name "What?"

    elise "Sarah told us you were coming."
    
    scene enteringsarahelise
    elise "So we were talking about friendly neighborhoods and how it's rare to have a good one."
    elise "I am changing the track, guys. This is getting boring."
    
    scene e4sarahsayinghi2
    sar "That's Jay and Elise, they are friends from work."
    sar "And that's Salomon, the cat."
    name "Hi, everyone."
    name "I'm [name], nice to meet you."
    jay "Hey, nice to meet you too."
    scene ericlookforaseat
    elise "We were talking about dates."
    
    scene everyone sit eric
    "I sit with them on the couch and try to catch up with the discussion."

    elise "Do you remember last Tuesday when Sacha vomited on the laptop? He just threw up, went to sleep, and then came back like nothing happened. He didn’t even remember that he threw up."

    sar "And he was like, who the fuck threw up on the computer? He didn't even remember."

    elise "And Marion was like, aren’t you tired? It's 10 p.m."

    sar "It's late."

    sar "Honestly, I can’t blame her. I'm getting more tired earlier and earlier."

    jay "You're getting old. What are you, like 30?"

    scene everyonesit2
    sar "Shut the fuck up. I'm 28."

    jay "It's the turning point before 30."

    sar "Yeah, that's what everyone says."

    elise "How original."

    name "As long as you realize your dreams, you stay young."

    elise "Are you competing for the most cliché phrase?"

    name "I'm just saying."

    scene laughing elise
    elise "Live as if you were to die tomorrow."

    jay "The worst mistake you can make is constantly being afraid of making a mistake."

    name "That's a good one."

    elise "I'll write it on my Facebook wall."

    sar "Next to the pro-Palestinian posts, it'll be engraved in stone. Everyone will think you've lost it."

    scene everyone sit eric
    elise "Anyway, how’s your team handling the new project, Sarah?"

    sar "Uh... Not great, honestly."

    sar "It seems like they've completely lost interest in it."

    elise "Really? They can't be that disengaged!"

    sar "Oh, they are. Just last Wednesday, James asked if we were supposed to be designing a video game."

    elise "Why would he think that?"

    sar "I have no idea. I just stared at him in disbelief."

    scene laughing elise
    elise "Haha, that's ridiculous."

    elise "Hopefully, they’ll get back on track soon."

    sar "If they don't, you might have to take charge."

    elise "Yeah, maybe."

    jay "Maybe Elise's secretly sabotaging your team to take your place!"

    jay "It's like Game of Thrones, but with less blood."

    jay "Who knows, maybe she's already poisoned the coffee machine."

    sar "I wouldn't put it past her."

    elise "I'm not that evil."

    sar "Honestly, I am too drained to start thinking about what my coworker could do to me."

    "The conversation continues for a while, and I start to feel more comfortable with them."

    scene looking elise2

    "As we talk, I notice that Elise is trying to catch my glance. She's kinda pretty."

    "I'm not sure if she's interested in me or if I have something weird on my face."

    "I decide to ignore it and keep talking with the group."

    sar "I'm going to make some tea. Does anyone want some?"

    jay "One for me."

    name "Me!"

    scene gettingteae

    sar "What sort of tea do you want, [name]?"

    name "I'll take red tea."

    sar "Got it."

    scene sarcastic
    elise "Red tea? Isn't that a bit strong?"

    name "What do you mean?"

    elise "You remind me of my little sister."
    if gender == "male":
        "I am not sure how I feel about that..."
    name "What's her name?"
    elise "Joanna."
    name "It's pretty."
    jay "Where is she now?"
    elise "She's in Paris for her studies."
    elise "Living the bohemian life."
    elise "A bit like you."
    elise "You remind me of her."
    name "I am not sure how to take it."
    elise "She's kinda cute, so I guess it's a compliment."
    elise "But she is a bit of a brat."
    elise "She sometimes needs to be put back in her place."
    name "I have no doubt that you take care of it very well."
    scene servingtea
    "Sarah is coming back with tea."
    sar "Here you go."
    name "Thanks."
    scene lookingatsarah

    sar "It's cool to see you here."
    name "Yeah, it's nice to meet new people."
    name "Your friends are cool."
    sar "When they are sober, they are, yeah."
    "Sarah keeps looking at me insistently."
    "She seems genuinely happy to see me here."
    jay "Hey, I am also nice when I am drunk."
    sar "Yeah, you are a real sweetheart."
    name "I am sure you are, Jay."
    jay "Thanks."
    sar "You should come to the next party, so you can judge for yourself."
    sar "I am sure you will have a good time."
    name "I'm always up for a party."
    sar "Cool, I'll let you know."
    scene elisestanding
    sar "But you can come by whenever you want, if you want to hang out."
    name "Mh, ok... cool, thanks."
    "Elise gets up and stretches."
    elise "I think I'm going to go. I have some stuff to do."
    jay "I'm going to leave soon too. I need to rest before tomorrow."
    
    name "I should probably go too."
    sar "You can stay if you want."
    "I'm not sure I want to stay alone with Sarah while her friends are leaving..."
    name "I have stuff to do as well, but it was nice to hang out with you guys."
    scene leaving

    sar "Alright, see you around, guys."
    jay "And we'll touch base again about this party, right?"
    sar "Of course, Jay."
    name "See you around."
    
    "We leave the apartment, and after saying goodbye to Jay and Elise, I head home."
    scene home00
    "It's cool to have Sarah as a neighbor. Her friends seem nice too."
    "It reminds me a bit of my friends from my hometown."
    "Ok, where was I?"

    $ sarah_relation_status_text = "I should hang out to the cafe (you will meet Elise there)"
    $ sarah_homedate_done = True
    $ sarah_conv_done = True
    show screen homescreen4
    call screen homescreen4
    



    # "Elise walks with me downstairs, despite her somewhat relaxed appearance, I notice that she wears a very elegant perfume." 
    # "Elle ne semble pas être du genre à se laisser aller."

    # name "well je suis arrivé, ahah, see you lat..."

    # # elise "Hey you are a student right?"

    # # name "huh.. yes?"

    # # elise "What are you studying?"

    # # name "art history, why?"

    # # elise "i have a few arts book at home, that i want to get rid of, are you interested?"

    # # name "Oh yeah sure"

    # # name "if they are not too heavy"

    # # elise "well you can come by and choose the ones you want"

    # # name "ok, i can come by tomorrow"

    # # elise "mmh yeah... you can"

    # # elise "or..."

    # # elise "why not now?"

    # # name "now?"

    # # elise "if you have nothing better to do"

    # # name "mmh..."

    # # elise "come on i promise my books are worth it"

    # # "I hesitate for a moment, this feels like a date."
    # # "I don't know if I should go, but I'm curious about her books."
    # # "and I am kind of flattered"
    # # name "i don't know, i am a bit tired"

    # # name "do you live far away?"

    # # elise "not really, but if you don't want to come, it's fine"

    # # elise "i'll give them to someone else"

    # # name "no, no i am interested"

    # # name "i follow you"

    # # elise "great, let's go"

    # # "we walked down the stairs and out of the building"
    # # "we walked for a few minutes silently"
    # # "A weird tension settle between us."
    # # "she finally break the silence"
    # # elise "so, what do you think of Sarah?"
    # # name "hm, she's nice"
    # # name "i like her even thoguh i don't know her that much"
    # # name "she has this kind of aura that makes you feel reassured"
    # # elise "yeah..."
    # # elise "I understand why people would have this impression"
    # # name "she seems she can be trusted, like a older sister"
    # # elise "that's just because she's a bit older"
    # # elise "it doesn't mean that she is more mature than you. Or me, for that matter"
    # # name "yeah i guess"
    # # "we walk through the streets for a few minutes"
    
    # # name "is it far? You said it was close"
    # # elise "yeah, we're almost there, don't worry"
    # # name "my legs are tired"
    # # elise "jeez stop whining"
    # # elise "do you wants these books or not?"

    # # "we arrived in front of a tall building"
    # # elise "it's here"
    # # "we enter the building and take the elevator"
    # # "a silence sets beetween us"
    # # elise "welcome to my place"
    # # elise "I hope my roomate is not there"
    # # name "Oh you have a roomate"
    # # elise "yeah but she's not here often"
    # # name "i won't stay long "
    # # elise "no it's ok, don't worry"
    # # name "ok"
    # # "we enter her apartment"
    # # "Elise flat is nicely decorate but a bit small"
    # # Elise "do you want something to drink?"
    # # Elise "I have a beer if you want"
    # # name "I'd love a beer!"
    # # Elise "got it"
    # # "I sit on the couch and look around"
    # # "I am not sure if i should ask her about the books right away"
    # # Elise "here, i don't have roobois sorry"
    # # name "no worries"
    # # name "so..."
    # # elise "yeah?"
    # # name "the books?"
    # # elise "oh right"
    # # elise "they are in my room"
    # # elise "wait here"
    # # "she goes to her room"
    # # "I am have a weird feeling"
    # # "I don't know if I should stay or leave"
    # # "I hear her rummaging through her things"
    # # "She comes back with a few books in her arms"
    # # elise "here you go"
    # # name "wow"
    # # "Elise sit on the couch with, and we start to talk about the books"
    # # "She show me the artist she prefer"
    # # "Suddenly, the door open"
    # # Clara "hello"
    # # Clara "oh, we have a guest"
    # # Clara "i am clara, nice to meet you"
    # # Name "[name], same here"
    # # Clara "what are you guys doing?"
    # # elise "i am giving away some books"
    # # Clara "oh right, the books.."
    # # clara "I don't think I've seen you before."
    # # name "yeah, i am new here"
    # # name "i am Sarah's neighbor"
    # # clara "oh right, i see"
    # # "clara look at the books"
    # # clara "Are you getting rid of this one?"
    # # clara "I like it."
    # # elise "You can keep it if you put it in your room."
    # # clara "mmh"
    # # name "Are you sure i can take them?"
    # # name "they are really nice"
    # # elise "yeah! i am telling you, i need spaces in my room"
    # # name "I don't know if i will be able to carry them all"
    # # elise "you can pick some and come back later"
    # # name "yeah i guess"
    # # elise "you can come back whenever you want"
    # # elise "you can drink your beer, you are not in a hurry are you?"
    # # clara "can i have a beer too?"
    # # elise "no, you can't"
    # # clara "why not?"
    # # elise "cause, you have been naughty"
    # # clara "oh no!"
    # # elise "don't you have some stuff to do?"
    # # clara "Oh, I get it. I'll let you two enjoy your book club."
    # # elise "Finaly, i thought i would have to be rude"
    # # elise "Let's go to my room, on sera plus mieux"

    # # elise "Let's move to my room, it's more chill."
    # # elise "I have some special books I'd love to show you."

    # # elise "And we won't be bothered by my roomate"
    # # "I'm not entirely sure how her roommate was bothering us, but I nod and follow her."
    # # "We entered her small bedroom, qui a l'air d'être plus une extension du salon, qu'une chambre à part"
    # # elise "Take a look at this"
    # # "she puts a large book on the bed"
    # # Elise " here, this one is cool "
    # # "She put a large book on the bed" 
    # # name "Wow... this is special."
    # # elise "Yeah, just like you."
    # # name "Haha, stop it."
    # # "I flip through the pages absentmindedly."
    # # "I can feel Elise's gaze on me."
    # # "Suddenly, my phone buzzes."
    # # "It's a text from Sarah."
    # # sar "Hey, are you at your apartment?"
    # # name "No, I'm out. Do you need something?"
    # # sar "Oh, okay. No, don't worry. It was nice seeing you."
    # # sar "I just wanted to see you real quick, but it can wait."
    # # name "I'll be back soon, I think."
    # # sar "Alright, have a nice day :)"
    # # elise "You and Sarah are texting?"
    # # name "I guess we are."
    # # name "How long have you known her?"
    # # elise "About a year and a half."
    # # name "What do you think of her?"
    # # elise "Why do you ask?"
    # # name "Because you asked me earlier."
    # # elise "Well, she's nice. She's a good listener."
    # # elise "She's just..."
    # # name "What?"
    # # elise "Nothing."
    # # name "Okay..."
    # # elise "She's just not good at her job."
    # # name "Oh."
    # # name "And you think you would be better, I suppose?"
    # # elise "Did you sleep together with Sarah?"
    # # name "What?? No?!"
    # # elise "That's what I thought."
    # # name "Why do you ask?"
    # # elise "You know why."
    # # name "No, I don't."
    # # elise "She has always had trouble taking what she desires."
    # # elise "Not like me."
    # # elise "I know what I want."
    # # name "yeah, that's a good thing, i guess"
    # # Elise "Do you feel that I want to fuck you ?"
     
        