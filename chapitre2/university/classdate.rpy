define cam = Character('Camille', color="#bd600a")
define sam = Character("Samuel", color="#04f8f8")
 


label classdate0:
    scene smallclassroom
    "I enter the classroom and sit at a table"
    "I try my best to focus on the teacher's lecture"
    show emma00
    emm "hey, do you have a pencil?"
    name "yeah sure"
    emm "Thanks!"
    $ classdate_count += 1
    "The class passes by slowly"
    "After two hours of class, everyone leaves,"
    "Finally"
    $ class_done = True
    scene black with dissolve
    "I leave the classroom and head to the garden"
    jump gardenuni_start2
label classdate1:
    scene smallclassroom
    "I enter the classroom and sit at a table"
    "I try my best to focus on the teacher's lecture"
    show camille00 
    cam "have you seen the architecture of the campus?"

    name "hm yes, its pretty nice"
    $ classdate_count += 1
    cam "it's so old-fashioned."

    cam "look at the tables, they’re made of poor quality wood."

    name "ok?"

    cam "why did i come here?"

    name "isn't it weird to judge a school by the quality of the table?"

    cam "You don't know, everything lie in the details"

    name "I see..."

    hide camille
    "The class passes by slowly"
    "After two hours of class, everyone leaves,"
    "Finally"
    $ class_done = True
    scene black with dissolve
    "I leave the classroom and head to the garden"

    jump gardenuni_start2



# //DIRECTION
# ////////////////////////
label classboring:
    if classdate_count == 0:
        jump classdate0
    elif classdate_count ==1:

        jump classdate1   
    # //Camille Spank
    elif camillelove_count ==2 and camillespank == False:
        scene camilleclassarriving
        "I walk down the corridor towards my class"
        scene spank
        "People are entering, I arrived just in time"
        scene spank2
        play sound "audio/music/spank.mp3" volume 1.0
        "I'm about to enter the classroom when suddenly, I feel a sharp slap on my butt."
        "I turn around and see Camille smiling at me."
        "I'm so shocked that I don't say anything."
        "She walks past me without saying a word and goes to sit down."
        "A few people saw the scene, which increases my embarrassment."
        "I enter the classroom trying to hide my discomfort."
        
        $ camillespank = True
        scene smallclassroom
        menu: 
            "Sit with Emma":
                jump emmadirection
    
            "Sit elsewhere": 
                jump classdatedirection
            "Sit with Camille":
                jump camilledirection
    elif camillelove_count ==3 and camillespank2 == False:
        scene spank with dissolve
        "As I enter the classroom, I feel a swift movement behind me"
        "It's probably Camille"
        menu: 
            "let her spank me":
                scene spank
                play sound "audio/music/spank.mp3" volume 1.0
                "I feel a sharp slap on my butt."
                scene spank4
                "I hear some laugh behind me"
                $ camillespank2 = True
                $ camillelove_count += 1
            "avoid her spank":
                "I hurry myself into the class before Camille can reach my ass"
        scene smallclassroom
        menu: 
            "Sit with Emma":
                jump emmadirection
    
            "Sit elsewhere": 
                jump classdatedirection
            "Sit with Camille":
                jump camilledirection
    elif camillelove_count >=3 and camillespank3 == False:
        scene spank with dissolve
        "As i enter the classroom, i feel a swift movement behind me"
        "It's probably Camille"
        menu: 
            "let her spank me":
                scene spank2
                play sound "audio/music/spank.mp3" volume 1.0
                "I feel a sharp slap on my butt."
                
                "I hear some laugh behind me"
                $ camillespank3 = True
                $ camillelove_count += 1
            "avoid her spank":
                "I hurry myself into the class before Camille can reach my ass"
                
        scene smallclassroom
        menu: 
            "Sit with Emma":
                jump emmadirection
    
            "Sit elsewhere": 
                jump classdatedirection
            "Sit with Camille":
                jump camilledirection 
#    /////////////


    elif classdate_count >= 2:
        scene smallclassroom
        menu: 
            "Sit with Emma":
                jump emmadirection
    
            "Sit elsewhere": 
                jump classdatedirection
            "Sit with Camille":
                jump camilledirection




label emmadirection :
    if classdateemma_count == 0:
        jump classemmadate
    elif classdateemma_count == 1:
        jump classemmadate1
    elif classdateemma_count == 2:
        jump classemmadate2
    elif classdateemma_count == 3:
        jump classemmadate3
    elif classdateemma_count == 4:
        jump classemmadate4
    elif classdateemma_count == 5:
        jump classemmadate5
label camilledirection:
    
    if classdatecamille_count == 0:
        jump classcamilledate
    elif classdatecamille_count == 1:
        jump classcamilledate1
    elif classdatecamille_count == 2:
        jump classcamilledate2
    elif classdatecamille_count == 3:
        jump classcamilledate3
    elif classdatecamille_count == 4:
        jump classcamilledate4
    elif classdatecamille_count == 5:
        jump classcamilledate5
    elif classdatecamille_count == 6 and camille_moneycheck_passed == False:
        jump classcamilledate6
    elif classdatecamille_count == 6 and camille_moneycheck_passed == True:
        jump classcamilledate7
    elif classdatecamille_count == 7:
        jump classcamilledate8
    elif classdatecamille_count == 8:
        jump classcamilledate9
    elif classdatecamille_count == 9:
        jump classcamilledate10
    elif classdatecamille_count == 10:
        jump classcamilledate11
    
    
label classdatedirection : 
    if classdate_count ==2:
        jump classdate2
    elif classdate_count ==3:
        jump classdate3
    elif classdate_count ==4:
        jump classdate4
    elif classdate_count == 5:
        jump classdate5
    elif classdate_count >= 5 and (camillespank2 == True or camillespank3 == True) and estelle_spankconv_done == False  :
        jump classdate5_1
    elif classdate_count >=6 and emma_date_done == True:
        jump classdate6
    elif classdate_count >=6 and camille_sdate_done == True:
        jump classdate6_1
    
    else:
        jump classdaterandom

    # elif classdate_count ==6:
    #     jump classdate6
    # elif classdate_count ==7:
    #     jump classdate7
    # elif classdate_count ==8:
    #     jump classdate8
    # elif classdate_count ==9:
    #     jump classdate9




