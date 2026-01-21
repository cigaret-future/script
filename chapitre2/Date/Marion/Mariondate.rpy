label marion_date_direction:
    if marion_date_done == True:
        scene secondfloorscreen2
        "I should probably not bother Marion again right now."
        jump secondfloor_corridor
    elif corridorconv_done == True:
        jump marion_not_here
    elif marion_date_count == 0:
        jump Marion_date
    elif marion_date_count == 1:
        jump Marion_date1
    elif marion_date_count == 2:
        jump Marion_date2
    elif marion_date_count == 3:
        jump Marion_date3
    else:
        "I don't have anything else planned with Marion right now."



label marion_not_here:
    scene elevator3
    "Let's see if Mrs. Gilsberg is around."
    scene marion-corridor
    "I arrive on the last floor of the university."
    scene upbuilding
    "I don't see Marion anywhere."
    "She's probably busy with her work."
    "I'll try another time."

    jump secondfloor_corridor




label Marion_librarydate:
    "We walk down the university hallway."
    "Marion walks quickly, with a confident stride."
    "She turns into a corridor I don’t recognize."
    scene universityresearchlibrary
    "On entre dans une grande salle au dernier étage d'un batiment éclairé par de grandes fenêtres."

    mar "Here we are."

    name "Oh, this isn’t the same library I went to before."
    mar "No, that one is different. This is the library dedicated to art history."
    name "I see. It looks impressive."

    mar "Come on, I’ll show you how everything is organized."
    scene marionlibraryvisit
    "She leads me through the aisles and points out the sections that might be useful for me."
    "She speaks calmly but very precisely; I can’t follow everything she says,"
    "but I nod along, telling myself I’ll have time to understand it better later."

    "It’s already really nice of her to give me a tour."
    "I feel privileged."
    "She can’t be doing this for every student."
    scene mariondate-arrivinglibrary
    "After a few minutes, we reach a table near the large windows."
    mar "Alright, I’ll let you settle here. I need to get some work done as well."
    mar "If you need anything, don’t hesitate to ask me."
    mar "And if you’d like, you can work here too."
    name "Thank you, that’s really kind of you."
    "Marion settles in and lets me get on with my research."
    scene ericsearchingforbooks with dissolve
    "I start looking through the books she recommended."
    "I wasn't really expecting to dive into my research right away."
    "But her offer was so unexpected that I let myself get a bit carried away."
    "I'd better put on a good show and work a bit with her."
    "I pick up one of the books she pointed out and start flipping through it."
    "..."
    "It looks interesting, but I'm not sure I really understand."
    "Maybe I'd be better off working directly on my article."
    "I go back over to Marion and sit down next to her."
    scene workingwithmarion with dissolve
    "She's already immersed in her work and doesn't say a word."
    "She seems absorbed."
    "I don't disturb her and get back to work myself."
    scene workingwithmarion_ericlookingleft with dissolve
    "From time to time, I sneak a discreet glance at what she's doing."
    "I get the feeling she's answering emails, but I'm not sure."
    "She switches between several tabs."
    "She probably has a lot of things to deal with."
    "I focus on my work..."
    "I write a few scattered sentences on the document I've started to organize."
    "I'm having a bit of trouble concentrating."
    "I feel like Mrs. Gilsberg is watching me."
    "But I don't quite dare turn my head."
    "It's a little strange for us to be sitting side by side working in this library."
    "I push away the images that start to appear in my mind."
    "..."
    scene black with dissolve
    window hide
    pause
    scene workingwithmarionleaving with dissolve
    "After an hour of work, she stands up."
    mar "Alright, I should get going."
    mar "I have to head home, my daughter is coming over for dinner."
    mar "Did you manage to get some work done?"
    name "Yes, I did. I’m working on the article, and I’m starting to find a few leads."
    scene workingwithmarionleaving2 with dissolve
    mar "Good."
    mar "You seem to be taking this seriously."
    mar "That’s encouraging."
    name "Yes, thank you for letting me work here."
    mar "Actually you are allowed to come here whenever you want."
    mar "Student access is free."
    mar "Don’t stay too late though. Concentration fades after a point... and other things take over."
    
    mar "See you soon."
    name "Goodbye!"
    "I watch her walk away through the stacks."
    "I return to my work, feeling motivated."
    "I need to make progress on this article."
    scene black with dissolve
    "Despite my efforts, I can't seem to concentrate."
    "I decide to pack up my things and leave the library."
    "People bustle in the corridors; my head is still full of research."
    jump gardenuni_start2


# // Present article and ask question
label Marion_date:
   
    scene secondfloorelevator
    "I take the elevator to the last floor."
    
    scene marion-corridor
    ""
    scene upbuilding
    ""
    scene marion-office
    ""
    show marionneutral
    mar "Hello, come in!"
    mar "I'm glad to see you."
    mar "Please, have a seat."
    name "Thank you, that's very kind."
    mar "So, how are you doing?"
    name "I'm fine, thank you. And you?"
    mar "I'm doing well."
    mar "I hope you have something to show me."
    name "Yes, I've been working on the article we discussed."
    name "I'm not finished yet."
    name "I'm trying to organize my ideas."
    mar "I see..."
    mar "I can take a look if you'd like."
    name "Yes, of course."
    mar "Go ahead, show me."
    "Mrs. Gillsberg stands and walks around the desk to where I am."
    "I open my laptop and show her the draft I've started."
    "She scans it quickly."
    mar "Hmm..."
    "She scrolls to the bottom of the page, then back up."
    mar "I see — you're still at an early stage."
    mar "But it's a good start."
    mar "Writing is a process, and it takes time."
    name "Yeah, it can be a bit overwhelming."
    mar "Let's meet again when you've made more progress."
    name "sure"   
    $ marion_date_done = True
    "Before I leave the office, Mrs. Gillsberg m'interpelle."
    mar "By the way, I wanted to know..."
    mar "What do you want to do with this?"
    mar "Je veux dire, est ce que vous avez une idée de vous voulez faire?"
    "Elle me regarde avec curiosité."
    "Je pense que je devrais être honnête avec elle."
    menu:
        "En vérité je ne sais pas trop..":
            name "Honestly, I'm not sure yet."
            name "Tout ce truc de recherche je ne sais pas si c'est pour moi.."
            mar "That's understandable."
            mar "Vous faites bien de le dire tout de suite."
            mar "It's important to know what you're getting into."
            
        "Je veux faire de la recherche.":
            name "I want to do research."
            $ search_chosen = True
            mar "hmm"
            mar "D'accord."
            mar "bon très bien à la prochaine alors."
    "Elle sourit et me raccompagne à la porte."
    mar "See you soon."
    name "Goodbye!"
    jump secondfloor_corridor


    
    name "Sure."
    show marionneutral
    scene black with dissolve

    jump secondfloor_corridor  



    elif article_progress >= 50:
        "She leans in closer, as if to get a better look."
        mar "Not bad at all."
        mar "You're making solid progress, quickly and competently."
        mar "There's still some work to do."
        mar "Let's meet again when you've made more progress."
        name "sure"

