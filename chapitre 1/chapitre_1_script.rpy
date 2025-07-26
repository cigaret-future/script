define lau = Character('Laura', color="#c8c8c8") 


label cafe:
    stop music fadeout 2.0
    play music "music/coffee.mp3" fadein 1 volume 1.0 loop
    show screen cafescreen

    call screen cafescreen





label barmaid1:
    if laura_repeat == True:
        scene cafe2 with dissolve
        
        show barmaidneutral with dissolve

        lau "Hey, I might not look like it, but I actually work right now, so just tell me what you want."
        menu: 
            "I'd like a coffee.": 
                lau "I'll bring it to you."
            
                scene smallcoffe

                "Always nice to kick back and enjoy a coffee." 
                
                "It's something we tend to overlook these days."
                jump cafe

            "I'm just looking around.": 

                hide barmaidneutral
                show barmaidpissed
                lau "Don't do anything stupid, alright? I'm watching you."
                jump cafe
    else:
        scene cafe2

        show barmaidneutral with dissolve
        
        "The waitress looks tired, like she's about to fall asleep." 
        "She's pretty though."

    lau "Hi, what can I get for you?"

    name "Hello, I just moved into the neighborhood, I live right nearby. Do you serve anything special here?"

    lau "Not really, mostly just coffee and alcohol in the evenings."

    name "Ah, too bad. I'll just have a coffee then."

    lau "Sure."

    name "Do you have any special coffees?"

    hide barmaidneutral 

    show barmaidpissed

    lau "...?"

    lau "Special coffee?"

    name "You know, something that ends with the letter 'o'? Or with some expensive milk?"

    lau "You want milk in your coffee?"

    name "Oh yes, great."

    hide barmaidpissed 

    show barmaidsleep

    lau "(Sigh)"

    lau "Alright, have a seat."

    hide barmaidsleep with dissolve

    "I find an empty table and sit down."
    "She doesn't seem very enthusiastic about her job, but she seems friendly."
    "The coffeeshop is filled with young people, likely students."
    "I'm excited to be a student myself. The holidays have been refreshing;"
    "I hope this year turns out great."

    show barmaidneutral

    lau "One latte."

    "She casually places the cup on the table."

    name "Thanks. How long have you been working here?"

    hide barmaidneutral

    show barmaidtired3

    lau "Too long. I do this alongside my studies."

    name "Oh, you're also in college? Cool! What are you studying?"

    lau "Geography."

    name "Nice! I'm studying art history. Maybe we'll bump into each other."

    hide barmaidtired3

    show barmaidsmug

    lau "I doubt it."

    name "Ah, you're probably in a different part of the building."

    lau "Yeah, that's it, I'm in a different building."

    lau "Plus, I mostly work from home, and I gotta be here for my shift."

    name "Alright, I'll see you around here then."

    lau "Sure."

    lau "If you've bought something, feel free to hang out in the coffee shop."

    hide barmaidsmug

    "She returns behind the bar to wash some glasses. I think she kinda likes me."

    $ laura_repeat = True
    jump cafe