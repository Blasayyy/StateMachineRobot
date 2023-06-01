# Projet Robot Rapport
## Christophe Auclair, Matei Pelletier, Frédéric Châteauneuf

Nous croyons que notre projet répond à environ 85% de ce qui a été demandé. Nous avons manqué de temps pour implémenter certaines fonctionnalités tels les couleurs des yeux et les blinkers et les yeux ne se ferment pas après avoir quitté une des tâches mais plutôt s’arrêtent au milieu de leur cycle. 

Pour ce qui est de l’infrastructure des éléments demandés, nous croyons que nous avons bien respecter l’utilisation de la librairie. 

Classe représentant le robot : 
-	Validation de l’intégrité du robot : 
En allumant le robot, nous passons par l’état robot_instantiation, qui a un in state action qui vérifie si le robot est instancié. Si l’instanciation est valide, nous passons à l’état robot_integrity par la transition correspondante. Sinon, nous passons par l’autre transition pour aller vers l’état instantiation_failed, qui elle en suite sort du programme. Dans robot_integrity nous avons un in state action qui détermine si le robot est intègre (qui return tout le temps vrai car nous ne pouvons pas vraiment vérifier). L’état transitionne alors à integrity_succeeded.
-	Gestion de la télécommande :
Nous instancions d’abord la télécommande dans les classes ou elle est nécessaire. Ensuite, nous avons plusieurs états où le in state action est de recevoir l’input, et ensuite nous assignons le custom value de l’état a ce résultat.
-	Gestion du télémètre et de son servo moteur
Nous initialisons le télémètre dans la classe Robot, et en suite nous l’utilisons dans les in state action de la tache 2 pour assigner la valeur au custom value de ces états. Ces états déclenchent alors les conditions pour changer d’état.
-	Gestion des moteurs
Nous avons utilisé les moteurs dans plusieurs états des tâches 1 et 2 dans le in state action.
-	Gestion de la couleur pour les yeux
Nous avons malheureusement manqué de temps pour faire cette fonctionnalité

Structure générale du logiciel :
-	Infrastructure générale du logicielle :
Nous utilisons la classe C64Proj qui est un state machine. Cette classe gère les états les changements d’états liés au robot. Elle a un initial state qui est robot_insantiation_state, qui entraîne alors les autres états jusqu’à temps que le logiciel arrive au home state. Quand les tâches 1 ou 2 sont débutées, elles partent leurs propres state machines qui gère leurs comportements respectifs. 
-	Capacite modulaire d’insertion d’une nouvelle tâche
On peut facilement insérer une nouvelle tâche dans notre logiciel. On doit simplement rajouter l’état de cette tâche, les conditions et transitions nécessaires pour la déclencher. Ensuite, il reste juste à rajouter des actions a cet état.