# // Present article and ask question



label Marion_date1:
    scene secondfloor
    "I arrive on the second floor of the university."
    
    scene secondfloorelevator
    "I take the elevator to the last floor."
    
    scene marion-corridor
    ""
    scene upbuilding
    ""
    scene marion-office
    ""
    show marionneutral
    mar "Hi! Come in."
    name "Hello, Mrs. Gillsberg. Thank you for seeing me again."
    mar "Of course, it's no problem."
   
    mar "So, have you made any progress on your article?"
    name "Yes, I've been working on it."
    mar "Let's see."
    mar "Did you send it to me?"
    name "Yes, I emailed it to you last night."
    "She leans in closer, as if to get a better look."
    mar "Not bad at all."
    mar "You're making progress"
    mar "There's still some work to do."
    mar "Si vous voulez vous pouvez travailler à la bibliotheque de recherche."
    mar "C'est un endroit calme et propice à la concentration."
    name "I didn't know that place."
    mar "You should go there sometime."
    mar "It's much better than the student library."
    mar "I can show you if you want."
    mar "Je dois y passer pour travailler aujourd'hui."
    mar "On peut y'aller ensemble"
    name "That would be great, thank you."
    mar "Perfect let's go then."
    jump Marion_librarydate
        
        
    show marionserious1
    hide marionneutral
   

    jump gardenuni_start2

# // task 1

label Marion_date2:
    scene secondfloor
    "I arrive on the second floor of the university."
    
    scene secondfloorelevator
    "I take the elevator to the last floor."
    
    scene marion-corridor
    ""
    scene upbuilding
    ""
    scene marion-office
    ""
    "Mrs.Gillsberg doesn't seem to be there.."
    "Peut être qu'elle est occupée ailleurs."
    "Je repasserais plus tard."
    scene upbuilding
    ""
    scene secondfloor
    "Soudain j'aperçois Mme Gillsberg qui arrive dans le couloir."
    "Elle me voit et s'approche de moi."
    mar "Oh, hello!"

    mar "I was just thinking about you."
    mar "Je dois aller à une réunion et je suis déja en retard, c'est terrible"
    mar "j'ai vus que vous m'avez envoyé votre article mais je n'ai pas eu le temps de regarder!"
    mar "On se voit plus tard alors.."
    name "Ok pas de problème"
    mar "Peut tu me rendre un service?"
    name "heu oui bien sûr"
    mar "j'ai oublié un dossier dans mon bureau et je dois l'avoir avec moi pour la réunion"
    mar "Tu penses que tu peux aller le chercher?"
    mar "C'est des feuilles blanches agraffé ensemble."
    mar "mon bureau est ouvert il te suffit d'entrer de les prendre."
    name "heuu.. ok.."
    mar "Merci, je serais en salle 530"
    mar "rejoins moi là bas"
    "Avant que je puisses lui demander plus de précision, elle disparait dans le couloir"
    "..."
    "Je devrais pouvoir trouver"
    scene elevator3
    ""
    scene upbuilding
    ""
    scene marion-corridor 
    ""
    scene marion-office
    ""
    scene marion-papers
    "J'apperçois un dossier sur le bureau."
    "Je le prends rapidement."
    scene runninguniveric
    "Je me dépêche de rejoindre Mme Gillsberg."
    scene marion-corridor
    ""
    scene secondfloorscreen
    ""
    scene black
    "Je la retrouve dans une salle de réunion."
    scene mariondate_almameet3
    mar "Oh, you found it! Thank you so much."
    name "No problem."
    mar "see you later!"
    "Elle refermes la portes"
    jump secondfloor_corridor




    label Marion_date3:
        show marionneutral
        mar "Hi! Come in."
        name "Hello, Mrs. Gillsberg."
        mar "Thanks again for last time."
        mar "I was a bit scattered that day. I don't usually forget things in my office."
        mar "Must be the fatigue, I suppose."
        name "No problem at all."
        name "You help me, I help you."
        name "It was the least I could do."
        mar "That's true."
        mar "I hope it wasn't too much trouble."
        mar "After I asked you, I felt a bit guilty."
        mar "Like maybe it wasn't appropriate to ask you to do that."
        name "No, really, it didn't bother me at all."
        mar "Well, that's a relief."
        mar "It's just that you seem trustworthy."
        mar "I wondered why you didn't say no."
        mar "I figured since you come to my office for help anyway,"
        mar "you wouldn't mind running a small errand."
        name "I did wonder if it was wise to leave your door unlocked."
        mar "Haha, yes, very careless of me."
        name "It caught me so off guard I didn't have time to think about it."
        mar "Okay, so we both found it strange."
        mar "That's reassuring."
        mar "Haha, I still can't get used to having such a big office."
        mar "Anyway, thank you for not overthinking it."
        mar "It really helped me out."
        mar "So then, how's the article coming along?"
        mar "Have you made any progress?"
        name "Yes, I've been working on it."
        mar "Let's see."
        mar "Did you send it to me?"
        name "Yes, I emailed it to you last night."
        mar "Well..."
        mar "What have you changed since last time?"
        name "Well... I just polished a few sections and added some references."
        mar "I see..."
        mar "Don't underestimate the work that still needs to be done."
        mar "You've made a good start, but some points need to be developed further."
        mar "For example, this paragraph here."
        mar "And this one too."
        name "I understand."
        mar "Alright, I'll let you work on that."
        mar "Don't hesitate to go to the research library if you need a quiet place."
        
        //Scene change//
        scene marion-office
        "I pack up my things and say goodbye to Mrs. Gillsberg."
        name "I'll head to the library right away."
        mar "Good idea. You'll be more productive there."
        scene marion-corridor with dissolve
        "I leave her office and walk down the hallway."
        scene secondfloorelevator with dissolve
        "I take the elevator down."
        scene secondfloorscreen with dissolve
        "I walk through the university corridors."
        "Students are scattered here and there, chatting or hurrying to their next class."
        scene universityresearchlibrary with dissolve
        "I arrive at the research library."
        "The atmosphere is calm and studious."
        "I find a quiet spot near the windows and settle in."
        scene ericsearchingforbooks with dissolve
        "I open my laptop and get back to work on my article."
        "With Mrs. Gillsberg's comments fresh in my mind, I know exactly what needs to be improved."
        "Time to focus."
        scene black with dissolve
        window hide
        pause
        scene ericsearchingforbooks with dissolve
        "After several hours of concentrated work, I finally feel satisfied with my progress."
        name "This is much better."
        name "I think I'm ready to show this to Mrs. Gillsberg."
        scene universityresearchlibrary with dissolve
        "I'm about to pack up when I notice someone approaching."
        "It's Mrs. Gillsberg."
        show marionneutral
        mar "Oh, hello! I didn't expect to see you here."
        name "Mrs. Gillsberg! I was just working on the revisions you suggested."
        mar "That's wonderful. May I?"
        "She gestures toward the empty chair beside me."
        name "Of course, please."
        hide marionneutral
        scene workingwithmarion with dissolve
        "She sits down and glances at my screen."
        mar "Let me see what you've done."
        "I show her the sections I've been working on."
        "She reads carefully, nodding occasionally."
        mar "Mm-hmm... yes, this is much better."
        mar "You've really taken my feedback to heart."
        mar "This paragraph flows much more naturally now."
        name "Thank you. Your comments were really helpful."
        mar "I'm glad to hear that."
        "She leans back in her chair, looking satisfied."
        mar "You know, it's refreshing to see a student who actually listens."
        mar "And who comes to the library to work, no less."
        name "Well, you recommended it. It really is a great place to focus."
        mar "Indeed it is."
        "There's a brief, comfortable silence."
        mar "How are you finding the research process overall?"
        mar "Is it what you expected?"
        name "It's challenging, but... I think I'm starting to enjoy it."
        mar "That's good to hear."
        mar "Research isn't for everyone, but those who enjoy it tend to excel."
        "She stands up."
        mar "Well, I won't disturb you any longer."
        mar "Keep up the good work."
        name "Thank you, Mrs. Gillsberg."
        mar "See you soon."
        "She walks away through the stacks."
        "I feel even more motivated now."
        $ marion_date_count += 1
        $ marion_date_done = True
        jump gardenuni_start2



