label sarahdate:
    if sarah_cafe == True:
        jump sarahdatecafe2

    elif sarah_count >= 1 and sarah_cafe == False:
        jump sarahdate1

    elif sarah_count == 0:
        jump sarahnotdate



label sarahdatecafe2: 
    scene cafesarah2
    sar "Hey, you!"
    name "Hey, you're here."
    name "Yeah, I was just wandering around."
  
    scene testsarahcafe
    name "How are you?"
    sar "I'm good, and you?"
    name "I'm good too."
    "I feel like there's a strange tension between us."
    name "Are you working remotely?"
    sar "Yeah, I need to focus."
    sar "I wanted to work here, but I think I'll go home. I'm too distracted here."
    sar "How's college going?"
    name "It's going... I'm keeping up for now."
    name "I'm trying to make progress on my thesis."
    sar "Cool, have you found a professor to supervise you?"
    name "Yeah, I have. It's..."
    scene hisacha
    sac "Hey, everyone."
    sac "Sorry to interrupt you."
    sac "I saw you in the coffee shop."
    sar "Hey, aren't you working today?"
    sac "Normally, yes, but I think I'm going to change jobs."
    name "Why?"
    sac "My manager is an asshole, that's why."
    scene sachatalkingcafe
    sac "That jerk accused me of stealing clothes from the store."
    sar "What?!"
    sac "It's a fucking thrift store. Of course, a pair of pants are going to disappear."
    sac "He only noticed it because he probably wanted them for himself."
    name "That's messed up."
    sac "Nah, I’m not going to work today. If I do, I might lose it and strangle him."
    sar ""
    sac "What are you guys up to?"
    if gender == "male":
        sar "[name] just arrived, and we were talking about his thesis."
    elif gender == "fem":
        sac "[name] just arrived, and we were talking about her thesis."
    
    sac "Ah, cool."
    scene sachatalkingcafe2 with dissolve
    sac "Don't you guys wanna go out for a bit? I need to enjoy my day off."
    sar "Man, why don’t you just sit down for a change?"
    sac "Nah, I need to move."
    sar "I am going to go home to work soon, so..."
    sac "I wanted to go buy a book at the bookstore. You guys wanna come?"
    sac "[name], come with me. I bet you don't know this store."
    sac "I'm sure you'll find some great books for your thesis."
    name "Sure, why not?"
    sar "I'm staying here. Have fun, guys."
    scene black
    "We leave the coffee shop with Sacha."

    scene walkingsacha
    "As we walk, Sacha tells me about his job at the thrift store."
    "He tells me about his manager and the job he would like to do."
    scene walking2
    "I listen to him talk and ask him questions."
    "I'm mostly happy to be able to explore the city with him."
    "After a few minutes of walking, we arrive in front of a bookstore on a small, discreet street."
    scene ericsachaenteringbiij
    "The bookstore is small, but it looks cozy."
    sac "Come, you'll see. There are always nice books in sight."
    
    scene lookingatbooksacha
    sac "You can ask the sales assistant if you're looking for something specific."
    name "I'm going to look around a bit."
    sac "Oh, look, this is new!"
    scene sachaericbookstore3
    "I look at the books placed on the table one by one."
    "They are art or social science books in large public formats."
    sac "I love this format, where you just have a photo and a bit of text next to it."
    sac "I want to buy everything."
    name "Yeah, me too."
    "We hang out in the bookstore for a while."
    "We read the summaries of the books and share our impressions."
    "I end up choosing a book on photography."
    name "I'm going to take this one."
    scene gobuyingbooksacha
    ""
    scene buyingbooksacha
    name "Hi!"
    "I hand the book to the sales assistant."
    oli "Hi, nice choice! I love this author's work."
    name "Yeah, me too."
    oli "He actually came to the shop to present his latest publication. He's super nice."
    name "Oh, really?"
    oli "Yes, we organize meet-and-greets with artists we like."
    oli "You can follow us on social media to stay updated."
    name "I'll check it out, thanks."
    oli "Here's your change."
    oli "Have a great day!"
    name "Thanks, you too!"
    scene goingoutbooksacha
    name "You didn't get anything?"
    sac "I need to know if I'll be unemployed first."
    sac "This place is nice, right?"
    name "Yeah, thanks for bringing me here."
    sac "No problem. I like to come here to relax."
    scene streeteric
    "We walk around the neighborhood."
    sac "Hey, how do you get along with Sarah?"
    sac "She seems to like you a lot."
    name "Yeah, she's cool."
    name "I actually went to her place the other day."
    sac "Oh, really?"
    sac "It took me at least a year to really get close to her."
    sac "We used to argue all the time at first."
    scene streeteric3
    sac "But now, we're super close."
    name "It's awesome to have a good friend living in the same building."
    sac "Yeah, she's like a big sister to me."
    name "She definitely gives off that vibe."
    sac "But don’t be fooled—she can be wild too."
    name "Oh yeah, like what?"
    sac "I mean, nothing extravagant."
    sac "She just likes to have fun, that's all."
    scene streeteric4
    "Sacha receives a text message."
    sac "It's Elise. She's asking if I want to meet her at a bar."
    sac "She's not far from here."
    sac "Do you want to come?"
    menu:
        "Let's go":
            "Alright, let's go."
            jump elisesachadate

        "I have stuff to do":
            name "I think I'll head back home."
            sac "Alright, see you later then."
            name "See you."
            $ sarah_relation_status_text = "I should hang out to the coffee shop"
            $ sarahcafe_conv2_done = True
            $ sarah_cafe = False
            $ sarah_conv_done = True
            $ sacha_conv_done = True
                   
            jump map3

