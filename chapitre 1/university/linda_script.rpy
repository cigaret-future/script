define lin = Character('Linda', color="#e6a7ff") 

label linda1:

    

    scene uni1
    show unilindaout2
    show lindaannoyed

    
    name "Hey, I was in the amphitheatre earlier. I saw you there."
    
    lin "Oh, hi! You.. saw me?..."
    
    name "Yeah, I mean someone told me to come see you for some infos. I wanted to come talk to you but you left too quickly."

    name "Anyway, I'm new here and I was wondering if you could help me choose a professor for my thesis."
    hide lindaannoyed
    show lindalooksupleft
    
    lin "Oh i see. Sure I can help. I know the professors pretty well."
    
    name "Great, I don't know where to start."

    lin "Well it's a big decision for your studies."
    
    lin "You should pick someone who fits you, not just someone who seems charismatic."
    
    lin "Some people choose their professor based on their influence at the university."
    
    hide lindalooksupleft
    show lindanewangle
    
    lin "But I think that's a mistake because those professors might just use you for their own gain."
    
    lin "There are a lot of things to consider. I can guide you if you want."

    lin "personaly i choose Mrs.Gillsberg"
    
    name "Wow, you really know your stuff. Maybe I should let you choose for me."
    
    lin "Haha, no, you need to find someone you feel comfortable with."
    
    name "Yeah, you're right."
    
    hide lindanewangle
    show lindapose24
    
    lin "What do you want to work on?"
    
    name "I was thinking about studying the representation of women in early 20th-century films."
    
    hide lindapose24
    show 3rdpose
    
    lin "Hmm, that's pretty broad. Are you focusing on Europe or the United States?"
    
    name "Haha, I haven't decided yet. Maybe Europe?"
    
    lin "There are probably big differences between the two. That could be an angle for your research."
    
    hide 3rdpose
    show lindapose23
    
    lin "But you'll likely need to focus on a specific country."
    
    name "Yeah, probably. I'll think about it."
    
    lin "It's an interesting topic, though it's been studied a lot lately. Maybe too much, but it depends on your approach."
    
    name "I know, my topic isn't particularly original, but I feel it could be meaningful."
    
    hide lindapose23
    show lindapose22
    
    lin "Yeah, you need to believe in it, or you'll give up quickly."
    
    name "Have you decided on your topic yet?"
    
    lin "Yeah, I'm working on the representation of Mercury through commerce, alchemy, eloquence, and imitative arts in the modern era."
    
    name "Wow, that sounds really specific."
    
    lin "Yeah, I spent the summer deciding on it. My professor will probably nominate me for a thesis scholarship."
    
    name "I didn't know there was a selection process for scholarships. I thought you just had to complete the thesis."
    
    hide lindapose22
    show lindasmile
    
    lin "Haha, you're so naive. Of course there's a selection process. Professors can't supervise just anyone."
    
    name "I see, it's going to be competitive."
    
    lin "That's why the sooner you choose your topic, the better your chances of being selected."
    
    name "You're off to a good start then."
    
    hide lindasmile
    show lindalooksup3
    
    lin "Yeah, pretty much. Honestly, I don't think the others in my class have much of a chance."
    
    name "Wow, that's harsh."
    
    lin "Yeah, I know, but it's true."
    
    name "I guess if you worked for it you deserve it."
    
    lin "Exactly."
    
    name "Well, I'll let you get back to work."
    
    
    
    hide lindalooksup3
    show lindadesire
    
    lin "Hey! If you want, I could help you with your thesis."
    
    name "What? Really? I wasn't expecting that from you."
    
    lin "Uh, why not."
    
    name "Are you sure? You seem pretty busy."
    
    hide lindadesire
    show lindapose21
    
    lin "I mean, if I have time, I will."

    lin "Anyway, I have to go. See you."
    
    "She quickly packs up her things and awkwardly heads for the exit. She seemed nervous, maybe she needed to go to the bathroom." 
    "Anyway, it was nice of her to offer to help. She seemed serious."
    "With a friend like her, I should be able to handle this thesis."

    $ linda_1st_conv_done = True
    $ linda_conv_done = True

    show screen uniscreenlindaout
    call screen uniscreenlindaout