# // Present article and ask task 2

    label Mariondate3:
        scene secondfloor
        "I arrive on the second floor of the university."
        
        scene secondfloorelevator
        "I take the elevator to the last floor."
        
        scene marion-corridor
        ""
        scene upbuilding
        ""
        scene marion-office
        ""
        show marionneutral
        mar "Hi! Come in."
        name "Hello, Mrs. Gillsberg. Thank you for seeing me again."
        mar "Of course, it's no problem."
        mar "So, have you made any progress on your article?"
        name "Yes, I've been working on it."
        mar "Let's see."
        mar "mh"
        mar "ça avance"
        mar "Je pense que vous devriez revoir ce paragraphe, l'argument pourrait être mieux amené"
        mar "Et évitez les tournures de phrases trop complexes."
        mar "Allez à l'essentiel!"
        name "Oui je comprend "
        mar "au fait je voulais vous demander une chose"
        mar "Avez vous déjà pensé à ce que vous voulez faire après vos études?"
        name "Pas vraiment"
        name "Pour l'instant j'ai envie de continuer à apprendre"
        name "Mais je ne suis pas sûr de ce que je veux faire avec toute ces connaissances"
        mar "Je vois"
        mar "C'est important de réfléchir à ça tôt"
        mar "La recherche demande beaucoup d'investissement personnel"
        mar "Il faut être sûr de ce que l'on veut"
        name "Oui je comprends"
        name "Bon je vais réfléchir à tout ça."
        mar "Très bien"
        "Je m'apprête à partir quand Mme Gillsberg m'interpelle"
        mar "Ah au fait, je fais une petite conférence cet aorès midi. Je ne sais pas si vous avez vus le mail."
        mar "Si vous voulez vous pouvez m'accompagner."
        mar "Pour... m'aider.."
        name "Vous aider?"
        mar "Oui un peu comme la dernière fois... vous voyez?"
        name "Heu.. oui d'accord"
        mar "Je me prépare et on y va alors."
        scene black with dissolve
        window hide
        pause
        scene marion-corridor with dissolve
        "We leave her office together."
        "Mrs. Gillsberg seems a bit preoccupied."
        mar "The conference room should be on the third floor."
        mar "I hope everything is ready."
        name "What's the conference about?"
        mar "Oh, it's just a presentation on recent research in art history."
        mar "Nothing too exciting, really."
        mar "But it's important to share our work with colleagues."
        scene secondfloorelevator with dissolve
        "We take the elevator down."
        scene thirdfloor_corridor with dissolve
        "We arrive on the third floor."
        "The hallway is quieter than usual."
        mar "Here we are."
        scene conferenceroom with dissolve
        "We enter a large conference room."
        
        mar "Please, take a seat."
        name "Of course."
        
        "Mrs. Gillsberg starts setting up her presentation."
        "She opens her laptop and begins connecting the cables."
        
        mar "Oh no..."
        name "What's wrong?"
        mar "My battery is almost dead."
        mar "I forgot to charge it this morning."
        
        "She rummages through her bag and pulls out a charger."
        
        mar "Could you plug this in for me?"
        mar "The outlet should be under the desk."
        name "Sure, no problem."
        
        "She hands me the charger."
        "I crouch down and look under the desk."
        
        scene black with dissolve
        "I find the outlet and plug in the cable."
        
        name "There, it's plugged in."
        
        "I stand back up and hand her the other end."
        "She connects it to her laptop."
        
        mar "Hmm, that's strange..."
        mar "It's not charging."
        name "Really?"
        mar "The indicator isn't showing up."
        mar "Could you check the connection under the desk?"
        
        "I crouch back down and check."
        name "It seems to be plugged in properly..."
        mar "Try pressing it in more firmly."
        
        "I push the plug in harder."
        name "Is it working now?"
        mar "Oh! Yes, it's charging now."
        mar "But... wait, it stopped again."
        name "Maybe the outlet is loose?"
        mar "Could you try holding it in place?"
        mar "Just to see if that's the problem."
        
        "I hold the plug firmly against the outlet."
        name "How about now?"
        mar "Yes, it's charging."
        mar "Oh, this is so inconvenient..."
        
        "She pauses for a moment."
        mar "I'm sorry to ask you this, but..."
        mar "Would you mind staying under there and holding it?"
        mar "Just until the battery charges a bit?"
        mar "I know it's awkward, but I really need the laptop for the presentation."
        
        name "Uh... sure, I can do that."
        mar "Thank you so much. I really appreciate it."
        mar "I'll try to make this as quick as possible."
        mar "Just keep the pressure on the plug."
        
        
        mar "Is it still charging?"
        name "Yes, the connection seems stable now."
        mar "Perfect. Thank you again."
        
        "I hear her typing on her keyboard above me."
        "The situation feels increasingly surreal."
        "Here I am, under a desk, holding a charger plug for my professor."
        
        mar "How are you doing down there?"
        name "I'm fine. My arm is getting a bit tired, but I can manage."
        mar "Just a few more minutes, I promise."
        mar "The battery is at 15% now."
        
        "Time seems to slow down."
        "I can hear her breathing, the clicking of her mouse."
        "The confined space under the desk feels strangely intimate."
        
        "Suddenly, I hear voices in the hallway."
        mar "Oh no... people are starting to arrive."
        name "Should I come out?"
        mar "Wait..."
        mar "If you come out now, it would look... strange."
        mar "People seeing you emerge from under my desk..."
        mar "That wouldn't look good."
        name "So what should I do?"
        mar "Could you... stay there a bit longer?"
        mar "Just during the conference."
        mar "I know it's a lot to ask, but..."
        mar "It would be really awkward to explain otherwise."
        name "You want me to stay under the desk during the entire conference?"
        mar "I'm so sorry. I know this is completely inappropriate."
        mar "But we don't have much choice now."
        mar "Just stay quiet and keep holding the plug."
        mar "I promise I'll make it up to you."
        name "I... okay."
        mar "Thank you. I owe you so much for this."
        
        scene conferenceroom_under with dissolve
        "I hear people entering the room."
        "Footsteps, conversations, chairs scraping against the floor."
        "I try to stay as still and quiet as possible."
        
        mar "Good afternoon, everyone. Thank you for coming."
        mar "Today I'll be presenting recent research in art history..."
        
        "Her voice takes on a professional tone."
        "I can see more legs now - colleagues and students taking their seats."
        "The absurdity of my situation hits me."
        
        "I'm crouched under my professor's desk, holding a charger plug."
        "During an academic conference."
        "This is completely surreal."
        
        "Mrs. Gillsberg continues her presentation."
        "Her voice is calm and confident."
        "Nobody suspects anything unusual."
        
        "From my position, I can see her legs clearly."
        "The way she crosses and uncrosses them occasionally."
        "I try to focus on holding the plug, but the proximity is... distracting."
        
        "I notice her perfume - subtle, sophisticated."
        "It's more intense down here, in this confined space."
        
        "The conference seems to go on forever."
        "My heart beats faster each time she shifts in her chair."
        "Each time her knee comes closer to where I'm crouched."
        
        scene black with dissolve
        window hide
        pause
        
        scene conferenceroom_under with dissolve
        "Finally, I hear applause."
        mar "Thank you all for your attention."
        mar "I'll be happy to answer any questions."
        
        "A few people ask questions."
        "Mrs. Gillsberg answers them professionally."
        "Her composure is remarkable, given the situation."
        
        "Eventually, people start to leave."
        "I hear footsteps, goodbyes, the door closing."
        "Then silence."
        
        mar "They're gone."
        mar "You can come out now."
        
        "I carefully release the plug and emerge from under the desk."
        "My legs are stiff from staying in one position so long."
        
        scene conferenceroom with dissolve
        "As I stand, our eyes meet."
        "There's something in her expression - a mix of amusement and warmth."
        
        name "That was... quite an experience."
        mar "I'm sure it was."
        
        "She leans back in her chair, a soft smile on her lips."
        
        mar "You did well. Thank you for being so patient."
        mar "Not everyone would have handled that situation so gracefully."
        name "I didn't really have much choice."
        mar "Perhaps. But you made it easier than it could have been."
        
        "The way she looks at me makes my heart beat a little faster."
        
        mar "I have to admit, I was a bit nervous."
        mar "Having you there, so close, during the entire conference..."
        name "What do you mean?"
        mar "Well, it was... intimate, wasn't it?"
        mar "You, crouched under my desk for so long."
        mar "I could feel your presence the whole time."
        
        "Her voice has become softer, almost tender."
        
        name "I was just trying to help."
        mar "I know. And I'm grateful."
        
        "She stands and walks closer, her movements graceful."
        "There's something magnetic about her presence."
        
        mar "You know what struck me?"
        mar "How comfortable you seemed down there."
        mar "Despite the awkwardness of it all."
        
        "My face grows warm."
        
        name "I... I didn't want to make things worse."
        mar "You didn't. Quite the opposite."
        mar "There was something... reassuring about knowing you were there."
        
        "She's standing close now, her perfume filling my senses."
        
        mar "This might sound strange, but..."
        mar "I felt safe. Knowing I could count on you."
        
        "I don't know what to say."
        "The air between us feels charged."
        
        mar "I hope I didn't make you too uncomfortable."
        mar "It's just... you seem different from other students."
        mar "More mature. More understanding."
        
        "She reaches out and gently touches my arm."
        
        mar "Thank you again."
        
        "Her touch lingers for a moment before she steps back."
        
        mar "Same time next week? For the article."
        mar "And... perhaps we could have that coffee we talked about."
        
        "The way she says it feels like an invitation to something more."
        
        name "I'd like that."
        mar "Good."
        
        "She smiles, her eyes warm."
        "There's a new understanding between us."
        "Something unspoken, but definitely there."
        $ marion_date_count += 1
        $ marion_date_done = True
        
        jump secondfloor_corridor
        label Marion_date4:
            scene secondfloor
            "I arrive on the second floor of the university."
            
            scene secondfloorelevator
            "I take the elevator to the last floor."
            
            scene marion-corridor
            ""
            scene upbuilding
            ""
            scene marion-office
            ""
            show marionneutral
            mar "Hi! Come in."
            name "Hello, Mrs. Gillsberg."
            mar "I'm glad you're here."
            mar "I need to prepare for a conference in a few minutes."
            mar "Would you mind accompanying me?"
            mar "I could use some help setting up."
            name "Of course, no problem."
            mar "Perfect. Let's go then."
            
            scene marion-corridor with dissolve
            "We leave her office together."
            
            scene secondfloorelevator with dissolve
            "We take the elevator down."
            
            scene thirdfloor_corridor with dissolve
            "We arrive on the third floor."
            
            scene conferenceroom with dissolve
            "We enter the conference room."
            "It's completely empty."
            mar "Good, we're early."
            mar "That gives us time to set everything up properly."
            
            "Mrs. Gillsberg walks over to the desk at the front of the room."
            "I follow her and help her arrange her materials."
            
            mar "Could you help me with the projector?"
            name "Sure."
            
            "We spend a few minutes setting up the equipment."
            "The room is quiet, almost intimate despite its size."
            
            mar "Thank you. You're very helpful."
            name "It's nothing, really."
            
            "She opens her laptop and starts going through her presentation."
            mar "Oh no..."
            name "What's wrong?"
            mar "My battery is almost dead."
            mar "I forgot to charge it this morning."
            mar "Could you plug in the charger? It should be in my bag."
            name "Of course."
            
            "I find the charger and look for an outlet."
            "There's one under the desk."
            
            name "I'll have to plug it in under the desk."
            mar "That's fine, go ahead."
            
            scene black with dissolve
            "I crouch down and reach under the desk."
            "I plug the cable into the outlet and connect it to her laptop."
            
            name "There, it's plugged in."
            
            "I stand back up."
            mar "Hmm, that's strange..."
            mar "It's not charging."
            name "Really?"
            mar "The indicator isn't showing up."
            mar "Could you check the connection under the desk?"
            
            "I crouch back down and check."
            name "It seems to be plugged in properly..."
            mar "Try pressing it in more firmly."
            
            "I push the plug in harder."
            name "Is it working now?"
            mar "Oh! Yes, it's charging now."
            mar "But... wait, it stopped again."
            name "Maybe the outlet is loose?"
            mar "Could you try holding it in place?"
            mar "Just to see if that's the problem."
            
            "I hold the plug firmly against the outlet."
            name "How about now?"
            mar "Yes, it's charging."
            mar "Oh, this is so inconvenient..."
            
            "She pauses for a moment."
            mar "I'm sorry to ask you this, but..."
            mar "Would you mind staying under there and holding it?"
            mar "Just for a few minutes, until the battery charges a bit?"
            mar "I know it's awkward, but I really need the laptop for the presentation."
            
            name "Uh... sure, I can do that."
            mar "Thank you so much. I really appreciate it."
            mar "I'll try to make this as quick as possible."
            mar "Just keep the pressure on the plug."
            
            "I settle into a more comfortable position under the desk."
            "I can see Mrs. Gillsberg's legs from where I'm crouched."
            "She's wearing professional shoes and dark stockings."
            
            mar "Is it still charging?"
            name "Yes, the connection seems stable now."
            mar "Perfect. Thank you again."
            mar "This is really embarrassing..."
            mar "I should have checked my battery before coming here."
            
            "I hear her typing on her keyboard above me."
            "The situation feels increasingly surreal."
            "Here I am, under a desk, holding a charger plug for my professor."
            
            mar "How are you doing down there?"
            name "I'm fine. My arm is getting a bit tired, but I can manage."
            mar "Just a few more minutes, I promise."
            mar "The battery is at 15% now."
            
            "Time seems to slow down."
            "I can hear her breathing, the clicking of her mouse."
            "The confined space under the desk feels strangely intimate."
            
            mar "Alright, it's at 20%."
            mar "That should be enough for the presentation."
            mar "You can come out now."
            
            "I carefully release the plug and emerge from under the desk."
            name "There we go."
            mar "Thank you so much. I know that was... unusual."
            mar "I'll need to get that outlet fixed."
            name "It's okay. I'm glad I could help."
            
            "She smiles warmly."
            mar "You're very patient."
            mar "Not many students would have done that without complaining."
            
            "Just then, we hear voices in the hallway."
            mar "Oh, people are starting to arrive."
            mar "You should probably take a seat."
            mar "Unless you'd prefer to leave?"
            name "I'll stay for the conference."
            mar "Wonderful."
            
            $ marion_date_count += 1
            $ marion_date_done = True
            
            scene conferenceroom_seated with dissolve
            "I take a seat in the back as people start filing in."
            "Mrs. Gillsberg greets them professionally, completely composed."
            "As if nothing unusual had just happened."
            
            scene black with dissolve
            window hide
            pause
            
            "The conference proceeds smoothly."
            "Mrs. Gillsberg's laptop works perfectly throughout."
            "When it's over, she thanks everyone and starts packing up."
            
            scene conferenceroom with dissolve
            mar "Thank you again for your help earlier."
            mar "I owe you one."
            name "Don't worry about it."
            mar "See you soon."
            
            jump secondfloor_corridor


