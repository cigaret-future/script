label linda_work_end:
    scene black with dissolve
    if linda_workday_count == 1:
        jump linda_workend1
    else:
        jump linda_workend1

label linda_workend1:
    scene anaislindadate-workin3
    "After a few more hours, Linda stands up and stretches."
    lin "Okay, that's enough for today."
    name "Phew… finally."
    lin "You did good. I'm impressed."
    name "Thanks… I tried."
    if marion_first_validation_done == True and linda_article_talk == False:
        lin "By the way, is everything going well with Mrs. Gillsberg about your thesis?"
        name "Yes, she's pretty nice."
        lin "I told you."
        name "She asked me to write an article first."
        "Linda lifts her gaze from her screen."
        lin "Oh really?"
        lin "An article..."
        lin "You didn't tell me."
        name "Well, yes, I thought she asked that of everyone..."
        lin "Not everyone."
        lin "Well, not to new students."
        lin "Usually that comes after one year."
        name "Ah yeah, I see..."
        lin "She must have seen potential in you..."
        name "Does that surprise you?"
        lin "Not at all..."
        lin "It's just unusual..."
        lin "Have you started working on it?"
        name "Yes, I've already made good progress."
        lin "That's good."
        lin "But did you meet to talk about it?"
        name "Yes."
        lin "Where?"
        lin "In her office?"
        name "Of course."
        lin "And?"
        name "Well, she told me I was making good progress and that she could help me if I needed it."
        lin "... Wtf..."
        lin "I mean... good for you."
        name "What's wrong?"
        lin "It's just that..."
        lin "You just arrived... and it's very unusual for her to get so involved right away."
        lin "Especially since she hasn't been able to read much of your work yet."
        name "Do you think she has ulterior motives?"
        lin "I don't know..."
        name "What, are you jealous?"
        lin "Me jealous? Of Mrs. Gillsberg?"
        lin "You must be joking."
        lin "Anyway... we've worked enough for today."
        lin "You should go home and rest a bit."
        $ linda_article_talk = True
    
    lin "Review your notes tonight."
    name "Okay, Mom..."
    lin "Don't get smart with me."
    "She playfully ruffles my hair."
    "She walks me to the door."
    lin "See you, [name]."
    name "Bye!"
    jump linda_workroutine

label linda_workend2:
    scene anaislindadate-workin4
