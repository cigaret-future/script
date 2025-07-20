label workplace:
    scene upview
    "I arrive at a coffee shop, people are lining up to order, and baristas are busy behind the counter."
    "It's a slightly different atmosphere from the café near my house, but it doesn't seem too bad."
    "I try to spot the boss, but I don't see her."
    "I should ask at the counter if she's here."
    "I approach the counter."
    scene upviewblur with dissolve
    show jenny with dissolve
    "test"
    jen "Hey there."
    name "Hi, I'm looking for the boss."
    jen "That's me, I'm Jenny."
    name "Oh, okay, nice to meet you. I am [name]."
    jen ""
    show jenny3 with dissolve
    hide jenny with dissolve
    
    jen "Nah, I'm just kidding. Why do you want to see the boss?"
    name "She offered me a job here."
    jen "Ah, okay, I'll let her know you're here."
    "Jenny walks away and heads towards the back of the café."
    "I wait for a few minutes, and she comes back."
    jen "She's coming. You can wait on the side."
    name "Thanks."
    hide jenny3 with dissolve
    scene upview with dissolve
    "I stand near the counter on the side."
    "It's not exactly what I imagined, but it should be fine."
    "After a few minutes, the boss comes out of a room in the back and approaches me, staring at me."
    show bossview
    elo "Hey, are you the new recruit?"
    name "Hello, I'm ready to work. When do I start?"
    elo "Perfect, you can start right now if you want."
    elo "That way, you can see if it suits you."
    name "Don't I need to sign a contract first?"
    elo "Yes, but this will allow you to get to know your colleagues."
    name "Well... okay, I don't mind."
    elo "Great, I'll get you an outfit."
    elo "You'll see, it's very dynamic here."
    elo "I'll be right back."
    "She walks away and comes back with a t-shirt and pants."
    elo "Here, put this on."
    name "Here?"
    elo "No, come to the storage room."
    scene changing2
    "She takes me to a room at the back of the café."
    "She shows me a room with boxes and clothes."
    "I put on the uniform and leave the room."
    elo "Great, it suits you very well."
    name "Cool."
    scene upviewblur with dissolve
    "I head to the counter and start watching Jenny work."
    
    "After a few hours, I start to get the hang of it."
    show jenny with dissolve
    jen "Do you want me to show you how to make a coffee?"
    name "Okay..."
    jen "Look, you just put the coffee here,"
    jen "then press here, and you're good to go."
    "The day goes by slowly."
    jen "Okay, my shift is over."
    jen "I think you can leave now."
    name "Okay est ce que je dois écrire mon nom quelque part ?"
    jen ""
    "I leave the coffee shop with Jenny, and we part ways."
    $ money += 200
    show text "+200$" at Move((0.5, 0.6), (0.5, 0.5), 10.0)
    hide text with dissolve
    jump map3


label workplace2:
    
        scene upview
        "A new day begins at the café. The smell of freshly ground coffee already floats in the air as the first customers walk through the door."
        "Sunbeams stream through the window, lighting up the still-empty tables. I quickly greet my colleagues, ready to tackle the morning shift."
        "The atmosphere is calm, but I know it won't last. Soon, the line will grow and the orders will start coming in."
        "I take a deep breath, put on my apron, and get ready to face another ordinary day of work behind the counter."