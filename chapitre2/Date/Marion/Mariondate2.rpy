label Marion_date2:
    scene secondfloor
    "I arrive on the second floor of the university."
    
    scene secondfloorelevator
    "I take the elevator to the last floor."
    
    scene marion-corridor
    ""
    scene upbuilding
    ""
    scene marion-office
    ""
    "Mrs.Gillsberg doesn't seem to be there.."
    "Peut être qu'elle est occupée ailleurs."
    "Je repasserais plus tard."
    scene upbuilding
    ""
    scene secondfloor
    "Soudain j'aperçois Mme Gillsberg qui arrive dans le couloir."
    "Elle me voit et s'approche de moi."
    mar "Oh, hello!"

    mar "I was just thinking about you."
    mar "Je dois aller à une réunion et je suis déja en retard, c'est terrible"
    mar "j'ai vus que vous m'avez envoyé votre article mais je n'ai pas eu le temps de regarder!"
    mar "On se voit plus tard alors.."
    name "Ok pas de problème"
    mar "Peut tu me rendre un service?"
    name "heu oui bien sûr"
    mar "j'ai oublié un dossier dans mon bureau et je dois l'avoir avec moi pour la réunion"
    mar "Tu penses que tu peux aller le chercher?"
    mar "C'est des feuilles blanches agraffé ensemble."
    mar "mon bureau est ouvert il te suffit d'entrer de les prendre."
    name "heuu.. ok.."
    mar "Merci, je serais en salle 530"
    mar "rejoins moi là bas"
    "Avant que je puisses lui demander plus de précision, elle disparait dans le couloir"
    "..."
    "Je devrais pouvoir trouver"
    scene elevator3
    ""
    scene upbuilding
    ""
    scene marion-corridor 
    ""
    scene marion-office
    ""
    scene marion-papers
    "J'apperçois un dossier sur le bureau."
    "Je le prends rapidement."
    scene runninguniveric
    "Je me dépêche de rejoindre Mme Gillsberg."
    scene marion-corridor
    ""
    scene secondfloorscreen
    ""
    scene black
    "Je la retrouve dans une salle de réunion."
    scene mariondate_almameet3
    mar "Oh, you found it! Thank you so much."
    name "No problem."
    mar "see you later!"
    "Elle refermes la portes"
    jump secondfloor_corridor
