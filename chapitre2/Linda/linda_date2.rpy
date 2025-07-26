



label linda2: 

    scene uni1
    show unilindaout2

    show lindalooksupleft
    name "Hi Linda! What's up today?"

    lin "Oh hey, [name]!"

    lin "I'm working, as you can see."
    
    lin "Have you thought about which professor you're going to choose?"

    name "Hmm, I think I'll go with the history professor you're working with. Mrs.Gillsberg"

    hide lindalooksupleft
    show lindaconfident
    lin "Good choice. She can be quite strict, but it's for good reasons."

    name "Really? Ugh, I don't know. I'm not always comfortable with overly authoritative personalities."

    lin "She's not really authoritative, just demanding. She pushes you to be demanding of yourself too."

    name "Yeah, I get it. Like pushing your limits and all that."

    hide lindaconfident
    show lindalookupleft 
    lin "Exactly. Why settle for good when you can be excellent?"

    name "Well, not everyone can be excellent."

    lin "Everyone can try, but not everyone will succeed. You have to feel it inside, you know?"

    name "I suppose you're right."

    lin "Of course I am, [name]."

    hide lindalookupleft
    show lindapose17
    lin "Anyway, do you want to work somewhere after class? I can help you with your thesis if you want."

    name "Yeah, sure. Where do you want to go?"

    hide lindapose17
    show lindahapp
    lin "We can go to a coffee shop. It'll be more comfortable, and we can drink something better than machine coffee."

    name "I'm in."

    lin "Lets roll!"

    hide lindahapp
    if gender == "fem" and characterdesign_done == False:
        scene characterdesign2
        window hide
        pause
        menu:
            "continue":
                pass
            "Don't show me that message again":
                $ characterdesign_done = True
                pass
    scene streetcar2
    "We leave the university and head to the street. Linda leads me to the northern part of the city, towards the business district."

    scene street25
    lin "So, how long have you been here? I don't remember seeing you last year."

    name "I moved here a month ago, but I came back two days ago for the start of classes. I was with my parents this summer." 
    name "I'm happy to be in the city, it's so much better than the suburbs."

    lin "Absolutely, everything you need is right here."

    name "Yeah, it's amazing! And the amount of people, it's impressive."

    lin "Yeah, it can even be overwhelming sometimes."

    scene streeteric2

    name "I feel like I'll never get tired of it."

    lin "Yeah, as long as you're a student it's fine, but once you start working, your view of the city changes."

    name "The metro, the people, the bars, everything gets more exhausting."

    name "We have to enjoy these years."

    lin "Totally."

    "We continue walking until we arrive at a rather fancy bar."

    scene streeteric5

    lin "And here we are, my little spot to chill and work."

    name "Pretty fancy. Are you sure you're not taking me on a date without telling me?"

    lin "Don't be ridiculous..."

    name "I'm just teasing you."

    scene cafeworking

    "We sit down at a table near the window and order. Linda takes out her laptop and starts typing while talking about her thesis."

    "I listen to her, but I can't help but feel a little overwhelmed by the amount of work she's done."

    "From time to time, I ask her questions."


    lin "...And that's how you build your thesis statement."

    name "I see, it doesn't get done in a few days."

    lin "No, you have to take your time, go over it a little every day."

    name "Phew... that sounds exhausting."

    "I take a sip of coffee."

    "Linda looks at me seriously."

    scene cafeeric2

    lin "Yeah, that's why you need to be disciplined."

    name "Hm I'm not a fan of that word."

    "Linda looks at me for a long moment in silence."

    lin "I think you need discipline."

    name "Really?"

    lin "I mean, you seem a bit scatterbrained. Having someone to push you might be good."

    scene cafeeric4
    lin "who knows, maybe you'll like it." 

    name "Huh, what?"

    lin "you know what I mean."

    name "I am not sure I do."

    scene lindasarcasl
    lin "I'm sure you don't make your bed in the morning."

    name "Depends on the day!"

    lin "Haha, yeah, you don't do it."

    name "So what?"

    lin "So you are a mess"

    name "Come on, I consider myself a serious student."

    scene finalheadshot
    lin "Tomorrow you'll do it. If you want my help, you have to put in some effort too."

    name "And if I don't?"

    lin "You'll be in trouble."

    name "Haha."

    "I take it as a joke, but Linda seemed pretty serious."

    scene lindastandupe
    lin "I'll get the check, stay here."

    "I stay seated. Linda goes to pay, then we leave the cafe."

    lin "Okay, see you tomorrow."

    name "Bye, and thanks for today."

    $ linda_2nd_conv_done = True
    $ linda_conv_done = True

    show screen minicarte3
    call screen minicarte3
