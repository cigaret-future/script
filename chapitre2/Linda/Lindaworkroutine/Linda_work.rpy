label linda_workroutine:
    
    default anais_flirtcount = 0
    default linda_flirtcount = 0
    default linda_workday_count = 0
  


    
    $ linda_workday_count += 1
    scene anaislindadate-lindaopening
    "Linda greets me at the door."
    lin "Hey, ready for another day of fun?"
    name "yaay!"
    lin "Let’s get to work then."
    scene black with dissolve
    "We heat up some coffee and settle in to work in Linda’s room."    
    scene anaislindadate-workin2 with dissolve
    window hide
    pause
    if linda_workday_count == 1:
        jump linda_work_1
    elif linda_workday_count == 2:
        jump linda_work_2
    elif linda_workday_count == 3:
        jump linda_work_3
    elif linda_workday_count == 4:
        jump linda_work_4
    elif linda_workday_count == 5:
        jump linda_work_5
    else: 
        jump linda_work_routine


label linda_work:
    scene anaislindadate-workin2
    "We work for a few hours. She has me read dense academic articles."
    lin "You should take notes."
    name "Yeah, I'm already trying to understand what's written."
    lin "That's exactly why taking notes helps with understanding."
    name "Hmm..."
    name "Okay.."
    "After a few hours of work, Linda gets up to go to the bathroom."
    "I let out a sigh; the pace is intense, and I feel like she's monitoring how I'm managing."
    "Linda seems to be talking on the phone in the bathroom."

    menu:
        "Take a break in the living room":
            jump lindadate_casual
        "Continue working.":
            "I'll keep going a bit longer."
            
            jump linda_work_end

label linda_work_1:
    scene anaislindadate-workin2
    "The workday begins..."
    "Linda is showing me how to analyze high-resolution images of paintings."
    "I pour myself several coffees."
    "My eyes sting. The cursor blinks in a half-written caption.  
    Linda leans in, zooms on a tiny detail in the negative."
    lin "See that scratch? That’s how you know it’s the original."
    name "oh i see.."
    lin "Yeah. Details matter."
    "We keep working for a while..."
    "Linda blinks slowly, then stands up and stretches."
    "I could suggest taking a break"

    menu:
        "Take a break and go to the living room":
            name "Hey, I think I’m going to take a break"
            lin "As you want, but don’t go too far"
            
            jump lindadate_casual
        "Continue working.":
            "Almost… there…"
            jump linda_work_end


label linda_work_2:
    scene anaislindadate-workin2
    "We spend hours working, each on our own."
    "Linda checks her watch and yawns."
    lin "Okay, my retinas are fried. Five-minute screen break?"
    name "Finally!"
    lin "Don’t get too excited. You’re coming right back."
    "She heads to the bathroom to refill her water."
    name "I could stretch my legs…"

    menu:
        "Take a break in the living room":
            jump lindadate_casual
        "Continue working.":
            "I’ll just… blink. Slowly."
            jump linda_work_end


label linda_work_3:
    scene anaislindadate-workin3
    "We spend hours working, each on our own."
    "Linda leans back, rubs her temples."
    lin "I’m gonna lie down for ten minutes. Don’t touch my computer."
    name "A nap? Now?"
    lin "It's a power nap.. "
    lin "You should do the same..."
    "She grabs a throw pillow and curls up on the bed."
    "Soft breathing fills the room within seconds."

    menu:
        "Take a break in the living room":
            jump lindadate_casual
        "Continue working.":
            "Don’t wake the curator…"
            jump linda_work_end
   

label linda_work_4:
    scene anaislindadate-workin2
    "My screen is a chaos of open tabs: Louvre database, Getty Provenance Index, auction catalogues."
    "I try to focus, but I can feel my brain starting to overload."
    "Her phone buzzes. She frowns."
    lin "Shoot. I need to step out, I have to return a book I borrowed from someone..."
    name "Now?"
    lin "Yeah, I promised I'd return it today."
    lin "I'll be right back."

    "She grabs her keys and slips outside."

    menu:
        "Take a break in the living room":
            jump lindadate_casual
        "Continue working.":
            jump linda_work_end


label linda_work_5:
    scene anaislindadate-workin1
    "Linda’s been drilling me on InDesign layout for an hour straight."
    lin "Caption: ‘Circle of Rubens, ca. 1620–25’. Not ‘Follower of’."
    name "I got it the first five times…"
    "She stands, stretches."
    lin "I need air. Walking to the mailbox. Back in three."
    name "Freedom!"
    lin "Don’t even think about opening Instagram"
    "She’s out the door before I can reply."

    menu:
        "Take a break in the living room":
            jump lindadate_casual
        "Continue working.":
            "She’ll spot a misaligned caption from space…"
            jump linda_work_end
        


label linda_tease:
    lin "Hey, you look distracted."
    name "Huh? Oh, no, I'm just... thinking."
    lin "Thinking about what?"
    name "Just... the article I have to write."
    lin "Mmm..."
    lin "You know, I don't think you should worry so much about that article."
    name "What do you mean?"
    lin "You need to learn to relax a little."
    lin "You already have a lot on your plate with that thesis."
    name "Yes, that's true..."
    "She gets up and sits on the bed."
    lin "Why don't you take a little break?"
    name "What? Now?"
    lin "Yes, now."
    lin "J'ai besoin que tu me détendes un peu."
    
    menu:
        "Accept":
            lin "Come over here."
            lin "Kneel down in front of me."
            jump linda_workbj
            
        "Decline and continue working.":
            name "No, I should keep working."
            lin "Suit yourself."
            scene black with dissolve
            "Linda prend une pause de quelques minutes puis reviens s'asseoir"
            
            jump linda_work_end
    
    
    
    