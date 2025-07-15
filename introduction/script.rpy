define E = Character('Player', color="#c8c8ff")
define sac = Character('Sacha', color="#b2c73d")
define sar = Character('Sarah', color="#4f5da0")
define mil = Character('Mila', color="#66668f")
define lis = Character('Lisa', color="#ff7f7f")
define oli = Character('Olivia', color="#0d695d")
define elo = Character('Elodie', color="#03312a")
define est = Character('Estelle', color="#8b5ac2ff")
define jen = Character('Jenny', color="#190b3fff")
define isa = Character('Isabelle', color="#ff7f7f")
define tra = Character('Tracy', color="#c4afba")
define mela = Character('Melany', color="#8dcee7")
define bru = Character('Bruno', color="#457409")
define jeni = Character('Jennifer', color="#ff7f7f")
define axel = Character('Axel', color="#868484")
define seb = Character('Sebastian', color="#ffffff")
define amy = Character('Amy', color="#ff7f7f")

init python:

    renpy.music.register_channel('coffee_ambiance', "music")
    class Item:
        def __init__(self, name, image):
            self.name = name
            self.image = image


# NVL characters are used for the phone texting

define n_nvl = Character("Nighten", kind=nvl, image="nighten", callback=Phone_SendSound)
define m_nvl = Character("Marie", kind=nvl, image="marie", callback=Phone_ReceiveSound)
define h_nvl = Character("Hugo", kind=nvl, image="hugo", callback=Phone_ReceiveSound)
define l_nvl = Character("Linda", kind=nvl, image="linda", callback=Phone_ReceiveSound)
define em_nvl = Character("Emma", kind=nvl, image="emma", callback=Phone_ReceiveSound)
define c_nvl = Character ("Chloe", kind=nvl, image="chloe", callback=Phone_ReceiveSound)
define s_nvl = Character ("Sarah", kind=nvl, image="sarah", callback=Phone_ReceiveSound)
define cl_nvl = Character ("Clara", kind=nvl, image="clara", callback=Phone_ReceiveSound)
define el_nvl = Character ("Elise", kind=nvl, image="elise", callback=Phone_ReceiveSound)
define elo_nvl = Character ("Elodie", kind=nvl, callback=Phone_ReceiveSound)
define cam_nvl = Character ("Camille", kind=nvl, image="camille", callback=Phone_ReceiveSound)



define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

# /// BLur shader
transform blur(amount=3.0):
    shader "custom.blur"
    u_blur amount

image elisevideo = safe_movie("output_video.ogv", "video_channel", "images/black.png", fit=True)

image sarahvideo = Movie(play="sarahericvid.ogv",channel="video_channel", fit=True)


init:
    $ screen_center = Position(xpos=0.5, ypos=0.5)
    $ screen_left = Position(xpos=0.1, ypos=0.5)
    $ screen_right = Position(xpos=0.9, ypos=0.5)


label start:
    define money = 2000
    define groceries = 2

    $ player_inventory = []
    $ laura_repeat = False
    default classe = False
    default day = 0
    default gender = "male"
    default rentdue_meet_count = 0
    default quickbed = False

    # //Linda variables
    default linda_1st_conv_done = False
    default linda_4th_conv_done = False
    default linda_2nd_conv_done = False
    default linda_conv_done = False
    default linda_invitation_sent = False
    default linda_relation_status_text = "Linda seems to enjoy hanging out at the university library, I should find her there"

    # //Sarah variables
    default sarah_tvdate_done = False
    default sarah_homedate_done = False
    default sarahcafe_conv1_done = False
    default sarah_conv_done = False
    default sarah_pissed = False
    default sarah_relation_exist = False
    default sarah_pissedconv_done = False
    default sacha_sarah_date_done = False
    default sarah_count = 0
    default day_until_new_date = 0
    default sarah_cafe = False
    default sarahcafe_conv2_done = False
    default sarahtexto_count = 0
    default sarah_sdate_done = False
    default sarah_sagain_done = False
    default sarahsproposalrefused = False
    default sarah_relation_status_text = "I hope to meet Sarah more often in the corridor in the coming days" 

    # //Sacha variables
    default laura_count = 0
    default sacha_count = 0
    default sacha_conv_done = False
    
    # //Other variables
    default cig_break_count = 0
    default class_done = False
    default day_not_over = False
    default classdate_count = 0
   

