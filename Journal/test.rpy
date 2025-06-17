
# label ju:
#     call HugandZoeyStart

# label HugandZoeyStart:
   
#     scene corridor10
    
#     if linda_1st_conv_done == True:
#         "I wander in the corridor until I arrive in front of the administration, on the 1st floor."
#         show hugopose11 at left:
#             xalign 0.3
        
#         hug "So, did you find what you were looking for?"
        
#         name "Yeah, Linda suggested I go see Mrs. Gillsberg."

#         hug "She knows her stuff."

#         name "Definitely, she even offered to help me with my thesis topic."

#         hug "Seriously?"

#         name "I think so."
        
#         show zoeypose04 at right:
#             xalign 0.7
            
#         zoey "That doesn't sound like her."

#         hug "Yeah, she'll probably charge you for it but hasn't told you yet."

#         name "You think?"

#         hide hugopose11
#         show hugopose08 at left:
#             xalign 0.3
#         hug "That's what she told me when I asked for her class notes."

#         name "Man, I hope she doesn't, I'm broke."

#         name "She seemed nice though."

#         hug "Yeah, she is... how to say it..."
#         hide zoeypose04
#         show zoeypose07 at right:
#             xalign 0.7
            
#         zoey "She's quite a character."

#         hug "That's putting it mildly."

#         name "Well, I hope she can help me. I'm still not sure about my topic."
#         hide hugopose11
#         show hugopose10 at left:
#             xalign 0.3
#         hug "Oh man, I need to get on that too."

#         hide zoeypose04
#         show zoeypose03 at right: 
#             xalign 0.7
#         zoey "Come on, Hugo... you still haven't found one yet." 

#         hide hugopose10
#         show hugopose09 at left:
#             xalign 0.3

#         hug "I am working on it, okay! I have too many ideas."

#         zoey "Yeah, right... you're just lazy."
        
#         zoey "That's what you get for spending your summer at festivals instead of working."

#         name "I thought you needed a topic to start a master's program."

#         zoey "Hugo has a way of getting on the professors' good side, right?"

#         hide hugopose09
#         show hugopose08 at left:
#             xalign 0.3

#         hug "They believe in my talent."

#         zoey "Sure, your talent for getting wasted."

#         hug "Hey, I'm a serious student too! I just like to have fun."

#         hide zoeypose03
#         show zoeypose01 at right:
#             xalign 0.7
#         zoey "Talking about fun, give me your phone number. If there's a party, I'll let you know."

#         name "Oh, ok, thanks. That's nice of you."

#         hug "No problem."

#         hide zoeypose01
#         show zoeypose11 at right:
#             xalign 0.7
#         "Zoey winks at me. That was weird."

#         name "Okay. Let's stay in touch."

#         name "Oh, by the way, do you know where Mrs. Gillsberg's office is?"
#         hug "Yeah, it's on the 6th floor. It's an office with a large window."

#         name "Thanks, see you."

       
#     elif linda_1st_conv_done == False: 
#         "I wander in the corridor, looking for a brunette with a black sweater."
#         "Hugo is there with a friend of his."
#         "Maybe I should ask him where I can find Linda."
#         show hugopose07 at left:
#             xalign 0.3
#         name "Hey, have you seen Linda? I couldn't find her in the amphitheater."

#         hug "No, I haven't seen her. Maybe she's in the library. She's always there."

#         name "Thanks, I'll go check there."
#         hide hugopose07
        
#     call linda1

# label linda1:
#     define lin = Character('Linda', color="#e6a7ff") 

# label linda1:

    

#     scene uni1
#     show unilindaout2
#     show lindaannoyed

    
#     name "Hey, I was in the amphitheatre earlier. I saw you there."
    
#     lin "Oh, hi! You.. saw me?..."
    
#     name "Yeah, I mean someone told me to come see you for some infos. I wanted to come talk to you but you left too quickly."

#     name "Anyway, I'm new here and I was wondering if you could help me choose a professor for my thesis."
#     hide lindaannoyed
#     show lindalooksupleft
    
#     lin "Oh i see. Sure I can help. I know the professors pretty well."
    
#     name "Great, I don't know where to start."

#     lin "Well it's a big decision for your studies."
    
#     lin "You should pick someone who fits you, not just someone who seems charismatic."
    
#     lin "Some people choose their professor based on their influence at the university."
    
#     hide lindalooksupleft
#     show lindanewangle
    
#     lin "But I think that's a mistake because those professors might just use you for their own gain."
    
#     lin "There are a lot of things to consider. I can guide you if you want."

#     lin "personaly i choose Mrs.Gillsberg"
    
#     name "Wow, you really know your stuff. Maybe I should let you choose for me."
    
#     lin "Haha, no, you need to find someone you feel comfortable with."
    
#     name "Yeah, you're right."
    
#     hide lindanewangle
#     show lindapose24
    
#     lin "What do you want to work on?"
    
#     name "I was thinking about studying the representation of women in early 20th-century films."
    
#     hide lindapose24
#     show 3rdpose
    
#     lin "Hmm, that's pretty broad. Are you focusing on Europe or the United States?"
    
#     name "Haha, I haven't decided yet. Maybe Europe?"
    
#     lin "There are probably big differences between the two. That could be an angle for your research."
    
#     hide 3rdpose
#     show lindapose23
    
#     lin "But you'll likely need to focus on a specific country."
    
#     name "Yeah, probably. I'll think about it."
    
#     lin "It's an interesting topic, though it's been studied a lot lately. Maybe too much, but it depends on your approach."
    
#     name "I know, my topic isn't particularly original, but I feel it could be meaningful."
    
#     hide lindapose23
#     show lindapose22
    
#     lin "Yeah, you need to believe in it, or you'll give up quickly."
    
#     name "Have you decided on your topic yet?"
    
#     lin "Yeah, I'm working on the representation of Mercury through commerce, alchemy, eloquence, and imitative arts in the modern era."
    
#     name "Wow, that sounds really specific."
    
#     lin "Yeah, I spent the summer deciding on it. My professor will probably nominate me for a thesis scholarship."
    
#     name "I didn't know there was a selection process for scholarships. I thought you just had to complete the thesis."
    
#     hide lindapose22
#     show lindasmile
    
#     lin "Haha, you're so naive. Of course there's a selection process. Professors can't supervise just anyone."
    
#     name "I see, it's going to be competitive."
    
#     lin "That's why the sooner you choose your topic, the better your chances of being selected."
    
#     name "You're off to a good start then."
    
#     hide lindasmile
#     show lindalooksup3
    
#     lin "Yeah, pretty much. Honestly, I don't think the others in my class have much of a chance."
    
#     name "Wow, that's harsh."
    
#     lin "Yeah, I know, but it's true."
    
#     name "I guess if you worked for it you deserve it."
    
#     lin "Exactly."
    
#     name "Well, I'll let you get back to work."
    
    
    
#     hide lindalooksup3
#     show lindadesire
    
#     lin "Hey! If you want, I could help you with your thesis."
    
#     name "What? Really? I wasn't expecting that from you."
    
#     lin "Uh, why not."
    
#     name "Are you sure? You seem pretty busy."
    
#     hide lindadesire
#     show lindapose21
    
#     lin "I mean, if I have time, I will."

#     lin "Anyway, I have to go. See you."
    
#     "She quickly packs up her things and awkwardly heads for the exit. She seemed nervous, maybe she needed to go to the bathroom." 
#     "Anyway, it was nice of her to offer to help. She seemed serious."
#     "With a friend like her, I should be able to handle this thesis."



#     call marion_1st_meet

# label marion_1st_meet:
#     define mar = Character('Mrs.Gillsberg', color="#e6a7ff") 
# default marion_1st_conv_done = False

# label marion_1st_meet:

#     scene officeteacher
#     "I enter the building and walk through the hallways."
#     "These offices look new. It seems they had been built recently on top of some old construction."
#     "I stop in front of a large glass window. This must be the place."

#     scene officeteacher2
#     "This must be her."

#     "I knock on the door."

#     mar "Come in!"

#     "I step into a spacious office. The large window faces the campus, filling the room with afternoon light. This professor must be important."

#     scene officeteachere0

#     name "Hello, Mrs. Gillberg. I am a new student here. I just started this year."
#     name "I'm looking for a professor to supervise my thesis. Could you help me with that?"

#     scene officeteacher3

#     mar "Well, you're catching me off guard. I already have a lot of students, and I make sure all of them are well-guided."

#     name "I understand."

#     scene officeteacher7
#     mar "Too many students wait until the last minute to find a supervisor."
#     mar "Every year, about ten students fall behind because of this."
#     mar "Anyway."
#     mar "What were you doing before you came here?"

#     scene officeteachere1

#     name "I attended a university in my hometown where I pursued anthropology courses."
#     name "Now, I'm interested in writing my thesis on the history of photography."
#     name "I want to focus on the representation of women in 20th-century photography."
#     name "I know it’s not a very original topic, but I was hoping to refine it with a professor's help."

#     scene officeteacher8
#     mar "At least you have an idea of your topic."
#     mar "Not everyone is at that stage."
#     mar "The representation of women, I see."
#     mar "Do you live on campus?"

#     name "No, I have my own apartment in the east district."

#     mar "That's good. You're independent."
#     mar "Well, I hope you're motivated."

#     name "I am!"

#     scene officeteachere02

#     mar "Do you keep up with your assignments?"

#     name "Yes, of course!"

#     mar "Are you comfortable with your writing skills?"

#     name "I'm good with writing."

#     mar "What about administrative procedures? Replying to emails promptly?"

#     name "Oh yeah, sure."

#     scene officeteacher9

#     mar "Oh, so you're the perfect little student, aren't you?"
#     mar "..."

#     scene officeteachere04
#     name "I’m not sure about that... but I want to do things well."
#     name "It’s just that, being new here, I don’t know the professors very well."
#     name "And I don't want to choose someone who isn’t a good fit for me."
#     name "Someone recommended you to me. I also looked into your work and found it very interesting. I heard you are an excellent professor."

#     scene officeteacher10
#     "She sighs deeply."

#     mar "..."
#     mar "That’s nice to hear. Not everyone at this university would agree."
#     mar "..."
#     mar "Well, you’ve caught me a bit off guard. I just moved into this new office. Give me some time to get organized."
#     mar "You’ll need to be dedicated, okay? If I take you on, it's an exception, and I'll push you to do your best."

#     name "Are you saying you’ll be my supervisor?"

#     scene officeteacher11
#     mar "I’ll see what I can do. I'll need to shift things around with my current students to fit in one or two more thesis defenses this year."
#     mar "I’ll let you know."

#     name "That’s great! Thank you so much, Mrs. Gillberg."

#     mar "You’re welcome."
#     mar "By the way, what's your name? I need to remember it in this maze."

#     name "Oh, right. I'm [name] Smith."

#     if gender == "male":
#         mar "Got it. See you soon, Mr. Smith. Good luck."
#     elif gender == "fem":
#         mar "Got it. See you soon, Mrs. Smith. Good luck."
#     name "Thank you, see you soon!"

#     scene officeteachere07

#     "I mumble to myself."
#     "Fuck yeah!"

#     mar "Can you close the door on your way out? Thanks."

#     name "Oh sure, thanks again."

#     $ marion_1st_conv_done = True

    
#     call raver_date_1

# label raver_date_1:
#     # Your existing code here
#     call elisedate

# label elisedate:
#     # Your existing code here
#     call elisesachadate

# label elisesachadate:
#     # Your existing code here
#     call emmadate

# label emmadate:
#     # Your existing code here
#     call cigarettebreak

# label cigarettebreak:
#     # Your existing code here
#     call cigbreak1

# label cigbreak1:
#     # Your existing code here
#     call sacha_sarah_date

# label sacha_sarah_date:
#     # Your existing code here
#     call linda2

# label linda2:
#     # Your existing code here
#     call linda3

# label linda3:
#     # Your existing code here
#     call lindakiss

# label lindakiss:
#     # Your existing code here
#     call lindasubmit

# label lindasubmit:
#     # Your existing code here
#     call linda4

# label linda4:
#     # Your existing code here
#     call sarahdate1

# label sarahdate1:
#     # Your existing code here
#     call sarahdate2

# label sarahdate2:
#     # Your existing code here
#     call sarahdate3

# label sarahdate3:
#     # Your existing code here
#     call sarahdate4

# label sarahdate4:
#     # Your existing code here
#     call sarahsagain

# label sarahsagain:
#     # Your existing code here
#     call camillelovescene

# label camillelovescene:
#     # Your existing code here
#     call work_here

# label work_here:
#     # Your existing code here
#     call sarahdatecafe2

# label sarahdatecafe2:
#     # Your existing code here
#     call sarahelisecafe

# label sarahelisecafe:
#     # Your existing code here
#     return