# //////////////////////////////Camille ///////////////////////////////////////
label classcamilledate:
    scene smallclassroomblur with dissolve 
    "I enter the classroom and sit at a table."
    "I try my best to focus on the teacher's lecture."
    show singleviewcamille01 with dissolve
    cam "This teacher is so boring."
    cam "I hate wasting my time like this."
    cam "I have so many things to do."
    name "Shh, I am trying to listen."
    show camille02 with dissolve
    hide singleviewcamille01 with dissolve
    cam "Are you serious right now?"
    name "Come on, it's interesting."
    cam "Why am I even talking to you?"
    name "Shh, the teacher is looking at us."
    cam "Don't shush me."
    cam "Unbelievable..."
    "The class passes by slowly."
    hide singleviewcamille02 with dissolve
    "After two hours of class, everyone leaves."
    "Finally."
    $ classdatecamille_count += 1
    $ class_done = True
    scene black with dissolve
    "I leave the classroom and head to the garden."
    jump gardenuni_start2
label classcamilledate1:
    scene smallclassroomblur with dissolve 
    show camille05
    cam "Hmmm, just because the seat is empty doesn't mean you can come sit next to me."
    menu : 
        "I don't like rude people anyway":
            jump classboring
        "I won't bother you, I promise":
            hide camille05 with dissolve
            show camille07 with dissolve
            cam "You better."
            hide camille07 with dissolve
            "I sit next to Camille and try my best to focus on the teacher's lecture."
            "I take my notes diligently."
            "Camille seems to be working on something else on her computer."
            "I wonder what she's doing."
            "She doesn't seem interested in the class."
            "She turns to me."
            show camille00 with dissolve
            cam "Hey, do you have any cigarettes?"
            name "Yeah, sure."
            cam "Can you give me one? I forgot my pack at home."
            menu :
                "Sure, here you go.":
                    $ classdatecamille_count += 1
                    $ camillelove_count += 1
                    "I hand Camille a cigarette, which she places in front of her computer."
                    cam "Thanks."
                    cam "I'll smoke that after class."
                    name "I am trying to quit smoking."
                    cam "Good for you."
                    name "It's too expensive anyway."
                    cam "Yeah, I know... it's a luxury item these days."
                    "The class passes by slowly."
                    "After two hours of class, everyone leaves."
                    "Finally."
                    $ class_done = True
                    scene black with dissolve
                    "I leave the classroom and head to the garden."
                    jump gardenuni_start2

                "Sorry, I don't have many left.":
                    $ classdatecamille_count += 1
                    "Camille stares at me but doesn't say anything."
                    "She turns to her computer."
                    "The class passes by slowly."
                    "After two hours of class, everyone leaves."
                    "Finally."
                    $ class_done = True
                    scene black with dissolve
                    "I leave the classroom and head to the garden."
                    jump gardenuni_start2

    "The class passes by slowly."
    "After two hours of class, everyone leaves."
    "Finally."
    $ classdatecamille_count += 1
    $ class_done = True
    scene black with dissolve
    "I leave the classroom and head to the garden."
    jump gardenuni_start2
label classcamilledate2:
    scene smallclassroomblur with dissolve 
    "I enter the classroom and sit at a table."
    "I try my best to focus on the teacher's lecture."
    show camillesmiling3 with dissolve
    cam "Ugh, it's this teacher again."
    cam "I can't listen to him."
    cam "It's clear he has no clue what he's talking about."
    name "I think he's interesting."
    cam "You're kidding me, right?"
    name "No, I'm serious."
    show camille14 with dissolve
    hide camillesmiling3 with dissolve
    cam "You're just trying to get on my nerves."
    cam "Give me a cigarette, you're stressing me out."
    menu :
        "Sure, here you go.":
            $ classdatecamille_count += 1
            $ camillelove_count += 1
            "I hand Camille a cigarette, which she places in front of her computer."
            cam "Thanks, darling."
        "Sorry, I don't have many left.":
            $ classdatecamille_count += 1
            "Camille stares at me but doesn't say anything."
            "She turns to her computer."
            "The class passes by slowly."
            "After two hours of class, everyone leaves."
            "Finally."
            $ class_done = True
            scene black with dissolve
            "I leave the classroom and head to the garden."
            jump gardenuni_start2
    cam "I am not gonna waste my time listening to this dude."
    "She closes the note tab on her computer and opens a new one."
    "She seems to be working on something else."
    name "What are you working on?"
    cam "It's a website that I run with some friends."
    cam "We're trying to make it big."
    name "What's it about?"
    cam "It's a blog about fashion."
    name "Cool."
    cam "Yeah, we have some sponsors that work with us. It's pretty cool."
    "I should find a job too."
    "The class passes by slowly."
    "After two hours of class, everyone leaves."
    "Finally."
    $ class_done = True
    scene black with dissolve
    "I leave the classroom and head to the garden."
    jump gardenuni_start2
label classcamilledate3:
    scene smallclassroomblur with dissolve 
    if camillespank == True:
        "Despite the embarrassment of the spank (or because of it), I sit next to Camille."
        "I try my best to focus on the teacher's lecture."
    else:
        "I enter the classroom and sit at a table."
        "I try my best to focus on the teacher's lecture."
    
    "Camille is not paying attention to the class, as usual."
    "She is just working on her website."
    "I am not sure if I want to talk to her."
    menu:
        "Is that your website?":
            show camille07 at Position(xpos=0.5, ypos=1.010) with dissolve 
            $ classdatecamille_count += 1
            $ camillelove_count += 1
            cam "Yup, I am posting an article that I wrote."
            name "Cool, can I read it?"
            cam "Sure, when it's finished."
            show camilleneutral with dissolve
            hide camille07 with dissolve
            cam "I am not sure if you'll understand it, though."
            cam "I'm writing about the launch of a shoe brand that you've probably never heard of."
            cam "Some friends of mine are starting their business."
            name "Cool."
            name "Do you make money with that?"
            "Camille looks embarrassed."
            show camille14 with dissolve
            hide camilleneutral with dissolve
            cam "Yeah, I mean, I manage part of the website, so yeah."
            name "Nice."
            name "I need to find a way to make money too."
            show camille08 with dissolve
            hide camille14 with dissolve
            cam "If I have plans for lingerie shoots, I'll call you." 
            cam "Ahah."
            show camille11 with dissolve
            hide camille08 with dissolve
            cam "With that cute ass of yours, you could make a few bucks."
            menu:
                "Why not":
                    name "Well, I am open to anything."
                    cam "That's the spirit."
                    cam "Willing to go all in to succeed."
                    "Camille chuckles softly."
                "I am not like that":
                    name "I would prefer a real job."
                    cam "It is a real job, actually."
            
            hide camille11 with dissolve
            "The class passes by slowly."
            "After two hours of class, everyone leaves."
            "Finally."
            $ class_done = True
            scene black with dissolve
            "I leave the classroom and head to the garden."
            jump gardenuni_start2
        "Stay silent and take notes":
            $ classdatecamille_count += 1
            "The class passes by slowly."
            "After two hours of class, everyone leaves."
            "Finally."
            $ class_done = True
            scene black with dissolve
            "I leave the classroom and head to the garden."
            jump gardenuni_start2
