define mar = Character('Mrs.Gillsberg', color="#e6a7ff") 
default marion_1st_conv_done = False

label marion_1st_meet:

    scene officeteacher
    "I enter the building and walk through the hallways."
    "These offices look new. It seems they had been built recently on top of some old construction."
    "I stop in front of a large glass window. This must be the place."

    scene officeteacher2
    "This must be her."

    "I knock on the door."

    mar "Come in!"

    "I step into a spacious office. The large window faces the campus, filling the room with afternoon light. This professor must be important."

    scene officeteachere0

    name "Hello, Mrs. Gillberg. I am a new student here. I just started this year."
    name "I'm looking for a professor to supervise my thesis. Could you help me with that?"

    scene officeteacher3

    mar "Well, you're catching me off guard. I already have a lot of students, and I make sure all of them are well-guided."

    name "I understand."

    scene officeteacher7
    mar "Too many students wait until the last minute to find a supervisor."
    mar "Every year, about ten students fall behind because of this."
    mar "Anyway."
    mar "What were you doing before you came here?"

    scene officeteachere1

    name "I attended a university in my hometown where I pursued anthropology courses."
    name "Now, I'm interested in writing my thesis on the history of photography."
    name "I want to focus on the representation of women in 20th-century photography."
    name "I know it’s not a very original topic, but I was hoping to refine it with a professor's help."

    scene officeteacher8
    mar "At least you have an idea of your topic."
    mar "Not everyone is at that stage."
    mar "The representation of women, I see."
    mar "Do you live on campus?"

    name "No, I have my own apartment in the east district."

    mar "That's good. You're independent."
    mar "Well, I hope you're motivated."

    name "I am!"

    scene officeteachere02

    mar "Do you keep up with your assignments?"

    name "Yes, of course!"

    mar "Are you comfortable with your writing skills?"

    name "I'm good with writing."

    mar "What about administrative procedures? Replying to emails promptly?"

    name "Oh yeah, sure."

    scene officeteacher9

    mar "Oh, so you're the perfect little student, aren't you?"
    mar "..."

    scene officeteachere04
    name "I’m not sure about that... but I want to do things well."
    name "It’s just that, being new here, I don’t know the professors very well."
    name "And I don't want to choose someone who isn’t a good fit for me."
    name "Someone recommended you to me. I also looked into your work and found it very interesting. I heard you are an excellent professor."

    scene officeteacher10
    "She sighs deeply."

    mar "..."
    mar "That’s nice to hear. Not everyone at this university would agree."
    mar "..."
    mar "Well, you’ve caught me a bit off guard. I just moved into this new office. Give me some time to get organized."
    mar "You’ll need to be dedicated, okay? If I take you on, it's an exception, and I'll push you to do your best."

    name "Are you saying you’ll be my supervisor?"

    scene officeteacher11
    mar "I’ll see what I can do. I'll need to shift things around with my current students to fit in one or two more thesis defenses this year."
    mar "I’ll let you know."

    name "That’s great! Thank you so much, Mrs. Gillberg."

    mar "You’re welcome."
    mar "By the way, what's your name? I need to remember it in this maze."

    name "Oh, right. I'm [name] Smith."

    if gender == "male":
        mar "Got it. See you soon, Mr. Smith. Good luck."
    elif gender == "fem":
        mar "Got it. See you soon, Mrs. Smith. Good luck."
    name "Thank you, see you soon!"

    scene yesposeeric

    "I mumble to myself."
    "Fuck yeah!"

    mar "Can you close the door on your way out? Thanks."

    name "Oh sure, thanks again."

    $ marion_1st_conv_done = True

    jump gardenuni_start