label Marion_date4:

    mar "This is excellent."
    mar "You could almost publish it as is."
    mar "Well done."
    mar "There are only a few minor things to polish."
    "Mrs. Gillsberg smiles and returns to her desk."
    mar "I thought I'd have to teach you how to write, but it seems you've already grasped it."
    mar "well, I suppose I can help you refine it a bit."
    mar "But overall, it's very good."
    mar "Let's schedule another meeting once you've made those final adjustments."
    name "Thank you, Mrs. Gillsberg. I really appreciate your help."
    mar "It's my pleasure."
    mar "You know, you've done some really solid work here."
    mar "I'm impressed by your dedication."
    name "Thank you, that means a lot coming from you."
    mar "To be honest, it's rare to see a student so invested."
    mar "Most of them just want to get it over with."
    mar "But you... you seem genuinely passionate."
    name "I guess I am. Your guidance has been really motivating."
    mar "That's kind of you to say."
    "She pauses for a moment, seeming to consider something."
    mar "You know, I don't often do this, but..."
    mar "Would you like to grab a coffee sometime?"
    mar "We could discuss your future plans, maybe talk about research opportunities."
    mar "And... well, it would be nice to chat in a less formal setting."
    name "Oh, I'd like that."
    mar "Perfect."
    mar "How about tomorrow afternoon?"
    mar "There's a nice café on campus. Quiet, with good coffee."
    mar "It's where I go when I need a break from all the meetings."
    name "That sounds great."
    mar "Wonderful."
    "She smiles warmly."
    mar "I look forward to it."
    mar "See you tomorrow then."
    name "See you tomorrow, Mrs. Gillsberg."
    $ marion_date_count += 1
    $ marion_date_done = True
    jump secondfloor_corridor