label classcamilledate4:
    scene smallclassroomblur with dissolve 
    "I enter the classroom and sit next to Camille."
    "I try my best to focus on the teacher's lecture."
    show camillesmiling3 with dissolve
    cam "I don't understand why you are trying so hard in this class."
    cam "You are the only one who cares."
    cam "Even the teacher has given up."
    name "I find it interesting."
    cam "Pfff, you are so boring."
    cam "I don't know why I am talking to you."
    name "Whatever."
    cam "I bet you are a virgin."
    name "What?"
    show camilleneutral with dissolve
    hide camillesmiling3 with dissolve
    cam "When was your last bang?"
    name "I don't know, I don't keep track of that."
    cam "Sure, ahah."
    show camilleneutral2 with dissolve
    hide camilleneutral with dissolve
    cam "Personally, I screwed two days ago."
    cam "It was a good one."
    "I am starting to feel uncomfortable."
    "A heat wave is rising in my face."
    "Camille notices it."
    
    if gender == "male":
        cam "It was a friend of mine, we are the same age, a small white boy like you."
        cam "Friends since forever, now potentially lovers too - life's funny."
    elif gender == "fem":
        cam "It was a friend of mine, we are the same age, a small white girl like you."
        cam "Friends since forever, now potentially lovers too - life's funny."
    name "Yeah, I guess."
    cam "Don't make that face, I am not interested in you."
    cam "I have some standards."
    name "Good, I am not interested either."
    "The class passes by slowly."
    "After two hours of class, everyone leaves."
    "Finally."
    "As I am walking out, Camille gets behind me and slaps me on the ass."
    "She walks away laughing."
    $ camillelove_count += 1
    $ classdatecamille_count += 1
    $ class_done = True
    scene black with dissolve
    "I leave the classroom and head to the garden."
    jump gardenuni_start2
label classcamilledate5:
    scene smallclassroomblur with dissolve
    "I enter the classroom and sit next to Camille."
    "I try my best to focus on the teacher's lecture."
    if camillespank2 == True and camillespank3 == True:
        show camille04 with dissolve
        cam "I can't believe you let me spank you like that."
        cam "Don't you have any dignity?"
        name "You always catch me off guard."
        cam "Or you like to be spanked."
        cam "Little slut..."
        hide camille04 with dissolve
    "Camille starts working on her project, ignoring the class."
    show camille07 with dissolve
    cam "Ok, I've finished my article."
    cam "Man... I am so tired."
    cam "I shouldn't multitask too much."
    cam "What are you up to?"
    cam "Still writing your notes like the perfect student."
    cam "Don't you want to take a break from being boring?"
    name "Fuck you..."
    if camillelove_count >= 3:
        jump camillelovescene
    elif camillelove_count < 3:
        jump camilleneutralscene
