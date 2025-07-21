label sebastianconv:
    if sebastianconv_count == 0:
        jump sebastianconv1
    elif sebastian_mission_started == True and sebastianconv_count == 1:
        jump sebastianconv3
    elif sebastian_asked_done == True:
        jump sebastianconv4
    elif sebastianconv_count == 1:
        jump sebastianconv2
    
    else:
        jump sebastianconv2
    label sebastianconv1:
        scene balconynobodyarrow
        scene balconynobodyarrowflou with dissolve
        show sebastian1 with dissolve
        seb "Hey!"
        name "Hey there..."
        seb "How's it going?"
        name "I'm good, just exploring around a bit."
        if gender == "male":
            seb "Nice, you seem like a pretty chill guy."
        elif gender == "fem":
            seb "Nice, you seem like a pretty chill girl."
        
        seb "It's good to see."
        name "Yeah, sure."
        seb "I'm Sebastian, by the way."
        name "I'm [name]."
        seb "Want to grab a drink?"
        name "Yeah, sounds good."
        seb "Here you go."
        "I take the beer Sebastian hands me and take a sip."
        $ drink_count += 1
        show text "Your mind feels a bit fuzzy." at Move((0.5, 0.6), (0.5, 0.5), 10.0)
        pause 5.0
        hide text with dissolve
        seb "So, what do you do?"
        name "Uh, I'm a student. I'm doing a master's in art history."
        seb "That's cool, I'm really interested in that field."
        seb "I've always been fascinated by art and its impact on society."
        seb "I love watching documentaries about ancient civilizations and their art."
        name "Yeah, I had a few classes about that."
        seb "Personally, I love everything about South American civilizations."
        seb "The Incas, the Mayas, the Aztecs..."
        name "Yeah, it's really interesting."
        seb "Did you know the Incas used to choose the most beautiful young people for sacrifices to their gods?"
        seb "It was their way of keeping the gods happy."
        name "Yeah... I remember hearing about that."
        seb "It's kind of dark, but also really interesting."
        seb "Anyway, maybe we shouldn't get too deep into that, or people will think we're weird."
        seb "Did you come here with anyone?"
        name "Yes, I came with some friends."
        name "What about you?"
        seb "Yeah, I'm here with my crew."
        seb "We're in business school, we're in the same class as the girl who lives here."
        seb "Did you meet her?"
        name "No, I think she opened the door for me, but I didn't really talk to her."
        seb "She's a chill girl, but a bit uptight."
        seb "Her dad is nice though."
        seb "He works in trading."
        seb "When we met him, he gave us lots of advice on how to invest."
        seb "He has real financial discipline."
        seb "Apparently, he's been doing that since he finished his studies, and it's worked out well for him."
        name "Yeah, it seems to be going well for him."
        name "I wonder if I chose the wrong path."
        seb "Haha, no, don't worry, there will always be a need for people to talk about art."
        seb "We can't all be traders."
        name "Yeah, that's true."
        "One of Sebastian's friends calls out to him."
        seb "I'll be right back."
        

        $ sebastianconv_count += 1
    
        hide sebastian1 with dissolve
        jump balcony

    label sebastianconv2:
        scene balconynobodyarrow
        scene balconynobodyarrowflou with dissolve
        show sebastian1 with dissolve
        seb "Yeah, as I was saying, you should really consider investing."
        seb "It's actually pretty accessible."
        seb "All you need is a computer and a bit of free time."
        seb "You can start small, and as you get the hang of it, you can put in a bit more."
        seb "You want to invest, right?"
        name "Not really, I don't have much money to invest."
        seb "You can invest just a little, but still get good returns."
        seb "The thing is, you just need to have the right sources."
        name "I'll think about it."
        seb "Yeah, you should."
        seb "So, do you have someone in mind?"
        name "No, not really."
        seb "I need to find someone for tonight."
        seb "It's been too long."
        seb "..."
        name "cool.."
        name "I hope you find someone."
        seb "I saw plenty of hot girls inside."
        seb "It shouldn't be too hard."
        name "Alright.. good luck then"
        seb "Thanks, you too!"
        $ sebastian_open = True
        jump balcony

    label sebastianconv3:
        scene balconynobodyarrow
        scene balconynobodyarrowflou with dissolve
        show sebastian1 with dissolve
        seb "This apartment is really amazing."
        seb "And so well located..."
        seb "One day I'll have a place like this."
        name "Hey Sebastian, I was wondering if you could help me with something."
        seb "Sure, what's up?"
        name "I met this girl inside, and I think she might be interested in you."
        seb "Really? What makes you say that?"
        name "She kept asking about you when I mentioned I was talking to someone out here."
        seb "Interesting... What's she like?"
        name "She is the girl in the kitchen with the pink sweatshirt and the ponytail."
        seb "Oh, I think I know exactly who you mean."
        seb "I noticed her earlier."
        name "Well, she definitely seemed curious about you."
        seb "That sounds promising."
        seb "I should probably go find her before the moment passes."
        name "Absolutely, go for it. Good luck!"
        show sebdrinking with dissolve
        hide sebastian1 with dissolve
        seb "Thanks, I'll finish this drink and head back inside."
        
        $ sebastian_asked_done = True
        
        $ sebastianconv_count += 1
        hide sebastian1 with dissolve
        jump balcony

    label sebastianconv4:
        scene balconynobodyarrow
        scene balconynobodyarrowflou with dissolve
        "I think he got the message."
        jump balcony