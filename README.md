#Introduction 

Notre application porte sur le sujet des présidentielles 2022 et nous avons utilisé le site Twitter pour notre étude. Nous avons analysé les tweets des principaux candidats (likes et retweet), mais aussi les principaux sujets que l’on retrouve chez les utilisateurs de twitter et le sentiment que l’on perçoit dans un twitter (positif, négatif, neutre).

#Lancement du projet :
Lancer dans un terminal de commande : 

pip install -r requirements.txt

lancer un serveur mongod

flask run

Puis dirigez vous sur localhost:5000/
Il faut aussi un compte twitter developpeur, dont les informations sont à stocker dans twitter_credentials.py. Des informations sont déja disponibles dans notre fichier.



#Scrapping de donnée :

Nous avons implémenté plusieurs fonctionnalité via l’api Tweepy de twitter :

-Une analyse de sentiment sur un mot clé donnée. Vous pouvez entrer un mot clé/hashtags et un nombre de tweets à analyser et l’app ressort une visualisation du nombre de tweet positif, négatif et neutre afin d’avoir un ressenti global rapide sur un sujet donné.
-Un worldcloud, sur la même recherche que la fonction précédente l’app va ressortir une image avec les mot clés/thèmes principaux qui reviennent le plus selon le hashtag entré
-Une analyse de la moyenne de likes et de rt des principaux candidats (liste fixée par rapport au dernier sondage à la présidentielle). L’analyse est fixé sur les 100 derniers tweets mais ce paramètre peut être changé
-une recherche des tweets les plus populaires suivant un hashtags

#librairies utilisées :





#Fichiers principaux : 

app.py : Application flask où l’on donne les routes pour nos templates 

rt_like.py : analyse les 100 tweets des principaux candidats aux élections présidentielles, et donne une moyenne des likes et retweet.

sentiment.py : donne le sentiment d’une liste de tweet en donnant un hashtag, donne aussi un nuage de mots qui sont le plus représenté dans les tweet.

search_hashtags.py: 

Le dossier templates : regroupe tous les templates du site.

#User Guide : 

Notre site est réparti en 4 pages html : 

Accueil : Elle permet d’accéder aux différentes pages du site, chacune représente une méthode de scraping et d’analyse différentes.

Retweet et likes : Donne un graphique des 100 derniers tweets d’un candidat à l’élection présidentielle et donne la moyenne des likes et retweets.

Hashtag : Donne les tweets les plus retweeter parmis le hashtag et le nombre de tweet choisi.

Sentiments : Il faut entrer un Hashtag et le nombre de tweets que l'on veut analyser, cela nous donne un pie chart et un barPlot sur la répartition des tweets positif, négatif ou neutre. Mais aussi un nuage de mots les plus représentés dans les tweets 