label camillelovescene:
    show camille11 with dissolve
    hide camille07 with dissolve
    cam "Wow, I didn't know you could stand up for yourself."
    name "I’m trying to stay on top of things; I don’t want to have to cram at the last minute."
    show camillesmiling with dissolve
    hide camille11 with dissolve
    cam "Hey, you never told me if you already had sex."
    name "I’m not even going to respond."
    cam "Yeah, cause you haven't."
    cam "I can tell."
    name "Actually, I have."
    show camillesmiling2 with dissolve
    hide camille07 with dissolve
    if gender == "male":
        cam "Oh really, with a man?"
        name "No! With a girl, I am not gay."
    if gender == "fem":
        cam "Oh really, with a girl?"
        name "Yes."
    "Camille seems to enjoy making me uncomfortable."
    "She leans back on her chair."

    scene camilleapproaching
    cam "And how was the sex?"
    name "It was ok."
    cam "You don't seem convinced."
    cam "Are you still together?"
    name "Not really, I mean since I moved from my town, we won't see each other, so..."
    cam "She could come here and visit you."
    name "Yeah, it's expensive."
    cam "Yeah..."
    cam "Maybe you're glad you left."
    cam "Breaking free from the norm gives you space to uncover your true tastes."
    cam "You can be whoever you want to be."
    "I feel like whatever I say, she will turn it around."
    name "I don't know."
    cam "That's what happened with my friend the other day."
    name "Who?"
    if gender == "male":
        cam "The boy I knew from high school."
    elif gender == "fem":
        cam "The girl I knew from high school."
    cam "He was convinced he liked being dominant with girls."
    cam "And with me, he was less cocky."
    "Camille reaches for my pants."
    menu:
        "Advance my chair":
            "Move the chair ahead (end the conversation)."
            "Camille moves away."
            cam "Ugh, you're so boring."
            "The class passes by slowly."
            hide singleviewcamille02 with dissolve
            "After two hours of class, everyone leaves."
            "Finally."
            $ classdatecamille_count += 1
            $ class_done = True
            scene black with dissolve
            "I leave the classroom and head to the garden."
            jump gardenuni_start2

        "Let her touch me":                    
            scene camillereaching with dissolve
            cam "Oh yeah, cause I don't know if I told you."
            cam "He was the one getting pounded."
            cam "It was so hot, like pam pam pam."
            scene camillepant1 with dissolve
            cam "He was moaning like a dog."
            cam "It makes you horny, doesn't it?"
            cam "You wished to be as lucky as my friend."
            scene camillepant2 with dissolve
            cam "I saw it the other day."
            cam "I am sure you touched yourself thinking you were him."
            scene camilleericfinger6 with dissolve
            cam "Let me show you how it was."
            scene camilleericfinger9 with dissolve
            cam "I mean, it was so hot."
            scene camilleericfinger6 with dissolve
            cam "He was like, 'pleaaase, fuck me, fuck me, fuck me.'"
            scene camilleericfinger9 with dissolve
            cam "I kinda feel sorry for him, since he had a girlfriend."
            scene camilleericfinger6 with dissolve
            cam "I don't know how he is going to do now."
            scene camilleericfinger9 with dissolve
            cam "He will probably ask me to fuck him again."
            scene camilleericfinger6 with dissolve
            cam "And I am not sure I will."
            scene camilleericfinger9 with dissolve
            cam "I could, but I have other people to see."
            scene camilleericfinger10 with dissolve
            cam "What a tight ass you have."
            scene camilleericfinger11 with dissolve
            cam "I bet your girlfriend never did that to you."
            scene camilleericfinger10 with dissolve
            cam "Fingering your little asshole like I am doing right now."
            scene camilleericfinger11 with dissolve
            cam "Untightening it."
            scene camilleericfinger21 with dissolve
            cam "Like that."
            scene camilleericfinger22 with dissolve 
            cam "Oh, your ass is begging for it, I can tell."
            cam "He wants to be widened."
            scene camilleericfinger23 with dissolve 
            cam "Maybe he hopes that I fuck him."
            scene camilleericfinger22 with dissolve
            cam "I am not sure if you deserve it, though."
            scene camilleericfinger23 with dissolve 
            cam "Ahahah."
            scene camilleericfinger22 with dissolve
            cam "I bet you dreamed of me fucking you like a girl."
            scene camilleericfinger23 with dissolve 
            cam "Oh yeah."
            scene camilleericfinger20 with dissolve 
            cam "I just need."
            scene camilleericfinger17 with dissolve
            cam "What a little slut."
            scene camilleericfinger18 with dissolve
            cam "Letting me finger him in class."
            scene camilleericfinger17 with dissolve
            cam "Pretending he wants to study."
            scene camilleericfinger18 with dissolve
            cam "And secretly dreaming of being pounded."
            scene hotcamilleeric with dissolve
            cam "Mmmh."
            cam "Yes."
            cam "This ass must be nice to fuck."
            show camilleericfinger7hover with dissolve
            cam "Take it."
            hide camilleericfinger7hover with dissolve
            show camilleericfinger18hover with dissolve
            cam "Take it."
            hide camilleericfinger18hover with dissolve
            
            hide camilleericfinger18hover with dissolve
            show camilleericfinger7hover with dissolve
            cam "Yeah."
            show camilleericfinger18hover with dissolve
            hide camilleericfinger7hover with dissolve
            cam "Yees."
            show camilleericfinger7hover with dissolve
            hide camilleericfinger18hover with dissolve
            cam "Take it."
            show camilleericfinger18hover with dissolve
            hide camilleericfinger7hover with dissolve
            cam "Yeah."
            hide camilleericfinger18hover with dissolve
            cam "That's it, baby."
            "She fingers my ass for the rest of the class."
            scene camilleericfinger23 with dissolve 
            "Alternating between fast and slow paces."
            scene camilleericfinger22 with dissolve
            ""
            scene camillereaching2 with dissolve 
            "I try to act normal."

            scene camilleericfinger22 with dissolve
            ""
            scene camilleericfinger23 with dissolve 
            "After a few minutes, I feel my pelvis contracting."
            if gender == "male":
                "I feel the orgasm coming."
            elif gender == "fem":
                "I am gonna cum."
            scene camilleericfinger23 with dissolve 
            ""
            scene camilleericfinger22 with dissolve
            ""
            scene camilleericfinger23 with dissolve 
            ""
            scene camilleericfinger22 with dissolve
            ""
            scene camilleericfinger23 with dissolve 
            ""
            scene camilleericfinger22 with dissolve
            ""
            scene camillereaching3 with dissolve
            name "Fucck..."
            name "...."
            "..."
            "..."
            
            scene smallclassroomblur with dissolve
            "Camille withdraws her fingers."
            "A few moments later, the class ends."
            "Without a word, Camille gets up and leaves."
            "Leaving me slumped over my desk."
            "I hope no one saw us."
            $ camille_sdate_done = True
            $ class_done = True
            $ classdatecamille_count += 1
            scene black with dissolve
            "I leave the classroom and head to the garden."
            jump gardenuni_start2         
label camilleneutralscene:
    scene smallclassroomblur with dissolve
    cam "Whatever."
    "The class passes by slowly."
    "After two hours of class, everyone leaves."
    "Finally."
    $ class_done = True
    $ classdatecamille_count += 1
    scene black with dissolve
    "I leave the classroom and head to the garden."
    jump gardenuni_start2

label classcamilledate6:
    scene smallclassroomblur with dissolve
        
    "I enter the classroom and sit next to Camille."
    "I try my best to focus on the teacher's lecture."
    show camille14 with dissolve
    cam "Hey, just so we're clear,"
    cam "I am not interested in you."
    if camillelove_count >= 3:
        cam "Last time was just for fun."
    
    name "Yeah, yeah, I know..."
    cam "I won't fuck you."
    cam "I don't want another weirdo being obsessed with me."
    cam "I mean..."
    show camilleneutral2 with dissolve
    hide camille14 with dissolve
    cam "Unless you're a rich heir."

    menu:
        "I am":
            if money >= 2000:
                name "I do have money."
                "Camille looks at me with a questioning expression."
                cam "Good for you."
                show camilleneutral with dissolve
                hide camilleneutral2 with dissolve
                cam "Seriously, would you be willing to pay for...?"
                "Camille seems to be thinking.."
                cam "You really would be ready for anything."
                menu:
                    "Yes":
                        cam "Ahahah."
                        name "What?"
                        cam "Nothing. You are funny."
                        show camille05 with dissolve
                        hide camilleneutral with dissolve
                        cam "Maybe you're not as boring as I thought."
                        name "Thanks i guess."
                        hide camille05 with dissolve
                        "Camille remains silent for the rest of the class."
                        "I don't dare restart the conversation for fear of saying something embarrassing."
                        $ camille_relation_status_text == "I think she is interested in me... I should talk to her during class"
                        $ camille_moneycheck_passed = True

                    "Not everything.":
                        cam "That's what I thought..."
               

            elif money =< 2000:
                name "I actually am, but I'm not interested in you, so..."
                "Camille looks at my clothes."
                show text "Not enough money."
                pause 0.5
                hide text with dissolve
                show camille13 with dissolve
                cam "Yeah, right."
                
        "I am not interested in you anyway":
            name "I don't know why you'd assume I'd be interested in sleeping with you."
            show camille13 with dissolve
            cam "Yeah, right."
            cam "I saw you looking at my boobs."

   
    "The class passes by slowly."
    "After two hours of class, everyone leaves."
    "Finally."
    $ class_done = True
    scene black with dissolve
    "I leave the classroom and head to the garden."
    jump gardenuni_start2
