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
    $ Marion_date_done = True
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

    if article_progress >= 90:
        mar "This is excellent."
        mar "You could almost publish it as is."
        mar "Well done."
        mar "There are only a few minor things to polish."
        "Mrs. Gillsberg smiles and returns to her desk."
        mar "I thought I'd have to teach you how to write, but it seems you've already grasped it."
        mar "well, I suppose I can help you refine it a bit."
        mar "But overall, it's very good."
        mar "Let's schedule another meeting once you've made those final adjustments."

    elif article_progress >= 50:
        "She leans in closer, as if to get a better look."
        mar "Not bad at all."
        mar "You're making solid progress, quickly and competently."
        mar "There's still some work to do."
        mar "Let's meet again when you've made more progress."
        name "sure"

    elif article_progress >= 10:
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
    if 90 <= article_progress < 94:
        mar "well..."
        mar "What have you changed since last time?"
        name "well... I just polished a few sections and added some references."
        mar "I see..."
        mar "Ne sous estimez pas le travail qu'il reste à faire."
        mar "Il faut être minutieux pour réussir dans la recherche."
        mar "Bon j'ai déja lus ce que vous avez fait."
        mar "On verra quand vous aurez finis."

    elif article_progress >= 2:
        "She leans in closer, as if to get a better look."
        mar "Not bad at all."
        mar "You're making solid progress, quickly and competently."
        mar "There's still some work to do."
        mar "Si vous voulez vous pouvez travailler à la bibliotheque de recherche."
        mar "C'est un endroit calme et propice à la concentration."
        
        if corridorconv_done == True:
            name "yes I know"
            name "I'll go there next time."
            mar "Stay focus."
            mar "See you later."
            name "Alright, goodbye!"
        else:
            name "I didn't know that place."
            mar "You should go there sometime."
            mar "It's much better than the student library."
            mar "I can show you if you want."
            mar "Je dois y passer pour travailler aujourd'hui."
            mar "On peut y'aller ensemble"
            name "That would be great, thank you."
            mar "Perfect let's go then."
            jump Marion_librarydate
        

    elif article_progress < 20:
        mar "You are not really making much progress yet."
        mar "It's ok, writing takes time."
        mar "Let me know when you have something more substantial."
        name "yeah... I have been struggling a bit."
        name "I am not really used to this kind of work."
        mar "..."
        mar "Yeah.. I guess you'll have to learn."
        name "Yeah, I'll try my best."
        if research_chosen == True:
            mar "Research is not for everyone."
            mar "I mean you are sweet, but I need dedicated students."
            mar "I have a lot of things to do.."
            name "I am sorry"
            name "I wish I could help."
            mar "What?"
            name "I mean..."
            name "I could help you.. with ... things"
            mar "Hmm..."
            mar "Like what?"
            name "Je ne sais pas, vous n'avez besoin de rien?"
            mar "Quoi vous voulez être mon assistant?"
            mar "ahah"
            name "Why not?"
            mar "I'll think about it."
            mar "Maybe you can help me with some errands."
            mar "I'll let you know."
            mar "On se voit plus tard alors.."
            name "alright."
            name "See you!"
            if gender == "male":
                mar "Goodbye, Mr. Smith."
            else:
                mar "Goodbye, Ms. Smith."
            jump secondfloor_corridor
        else:
            mar "Alright."
            mar "Hey maybe you could help me with something."
            mar "Maybe this article idea is not the best fit for you."
            mar "Would you be interested in assisting me with some tasks?"
            mar "I might found you something that fits you better."
            name "Sure, I would like that."
            mar "Great, let's talk about it next time."
            name "Alright, see you!"
            mar "bye!"

        
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
    if search_chosen == True:
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
    show marionneutral
    mar "Hi! Come in."
    name "Hello, Mrs. Gillsberg. Thank you for seeing me again."
    mar "Of course, it's no problem."
   
    mar "So, have you made any progress on your article?"
    name "Yes, I've been working on it."
    mar "Let's see."
    mar "Did you send it to me?"
    name "Yes, I emailed it to you last night."
    if 90 <= article_progress < 94:
        mar "well..."
        mar "What have you changed since last time?"
        name "well... I just polished a few sections and added some references."
        mar "I see..."
        mar "Ne sous estimez pas le travail qu'il reste à faire."
        mar "Il faut être minutieux pour réussir dans la recherche."
        mar "Bon j'ai déja lus ce que vous avez fait."
        mar "On verra quand vous aurez finis."

    elif article_progress >= 50:
        ""

# // Present article and ask task 2
label Marion_date3:


label Marion_date4:
# // Present article and ask to take a coffee

label Marion_date5:
# // Present article and SScene




label marionmail:
    if gender == "male":
        "Hello Mr. Smith,"
    else:
        "Hello Ms. Smith,"
    "I wanted to remind you that you're welcome to visit my office if you need help with your article."
    "I'd be happy to review it with you in person."
    "Best regards,"
    "Marion Gillsberg"

label marionmail2:
    "Hello [name],"
    "I hope you're doing well."
    "Just a quick reminder that the university library is an excellent place to work on your article."
    "Feel free to stop by if you need a quiet, focused environment."
    "Sincerely,"
    "Marion Gillsberg"

label marionmail3:
    "Hello [name],"
    "I hope your article is progressing well."
    "I really enjoyed our conversation in the corridor the other day."
    "I look forward to speaking with you again soon."
    "Sincerely,"
    "Marion Gillsberg"

label marionmail4:
    "Hello [name],"
    "I wanted to let you know I'm organizing a small meeting with some students from my class next week."
    "It would be a good chance to meet other students and discuss your work."
    "Please let me know if you'd like to join."
    "Sincerely,"
    "Marion Gillsberg"



