label textdirection:
    scene beforebedphone
        
    if day == 0:
        "a notification pops up on my phone"
        pause 1.0
        h_nvl "Hey, do you think you could send me the history notes when I'm not there, just in case?"
        n_nvl "Sure, just let me know when you need them."
        h_nvl "Okay."
        h_nvl "Can you send me today's notes?"
        n_nvl "But you were there today..?"
        h_nvl "Oh yeah, that's right. But I felt sick and didn't follow along."
        n_nvl "Wow, it's the first day."
        h_nvl "Probably my pollen allergy."
        n_nvl "Okay, okay, I'll send them to you."
        nvl clear
        jump endofday_choice
       
        
    elif day >= 0:
        
        label camilletext: 
            if camille_sdate_done == True and camilletext1_done == False:
                "A notification pops up on my phone."
                cam_nvl "Your ass is really sweet"
                n_nvl "It was something..."
                n_nvl "I hope no one saw us"
                cam_nvl "don't count on that"
                cam_nvl "Anyway it was fun"
                n_nvl "maybe we could do this again in a more intimate place"
                pause 2.0
                n_nvl "You there?"
                pause 2.0
                "..."
                "Camille seems to have gone to bed."
                $ camilletext1_done = True
                nvl clear

            elif classdatecamille_count == 8 and camilletext2_done == False:
                "A notification pops up on my phone."
                "Camille is sending me a picture"
                cam_nvl "{image=avaconv.png}"
                cam_nvl "I think Amy likes you"
                $ camilletext2_done = True
                nvl clear

        label zoeytext:
            if zoeyconv_count == 1:
                "A notification pops up on my phone."
                z_nvl "Helloo! :)"
                z_nvl "J'espère que ça te dérange pas que Hugo m'a donné ton numéro."
                n_nvl "No, not at all."
                z_nvl "Cool!"
                z_nvl "So how was your mythology class?"
                n_nvl "It was nice!"
                z_nvl "Did you talked about Dionysus?"
                z_nvl "Just wanted to check in on you."
                n_nvl "Thanks, I appreciate it."
                nvl clear

        if linda_4th_conv_done == True and linda_invitation_sent == False:

            "A notification pops up on my phone."

            l_nvl "Next time, come directly to my place."
            n_nvl "okay"
            l_nvl "I'll be waiting for you."
            $ linda_relation_status_text = "Linda is waiting for me at her place"
            $ linda_invitation_sent = True
            nvl clear

        if classdateemma_count == 3 and textoemma_send == False: 
            "A notification pops up on my phone."
            em_nvl "{image=ericass.jpg}"
            n_nvl "wtff is that??"
            em_nvl "Its your new profile picture"
            $ textoemma_send = True
            
            nvl clear
        elif sarah_homedate_done == True and sarahtexto_count == 0:
            "A notification pops up on my phone."
            s_nvl "Hey, it was cool having you at my place."
            s_nvl "How do you find my friends? They're funny, right?"
            n_nvl "Yeah, they're cool."
            s_nvl "We should do it again."
            s_nvl "With pleasure"
            s_nvl "alright sleep well <3"
            n_nvl "you too!"
            nvl clear
            "She is so sweet."
            $ sarahtexto_count += 1
            jump endofday_choice

        elif sarahtexto_count == 1:
            "A notification pops up on my phone."
            s_nvl "Hey, are you sleeping?"
            n_nvl "No, not yet, I am chilling in bed"
            s_nvl "Oh, okay."
            n_nvl "What are you up to?"
            s_nvl "Just chilling, you?"
            n_nvl "Same."
            s_nvl "Cool, cool."
            n_nvl "Yeah."
            s_nvl "Well, good night."
            n_nvl "Good night."
            $ sarahtexto_count += 1
            nvl clear
            jump endofday_choice
        elif sarahtexto_count == 2 :
            "A notification pops up on my phone."
            s_nvl "Hey, are you sleeping?"             
            n_nvl "No, not yet, I am chilling in bed and you?"
            s_nvl "I am making diner"
            n_nvl "What are you making?"
            s_nvl "Pasta"
            n_nvl "Nice, you are making me hungry"
            s_nvl "Haha, sorry I have only made enough for me"
            n_nvl "I see how it is"
            s_nvl "{image=sarahdpic.png}]"
            n_nvl "yummy {image=emojihungry.png}"
            $ sarahtexto_count += 1
            nvl clear
            "Another notification pops up on my phone."
            m_nvl "Hey, how's it going?"
            n_nvl "I'm good, just chilling in bed."
            m_nvl "You haven't been giving much news.."
            m_nvl "I'm a bit worried"
            menu: 
                "I'm sorry, I've been busy with the move":
                    n_nvl "I'm sorry, I've been busy with the move."
                    n_nvl "I had to work more to catch up at the beginning of the year."
                    m_nvl "... ok."
                    m_nvl "I understand."
                    m_nvl "I miss you."
                    n_nvl "I miss you too."
                    m_nvl "Keep me updated or I'll start worrying again."
                    m_nvl "I have to go."
                    m_nvl "Good night <3"
                    n_nvl "Good night <3"
                    nvl clear
                "Yeah I'm not into texting lately":
                    n_nvl "Yeah, I'm not into texting lately."
                    m_nvl "I see.."
                    m_nvl "I am bothering you"
                    n_nvl "I'm just tired"
                    m_nvl "... ok."
                    nvl clear
          
            jump endofday_choice
       
        elif sarah_elise_cafedate_done == True and sarahsproposalrefused == False and elise_sdate_done == False and sarah_sdate_done == False:
            "A notification pops up on my phone."
            s_nvl "Hey, I need to tell you something."             
            n_nvl "What?"
            s_nvl "I've been thinking about you all day"
            s_nvl "Come up."
            
            menu:
                "I am coming":
                    n_nvl "Ok I am coming"
                    nvl clear
                    jump sarahdate4
                "I am sorry, I am not interested ":
                    n_nvl "I am sorry, I am not sure"
                    s_nvl "Ok..."
                    $ sarahsproposalrefused = True
                    nvl clear
                    jump endofday_choice
                     
        
    

label endofday_choice:

    if  quickbed == True:
        jump gotobed
    menu:   
            "go to bed":
                jump gotobed
            
            "hang out": 
                jump hangoutdirection

label bosstexting:
    scene home00
    "a notification pops up on my phone"
    elo_nvl "Hello, my name is Elodie, one of my employees told me you were looking for a job."
    n_nvl "Yes, that's me."
    
    elo_nvl "If you're interested, I'll send you the address of a café."
    elo_nvl "I'll be waiting for you there."
    n_nvl "Very well, thank you very much."
    $ boss_textconv_done = True
    show screen homescreen4
    call screen homescreen4  