label classcamilledate7:
    scene smallclassroomblur with dissolve
        
    "I enter the classroom and sit next to Camille."
    "I try my best to focus on the teacher's lecture."
    show camille06 with dissolve
    cam "Hey, do you want to do something after class?"
    name "hm? Yeah, sure.."
    name "I'm surprised you're asking me."
    show camilleneutral2 with dissolve
    hide camille06 with dissolve
    cam "We could go have a coffee at the campus pub."
    name "Oh, great, I've never been there yet."
    cam "I'll show you."
    "The class goes on as usual."
    "Once it's over, Camille gestures for me to follow her."
    cam "Come on, let's get out of here."
    scene black with dissolve
    "Camille leads me through the university hallways."
    "We head down to the garden and walk along the buildings."
    scene upview3 with dissolve
    "Eventually, we arrive at a small building that looks like a student café."
    cam "Go grab a seat, I'll be right back."
    name "Okay."
    "I sit at a table. The atmosphere is relaxed, with students chatting or working over their coffee."
    "I wonder why I've never come here before."
    
    scene camilldeunidate5 with dissolve
    
    "Camille comes back with two coffees and sits down across from me."
    cam "Here, this is for you."
    name "Thanks."
    cam "So, do you like the place?"
    name "Yeah, it's nice."
    scene camilldeunidate8c with dissolve
    "Camille takes a sip of her coffee, looking a bit thoughtful."
    name "But I don't really get why you invited me here."
    name "You usually seem so distant, it caught me off guard."
    cam "Yeah, well, sometimes I get these random urges to be nice."
    cam "But I admit, it doesn't happen often."
    name "I knew you had a good side"
    scene camilldeunidate7 with dissolve
    cam "yeaah..."
    cam "Let's just say I like people I can be a little mean to."
    cam "And you seem to fit the profile."
    name "Oh..."
    name "..."
    name "I mean, if you say so.."
    name "So you like me, we could say that?"
    scene camilldeunidate8 with dissolve
    cam "Whoa, don't get carried away."
    cam "I just like to tease you."
    "Camille takes another sip of her coffee, looking around the place."
    scene camilldeunidate5 with dissolve
    name "So, you run a blog, right?"
    cam "Yeah."
    name "Tell me about it?"
    cam "What, you want us to share our life stories?"
    name "yeah why not."
    cam "Okk.."
    scene camilldeunidate7 with dissolve
    cam "We try to create content about fashion—interviews, discovery videos, articles on trends, sometimes designer spotlights."
    name "That sounds cool. Do you do all that with your friends?"
    cam "Yeah, we're a small team. Everyone has their own role."
    name "What do you do?"
    cam "I'm the boss, obviously."
    name "Really? Wow."
    cam "I handle the writing and a bit of social media. I'm kind of an influencer in my spare time."
    cam "Gotta keep busy outside of class."
    cam "It's not like we're going to find a job here. Unless you want to become an expert in intellectual procrastination."
    name "So what kind of articles do you write?"
    cam "I do reviews of different collections."
    name "Oh, like critiques?"
    cam "Exactly. I roast designers, but with style."
    name "So you give your opinion on other people's work?"
    scene camilldeunidate5 with dissolve
    cam "Pretty much, but don't think you can just be mean for no reason. It takes work."
    cam "You have to put aside your biases and sometimes your feelings. Except when it comes to ugly shoes—then I can be ruthless."
    name "Sounds serious."
    cam "I try to do it well."
    scene camilldeunidate8c with dissolve
    cam "And you, what do you do besides asking everyone else questions?"
    name "Me? Nothing special. I go to class, work on my thesis, and try to survive."
    cam "Yeah, in 2 or 3 years you'll be lost if you don't find something to do on the side."
    name "..."
    name "Yeah, I know."
    cam "Don't make that face. Like I said, if I ever need someone for a lingerie shoot, I'll let you know."
    name "Well, maybe I'd be interested."
    cam "You could find work easily."
    cam "People are always looking for affordable models."
    cam "Of course, when you're just starting out, it doesn't pay much."
    cam "Not trying to put you on the market too fast, haha."
    name "Well, I'll think about it."
    cam "Sure."
    "After a moment, she looks at her phone."
    cam "I have to go. But this was nice. Let's do it again if you're not too clingy."
    name "Hey, if you need me, I'm here."
    "Camille gives a slight smile nad grabs her bag."
    name "Should I pay for the coffee?"
    cam "No, it's ok, don't worry."


    $ classdatecamille_count += 1
    $ class_done = True
    scene black with dissolve
    
    "I leave the café and head back to the garden."
    jump gardenuni_start2
label classcamilledate8:
    scene smallclassroomblur with dissolve
        
    "I enter the classroom and sit next to Camille."
    "I try my best to focus on the teacher's lecture."
    
    show camille07 with dissolve
    cam "Hey, do you want to grab a coffee after class?"
    menu: 
            "I'd love to":
                show camillesmiling with dissolve
                hide camille07 with dissolve
                name "oh like last time, it would be awesome"
                
                cam "Yeah, and my friend will be there too."
                cam "She works on the website with me."
                name "Oh cool, I'd love to meet her."
                name "Did you tell her about me?"
                cam "What? Why would I have done that?"
                cam "I mean, I don't know, maybe I did."
                name "What did you tell her?"
                cam "Nothing special."
                cam "Just that you had a cute butt"
                name "oh ok..."
                cam "She's cool don't worry.."
                "The class passes by slowly."
                "After two hours of class, everyone leaves."
                "Finally."
                $ classdatecamille_count += 1
                $ class_done = True
                $ camille_coffeedate_activated = True
                cam "Come on lets go."
                scene black with dissolve
                jump camilleuni_date

                
            "No, i need to study":
                name "No, I need to study."
                show camille13 with dissolve
                cam "Wow, you're really taking this student thing seriously."
                cam "I bet you iron your underwear too."
                name "I just want to focus on class..."
                cam "You're such a nerd."
                cam "But hey, when you're done organizing your paperclips by size..."
                cam "You know where to find me."
                "Camille turns back to her work, occasionally glancing over with an amused smirk."
                name "..."
                "The class passes by slowly."
                "After two hours of class, everyone leaves."
                "Finally."
               
                $ class_done = True
                
                scene black with dissolve
                "I leave the classroom and head to the garden."
                jump gardenuni_start2
