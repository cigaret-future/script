label rosedate:
    default club = Character('Club people', color="#66668f")
    "I'm getting ready to go out."
    "I think I'll try to dress a little sharper tonight."
    "At least mix things up a bit."
    "Once I'm ready, I step out into the street."
   
    scene streetcut2
    "The night has already fallen—thick, velvet-dark, the kind that swallows the edges of buildings and turns street-lamps into hazy gold islands."

    scene rosedate-arriving
    "I arrive at the club, the music pounding through the walls."
    n_nvl "Hey, I am at the club, you here?"
    $ renpy.pause(3, hard = True)
    "No answer..."
    "I'll go in anyway, we'll see what happens."
    "I hope the bouncer will let me in."
    scene black
    "I wait outside for several minutes."
    "People around me are already getting excited, a mix of enthusiasm and nervousness."
    "Then after about ten minutes the bouncer lets us in in groups of 10."
    play music clubmusicambiance volume 1 loop fadein 0.5
    $ renpy.music.set_volume(0.3, delay=0.5, channel="music")
    
    scene chloedate2enteringclub
    $ renpy.music.set_volume(1, delay=0.5, channel="music")
    "This time, I already feel more used to the noise level."
    "But it's still impressive to see the crowd dancing so wildly."
    "..."
    "Where's Chloe?"
    "She still hasn't replied."
    "I'll grab a drink while I wait."
    scene black with dissolve
    "I head to the bar to order a gin and tonic."

    scene rosedate-sittingwaiting2 with dissolve
    "I sit in the same spot where I was with Chloe last time."
    "People around me burst into laughter."
    "I'm not completely at ease."
    scene rosedate-sittingwaiting with dissolve
    "Maybe there are people I know here?"
    "Linda, maybe?"
    "No, not Linda."
    default chloedate2_text_count = 0
    default chloedate2_drink_count = 0
    default chloedate2_bathroom_count = 0
    default chloedate2_talk_count = 0
    default chloedate2_text_date = False

    scene rosedate-sittingwaiting3b with dissolve
    "I scan the room for a familiar face."
    "But I don't see anyone."
    "What is Chloe doing?"

    "I need to find something to do while I wait..."

    label date2somethingtodo:
        scene rosedate-sittingwaiting with dissolve
        menu:
            "Go to the bathroom":
                $ chloedate2_bathroom_count += 1
                if chloedate2_bathroom_count == 1:
                    scene chloedate_bathroom
                    "I slip between bodies; the music follows me all the way to the hallway."
                    
                    "I splash water on my face and inhale deeply."
                    "In the glass, I think I look a little more… desirable tonight."
                    "I lean in, adjust my shirt to hint at the line of my collarbone."
                    "I hear some noises coming from the stalls."
                    "I step back out, heart beating faster."
                elif chloedate2_bathroom_count == 2:
                    scene chloedate_bathroom
                    "I slip between bodies; the music follows me all the way to the hallway."
                    
                    "In the bathroom, I splash cold water on my face and exhale."
                   
                    "Suddenly someone calls my name."
                    scene chloedate_bathroomblur with dissolve
                    show emma00 with dissolve
                    emm "Hey, [name]? That really you?"

                    name "Emma? What are you doing here?"
                    show emma01 with dissolve
                    hide emma00 with dissolve
                    emm "Me? You’re the one in a club. You go out now?"

                    emm "Who’re you with?"

                    name "Just… me."
                    show emma05 with dissolve
                    hide emma01 with dissolve
                    emm "Wow. Bold. Didn’t peg you for the solo-night-out type."

                    emm "Guess the city’s rubbing off on you."

                    name "Yeah… something like that."

                    emm "So…"

                    name "Yeah."
                    show emma04 with dissolve
                    hide emma05 with dissolve
                    emm "Enjoy your night, I guess."

                    "She flashes a quick smile and slips back into the noise."
                    hide emma04 with dissolve
                elif  chloedate2_bathroom_count == 3:
                    scene chloedate_bathroom
                    "I slip between bodies; the music follows me all the way to the hallway."
                    "I splash water on my face and take a deep breath."
                    "I hear some noises coming from the stalls."
                    "I hear the door opening behind me."
                    with hpunch
                    "Before I can turn around, I feel someone grab me by the waist."
                    "It's Emma!"
                    scene chloedate_bathroomblur with dissolve
                    emm "You okay?"
                    menu:
                        "Push her away":
                            scene chloedate_bathroomblur with dissolve
                            name "Yeah.. maybe leave me some space."
                            "I push her away and go back to my seat."

                        "Let her do what she wants":
                            scene chloedate_bathroomblur with dissolve
                            "Without waiting for my answer, Emma grabs me and takes me into one of the stalls."
                            "The door slams shut behind us. Emma locks it with a flick of her wrist." 
                            "She pushes me down on the seat and lowers her pants."
                            play sound pantdown
                            scene emmadateclub-bathroom with dissolve
                            "Emma bends over and spreads her cheeks, positioning her rear close to my face."
                            "With one movement, she presses herself against my mouth."

                            "I lean in. My tongue finds her tight ring — warm, musty. I trace, press, flatten."
                            "She exhales through her teeth. Her hips rock back, pushing against my mouth."
                            "I lick it clean, without a word."
                        
                            scene emmadateclub-bathroom2 with dissolve
                            window hide
                            pause
                            play sound zoeykiss volume 1 loop
                            play voicebis moaningemma volume 1 loop

                            scene emmadateclub-bathroom3 with dissolve
                            window hide
                            pause


                            

                            scene emmadateclub-bathroom4 with dissolve
                           

                            emm "You like this?..."
                            "I lick deeper, circling, probing."

                            scene emmadateclub-bathroom3 with dissolve
                            
                          

                            scene emmadateclub-bathroom2 with dissolve
                            window hide
                            pause


                         
                            scene emmadateclub-bathroom3 with dissolve
                            
                            window hide
                            pause

                            scene emmadateclub-bathroom4 with dissolve
                        
                            window hide
                            pause

                            scene emmadateclub-bathroom3 with dissolve
                            window hide
                            pause

                            scene emmadateclub-bathroom2 with dissolve
                            
                            window hide
                            pause

                            scene emmadateclub-bathroom3 with dissolve
                            "I do my best to please her."
                            "Her breath hitches. My tongue presses flat, relentless against her flesh."


                            scene emmadateclub-bathroom4 with dissolve
                            window hide
                            pause

                            scene emmadateclub-bathroom3 with dissolve
                            window hide
                            pause
                       

                            scene emmadateclub-bathroom4 with dissolve
                            
                            window hide
                            pause
                       
                            scene emmadateclub-bathroom3 with dissolve
                            window hide
                            pause


                            scene emmadateclub-bathroom2 with dissolve
                            

                            window hide
                            pause


                            scene emmadateclub-bathroom3 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom4 with dissolve
                            window hide
                            pause

                            scene emmadateclub-bathroom3 with dissolve
                            window hide
                            pause
                       

                            scene emmadateclub-bathroom4 with dissolve
                            
                            window hide
                            pause
                       
                            scene emmadateclub-bathroom3 with dissolve
                            window hide
                            pause


                            scene emmadateclub-bathroom2 with dissolve
                            

                            window hide
                            pause
                            scene emmadateclub-bathroom4 with dissolve
                            window hide
                            pause

                            scene emmadateclub-bathroom3 with dissolve
                            window hide
                            pause
                       

                            scene emmadateclub-bathroom4 with dissolve
                            
                            window hide
                            pause
                       
                            scene emmadateclub-bathroom3 with dissolve
                            window hide
                            pause


                            scene emmadateclub-bathroom2 with dissolve
                            

                            window hide
                            pause


                            scene emmadateclub-bathroom3 with dissolve

                            scene emmadateclub-bathroom3 with dissolve

                            scene emmadateclub-bathroom5 with dissolve
                            "Her hand wraps around her thick shaft, stroking slow and steady."
                            "Her other hand grabs my hair, pushing my face between her cheeks."
                            scene emmadateclub-bathroom6 with dissolve
                            play background handjob2 volume 1 loop
                            window hide
                            pause
                        

                            scene emmadateclub-bathroom5 with dissolve
                            
                            "She strokes faster — wet, slick sounds mixing with the muffled music." 
                            

                            scene emmadateclub-bathroom8 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom5 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom6 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom5 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom8 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom5 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom6 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom5 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom8 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom5 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom6 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom5 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom8 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom5 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom6 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom5 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom8 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom5 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom6 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom5 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom8 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom5 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom6 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom5 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom8 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom5 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom6 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom5 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom8 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom5 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom6 with dissolve
                            window hide
                            pause
                            
                            scene black with dissolve
                            window hide
                            pause
                            "After long minutes spent eating her ass, she starts to speed up the pace."
                            play sound handjobfast volume 1 loop
                            scene emmadateclub-bathroom8 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom5 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom6 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom5 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom8 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom5 with dissolve
                            "She grinds back hard, smothering me, thighs trembling."
                            scene emmadateclub-bathroom6 with dissolve
                            "She’s close. I feel it in the jerk of her hips."
                            "I push deeper, eager for the climax."
                            scene emmadateclub-bathroom5 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom8 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom5 with dissolve
                            window hide
                            pause
                            play voicebis climax volume 1 noloop
                            scene emmadateclub-bathroom6 with dissolve
                            "Her cock swells in her grip."
                            scene emmadateclub-bathroom8 with dissolve
                            "She comes — hot, thick ropes splattering the stall wall."
                            scene emmadateclub-bathroom6 with dissolve
                            "Her hips stutter, riding my tongue through every pulse."
                            scene emmadateclub-bathroom8 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom6 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom8 with dissolve
                            
                            scene emmadateclub-bathroom6 with dissolve
                            window hide
                            pause
                            scene emmadateclub-bathroom8 with dissolve
                            window hide
                            scene black with dissolve
                            stop voicebis
                            stop sound
                            stop background
                            "Her grip loosens. She sags forward."
                            "I step back, catching my breath."
                            "Without a word, she get out of the stall and leave the bathroom."

                jump date2somethingtodo


            "Talk to people around me":
                $ chloedate2_talk_count += 1
                
                if chloedate2_talk_count == 1:
                    "I turn to the couple on my left. Two girls are laughing together, somehow louder than the music."
                    
                    name "Hey… uh, first time here?"
                    
                    "The brunette with silver hoop earrings glances at me."
                    
                    club "No, we are regulars, you?"
                    
                    name "Same. My friend was supposed to show up an hour ago."
                    
                    "The blonde snorts into her drink."
                    
                    club "Ghosted? Unusual for a guy, isn't it?"
                    
                    name "Yeah I don't know..."
                    
                    "They both laugh. I relax a little."
                    
                    club "Classic. You’re flying solo then?"
                    
                    name "Looks like it."
                    
                    club "We’ve all been there. Waiting on someone who never shows."
                    
                    name "Yeah… still checking my phone every five minutes."
                    
                    club "Put it away. The night’s not over."
                    
                    "I nod, unsure what to say next. They go back to their conversation."
                    
                else:
                    "I turn to the two girls on my left."
                    "They smile, but their attention drifts back to their drinks."
                    



                jump date2somethingtodo

            "Get another drink":
                $ chloedate2_drink_count += 1
                scene black with dissolve
                "I swallow down the rest of my glass and head to the bar."
                scene nightdate_barmanscene

                if chloedate2_drink_count == 1:
                    "I inch forward in the slow-moving line, bodies pressed tight, until I reach the counter."
                    "Then I lean in and shout over the bass:"
                    name "ONE GIN AND TONIC, PLEASE!"
                    "The bartender nods silently, already shaking."
                    "While he preps, I let my eyes drift across the crowd."
                    club "Ever seen the floor blow up like this on a Tuesday?"
                    "A guy to my right jerks his chin toward the dance floor."
                    name "I don't come here often."
                    name "But yeah, it's really intense."
                    club "Big-name DJ spinning tonight. Usually only does festivals."
                    "He snickers, taps his glass on the counter."
                    club "Stick around till the end—he drops an exclusive edit. Worth it."
                    name "Noted. Thanks for the tip."

                elif chloedate2_drink_count == 2:
                    "Another slow shuffle through the crowd, elbows and perfume."
                    "At the counter I yell:"
                    name "GIN AND TONIC!"
                    "Bartender nods, no words."
                    scene nightdate_barmanscenetwogirls
                    "Two young women in crop-tops lean in from my right."

                    club "Third one tonight, lightweight?"
                    club "He’s counting the ice cubes — look!"
                    club "Bet he’s writing a Yelp review in his head."
                    "They giggle playfully."
                    name "Hey, hydration is important."
                    club "Sure, sure. Next round’s on us if you survive the drop."

                elif chloedate2_drink_count == 3:
                    "Queue’s worse now; I wait, shoulder-to-shoulder."
                    "Finally:"
                    name "GIN TONIC!"
                    "Silent nod from the bartender."
                    scene nightdate_barmanscenetwogirls
                   
                    club "Back again? That’s your fourth drink, right?"
                    club "You’re gonna be peeing every five minutes soon."
                    club "Or are you just trying to drown the boredom?"
                    name "I can drink as much as I want, so that's what I'm going to do!"
                    club "Yeah, yeah. Keep going like that and you’ll be hugging the toilet by midnight."
                    club "We’ll wave from the dance floor."

                elif chloedate2_drink_count == 4:  # 4th+ drink
                    "Slow crawl to the front, music pounding."
                    name "GIN AND TONIC, PLEASE!"
                    "Bartender nods, mechanical."
                    "A pretty futa in a loose black mesh dress leans in next to me, neckline low enough to show her breasts."
                    "I look, trying not to make it obvious."
                    "She’s scrolling her phone, one eyebrow raised."
                    scene nightdate_barmanscene2
                    "Suddenly she looks at me."
                    "She looks a little tipsy, eyes glassy under the strobes, one hand lazily propping her head."
                    club "You’ve had, what, three of those already?"
                    club "At least?"
                    "She glances at my empty glass, then back to her screen."
                    club "I’m counting. You’re on autopilot."
                    name "Keeps the night simple."
                    club "Simple’s fine. Boring’s the problem."
                    "She pockets her phone, shrugs."
                    club "Whatever. It's not my liver."

                    club "So… you waiting on someone?"
                    "She tilts her head, half-smirk, half-bored."
                    name "Yeah. But I’m not against meeting new faces."
                    club "Cute."
                    "She takes a slow sip of her neon drink."
                    club "I’ve already got someone who keeps me plenty busy. No vacancies."
                    name "Really?"
                    club "Yeah. Cute little thing, barely five-foot, begs me to pin him down every night."
                    "She licks a drop from the rim of her glass."
                    "I choke on air, heat flooding my face so fast the strobes blur."
                    "My imagination is running wild."
                    "My mouth opens, nothing comes out, then I manage a strangled..."
                    name "...wow"
                    club "Last night I had him face-down on the kitchen counter, wrists tied with my belt. Still whimpering when I left for work."
                    club "So yeah — no openings tonight. Maybe another time cutie."
                    club "But good luck out there, autopilot boy."
                    "She just snorts, amused, and turns away."
                    "The bartender slides my drink and clears his throat."
                    club "Hey, keep the lane clear."
                    "She grabs her glass and steps aside without another word."
                elif chloedate2_drink_count == 5:
                    "It's a slow crawl to the front, music pounding."
                    name "GIN AND TONIC, PLEASE!"
                    "Bartender nods, mechanical."
                    "I finish my drink, my head starting to spin a little from all the alcohol."
                    "I should go dance, it'll help clear my head."
                    jump dancingandmeettingrose
                scene black with dissolve
                window hide
                pause
                jump date2somethingtodo




            "Text Chloe again":
                if chloedate2_text_count == 0:
                    n_nvl "Heeey! where are you?"
                    $ renpy.pause(3, hard=True)
                    "Nothing.."
                    $ chloedate2_text_count += 1
                    jump date2somethingtodo

                elif chloedate2_text_count == 1:
                    n_nvl "I'm in the same spot as last time."
                    n_nvl "When are you coming?"
                    
                    $ renpy.pause(3, hard=True)
                    "Nothing.."
                    nvl clear
                    $ chloedate2_text_count += 1
                    jump date2somethingtodo

                elif chloedate2_text_count == 2:
                    $ chloedate2_text_count += 1
                    n_nvl "Chloe, seriously. I’m here alone like an idiot."
                    n_nvl "If you’re not coming, just say it."
                    
                    $ renpy.pause(4, hard=True)
                    "Still nothing. The screen stays dark."
                    scene black
                    "Maybe I should try to call her."
                    "I duck into a quiet corner near the emergency exit, music thumping through the wall."
                    nvl clear
                    scene nightdate_ericcalling with dissolve
                    "I press the call button next to Chloe's name."
                    $ renpy.pause(1.5)
                    "..."
                    $ renpy.pause(1.0)
                    name "Chloe? …Yeah, it’s me."
                    "Her voice crackles through, muffled by the club noise."
                    chloe "(inaudible, fast, apologetic)"
                    name "I — what? No, I can’t hear you…"
                    chloe "(inaudible, louder, something about traffic / friends / sorry)"
                    name "…When are you going to arrive??"

                    "I hang up."

                    "The phone barely leaves my ear when the door beside me swings open."
                    scene nightdate_ericcalling2
                    "A bouncer steps out from behind it."

                    club "Corner’s off-limits for phone calls, sweetheart."

                    club "Club rules. No loitering by the emergency exit."

                    "She folds her arms, biceps flexing; the hallway light catches the faint stubble on her jaw."

                    club "Move back to the bar or I walk you out myself."

                    "Her eyes flick down my body, slow, deliberate, then back up."

                    club "Come on, hurry up, don’t make me wait."
                    club "She stares at me strangely, like she’s daring me."
                    "I shoot her a frightened glance, then obey."
                    if gender == "male":
                        club "Good boy."
                        club "Don't play smart with me."
                    else:
                        club "Good girl"
                        club "Don't play smart with me."
                    "Better not push her."
                    scene black
                    "Back at the table, I sink into the seat."
                    
                    jump date2somethingtodo
                elif chloedate2_text_count == 3:
                    $ chloedate2_text_count += 1
                    "I open a new chat."
                    n_nvl "Hey babe… just chilling at home."
                    n_nvl "TV’s boring, thought I’d text you ❤️"
                    $ renpy.pause(2.5)
                    "Typing…"
                    m_nvl "Aww missed your voice already."
                    m_nvl "What are you up to? 😊"
                    n_nvl "Nothing much, just in bed scrolling."
                    n_nvl "Kinda lonely without you here."
                    m_nvl "Same 💕 tell me about your day?"
                    n_nvl "Eh, same old. Work, gym, now this."
                    n_nvl "Wish you were here to cuddle."
                    m_nvl "Soon baby, promise"
                    m_nvl "send me a sleepy selfie? 🥺"
                    n_nvl "Ok wait..."
                    "I angle the camera away from the strobing lights, fake a yawn."
                    m_nvl "Cute 🥰 night babe"
                    n_nvl "Night ❤️"
                    jump date2somethingtodo
                elif chloedate2_text_count >= 4 and chloedate2_text_date == False:
                
                    "*bzzzzt*"
                    "Incoming call: **Chloe**."
                    "I duck back into the hallway by the emergency exit."
                    scene nightdate_ericcalling with dissolve
                    "I swipe."
                    name "Chloe?"
                    chloe "(inaudible, fast, apologetic, traffic / friends / late)"
                    name "I...what? I can’t hear you..."
                    chloe "(inaudible, louder, maybe 20 minutes, maybe not)"

                    "The door creaks open behind me."
                    scene nightdate_bouncersscene1 with dissolve
                    "The bouncer steps in."
                    club "Still here? I told you, no loitering."
                    "I keep the phone to my ear."
                    chloe "(inaudible, still talking, excuses piling up)"
                    club "What’s your problem? Trying to piss me off?"
                    "She steps closer, voice rising over the muffled music."
                    club "I said move."
                    "Chloe’s voice crackles, overlapping."
                  

                    menu:
                        "Hang up and leave":
                            name "Whatever. Text me when you’re actually here."
                            "I end the call, pocket the phone."
                            name "No, I’m going."
                            "I step past her."
                            if gender == "male":
                                club "Good boy."
                            else:
                                club "Good girl."
                            club "Don’t make me say it twice."
                            scene black
                            "I push back into the club."
                            jump date2somethingtodo

                        "Keep talking, ignore her":
                            "I turn my shoulder, still on the line."
                            scene nightdate_bouncersscene2 with dissolve
                            name "Chloe, I literally can’t hear a word—"
                            chloe "(inaudible, louder, defensive)"
                            club "Hey. Phone down. Now."
                            "I don’t move."
                            club "You deaf or just stupid?"
                            "She grabs my upper arm — firm, not painful."
                            club "Last warning."
                            "Chloe keeps babbling in my ear."
                            club "What’s your problem? Trying to get me worked up?"

                            menu:
                                "Hang up before she snaps":
                                    name "Chloe, I’ll call you back."
                                    "I end the call quickly, pocket the phone."
                                    name "Sorry, I’m leaving."
                                    "I step past her."
                                    if gender == "male":
                                        club "Smart boy."
                                    else:
                                        club "Smart girl."
                                    club "Don’t let me catch you here again."
                                    scene black
                                    "I hurry back into the club."
                                    jump date2somethingtodo
                                "Maybe...":
                                    scene nightdate_bouncersscene3
                                    name "…Maybe."
                                    "I mutter it, but the bouncer hears."
                                           
                                    chloe "(inaudible, confused)"
                                    club "Oh. You need to blow off steam, that it?"
                                    name "I… yeah."
                                    "She snatches the phone from my hand."
                                    
                                    club "Tell your friend you’re busy."
                                    club "I think I know what you are looking for.."
                                    club "On your knees."
                                    scene black with dissolve
                                    window hide 
                                    pause
                                    play sound pantdown volume 1 noloop
                                    scene nightdate_bouncersscene4 with dissolve
                                    "I drop. The floor is cold."
                                    "She unzips and frees her cock from its confines — it's thick, and already half-hard."
                                    "She holds the phone up like a trophy, speaker on."
                                    
                                    chloe "(inaudible, still talking, traffic, sorry, wait—)"
                                    
                                    club "Hear that? Your friend’s busy."
                                    play background suckslowv1 volume 1 loop
                                    "She slides her member into my mouth, slow, deliberate."
                                    scene nightdate_bouncersscene5 with dissolve
                                    "I take her in. It's salty and warm, with tinges of leather and smoke."
                                    scene nightdate_bouncersscene4 with dissolve
                                    "Chloe’s voice crackles faintly from the phone in her hand."
                                    scene nightdate_bouncersscene5 with dissolve
                                    chloe "(inaudible, confused, then louder: hello? hello?)"
                                    scene nightdate_bouncersscene4 with dissolve
                                    "The bouncer grips my hair, guiding her dick down to the back of my throat."
                                    club "That’s it… let her listen to it."
                                    $ chloedate2_text_date = True
                                    scene nightdate_bouncersscene5 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene4 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene5 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene4 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene5 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene4 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene5 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene4 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene5 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene4 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene5 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene4 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene9 with dissolve
                                    window hide 
                                    pause
                                    club "Fuuck... you really like sucking dick, don't you?"
                                    scene nightdate_bouncersscene10 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene9 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene10 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene9 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene10 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene9 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene10 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene9 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene10 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene9 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene10 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene5 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene4 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene5 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene4 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene5 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene4 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene5 with dissolve
                                    window hide 
                                    pause

                                    scene nightdate_bouncersscene4 with dissolve
                                    window hide 
                                    pause
                                    scene nightdate_bouncersscene5 with dissolve
                                    window hide 
                                    pause
                                    "She groans low, hips rocking slow and steady against my face."
                                    scene nightdate_bouncersscene4 with dissolve

                                    if gender == "male":
                                        club "Fuck… good boy."
                                    else:
                                        club "Fuck… good girl."
                                    scene nightdate_bouncersscene7 with dissolve
                                    "Her hand tightens in my hair and makes one last deep thrust."
                                    "She climaxes with a low grunt, her cum hot and thick across my tongue."
                                    scene nightdate_bouncersscenefinal with dissolve
                                    stop background
                                    "I swallow instinctively, throat bobbing, eyes watering."
                                    "She pulls her cock out slowly, bundling it back into her pants and zips up with a sharp *zzzt*."
                                    "Her smirk is lazy, satisfied."
                                    "She glances at the still-ringing phone, then ends the call with her thumb."
                                    club "Now get out. And stay out of my hallway or you'll feel my dick again."
                                    club "Unless of course, that's what you wanted."
                                    "She hands me back my phone."
                                    "I stand on shaky legs, wipe my mouth with the back of my hand."
                                    "The taste of her lingers — salt, smoke, and something darkly addictive."
                                    scene black with dissolve
                                    "I slip back into the club, pulse racing, head spinning."
                                    
                                    jump date2somethingtodo
                else:
                    "I think I've texted enough for now."
                    jump date2somethingtodo
   

    label dancingandmeettingrose:

        scene rosedate-dancing with dissolve
        "I start moving my body to the music, letting myself go."
        "The sensation is pleasant."

        scene rosedate-dancing2approaching with dissolve 
        "I feel a warmth rising inside me."
        "As if I was exactly where I needed to be."

        scene rosedate-dancing3approaching with dissolve
        "A hand slides low on my hip from behind — firm, deliberate."
        "I feel a warm breath at my ear."
        ros "Looking for someone?"
        "She’s already moving with me, hips rolling slow, predatory."

        scene rosedate-dancing4 with dissolve
        "Her thigh slips between mine, guiding the rhythm."
        "Sweat, perfume, neon — she smells like trouble."

        scene rosedate-dancing5 with dissolve
        "She leans in, lips brushing my neck."
        ros "Saw you chatting up those girls at the bar. Real smooth."
        ros "Almost looked… confident."
        "Her hand finds mine, fingers locking."
        scene rosedate-dancing6 with dissolve
        "We dance together for a while, lost in the music and lights."
        "Rose dances close to me, but as if we had just met."
        "Like she needed to seduce me all over again."
        "The atmosphere becomes more and more pleasant now that I'm with her."
        "The alcohol that was making my stomach turn seems to dissolve into waves of joy through my body."
        "I'm glad I found her."
        menu:

            "Go back home alone":
                name "I think I should head home now."
                name "It's been fun dancing with you, but I need to sober up."
                ros "Sure. Take care of yourself."
                scene black with dissolve
                "I make my way back through the crowd, the music fading behind me."
                "Outside, the cool night air hits my face."
                "I hail a cab and head home alone."
                "..."
                jump quickgotobed
            "Spend the night with her":
                window hide
                pause

        ros "Come."
        "She tugs me through the crowd, up a narrow staircase to the mezzanine overlooking the floor."

        scene black with dissolve
        window hide
        pause

        scene rosedate-dancing7 with dissolve
        
        "Up here it’s quieter — just the muffled thump of bass and colored lights sweeping below."
        "Up here, I position myself on one of the stairway steps for a better view of the crowd."
        "I feel like I'm as tall as her."
        "She leans on the railing, eyes on me."
        ros "So... You always let strangers grind on you when you’re drunk?"
        name "You're not a stranger [ros]."
        
        ros "You were looking for me?"
        name "Actually, I was supposed to meet a friend, but I think subconsciously I was looking for you."
        ros "You're cute [name]. This club is full of women like me, and you had options."
        name "But none of them are you [ros]."
        "She steps closer."
        ros "I’ve been watching you."
        ros "You looked lonely. Then desperate. Then… hungry."

        scene rosedate-dancing9 with dissolve
    
        ros "Tell me I’m wrong."
        name "No. You're not wrong [ros]."

        scene rosedate-dancing10 with dissolve
        "She kisses me passionately, her tongue lingering on mine."
        "She tastes of dark rum and burnt sugar, like a spiced old-fashioned."
        "I know what's coming."
        "[ros]'s arm catches my waist and I'm hers."
        scene black with dissolve
        window hide
        pause

        "She pulls me deeper into the shadows, past velvet ropes, into a corner."
        "The mezzanine is closed, and the lights are off."
        "The atmosphere is calmer here."
        "Almost romantic."
        ros "On your knees [name]."
        "I drop, dizzy, mouth watering before I even touch her."
        "Her hand drops to her crotch and barely lingers there before she has unzipped."
        "Her big dick is already hard, a bead of precum catching the light."
        "She must be as eager as I am."
        scene rosedate-bj with dissolve
        "I need no further instruction."
        "I open my mouth and take her in, sloppy and eager, the alcohol making my head swim as I suck her dick."
        "She threads fingers through my hair, guiding, not forcing."
        ros "That’s it… just like that [name]."
        window hide
        pause
        
        scene rosedate-bj2 with dissolve
        play sound suckslowv1 volume 0.5 loop
        "I swirl my tongue around her head, tasting her salt and the faint trace of rum on her skin."
        "She exhales a low moan, hips rocking gently."
        window hide
        pause

        scene rosedate-bj with dissolve
        if gender == "male":
            ros "Good boy... keep going."
        else:
            ros "Good girl... keep going."
        window hide
        pause
        scene rosedate-bj2 with dissolve
        window hide
        pause
        scene rosedate-bj with dissolve
        window hide
        pause
        scene rosedate-bj2 with dissolve
        window hide
        pause
        scene rosedate-bj with dissolve
        window hide
        pause
        "I lavish all my attention on her cock, enthusiastically sucking and lapping up her juices."
        ros "Ahhhh - you've gotten better since last time."
        "I moan in agreement."
        scene rosedate-bj2 with dissolve
        window hide
        pause
        scene rosedate-bj with dissolve
        window hide
        pause
        scene rosedate-bj2 with dissolve
        window hide
        pause
        scene rosedate-bj with dissolve
        window hide
        pause
        ros "Not that you were-ahhh ever bad at blowjobs [name] - you were made to please hung futas weren't you?"
        "I moan again, unable to answer verbally with such a big dick in my mouth and unwilling to relinquish it for even a moment."
        scene rosedate-bj2 with dissolve
        window hide
        pause
        scene rosedate-bj with dissolve
        window hide
        pause
        ros "This is where you belong [name]."
        ros "You suck me off so well."
        scene rosedate-bj2 with dissolve
        window hide
        pause
        scene rosedate-bj with dissolve
        window hide
        pause
        scene rosedate-bj2 with dissolve
        
        window hide
        pause

        scene black with dissolve
        "After a while sucking on [ros]'s fat cock, she seems to grow impatient."
        "She offers to take me home."
        
        "We gather our things and head out into the street."
        "Walking helps clear the alcohol from my system."
        "I feel a bit better."

        play music skylineparty volume 1 loop fadein 0.5
        scene rosedate-arrivingcar with dissolve
        "Cool night air hits my face. We’re in front of her car — sleek, hood still warm from the engine."
        ros "So [name], do you still like my cock?"
        name "More than my gin."
        "She laughs, low and pleased."

        scene rosekisscar with dissolve
        play voicebis zoeykiss volume 1 noloop
        "She kisses me again, her hands sliding under my shirt."
        window hide
        pause

        scene rosekisscar3 with dissolve
        window hide
        pause
        scene rosekisscar2 with dissolve
        stop voicebis

        name "So... where are you taking me?"
        ros "Mmh..."
        ros "Right here works just fine."

        name "...Here?"
        "I can feel her arms slip down to my waist."
        scene black
        "She spins me around and pushes me down onto the hood of her car."
        "I don't resist."  
        play sound pantdown volume 1 noloop
        window hide
        pause
        "Deftly, she pulls down my pants, exposing my bare ass to the open air."
        scene rosesscene-start 
        "I can feel her sizeable dick resting on my ass."
        ros "Mmh... we're gonna have some fun, you and me..."

        scene roseffrontpose4 with dissolve
        "Rose grabs me by the waist and starts penetrating me with her large cock."
        "I feel so relaxed, my body surrendering to her confident movements."
        "I moan with pleasure, feeling her thick dick fill me."
        "The distant sound of a car horn cuts through the air, reminding me how exposed we are, but I’m too far gone to care."
       
        scene roseffrontpose4 with dissolve
        "[ros] thrusts forward, her cock driving into me as I moan with delight."
        scene roseffrontpose5 with dissolve
        name "You are so... biig..."
        ros "Mmh... I know..."
        play background rosefucknovoice volume 1 loop
        play sound rosebreathingv2 volume 2 loop
        scene roseffrontpose4 with dissolve
        window hide 
        pause
        scene roseffrontpose5 with dissolve
        window hide 
        pause
        scene roseffrontpose4 with dissolve
        window hide 
        pause
        scene roseffrontpose5 with dissolve
        window hide 
        pause
        scene roseffrontpose4 with dissolve
        window hide 
        pause
        scene roseffrontpose5 with dissolve
        window hide 
        pause
        scene roseffrontpose4 with dissolve
        window hide 
        pause
        scene roseffrontpose5 with dissolve
        window hide 
        pause
        scene rosebackposeback6 with dissolve
        ros "You like that, don't you?"
        name "Y-Yes... please keep going!"
        ros "Do you-ahhh-think I wouldn't?"
        scene rosebackposeback7 with dissolve
        window hide 
        pause
        scene rosebackposeback6 with dissolve
        window hide
        pause
        scene rosebackposeback8 with dissolve
        window hide
        pause
        scene rosebackposeback6 with dissolve
        window hide
        pause
        scene rosebackposeback7 with dissolve
        window hide
        pause
        scene rosebackposeback6 with dissolve
        window hide
        pause
        scene rosebackposeback8 with dissolve
        window hide
        pause
        scene rosebackposeback6 with dissolve
        window hide
        pause
        scene rosebackposeback7 with dissolve
        ros "You're mine, you know that, right?"
        "My heart races, her words sinking in as her thrusts keep me pinned beneath her."
        window hide
        pause
        scene rosebackposeback6 with dissolve
        window hide
        pause
        scene rosebackposeback2 with dissolve
        "She raises her hand, her eyes glinting with dominance, and I brace myself, my skin tingling with anticipation."

        menu:
            ros "Who do you belong to?"
            "You, Rose... I'm yours.":
                ros "Good boy... that's what I like to hear."
                "She lowers her hand, stroking my hip instead, her thrusts deepening as she rewards my submission."
                "My body melts under her control, the threat of her raised hand enough to make me shiver."
            "I don't belong to anyone.":
                play sound spank volume 2 noloop
                scene rosebackposeback3 with dissolve
                ros "Wrong answer."
                
                "Her hand comes down with a sharp, stinging spank, the crack echoing as my skin burns with heat."
                name "Nngh!"
                play voicebis youlikethatrose volume 1 noloop
                "The pain blends with pleasure, my ass throbbing as her cock drives deeper, amplifying every sensation."
    
        scene rosebackposeback6 with dissolve
        name "Mmmh yess.."
        play sound rosebreathingv2 volume 2 loop
        scene rosebackposeback7 with dissolve
        window hide
        pause
        scene rosebackposeback6 with dissolve
        window hide
        pause
        scene rosebackposeback7 with dissolve
        window hide
        pause
        scene rosebackposeback6 with dissolve
        window hide
        pause
        scene rosebackposeback7 with dissolve
        window hide
        pause
        scene rosebackposeback6 with dissolve
        window hide
        pause
        scene rosebackposeback7 with dissolve
        window hide
        pause
        scene rosebackposeback6 with dissolve
        window hide
        pause
        scene rosebackposeback7 with dissolve
        window hide
        pause
        scene rosebackposeback6 with dissolve
        window hide
        pause
        scene rosebackposeback7 with dissolve
        window hide
        pause
        scene rosebackposeback6 with dissolve
        window hide
        pause
        scene rosebackposeback7 with dissolve
        window hide
        pause
        scene rosebackposeback6 with dissolve
        window hide
        pause
        scene rosebackposebackhairpull4 with dissolve
        ros "I am not done with you [name]!"
        "She grabs my hair with a firm, vigorous tug, yanking my head back with controlled force."
        "The sharp tension in my scalp sends electric shivers down my spine, a mix of pain and raw pleasure."
        menu:
            ros "Say you're my little slut."
            "I'm your little slut...":
                ros "That's right, my sweet little toy."
                "She eases her grip slightly, her thrusts slowing to a sensual rhythm, rewarding my submission."
                "My body trembles, the lingering tension in my scalp blending with the pleasure of her cock."
            "No way, I'm not saying that.":
                scene rosebackposebackhairpull5 with dissolve
                ros "Oh, you'll learn."
                play sound longvoicerose volume 1 noloop

                play background fuckrosefast volume 1 loop
                scene rosebackposebackhairpull4 with dissolve
                window hide
                pause
                scene rosebackposebackhairpull5 with dissolve
                window hide
                pause
                scene rosebackposebackhairpull4 with dissolve
                window hide
                pause
                scene rosebackposebackhairpull5 with dissolve
                window hide
                pause
                scene rosebackposebackhairpull4 with dissolve
                window hide
                pause
                scene rosebackposebackhairpull5 with dissolve
                ros "You love it when I take charge, don't you?"
                name "Yes..."
                "My mind is clouded, overwhelmed by the tension in my scalp and the deep pressure of her thrusts."
                scene rosebackposebackhairpull4 with dissolve
                window hide
                pause
                scene rosebackposebackhairpull5 with dissolve
                window hide
                pause
                scene rosebackposebackhairpull4 with dissolve
                window hide
                pause
                scene rosebackposebackhairpull5 with dissolve
                window hide
                pause
                scene rosebackposebackhairpull4 with dissolve
                window hide
                pause
                scene rosebackposebackhairpull5 with dissolve
                window hide
                pause
                scene rosebackposebackhairpull4 with dissolve
                window hide
                pause
                scene rosebackposebackhairpull5 with dissolve
                window hide
                pause
                scene rosebackposebackhairpull4 with dissolve
                window hide
                pause
                scene rosebackposebackhairpull5 with dissolve
                window hide
                pause
                scene rosebackposebackhairpull4 with dissolve
                window hide
                pause
                scene rosebackposebackhairpull5 with dissolve
                window hide
                pause
                name "Fuck.....!!"
                play background rosefuck volume 1 loop
        window hide
        pause
        play sound rosebreathingv2 volume 2 loop
        scene rosebackposeback9 with dissolve
        "Her hold on my hair loosens, but the sting in my scalp remains, keeping me hyper-aware of her control."
        ros "Look at you, my perfect little slut, hmm?"
        window hide
        pause
        scene rosebackposeback10 with dissolve
        window hide
        pause
        scene rosebackposeback9 with dissolve
        window hide
        pause
        scene rosebackposeback10 with dissolve
        window hide
        pause
        scene rosebackposeback9 with dissolve
        window hide
        pause
        scene rosebackposeback10 with dissolve
        window hide
        pause
        scene rosebackposeback9 with dissolve
        window hide
        pause
        scene rosebackposeback10 with dissolve
        window hide
        pause
        scene rosebackposeback9 with dissolve
        window hide
        pause
        scene rosebackposeback10 with dissolve
        window hide
        pause
        scene rosebackposeback9 with dissolve
        window hide
        pause
        scene rosebackposeback10 with dissolve
        window hide
        pause
        scene rosebackposeback9 with dissolve
        window hide
        pause
        scene rosebackposeback10 with dissolve
        window hide
        pause
        scene rosebackposeback9 with dissolve
        window hide
        pause
        scene rosebackposeback10 with dissolve
        window hide
        pause
        scene rosebackposeback9 with dissolve
        window hide
        pause
        scene rosebackposeback2 with dissolve
        "She raises her hand again, the sight making my heart pound, my skin already sensitive from her earlier spank."
        menu:
            ros "Tell me who you belongs to!"
            "I'm yours, Rose... completely yours.":
                ros "That's my good boy."
                "She lowers her hand, caressing my hip instead, her thrusts slow and deliberate, letting me savor her control."
                "My body shakes, overwhelmed by the mix of anticipation and surrender."
            "I'm not yours.":
                scene rosebackposeback3 with dissolve
                play sound spank volume 2 noloop
                
                "Her hand crashes down with brutal force, the spank searing my skin, leaving it screaming with heat."
                
                name "Ahh... fuck!"
                "The pain is intense, my ass burning as her cock drives deeper, pushing me to the edge of pleasure and pain."
        window hide
        pause
        play sound rosebreathingv2 volume 2 loop
        play sound fuckyesrose volume 1 noloop
        scene roseffrontpose5 with dissolve
        ros "You're so gorgeous like this, completely mine..."
        window hide
        pause
        scene roseffrontpose4 with dissolve
    
        window hide
        pause
        scene roseffrontpose5 with dissolve
        
        window hide
        pause
        scene roseffrontpose4 with dissolve
        window hide
        pause
        scene roseffrontpose5 with dissolve
        window hide
        pause
        scene roseffrontpose4 with dissolve
    
        window hide
        pause
        scene roseffrontpose5 with dissolve
        
        window hide
        pause
        scene roseffrontpose4 with dissolve
        window hide
        pause
        scene roseffrontpose5 with dissolve
        window hide
        pause
        scene rosefpose1 with dissolve
        play sound takemydrose volume 1 noloop
        window hide
        pause
        scene rosefpose2 with dissolve
        window hide
        pause
        scene rosefpose3 with dissolve
    
        window hide
        pause
        scene rosefpose4 with dissolve
        ros "You're perfect when you give in like this..."
        "I'm lost in a whirlwind of sensations: the lingering burn of her spank, the electric pull in my scalp, and the deep pleasure of her thrusts."
        window hide
        pause
        scene rosefpose1 with dissolve
        
        window hide
        pause
        scene rosefpose2 with dissolve
        ros "You're so responsive... I love seeing you like this."
        "Her thrusts push me closer to the edge, the memory of her spank amplifying every sensation."
        window hide
        pause
        scene rosefpose3 with dissolve
        window hide
        pause
        scene rosefpose4 with dissolve
        window hide
        pause
        scene rosebackposeback7 with dissolve
        window hide
        pause
        scene rosebackposeback6 with dissolve
        window hide
        pause
        
        window hide
        pause
        scene rosebackposeback8 with dissolve
    
        window hide
        pause
        scene rosebackposeback2 with dissolve
        "She raises her hand again, the sight making my heart race, my ass already burning from her previous spanks."
        menu:
            ros "Say you're my little bitch."
            "I'm your little bitch, Rose...":
                ros "That's it, my perfect little toy."
                "She lowers her hand, her thrusts slowing to a deep, sensual rhythm, rewarding my submission."
                "My body melts, the lingering pain and pleasure merging into a haze of surrender."
            "I'm not saying that.":
                scene rosebackposeback3 with dissolve
                play sound spank volume 3 noloop
                ros "Still resisting?.."
                "Her hand crashes down with savage force, the spank so brutal it leaves my skin screaming and my body shaking."
                name "Fuck...!"
                "The pain pushes me to the edge, but the pleasure of her cock and her control keeps me tethered to her."
        window hide
        pause
        play sound rosebreathingv2
        scene rosebackposebackhairpull4 with dissolve
        "She pulls my hair with a fierce, commanding tug, holding me in place as her thrusts grow erratic."
        "My scalp burns under her grip, the pain fueling a primal pleasure that makes me cry out."
        window hide
        pause
        scene rosebackposebackhairpull5 with dissolve
        ros "That's it, give in to me completely..."
        window hide
        pause
        scene rosebackposebackhairpull4 with dissolve
        window hide
        pause
        scene rosebackposebackhairpull5 with dissolve
        window hide
        pause
        scene rosebackposebackhairpull4 with dissolve
        window hide
        pause
        scene rosebackposebackhairpull5 with dissolve
        
        window hide
        pause
        scene rosebackposebackhairpull4 with dissolve
        window hide
        pause
        scene rosebackposebackhairpull5 with dissolve
        window hide
        pause
        scene rosebackposebackhairpull4 with dissolve
        window hide
        pause
        scene rosebackposebackhairpull5 with dissolve
        
        window hide
        pause
        scene rosebackposebackhairpull4 with dissolve
        window hide
        pause
        scene rosebackposebackhairpull5 with dissolve
        window hide
        pause
        scene rosebackposebackhairpull4 with dissolve
        window hide
        pause
        scene rosebackposebackhairpull5 with dissolve
        
        window hide
        pause
        scene rosebackposeback2 with dissolve
        
        "She raises her hand again, her eyes gleaming with dominance, and I brace myself, my skin already marked by her."
        menu:
            ros "Who's a little bitch"
            "I am... I am your little bitch":
                ros "That's my good boy, completely mine."
                "She lowers her hand, her thrusts slow and possessive, sealing my submission."
                "My body trembles, overwhelmed by the intensity of her control and my surrender."
            "No, I won't say that.":
                scene rosebackposeback3 with dissolve
                play sound spank volume 3 noloop
                play voicebis roseohfuck volume 1 noloop
                ros "You'll learn to obey."
                name "Ahh... "
                scene rosebackposeback2 with dissolve
                window hide
                pause
                scene rosebackposeback3 with dissolve
                play sound spank volume 3 noloop
                window hide
                pause
                scene rosebackposeback2 with dissolve
                window hide
                pause
                scene rosebackposeback3 with dissolve
                play sound spank volume 3 noloop
                window hide
                pause
                "The pain is overwhelming, blending with the pleasure of her cock, pushing me into complete submission."
        window hide
        pause
        play sound rosebreathingv3 volume 2 loop
        scene rosebackposeback9 with dissolve
        ros "Mmh, you're so beautiful, marked by me..."
        ros "Do the other futas fuck so good?"
        "Her voice is husky, dripping with desire as she shifts to a slower, deeper rhythm."
        window hide
        pause
        scene rosebackposeback10 with dissolve
    
        window hide
        pause
        scene rosebackposeback9 with dissolve
    
        window hide
        pause
        scene rosebackposeback10 with dissolve
        
        window hide
        pause
        
        scene rosefrontposemouth3 with dissolve
        "She slides two fingers into my mouth, I moan around them."
        ros "Suck on those."
        ros "Look at you [name]!"
        ros "So eager to please me.."
        scene rosefrontposemouth7 with dissolve
    
        window hide
        pause
        scene rosefrontposemouth3 with dissolve
        
        window hide
        pause
        scene rosefrontposemouth8 with dissolve
        ros "Mmh, you're so good at this..."
        ros "I love your tight fuckhole [name]."
        ros "You were-ahh made for fucking."
        window hide
        pause
        scene rosefrontposemouth9 with dissolve

        window hide
        pause
        scene rosefrontposemouth7 with dissolve
        window hide
        pause
        scene rosefrontposemouth3 with dissolve
        ros "Yes... just like that..."
        "I double my efforts and push back onto her big dick, wanting to give her as much pleasure as she's given me."
        window hide
        pause
        scene rosefrontposemouth8 with dissolve
    
        window hide
        pause
        scene rosefrontposemouth9 with dissolve
        
        window hide
        pause
        scene rosefrontposemouth7 with dissolve
        window hide
        pause
        scene rosefrontposemouth3 with dissolve
        
        window hide
        pause
        scene rosefrontposemouth7 with dissolve
        
        scene side1 with dissolve
        "Her rhythm quickens, she is getting close."

        play voicebis rosemhtakeit volume 1 noloop
        play background slapswetfastv2 volume 2 loop
        window hide
        pause
        scene side2 with dissolve
        ros "Look at you.. "
        ros "Letting me use you like this..."
        window hide
        pause
        scene side3 with dissolve
        window hide
        pause
        scene side4 with dissolve
        window hide
        pause
        scene side5 with dissolve
    
        window hide
        pause
        scene side2 with dissolve
        window hide
        pause
        ros "Fucking you so deep and raw on my car."
        scene side3 with dissolve
        window hide
        pause
        scene side4 with dissolve
        window hide
        pause
        scene side5 with dissolve
        window hide
        pause
        scene side2 with dissolve
        window hide
        pause
        scene side3 with dissolve
        window hide
        pause
        scene side4 with dissolve
        window hide
        pause
        scene side5 with dissolve
        
        scene side2 with dissolve
        window hide
        pause
        scene side3 with dissolve
        window hide
        pause
        scene side4 with dissolve
        window hide
        pause
        scene side5 with dissolve
        play sound normalbreathing volume 0.5 loop
        scene side2 with dissolve
        window hide
        pause
        scene side3 with dissolve
        window hide
        pause
        scene side4 with dissolve
        window hide
        pause
        scene side5 with dissolve
        window hide
        pause
        ros "I'm going to cum so much, you've earned it [name]."
        scene rosefrontposemouth7 with dissolve
        window hide
        pause
        scene rosefrontposemouth3 with dissolve
        window hide
        pause
        scene rosefrontposemouth8 with dissolve
        window hide
        pause
        scene rosefrontposemouth9 with dissolve
        window hide
        pause
        scene rosefrontposemouth7 with dissolve
        window hide
        pause
        scene rosefrontposemouth3 with dissolve
        window hide
        pause
        scene rosefrontposemouth8 with dissolve
        window hide
        pause
        scene rosefrontposemouth9 with dissolve
        window hide
        pause
        scene rosesscene-cum1 with dissolve
        window hide
        pause
        scene rosesscene-cum2 with dissolve
        window hide
        pause
        scene rosesscene-cum4 with dissolve
        window hide
        pause
        scene rosesscene-cum3b with dissolve
        window hide
        pause
        scene rosesscene-cum1 with dissolve
        window hide
        pause
        scene rosesscene-cum2 with dissolve
        window hide
        pause
        scene rosesscene-cum4 with dissolve
        window hide
        pause
        scene rosesscene-cum3b with dissolve
        window hide
        pause
        scene rosesscene-cum1 with dissolve
        window hide
        pause
        scene rosesscene-cum2 with dissolve
        window hide
        pause
        scene rosesscene-cum4 with dissolve
        window hide
        pause
        scene rosesscene-cum3b with dissolve
        window hide
        pause
        scene rosesscene-cum1 with dissolve
        window hide
        pause
        scene rosesscene-cum2 with dissolve
        window hide
        pause
        scene rosesscene-cum4 with dissolve
        window hide
        pause
        scene rosesscene-cum3b with dissolve
        window hide
        pause
        scene rosesscene-cum2 with dissolve
        window hide
        pause
        scene rosesscene-cum4 with dissolve
        window hide
        pause
        scene rosesscene-cum3b with dissolve
        window hide
        pause
        scene rosesscene-cum1 with dissolve
        window hide
        pause
        scene rosesscene-cum2 with dissolve
        window hide
        pause
        scene rosesscene-cum4 with dissolve
        window hide
        pause
        scene rosesscene-cum3b with dissolve
        window hide
        pause
        scene side6 with dissolve
        window hide
        pause
        scene side7 with dissolve
        window hide
        pause
        scene side6 with dissolve
        window hide
        pause
        scene side7 with dissolve
        window hide
        pause
        scene side6 with dissolve
        window hide
        pause
        scene side7 with dissolve
        window hide
        pause
        scene side6 with dissolve
        window hide
        pause
        scene side7 with dissolve
        window hide
        pause
        scene side6 with dissolve
        window hide
        pause
        scene side7 with dissolve
        window hide
        pause
        scene side6 with dissolve
        window hide
        pause
        scene side7 with dissolve
        window hide
        pause
        scene side6 with dissolve
        "She’s going wild, her big cock engorging inside me, pulsing ever-more urgently as she gets closer to release."
        scene side7 with dissolve
        window hide
        pause
        scene side6 with dissolve
        "I want it so bad."
        window hide
        pause
        scene side7 with dissolve
        window hide
        pause
        play sound rosemoan volume 1 noloop
        "She lets out a raw moan, her body tensing as she reaches her climax."
        stop background 
        scene rosesscene-cum1 with dissolve
        window hide
        pause
        "I can feel her balls tensing up with such ferocity as she unloads her cream inside me."
        scene rosesscene-cum2 with dissolve
        window hide
        pause
        pause
        "Her orgasm seems to last forever, every moment I can feel her hard cock pulsating inside me."
        pause
        scene rosesscene-cum3b with dissolve
        window hide
        pause
        "It feels like I've been inflated as she continues to fill me with her load."
        scene rosesscene-cum2 with dissolve
        window hide
        pause
        scene rosesscene-cum3b with dissolve
        window hide
        pause
        scene frosedatefinalshot with dissolve
        window hide
        "Her dick finally stops pumping and she slides out of me."
        "Without her big dick inside me I feel strangely bereft."
        "My mind is hazy with my own afterglow."
        play sound rosesuchagoodbitch volume 1 noloop
        pause
        pause
        pause
        ros "Ahhhhh fuck..."
        ros "Goddamn [name], I don't think I've ever cum so much in my life!"
        ros "You really know how to please a futa."
        ros "Come on grab your pants, I'll take you home."
        "I pick up my pants and do my best to not make a mess as I get into the car."
        "[ros] came so much."
        stop music 
        play sound caropenclose volume 1 noloop

        scene black with dissolve
        window hide
        pause
        "The interior of Rose's car is soothing, in contrast to the street where she fucked me."
        "I take my time putting my pants back on, without rushing."
        play sound rosecardriving fadein 0.5 volume 1 loop
        window hide 
        pause
        scene rosecarinterior with dissolve
        window hide 
        pause
        
        
        "The sound of the engine soothes me."
        "After such a good fucking, I'm exhausted."

        scene rosedategoinghome with dissolve
        "Rose says nothing, she seems at peace."
        "I am not sure if I want to talk. I doubt much would come out."
        "I don't really know her at all, yet twice now I've pleasured her without a second thought."
        "We must lead very different lives but I feel like we understand each other."
        "At least, I understand her passion and her needs, and she knows my weakness and my desire."
        "I doubt there'd be much to say."
        window hide 
        pause
        scene rosecarinterior2 with dissolve
        "Outside, people we pass on the street look peaceful too."
        "Perhaps I have a different perspective now."
        "I just feel so satisfied."
        "I watch them with curiosity."
        "They seem to be in another world."
        "I wonder what they're thinking."
        "I close my eyes."
        scene black with dissolve
        stop sound fadeout 1.0
        window hide
        pause
        
        scene roseericbackatplace with dissolve
        "I arrive home feeling drained."
        "I said very little to [ros] - just thanked her for the lift and walked in."
        "Was it rude?"
        "It feels like we expressed everything we needed to."
        "The small lamp provides just enough light."
        "I undress slowly, take a shower and fall asleep straightaway."
        $ rose_date_done = True
        jump justbed
        jump map3


    label rosedate_bathroom:
