import random


def choisir_message(blagues):
    return random.choice(blagues)

# Liste des messages
blagues = [
    "Quelle mamie fait peur aux voleurs ? Mamie Traillette.",
    "Pourquoi est-ce si difficile de conduire dans le Nord ? Parce que les voitures n’arrêtent pas de caler (Pas-de-Calais).",
    "Pourquoi est-ce qu'on dit que les bretons sont tous frères et sœurs ? Parce qu’ils n’ont Quimper.",
    "Pourquoi faut-il mettre tous les crocos en prison ? Parce que les crocos dealent.",
    "Comment fait-on pour allumer un barbecue breton ? On utilise des breizh.",
    "Pourquoi dit-on que les poissons travaillent illégalement ? Parce qu’ils n’ont pas de FISH de paie.",
    "Quel fruit est assez fort pour couper des arbres ? Le citron.",
    "Que fait un cendrier devant un ascenseur ? Il veut des cendres.",
    "Que dit une imprimante dans l'eau ? J’ai papier.",
    "Pourquoi les girafes n'existent pas ? Parce que c’est un coup monté.",
    "Comment appelle-t-on un jeudi vraiment nul ? Une trajeudi.",
    "Que fait un geek quand il a peur ? Il URL.",
    "Quel est le carburant le plus détendu ? Le kérozen.",
    "Quel est le sport préféré des insectes ? Le cricket.",
    "Pourquoi est-ce que les éoliennes n'ont pas de copain ? Parce qu’elles se prennent toujours des vents.",
    "Pourquoi les cordonniers sont-ils curieux ? Parce qu’ils se mêlent de tout (semelle).",
    "Que dit le citron quand il braque une banque ? « Pas un zeste, ze suis pressé ! »",
    "Comment appelle-t-on une manifestation d'aveugles ? Un festival de cannes.",
    "Que risque-t-on à lancer de l'ail sur un mur ? Le retour du jet d’ail.",
    "Quelle est la fée la plus paresseuse ? La fée Néante.",
    "Que dit une noisette qui tombe à l'eau ? « Au secours, je me noix ! »",
    "Tu connais l'histoire de l'armoire ? Elle est pas commode.",
    "Tu connais l'histoire de la feuille de papier ? Elle déchire !",
    "Comment appelle-t-on un chat tout-terrain ? Un cat cat.",
    "Quelle est l'info la plus tirée par les cheveux ? Il n’y a pas de chauve à Bastia, mais à Calvi si.",
    "Que disaient les apôtres à Jésus quand il racontait une blague de ce top ? « C’est naze, arrête. »",
    "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent toujours dans le bateau.",
    "Pourquoi les poissons détestent l'ordinateur ? Parce qu'ils ont peur du net.",
    "Quel est le comble pour un électricien ? De ne pas être au courant.",
    "Pourquoi les moutons ne racontent jamais de blagues ? Parce qu'ils ont peur de se faire tondre.",
    "Quel est le comble pour un électricien ? De ne pas être au courant.",
    "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent toujours dans le bateau.",
    "Pourquoi les poissons détestent l'ordinateur ? Parce qu'ils ont peur du net.",
    "Quel est le comble pour un électricien ? De ne pas être au courant.",
    "Pourquoi les moutons ne racontent jamais de blagues ? Parce qu'ils ont peur de se faire tondre."
]

if __name__ == "__main__":
    message_choisi = choisir_message(blagues)


    print(message_choisi)