label classcamilledate9: 
    scene smallclassroomblur with dissolve
        
    "I enter the classroom and sit next to Camille."
    "I try my best to focus on the teacher's lecture."
    
    show camille07 with dissolve
    cam "whats up [name]?"
    name "Not much, just trying to survive this class."
    cam "Hey, would you like to come to my place after class?"
    name "Come to your place?"
    name "Yeah awesome."
    cam "I thought you might like it."

    show camille05 with dissolve
    hide camille07 with dissolve
    cam "We could you know... chill and stuff."
    name "Chill and stuff?"
    name "I like the sound of that."
    "The class passes by slowly."
    "After two hours of class, everyone leaves."
    "Finally."
    $ classdatecamille_count += 1
    $ class_done = True
    jump camillehomedate
label classcamilledate10:
    scene smallclassroomblur with dissolve
        
    "I enter the classroom and sit next to Camille."
    "I try my best to focus on the teacher's lecture."
    show camille11 with dissolve
    name "Hello!"
    cam "Look who's here."
    cam "My little pet"
    cam "Are you having a good day?"
    name "I... yes, I think so."
    cam "I knew you'd show up quickly"
    name "I mean it was fun, i have to admit."
    name "How did your meeting go?"
    show camillesmiling with dissolve
    hide camille11 with dissolve
    cam "Great, the guy is interested in what we're doing"
    cam "It was more about networking than real professional collaboration."
    cam "But he's someone important."
    cam "I know how to make myself desirable in these situations"
    name "I bet."
    cam "It's really important to know how to leave your mark in people's minds."
    cam "So they don't forget you."
    cam "Especially in this industry."
    name "I'm glad it went well."
    cam "Yeah.."
    show camille11 with dissolve
    hide camillesmiling with dissolve
    cam "Speaking of leaving your mark.."
    cam "Do you want to come to my place after class?"
    cam "I'm in the mood to be served."
    menu:
        "Yes, I want to":
            cam "Perfect."
            jump camilleshokerdate

            
        "No, I need some time":
            cam "Hmm, that's... unfortunate."
            cam "I thought you understood where this was leading to."
            cam "Well, when you're ready to stop playing games, let me know."
            scene black with dissolve
            "The class passes by slowly."
            "After two hours of class, everyone leaves."
            "Finally."
            
            $ class_done = True
    
            "I leave the classroom and head to the garden."
            jump gardenuni_start2

            
label classcamilledate11:
    scene smallclassroomblur with dissolve
        
    "I enter the classroom and sit next to Camille."
    "I try my best to focus on the teacher's lecture."
    show camilleneutral2 with dissolve
    name "Hey..."
    cam "You back for more?"
    name "I guess."
    cam "I suppose you're ready to be completely mine."
    name "What do you mean?"
    cam "I mean, you know, you could stay at my place more"
    cam "I could take care of you."
    show camilleneutral1 with dissolve
    hide camilleneutral2 with dissolve
    name "I thought you didn't want someone to be obsessed with you."
    cam "You seem discreet, I like that."
    cam "You won't harass me with messages."
    cam "So do you want to come to my place after class?"
    menu:
        "Yes, I want to":
            cam "Perfect."     
            cam "I suppose you've understood that you need to be totally mine."
            cam ""
            name "I think I need that."
            "..."
            jump camillebonusdate
           

        "No, I am not ready for that":
            cam "Hmm, that's... unfortunate."
            cam "But i understand."

            cam "Well, when you're ready to stop playing games, let me know."
            "The class passes by slowly."
            "After two hours of class, everyone leaves."
            "Finally."
            $ class_done = True
            scene black with dissolve
            "I leave the classroom and head to the garden."
            jump gardenuni_start2
    
  





# //////////////////////////////Random////////////////////////
label classdate2:
    scene smallclassroom
    "I enter the classroom and sit at a table."
    "I try my best to focus on the teacher's lecture."
    show camille00
    cam "Do you like plants?"

    name "Uh, yeah, I guess. Why?"

    cam "Because you look like a plant."
    $ classdate_count += 1

    name "What?"

    cam "Yeah, like you could just stand there all day without moving."

    name "Very funny."

    hide camille
    "The class passes by slowly."
    "After two hours of class, everyone leaves."
    "Finally."
    $ class_done = True
    scene black with dissolve
    "I leave the classroom and head to the garden."
    jump gardenuni_start2

label classdate3:
    scene smallclassroom
    "I enter the classroom and sit at a table."
    "I try my best to focus on the teacher's lecture."
    show samuel
    sam "I need a coffee."
    $ classdate_count += 1
    name "Are you allowed to go get one during class?"

    sam "Yeah, but I don't have much money to spare right now."

    name "Yeah, I feel you. I'm broke too."

    sam "It's not like I have parents that can pay for my coffee."

    sam "I have to work for it."

    name "I am sorry to hear that."

    sam "I am not complaining, I am just saying."

    sam "I am not a spoiled brat."

    sam "Like some people here..."

    name "I understand."
    hide samuel
    "The class passes by slowly."
    "After two hours of class, everyone leaves."
    "Finally."

    $ class_done = True
    scene black with dissolve
    "I leave the classroom and head to the garden."
    jump gardenuni_start2