label sarahelisecafe: 
    scene elisesarahcafe
    "Elise is sitting at the table with Sarah."
    name "Hey, what's up, guys?"
    elise "Hey, [name]."
    sar "Hey, you."
    scene kisseric
    "As I sit down, Sarah wraps her arm around my neck and kisses me on the cheek."
    "I can smell her perfume and feel her breath on my skin."
    "I'm surprised, but I don't move."
    "It feels like we're a couple, but I'm not sure."
    scene elisesarahericcafe
    "Elise looks upset but doesn't say anything."
    name "What are you guys doing here?"
    elise "We're talking about work."

    elise "So, as I was saying, I think you're letting your team slack off too much."
    scene elisesarahericcafe2
    elise "It's going to come back to bite you."
    sar "Yeah, I know."
    scene eliseaskin7
    sar "It's just that I'm too nice."
    elise "You need to be firmer."
    sar "I know."
    name "Was there a problem?"
    elise "Her team messed up a project."
    elise "I would never have let that happen."
    sar "Yeah, I know."
    sar "I'll take care of it."
    scene eliseaskin9
    sar "Anyway, do you want something to drink, [name]?"
    name "No, I'm good."
    sar "Okay."
    name "Do you have any plans after this?"
    sar "Not really. I have to work later."
    scene eliseasking
    elise "I'm free."
    $ sarah_elise_cafedate_done = True
    elise "I don't have work today."
    elise "If you want, you can come to my place to check out the books I mentioned."
    $ sarah_elise_cafe = False
    menu: 
        "Okay, I'm down":
            elise "Perfect, let's go."
            sar "See you guys."
            scene black
            "We leave the coffee shop with Elise and head toward her place."
            jump elisedate
        "I'd rather stay here":
            scene black
            "Elise leaves after a while."
            "Sarah and I stay at the coffee shop."
            "Then Sarah goes back to work."
            name "I'll go with you. I'm heading back anyway."
            "I leave the coffee shop with Sarah."
            
            scene walkingstreetsaraheric
            sar "Don't you think Elise would make a good manager?"
            name "Yeah, maybe."
            name "She might be a bit toxic, though."
            sar "Yeah, probably."
            sar "She's quite direct."
            sar "I don't think my team would handle her well."
            name "She seems like the type to make you cry if you provoke her."
            sar "Haha, yeah, I see what you mean."
            name "She has a bit of a stern face, doesn't she?"
            sar "But I think she's a good person."
            sar "She's pretty open-minded."
            sar "Despite her upbringing in a rather conservative environment."
            name "Yeah, I see."
            sar "Some people never leave their social bubble."
            sar "I think she did."

            scene walkingstreetsaraheric2
            "We walk down the street, chatting."
            "Sarah tells me stories about her work."
            "I listen and laugh with her about her adventures."
            scene walkingstreetsaraheric3
            sar "Alright, I need to head back to work."
            sar "It was nice seeing you."
            sar "..."
            "She looks at me for a moment."
            "I feel like she wants to say something."
            
            scene walkingstreetsaraheric10 with dissolve
            "Suddenly, she leans in and kisses me."
            "I'm caught off guard, but I remain still."
            "Her moist tongue slides along my lips."
            "I feel her cock pressing against my thigh."
            "A wave of heat washes over my face."
            "She gently presses her lips, exhaling her warm breath into my mouth."
            "We share a soft, lingering kiss for several minutes."
            "Then she pulls away."
            scene walkingstreetsaraheric11 with dissolve
            sar "I'll see you later."
            
            $ sarah_elise_cafedate_done = True
            $ sarah_elise_cafe = False
  
            jump map3