# // Present article and ask to take a coffee

label Marion_date5:
    
label Marion_date5:
    scene marion-office
    show marionneutral
label Marion_date4:
    scene marion-office
    show marionneutral

    "Je suis déjà derrière le bureau de Marion, penché légèrement au-dessus de son épaule pour suivre sur l’écran la version finale de l’article que je lui ai envoyée."
    "Nos corps sont proches ; je sens la chaleur de son dos et son parfum discret."

    mar "This is excellent."
    mar "You could almost publish it as is."
    mar "Well done."

    "Elle fait défiler lentement le document, les yeux rivés sur l’écran, pointant certains passages du doigt."

    mar "Look here… the conclusion flows perfectly now."
    mar "These references are impeccable. You've really tied everything together."
    mar "I thought I'd have to teach you how to write, but it seems you've already grasped it."
    mar "Overall… it's very good. Truly remarkable."

    name "Thank you, Mrs. Gillsberg. I really appreciate your help."

    mar "It's my pleasure."
    mar "You've done some really solid work here."
    mar "I'm impressed by your dedication… and your patience."

    name "Thank you, that means a lot coming from you."

    mar "It's rare to see a student so invested."
    mar "Most just want to get it over with."
    mar "But you… you seem genuinely passionate. And obedient."

    name "I guess I am. Your guidance has been really motivating."

    mar "That's kind of you to say."

    "Elle ferme le document d’un clic lent."
    "Puis, sans un mot de plus, elle pivote lentement dans son fauteuil pour me faire face, les yeux levés vers moi."

    show marionwarm close at center with dissolve

    mar "Tu mérites une récompense… une vraie récompense."

    name "Je… merci, c’est déjà—"

    mar "Chut."

    "Elle se lève avec une grâce mesurée, le pantalon noir ultra-serré craquant légèrement quand elle déplie ses jambes."
    "Elle s’approche de moi, réduisant la distance jusqu’à ce que nos corps se frôlent presque dans l’espace étroit derrière le bureau."

    "Sa main droite monte doucement vers mon visage."
    "Elle caresse ma joue du revers des doigts, puis glisse jusqu’à ma mâchoire, la tenant légèrement."

    mar "Tu as été si sage… si attentif."

    "Sa main gauche rejoint ma nuque, puis remonte dans mes cheveux."
    "Elle pose sa paume à plat sur le sommet de ma tête."

    mar "À genoux."

    "Elle appuie doucement mais fermement, sans violence, juste une pression insistante et possessive."
    "Je plie les genoux, descendant lentement jusqu’à ce que mon visage soit à hauteur de son entrejambe."

    mar "Bien… exactement là."

    "Elle porte maintenant ses mains à sa ceinture fine en cuir noir."
    "La boucle cliquette doucement."
    "Le bouton saute. La fermeture Éclair descend millimètre par millimètre."

    mar "Regarde bien."

    "Le pantalon noir s’ouvre en V."
    "Pas de sous-vêtement."
    "Son sexe se dresse déjà, épais, veiné, la peau tendue et luisante à l’extrémité."
    "Le tissu sombre encadre sa hampe comme un écrin."

    mar "Tu vois l’effet que ton article a eu sur moi ?"
    mar "Ce que toi tu m’as fait, depuis des semaines ?"

    "Elle baisse lentement le pantalon jusqu’à mi-cuisses ; le tissu reste tendu, soulignant la puissance de ses jambes."

    mar "Embrasse-le d’abord."
    mar "Comme on embrasse quelqu’un qu’on admire."

    "Je pose mes lèvres sur le gland, très doucement."
    "Elle soupire longuement, un son grave et satisfait."

    mar "Encore… plus bas."

    "Petits baisers appliqués le long de la hampe, lents, révérencieux."

    mar "Mmmh… oui… exactement comme ça."
    mar "Tu sais si bien t’y prendre quand tu veux me plaire."

    "Elle glisse une main dans mes cheveux, la referme légèrement."

    mar "Ouvre la bouche maintenant."
    mar "Large. Et regarde vers le haut."

    "J’obéis. Elle guide son gland entre mes lèvres, très lentement."

    mar "Prends ton temps."
    mar "Suce-moi comme si tu voulais me remercier pour chaque correction, chaque conseil."

    "Je commence à bouger la tête, doucement d’abord, puis plus profond."
    "Elle laisse échapper de petits soupirs contrôlés."

    mar "Plus profond… essaie pour moi."
    mar "Je sais que tu peux."

    "Je descends jusqu’au fond."
    "Sa main guide sans forcer, possessive et tendre."

    mar "C’est parfait… tu es parfait comme ça."
    mar "Tu sens comme je gonfle dans ta bouche ?"
    mar "C’est toi qui fais ça. Ton talent. Ta dévotion."

    "Elle roule légèrement des hanches, petits mouvements mesurés."

    mar "Tu es à moi maintenant."
    mar "Cet article n’était qu’une excuse."
    mar "Ce que je voulais vraiment… c’était ta bouche autour de moi, ici, derrière mon bureau."

    "Sa respiration s’accélère légèrement, mais sa voix reste veloutée, posée."

    mar "Je vais jouir bientôt… et tu vas tout prendre."
    mar "Jusqu’à la dernière goutte."

    "Elle resserre sa prise dans mes cheveux."
    "Ses cuisses se tendent."

    "Mais soudain, elle s'arrête, se retire lentement de ma bouche avec un soupir contrôlé."
    "Son sexe palpite encore, luisant de salive, mais elle se retient, les yeux brûlants de désir contenu."

    mar "Non… pas encore."
    mar "Je veux plus que ta bouche."
    mar "Je veux te prendre… te posséder complètement."

    "Elle me relève doucement par les épaules, son regard possessif et tendre à la fois."
    mar "Tourne-toi. Mets-toi sur le bureau, à quatre pattes."

    "Je m'exécute, grimpant sur le bureau large, me positionnant à quatre pattes, les genoux et les mains sur le bois poli."
    "Le bureau est solide, assez grand pour supporter mon poids ; je sens le froid du bois contre mes paumes."

    "Marion s'approche par derrière, ses mains glissent sur mes hanches, descendant mon pantalon et mon sous-vêtement d'un geste fluide et assuré."
    mar "Voilà… ouvre-toi pour moi, mon chéri."
    mar "Je vais te prendre doucement d'abord… pour que tu sentes chaque centimètre."

    "Elle positionne son gland contre mon entrée, lubrifié par ma salive et son excitation."
    "Elle pousse lentement, très lentement, entrant millimètre par millimètre."
    "Je sens la pression, l'étirement progressif, chaud et envahissant."

    name "Ah… Marion…"

    mar "Chut… respire. Laisse-moi entrer."
    "Sa voix est douce, presque murmurée à mon oreille alors qu'elle se penche sur moi."
    "Elle caresse mon dos d'une main, apaisante, tandis que l'autre tient ma hanche fermement."

    "Une fois à moitié enfoncée, elle commence un va-et-vient lent, mesuré, laissant mon corps s'habituer."
    mar "Tu es si serré… si parfait pour moi."
    mar "Sens comme je te remplis… comme je te possède."

    "Le rythme reste doux au début, des mouvements fluides, presque tendres, qui font monter le plaisir progressivement."
    "Chaque poussée est accompagnée d'un petit soupir de sa part, et je sens son corps contre le mien, chaud et dominant."

    "Puis, progressivement, elle accélère, les coups de reins deviennent plus intenses, plus profonds."
    mar "Mmmh… oui… maintenant plus fort."
    mar "Tu le mérites… tu as été si bon."

    "Ses hanches claquent contre les miennes avec plus de vigueur, le bureau tremblant légèrement sous l'impact."
    "La sensation est intense, un mélange de plaisir et de soumission totale ; ses mains serrent mes hanches, me maintenant en place."

    mar "Tu sens ça ?"
    mar "C'est pour toi… tout pour toi."

    "Après plusieurs minutes d'intensité croissante, elle ralentit un instant."
    mar "Changeons… descends les pieds au sol."
    mar "Penche-toi sur le bureau."

    "Je glisse du bureau, me penchant en avant, les pieds fermement au sol, les mains posées à plat sur le bois, le torse incliné."
    "Cette position est plus stable, plus exposée ; mes jambes écartées légèrement pour l'accueillir."

    "Marion se repositionne derrière moi, ses mains caressant mes fesses avant de me pénétrer à nouveau."
    mar "Comme ça… parfait."
    mar "Je vais te prendre plus profondément maintenant."

    "Elle entre d'un coup plus assuré, reprenant le rythme intense de tout à l'heure."
    "Dans cette position, chaque poussée va plus loin, plus fort ; je sens son ventre contre mes fesses, ses seins effleurant mon dos quand elle se penche."

    mar "Tu es à moi… complètement à moi."
    mar "Sens comme je te remplis… comme je te fais mien."

    "Le plaisir monte, ses mouvements deviennent plus rapides, plus passionnés, mais toujours avec cette tendresse dominante dans sa voix."
    "Ses mains explorent mon corps, une sur mon dos, l'autre descendant pour caresser mon propre sexe durci."

    mar "Jouis pour moi si tu veux… mais attends-moi."

    "Soudain, on frappe à la porte — trois coups secs et inattendus."
    "Je sursaute, mais Marion ne s'arrête pas."
    "Au contraire, elle accélère légèrement, posant vivement une main sur ma bouche pour étouffer tout son potentiel."

    mar "Chut… ne dis rien."
    "Sa voix est un murmure brûlant à mon oreille, tandis que son autre main reste sur ma hanche, guidant ses coups de reins ininterrompus."

    "Les coups à la porte se répètent, plus insistants, mais Marion continue, son rythme intense et silencieux maintenant."
    "Sa main presse fermement sur ma bouche, m'empêchant de gémir, tandis que son sexe me pénètre profondément, sans relâche."

    mar "Ils partiront… et toi, tu restes à moi."
    mar "Sens comme je suis proche… comme je vais jouir en toi."

    "Le danger de la situation rend tout plus intense ; mon cœur bat la chamade, mais le plaisir est décuplé."
    "Marion accélère encore, ses cuisses claquant discrètement contre les miennes, jusqu'à ce qu'elle se tende enfin."

    mar "Maintenant… viens avec moi."
    # (suite immédiate après la deuxième position, penché sur le bureau, pieds au sol)

    "Marion ralentit progressivement ses coups de reins, restant profondément enfoncée en moi un long moment."
    "Son souffle est chaud contre ma nuque, sa main toujours plaquée sur ma bouche même si les pas dans le couloir se sont enfin éloignés depuis plusieurs minutes."

    mar "Ils sont partis…"
    "Elle retire lentement sa main de ma bouche, caresse mes lèvres du pouce comme pour s’excuser de la pression."
    mar "Tu as été si courageux… si silencieux pour moi."

    "Elle se retire avec une douceur infinie, son sexe encore dur glissant hors de moi."
    "Je sens son sperme chaud couler légèrement le long de mes cuisses ; elle sourit en le voyant."

    mar "Regarde ce que tu m’as fait faire…"
    mar "Mais ce n’est pas fini."

    "Elle me relève doucement par les hanches, me fait pivoter pour que je lui fasse face."
    "Ses yeux brillent d’un mélange de tendresse possessive et de désir inassouvi."

    mar "Viens."

    "Elle me guide par la main vers le petit canapé en cuir sombre qui occupe un coin du bureau — celui où elle reçoit parfois des collègues ou des doctorants pour des discussions informelles."
    "Elle s’assoit la première, dos contre le dossier, jambes légèrement écartées, son pantalon toujours baissé à mi-cuisses, son sexe dressé et luisant de nos fluides."

    mar "Monte sur moi."

    "Je grimpe sur le canapé, m’installant à califourchon sur ses cuisses."
    "Elle pose les mains sur mes hanches, me guide lentement pour que je m’abaisse sur elle."

    mar "Doucement… prends-moi en toi."

    "Je descends centimètre par centimètre ; la sensation est différente dans cette position — plus profonde, plus contrôlée par elle."
    "Une fois complètement empalé, je reste immobile un instant, haletant, les mains posées sur ses épaules pour garder l’équilibre."

    mar "Regarde-moi."

    "Nos regards se verrouillent."
    "Elle commence à bouger les hanches par en dessous, de petits mouvements circulaires d’abord, puis des poussées plus affirmées vers le haut."

    mar "Bouge avec moi… monte et descends."
    mar "Montre-moi à quel point tu veux me faire plaisir."

    "Je commence à onduler, me soulevant puis redescendant sur sa longueur."
    "Chaque descente est accompagnée d’un petit gémissement étouffé de sa part ; ses mains serrent mes hanches, guidant le rythme sans jamais le brusquer."

    mar "Oui… exactement comme ça."
    mar "Tu es magnifique quand tu chevauches."
    mar "Si ouvert… si à moi."

    "Le canapé grince légèrement sous nos mouvements synchronisés."
    "Elle glisse une main entre nous, caresse mon sexe durci au rythme de nos va-et-vient, synchronisant le plaisir."

    mar "Tu sens comme je te remplis complètement ?"
    mar "Comme je suis faite pour être en toi ?"

    "Elle accélère progressivement, ses hanches se soulevant plus fort pour venir à ma rencontre à chaque descente."
    "La position cowgirl inverse les rôles apparents : c’est toujours elle qui dirige, qui impose le tempo, qui décide de la profondeur et de la vitesse."

    "Je m’exécute, montant et descendant avec plus d’intensité, nos peaux claquant doucement l’une contre l’autre."
    "Ses seins se soulèvent sous sa chemise entrouverte à chaque poussée ; elle rejette la tête en arrière un instant, les yeux mi-clos de plaisir."
    
        # (suite immédiate après la position cowgirl sur le canapé)

    mar "God, you're still so tight around me… but I'm not done with you yet."
    mar "I want to see your face when I fuck you senseless one last time."

    "She lifts you off her slowly, her cock slipping free with a wet sound, still rock-hard and glistening."
    "She stands, pants around her thighs, and pulls you gently by the wrist toward the floor."

    mar "Down. On your back. Now."

    "You lie on the thin blanket she spread out. Marion kneels between your legs, eyes dark with hunger."
    "She grabs the backs of your thighs and folds you in half — knees pushed toward your chest, legs spread wide and high in the air."

    mar "Look at you… legs up like a desperate bitch in heat."
    mar "Your hole's twitching already — begging for my cock again, isn't it?"

    "She lines herself up, the thick head pressing against your entrance, still slick and open from before."
    "She pushes in slowly, deliberately, watching your face the whole time."

    mar "Fuck… feel that? Every inch stretching you open again."
    mar "You're such a greedy little whore for it, taking me so deep."

    name "Marion… please…"

    mar "Please what? Please fuck you harder? Please breed you like the needy slut you are?"
    "She starts thrusting — slow at first, letting you feel the drag and push, then gradually picking up speed."

    mar "Listen to that wet sound… that's your cunt swallowing me whole."
    mar "You're dripping for me, aren't you? My perfect little cock-sleeve."

    "Her hips snap forward harder now, each thrust driving deep, making your legs shake in the air."
    "She leans over you, folding you even more, her chest brushing yours, eyes locked on yours."

    mar "Look at me while I pound this tight hole."
    mar "Watch your professor fuck you like the desperate bitch you turned out to be."
    mar "You love it, don't you? Legs spread, ass up, getting railed on my office floor."

    "Her pace turns relentless — long, powerful strokes that hit deep every time."
    "The blanket bunches under you; the desk nearby rattles faintly with each impact."

    mar "I'm gonna fill you again… pump you so full you'll be leaking me for hours."
    mar "Gonna breed my little whore until you're overflowing."

    "She speeds up even more, breath ragged, voice low and filthy."

    mar "Fuck — I'm close… gonna cum so deep inside you…"
    mar "Beg for it. Beg your professor to breed your slutty hole."

    "Her thrusts become erratic, brutal, possessive."
    "Then she slams in one last time, burying herself to the hilt."

    mar "Take it — take every fucking drop!"

    "She comes hard, cock pulsing violently, flooding you with thick, hot spurts."
    "She grinds against you, milking out every last pulse, groaning low in her throat."

    mar "Yes… fuck yes… feel that? All mine now… stuffed and claimed."

    "She stays buried inside you for a long minute, breathing heavily, still holding your legs high."
    "Finally she eases back, watching her cum slowly leak out as she pulls free."

    mar "Look at the mess I made of you… my perfect little cum-dump."
    "She runs two fingers through the slick mess between your legs, then brings them to your lips."

    mar "Clean them. Taste how much I gave you."

    "After you obey, she softens slightly — strokes your cheek, kisses you slow and deep."

    mar "You were incredible… my good little bitch."
    mar "Next time — my place. All night. No holding back."

    "She helps you sit up, pulls you into a tight embrace."

    mar "Go clean yourself up… but don't think we're done."
    mar "Come back tomorrow. I already want you again."


    jump secondfloor_corridor