label classdate4:
    scene smallclassroom
    "I enter the classroom and sit at a table."
    "I try my best to focus on the teacher's lecture."

    show estellesmile with dissolve

    est "Hey there."
    name "Hi."
    est "Can I sit here?"
    name "Yes, go ahead. It's free."
    est "Thanks."
    est "What's your name?"
    name "I'm [name]. You?"
    est "Estelle."
    est "I love this class."
    est "The professor is kinda charming."
    name "Yes... why not?"
    est "I think I'm going to ask him to be my thesis advisor."
    name "Cool."
    hide estellesmile with dissolve
    "The class passes by slowly."
    "After two hours of class, everyone leaves."
    "Finally."
    $ estelle_firstconv_done = True
    $ classdate_count += 1
    $ class_done = True
    scene black with dissolve
    "I leave the classroom and head to the garden."
    jump gardenuni_start2

label classdate5:
    scene smallclassroom
    "I enter the classroom and sit at a table."
    "I try my best to focus on the teacher's lecture."
    show estellewondering with dissolve
    est "I can't focus. I'm so tired."

    name "Go get a coffee."

    est "I'm trying to quit caffeine."

    est "It makes me jittery."

    name "Studying without coffee is like driving without gas."

    est "I knooow."

    est "But I still smoke."
    est "I would die otherwise."
    hide estellewondering with dissolve
    "The class passes by slowly."
    "After two hours of class, everyone leaves."
    "Finally."
    
    $ classdate_count += 1
    $ class_done = True
    scene black with dissolve
    "I leave the classroom and head to the garden."
    jump gardenuni_start2

label classdate5_1:
    scene smallclassroom
    "I enter the classroom and sit at a table."
    "I try my best to focus on the teacher's lecture."
    show estellewondering with dissolve
    est "Hey there."
    name "Hey."
    est "Can I ask you something?"
    name "Sure."
    est "Why does Camille spank you like that?"
    est "I mean, no kink shaming, but..."
    name "What? It's just a joke between us."
    est "Right..."
    est "I mean, I'm not judging you."
    est "It feels like getting spanked might be your thing."
    est "It's just... funny."
    est "But hey, no judgment."
    est "It's a free country."
    
    $ estelle_spankconv_done = True
    hide estellewondering with dissolve
    "The class drags on slowly."
    "After two hours, everyone finally leaves."
    "At last."
    $ classdate_count += 1
    $ class_done = True
    scene black with dissolve
    "I leave the classroom and head to the garden."
    jump gardenuni_start2

label classdate6:
    scene smallclassroom
    "I enter the classroom and sit at a table."
    "I try my best to focus on the teacher's lecture."

    show estellesmile with dissolve
    est "What's up?"
    name "Nothing much."
    est "Really?"
    est "I had the impression that you were quite busy lately."
    name "What do you mean?"
    est "I mean..."
    est "With Emma."
    est "Are you two dating or something?"
    name "Oh no, not really."
    est "No? But you followed her into the restrooms, right?"
    name "What?"
    est "I mean, it's just something I heard."
    est "That you did..."
    est "Sucked her dick in the restrooms."
    "She holds back a laugh."
    name "Pff, whatever."
    est "Did she cum in your mouth?"
    name "Why would you want to know that?"
    est "I don't know."
    est "It's just... to get to know you better, i guess.."

    "The class drags on slowly."
    "After two hours, everyone finally leaves."
    "At last."
    $ estelle_emmaconv_done = True
    $ classdate_count += 1
    $ class_done = True
    scene black with dissolve
    "I leave the classroom and head to the garden."
    jump gardenuni_start2

label classdate6_1:
    scene smallclassroom
    "I enter the classroom and sit at a table."
    "I try my best to focus on the teacher's lecture."

    show estellesmile with dissolve
    est "Helloo."
    name "Hi."
    est "What the fuck was that last time?"
    name "What?"
    est "What do you mean 'what?'"
    est "Camille."
    est "She was playin' with your ass during class?!!"
    name "You were probably imagining things."
    est "You are so wild, ahah."
    est "Figured you'd sneak a quickie without anyone noticing?"
    est "Not on my watch."
    name "Yeah, sure."
    est "Seems like..."
    est "You're kinda a slut."
    est "Guess appearances can be deceiving, huh?"
    name "Shut up..."
    est "Don't worry, your secrets are safe with me."
    $ classdate_count += 1
    $ class_done = True
    scene black with dissolve
    "I leave the classroom and head to the garden."
    jump gardenuni_start2

label classdaterandom:
        scene smallclassroom
        "I enter the classroom and sit at a table."
        "I try my best to focus on the teacher's lecture."
        
        # Random chance to get different events
        $ random_event = renpy.random.randint(1,4)
        
        if random_event == 1:
            show samuel
            sam "This class is so boring..."
            name "Yeah, I know what you mean."
            sam "I'm only here because I need to ."
            "Samuel spends the rest of class doodling in his notebook."
            
        elif random_event == 2:
            "The person next to me falls asleep during the lecture."
            "Their gentle snoring is actually kind of relaxing."
            "I let them sleep through class."
            
        elif random_event == 3:
            show estellewondering
            est "Do you understand any of this?"
            name "Sort of... want to compare notes after class?"
            est "That would be great, thanks!"
            "We exchange confused looks for the rest of the lecture."
            
        elif random_event == 4:
            "A paper airplane soars across the classroom."
            "The teacher pretends not to notice."
            "College students will be college students..."

        $ classdate_count += 1
        $ class_done = True
        scene black with dissolve
        "I leave the classroom and head to the garden."
        jump gardenuni_start2


#////////////////////////////////// Emma///////////////////////////
label classemmadate:
    scene smallclassroom
    "I enter the classroom and sit at a table."
    "I try my best to focus on the teacher's lecture."
    show emma03
    emm "Hey, can I sit here?"

    name "Yeah, sure."

    emm "Thanks."

    emm "You seem like an interesting person."

    name "Oh, really? No one's ever told me that before."

    emm "Yeah, you look like you're always deep in thought."
    $ classdateemma_count += 1
    name "Haha, not really, but thanks, I guess."
    hide emma03
    "The class passes by slowly."
    "After two hours of class, everyone leaves."
    "Finally."
    $ class_done = True
    scene black with dissolve
    "I leave the classroom and head to the garden."
    jump gardenuni_start2