#    //Barmaid variables
    default jobaskedlaura_done = False


    # //Emma variables
    default emma_date_started = False
    default classdateemma_count = 0
    default textoemma_send = False
    default emma_date_done = False
    default emma_relation_status_text = "I should try to sit next to her in class to get to know her"

    # // Raver variables
    default raver_date_done = False
    default raver_not_over = False
    default raver_first_conv_done = False
    default raver_text_done = False
    default chloe_relation_status_text = "I should send her a text tonight to see if she's free"

    # //Elise variables
    default elise_cafe = False
    default elise_cafe_conv_done = False
    default sarah_elise_cafe = False
    default sarah_elise_cafedate_done = False
    default elise_sdate_done = False
    default elise_sagain_done = False
    default elise_relation_status_text = "               "

    # // Lisa variables
    default lisa_count = 0
    default lisa_conv_done = False

    # // Boss variables
    $ boss_conv_done = False
    $ boss_textconv_done = False

    # // Camille variables
    default classdatecamille_count = 0
    default camillelove_count = 0
    default camillespank = False
    default camillespank2 = False
    default camillespank3 = False
    default camille_sdate_done = False 
    default camille_relation_status_text = "I should try to sit next to her in class to get to know her"
    default camille_moneycheck_passed = False
    default camille_coffeedate_activated = False
    default camilletext1_done = False
    default camilletext2_done = False
    default camille_shomedate_done = False


    # // Mila variables
    default mila_count = 0
    default mila_conv_done = False

    # // Estelle variables
    default estelle_spankconv_done = False 
    default estelle_firstconv_done = False
    default estelle_emmaconv_done = False

    # //Party variables
    

    default stacybourreconv_done = False
    default estellebourreconv_done = False
    default tracybourreconv_done = False

    default stacymelanieconv_count = 0
    default stacydate_activated = False

    default isabelleconv_count = 0

    default estellepartyconv_count = 0

    default trioconv_count = 0
    default trio_musicasked = False

    default zoeyaxelconv_count = 0
    default zoeyconv_count = 0
    default zoeyasketfor_music = False
    default zoey_vestibul_asked = False
    default drink_count = 0

    default sebastianconv_count = 0
    default sebastianjen_date_started = False
    default sebastianjen_date_done = False
    $ key = Item("key", "cupoftea.png")

    scene disclaimer with dissolve
    pause
    scene earlyaccess with dissolve
    pause
    scene black with dissolve
    "whats your name?"
    $ name = renpy.input("Enter your name")
    $ name = name.strip()

    if not name:
        $ name = "Jess"
    "Your name is [name]."
    "You are a 23-year-old student who is moving to a new city to start a thesis."

    
   
    
    jump camilleuni_date


    scene train
    with dissolve
    "It's been almost 3 hours since I've been on the train."
    "I open my eyes to a landscape passing by outside the train window."
    "In 20 minutes, I'll arrive at the central station."

    "A new chapter of my life opens."

    "At least, that's what I thought when I signed up for a thesis in this city."
    "I'm not sure what to expect, but it can't be worse than my hometown."
    "I feel like my life was on pause until now."
    "As I'm lost in my thoughts, the train finally arrives at the station."

    scene railway with dissolve

    "Everyone rushes onto the platform. I follow the flow of people without knowing exactly where I'm going."
    "I end up entering the subway station at the train station."

    "I buy a ticket and get on the subway that takes me to my neighborhood."

    scene subwaybis with dissolve

    "I hope I'll quickly find a solution to make money."
    "Even though I have enough to get by for a while, it won't last forever."

    "I'll have to find a job at some point."

    "I'd prefer to be able to focus on my studies."
    "I read somewhere that those who have a job alongside their studies are 3 times more likely to drop out."
    "It makes sense if you think about it."

    "I need to find some good opportunities."

    "There must be ways to make money quickly in this city."
    "I need to make contacts."

    "I get a message from my girlfriend."

    m_nvl "Hey, did you arrive safely?"
    n_nvl "I'm on the subway."
    m_nvl "Good, tell me when you arrive."
    n_nvl "I will."

    "She's supposed to move here next year."
    "I hope everything goes well until then."
    "Things can change so much in a year."
    nvl clear

    "I get off at my stop."

    scene suburb

    "Hmm, I should have taken a map of the city with me."
    "I'm not sure if I recognize the place."
    "I check my phone to see where I am."
    "Fuck... I got off at the wrong station."
    "Oh well, I'll just walk."
    "I'll figure it out with my phone."
    
    scene suburb2

    "I start walking as the night falls."
    "The streets are pretty quiet around here."
    "What do people do to make money here?"
    "Maybe I could be a delivery person."
    "It shouldn't be too complicated."
    "Plus, I could probably have flexible hours."

    "After a 10-minute walk, I finally reach my neighborhood."

    scene arriving2

    "Finally, I make it to my place."
    "I'm exhausted."
    "I'll go to bed early tonight."

    scene stairs2
    "It's a small studio, but it's enough for me."

    scene dark
    "I need to turn the light on."
    scene light

    "I am so tired."

    scene ericsleep

    scene black
    "I pass out on the couch."

    scene ericawake
    "I wake up still dressed."
    "Shit, I have to go to the university."
    if gender == "fem":
        scene characterdesign
        pause 2.0
        window hide
        pause
    show screen homescreen3

    call screen homescreen3
