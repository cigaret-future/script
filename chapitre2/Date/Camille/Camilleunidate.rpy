label camilleuni_date:
    play background universitycoffeeshop volume 2 loop
    scene upview3 with dissolve
    "We enter the coffee shop, and Camille guides me to a table by the window."
    "She greets her friend and introduces her to me."

    scene camilldeunidate19 with dissolve
    cam "[name], this is my friend Amy."
    name "Nice to meet you, Amy."
    "Amy smiles warmly, her eyes sparkling with curiosity."
    av "Nice to meet you too."
    scene camilldeunidate17 with dissolve
    play sound drinkcoffee volume 2 noloop 
    "Amy and Camille dive into conversation about their blog and upcoming ideas."
    "They exchange the latest gossip, critiquing various influencers and debating current trends."
    "I listen quietly, enjoying the dynamic between them even though I understand very little."
    scene camilldeunidate18 with dissolve
    "They clearly know each other well, and I don't mind being an observer."
    "Though I can't help feeling a bit forgotten in their animated discussion."
    "I glance around the coffee shop, watching other customers come and go."
    "After a while, Amy turns to me with a friendly smile."
    scene camilldeunidate14 with dissolve
    av "How's your coffee?"
    name "It's really good, thanks."
    name "Sorry, I was trying to follow along..."
    name "...but there were too many names and brands I don't know!"
    name "So I didn't really follow along."
    av "Ahah, no problem!"
    av "We can talk about something else."
    av "So, how did you two meet?"
    scene camilldeunidate20 with dissolve
    "Camille seems amused by the question."
    play sound drinkcoffee volume 2 noloop 
    cam "We met in class..."
    if gender == "male":
        cam "He was sitting next to me, and I thought he looked like a nice guy."
        cam "So I decided to be nice to him."
    elif gender == "fem":
        cam "She was sitting next to me, and I thought she looked like a nice girl."
        cam "So I decided to be nice to her."
    av "Really? Camille being nice to someone?"
    "Camille rolls her eyes playfully."
    av "So you study art history, is that right?"
    name "Yep, and you?"
    av "I'm studying psychology."
    av "I love understanding how people think and behave."
    name "Yeah I bet."
    av "It's fascinating."
    av "And on the side I'm a fashion fan, so I started the blog with Camille."
    name "That's cool. Do your courses help with the blog?"
    av "Not always, but I sometimes use psychological concepts to analyze trends and people's behavior."
    av "And it can help with relationships too."
    name "I can see that."
    cam "Amy sees people like lab rats."
    cam "She's mentally working on a case study every time she meets someone."
    cam "She told me that once."
    av "Haha, come on, I don't do that with everyone."
    av "Just sometimes there are interesting cases."
    cam "She won't tell you, but in her head, you're already a study subject."
    cam "She's picturing you running on a wheel."
    av "No way, not at all!"
    name "Haha, I don't mind being a subject of study, must mean I'm an interesting person!"
    cam "Yeah but you don't know what she's studying, or how she does it!"
    cam "She'll make you do weird stuff."  
    cam "And you'll wake up with a plastic object in your ass."
    av "Oh very funny Camille."
    if gender == "male":
        cam "Maybe he'll like it."
    elif gender == "fem":
        cam "Maybe she'll like it."
    av "No, no, I promise I won't do anything weird."
    name "I hope."

    av "The people I like to study are usually those in the fashion world."
    av "I swear it's really fascinating to watch."
    cam "I bet there are plenty of people we meet who would love to become your lab animals."
    "Camille and Amy continue to joke about psychology and fashion, their laughter filling the coffee shop."
    "The vibe gets way more chill as we keep talking."
    "Amy starts asking me about what I do outside university."
    "Time flies by while we're just chatting about random things."
    "Then Amy checks her phone and her eyes go wide."
    av "Oh shit, I totally lost track of time."
    scene amyleave
    av "I gotta meet my study group in like twenty minutes."
    "She starts grabbing her stuff."
    av "This was fun!"
    av "We should totally do this again."
    name "Yeah, for sure. It was cool meeting you."
    cam "I'll hit you up later, Amy."
    "Amy waves and rushes out of the coffee shop."
    scene amyleave2
    "Now it's just me and Camille at the table."
    cam "She totally liked you, I could tell."
    "Camille grins and takes another sip of her coffee."
    cam "Wanna head back?"
    name "Yeah, let's go."
    "We finish up and head out of the coffee shop."
    cam "It was cool hanging out."
    cam "We should do this again sometime."
    name "Yeah, definitely."
    name "See you."
    cam "See you, lab rat."
    stop background fadeout 0.5
    $ class_done = True
    scene black with dissolve
    "I head back to the garden."
    jump gardenuni_start2