label classemmadate1:
    scene smallclassroom
    "I enter the classroom and sit at a table."
    "I try my best to focus on the teacher's lecture."
    show emma03
    emm "Are you an artist?"

    name "No, not really. Why?"

    emm "I’m looking for someone to draw my portrait."
    $ classdateemma_count += 1
    emm "You seem like the creative type."

    emm "The kind who daydreams and draws weird stuff all day."

    name "No, not really, sorry. But if I find someone who can help, I’ll let you know."

    emm "Thanks, that’s nice of you."

    hide emma03
    "The class passes by slowly."
    "After two hours of class, everyone leaves."
    "Finally."
    $ class_done = True
    scene black with dissolve
    "I leave the classroom and head to the garden."
    jump gardenuni_start2
label classemmadate2:
    scene smallclassroom
    "I enter the classroom and sit at a table."
    "I try my best to focus on the teacher's lecture."
    show emma04
    emm "Hey partner."
    emm "Can I tell you something?"

    name "What?"

    emm "I mean, it might sound a bit weird."

    emm "Don't take it the wrong way."

    name "I'm ready."

    "She whispers in my ear."

    emm "You seem really slutty."

    name "What?"

    emm "Yeah, I know it's a weird thing to tell someone."

    emm "How does that make you feel?"

    name "WTF?"

    emm "Nobody ever tells you that?"

    name "Huh, not really..."

    emm "You should be flattered."

    name "I am not sure about that."

    name "And you decided to tell it to me just like that?"

    emm "It was on my mind for a while, so I needed to tell you."

    emm "You're a sneaky one!"
    emm "But it's something in your eyes."

    emm "I bet you're wild between the sheets."

    name "Stop it, it's embarrassing."

    emm "Ahahah."

    emm "Aww, don't be shy."
    "The class passes by slowly."
    "After two hours of class, everyone leaves."
    "Finally."
    hide emma04
    $ classdateemma_count += 1
    $ class_done = True
    jump gardenuni_start2
label classemmadate3:
    scene smallclassroom
    show emma04
    if gender == "male":
        emm "Hey there, buddy! Catch any shut-eye last night?"
    elif gender == "fem":
        emm "Hey there, girl! Catch any shut-eye last night?"
    name "Hey, it was okay."

    emm "Man, I was tossin' and turnin' all night."
    emm "What's your go-to sleep trick?"

    name "I just check my phone till I black out."
    name "And you?"
    emm "I think of you and give myself a treat."
    name "Oh."
    emm "I am joking, don't make that face."
    "Is she though?"
    "The class passes by slowly."
    "After two hours, everyone leaves."
    "Finally."
    $ classdateemma_count += 1
    $ class_done = True
    scene black with dissolve
    "I leave the classroom and head to the garden."
    jump gardenuni_start2
label classemmadate4:
    scene smallclassroom
    show emma04
    emm "Hey you."

    name "What's up?"

    emm "You look so handsome today."

    name "Thanks."

    emm "You're glowing, like an angel."

    emm "Did you dress up for me?"

    name "What? Why would I do that?"

    emm "Because you crave me?"

    name "Yeah, sure."

    emm "I can see it in your eyes."

    emm "Don't lie to me."

    emm "I know you want it to go further."

    name "We barely know each other."

    emm "I know, but I want to get to know you better."

    name "What, you want me to give you my life story?"

    emm "I don't know, just tell me more about yourself."

    name "Well, I don't know what to say. I arrived here a few days ago."

    name "Before that, I used to live in a small town in the countryside."

    name "I..."

    "I feel a pressure against my leg."
    hide emma04
    scene handsexy05
    name "Hey, what are you doing?..."
    emm "What? I'm listening."
    scene handsexy04 with dissolve
    name "Your hand..."
    emm "It doesn't mean I am not listening. It's just a friendly gesture to make you feel comfortable."
    name "Is it supposed to make me feel comfortable?"
    scene handsexy05 with dissolve
    emm "Try removing it if it bothers you."
    name "I'm not going to do that, you'll resist and it will be even more embarrassing."
    name "I'll just wait for you to remove it."
    scene handsexy04 with dissolve
    emm "You'll be waiting a long time then."
    "She gently strokes my leg from bottom to top."
    "The sensation is pleasant, but I try not to show it."
    emm "You were saying? Living in a small town...?"
    emm "You must be a little lost here, right?"
    scene handsexy05 with dissolve
    name "I mean, I'm not a hick either."
    emm "Ahah, I bet you've already gotten lost in the subway."
    name "Well... it's a bit hard to find your way around at first, but I got used to it."
    emm "I bet you'll become a real city dweller in no time, you'll see."
    scene handsexy06 with dissolve
    emm "Have you ever had a girlfriend?"
    name "Mh, I do have a girlfriend actually..."
    emm "You've never had a real girlfriend."
    emm "I mean someone who understands your cravings and knows just how to make you moan."
    emm "Aren't you curious to know what it feels like?"
    name "... I guess..."
    emm "I knew it."
    "She raises her hand and plunges it into my pants."
    
    scene handsexy07
    emm "Let's see what you've got underneath."
    if gender == "male":
        "She grabs my penis and starts rubbing it."
        emm "Do you want to be my boyfriend?"
    elif gender == "fem":
        "She grasps my pussy and tenderly rubs it."
        emm "Do you want to be my girlfriend?"
   
    name "I... I am not sure how it would work."
    emm "Meet me in the corridor after class, I'll show you."
    name "What do you want to do?"
    emm "You'll see."
    "Suddenly, the teacher announces the end of the class."
    "Emma quickly removes her hand. Everyone stands up and leaves the classroom."
    "As she exits, Emma winks at me. It was kinda pleasant. But should I follow her?"
    $ emma_date_started = True
    $ classdateemma_count += 1
    $ class_done = True
    $ emma_relation_status_text = "I think Emma is waiting for me in the university corridors."

    scene black with dissolve
    "I leave the classroom and head to the garden."
    jump gardenuni_start2
label classemmadate5:
    if emma_date_done == False:
        scene smallclassroom
        show emma04 
        emm "Hey, just so you know, my offer still stands."
        hide emma04
        "The class passes by slowly."
        "After two hours, everyone leaves."
        "Finally."
        $ emma_date_started = True
        $ class_done = True
        $ emma_relation_status_text = "I think Emma is waiting for me in the university corridors."
        scene black with dissolve
        "I leave the classroom and head to the garden."
        jump gardenuni_start2
    elif emma_date_done == True:
        scene smallclassroom
        show emma04     
        "Thanks for playing!"
        "This story is still in development."
        jump gardenuni2


    