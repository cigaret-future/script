label Elise:

    scene cafeelisefinal
    scene cafeelisefinalblur with dissolve
    

    elise "Hey! What's up?" 
    show test05 with dissolve
    name "Hey Elise"
    elise "Are you here to sit and work?"
    menu:
        
        "Yes, I needed to get out of the house to work":
            jump work_here
        "No, nothing special, I was just passing by, i am not staying":
            jump just_passing




label work_here:
    name "Yeah, I needed to get out a bit to work."
    elise "Oh cool, you can work at my table if you want."
    elise "What are you working on?"
    name "My thesis."
    name "But I don’t want to bore you with that."
    elise "You know, I have a degree in literature."
    elise "Maybe I can help you."
    show test02 with dissolve
    hide test05 with dissolve
    elise "I was a student too, after all."
    name "Oh, that’s cool."
    elise "Yeah, I’ve been there."
    elise "Originally, I wanted to be a journalist."
    name "By studying literature?"
    elise "Yes, it’s important to know literature even if it’s not explicitly required."
    elise "People pay attention to those kinds of details."
    name "So, how did you end up in advertising?"
    show test05 with dissolve
    hide test02 with dissolve
    elise "My parents, who were supporting me financially, had a sort of crisis."
    elise "They told me I needed to find a job."
    name "Ah, shit. That must’ve been rough."
    elise "Yeah, it was. My parents were never good with money, and they lost a big chunk of their income in just a few days."
    name "That sucks."
    elise "Yeah… I didn’t handle it well at first, but my father found me a job in advertising."
    elise "At first, I worked alongside my studies, but eventually, I started to like it, so I went full-time."
    name "Wow, okay. And your parents? Are they doing better now?"
    elise "Yeah, you know, they lost money, but they’ll never truly be broke."
    name "How come? Are they rich?"
    elise "Kinda, I come from a noble family."
    elise "They have plenty of connections, so they’ll never really be in need, unless they seriously mess up."
    elise "There are always people willing to lend them money."
    name "That's convenient..."
    name "And you’re a noble too?"
    elise "Yes, [name], that’s how it works."
    name "Wow, so..."
    name "You grew up in a castle?"
    show test03 with dissolve
    hide test05 with dissolve
    elise "Of course not, you idiot."
    
    elise "I grew up in a big house, but it wasn’t an actual castle."
    elise "I got the kind of education nobles get, with some fancy rules and stuff."
    show test05 with dissolve
    hide test03 with dissolve
    elise "I learned to speak several languages when I was a kid."
    name "That’s impressive."
    elise "Yeah, I think it's pretty cool too, haha."
    name "How did you manage to pick up so many languages?"
    elise "I had a private tutor."
    elise "It was a friend of my father."
    name "I mean, I can barely speak English."
    show test02 with dissolve
    hide test05 with dissolve   
    elise "I could be your tutor if you want, haha."
    name "Honestly, I could use that."
    name "I feel like at university they expect me to speak a more... complicated language."
    elise "Yes, it's a habit you need to develop."
    elise "If you stay with me, you'll already improve your English."
    elise "And I can give you private lessons."
    name "How much do you charge?"
    
    show test05 with dissolve
    hide test02 with dissolve
    elise "For a studious and disciplined student like you,"
    elise "I'll give you a discount."
    name "Haha, thanks, although I am not that disciplined."
    elise "I can arrange that too."
    "I am not sure if she is joking or not."
    name "Well, I already have a lot of work with my thesis."
    elise "As you want."
    show test06 with dissolve
    hide test05 with dissolve
    elise "So... What’s your thesis about?"
    name "I’m studying the representation of women through cinema in the 20th century."
    elise "Interesting."
    elise "You should look to the Museum of Cinema for inspiration."
    elise "They have a lot of old movies there."
    elise "They could help you."
    name "Thanks, I’ll keep that in mind."
    show test07 with dissolve
    hide test06 with dissolve
    elise "Maybe I'll go back to studying at some point."
    name "Oh, really?"
    elise "I liked the atmosphere, the young people, the parties."
    elise "Meeting beautiful, intelligent, interesting people."
    elise "It's exciting."
    "She fixes me for a moment."
    name "Yeah, I get that."
    name "I haven't been to many parties yet, but I imagine there must be a lot of them."
    elise "You'll find some if you come out of your shell."
    elise "You just have to take the plunge and talk to people."
    name "Yeah, I guess."
    elise "You should come to our parties in the meantime, until you make some friends."
    elise "It'll help you relax."
    name "Yeah, I guess."
    name "Well, I think I should work a bit on my thesis."
    elise "Sure, you can work here with me."
    name "Okay, let's do that."
    hide test07
    scene black
    "I take out my laptop and start diving into my notes."
    "We stay silent for a while."
    "From time to time, I ask Elise for advice."
    scene legshot
    "She helps me rephrase some sentences."
    "Every time she corrects me, she presses her foot against my leg."
    "Sometimes gently, sometimes insistently."
    "But I don't say anything."
    "After an hour, I start to get tired."
    scene cafeelisefinalblur
    show testees
    name "Well, I've made good progress, I am gonna go."
    elise "Already?"
    name "Yeah, I need to."
    if gender == "male":
        elise "Anytime, boy..."
    elif gender == "fem":
        elise "Anytime, girl."
    name "Thanks, that's kind of you."
    name "See you."
    hide testees with dissolve
    $ sarah_relation_status_text = "I'll probably meet Sarah in the stairs (She'll ask to see you in a few days if you run into her in the stairs)"
    $ elise_cafe_conv_done = True
    $ elise_cafe = False

    hide test05 with dissolve
    jump cafedirection

label just_passing:
    elise "Okay, whatever."
    hide test05 with dissolve
    
    jump cafedirection
