Résumé : Français

L’objectif que nous nous sommes fixé est de pouvoir observer et modéliser la propagation d’une température qui évolue grâce à une source de chaleur et une volume d’air plus froid. 
La majorité de notre temps sur ce projet a été consacrée à la recherche des formules, dans un premier temps, puis à la programmation. Pour réellement constater la validité de notre hypothèse et atteindre notre objectif, plusieurs tests ont été réalisés à la fin de notre projet. 
Les résultats importants que l’on a pu constater sont ceux de l’augmentation de température des composants de l’ordinateur, qui croît de manière exponentielle et qui atteint une température critique, sans puis avec une ventilation, la matrice qui modélise la propagation de chaleur dans la salle mais aussi l’évolution de la température moyenne de la salle, avec et sans ventilation, qui marque la fin de notre étude.

Introduction

Notre équipe de développement est composée de Gabin MAZUE, Émilien LENDROIT, Shanita NGUYEN et Romane DELABORDE. Après avoir discuté des différents choix possibles pour notre projet final, nous nous sommes rapidement mis d'accord sur une étude thermique.
On cherche dans un premier temps à connaître et à comprendre l'évolution de la température d'une salle comportant un ordinateur en fonctionnement, à l'aide de phénomènes thermodynamiques précis, en particulier la convection et la conduction. Nous avons donc supposé un nombre important de faits, étant donné l'étude complexe de la thermodynamique, ainsi que notre niveau d'étude relativement insuffisant.
Tout d'abord, notre modélisation se base sur une salle de dimensions finies ( 5 m de large, 10 m de long, 3 m de hauteur) et dont la température au démarrage est posée et répartie de façon homogène dans toute la pièce. L’ordinateur établi dans notre premier modèle […]. Par soucis de simplification, les ordinateurs, pris en compte dans la suite de notre projet, seront tous de mêmes modèles. De plus, la salle ne possède ni fenêtres, ni portes, ni être humains afin de négliger au maximum les transferts thermiques avec l'extérieur. D'autre part, les effets de l'humidité dans l'air sont négligés et la salle étudiée se situe au niveau de la mer puisque nous avons posé une valeur précise de la chaleur massique de l'air, qui dépend de l'altitude. Enfin, le transfert de chaleur par rayonnement a aussi été négligé, étant nettement négligeable fac à la convection et la conduction.
Quant à l'ordinateur, nous admettons que sa conductivité thermique est constante, ce qui signifie que nous l'assimilons à un unique bloc d'acier. Notre postulat désormais posé, on peut se demander de quelle façon évolue la température dans une salle informatique et comment optimiser le placement de climatiseurs au sein de cette pièce.

Les solutions envisageables sont restreintes étant donné le postulat posé précédemment, ainsi nous avons décidé de nous consacrer principalement à l’étude intérieure de l’ordinateur avant de s’intéresser à la salle informatique dans sa globalité. D’autre part, nous nous demandons si la ventilation serait plus efficace si celle-ci se situait à proximité de la source de chaleur. Notre modélisation peut être en mesure de répondre à cette interrogation et ainsi montrer l’importance de la position des climatiseurs.



Présentation Thématique

Les notions fondamentales que nous avons abordées afin de pouvoir modéliser notre étude de l'évolution de la température au sein d'une salle informatique sont principalement en lien avec la thermodynamique. En effet, pour le calcul de l'homogénéisation de la température interne du terminal par conduction, nous avons utilisé la formule suivante () trouvée dans le manuel, intitulé ‘Introduction aux transferts thermiques’,  à la bibliothèque des licences. Étant donné que S la surface de contact, m la masse du composant, Cp la chaleur massique et h le coefficient d'échange dont la formule est ci-jointe (), sont des valeurs connues et constantes pour chaque composant, il reste à trouver la température de chaque composant en fonction du temps.
Cette formule a été obtenue grâce à l'exploitation des annales de physique du premier semestre se trouvant à la fin du livret de travaux dirigés {}. D'autre part, la  formule de convection liée à l'intérieur de l'ordinateur est une moyenne volumique des différents composants impliqués.
Concernant la modélisation de la salle, nous avons décidé de négliger les transferts thermiques liés à la conduction au niveau des cases en contact avec le terminal, car ceux-ci sont négligeables par rapport aux mouvements de convection. 

Résumé : Anglais

Our aim for this project is to be able to watch and model a thermal spread which evolve because of a heat source and a colder air volume. 
A majority of our time on this project was dedicated to our researches for the formulas, first, and then to our computer programs. To truly see the validity of our hypothesis and reach our goal, many tries were made, at the end of our project.
The main results that we could have here were the temperature increase of the various components from the computer, which exponentially rise and get at a critical temperature, without then with an air conditioner, the matrix which model the heat spread in the room but also the mean temperature evolution, with and without an air conditioner, which mark the end of our project.
