### Etude de l'évolution de la température dans une salle informatique

Notre sujet se base sur l'évolution de la température d'une pièce contenant des ordinateurs.
La première chose à faire est de pouvoir calculer la chaleur produite par un ordinateur allumé. Pour cela, il faut étudier chaque
composant individuellement. Nous considèrerons l'ordinateur comme un pavé droit en acier ne régulant sa température que par 
conduction et par ventilation. Cela nous permettra de simplifier des calculs trop complexes.

Il faut pouvoir calculer l'homogénéisation de l'air à l'intérieur de l'ordinateur en comptant que chaque composant a une 
température constante différente, qui modifie la température interne de l'ordinateur par conduction et certains composants précis
par ventilation.

Pour la salle, on devra considérer la conduction procurée par l'ordinateur et la convection créée par la ventilation vers l'extèrieur de celui-ci pour un volume d'air qu'on choisira pour notre modèle, contenant cette ordinateur. Pour la reste de la salle, on effectuera des calculs pour des transferts de températurs par convection. Enfin, on introduira la ventilation grâce au phénomène de convection forcée.

### Semaine du 18 février 2019

Suite à notre choix du sujet la semaine précédente, nous avons choisi de nous réunir à la Bibliothèque des Licences pour débuter notre projet se basant sur l'évolution de la température d'une pièce contenant des ordinateurs. Nous avons tout d'abord mis en commun nos recherches sur le sujet : Emilien s'est chargé de prendre les dimensions de son ordinateur qui nous serviront de base pour un modèle réaliste. Gabin a, quant à lui, commencé à programmer celui-ci grâce aux données d'Émilien. Shanita a, elle, entamé des recherches pour les formules de transferts thermiques et Romane a également effectué ces recherches et a amené, cette semaine, des revues concernant l'informatique et les différents composants d'un ordinateur. Avec cette mise en commun, des schémas étaient nécessaires pour faciliter la compréhension et éviter les malentendus. Nous avons donc utilisé le tableau de notre box pour les schémas de nos modèles et les formules à utiliser. Par ailleurs, nous avons dû appronfondir nos recherches à l'aide d'un ouvrage intitulé 'Introduction aux transferts thermiques' car nos connaissances en thermodynamique étaient trop limitées pour ce que nous voulons envisager. Nous avons notamment pu trouver [cette formule ci](https://github.com/are2019-mipia1a2/Temperature-salle-info/blob/master/formules.pdf) (1) qui nous est utile pour le calcul de la température en conduction.

D'autre part, nous avons créé notre [Diaporama](https://github.com/are2019-mipia1a2/Temperature-salle-info/blob/master/Diapo%20pr%C3%A9sentation.odp) pour notre passage oral la semaine suivante.

### Semaine du 25 février 2019

La séance a débuté par la présentation des différents projets de chaque groupe. Nous avons donc présenté notre projet en quelques minutes, puis nous avons discuté des diverses modélisations possibles. Nous avons constaté que le sujet que nous allons abordé semble diverger des idées des autres groupes, plus axés sur les interactions sociales . Même si notre projet paraît ambitieux, nous sommes déterminés à aboutir notre modélisation. Nous avons continué nos recherches par la suite et programmé pendant le temps qui nous restait.

### Semaine du 4 mars 2019

La première partie de la séance a été consacrée à la poursuite de notre projet: nous avons cherché en priorité une relation entre la convection et la conduction. En effet, afin d'obtenir la température ambiante de la salle après un temps t, celle-ci doit comprendre deux transferts thermiques venant des ordinateurs, de convection et de conduction. Nous nous sommes arrêtés sur une formule étant basée sur la moyenne de deux masses volumiques, d'une part celle de la salle (qui ne prend pas en compte le volume de l'ordinateur), et d'autre part celle en lien avec le volume chaud d'air brassé sortant de l'ordinateur. La deuxième partie du cours a été réservée pour une intervention visant à nous aider dans nos recherches documentaires, ce qui nous a été assez utile (archives bibliothèques, sites scientifiques, recherches en anglais,...) .

### Semaine du 11 mars 2019

Pendant ces quatre heures, une partie du groupe s'est focalisée sur les formules liées aux échanges thermiques internes et au brassement d'air du PC, tandis que l'autre partie s'est concentrée sur le blog, la modélisation en 2D, ainsi que la transmission thermique en chaque point de l'air de la salle.Des interrogations ont été soulevées quant à la modélisation complexe de nos modèles, créant des débats au sein du groupe. Cependant, nous avons trouvé un accord à ce sujet.

### Semaine du 18 mars 2019

Pour cette séance, on s'est focalisé sur trois points de ce projet : la finition du codage de la variation de tempérarture de l'ordinateur (nous avions besoin de finir la partie conduction donnée par les composants de l'ordinateur et la partie sur la ventilation retirant une partie de l'air chaud interne permettant de ne pas faire surchauffer l'ordinateur), la convection dans l'air, démarrant de l'ordinateur pour que la température se propage dans la salle, et commencer la modélisation par des matrices. 
Suite au choix de modéliser notre sujet avec des matrices, des décicsions ont dû être prises quant au postulat lié à celui-ci : que représente une case de la matrice, combien d'ordinateurs peuvent se trouver sur un espace d'air, ect. 
On a terminé ces quatre heures par tester notre modèle avec des exemples pour voir si notre codage fonctionnait.

Il nous faut donc désormais finir notre programme principale en ajoutant les convections de températures dans la salle en travaillant par unité d'air puis faire notre modélisation iconographique.

### Semaine du 25 mars 2019

Après de nombreuses recherches en ligne, nous avons enfin trouvé une relation qui nous permettrerait d'obtenir la température finale d'une "case" de la matrice grâce à différents facteurs connus ou bien constants . Cela signifie que nous pouvons désormais commencer à coder la modélisation des flux thermiques dans la salle. D'autre part, les dimensions de notre salle d'étude ont été fixées et Gabin a continué à programmer avec l'aide des trois autres membres du groupe. Nous nous posons encore des questions sur la modélisation de notre salle informatique, par rapport à la propagation du flux de chaleur à travers la salle. D'un autre côté, nous avons achevé la modélisation de l'ordinateur, en particulier la partie concernant le ventilateur en contact avec l'extérieur du PC. Nous avons aussi commencé à programmer la case de la matrice liée à l'ordinateur, grâce aux formules de convection et de conduction trouvées précédemment. 

### Semaine du 1 avril 2019

Pendant cette séance, nous avons continué les travaux déjà entamés, c'est à dire le modèle de l'ordinateur et l'homogénéisation des cases de la matrice. Gabin s'est surtout centré sur l'ordinateur et Shanita sur le modèle de la salle. L'homogénéisation pose certains problèmes quant au temps pris par une case pour s'homogénéiser ainsi que la prise en compte d'une case étant entourée de plusieurs autres cases. Nous avons aussi commencé à préparer notre compte rendu en entamant le diaporama. Avec le modèle de l'ordinateur terminé, il ne restera plus qu'à mêler les différents programmes pour obtenir notre modèle 2, un ordinateur dans une salle sans ventilateur. [Cette formule](https://github.com/are2019-mipia1a2/Temperature-salle-info/blob/master/formulesV2.pdf) (7) nous sert à homogénéiser la température entre différentes cases de la matrice.

### Semaine du 8 avril 2019




