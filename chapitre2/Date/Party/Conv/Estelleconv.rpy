label estelleconv :
    label estelleconv_direction:
        
        if drink_count >= 5 and estellebourreconv_done == False:
            jump estelleconvbourre1
        elif drink_count >= 5 and estellebourreconv_done == True:
            jump estelleconvbourre2


        elif estellepartyconv_count == 0:
            jump estelleconv1
        elif estellepartyconv_count == 1:
            jump estelleconv2
        
    label estelleconvbourre:
        label estelleconvbourre1:
            scene livingroomarrow
            scene livingroomarrowflou with dissolve
            show estherparty with dissolve
            name "You know you have the same eyes as my cat."
            est "Thanks, I guess?"
            name "No, it's a compliment! He's very mysterious. And a bit aggressive."
            est "What's his name?"
            name "Uh, I don't know."
            show esther15 with dissolve
            hide estherparty with dissolve
            est "You don't know your cat's name?"
            name "No, but I don't have a cat. But if I did, he'd have those eyes."
            est "..."
            name "Do you want to come to my place? He needs an eye model."
            est "No thanks."
            $ estellebourreconv_done = True
            $ estellepartyconv_count += 1
            jump livingroom
            
        label estelleconvbourre2:
            scene livingroomarrow
            scene livingroomarrowflou with dissolve
            show esther12 with dissolve
            est "Are you okay?"
            name "Sure, I just need to dance a little."
            name "Do you want to dance with me?"
            est "No thanks."
            est "Just so you know, if you faint, don't count on me to help you."
            name "Thanks, I knew I could count on you."
            $ estellebourreconv_done = True
            $ estellepartyconv_count += 1
            jump livingroom

    label estelleconv1:
        scene livingroomarrow
        scene livingroomarrowflou with dissolve
        show estherparty with dissolve
        if estelle_firstconv_done == True:
            est "Hey, are you here?"
            name "Yeah, Zoey and Bruno invited me."
            est "Cool..."
        else:
            est "Hey, do I know you?"
            name "We must have crossed paths at college."
            est "Oh, okay. Well, I don't know you very well."
            est "We probably wouldn't have much to talk about, I think."
            est "No offense, I like people who have interesting story to tell."
            name "wow that's so rude"
            jump livingroom
        est "soo..."
        name "sooo..."
        name "Tu connais beaucoups de gens ici?"
        est "Oui la plupart"
        name "oh ok"
        est "Mais je ne suis pas là pour faire la fête"
        est "Je suis là pour me faire un peu de fric"
        name "ah bon?"
        est "Oui, je fais un peu de babysitting"
        name "ah ok"
        est "Mais je ne fais pas ça pour l'argent"
        name "ah bon?"
        est "Je fais ça pour la gloire"
        name "la gloire?"
        est "Oui, je suis une influenceuse"
        name "ah ok"
        est "Je fais des vidéos sur les réseaux sociaux"
        name "ah ok quelle genre de vidéo?"
        est ""
        if estelle_spankconv_done == True:
            est "hey, ducoup tu cherches quelque chose en particulier ici?"
            name "qu'est ce que tu veux dire?"
            show estherhorny2 with dissolve
            hide estherparty with dissolve
            est "Ba tu sais.."
            est "Quelqu'un qui te remettes à ta place"
            est "en te mettant des fessées par exemple"
            name "what, je vois pas de quoi tu parles"
            est "Tu sais, je suis pas la seule à avoir remarqué que tu es un peu trop sage"
            est "Tu"
            
        hide estherparty
        
        jump livingroom