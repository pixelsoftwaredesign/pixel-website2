"""Contenu textuel des cours de la PixelSoftware Academy."""
FONDEMENTS_TEXT = r"""Pixel Software Design — Département de Recherche & Développement
PIXEL SOFTWARE DESIGN
Département de Recherche & Développement
Intelligence Artificielle Avancée & Federated Learning

• Fondations de l'intelligence artificielle
• Algorithmes d'apprentissage fédéré
• Confidentialité, attaques et défenses
• Applications et grands modèles fédérés
• Framework FedX de référence
• Nouveaux fronts de recherche
• Travaux pratiques, projets et évaluation

Auteur Ghiloufi Jamel
Fonction Architecte Logiciel Principal
Direction Département de Recherche & Développement
Service R&D - Intelligence Artificielle Avancée & Apprentissage Fédéré
Niveau Recherche
Édition Édition 2026 — 1.0
Copyright © Pixel Software Design
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans autorisation écrite préalable de l'auteur.

PIXEL SOFTWARE DESIGN Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
Copyright et mentions légales
Éditeur Pixel Software Design
Auteur Ghiloufi Jamel
Fonction Architecte Logiciel Principal
Département Département de Recherche & Développement
Intitulé Intelligence Artificielle Avancée & Federated Learning
Sous-titre Fondations mathématiques de l'apprentissage automatique, algorithmes fédérés, protection de la vie privée, défense contre les attaques, grands modèles de langage fédérés, systèmes embarqués, renforcement appris, applications critiques (santé, V2X), plateforme de référence FedX et feuille de route de recherche.
Édition Édition 2026 (version 1.0)
Langue Français
Niveau Recherche
Collection Supports de formation et de recherche, Pixel Software Design

Droits d'auteur
© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans autorisation écrite préalable de l'auteur.

Droits de l'auteur. Ghiloufi Jamel est l'auteur unique de l'ensemble du contenu scientifique, pédagogique et technique de cet ouvrage. Toute adaptation, traduction, reproduction ou exploitation, y compris partielle, requiert une autorisation écrite préalable.

Droits des tiers. Les algorithmes, modèles et travaux cités restent la propriété de leurs auteurs respectifs. Les références employées figurent en fin d'ouvrage, ce qui permet de remonter au travail original pour toute affirmation chiffrée.

Marques et licences externes. PyTorch, TensorFlow, Flower, Opacus, MONAI, scikit-learn et PySyft sont des logiciels libres sous licences respectives (BSD, Apache 2.0, MIT). Leur usage dans ce document est purement pédagogique et n'emporte aucune prescription commerciale.

Mentions relatives aux données et aux expérimentations
Document pédagogique à usage de formation interne. Les exemples de code fournis sont livrés à titre pédagogique ; les résultats numériques illustrés sont issus d'expérimentations conduites dans un cadre de recherche et ne constituent pas des performances de production.

Sommaire
Structure détaillée du cours

Partie 1 — Fondements théoriques de l'intelligence artificielle
1.1 Logique symbolique, langages formels et limites du consensus
1.2 Théorie des langages de programmation et calcul différentiable
1.3 Compilation des graphes de calcul : dialectes et mémoire
1.4 Informatique théorique : complexité, information, graphes
1.5 Science des données et méthode empirique
1.6 Les disciplines qui préparent l'IA de demain

Partie Thème Contenu Compétence visée Durée
Partie 1 Fondations Statistique, optimisation, courbes d'apprentissage Comprendre et formaliser 2-3 semaines
Partie 2 Algorithmes FL FedAvg, convergence, hétérogénéité, système Implémenter et régler 3-4 semaines
Partie 3 Confidentialité DP, attaques, défenses, agrégation sécurisée Auditer et sécuriser 2-3 semaines
Partie 4 Applications FedLLM, santé, V2X, FedRL, TinyML, graphes Transposer à un domaine 3-4 semaines
Partie 5 Framework FedX Architecture, API, benchmarks, exploitation Industrialiser 2 semaines
Partie 6 Nouveaux fronts FedCL, FedCI, SNN, FedGL, feuille de route Ouvrir la recherche 2 semaines
Partie 7 TP et projets 9 labs, 5 projets, corrigés, évaluation Faire et rendre 4-6 semaines

Préface — Comment utiliser ce cours
Ce support est conçu pour un parcours de formation et de recherche couvrant l'ensemble de la chaîne de valeur de l'intelligence artificielle distribuée : les fondations mathématiques, les algorithmes d'apprentissage fédéré, les menaces et défenses, les applications de pointe, une plateforme de référence opérationnelle, et enfin les nouveaux fronts ouverts par la recherche du Département.
Ce n'est pas un manuel de référence à lire d'un trait : c'est un manuel opératoire. Chaque chapitre alterne exposition, formalisation, mise en œuvre numérique et évaluation. Les listings sont complets et exécutables ; les tableaux comparatifs servent de grille de décision ; les schémas d'architecture servent de support de revue de conception.
Public et prérequis : étudiants de master et de doctorat, ingénieurs IA, praticiens de la recherche appliquée. Prérequis : apprentissage automatique classique, algorithmique numérique, bases de probabilités. Les parties 1 à 3 sont auto-suffisantes ; les parties 4 à 7 supposent la mécanique et les outils de la partie 2.

Partie 1 — Fondements théoriques de l'intelligence artificielle
Logique, langages, compilation, complexité et méthode. On peut utiliser l'IA sans connaître ses fondements. On ne peut pas en concevoir de nouvelles architectures, ni comprendre pourquoi une optimisation marche, sans eux. Ce cours assemble les six disciplines théoriques qui déterminent ce qui est possible, ce qui est rapide, et ce qui reste hors de portée.

Objectifs de la partie
• Lire un algorithme d'inférence formelle et connaître la limite de complétude du premier ordre.
• Relier une fonction de perte à une grandeur de la théorie de l'information.
• Expliquer pourquoi un réseau profond est un graphe de calcul, et ce qu'est sa descente.
• Justifier le passage d'une grammaire à une autre, et connaître la hiérarchie de Chomsky.
• Comprendre ce qu'apporte un compilateur de tenseurs, et pourquoi la fusion de noyaux change tout.
• Énoncer ce que le théorème de l'impossibilité du consensus distribué impose à un système asynchrone.

Plan de la partie
1. Logique symbolique, langages formels et limites du consensus
2. Théorie des langages de programmation et calcul différentiable
3. Compilation des graphes de calcul : dialectes et mémoire
4. Informatique théorique : complexité, information, graphes
5. Science des données et méthode empirique
6. Les disciplines qui préparent l'IA de demain

Chapitre 1.1 — Logique symbolique, langages formels et limites du consensus
Trois fondations : ce qu'on sait énoncer, ce qu'on sait calculer, ce qu'il est impossible de garantir.

Langages formels et grammaires : un langage formel est défini par un alphabet fini et un ensemble de règles de production. La grammaire décrit la syntaxe ; elle ne dit rien du sens des phrases.
G : S → a S b | a  =>  a^n b^n, n ≥ 1
La récursion produit des langages infinis à partir d'un nombre fini de règles.

Hiérarchie de Chomsky :
• Type 0 — machine de Turing — aucune borne — problèmes indécidables
• Type 1 — automate à pile — pile non bornée — expressions régulières, analyse syntaxique
• Type 2 — automate à pile — pile non bornée, transduction — la plupart des langages de programmation
• Type 3 — automate fini — un seul état courant — expressions régulières
Le type 1 et le type 2 partagent le même pouvoir de mémoire ; ils diffèrent par la nature de l'algorithme de reconnaissance.

Logique des prédicats et incomplétude : la logique des prédicats du premier ordre est expressive au point d'être incomplète : il existe des énoncés vrais dans toute structure sans être démontrables (théorème de Gödel). Vérifier la satisfiabilité d'une formule du premier ordre est indécidable en général.
Satisfiabilité = ∃ M, M ⊨ φ.  Validité = ∀ M, M ⊨ φ.
Un énoncé peut être satisfiable sans être valide : il existe une structure où il est vrai, mais pas toutes. Confondre les deux est l'erreur logique la plus répandue dans les systèmes de règles.

Programmation logique : fait (homme(socrate)), règle (homme(X) :- mortel(X)), clause (¬homme(X) ∨ mortel(X)), question (?- mortel(socrate)), unification (X = socrate), résolution.

Théorème de l'impossibilité du consensus : dans un système asynchrone où un seul nœud peut tomber en panne, aucun algorithme déterministe ne peut garantir l'accord. Au moins une des propriétés suivantes doit être abandonnée : terminaison, sûreté, tolérance à la panne ou déterminisme. Aucun système réel ne satisfait les quatre ; l'agencement pratique est presque toujours : accord exact, délai borné, tolérance à la panne, et hasard dans le choix de l'arbitre.

A retenir (1.1)
• Un langage formel est infini, décrit par un ensemble fini de règles.
• La logique des prédicats est expressive mais incomplète.
• Le théorème d'impossibilité borne l'accord exact, le temps borné, la tolérance à la panne et le déterminisme.
• Tout système réel abandonne au moins une de ces quatre propriétés.

Chapitre 1.2 — Théorie des langages de programmation et calcul différentiable
Un réseau de neurones est un programme. C'est un programme qui se dérive.

Lambda-calcul : modèle universel du calcul. Trois formes seulement, mais universellement puissant. L'application se lit comme une fonction : T' = t'[x ↦ t].

Systèmes de types et dimensions des tenseurs : l'erreur la plus fréquente en apprentissage profond n'est pas algorithmique, c'est l'incompatibilité de dimensions.
(d1,d2) × (d1,d3) → (d2,d3) ; incompatible si d2 ≠ d3.
Quatre dimensions à vérifier systématiquement : après toute normalisation (écart-type non nul), avant toute réduction de dimension (nombre de composantes ≤ nombre d'exemples), entre deux lots (pas de lot vide), avant toute réduction de mémoire (taille alignée sur la granularité réelle).

Calcul différentiable comme langage : un programme devient apprenable lorsque chaque opération est différentiable. Le compilateur construit un second programme, le graphe de rétropropagation.
Algorithme 1 — Descente de gradient : initialiser les poids au hasard ; choisir un lot ; passer avant ; enregistrer chaque opération dans un graphe ; calculer la perte ; dériver locale ; propager vers l'arrière ; mettre à jour les poids ; répéter ; évaluer sur validation. Coût de la passe arrière ≈ 2 fois la passe avant. La ligne 3 (enregistrement) est la charnière : sans elle, la rétropropagation est impossible, et c'est la source de la plus grande consommation mémoire.

A retenir (1.2)
• Le lambda-calcul est un modèle universel du calcul.
• Une erreur de dimensions est une erreur de type déguisée.
• Le calcul différentiable transforme un programme en un second programme qui le dérive.
• L'enregistrement du graphe est la condition de la rétropropagation, et la première source de coût mémoire.

Chapitre 1.3 — Compilation des graphes de calcul : dialectes et mémoire
Le même code doit tourner sur un processeur, une carte graphique ou un circuit. C'est un problème de langages.

Dialecte : un sous-ensemble de types, d'opérations et de règles de transformation, correspondant à un niveau d'abstraction précis. Un même programme peut être exprimé dans plusieurs dialectes ; le compilateur passe de l'un à l'autre par abaissement.
Dialectes : tensor (opérations mathématiques abstraites, fusion sur tenseurs entiers), linalg (itérations d'algèbre linéaire structurées, parallélisation/pavage/vectorisation), sparse (matrices creuses), memref (blocs mémoire/adresses/durées de vie, allocation/réutilisation), scf (contrôle de flux structuré), gpu (unités de calcul de la carte), llvm (instruction machine générique).

Les trois techniques de gestion de la mémoire : analyse de durée de vie (déterminer quand un tenseur est créé, utilisé pour la dernière fois, puis mort), réutilisation de tampons (deux tenseurs dont les durées de vie ne se chevauchent pas peuvent occuper le même bloc physique), fusion de noyaux (si un résultat temporaire est produit puis relu immédiatement, il n'est jamais écrit en mémoire globale).

La bande passante, pas le calcul : un accélérateur passe l'essentiel de son temps à attendre des données. Multiplier la puissance de calcul sans réduire les transferts mémoire ne produit aucune accélération.

A retenir (1.3)
• Un dialecte est un niveau d'abstraction avec ses propres types et règles.
• L'abaissement progressif permet d'optimiser là où une représentation unique ne le peut pas.
• La durée de vie d'un tenseur autorise la réutilisation de tampon.
• La fusion de noyaux supprime les allers-retours en mémoire globale, premier poste de coût.

Chapitre 1.4 — Informatique théorique : complexité, information, graphes
Trois théories qui disent ce qui est faisable, ce qui est rapide, et ce que vaut une information.

Complexité : la classe NP décrit les problèmes dont on vérifie facilement une solution. La question P = ? NP est ouverte. L'apprentissage automatique contourne la difficulté NP par statistique : il n'essaie pas de trouver la solution optimale, il apprend une politique bonne en moyenne.
Classes : P (solution en temps polynomial), NP-complet (vérifier une solution est polynomial, accepter une solution approximative), PSPACE (problèmes de jeux et d'agents), Indécidable (aucun algorithme).

Théorie de l'information : H(p) = -Σ p_k log2 p_k ; L = -Σ p*_k log2 p̂_k (entropie croisée). Minimiser l'entropie croisée revient à maximiser la vraisemblance. Quantités : entropie (incertitude moyenne), entropie croisée (écart entre distributions), information mutuelle (information partagée), divergence de Kullback-Leibler (distance non symétrique), bande passante (capacité d'un canal).

Théorie des graphes : un réseau profond est un graphe orienté acyclique de calcul. Passage avant et arrière = deux parcours du même graphe. Processus décisionnel de Markov : modèle formel d'un agent qui évolue entre états. Graphe de connaissance : entités reliées par des relations typées, base d'un raisonnement symbolique explicable.

A retenir (1.4)
• La classe NP borne ce qu'une recherche exhaustive peut produire ; l'AA la contourne par approximation.
• L'entropie croisée est la traduction directe de la théorie de l'information en fonction de perte.
• Un réseau profond est un graphe orienté acyclique de calcul, parcouru dans deux sens.
• Le processus de Markov est le modèle formel d'un agent qui évolue entre états.

Chapitre 1.5 — Science des données et méthode empirique
La science des données est l'ensemble des contraintes qui empêchent une bonne méthode de produire un mauvais résultat.

Préparation : valeurs manquantes (comprendre pourquoi elles manquent — une valeur absente après un refus est une information), normalisation (indispensable si variables d'unités différentes), détection d'anomalies, fuite d'information (une variable qui n'existait pas au moment de la prédiction ne peut pas servir).

Statistiques et probabilités : y_i ∼ N(μ, σ²) → μ̂ ± (σ/√n) z_{1-α/2}. L'intervalle de confiance porte sur la procédure, pas sur le paramètre estimé.

Ingénierie des caractéristiques : normalisation centrée réduite (sensible aux valeurs extrêmes), discrétisation, indicateurs, interactions (explosion combinatoire), réduction de dimension, transformations logarithmiques (impossible sur les valeurs négatives).

Évaluation et validation — protocole en cinq temps : séparer en trois jeux (entraînement, validation, test) ; valider croisée sur l'entraînement, jamais sur le test ; choisir les hyperparamètres sur la validation ; consulter le test une seule fois, à la fin ; rapporter l'intervalle de confiance. Le test consulté régulièrement cesse d'être un test.
Indicateurs : exactitude (classes équilibrées), précision (faux positif coûte cher), rappel (faux négatif coûte cher), score F1 (compromis), AUC (comparaison de classifieurs), matrice de confusion (audit).

A retenir (1.5)
• La préparation des données précède le choix du modèle et détermine le plafond de performance.
• Un intervalle de confiance porte sur la procédure, pas sur le paramètre estimé.
• Le test consulté régulièrement cesse d'être un test.
• Le choix de l'indicateur découle du coût de chaque type d'erreur.

Chapitre 1.6 — Les disciplines qui préparent l'IA de demain
Cinq domaines dont la rencontre déterminera les dix prochaines années.
Disciplines : Matériel et calcul (comment calculer plus vite, moins cher — court terme), Neuro-symbolique (comment vérifier un raisonnement — moyen terme), Systèmes multi-agents (comment coordonner des agents — moyen terme), Neurosciences computationnelles (comment apprendre en continu — long terme), Éthique et gouvernance (comment garder le contrôle — immédiat). Les deux dernières ne sont pas de la recherche : elles déterminent ce qui peut être déployé.

Matériel, accélérateurs et informatique quantique : la contrainte matérielle a façonné toute l'histoire de l'IA. L'apprentissage automatique quantique est un domaine de recherche ; aucune application industrielle à ce jour ; la question de savoir si le calcul quantique accélérera un modèle d'apprentissage reste ouverte.

Architectures neuro-symboliques : faire produire une conclusion par un réseau, puis la faire vérifier par un moteur logique. Vérification de la sortie, exécution de contraintes, appel d'outils symboliques, explication par trace. Exemple : un assistant de requête en langage naturel produit une requête SQL ; encadrer la génération d'une couche symbolique (typage des colonnes, vérification des prédicats, contrôle des droits d'accès) donne un système dont le comportement est borné.

Systèmes multi-agents : les organisations en essaim remplacent progressivement l'assistant unique. La théorie des jeux, les protocoles de consensus et l'auto-organisation sont les outils de conception.

Neurosciences computationnelles : plasticité synaptique, mémoire, sparsité, niveaux de mémoire — emprunter des principes, pas reproduire le cerveau.

Éthique, alignement et gouvernance : alignement des objectifs, théorie du choix social, cryptographie appliquée à la traçabilité ; droit et gouvernance comme cadre opérationnel.

Comment lire une prévision à dix ans : séparer trois registres — déployé aujourd'hui, recherche expérimentale, spéculation. Si l'affirmation ne peut pas être testée par une expérimentation publiée, elle relève du troisième registre.

A retenir (1.6)
• Les cinq disciplines qui comptent ne sont pas cinq voies technologiques, mais cinq questions distinctes.
• Le neuro-symbolique vise la vérifiabilité, pas la performance.
• L'apprentissage quantique reste un domaine de recherche sans application industrielle.
• Trois registres de lecture — déployé, recherché, spéculatif — doivent être séparés dans tout document prospectif.

Index des figures et des tableaux
Figures : chaîne symbolique et chaîne neuronale ; descente d'un graphe de calcul ; temps de calcul selon la taille du problème ; cycle empirique de la science des données ; cinq disciplines qui préparent l'IA de demain.
Tableaux : hiérarchie de Chomsky ; programmation logique ; ce que l'impossibilité impose ; programmation fonctionnelle et réseaux de neurones ; dialectes de la chaîne de compilation ; quatre phases de la compilation ; classes de complexité ; quantités de la théorie de l'information ; transformations de variables ; indicateurs de classification ; cinq disciplines.

© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans autorisation écrite préalable de l'auteur.
Document généré automatiquement le 29/09/2026 — mise en page Pixel Software Design.
"""

PROGRAMME_OFFICIEL_TEXT = r"""Module 1 — Systèmes distribués & Federated Learning (FedProx)
Support de cours — PixelSoftware Academy, édition 2026
Public : Master 2 / cycle ingénieur. Volume : 30 h (10 h de cours, 20 h de TP). Prérequis : Python, algèbre linéaire, descente de gradient, notions de probabilités.

Objectifs du module
À la fin du module, vous saurez :
• expliquer pourquoi et quand l'apprentissage fédéré remplace l'entraînement centralisé ;
• décrire les formes d'hétérogénéité des données (non-i.i.d.) et leurs effets ;
• formuler le problème d'optimisation fédérée, implémenter FedAvg et FedProx ;
• protéger les mises à jour par clipping et bruit gaussien (DP-SGD) ;
• rendre l'agrégation robuste à des clients malveillants avec la moyenne tronquée (Trimmed Mean).

Plan
1. Pourquoi l'apprentissage fédéré ?
2. Données i.i.d. et non-i.i.d.
3. Formulation du problème et FedAvg
4. Le Client Drift
5. FedProx
6. Confidentialité différentielle et DP-SGD
7. Robustesse : empoisonnement et Trimmed Mean
8. Implémentation en Python pur
9. Exercices et corrigés courts
10. Résumé et références

1. Pourquoi l'apprentissage fédéré ?
1.1 Les limites de l'architecture centralisée
Dans l'approche classique, toutes les données sont copiées sur un serveur qui entraîne le modèle. Trois limites apparaissent dès que les données sont sensibles ou massives.
• Conformité. Le RGPD, le secret médical ou des contrats peuvent interdire de transférer des données hors de leur lieu d'origine. Copier des dossiers patients vers un serveur commun est souvent impossible.
• Latence et coût. Déplacer de gros volumes de données coûte en bande passante et en temps ; pour des appareils mobiles, c'est parfois irréaliste.
• Point de défaillance unique (SPOF). Un serveur central qui contient toutes les données est une cible d'attaque et un point de panne unique.

1.2 Le principe fédéré
En apprentissage fédéré, les données restent chez les clients (hôpitaux, téléphones, entreprises). Un serveur coordonne : il envoie le modèle courant, chaque client l'entraîne localement sur ses données, renvoie une mise à jour, et le serveur les agrège pour produire le nouveau modèle. Seuls des paramètres circulent.
Deux contextes à distinguer. Le cadre cross-silo regroupe peu de clients fiables et puissants (par exemple trois hôpitaux). Le cadre cross-device regroupe un très grand nombre d'appareils, dont une fraction seulement participe à chaque tour. Le projet fil rouge relève du premier.

1.3 Une précision importante
Le fédéré protège la localisation des données, pas automatiquement leur confidentialité. Les mises à jour peuvent révéler de l'information sur les données qui les ont produites. C'est pourquoi on ajoute la confidentialité différentielle (section 6).

2. Données i.i.d. et non-i.i.d.
Des données sont i.i.d. (indépendantes et identiquement distribuées) si tous les clients tirent leurs échantillons de la même distribution. C'est rarement le cas. Les principales formes d'hétérogénéité sont les suivantes.
Forme | Description | Exemple médical
Déséquilibre des classes (label skew) | Les proportions de classes diffèrent selon le client | Un hôpital spécialisé voit surtout une pathologie
Feature Shift | La distribution des entrées diffère | Deux appareils d'imagerie de réglages différents
Concept Drift | La relation entrée-sortie change selon le client ou le temps | Deux protocoles de diagnostic différents
Déséquilibre de quantité | Les clients ont des nombres d'exemples très inégaux | Un grand CHU et une petite clinique
Conséquence. Le gradient calculé par un client n'est plus une estimation fidèle du gradient global : chaque client « tire » le modèle vers son propre optimum.

Partition de Dirichlet (outil de TP). Pour simuler le déséquilibre de classes, on tire pour chaque classe une répartition entre clients selon une loi de Dirichlet de paramètre beta : un petit beta (0,1) donne des clients très spécialisés, un grand beta (100) donne des données presque i.i.d.

3. Formulation du problème et FedAvg
3.1 Objectif global
Soit K clients. Le client k possède n_k exemples ; n est la somme des n_k. Sa perte locale est F_k(w). L'objectif global est
F(w) = somme sur k de p_k · F_k(w), avec p_k = n_k / n.
Les poids p_k donnent plus d'importance aux clients qui ont plus de données.

3.2 L'algorithme FedAvg
À chaque tour t :
1. Le serveur choisit un sous-ensemble de clients et leur envoie w_t.
2. Chaque client effectue E époques de descente de gradient locale à partir de w_t et obtient w_k.
3. Le serveur calcule le nouveau modèle : w_(t+1) = somme sur k de p_k · w_k.

Exemple numérique. Trois clients ont n = 100, 300 et 600 exemples, donc p = 0,1 ; 0,3 ; 0,6. Pour un paramètre scalaire, ils renvoient 1,0 ; 2,0 et 3,0. Le serveur obtient 0,1 × 1,0 + 0,3 × 2,0 + 0,6 × 3,0 = 0,1 + 0,6 + 1,8 = 2,5. Une moyenne simple aurait donné 2,0 : la pondération compte.

Compromis communication-calcul. Augmenter E réduit le nombre de tours (donc la communication) mais accroît la dérive décrite ci-dessous.

4. Le Client Drift
Si les données sont non-i.i.d., l'optimum de F_k diffère de l'optimum de F. Plus un client fait d'étapes locales, plus il s'éloigne du modèle global vers son propre optimum, et la moyenne de modèles très éloignés est un mauvais compromis.

Exemple scalaire. Deux clients de poids égaux (p = 0,5 chacun) :
• client 1 : F_1(w) = (1 / 2) · w², optimum local 0 ;
• client 2 : F_2(w) = (0,1 / 2) · (w − 10)², optimum local 10, avec une courbure dix fois plus faible.
L'optimum global annule le gradient moyen : w + 0,1 · (w − 10) = 0, donc 1,1 · w = 1 et l'optimum vaut w_opt ≈ 0,909.
Si chaque client résout complètement son problème local à chaque tour (E très grand), le serveur moyenne 0 et 10 et obtient 5, très loin de 0,909. Le client 2, plus « plat », ne devrait presque pas peser dans la solution, mais la moyenne simple lui donne autant de poids qu'au client 1. C'est le Client Drift : l'algorithme converge vers un point qui n'est pas l'optimum global.

5. FedProx
5.1 Idée
FedProx limite la dérive en ajoutant à l'objectif local un terme qui pénalise l'éloignement par rapport au modèle global courant w_t :
h_k(w ; w_t) = F_k(w) + (mu / 2) · ‖w − w_t‖².
Le paramètre mu ≥ 0 règle la force de rappel. Le gradient local devient
gradient de F_k en w, plus mu · (w − w_t).
Le second terme tire le modèle local vers w_t, comme un ressort.

5.2 Propriétés
• mu = 0 redonne exactement FedAvg.
• mu grand : le client bouge peu, la dérive est faible, mais la progression locale aussi (plus de tours nécessaires).
• Travail local variable. FedProx tolère que des clients lents ou contraints fassent moins de calcul sans bloquer le tour, ce qui est utile en pratique.
• Réglage. Valeurs à tester : 0,001 ; 0,01 ; 0,1 ; 1. Le meilleur mu dépend du degré d'hétérogénéité ; on le choisit sur un jeu de validation.

5.3 Retour sur l'exemple scalaire
Supposons que chaque client résolve exactement son problème proximal à chaque tour.
• Client 1 : on minimise w²/2 + (mu/2)(w − w_t)², d'où w = mu · w_t / (1 + mu).
• Client 2 : on minimise 0,1(w − 10)²/2 + (mu/2)(w − w_t)², d'où w = (1 + mu · w_t) / (0,1 + mu).
Le modèle global se stabilise au point fixe de la moyenne de ces deux réponses. On obtient :
mu | Point fixe du serveur | Écart à l'optimum 0,909
0 (FedAvg) | 5,00 | 4,09
1 | environ 1,54 | environ 0,63
10 | environ 0,98 | environ 0,07
Plus mu est grand, plus le point fixe se rapproche de l'optimum global. Le prix à payer est que chaque tour progresse moins loin : il faut un compromis. Ce résultat est propre à cet exemple (résolution exacte, problème quadratique), mais il illustre le mécanisme.

6. Confidentialité différentielle et DP-SGD
6.1 Définition
Un mécanisme aléatoire M est (epsilon, delta)-différentiellement privé si, pour deux jeux de données voisins D et D' (qui diffèrent d'un individu, ou d'un client), et pour tout ensemble de sorties S :
Probabilité(M(D) dans S) ≤ e^epsilon · Probabilité(M(D') dans S) + delta.
Intuitivement, la sortie change très peu que l'individu soit présent ou non : un observateur ne peut presque rien déduire de sa présence. Plus epsilon est petit, plus la protection est forte.

6.2 Le mécanisme en deux étapes
1. Clipping L2. On borne la norme de chaque mise à jour : delta_w_bar = delta_w · min(1, C / ‖delta_w‖₂). Ainsi aucun client ne peut influencer l'agrégat de plus de C ; la sensibilité est bornée.
2. Bruit gaussien. On ajoute à la somme des mises à jour clippées un bruit N(0, sigma² · C² · I).
Exemple. Une mise à jour vaut (3 ; 4) ; sa norme est 5. Avec C = 1, le facteur vaut min(1 ; 1/5) = 0,2 et la mise à jour clippée vaut (0,6 ; 0,8), de norme 1. Avec sigma = 1, on ajoute à chaque coordonnée de la somme un bruit d'écart-type sigma · C = 1. Si l'on moyenne K = 10 clients, le bruit sur la moyenne a un écart-type de 0,1 par coordonnée : plus il y a de clients, moins le bruit relatif est gênant.

6.3 Compromis confidentialité-utilité
• Un sigma plus grand donne un epsilon plus petit (meilleure confidentialité) mais un entraînement plus bruité.
• Un C trop petit écrête l'information utile ; un C trop grand exige plus de bruit pour la même garantie.
• Le budget se consomme à chaque tour : un comptable de confidentialité (comptable des moments, confidentialité de Rényi) suit le total. L'échantillonnage aléatoire des clients amplifie la protection.
Précision. Dans l'article original de DP-SGD, le clipping porte sur les gradients de chaque exemple. En fédéré, on clippe souvent la mise à jour de chaque client, ce qui protège un client entier. C'est la variante utilisée en TP.

7. Robustesse : empoisonnement et Trimmed Mean
7.1 Menaces
Un client malveillant peut empoisonner ses données (inversion d'étiquettes) ou envoyer directement une mise à jour nuisible. Contre une simple moyenne, un seul client suffit pour déplacer le résultat arbitrairement loin.

7.2 Moyenne tronquée (Trimmed Mean)
Pour chaque paramètre (coordonnée par coordonnée) :
1. on trie les K valeurs reçues ;
2. on retire les b plus petites et les b plus grandes ;
3. on moyenne les K − 2b valeurs restantes.
Exemple. Sept clients envoient, pour un même paramètre : 0,9 ; 1,0 ; 1,1 ; 1,0 ; 0,95 ; 1,05 et 50 (valeur d'un client malveillant).
• Moyenne simple : (0,9 + 1,0 + 1,1 + 1,0 + 0,95 + 1,05 + 50) / 7 = 56 / 7 = 8,0.
• Valeurs triées : 0,9 ; 0,95 ; 1,0 ; 1,0 ; 1,05 ; 1,1 ; 50. Avec b = 1, on retire 0,9 et 50, et on moyenne les cinq valeurs restantes : 5,1 / 5 = 1,02.
Le résultat est proche de la vérité (environ 1), alors que la moyenne simple est faussée par un seul client.

7.3 Limites
• La méthode résiste si le nombre de clients malveillants ne dépasse pas b.
• En non-i.i.d., des clients honnêtes mais atypiques peuvent être écartés : la robustesse coûte de l'efficacité. Le choix de b est un compromis.
• Elle ne protège pas la confidentialité : elle se combine avec DP-SGD, elle ne le remplace pas.

8. Implémentation en Python pur
Le programme ci-dessous reproduit l'exemple scalaire de la section 4 et permet de comparer FedAvg (mu = 0) et FedProx. Les clients ont chacun une perte quadratique F_k(w) = (a / 2) · (w − c)².

def local_update(w_t, a, c, mu, lr, steps):
    w = w_t
    for _ in range(steps):
        grad = a * (w - c) + mu * (w - w_t)
        w -= lr * grad
    return w


def run(mu, rounds=200, steps=500, lr=0.1):
    clients = [(1.0, 0.0), (0.1, 10.0)]   # (a, c) ; poids egaux
    w = 5.0
    for _ in range(rounds):
        locals_ = [local_update(w, a, c, mu, lr, steps) for a, c in clients]
        w = sum(locals_) / len(locals_)
    return w


for mu in (0.0, 1.0, 10.0):
    print(mu, round(run(mu), 3))
Résultats attendus (approximatifs, car la résolution locale n'est pas exacte) : environ 5 pour mu = 0, environ 1,5 pour mu = 1 et environ 1,0 pour mu = 10. L'optimum global est 0,909.
Pour le TP. Remplacez la perte quadratique par une régression logistique sur des données simulées, ajoutez la partition de Dirichlet, puis le clipping, le bruit et la moyenne tronquée. Vérifiez chaque brique par un test numérique (par exemple, avec mu = 0 votre FedProx doit coïncider avec votre FedAvg).

9. Exercices
1. FedAvg. Quatre clients ont n = 50, 150, 300, 500 exemples et renvoient 2, 4, 6, 8 pour un paramètre. Calculez le résultat de l'agrégation pondérée et celui de la moyenne simple.
2. Terme proximal. Pour F_k(w) = (w − 4)² / 2 et w_t = 0, écrivez h_k(w ; w_t) et trouvez le minimiseur en fonction de mu. Que se passe-t-il quand mu tend vers 0 ? vers l'infini ?
3. Clipping. Une mise à jour vaut (6 ; 8). Calculez sa version clippée avec C = 2. Quelle est sa norme ?
4. Bruit. Avec sigma = 2, C = 1 et K = 20 clients, quel est l'écart-type du bruit sur la moyenne, par coordonnée ?
5. Trimmed Mean. Neuf clients envoient 3,0 ; 3,1 ; 2,9 ; 3,0 ; 3,2 ; 2,8 ; 3,0 ; −40 ; 90. Calculez la moyenne simple, puis la moyenne tronquée avec b = 2.
6. Réflexion. Pourquoi une forte confidentialité différentielle et une forte robustesse (b grand) peuvent-elles toutes deux ralentir la convergence ? Proposez une expérience qui mesure ces effets.

Corrigés courts
1. Poids : 0,05 ; 0,15 ; 0,30 ; 0,50. Agrégation : 0,1 + 0,6 + 1,8 + 4,0 = 6,5. Moyenne simple : 5.
2. h_k = (w − 4)² / 2 + (mu / 2) · w². Le gradient (w − 4) + mu · w s'annule en w = 4 / (1 + mu). Quand mu tend vers 0, w tend vers 4 (optimum local) ; quand mu tend vers l'infini, w tend vers 0 (on reste en w_t).
3. Norme 10 ; facteur min(1 ; 2/10) = 0,2 ; mise à jour clippée (1,2 ; 1,6), de norme 2.
4. Bruit sur la somme : sigma · C = 2 ; sur la moyenne : 2 / 20 = 0,1.
5. Somme : 3,0 + 3,1 + 2,9 + 3,0 + 3,2 + 2,8 + 3,0 − 40 + 90 = 70,0 ; moyenne simple 70 / 9 ≈ 7,78. Triées : −40 ; 2,8 ; 2,9 ; 3,0 ; 3,0 ; 3,0 ; 3,1 ; 3,2 ; 90. On retire les deux plus petites (−40 ; 2,8) et les deux plus grandes (3,2 ; 90) ; il reste 2,9 ; 3,0 ; 3,0 ; 3,0 ; 3,1 de somme 15,0, soit une moyenne tronquée de 3,0.
6. Le bruit et le clipping dégradent le signal de chaque mise à jour ; la troncature jette des informations de clients honnêtes. Expérience : faire varier sigma et b séparément puis ensemble, et tracer la précision en fonction du nombre de tours, sur plusieurs graines aléatoires.

10. Résumé et références
À retenir
• Le fédéré garde les données sur place mais ne garantit pas la confidentialité à lui seul.
• Avec des données non-i.i.d., la moyenne de modèles locaux dérive (Client Drift).
• FedProx ajoute (mu / 2) · ‖w − w_t‖² pour borner cette dérive ; mu = 0 redonne FedAvg.
• DP-SGD = clipping L2 + bruit gaussien ; le budget epsilon se consomme à chaque tour.
• La moyenne tronquée résiste à b clients malveillants mais coûte de l'efficacité en non-i.i.d.

Glossaire
• Client Drift : éloignement des modèles locaux dû à l'hétérogénéité des données.
• Cross-silo / cross-device : peu de clients fiables contre beaucoup d'appareils intermittents.
• Sensibilité : variation maximale de la sortie quand un individu est ajouté ou retiré.
• Trimmed Mean : moyenne après retrait des valeurs extrêmes, coordonnée par coordonnée.

Références
• McMahan et al., 2017 : Communication-Efficient Learning of Deep Networks from Decentralized Data (FedAvg).
• Li et al., 2020 : Federated Optimization in Heterogeneous Networks (FedProx).
• Abadi et al., 2016 : Deep Learning with Differential Privacy (DP-SGD).
• Yin et al., 2018 : Byzantine-Robust Distributed Learning: Towards Optimal Statistical Rates (moyenne tronquée).
Références citées de mémoire : à vérifier avant diffusion aux étudiants.

Feuille de route Recherche & Développement
Objectif : faire de l'Académie un lieu où le cursus se nourrit de la recherche, et où les travaux des étudiants alimentent en retour les cours. Cette feuille de route s'appuie sur une veille de la littérature 2026 ; les références citées sont à vérifier par l'équipe avant publication dans le syllabus.

Principes
• Boucle recherche vers cours : chaque semestre, les résultats de veille ou d'expériences menées en labo sont intégrés comme TP, étude de cas ou question ouverte.
• Reproductibilité d'abord : dépôt de code partagé, graines aléatoires fixées, jeux de données simulés documentés, résultats chiffrés accompagnés de leurs conditions.
• Honnêteté expérimentale : comparer toujours à des lignes de base simples ; publier aussi les résultats négatifs.
• Données simulées uniquement pour la santé, tant qu'aucun cadre de conformité avec un partenaire n'est signé.

Axe 1 : Apprentissage fédéré, LoRA et confidentialité
État de la veille : la littérature récente montre que LoRA appliqué tel quel en apprentissage fédéré confidentialisé dégrade les performances. Un article de février 2026 (LA-LoRA, arXiv 2602.19926) identifie le couplage des gradients entre les deux matrices, l'amplification du bruit sous confidentialité différentielle et la netteté du modèle agrégé, et propose une optimisation alternée locale. RoLoRA (alternance d'optimisation de A et B) est une autre référence de robustesse. Côté communication, FedSRD (parcimonie structurée) et GMFL (masquage global, ACL 2026) cherchent à réduire encore le volume échangé.
Questions de recherche pour l'Académie :
• L'agrégation séparée de A et B (module 4, C3) dégrade-t-elle la précision, et de combien, selon le niveau de bruit sigma ?
• Une optimisation alternée reproduit-elle sur nos données simulées les gains rapportés ?
• Quel rang r minimise le coût de communication pour une perte d'utilité fixée ?
Projets étudiants possibles : reproduction d'un article (FedAvg-LoRA contre alternance), étude d'ablation sur r, sigma et mu, mesure de la fuite d'information par attaque d'inférence d'appartenance.
Impact sur le cursus : ajouter au module 4 un TP optionnel de reproduction (3 h) et une séance de lecture d'article.

Axe 2 : GraphRAG, quand et pourquoi
État de la veille : plusieurs travaux de 2025-2026 nuancent l'enthousiasme initial. Le benchmark GraphRAG-Bench (ICLR 2026) rapporte que GraphRAG sous-performe fréquemment un RAG classique sur de nombreuses tâches réelles et que le RAG simple est comparable, voire meilleur, sur la recherche de faits simples ; l'avantage du graphe apparaît surtout sur le raisonnement multi-sauts, avec un surcoût de latence. Une évaluation systématique (RAG contre GraphRAG, mars 2026) souligne en outre que des graphes construits automatiquement couvrent mal les réponses : environ 65,8 % des entités-réponses de HotpotQA seulement y figuraient, ce qui plafonne la récupération.
Questions de recherche pour l'Académie :
• Sur notre corpus médical simulé, dans quels types de questions le terme gamma (centralité) améliore-t-il le score ?
• Peut-on régler alpha, beta, gamma dynamiquement selon le type de requête (fait simple contre multi-sauts) ?
• Quelle est la couverture réelle du graphe, et comment la mesurer et l'améliorer ?
Projets étudiants possibles : routeur de requêtes entre RAG simple et GraphRAG (réutilise le pattern du module 3), mesure de couverture et de latence, évaluation sur un sous-ensemble de GraphRAG-Bench.
Impact sur le cursus : dans le module 2 (T4), exiger une comparaison explicite avec la ligne de base RAG simple, y compris le coût de latence ; c'est une évolution à faible coût et forte valeur pédagogique.

Axe 3 : Sécurité des agents et guardrails
Questions de recherche : robustesse des guardrails face à des attaques adaptatives, injection indirecte via le Meaning Graph ou le cache sémantique, compromis faux positifs et faux négatifs, fuite de PII par les journaux et le cache.
Projets étudiants possibles : constitution d'un jeu de tests adverses réutilisable d'une promotion à l'autre, red teaming croisé entre équipes du projet fil rouge, évaluation de l'effet des guardrails sur la latence.
Impact sur le cursus : transformer l'évaluation du module 5 (T4) en défi inter-équipes, avec un jeu d'attaques enrichi chaque année.

Axe 4 : Edge ML et efficacité
Questions de recherche : quantification des poids gelés, adaptation par sous-ensemble de couches, participation de clients à ressources hétérogènes, mesure d'énergie et de mémoire sur appareil réel.
Projets étudiants possibles : banc de mesure sur mobile ou carte embarquée, comparaison de plusieurs rangs et précisions, profil mémoire de bout en bout.

Axe 5 : Évaluation, gouvernance et conformité
Questions de recherche : grilles d'audit d'un système d'IA de santé, traçabilité des décisions, documentation des modèles et des données, lien avec le RGPD et le cadre réglementaire européen sur l'IA.
Livrables : modèle de dossier d'audit fourni avec le projet fil rouge, évalué à la soutenance.

Organisation du laboratoire
Élément | Description
Séminaire de veille | Une séance mensuelle : un article présenté par un étudiant ou un enseignant, discussion et décision d'intégration au cursus
Dépôt de reproductibilité | Code, données simulées, configurations et résultats de référence par expérience
Parcours recherche | Option pour les meilleurs étudiants : remplacer une partie du projet fil rouge par une reproduction ou une extension d'article, encadrée
Publication | Rapports techniques internes, puis soumission à un atelier ou une conférence pour les travaux les plus solides
Partenariats | Hôpitaux, laboratoires et entreprises pour des cas d'usage réels, uniquement avec cadre de conformité signé

Calendrier sur 12 mois
Trimestre | Actions | Résultat attendu
T1 | Mise en place du dépôt, du séminaire de veille et des jeux de données simulés de référence ; ajout de la comparaison RAG contre GraphRAG au module 2 | Socle reproductible et premier TP enrichi
T2 | Reproduction d'un article de LoRA fédéré (axe 1) ; premier défi inter-équipes de guardrails (axe 3) | Rapport de reproduction, jeu de tests adverses v1
T3 | Banc de mesure Edge (axe 4) ; routeur RAG ou GraphRAG (axe 2) ; modèle de dossier d'audit (axe 5) | Prototype et dossier d'audit type
T4 | Bilan, mise à jour du syllabus, rédaction d'un rapport technique, sélection des travaux à soumettre | Syllabus 2027 et premier rapport technique

Indicateurs de suivi
• Nombre d'expériences reproduites avec écart documenté.
• Part des séances de cours mises à jour chaque année grâce à la veille.
• Nombre de rapports techniques et de soumissions.
• Résultats du jeu de tests adverses d'une promotion à l'autre.
• Satisfaction et progression des étudiants du parcours recherche.

Évolutions de cursus proposées
1. Module 2, T4 : ligne de base RAG simple obligatoire, avec mesure de latence et de couverture du graphe.
2. Module 4 : séance de lecture d'article et TP optionnel de reproduction sur la combinaison LoRA, bruit et agrégation.
3. Module 5, T4 : défi de red teaming entre équipes.
4. Option « Parcours recherche » en S2 à la place d'une partie du projet fil rouge.
5. Nouveau module optionnel de 10 à 15 h : méthodologie de la recherche et reproductibilité (lecture critique, protocoles d'expérience, statistiques de base, rédaction).
Ces évolutions modifieraient les volumes du programme ; elles sont à arbitrer par l'équipe pédagogique avant intégration.

Cours avancés du Master (modules d'approfondissement)
Ces cours prolongent chacun des cinq modules du tronc commun et alimentent les axes de recherche. Ils sont proposés comme électifs de 20 h (6 h de cours, 14 h de TP), à choisir en S2 ou en S3 selon l'organisation du master. Le choix de deux électifs ajoute 40 h au cursus : cet arbitrage revient à l'équipe pédagogique.

Vue d'ensemble
Code | Cours avancé | Prolonge | Axe R&D | Volume
A1 | Apprentissage fédéré avancé et vie privée | Module 1 | Axe 1 | 20 h
A2 | Graphes de connaissances et raisonnement | Module 2 | Axe 2 | 20 h
A3 | Systèmes d'IA agentiques et inférence à grande échelle | Module 3 | Axes 2 et 3 | 20 h
A4 | Compression, PEFT avancé et déploiement Edge | Module 4 | Axe 4 | 20 h
A5 | IA de confiance : attaques, audit et conformité | Module 5 | Axes 3 et 5 | 20 h
A6 | IA et données de santé | Projet fil rouge | Axes 1, 2 et 5 | 20 h
A7 | Méthodologie de recherche et reproductibilité | Tous | Tous | 15 h

A1 : Apprentissage fédéré avancé et vie privée (6 h cours, 14 h TP)
Prérequis : modules 1 et 4. Objectif : maîtriser la personnalisation, l'agrégation sécurisée et la mesure rigoureuse de la confidentialité.
Contenu du cours :
• Cross-silo (hôpitaux) contre cross-device (mobiles) : hypothèses, participation, fiabilité.
• Personnalisation face à l'hétérogénéité : modèles par client, couches personnalisées, apprentissage fédéré par groupes de clients similaires.
• Agrégation sécurisée : le serveur ne voit que la somme des mises à jour ; coût de communication et gestion des abandons.
• Comptabilité de la confidentialité : composition du budget (epsilon, delta) sur les tours, comptable des moments, confidentialité de Rényi.
• Attaques : inférence d'appartenance, reconstruction à partir des gradients, attaques de porte dérobée ; défenses associées.
• LoRA et confidentialité : alternance d'optimisation, effet du bruit sur A et B (lien avec l'axe 1).
TP : implémenter une agrégation sécurisée simplifiée par masquage, mesurer l'effet d'une attaque d'inférence d'appartenance avant et après DP-SGD, comparer FedProx et un modèle personnalisé sur données non-i.i.d.
Évaluation : rapport d'expériences reproductible, avec courbe confidentialité-utilité.

A2 : Graphes de connaissances et raisonnement (6 h cours, 14 h TP)
Prérequis : module 2. Objectif : construire, interroger et faire évoluer des graphes de qualité, et décider quand le graphe apporte vraiment quelque chose.
Contenu du cours :
• Langages et standards : RDF, OWL, SPARQL, validation de schéma (SHACL).
• Plongements de graphes et complétion de relations manquantes.
• Réseaux de neurones sur graphes appliqués à la récupération.
• Construction automatique par modèle de langage : qualité, couverture, résolution d'entités, mise à jour incrémentale.
• Évaluation de GraphRAG : lignes de base, tâches simples contre multi-sauts, latence, couverture du graphe (lien avec l'axe 2).
• Pondération adaptative de alpha, beta, gamma selon le type de requête.
TP : requêtes SPARQL sur l'ontologie médicale simulée, mesure de la couverture du graphe construit, routeur entre RAG simple et GraphRAG, comparaison chiffrée.
Évaluation : étude comparative RAG contre GraphRAG sur le corpus du projet.

A3 : Systèmes d'IA agentiques et inférence à grande échelle (6 h cours, 14 h TP)
Prérequis : module 3. Objectif : passer de la passerelle du module 3 à un système de production performant et sûr.
Contenu du cours :
• Serving de modèles : batching continu, cache clé-valeur de l'attention, décodage spéculatif, gestion de la mémoire.
• Orchestration multi-agents : décomposition de tâches, mémoire, coordination, arrêt et reprise.
• Outils et protocoles d'intégration, principe du moindre privilège, validation des appels.
• Observabilité : traces, évaluation continue, détection de dérive de qualité.
• Coût et latence : budgets, files d'attente, routage dynamique entre modèles.
• Sécurité des agents : injection indirecte via les outils et la mémoire (lien avec A5).
TP : ajouter traçage et métriques à la passerelle, mettre en place une évaluation automatique de régression, simuler une montée en charge.
Évaluation : rapport de performance (p50, p95, p99, coût par requête) et revue d'architecture.

A4 : Compression, PEFT avancé et déploiement Edge (6 h cours, 14 h TP)
Prérequis : module 4. Objectif : déployer des modèles adaptés sur des appareils contraints, en maîtrisant le compromis précision, mémoire et énergie.
Contenu du cours :
• Quantification des poids et des activations, quantification combinée à LoRA.
• Élagage et distillation de connaissances.
• Variantes de LoRA : choix du rang par couche, adaptation d'un sous-ensemble de modules, parcimonie des adaptateurs.
• Formats et moteurs d'exécution embarqués ; profilage mémoire, latence et énergie.
• Fédéré sur appareils hétérogènes : clients à capacités différentes, stratégies de participation (lien avec l'axe 4).
TP : quantifier un petit modèle et mesurer la perte de précision, comparer plusieurs rangs et précisions, produire un profil mémoire de bout en bout.
Évaluation : tableau de compromis et recommandation de configuration pour un appareil cible donné.

A5 : IA de confiance : attaques, audit et conformité (6 h cours, 14 h TP)
Prérequis : module 5. Objectif : évaluer et documenter la sécurité et la conformité d'un système d'IA.
Contenu du cours :
• Menaces sur les modèles : exemples adverses, empoisonnement, extraction de modèle, inférence d'appartenance, fuite de données d'entraînement.
• Red teaming : méthodologie, jeux d'attaques, mesure du taux de réussite, attaques adaptatives contre les guardrails.
• Évaluation de sécurité et de robustesse : métriques, intervalles de confiance, reproductibilité.
• Gouvernance : documentation des modèles et des données, traçabilité, journalisation sans données personnelles.
• Cadre réglementaire : RGPD et cadre européen sur l'IA, classification par niveau de risque, obligations pour les systèmes de santé.
TP : conduire un red teaming sur le pipeline du module 5, rédiger un dossier d'audit complet (modèle fourni avec le projet fil rouge).
Évaluation : dossier d'audit et défi inter-équipes.

A6 : IA et données de santé (6 h cours, 14 h TP)
Prérequis : modules 1 et 2 ; recommandé : A1 ou A2. Objectif : comprendre les spécificités du domaine médical pour concevoir un système réaliste.
Contenu du cours :
• Standards d'interopérabilité (FHIR, HL7) et terminologies cliniques (SNOMED CT, CIM-10).
• Qualité et biais des données médicales : déséquilibres, mesures manquantes, différences entre établissements.
• Évaluation clinique des modèles : sensibilité, spécificité, calibration, équité entre sous-populations.
• Contraintes éthiques et juridiques : secret médical, consentement, hébergement des données de santé.
• Explicabilité et traçabilité des réponses : citer les triplets et sources utilisés (lien avec GraphRAG).
TP : transformer des dossiers simulés au format FHIR, aligner le graphe du projet sur une terminologie, mesurer l'équité d'un modèle fédéré entre trois établissements simulés.
Évaluation : note technique sur la validité clinique et les risques du système du projet fil rouge.

A7 : Méthodologie de recherche et reproductibilité (5 h cours, 10 h TP)
Objectif : donner les outils pour mener et publier une expérience fiable.
Contenu : lecture critique d'un article, formulation d'une question de recherche, conception de protocole et d'ablations, statistiques de base (variance entre graines, intervalles de confiance, tests de comparaison), gestion de code et de données, rédaction scientifique.
TP : reproduire un résultat publié, documenter l'écart, rédiger un rapport technique de quatre pages.
Évaluation : rapport de reproduction.

Parcours conseillés
Parcours | Électifs recommandés | Profil visé
Vie privée et systèmes distribués | A1 + A5 | Ingénieur confidentialité, sécurité des données
Connaissances et recherche d'information | A2 + A3 | Ingénieur RAG, architecte de systèmes de connaissances
Edge et efficacité | A4 + A3 | Ingénieur IA embarquée, MLOps
IA de santé | A6 + A1 ou A2 | Ingénieur IA pour la santé numérique
Recherche | A7 + un électif au choix | Poursuite en doctorat ou en laboratoire

Liens avec le tronc commun et le projet
• Chaque électif réutilise le code produit dans le module qu'il prolonge, ce qui évite de repartir de zéro.
• Le projet fil rouge propose une variante par parcours : l'équipe approfondit un axe (par exemple agrégation sécurisée pour A1, couverture et latence du graphe pour A2) en plus du socle commun.
• Les travaux d'électifs les plus solides alimentent le dépôt de reproductibilité et le séminaire de veille de la feuille de route R&D.

Impact horaire et à valider
• Volume ajouté : 40 h pour deux électifs de 20 h ; A7 compte 15 h.
• Les prérequis, durées et contenus sont des propositions : à ajuster selon le calendrier du master, les enseignants disponibles et le matériel (appareils pour A4).
• Les standards et terminologies cités (FHIR, HL7, SNOMED CT, CIM-10, OWL, SPARQL, SHACL) sont réels mais leur usage en TP dépend des licences et jeux de données accessibles.

© 2026 Pixel Software Design. Tous droits réservés."""

IA_DONNEES_SYSTEMES_TEXT = r"""Pixel Software Design — Département de Recherche & Développement
PIXEL SOFTWARE DESIGN
Département de Recherche & Développement
Intelligence Artificielle Avancée & Federated Learning

• Fondations de l'intelligence artificielle
• Algorithmes d'apprentissage fédéré
• Confidentialité, attaques et défenses
• Applications et grands modèles fédérés
• Framework FedX de référence
• Nouveaux fronts de recherche
• Travaux pratiques, projets et évaluation

Auteur Ghiloufi Jamel
Fonction Architecte Logiciel Principal
Direction Département de Recherche & Développement
Service R&D - Intelligence Artificielle Avancée & Apprentissage Fédéré
Niveau Recherche
Édition Édition 2026 — 1.0
Copyright © Pixel Software Design

Sommaire
Partie 1 — IA, Données et Systèmes Distribués
1.1 Apprentissage automatique : typologie et chaîne de production
1.2 Observabilité et supervision des systèmes
1.3 Calcul et analyse de graphes
1.4 Fouille de données
1.5 Systèmes Big Data et architectures distribuées

Partie Thème Contenu Compétence visée Durée
Partie 1 Fondations Statistique, optimisation, courbes d'apprentissage Comprendre et formaliser 2-3 semaines
Partie 2 Algorithmes FL FedAvg, convergence, hétérogénéité, système Implémenter et régler 3-4 semaines
Partie 3 Confidentialité DP, attaques, défenses, agrégation sécurisée Auditer et sécuriser 2-3 semaines
Partie 4 Applications FedLLM, santé, V2X, FedRL, TinyML, graphes Transposer à un domaine 3-4 semaines
Partie 5 Framework FedX Architecture, API, benchmarks, exploitation Industrialiser 2 semaines
Partie 6 Nouveaux fronts FedCL, FedCI, SNN, FedGL, feuille de route Ouvrir la recherche 2 semaines
Partie 7 TP et projets 9 labs, 5 projets, corrigés, évaluation Faire et rendre 4-6 semaines

Préface — Comment utiliser ce cours
Ce support est conçu pour un parcours de formation et de recherche couvrant l'ensemble de la chaîne de valeur de l'intelligence artificielle distribuée. Ce n'est pas un manuel de référence à lire d'un trait : c'est un manuel opératoire. Chaque chapitre alterne exposition, formalisation, mise en œuvre numérique et évaluation. Les listings sont complets et exécutables ; les tableaux comparatifs servent de grille de décision.

Public et prérequis : étudiants de master et de doctorat, ingénieurs IA, praticiens de la recherche appliquée. Prérequis : apprentissage automatique classique, algorithmique numérique, bases de probabilités.

Partie 1 — IA, Données et Systèmes Distribués
Les cinq piliers de la chaîne de valeur numérique. On part du modèle qui apprend, on passe à la mesure du système qui le sert, puis aux structures qui relient les entités, aux méthodes qui extraient des connaissances, et enfin aux architectures qui rendent l'ensemble possible à l'échelle.

Objectifs de la partie
• Distinguer une tâche d'apprentissage d'un outil, et choisir l'un avant l'autre.
• Concevoir une chaîne d'observabilité en tenant compte du volume, de la rétention et du coût.
• Implémenter et comparer un plus court chemin, une centralité et une détection de communauté.
• Extraire des règles d'association et juger leur intérêt par le support et la confiance.
• Concevoir un traitement par lots ou en flux, et justifier ce choix en latence et en exactitude.

Plan de la partie
1. Apprentissage automatique : typologie et chaîne de production
2. Observabilité et supervision des systèmes
3. Calcul et analyse de graphes
4. Fouille de données
5. Systèmes Big Data et architectures distribuées

Chapitre 1.1 — Apprentissage automatique : typologie et chaîne de production
Le choix de l'algorithme vient après le choix de la question. L'inverse est l'erreur la plus répandue.

La typologie : quatre questions, pas une liste d'outils. L'apprentissage automatique se classe selon la disponibilité des étiquettes, la nature de la sortie, et le moment où l'erreur est révélée.

Situations d'apprentissage :
• Supervisé, sortie continue (un nombre) — régression linéaire, forêt, réseau — question : quelle erreur coûte le plus cher ?
• Supervisé, sortie discrète (une classe) — régression logistique, SVM, arbre — question : quel est le coût d'un faux positif, d'un faux négatif ?
• Non supervisé, structure (des groupes) — k-moyens, densité, hiérarchique — question : le découpage obtenu est-il interprétable ?
• Non supervisé, compression (moins de dimensions) — ACP, voisinage — question : quelle variance faut-il vraiment garder ?
• Renforcement (une politique d'actions) — gradient de politique, recherche de politique — question : quelle récompense mesure-t-on réellement ?

Formules :
y = w^T x + b,  ŷ - y ⇒ w ← w - η (w^T x - y) x
p(y = 1 | x) = σ(w^T x + b),  σ(z) = 1/(1 + e^{-z})

La régression linéaire ajuste une droite. La régression logistique ajuste une probabilité : la sigmoïde borne la sortie entre zéro et un.

La réduction de dimension et la segmentation partagent la même question : que perdre en échange de ce qu'on gagne ? L'ACP maximise la variance conservée (linéaire, lisible) ; les méthodes de voisinage sont plus expressives et moins interprétables.

La chaîne de production d'un modèle (Algorithme 1) :
01 Recueillir, identifier la source, horodater chaque enregistrement. Contrôler la qualité : valeurs manquantes, doublons, valeurs aberrantes.
02 Corriger les erreurs de mesure connues par le métier.
03 Séparer en trois jeux disjoints, avant toute transformation.
04 Transformer : normalisation, encodage des catégories, réduction de dimension.
05 Entraîner sur le jeu d'entraînement, ajuster sur le jeu de validation.
06 Évaluer une seule fois sur le jeu de test, jamais avant.
07 Rendre reproductible : version des données, du code, de la configuration.
08 Déployer sous conteneur, surveiller, et prévoir le retour arrière.
Effort dominant : la préparation, pas l'entraînement. La ligne 4 est irremplaçable et presque toujours faite trop tard.

Gouvernance d'un modèle (Listing 1) : une version n'est acceptée que si elle améliore au moins une métrique globale, si aucune métrique de sous-groupe ne se dégrade au-delà du seuil, et si elle respecte les contraintes de coût et de latence. Le critère sur les sous-groupes est celui qu'on oublie le plus souvent. Un modèle peut gagner deux points de précision globale en dégradant sévèrement un groupe de dix pour cent de la population : la moyenne masque exactement ce qui doit être surveillé.

Le seuil de 0,5 n'a aucune signification en soi : il doit être choisi sur le jeu de validation, en fonction du coût relatif d'un faux positif et d'un faux négatif. C'est la seule décision qui demande un arbitrage métier, pas une mesure technique.

Exercice 1.1.1 : un modèle de crédit atteint 92 % de justesse sur l'ensemble de test, mais 71 % sur le plus petit groupe de population. L'exactitude globale est une moyenne pondérée par la taille de chaque groupe. Si le groupe minoritaire pèse dix pour cent de la population, la contribution de ses vingt et un points d'écart au score global est deux points. Il faut demander la décomposition complète par groupe et la taille de chaque groupe.

A retenir (1.1)
• La question précède l'algorithme, et le coût de l'erreur décide de la métrique.
• La séparation des jeux de données précède toute transformation, sinon l'estimation est optimiste.
• Une métrique globale masque les sous-groupes : la décomposition fait partie de la mesure.
• Le seuil de décision est un arbitrage métier, pas un paramètre technique.

Chapitre 1.2 — Observabilité et supervision des systèmes
Savoir si un système fonctionne est la moitié du travail. Savoir pourquoi il ne fonctionne pas est l'autre moitié.

La supervision historique consistait à interroger périodiquement un état. L'observabilité moderne répond à une question plus difficile : dans un système distribué, quelle est la cause de ce comportement observable ? Elle se construit sur trois signaux de nature et de coût très différents.

Signaux :
• Métrique : quel est le niveau et sa tendance ? Une valeur par fenêtre de temps — coût faible, on garde tout.
• Journal : que s'est-il passé à cet instant ? Un événement par ligne — coût élevé, on archive.
• Tracé : où le temps est-il passé ? Une portion par étape d'un parcours — coût très élevé, on échantillonne.
• Événement métier : l'activité a-t-elle un sens ? Un changement d'état métier — coût faible, très haute valeur.
• Profil de charge : où va la charge, et pour qui ? Une requête analysée — coût moyen, protection des données.

Tirage ou poussée : une décision structurante. Tirage : le collecteur interroge les cibles à intervalle fixe (mode par défaut). Poussée : l'agent envoie ses valeurs (indispensable derrière un pare-feu ou pour les systèmes à très forte dispersion). Trente secondes est un compromis usuel pour le délai de scrape. La rétention doit être dégressive.

Concevoir une règle d'alerte qui ne fatigue pas l'équipe : condition de durée (l'anomalie doit persister plus longtemps qu'un pic normal, par exemple deux minutes), fenêtre de calcul (taux d'erreur sur cinq minutes, et non sur la dernière requête), action liée à la gravité (avertissement pour surveillance, escalade vers un humain uniquement si la durée franchit un seuil). La meilleure mesure de la qualité d'un système d'alerte est le nombre d'alertes ignorées par semaine.

taux_erreur = (N_échec(Δ) / N_0(Δ)) ≥ s ∧ durée ≥ τ. Les deux conditions sont indissociables.

Du symptôme à la cause : la méthode des quatre questions :
• Symptôme : qu'est-ce qui est faux, vu de l'extérieur ?
• Changement : qu'est-ce qui a changé récemment ? (version, configuration, volume, dépendance)
• Périmètre : qui est affecté, et par quoi cela se distingue-t-il ?
• Cause : qu'est-ce qui explique simultanément le symptôme, le changement et le périmètre ?
Un identifiant de corrélation propagé dans toutes les couches vaut souvent davantage que n'importe quel tableau de bord supplémentaire.

Surveillance d'un modèle et surveillance d'un service : un service peut être parfaitement sain (latence normale, aucune erreur) et le modèle dégradé (réponses plus courtes, plus vagues, silencieusement biaisées). La supervision technique ne voit rien. Il faut surveiller la qualité séparément : distribution des entrées, taux de refus, longueur des réponses, et décomposition des métriques par groupe.

Travaux pratiques 1.1 — Superviser un service distribué de bout en bout (3 h, niveau intermédiaire) : exposer une métrique de latence par percentile et un compteur d'erreurs ; configurer la collecte en mode tirage ; écrire une règle d'alerte sur le taux d'erreur avec condition de durée ; construire un tableau de bord en trois volets (santé technique, santé de la qualité, répartition de la charge) ; éteindre un composant pendant deux minutes et consigner les délais ; rédiger la règle d'escalade.

Barème : l'alerte se déclenche exactement une fois sur la panne simulée (5 pts), le tableau de bord nomme le composant responsable en moins de deux minutes (3 pts), la procédure d'escalade nomme un responsable et un délai (2 pts).

A retenir (1.2)
• Métriques, journaux et tracés ont des coûts et des durées de conservation différents.
• Une alerte utile est une conjonction de seuil et de durée, jamais un dépassement instantané.
• Le nombre d'alertes ignorées par semaine mesure la qualité du système d'alerte.
• La qualité d'un modèle se surveille séparément de la santé technique du service.

Chapitre 1.3 — Calcul et analyse de graphes
Dès qu'une question porte sur des relations, la structure naturelle n'est pas la table mais le graphe.

G = (V, E), E ⊆ V × V, deg⁺(v) = |{(v,u) ∈ E}|
PR(v) = (1-α)/N + α Σ_{u→v} PR(u)/deg⁺(u)

Le plus court chemin : Dijkstra (on explore par coût croissant du chemin) et A* (on explore par coût estimé du chemin complet). A* est optimal si et seulement si son estimation du coût restant est admissible (jamais supérieure au coût réel). Une estimation qui surestime transforme A* en recherche gloutonne.

Mesures de centralité :
• Degré : combien de relations directes ? popularité brute, facilement trompeuse.
• PageRank : combien de voisins réputés ? influence propagée par le graphe orienté.
• Médiation : sur quels chemins ce sommet est-il indispensable ? goulot d'étranglement, pont entre communautés.
• Proximité : combien de chemins courts vers tous les autres ? position périphérique ou centrale.
• Communauté : quels sommets se ressemblent structurellement ? groupes denses à l'intérieur, clairs entre eux.

Le degré n'est presque jamais la bonne mesure. Un sommet très connecté peut n'être connu que d'un seul groupe. Ce qui compte, c'est la qualité des voisins, pas leur nombre. Pour la détection de fraude en transactions, la mesure utile est presque toujours la médiation : un compte intermédiaire qui apparaît sur les plus courts chemins entre plusieurs comptes est bien plus suspect qu'un compte très actif.

A retenir (1.3)
• Les questions de parcours et de relations exigent une structure de graphe, pas des jointures récursives.
• A* est optimal si et seulement si son estimation du coût restant est admissible.
• Le PageRank mesure une influence propagée, pas un nombre de relations.
• La médiation signale les sommets indispensables aux parcours, donc les goulots d'étranglement.

Chapitre 1.4 — Fouille de données
Extraire des connaissances ne signifie pas trouver des corrélations : cela signifie en trouver qui résistent à une vérification.

Classification : l'arbre comme langage de décision. Un arbre de décision est une suite de questions binaires. Le critère de choix de la question de premier rang est la réduction d'incertitude qu'elle procure.
Entropie(S) = -Σ_c (|S_c|/|S|) log2(|S_c|/|S|)
Gain(S, A) = Entropie(S) - Σ_v (|S_v|/|S|) Entropie(S_v)

Surapprentissage : un arbre sans contrainte mémorise chaque feuille d'entraînement. Les trois coupes principales : limiter la profondeur, imposer un nombre minimal d'exemples par feuille, élaguer les branches dont le gain est inférieur à un seuil. La forêt aléatoire construit des arbres sur des tirages aléatoires des variables et des exemples, puis moyenne leurs décisions. La dispersion d'un seul arbre devient une estimation de l'incertitude.

Segmentation : deux philosophies.
• K-moyens : minimise la dispersion autour de centroïdes ; groupes fixes à l'avance, forme sphérique, valeur d'initialisation critique. Impose une forme aux données.
• Densité : regroupe les zones denses séparées par du vide ; nombre de groupes découvert, non paramétrique, forme arbitraire, peut identifier et exclure le bruit. Sensible aux échelles de densité.
K-moyens suppose que les groupes sont compacts. Sur des données réelles en orbites concentriques, il échoue complètement.

Règles d'association (Apriori) :
support(A → B) = n(A ∪ B)/N
confiance(A → B) = n(A ∪ B)/n(A)
Le support mesure la fréquence de la co-occurrence, la confiance mesure la probabilité conditionnelle.

Juger une règle d'association, dans l'ordre :
1. Support : combien de transactions ? En dessous de la centaine, la règle n'a aucun usage statistique.
2. Confiance : le conséquent est-il réellement tiré par l'antécédent, ou seulement par sa fréquence propre ?
3. Levier : la confiance excède-t-elle nettement la fréquence du conséquent seul ? Seul test qui distingue une vraie règle d'un artefact de fréquence.
4. Négativité : le nombre de règles est un tsunami ; il faut un critère de sélection final.
5. Décision : une règle n'est un résultat que si elle déclenche une action mesurable et évaluable.

Détection d'anomalies : deux approches.
• Par densité (isolation des arbres) : mesure la rareté d'un point dans son voisinage ; simple, explicable, détecte l'inconnu ; sensible à l'échelle et à la densité.
• Par reconstruction (auto-encodeur) : reconstruit l'entrée et mesure l'écart ; capte des anomalies de forme complexe ; une anomalie fréquente dans l'entraînement devient normale.
Statistiquement, détecter une anomalie est aisé ; décider qu'elle doit déclencher une alerte relève du métier. Sans cette règle métier écrite, un système de détection produit un flux d'alertes que personne ne traite.

Travaux pratiques 1.2 — Panier de marché et détection d'anomalies (4 h, niveau avancé) : écrire le générateur d'itemsets fréquents par largeur croissante ; mesurer support, confiance et levier ; afficher la courbe de nombre de règles en fonction du seuil de support ; construire un score d'anomalie fondé sur la rareté locale ; répondre par écrit parmi les anomalies lesquelles justifient une enquête et sur quel critère métier.

Barème : la règle est justifiée par le levier (4 pts), le nombre de règles en fonction du seuil est expliqué (2 pts), l'analyse distingue ce qui est statistique et ce qui est décisionnel (4 pts).

A retenir (1.4)
• Un arbre se construit par gain maximal d'information et se contraint par élagage, profondeur minimale et taille de feuille.
• La dispersion d'une forêt aléatoire fournit une estimation d'incertitude qu'un arbre seul ne donne pas.
• K-moyens impose une forme aux groupes, la densité ne l'impose pas : le choix suit les données.
• Une règle d'association n'est exploitable qu'après le test du levier et un critère de sélection explicite.

Chapitre 1.5 — Systèmes Big Data et architectures distribuées
Distribuer n'est pas une optimisation de performance : c'est la condition pour accepter l'échelle, avec le prix de la cohérence.

Pourquoi distribuer, et à quel prix :
• Capacité de stockage extensible — la donnée est découpée, l'accès doit connaître la découpe.
• Débit d'écriture et de lecture — la charge doit être répartie sans déséquilibre.
• Tolérance à la panne — il faut détecter et reconstruire.
• Extensibilité linéaire — la coordination coûte, et son coût croît avec le nombre de machines.
• Isolation des charges — le partage de ressources crée des interférences imprévisibles.

Stockage : pourquoi la disposition en colonnes change tout.
• Stockage par lignes : une ligne complète est l'unité lue. Bon pour les mises à jour ponctuelles, coûteux pour l'analyse.
• Stockage par colonnes : seule la colonne demandée est lue, et les valeurs d'une même colonne se compressent très bien. C'est la disposition qui rend praticable l'analyse sur de grands volumes.
• Indexation : l'index accélère la sélection mais ralentit l'écriture.
• Partage : répartir par plage de clés met les écritures réparties, mais rend les parcours multi-clés plus coûteux.

Traitement : deux philosophies.
Critère Par lots En flux Choix pratique
• Latence : minutes à heures / millisecondes — le flux si l'action doit suivre l'événement.
• Exactitude : voit l'intégralité de la période / estimate, corrigée ensuite — le lot si le calcul doit être exact.
• Reprise : relance complète / reprise au point de reprise — le flux, si l'état est externalisé.
• Coût : bon pour de gros volumes / coût par unité plus élevé — lots pour l'historique, flux pour le direct.
• Complexité : faible / gestion d'état, temps d'événement — commencer par lots.
En pratique, les deux coexistent presque toujours : flux pour l'alerte immédiate, lots pour la consolidation exacte.

Traiter un flux : trois notions à décider avant d'écrire la première ligne :
• Fenêtre : par temps fixe (une minute) ou par nombre d'événements (les mille premiers) ?
• Temps d'événement : l'horodatage du capteur (peut être en retard) ou l'horodatage de réception (toujours juste).
• État : les traitements inhomogènes supposent de conserver un état au-delà d'un événement ; il doit être périodiquement sauvegardé.
L'erreur la plus courante consiste à traiter un flux comme un lot : sans fenêtre, chaque événement est traité seul et aucun agrégat n'est possible.

Cadre juridique de l'usage des données : finalité déterminée, base légale explicite, minimisation des données collectées, information des personnes concernées, droit d'opposition et d'effacement. Un entrepôt distribué n'améliore ni n'aggrave la conformité, il rend simplement l'incapacité à répondre à une demande de suppression beaucoup plus coûteuse — parce qu'il faut retrouver toutes les copies. C'est le premier argument à opposer avant de distribuer une donnée.

Projet — Concevoir une chaîne complète, de la source à la restitution (6 semaines, équipe de 3 à 5 étudiants) : une entreprise de logistique veut suivre ses véhicules, détecter les anomalies de conduite et produire un tableau de bord temps réel, tout en conservant un historique exact pour la facturation. Volume annuel de l'ordre de deux milliards d'enregistrements.
Missions : spécifier le schéma des événements ; choisir le découpage du stockage ; définir la fenêtre de temps et le temps d'événement du traitement de flux ; concevoir la consolidation exacte par lots ; écrire le plan de reprise après panne ; établir ce qu'il faut pour répondre à une demande d'effacement d'un conducteur.
Livrables : document d'architecture en cinq étages, schéma de découpage, plan de reprise après panne, note sur la conformité aux demandes d'effacement.
Évaluation : le jury vérifie trois points — le critère de découpage est justifié par le type de requête, la réconciliation entre flux et lots est explicite, et l'effacement est traité comme une contrainte de conception et non comme un verrou.

A retenir (1.5)
• La distribution achète de l'échelle et introduit de la coordination : le prix est à chiffrer avant.
• La disposition en colonnes rend praticable l'analyse, mais coûte à l'écriture.
• Par lots et en flux coexistent : flux pour l'alerte, lots pour la consolidation exacte.
• Une fenêtre, un temps d'événement et un état : trois décisions précèdent toute ligne de traitement de flux.
• L'effacement d'une donnée se paie en conception, pas en procédure d'urgence.

Index des figures et des tableaux
Figures : les trois signaux de l'observabilité et leur échelle ; architecture de supervision ; un graphe, ses trois lectures ; PageRank ; les quatre tâches de la fouille de données ; Apriori ; les cinq dimensions du Big Data ; architecture de référence en cinq étages ; traitement par lots contre traitement en flux.
Tableaux : situations d'apprentissage et algorithme ; métriques, journaux, tracés ; Dijkstra et A* ; quatre mesures, quatre questions ; K-moyens et densité ; anomalies par densité et par reconstruction ; ce que la distribution achète et ce qu'elle coûte ; par lots, en flux, ou les deux.

© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans autorisation écrite préalable de l'auteur.
Document généré automatiquement le 29/09/2026 — mise en page Pixel Software Design.
"""



ARCHITECTURES_IA_TEXT = r"""Pixel Software Design — Département de Recherche & Développement
PIXEL SOFTWARE DESIGN
Département de Recherche & Développement
Intelligence Artificielle
Avancée
& Federated Learning
•  Fondations de l'intelligence artificielle
•  Algorithmes d'apprentissage fédéré
•  Confidentialité, attaques et défenses
•  Applications et grands modèles fédérés
•  Framework FedX de référence
•  Nouveaux fronts de recherche
•  Travaux pratiques, projets et évaluation
Auteur
Ghiloufi Jamel
Fonction
Architecte Logiciel Principal
Direction
Département de Recherche & Développement
Service
R&D - Intelligence Artificielle Avancée & Apprentissage Fédéré
Niveau
Recherche
Édition
Édition 2026 — 1.0
Copyright
© Pixel Software Design
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou
diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans
autorisation écrite préalable de l'auteur.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
2
Copyright et mentions légales
Éditeur
Pixel Software Design
Auteur
Ghiloufi Jamel
Fonction
Architecte Logiciel Principal
Département
Département de Recherche & Développement
Intitulé
Intelligence Artificielle Avancée & Federated Learning
Sous-titre
Fondations mathématiques de l'apprentissage automatique, algorithmes fédérés,
protection de la vie privée, défense contre les attaques, grands modèles de langage
fédérés, systèmes embarqués, renforcement appris, applications critiques (santé,
V2X), plateforme de référence FedX et feuille de route de recherche.
Édition
Édition 2026 (version 1.0)
Langue
Français
Niveau
Recherche
Collection
Supports de formation et de recherche, Pixel Software Design
Droits d'auteur
© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation
ou diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite
sans autorisation écrite préalable de l'auteur.
Droits de l'auteur. Ghiloufi Jamel est l'auteur unique de l'ensemble du contenu scientifique, pédagogique et
technique de cet ouvrage. Toute adaptation, traduction, reproduction ou exploitation, y compris partielle, requiert
une autorisation écrite préalable.
Droits des tiers. Les algorithmes, modèles et travaux cités restent la propriété de leurs auteurs respectifs. Les
références employées figurent en fin d'ouvrage, ce qui permet de remonter au travail original pour toute
affirmation chiffrée.
Marques et licences externes. PyTorch, TensorFlow, Flower, Opacus, MONAI, scikit-learn et PySyft sont des
logiciels libres sous licences respectives (BSD, Apache 2.0, MIT). Leur usage dans ce document est purement
pédagogique et n'emporte aucune prescription commerciale.
Mentions relatives aux données et aux expérimentations
Document pédagogique à usage de formation interne. Les exemples de code fournis sont livrés à titre pédagogique
; les résultats numériques illustrés sont issus d'expérimentations conduites dans un cadre de recherche et ne
constituent pas des performances de production.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
3
Ce support synthétise les travaux de recherche du Département de Recherche & Développement de Pixel Software
Design sur l'intelligence artificielle distribuée, l'apprentissage fédéré, la protection de la vie privée et les systèmes
embarqués intelligents.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
4
Sommaire
Structure détaillée du cours
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 8
Partie 1 — Architectures d'IA : évolution, évaluation et perspectives
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 9
1.1 La frise des neuf générations
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 10
1.2 Générations 1 à 3 : convolution, récurrence, attention
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 11
1.3 Générations 4 à 6 : état, hybride, mélange d'experts
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 13
1.4 Générations 7 à 9 : agentique, neuromorphique, quantique
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 14
1.5 Évaluer une architecture
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 15
1.6 Acteurs du secteur et travaux fondateurs
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 18
Annexes
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 19
A.1 Liste des abréviations
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 19
A.2 Table de notation
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
5
Partie
Thème
Contenu
Compétence visée
Durée
Partie 1
Fondations
Statistique, optimisation, courbes d'apprentissage
Comprendre et formaliser
2-3 semaines
Partie 2
Algorithmes FL
FedAvg, convergence, hétérogénéité, système
Implémenter et régler
3-4 semaines
Partie 3
Confidentialité
DP, attaques, défenses, agrégation sécurisée
Auditer et sécuriser
2-3 semaines
Partie 4
Applications
FedLLM, santé, V2X, FedRL, TinyML, graphes
Transposer à un domaine
3-4 semaines
Partie 5
Framework FedX
Architecture, API, benchmarks, exploitation
Industrialiser
2 semaines
Partie 6
Nouveaux fronts
FedCL, FedCI, SNN, FedGL, feuille de route
Ouvrir la recherche
2 semaines
Partie 7
TP et projets
9 labs, 5 projets, corrigés, évaluation
Faire et rendre
4-6 semaines
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
6
Préface
Comment utiliser ce cours
Ce support est conçu pour un parcours de formation et de recherche couvrant l'ensemble de la chaîne de valeur de
l'intelligence artificielle distribuée : les fondations mathématiques, les algorithmes d'apprentissage fédéré, les
menaces et défenses, les applications de pointe, une plateforme de référence opérationnelle, et enfin les nouveaux
fronts ouverts par la recherche du Département.
Ce n'est pas un manuel de référence à lire d'un trait : c'est un manuel opératoire. Chaque chapitre alterne
exposition, formalisation, mise en œuvre numérique et évaluation. Les listings sont complets et exécutables ; les
tableaux comparatifs servent de grille de décision ; les schémas d'architecture servent de support de revue de
conception.
Public et prérequis
Le contenu s'adresse à des étudiants de master et de doctorat, à des ingénieurs IA et à des praticiens de la
recherche appliquée. Les prérequis sont la connaissance de l'apprentissage automatique classique, de
l'algorithmique numérique et des bases de probabilités. Les parties 1 à 3 sont auto-suffisantes pour un étudiant qui
découvre le domaine ; les parties 4 à 7 supposent la mécanique et les outils présentés dans la partie 2.
Conventions de lecture. Une expression mathématique est encadrée par deux signes dollars ; un identifiant, un
fichier ou une commande est écrit en caractères à chasse fixe ; les encadrés Définition, Théorème, Méthode et
Attention signalent les points à maîtriser et les pièges fréquents. Les renvois de la forme « voir chapitre 3.2 »
désignent le second chapitre de la troisième partie.
Progression pédagogique
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
7
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
8
De la convolution à l'auto-modélisation, et comment on les juge
Partie 1
Architectures d'IA : évolution,
évaluation et perspectives
Les architectures de l'intelligence artificielle se sont remplacées neuf fois en quinze ans, et chaque
remplacement a résolu un problème que la génération précédente ne savait pas traiter. Ce cours
retracé cette séquence, puis pose la seule question qui compte en production : sur quels critères
concrets juge-t-on une architecture, et comment ces critères changent-ils selon la contrainte
dominante — la latence, la mémoire, ou le coût.
Objectifs de la partie
• Situer les neuf générations et nommer la propriété que chacune ajoute.
• Expliquer pourquoi l'auto-attention a déplacé le coût du calcul vers la mémoire.
• Distinguer une architecture à état d'une architecture récurrente, et dire laquelle convient à quoi.
• Justifier le mélange d'experts par une contrainte de calcul, et non par une mode.
• Évaluer une architecture sur des critères mesurables plutôt que sur des performances annoncées.
• Distinguer ce qui est déployé, ce qui est en recherche, et ce qui relève de la spéculation.
Plan de la partie
1.  La frise des neuf générations
2.  Générations 1 à 3 : convolution, récurrence, attention
3.  Générations 4 à 6 : état, hybride, mélange d'experts
4.  Générations 7 à 9 : agentique, neuromorphique, quantique
5.  Évaluer une architecture
6.  Acteurs du secteur et travaux fondateurs
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
9
Chapitre 1.1
La frise des neuf générations
Figure 1 — Les neuf générations et ce que chacune ajoute
Gén.
Nom
Paradigme
Horizon
Force majeure
Statut
1
CNN
Locale (spatiale)
2012 – 2018
Vision par ordinateur
Absorbé 
par 
la 
vision
multimodale
2
RNN / LSTM
Séquentielle O(N)
2015 – 2019
Séries temporelles, audio
Obsolète pour le texte
3
Transformer
Quadratique O(N2)
2017 – présent
Contexte global, génération
Standard de l'industrie
4
SSM (Mamba)
Linéaire O(N)
2023 – présent
Vitesse, efficacité mémoire
Croissance forte (Edge)
5
Hybride et réflexion
Mixte + inférence
2024 – présent
Raisonnement poussé
Pointe de production
6
MoE et multimodal
Routage d'experts
2024 – présent
Efficacité à grande échelle
Standard industriel massif
7
Agentique et
neuromorphique
Distribué, bio-inspiré
2026 – futur proche
Autonomie, 
basse
consommation
Émergence et recherche
8
Quantique et
auto-récursif
Qubits, auto-modélisation
2030 et au-delà
Problèmes combinatoires
Recherche fondamentale
9
Holographique et
optique
Photonique, non localisé
2040 et au-delà
(hypothétique)
Résilience, 
absence 
de
latence
Spéculation théorique
Tableau 1 — Les neuf générations d'architectures
Chaque génération ne remplace pas la précédente : elle ajoute une propriété que la précédente ne pouvait
pas exprimer. C'est pourquoi les trois premières restent utilisées en production, chacune pour ce qu'elle fait
mieux.
A retenir
• Les générations s'ajoutent plus qu'elles ne se remplacent.
• Le coût de l'attention est passé du calcul vers la mémoire.
• L'état, l'hybride et le mélange d'experts répondent à des contraintes de mesure, pas de principe.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
10
• Générations 7 à 9 : ce sont des domaines de recherche, et doivent être lus comme tels.
Chapitre 1.2
Générations 1 à 3 : convolution, récurrence,
attention
Trois hypothèses sur la structure de la dépendance, et trois familles d'architectures qui en
découlent.
Figure 1 — Le coût comparé des trois hypothèses
Convolution
Récurrence
Attention
Hypothèse
la 
dépendance 
est 
locale 
et
stationnaire
la 
dépendance 
est 
strictement
ordonnée
la dépendance relie des positions
quelconques
Portée
limitée par la taille du noyau
limitée par la longueur de la
séquence
illimitée, 
dans 
la 
fenêtre 
du
contexte
Coût en séquence
O(N)
O(N)
O(N2)
Parallélisme à l'entraînement
par positions
séquentiel
total
Point faible
invariance par translation non
apprise
oubli sur les longues séquences
coût quadratique en mémoire
Terrain naturel
image, signal, audio
série temporelle, texte
texte, code, multimodal
Tableau 1 — Convolution, récurrence, attention : la question à laquelle chacune répond
Aucune des trois hypothèses n'est fausse : ce sont trois fausses bonnes idées pour trois régimes de données différents. Le
transformateur n'a pas rendu la convolution inutile ; il l'a rendue cantonnée à l'image.
Attention(Q, K, V) = softmax≤ft((Q K⊤)/(√(dk)) + M) V
Complexité = O≤ft(N2 d) mémoire, O≤ft(N2 d) calcul
(A.1)
Le facteur deux n'est pas un défaut d'implémentation mais une conséquence de l'hypothèse : si chaque position
peut regarder chaque autre position, il y a N au carré de relations possibles. Réduire ce coût exige de sacrifier
l'accès complet : par fenêtre, par échantillonnage, ou par approximation de bas rang.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
11
Le déplacement du goulot d'étranglement
Pendant la transition, le coût dominant de l'attention a changé de nature : le calcul de la matrice de scores est
became négligeable devant le stockage des clés et des valeurs. Les architectures materialisées puis fenêtrées ne
visent pas à réduire le calcul, mais la mémoire. C'est pourquoi les techniques d'attention efficace sont presque
toutes des techniques de gestion de la mémoire, et non du calcul.
Astuce
Le choix se fait sur la contrainte, jamais sur l . Un contexte long exige l'attention ; une latence de quelques
millisecondes sur un capteur impose l'état ; une séquence très courte et fortement bruitée tolère mieux une règle
fixe qu'un modèle appris.
A retenir
• Les trois hypothèses de structure donnent trois architectures, et chacune excelle sur son terrain.
• L'attention paie son coût en mémoire avant de le payer en calcul.
• Les architectures matérialisées et fenêtrées visent la mémoire, pas le calcul.
• Le choix se fait sur la contrainte dominante, jamais sur l pertain du procédé.
Chapitre 1.3
Générations 4 à 6 : état, hybride, mélange
d'experts
Trois réponses à la même question : comment tenir la longueur de contexte sans la payer en
mémoire ?
• État d'espace : un vecteur d'état de taille fixe remplace la séquence. Le coût devient linéaire en
longueur, au prix d'un compresseur appris. La perte est réelle : deux contextes distincts peuvent produire
le même état.
• Hybride et réflexion : on alterne une phase de raisonnement longue et une phase de révision.
L'aller-retour coûte deux à trois fois plus qu'un passage direct, et gagne en exactitude sur les tâches où la
première réponse était fausse.
• Mélange d'experts : plusieurs réseaux specialized, un routeur qui choisit lesquels activer. La qualité
s'approche de celle d'un modèle bien plus grand, pour un coût de calcul proche d'un modèle petit. C'est
de loin le meilleur rapport gain / coût actuellement disponible.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
12
Figure 1 — Le mélange d'experts et la fonction de routage
y = ∑i=1
k gi(x) Ei(x), ∑i gi(x) = 1, gi(x) ≥ 0
Coût(x) = ∑i gi(x) Coût(Ei(x))
(A.2)
La seconde expression est la raison économique du mélange : le coût est celui des experts activés, non celui de la
somme. Le routeur devient donc le point critique — un routeur mal entraîné coûte plus cher que le modèle entier,
parce qu'il active trop d'experts et perd les deux avantages à la fois.
État d'espace
Hybride
Mélange d'experts
Gain principal
coût linéaire en longueur
exactitude 
sur 
les 
tâches
complexes
qualité / coût
Coût caché
compression de l'information
deux 
à 
trois 
passages 
par
question
routeur et déséquilibre d'activation
Sensitive à la longueur
très
moyenne
faible
Difficulté de mise en œuvre
moyenne
faible
moyenne
Maturité industrielle
en croissance
en croissance
déployé à grande échelle
Tableau 1 — État, hybride, mélange : comparaison opérationnelle
Le mélange d'experts est le plus mûr des trois, et le moins coûteux : son coût de migration est essentiellement nul,
puisqu'il s'applique à un modèle existant sans changer son interface.
Le routeur qui dégrade le mélange
Un routeur entraîné sur une distribution de requêtes ne fonctionne pas sur une autre, et le symptôme n'est pas
une erreur visible : c'est une activation excessive. Le modèle active six experts sur huit, se rapproche de son coût
complet, et perd le bénéfice du mélange sans que la qualité chute. Surveiller le nombre d'experts actifs est un
indicateur de surveillance, pas un détail d'implémentation.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
13
A retenir
• État, hybride et mélange répondent à la même contrainte : tenir la longueur sans payer la mémoire.
• Le mélange d'experts est le meilleur rapport gain / coût disponible, parce que le coût ne suit que les experts
activés.
• Le routeur est le point critique : une activation excessive annule les deux avantages.
• Surveiller le nombre d'experts actifs est un indicateur de production.
Chapitre 1.4
Générations 7 à 9 : agentique,
neuromorphique, quantique
Trois domaines de recherche. Les lire comme tels est déjà une compétence professionnelle.
Les trois générations suivantes ne sont pas des improvesments incrémentaux : ce sont des programmes de
recherche qui répondent à des limites structurelles de l'architecture actuelle. Les présenter comme des
technologies disponibles conduit à des décisions d'investissement erronées.
Génération
Promesse
Obstacle principal
Statut
Agentique
un système qui planifie et agit
fiabilité sur les actions longues, coût
déploiement 
encadré, 
pas
autonomie générale
Neuromorphique
consommation réduite d'un à trois
ordres
entraînement et outillage immature
recherche et quelques pilotes
industriels
Quantique
accélération de problèmes spécifiques
aucun avantage établi sur une tâche
d'IA
recherche 
fondamentale, 
sans
application
Auto-récursif
le modèle améliore son propre code
vérification, 
coût, 
boucle 
de
degeneration
recherche, résultats préliminaires
Holographique et optique
mémoire et calcul photoniques
intégration, précision, adressage
spéculation théorique
Tableau 1 — Générations 7 à 9 : statut réel et ce qu'elles promettent
La ligne quantique mérite d'être lue attentivement : l'apprentissage automatique quantique est un domaine de recherche
sans application industrielle établie à ce jour. Citer un avantage quantique démontré sur une tâche concrète serait
inexact.
Un document prospectif sur l'intelligence artificielle se lit en séparant trois registres : ce qui est déployé
aujourd'hui, ce qui est en recherche expérimentale, et ce qui relève de la spéculation. Un critère simple : si
l'affirmation ne peut pas être testée par une expérience publiée et reproductible, elle relève du troisième
registre.
Précaution de lecture sur les prévisions
Astuce
La question utile devant une promesse de génération future n'est jamais « est-ce vrai ? » mais « quelle contrainte
actuelle rouvrirait-elle, et qui la finances ? ». Une génération qui ne rouvre aucune contrainte connue n'est pas
une génération, c'est un thème.
A retenir
• Générations 7 à 9 : programmes de recherche, pas technologies disponibles.
• L'apprentissage automatique quantique n'a aujourd'hui aucune application industrielle établie.
• Lire un document prospectif suppose de séparer trois registres : déployé, recherché, spéculatif.
• La question utile est « quelle contrainte rouvre-t-elle », pas « est-ce vrai ».
Chapitre 1.5
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
14
Évaluer une architecture
Figure 1 — Les quatre familles de critères d'évaluation
Évaluer une architecture revient à choisir un jeu de critères qui correspondent à la contrainte dominante.
Comparer deux architectures sans avoir déclaré la contrainte revient à comparer deux réponses à deux
questions différentes.
Famille
Mesures
Ce qu'elle décide
Piège
Qualité
exactitude, robustesse, calibration
le modèle est-il bon en général
mesurée sur une distribution qui
ressemble au test
Coût
paramètres, 
mémoire 
d'inférence,
énergie par requête
quelle machine, et quel budget
ignoré au profit du nombre de
paramètres seul
Latence
temps 
au 
premier 
jeton, 
débit,
variance
l'usage est-il interactif ou différé
mésurée en médiane, jamais au 99e
centile
Exploitabilité
données requises, domaine de validité,
dépendance de version
peut-on l'exploiter à l'échelle
oubliée, et découverte en production
Tableau 1 — Quatre familles de critères et ce qu'elles tranchent
La famille « exploitabilité » est la plus négligée et la plus coûteuse. Un excellent modèle exigeant une donnée rare est, en
pratique, un modèle non déployable.
Coûtreq = cmem · mémoire + ccalc · FLOPs + cio · octets lus
Latencep99 = q0,99≤ft(durée)
(A.3)
La première expression rappelle que le coût d'une requête n'est pas le nombre de multiplications : c'est la
somme des accès mémoire et des entrées-sorties, et sur un accélérateur ces deux postes dominent. La seconde
rappelle qu'une latence annoncée en médiane ne décrit pas le comportement perçu par un utilisateur.
Conduire une comparaison d'architectures en cinq temps
• Écrire la contrainte dominante en une phrase. Latence, mémoire, qualité, coût, ou domaine de validité. Pas
de réponse valide sans cette phrase.
2. Fixer le jeu de données d'évaluation avant de voir les résultats. Un jeu choisi après est un jeu favorable.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
15
3. Mesurer les quatre familles, même si la réponse paraît évidente. C'est la mesure qui évite les mauvaises
surprises.
4. Comparer à coût égal, pas à taille égale. Un modèle deux fois plus grand n'est pas deux fois meilleur ; il
faut comparer à paramètres constants.
5. Tester hors distribution. Un gain obtenu sur le jeu d'évaluation ne vaut rien s'il s'effondre sur des entrées
légitimes mais non couvertes.
Exercice 1.5.1  (difficulte : Moyen)
Deux modèles obtiennent la même exactitude sur le jeu d'évaluation. Le premier a 7 milliards de paramètres
et exige 16 gigaoctets de mémoire d'inférence. Le second en a 3 milliards et en exige 4 gigaoctets. Le service
doit répondre en moins de 300 millisecondes sur un matériel disposant de 8 gigaoctets. Quel modèle retenir,
et que manque-t-il à la comparaison ?
Indice : Deux questions distinctes : la faisabilité matérielle et la mesure de la latence.
Correction
• Le second modèle, sans discussion : le premier ne tient pas sur le matériel disponible, et c'est une élimination
avant toute autre consideration. La comparaison reste pourtant incomplète : l'égalité des exactitudes ne dit
rien de la latence, de la variance, ni de la robustesse hors distribution. Il manque au minimum la latence au
99e centile, le débit soutenu sous charge, et un test de dégradation hors distribution. Une égalité d'exactitude
sur un jeu de validation est le point de départ de la comparaison, jamais son conclusion.
A retenir
• Évaluer une architecture suppose d'abord d'écrire la contrainte dominante en une phrase.
• Le coût d'une requête est dominé par la mémoire et les entrées-sorties, pas par les multiplications.
• Une latence annoncée en médiane ne décrit pas le comportement perçu : il faut le 99e centile.
• L'exploitabilité — données requises, domaine de validité — est la famille de critères la plus négligée.
• Comparer deux architectures à taille égale n'a pas de sens : il faut comparer à coût égal.
Chapitre 1.6
Acteurs du secteur et travaux fondateurs
Repérer les travaux qui font référence, et savoir quand ils ont été corrigés ou dépassés.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
16
Figure 1 — Les travaux fondateurs et leur portée réelle
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
17
Travail
Apport
Statut actuel
AlexNet, 2012
profondeur et accélération matérielle sur la vision
travail de référence, dépassé par l'architecture
Attention Is All You Need, 2017
l'attention seule suffit à
le papier le plus cité du domaine, toujours
valide
LSTM, 1997
mémoire à porte d'oubli dans la récurrence
utilisé hors texte, remplacé sur le texte
Mixture of Experts, 1971
routage vers des spécialistes
principe ancien, mise en œuvre récente et
déployée
Scaling Laws, 2020
lois d'échelle en données et calcul
utilisées pour dimensionner, discutées sur leurs
limites
Mixture of Depths, 2024
calcul conditionné à la profondeur
prometteur, déploiement limité
Tableau 1 — Travaux fondateurs, ce qu'ils ont établi, et leur statut
Le principe du mélange d'experts précède de quarante-six ans son usage industriel. Rappeler cette antériorité est utile :
elle montre que l'innovation est souvent dans la mise en œuvre à l'échelle, pas dans l'idée.
Ce que la bibliographie ne dit pas
Citer un travail fondateur sans indiquer la version consultée, la configuration expérimentale et les limites
déclarées par les auteurs produit une bibliographie trompeuse. Un travail de recherche est un document daté,
dans un état daté, et les résultats sont reproductibles ou ne le sont pas. La mention d'une version ou d'un
identifiant de dépôt fait partie de la référence.
Astuce
La question la plus rentable devant une architectureIRC éditée : quels résultats l'article rapporte-t-il, et quels
résultats ne rapporte-t-il pas ? Le second point est presque toujours plus informatif que le premier.
A retenir
• Le mélange d'experts précède de quarante-six ans sa mise en œuvre industrielle : l'innovation est souvent dans
l'échelle.
• Un travail de recherche est un document daté, dans un état daté, reproductible ou non.
• Ce qu'un article ne rapporte pas est plus informatif que ce qu'il rapporte.
• La référence complète inclut la version, la configuration et les limites déclarées.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
18
Abréviations, notation et ressources de consultation
Annexes
Annexes
Ce cours se termine par deux annexes de référence. La première donne la signification de chaque sigle
employé, sous les deux formes — sigle et développé — car la litterature emploie indifféremment l'une
ou l'autre. La seconde donne la signification de chaque symbole mathématique : elle permet de relire
une démonstration sans revenir au chapitre dont elle est extraite, et de vérifier qu'un même symbole
garde le même sens d'un chapitre à l'autre.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
19
Chapitre A.1
Liste des abréviations
Les sigles ci-dessous sont ceux que le cours emploie. Chacun est donné avec sa forme développée
et le sens précis qu'il prend ici, qui n'est pas toujours celui qu'on lui donne ailleurs.
Un sigle employé sans être développé oblige le lecteur à le reconnaître au passage, ou à l'abandonner. Le
tableau ci-dessous ferme la liste de ceux que le cours emploie : il est exhaustif pour ce document, et non
pour la discipline.
Sigle
Forme développée
Sens dans ce cours
CNN
Convolutional Neural Network
Réseau convolutif : première génération, reconnaissance d'images.
GNN
Graph Neural Network
Réseau de convolution sur graphe, qui propage l'information selon
l'adjacence.
LSTM
Long Short-Term Memory
Cellule récurrente à mémoire longue, deuxième génération.
MoE
Mixture of Experts
Mélange d'experts : un sous-réseau par jeton, un seul étant activé.
MoT
Mixture of Tokens
Mélange opéré au niveau du jeton, et non de l'expert.
Mamba
Modèle à convolution sélective
Couche d'espace d'état à balayage sélectif, de coût linéaire en longueur.
RNN
Recurrent Neural Network
Réseau récurrent, qui lit une séquence dans l'ordre.
SSM
State Space Model
Modèle d'espace d'état, quatrième génération.
Transformer
Modèle à mécanisme d'attention
Troisième génération, devenue le standard de l'industrie.
ViT
Vision Transformer
Transformer appliqué à l'image, par découpage en jetons.
xLSTM
Extended Long Short-Term Memory
Cellule récurrente révisée, dont les opérations sont parallélisables.
Tableau 1 — Abréviations employées dans le cours
Chapitre A.2
Table de notation
Les symboles ci-dessous gardent le même sens d'un chapitre à l'autre. Lorsqu'un chapitre doit
réemployer un symbole pour un autre objet, il le redéclare sur la page même.
La notation est celle du cours : vecteurs en gras, matrices en majuscules grasses, scalaires en italique. Les
espérances sont notées E, les lois de données D, les espaces de paramètres Θ.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
20
Symbole
Signification
N
Longueur de la séquence traitée.
dmodel
Dimension du modèle, celle de chaque représentation.
dk
Dimension d'une clé, puis d'une tête d'attention.
dv
Dimension d'une valeur.
H
Nombre de têtes d'attention.
Q
Matrice des requêtes, pour la i-ième tête d'attention.
K
Matrice des clés, dont l'attention pondère les valeurs.
V
Matrice des valeurs, que l'attention combine.
Attention(Q,K,V)
Sortie d'un bloc d'attention, après masquage causal.
O(N)
Complexité linéaire en la longueur de la séquence.
O(N2)
Complexité quadratique, celle de l'attention dense.
FLOPs
Nombre d'opérations en virgule flottante, mesure du coût de calcul.
MAC
Multiplications-accumulations, unité de mesure matérielle du coût.
α
Efficience, rapport du travail utile au travail total.
K
Nombre d'experts actifs dans un mélange d'experts.
g(x)
Fonction de routage, qui désigne l'expert d'un jeton.
h
Nombre de tours de récurrence, ou hauteur d'un réseau.
Tableau 1 — Symboles mathématiques et leur signification
Convention
Toute divergence constatée entre cette table et un chapitre signale une erreur de transcription, non une
définition nouvelle : la table fait foi.
A retenir
• Un sigle employé sans être listé ici est un oubli de l'auteur, non une définition nouvelle.
• Un symbole qui change de sens d'un chapitre à l'autre rend toute démonstration ininterprétable : c'est la
principale cause des contresens que nous avons relevés.
• Ces deux tables sont les seules parties du cours à maintenir à la main : le reste se relit tout seul.
Index des figures et des tableaux
Référence rapide du matériel visuel
Figures
1.  Les neuf générations et ce que chacune ajoute
1.  Le coût comparé des trois hypothèses
1.  Le mélange d'experts et la fonction de routage
1.  Les quatre familles de critères d'évaluation
1.  Les travaux fondateurs et leur portée réelle
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
21
Tableaux
1.  Les neuf générations d'architectures
1.  Convolution, récurrence, attention : la question à laquelle chacune répond
1.  État, hybride, mélange : comparaison opérationnelle
1.  Générations 7 à 9 : statut réel et ce qu'elles promettent
1.  Quatre familles de critères et ce qu'elles tranchent
1.  Travaux fondateurs, ce qu'ils ont établi, et leur statut
1.  Abréviations employées dans le cours
1.  Symboles mathématiques et leur signification
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
22
Fin du document
Intelligence Artificielle Avancée & Federated Learning — Fondations mathématiques de
l'apprentissage automatique, algorithmes fédérés, protection de la vie privée, défense contre les attaques,
grands modèles de langage fédérés, systèmes embarqués, renforcement appris, applications critiques
(santé, V2X), plateforme de référence FedX et feuille de route de recherche.<br/>Ghiloufi Jamel,
Architecte Logiciel Principal — Pixel Software Design<br/>Département de Recherche & Développement
— Recherche<br/>Pixel Software Design — Édition 2026
© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou
diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans
autorisation écrite préalable de l'auteur.
Document généré automatiquement le 29/09/2026 — mise en page Pixel Software Design.
"""


INTRODUCTION_IA_TEXT = r"""Pixel Software Design — Département de Recherche & Développement
PIXEL SOFTWARE DESIGN
Département de Recherche & Développement
Intelligence Artificielle
Avancée
& Federated Learning
•  Fondations de l'intelligence artificielle
•  Algorithmes d'apprentissage fédéré
•  Confidentialité, attaques et défenses
•  Applications et grands modèles fédérés
•  Framework FedX de référence
•  Nouveaux fronts de recherche
•  Travaux pratiques, projets et évaluation
Auteur
Ghiloufi Jamel
Fonction
Architecte Logiciel Principal
Direction
Département de Recherche & Développement
Service
R&D - Intelligence Artificielle Avancée & Apprentissage Fédéré
Niveau
Recherche
Édition
Édition 2026 — 1.0
Copyright
© Pixel Software Design
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou
diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans
autorisation écrite préalable de l'auteur.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
2
Copyright et mentions légales
Éditeur
Pixel Software Design
Auteur
Ghiloufi Jamel
Fonction
Architecte Logiciel Principal
Département
Département de Recherche & Développement
Intitulé
Intelligence Artificielle Avancée & Federated Learning
Sous-titre
Fondations mathématiques de l'apprentissage automatique, algorithmes fédérés,
protection de la vie privée, défense contre les attaques, grands modèles de langage
fédérés, systèmes embarqués, renforcement appris, applications critiques (santé,
V2X), plateforme de référence FedX et feuille de route de recherche.
Édition
Édition 2026 (version 1.0)
Langue
Français
Niveau
Recherche
Collection
Supports de formation et de recherche, Pixel Software Design
Droits d'auteur
© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation
ou diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite
sans autorisation écrite préalable de l'auteur.
Droits de l'auteur. Ghiloufi Jamel est l'auteur unique de l'ensemble du contenu scientifique, pédagogique et
technique de cet ouvrage. Toute adaptation, traduction, reproduction ou exploitation, y compris partielle, requiert
une autorisation écrite préalable.
Droits des tiers. Les algorithmes, modèles et travaux cités restent la propriété de leurs auteurs respectifs. Les
références employées figurent en fin d'ouvrage, ce qui permet de remonter au travail original pour toute
affirmation chiffrée.
Marques et licences externes. PyTorch, TensorFlow, Flower, Opacus, MONAI, scikit-learn et PySyft sont des
logiciels libres sous licences respectives (BSD, Apache 2.0, MIT). Leur usage dans ce document est purement
pédagogique et n'emporte aucune prescription commerciale.
Mentions relatives aux données et aux expérimentations
Document pédagogique à usage de formation interne. Les exemples de code fournis sont livrés à titre pédagogique
; les résultats numériques illustrés sont issus d'expérimentations conduites dans un cadre de recherche et ne
constituent pas des performances de production.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
3
Ce support synthétise les travaux de recherche du Département de Recherche & Développement de Pixel Software
Design sur l'intelligence artificielle distribuée, l'apprentissage fédéré, la protection de la vie privée et les systèmes
embarqués intelligents.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
4
Sommaire
Structure détaillée du cours
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 8
Partie 1 — Introduction et définitions fondamentales
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 9
1.1 Qu'est-ce que l'intelligence artificielle ?
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 12
1.2 Historique et évolution
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 14
1.3 Le fonctionnement du machine learning
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 17
1.4 Applications pratiques et enjeux éthiques
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 21
Annexes
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 22
A.1 Liste des abréviations
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 22
A.2 Table de notation
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
5
Partie
Thème
Contenu
Compétence visée
Durée
Partie 1
Fondations
Statistique, optimisation, courbes d'apprentissage
Comprendre et formaliser
2-3 semaines
Partie 2
Algorithmes FL
FedAvg, convergence, hétérogénéité, système
Implémenter et régler
3-4 semaines
Partie 3
Confidentialité
DP, attaques, défenses, agrégation sécurisée
Auditer et sécuriser
2-3 semaines
Partie 4
Applications
FedLLM, santé, V2X, FedRL, TinyML, graphes
Transposer à un domaine
3-4 semaines
Partie 5
Framework FedX
Architecture, API, benchmarks, exploitation
Industrialiser
2 semaines
Partie 6
Nouveaux fronts
FedCL, FedCI, SNN, FedGL, feuille de route
Ouvrir la recherche
2 semaines
Partie 7
TP et projets
9 labs, 5 projets, corrigés, évaluation
Faire et rendre
4-6 semaines
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
6
Préface
Comment utiliser ce cours
Ce support est conçu pour un parcours de formation et de recherche couvrant l'ensemble de la chaîne de valeur de
l'intelligence artificielle distribuée : les fondations mathématiques, les algorithmes d'apprentissage fédéré, les
menaces et défenses, les applications de pointe, une plateforme de référence opérationnelle, et enfin les nouveaux
fronts ouverts par la recherche du Département.
Ce n'est pas un manuel de référence à lire d'un trait : c'est un manuel opératoire. Chaque chapitre alterne
exposition, formalisation, mise en œuvre numérique et évaluation. Les listings sont complets et exécutables ; les
tableaux comparatifs servent de grille de décision ; les schémas d'architecture servent de support de revue de
conception.
Public et prérequis
Le contenu s'adresse à des étudiants de master et de doctorat, à des ingénieurs IA et à des praticiens de la
recherche appliquée. Les prérequis sont la connaissance de l'apprentissage automatique classique, de
l'algorithmique numérique et des bases de probabilités. Les parties 1 à 3 sont auto-suffisantes pour un étudiant qui
découvre le domaine ; les parties 4 à 7 supposent la mécanique et les outils présentés dans la partie 2.
Conventions de lecture. Une expression mathématique est encadrée par deux signes dollars ; un identifiant, un
fichier ou une commande est écrit en caractères à chasse fixe ; les encadrés Définition, Théorème, Méthode et
Attention signalent les points à maîtriser et les pièges fréquents. Les renvois de la forme « voir chapitre 3.2 »
désignent le second chapitre de la troisième partie.
Progression pédagogique
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
7
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
8
De quoi parle-t-on exactement quand on dit « IA » ?
Partie 1
Introduction et définitions
fondamentales
L'expression « intelligence artificielle » est employée si souvent qu'elle a cessé d'informer. Ce premier
module sert à lui rendre une définition opératoire, à la décomposer en branches réellement distinctes,
et à distinguer ce qui relève de la recherche de ce qui relève de l'industrie. Sans cette précision,
chaque discussion ultérieure — sur la confidentialité, l'éthique ou l'emploi — repose sur une
ambiguïté.
Objectifs de la partie
• Définir l'IA et distinguer IA faible, IA forte et apprentissage automatique.
• Nommer les grandes branches et situer leurs recouvrements.
• Expliquer pourquoi le mot a unmet une trajectoire non lineaire.
• Reconnaître les quatre métiers de l'IA : données, modèles, produits, conduite.
Plan de la partie
1.  Introduction et définitions fondamentales
2.  Historique et évolution
3.  Fonctionnement du Machine Learning
4.  Applications pratiques et enjeux éthiques
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
9
Chapitre 1.1
Qu'est-ce que l'intelligence artificielle ?
Une définition utile n'est pas celle qui ressemble à un dictionnaire : c'est celle qui permet de
trancher un débat.
L'intelligence artificielle désigne l'ensemble des méthodes qui permettent à une machine d'accomplir une
tâche qui, faite par une personne, serait qualifiée d'intellectuelle : percevoir, raisonner, décider, apprendre.
Cette définition est großen—— pleasing, mais elle est inutilisable en pratique.
Le piège de la définition par imitation
« L'IA est ce qui fait ce que ferait un humain » conduit à des conclusions fausses dans les deux sens. Une machine
qui joue aux échecs bat le champion du monde sans comprendre l'échecs ; un humain qui calcule de tête ne
serait pas.animation. L'intelligence n'est pas le critère pertinent : ce qui compte est l adaptabilité à des situations
non prévues.
Une définition plus opératoire enchaîne trois conditions. Premièrement, le système doit produire une
sortie dans un espace de décision délimité. Deuxièmement, cette sortie doit être produite par une
procédure et non par une simple table de correspondance. Troisièmement, la procédure doit avoir été
construite — par apprentissage, par optimisation, ou par une modélisation explicite d'un domaine.
Definition — Système d'IA
Un artefact logiciel qui produit une sortie dans un espace de décision, à partir d'une procédure construite sur un
corpus de connaissances ou d'exemples, et dont le comportement n'est pas intégralement spécifié à la main pour
chaque cas d'entrée.
Figure 1 — Les grandes branches de l'IA et leurs recouvrements réels
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
10
Les quatre branches et ce qu'elles ne sont pas
La classification usuelle en cinq branches est pédagogique ; elle l'est moins comme découpage du champ,
car les branches se recoupent presque toutes. Le machine learning alimente la vision, le traitement du
langage et le renforcement ; le traitement du langage alimente les agents ; l'apprentissage par renforcement
produit une partie des systèmes de recommandation.
Branche
Entrée
Sortie
Socle technique
Relation aux autres
Apprentissage automatique
données (x)
une fonction
appriseoptimisation
numérique, statistiques
socle de toutes les autres
Apprentissage profond
données (x)
une fonction apprise
réseaux de neurones profonds
cas particulier du ML
Traitement du langage
texte
texte, décision, requête
transformers, 
modèles 
de
séquence
consomme 
les 
deux
précédents
Vision par ordinateur
image, vidéo
étiquette, position
convolutions, 
transformeurs
visuels
consomme 
les 
deux
précédents
Apprentissage par
renforcement
état, action
politique d'action
optimisation 
de 
politique,
simulation
boucle avec le traitement
du langage
Tableau 1 — Les branches de l'IA : ce qu'elles font et comment elles s'emboîtent
La dernière colonne est la plus utile en pratique : c'est elle qui explique pourquoi un projet « vision » finit souvent par
être un projet de données et non un projet d'algorithme.
• Le machine learning n'est pas une branche parmi d'autres : c'est la méthode dominante de construction
des systèmes d'IA actuels.
• L'apprentissage profond n'est pas plus « intelligent » que le machine learning : il est simplement plus
gourmand en données et meilleur sur les données non structurées.
• Le traitement du langage et la vision sont des domaines d'application qui empruntent leurs méthodes
au socle automatique.
• L'apprentissage par renforcement est la branche la plus lente à produire des résultats, et la plus
exigeante en infrastructure.
IA faible, IA forte, et la place du contexte
La distinction utile n'est pas « intelligence simulée contre intelligence réelle » : c'est « Intelligence bornée
contre intelligence générale ». Une IA faible est spécialisée et limitée à une tâche. Une IA forte est censée
transférer sa compétence d'un domaine à un autre. Toutes les IA industrielles sont faibles.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
11
Figure 2 — IA faible et IA forte : la frontière réellement utile
Attention
La confusion « IA faible / IA forte » est unPairs(argument) fréquent. Dire qu'un système est « faible » ne dit rien
de sa qualité : un modèle de reconnaissance d'images peut être extrêmement fort dans son domaine tout en
étant faible au sens strict. Le couple utile est généraliste contre spécialiste.
Ce que l'IA n'est pas
• Ce n'est pas de l'intuition. Un système de recommandation « devine » le prochain achat, mais il ne
représente aucun raisonnement.
• Ce n'est pas une obligation de comprendre. On peut audit et corriger un modèle sans connaître son
fonctionnement interne ; on ne peut en revanche pas le corriger sans critères.
• Ce n'est pas de l'automatisation. Automatiser, c'est exécuter une règle écrite. L'IA apparaît quand la
règle n'a pas été écrite, parce qu'elle n'est pas connue.
• Ce n'est pas une garantie de résultat. Un système performant en moyenne peut échouer gravement sur
un cas particulier.
Cette dernière nuance prépare tout le module consacré à l'éthique : la question utile n'est jamais « l'IA
est-elle fiable ? » — la réponse est toujours « sur quelle population, avec quelle marge d'erreur » — mais «
quelle erreur est-il acceptable, et qui la supporte ? ».
Astuce
Retenez la formule : l'IA est une fonction apprise, pas une intelligence acquise. Toute la suite du cours découle de
cette distinction : ce qui est appris peut être mesuré, ce qui est « compris » ne le peut pas.
A retenir
• L'IA se définit par sa procédure de construction, pas par son résultat.
• Le machine learning est le socle ; les autres branches sont des domaines d'application.
• IA faible contre IA forte est une distinction de portée générale, pas de qualité.
• Toute question sur l'IA se formule mieux en termes de population, de marge d'erreur et de responsabilité.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
12
Chapitre 1.2
Historique et évolution
L'IA n'est pas nouvelle : elle est en période. Comprendre les cycles d'euphorie et de reflux est la
meilleure façon de ne pas être surpris par le prochain.
L'histoire de l'IA se raconte rarement comme une progression linéaire. C'est une alternance entre promesses
excédant les capacités techniques, et périodes de recul où le financement disparaît. Comprendre ce cycle
change la façon dont on évalue une annonce.
Figure 1 — Quatre siècles de réflexion et soixante ans de calcul
Les origines intellectuelles
Avant l'informatique, la logique formelle tentait déjà de mécaniser le raisonnement. Leibniz cherchait une
langue de caractères dont la manipulation mécanique produirait des conclusions vraies ; le logicien Boole
proposait en 1854 une algèbre de la logique. Ces travaux ne deviennent(real) des programmes qu'avec la
machine, mais ils fixent le programme théorique : rendre le raisonnement calculable.
Algorithme 1 — Le test de Turing (1950)
01  Présenter a la machine des questions écrites sansvoir qui repondLa machine repond de façon
cohérente et pertinente
02  L'examinateur ne peut pas distinguer la machine de l'humain
03  Alors la machine imité l'intelligence dans ses effets
04  Ce que nous appelons intelligence
Entrées : Un examinateur humain, un interlocuteur suppose humain • Sorties : Une réponse a la question :
les machines peuvent-ils penser ? • Complexité : Test philosophique, pas procédure automatique
Le test est souvent lu de travers. Turing ne demande pas « la machine pense-t-elle ? » mais « cette distinction
est-elle observable ? ». C'est un critère opérationnel, pas une these sur la conscience.
Les trois ères de l'IA
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
13
Ère
Période
Paradigme dominant
Factor limitant
Fin de l'ère
Systèmes experts
1970-1987
règles 
expertes,
logiqueacquisition 
et
maintenance des règles
effondrement du Apprentissage
statistique
1988-2012
données, modèles linéaires
volume 
de 
données 
et
capacité de calcul
dépassement par le deep
learning
Apprentissage
profond
2012-2026
réseaux de neurones profonds
coût 
d'entraînement 
et
annotation
en cours
Tableau 1 — Les trois ères de l'IA : paradigme, techniques, facteur limitant
Chaque ère ne remplace pas la précédente : elle empile. Un système de recommandation actuel combine règles métier,
modèle statistique et réseau de neurone.
Figure 2 — Le cycle de l'hiver de l'IA et ses trois causes
Pourquoi l'IA a gelé, et pourquoi elle est repartie
Les deux hivers de l'IA ne sont pas dus à un manque d'idées. Ils sont dus à un écart entre ce qui était promis
et ce qui était littéralement atteignable avec le matériel et les données de l'époque. L fulfi.string est toujours
le même, et il porte un nom : extrapolation abusive des capacités observées.
• 1974 : les systèmes experts produisent des résultatss sur des cas bien couverts et échouent
spectacularment dès qu'on sort du domaine couvert. Le coût de maintenance des règles dépasse le
bénéfice.
• 1987-1993 : le rapport Lighthill que des années de recherche sur l'inférence en logique ne produisent
pas de bond spectaculaire, et le financement baisse d'un coup.
• 2012 : un réseau convolutif obtient un gain de dix points sur la reconnaissance d'images. Le facteur
limitant n'était pas l'idée, mais la puissance de calcul et les données étiquetées — tous deux suddenly
disponibles.
Astuce
Le cycle se répète à chaque fois qu'une capacité observée sur un cas particulier est présentée comme une
capacité générale. Se méfier d'un mot comme « raisonnement », « compréhension » ou « conscience » employé
sans critère d'évaluation est le meilleur garde-fou contre les annonces excessives.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
14
L'ère industrielle
Depuis 2015 environ, la structure du système a changé : la conception d'un modèle n'est plus un travail de
recherche, mais l_ASSEMBLAGE d'un modèle existant, d'une source de données et d'un dispositif
d'évaluation. C'est ce glissement qui rend l'IA accessible à des équipes qui n'ont pas de laboratoire.
Figure 3 — Le cycle de vie responsable d'un système d'IA
A retenir
• L'histoire de l'IA alterne promesses et reflux ; le reflux suit toujours un écart entre démonstration et usage réel.
• Chaque ère ajouté une couche à la précédente sans la remplacer.
• Ce qui a changé depuis 2012 n'est pas l'idée mais la disponibilité simultanée des données, du calcul et des
algorithmes.
• Un vocabulaire non défini (« raisonnement », « compréhension ») est le premier signé d'une annonce excessive.
Chapitre 1.3
Le fonctionnement du machine learning
Six étapes, dont quatre sont du travail d'ingénieur. L'erreur de méthode la plus courante consiste à
les sauter.
Un modèle d'apprentissage automatique est le résultat d'un processus, pas un objet. Le processus comporte
six étapes, et la qualité finale dépend moins du choix de l'algorithme que de l'exactitude des trois premières.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
15
Figure 1 — Le cycle de vie d'un modèle d'apprentissage
Étape 1 — Collecter
La collecte détermine la plafond de performance. Aucun algorithme ne peut apprendre une régularité
absente des données. Les trois questions à poser avant de chercher un modèle sont : que représente
réellement cette donnée ?, qui l'a produite ?, que se passe-t-il si elle est fausse ?
Attention
La question « qui a produit la donnée ? » est celle qu'on néglige le plus. Une donnée collectée par un capteur
défaillant produit un modèle faux avec une assurance élevée : l'erreur est systématique, donc invisible dans les
indicateurs de performance.
Étape 2 — Préparer et nettoyer
• Valeurs manquantes : comprendre pourquoi elles manquent. Une valeur absente après un refus de
réponse n'est pas une valeur absente : c'est une information.
• Normalisation : indispensable dès que des variables ont des unités différentes ; sans elle, la variable la
plus ample écrase toutes les autres dans le calcul des distances.
• Détection d'anomalies : un point atypique n'est pas forcément une erreur, mais il mérite une
explication.
• Fuite d'information : une variable qui n'existait pas au moment de la prédiction ne peut pas être
utilisée.
Exemple
Une fuite d'information classique consiste à inclure dans les variables d'un modèle de crédit une variable «
nombre de retards enregistrés », mise à jour après la décision de credit. Le modèle obtient d'excellentes
performances sur ses données d'entraînement et est inutilisable, car aucune de ces valeurs n'est disponible au
moment où la décision doit être prise.
Étape 3 — Entraîner
L'entraînement consiste à ajuster les paramètres internes d'une fonction pour minimiser une erreur mesurée
sur les données. Le vocabulaire est celui de l'optimisation numérique : fonction d'erreur, gradient, pas
d'apprentissage, itérations.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
16
θ̂ = argminθ L(θ, S)
L(θ, S) = (1)/(m) ∑i=1
m ℓ≤ft(yi, f_θ(xi))
(1.1)
La première expression est le problème à résoudre, la seconde la façon de mesurer l'erreur. Les deux permet de
discuter l'une sans l'autre : on peut changer l'algorithme d'optimisation sans changer la fonction d'erreur.
Famille
Donnée disponible
Question posée
Exemples d'usage
Supervisé
exemples étiquetés
quel est l'étiquette ?cotation de
crédit, diagnostic, prévision de
panne
Non supervisé
exemples bruts
quels groupes se dessinent ?
segmentation client, détection d'anomalie,
compression
Par renforcement
actions et récompenses
que 
faire 
pour 
maximiser 
la
récompense ?
jeux, robotique, régulation, pilotage de
stock
Tableau 1 — Les trois familles d'apprentissage automatique
Le choix de la famille précède le choix de l'algorithme : il découle de la donnée réellement disponible, jamais du résultat
souhaité.
Figure 2 — Trois familles d'apprentissage automatique et leur domaine d'application
Étape 4 — Évaluer
L'évaluation est la seule étape qui protège contre l'illusion. Un modèle doit être jugé sur des données qu'il
n'a jamais vues ; sinon il ne mesure que sa capacité à mémoriser l'échantillon d'entraînement.
Le test final ne doit servir qu'une fois
Le jeu de test sert à décider, une seule fois, à la fin de tout le processus. Le consulter régulièrement — pour
choisir un paramètre, un modèle, une méthode — le transforme en jeu d'entraînement déguisé, et l'estimation
finale devient optimiste. C'est la cause la plus fréquente d'un modèle qui déçoit en production alors qu'il brillait
en évaluation.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
17
Indicateur
Domaine
Ce qu'il mesure
Ce qu'il masque
Exactitude
classification
proportion de bonnes réponsesles classes
déséquilibrées
Rappel
détection
part des positifs réellement trouvés
le coût des faux positifs
Précision
détection
part des signalés qui sont justes
le coût des faux négatifs
Aire sous la courbe
détection
compromis rappel-précision
le choix du seuil
Erreur absolue
régression
écart moyen en unités métier
l'existence de cas extrêmes
AUC
détection
classement des cas par probabilité
la calibration des probabilités
Tableau 2 — Indicateurs courants et ce qu'ils mesurent réellement
Aucun indicateur n'est « bon » dans l'absolu : il est pertinent parce qu'il est lié à un coût asymétrique entre les erreurs.
Étape 5 et 6 — Déployer et suivre
Le déploiement déplace le problème. Un modèle juste sur un échantillon peut être faux en production,
parce que la distribution des données a changé, parce que les entrées ont un format différent, ou parce que
le comportement attendu a été redéfini depuis l'entraînement. Le suivi n'est donc pas une option : c'est la
moitié du travail.
Dérive(t) = Pt(x) ≠ P0(x)
(1.3.2)
La dérive n'est pas une panne : c'est un changement de la loi des données. Tant que le modèle n'a pas été
réentraîné, son erreur augmente silencieusement.
Astuce
Le cycle de vie est circulaire : le suivi doit pouvoir déclencher une nouvelle collecte. Un système d'IA sans boucle
de retour n'est pas en production, il est en démonstration.
A retenir
• Six étapes, dont la moitié relève de l'ingénierie des données plutôt que de l'algorithme.
• La performance est plafonnée par la qualité de la collecte, pas par le choix du modèle.
• L'évaluation sur données inédites est la seule protection contre le surapprentissage et la fuite d'information.
• Le déploiement n'est pas la fin du travail : le suivi et la dérive font partie du système.
Chapitre 1.4
Applications pratiques et enjeux éthiques
Trois domaines où l'IA a produit des effets mesurables, et trois questions qu'on ne peut plus éviter
de poser.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
18
Figure 1 — Domaines d'application et niveau de maturité observé
Industrie et entreprise
Le premier terrain de l'IA industrielle est la maintenance prédictive : instrumenter un équipement,
surveiller ses signaux, et déclencher une intervention avant la panne. Le gain est directement chiffrable en
heures d'arrêt évitées, ce qui explique que ce soit le cas d'usage le mieux établi.
• Maintenance prédictive : surveillance de vibration, température et courant pour anticiper une usure.
• Contrôle qualité : détection visuelle de défauts sur ligne de production, à cadence supérieure à celle
d'un contrôle humain.
• Service client : traitement automatique des demandes simples, avec escalade vers un humain dès que la
demande sort du cadre.
• Planification : prévision de la demande et optimisation des stocks sous contraintes de production.
Santé
En santé, l'IA intervient d'abord en aide au diagnostic, particulièrement en imagerie. Le traitement
automatique des images médicales s'est établi sur des tâches bien délimitées : dépistage du cancer du sein
sur mammographie, analyse de rétinophotographies, détection de fractures. Le résultat n'est pas un
remplacement du radiologue mais un second regard systématique.
Un résultat statistique n'est pas un résultat clinique
Un modèle de dépistage qui détecte 95 % des cas sur une population générale n'apporte rien si cette population
n'est pas celle du déploiement : la prévalence change, donc la valeur prédictive positive aussi. L'évaluation d'un
système médical se fait toujours sur la population d'usage, pas sur un jeu d Venetie académique.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
19
Transport
Le véhicule autonome est l'application la plus visible et la plus exigeante : il combine perception
multi-capteurs, localisation, planification et anticipation du comportement d'autres acteurs. Au-delà de la
conduite, l'IA transforme l'optimisation logistique — tournées, stocks, délais — qui représente une part
importante des coûts d'exploitation d'une entreprise de transport.
Enjeu n° 1 — Biais et équité
Un modèle apprend les régularités de ses données, y compris les inégalités historiques qu'elles contiennent.
Le biais ne vient donc pas de l'algorithme : il vient de la société qui a produit la donnée, et il est amplifié
par la boucle de décision.
Figure 2 — La boucle du biais algorithmique et ses trois conséquences
• Un sous-représentation conduit à des performances dégradées sur le groupe correspondant, et donc à
une exclusion.
• Une exclusion modifié la population décrite par les données futures, ce qui aggravme le biais initial.
• Un décalage de variable — par exemple le code postal comme proxy de la richesse — produit une
discrimination indirecte, difficile à contester.
Auditer un modèle en trois questions
• Qui est représenté ? Comparer la distribution de la population d'entraînement à celle de la population
d'usage.
2. Qui performe ? Décomposer les indicateurs par sous-groupe plutôt que de regarder la moyenne globale.
3. Qui est lésé ? Identifier le coût d'une erreur pour chaque groupe, et vérifier qu'il n'est pas supporté par le
même groupe que la performance faible.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
20
Enjeu n° 2 — Confidentialité et sécurité
Un modèle appris est une chose nouvelle : il ne contient pas les données, mais il les résume. Cette propriété
a des conséquences pratiques : il existe des méthodes d'extraction de données d'entraînement à partir des
seuls poids du modèle, et des méthodes d'inversion qui reconstruit approximativement les exemples d'un
lot.
Cadre juridique et ethique
Cadre juridique. Le règlement européen sur la protection des données (RGPD) impose la minimisation, la
limitation des finalités et la transparence, et considère la minimisation comme un principe de conception. Le
règlement européen sur l'intelligence artificielle (AI Act, 2024) ajoute, selon la classe de risque, des obligations
de documentation technique, de gestion du risque, de qualité des données et de supervision humaine. Un
modèle entraîné sur des données personnelles n'est jamais hors périmètre, même si les données ne sont pas
conservées.
• Apprentissage fédéré : les données restent chez leur détenteur, seules les mises à jour du modèle
circulent.
• Confidentialité différentielle : ajout de bruit calculé pour que la contribution d'une personne donnée
soit indiscernable.
• Chiffrement et calcul : l'entraînement peut s'exécuter sans que personne ne voie les données d'autrui.
Enjeu n° 3 — Impact sur l'emploi
La question de l'emploi se pose mal lorsqu'elle se réduit à « les machines vont-elles remplacer les personnes
». Ce qui s'observe est plus fin : une tâche est plus souvent automatisée qu'un métier. Un métier est un
ensemble de tâches, certaines automatisables, d'autres non.
Situation
Effet observé
Ce qui ne disparaît
pasCompétence à développer
Tâche répétitive à règle fixe
automatisation 
complètele
contrôle et la correction
vérifier plutôt qu'exécuter
Tâche à forte variabilité
assistance, 
non
remplacement
le jugement et l'arbitrage
savoir se saisir d'un cas rare
Métier à forte responsabilité
outillage, non substitution
la décision et la relation
assumer la décision
Métier à forte répétabilité
réorganisation du poste
la coordination et le sens
concevoir le travail
Tableau 1 — Tâches et métiers : ce que l'automatisation touche réellement
La conséquence pratique est un déplacement de la valeur : ce qui devient rare, c'est la responsabilité et le diagnostic ; ce
qui devient abondant, c'est l'exécution.
A retenir
• Les usages les plus établis sont ceux dont le gain se mesure en heures ou en risque évité.
• Un modèle de santé se juge sur la population d'usage, pas sur un résultat de publication.
• Le biais est produit par la boucle données-décision-données, pas par l'algorithme seul.
• L'automatisation porte sur la tâche ; l'effet sur le métier passe par la réorganisation du poste de travail.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
21
Abréviations, notation et ressources de consultation
Annexes
Annexes
Ce cours se termine par deux annexes de référence. La première donne la signification de chaque sigle
employé, sous les deux formes — sigle et développé — car la litterature emploie indifféremment l'une
ou l'autre. La seconde donne la signification de chaque symbole mathématique : elle permet de relire
une démonstration sans revenir au chapitre dont elle est extraite, et de vérifier qu'un même symbole
garde le même sens d'un chapitre à l'autre.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
22
Chapitre A.1
Liste des abréviations
Les sigles ci-dessous sont ceux que le cours emploie. Chacun est donné avec sa forme développée
et le sens précis qu'il prend ici, qui n'est pas toujours celui qu'on lui donne ailleurs.
Un sigle employé sans être développé oblige le lecteur à le reconnaître au passage, ou à l'abandonner. Le
tableau ci-dessous ferme la liste de ceux que le cours emploie : il est exhaustif pour ce document, et non
pour la discipline.
Sigle
Forme développée
Sens dans ce cours
AI
Artificial Intelligence
Dénomination anglaise du champ.
IA
Intelligence artificielle
Systèmes capables de produire des comportements qui demandent
d'intelligence humaine.
ML
Machine Learning
Apprentissage automatique : le modèle tire ses paramètres des données, et
non d'une règle écrite.
RGPD
Règlement général sur la protection des
données
Cadre européen applicable aux données personnelles.
RO
Recherche opérationnelle
Optimisation de décisions sous contraintes.
SII
Système d'information
Ensemble des traitements qui soutiennent l'activité d'une organisation.
Tableau 1 — Abréviations employées dans le cours
Chapitre A.2
Table de notation
Les symboles ci-dessous gardent le même sens d'un chapitre à l'autre. Lorsqu'un chapitre doit
réemployer un symbole pour un autre objet, il le redéclare sur la page même.
La notation est celle du cours : vecteurs en gras, matrices en majuscules grasses, scalaires en italique. Les
espérances sont notées E, les lois de données D, les espaces de paramètres Θ.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
23
Symbole
Signification
x
Observation, ou exemple d'entrée.
y
Étiquette, ou résultat attendu.
(x, y)
Exemple annoté.
D = (xi, yi)i=1
m
Jeu de données d'apprentissage.
m
Nombre d'exemples du jeu.
f
Fonction à apprendre, qui relie x à y.
f_θ
Fonction apprise, paramétrée par θ.
θ
Vecteur de paramètres du modèle.
L(ŷ, y)
Perte entre la prédiction et l'étiquette attendue.
J(θ) = (1)/(m) ∑i=1
m L(f_θ(xi), yi)
Perte moyenne sur le jeu entier.
p
Précision d'un détecteur.
r
Rappel d'un détecteur.
F1
Moyenne harmonique de la précision et du rappel.
ℙ(A)
Probabilité de l'événement A.
E[X]
Espérance de la variable aléatoire X.
Tableau 1 — Symboles mathématiques et leur signification
Convention
Toute divergence constatée entre cette table et un chapitre signale une erreur de transcription, non une
définition nouvelle : la table fait foi.
A retenir
• Un sigle employé sans être listé ici est un oubli de l'auteur, non une définition nouvelle.
• Un symbole qui change de sens d'un chapitre à l'autre rend toute démonstration ininterprétable : c'est la
principale cause des contresens que nous avons relevés.
• Ces deux tables sont les seules parties du cours à maintenir à la main : le reste se relit tout seul.
Index des figures et des tableaux
Référence rapide du matériel visuel
Figures
1.  Les grandes branches de l'IA et leurs recouvrements réels
2.  IA faible et IA forte : la frontière réellement utile
1.  Quatre siècles de réflexion et soixante ans de calcul
2.  Le cycle de l'hiver de l'IA et ses trois causes
3.  Le cycle de vie responsable d'un système d'IA
1.  Le cycle de vie d'un modèle d'apprentissage
2.  Trois familles d'apprentissage automatique et leur domaine d'application
1.  Domaines d'application et niveau de maturité observé
2.  La boucle du biais algorithmique et ses trois conséquences
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
24
Tableaux
1.  Les branches de l'IA : ce qu'elles font et comment elles s'emboîtent
1.  Les trois ères de l'IA : paradigme, techniques, facteur limitant
1.  Les trois familles d'apprentissage automatique
2.  Indicateurs courants et ce qu'ils mesurent réellement
1.  Tâches et métiers : ce que l'automatisation touche réellement
1.  Abréviations employées dans le cours
1.  Symboles mathématiques et leur signification
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
25
Fin du document
Intelligence Artificielle Avancée & Federated Learning — Fondations mathématiques de
l'apprentissage automatique, algorithmes fédérés, protection de la vie privée, défense contre les attaques,
grands modèles de langage fédérés, systèmes embarqués, renforcement appris, applications critiques
(santé, V2X), plateforme de référence FedX et feuille de route de recherche.<br/>Ghiloufi Jamel,
Architecte Logiciel Principal — Pixel Software Design<br/>Département de Recherche & Développement
— Recherche<br/>Pixel Software Design — Édition 2026
© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou
diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans
autorisation écrite préalable de l'auteur.
Document généré automatiquement le 29/09/2026 — mise en page Pixel Software Design.
"""


FONDEMENTS_IA2_TEXT = r"""Pixel Software Design — Département de Recherche & Développement
PIXEL SOFTWARE DESIGN
Département de Recherche & Développement
Intelligence Artificielle
Avancée
& Federated Learning
•  Fondations de l'intelligence artificielle
•  Algorithmes d'apprentissage fédéré
•  Confidentialité, attaques et défenses
•  Applications et grands modèles fédérés
•  Framework FedX de référence
•  Nouveaux fronts de recherche
•  Travaux pratiques, projets et évaluation
Auteur
Ghiloufi Jamel
Fonction
Architecte Logiciel Principal
Direction
Département de Recherche & Développement
Service
R&D - Intelligence Artificielle Avancée & Apprentissage Fédéré
Niveau
Recherche
Édition
Édition 2026 — 1.0
Copyright
© Pixel Software Design
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou
diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans
autorisation écrite préalable de l'auteur.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
2
Copyright et mentions légales
Éditeur
Pixel Software Design
Auteur
Ghiloufi Jamel
Fonction
Architecte Logiciel Principal
Département
Département de Recherche & Développement
Intitulé
Intelligence Artificielle Avancée & Federated Learning
Sous-titre
Fondations mathématiques de l'apprentissage automatique, algorithmes fédérés,
protection de la vie privée, défense contre les attaques, grands modèles de langage
fédérés, systèmes embarqués, renforcement appris, applications critiques (santé,
V2X), plateforme de référence FedX et feuille de route de recherche.
Édition
Édition 2026 (version 1.0)
Langue
Français
Niveau
Recherche
Collection
Supports de formation et de recherche, Pixel Software Design
Droits d'auteur
© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation
ou diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite
sans autorisation écrite préalable de l'auteur.
Droits de l'auteur. Ghiloufi Jamel est l'auteur unique de l'ensemble du contenu scientifique, pédagogique et
technique de cet ouvrage. Toute adaptation, traduction, reproduction ou exploitation, y compris partielle, requiert
une autorisation écrite préalable.
Droits des tiers. Les algorithmes, modèles et travaux cités restent la propriété de leurs auteurs respectifs. Les
références employées figurent en fin d'ouvrage, ce qui permet de remonter au travail original pour toute
affirmation chiffrée.
Marques et licences externes. PyTorch, TensorFlow, Flower, Opacus, MONAI, scikit-learn et PySyft sont des
logiciels libres sous licences respectives (BSD, Apache 2.0, MIT). Leur usage dans ce document est purement
pédagogique et n'emporte aucune prescription commerciale.
Mentions relatives aux données et aux expérimentations
Document pédagogique à usage de formation interne. Les exemples de code fournis sont livrés à titre pédagogique
; les résultats numériques illustrés sont issus d'expérimentations conduites dans un cadre de recherche et ne
constituent pas des performances de production.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
3
Ce support synthétise les travaux de recherche du Département de Recherche & Développement de Pixel Software
Design sur l'intelligence artificielle distribuée, l'apprentissage fédéré, la protection de la vie privée et les systèmes
embarqués intelligents.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
4
Sommaire
Structure détaillée du cours
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 8
Partie 1 — Fondements théoriques de l'intelligence artificielle
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 9
1.1 Logique symbolique, langages formels et limites du consensus
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 11
1.2 Théorie des langages de programmation et calcul différentiable
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 13
1.3 Compilation des graphes de calcul : dialectes et mémoire
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 15
1.4 Informatique théorique : complexité, information, graphes
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 18
1.5 Science des données et méthode empirique
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 19
1.6 Les disciplines qui préparent l'IA de demain
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 22
Annexes
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 23
A.1 Liste des abréviations
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 23
A.2 Table de notation
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
5
Partie
Thème
Contenu
Compétence visée
Durée
Partie 1
Fondations
Statistique, optimisation, courbes d'apprentissage
Comprendre et formaliser
2-3 semaines
Partie 2
Algorithmes FL
FedAvg, convergence, hétérogénéité, système
Implémenter et régler
3-4 semaines
Partie 3
Confidentialité
DP, attaques, défenses, agrégation sécurisée
Auditer et sécuriser
2-3 semaines
Partie 4
Applications
FedLLM, santé, V2X, FedRL, TinyML, graphes
Transposer à un domaine
3-4 semaines
Partie 5
Framework FedX
Architecture, API, benchmarks, exploitation
Industrialiser
2 semaines
Partie 6
Nouveaux fronts
FedCL, FedCI, SNN, FedGL, feuille de route
Ouvrir la recherche
2 semaines
Partie 7
TP et projets
9 labs, 5 projets, corrigés, évaluation
Faire et rendre
4-6 semaines
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
6
Préface
Comment utiliser ce cours
Ce support est conçu pour un parcours de formation et de recherche couvrant l'ensemble de la chaîne de valeur de
l'intelligence artificielle distribuée : les fondations mathématiques, les algorithmes d'apprentissage fédéré, les
menaces et défenses, les applications de pointe, une plateforme de référence opérationnelle, et enfin les nouveaux
fronts ouverts par la recherche du Département.
Ce n'est pas un manuel de référence à lire d'un trait : c'est un manuel opératoire. Chaque chapitre alterne
exposition, formalisation, mise en œuvre numérique et évaluation. Les listings sont complets et exécutables ; les
tableaux comparatifs servent de grille de décision ; les schémas d'architecture servent de support de revue de
conception.
Public et prérequis
Le contenu s'adresse à des étudiants de master et de doctorat, à des ingénieurs IA et à des praticiens de la
recherche appliquée. Les prérequis sont la connaissance de l'apprentissage automatique classique, de
l'algorithmique numérique et des bases de probabilités. Les parties 1 à 3 sont auto-suffisantes pour un étudiant qui
découvre le domaine ; les parties 4 à 7 supposent la mécanique et les outils présentés dans la partie 2.
Conventions de lecture. Une expression mathématique est encadrée par deux signes dollars ; un identifiant, un
fichier ou une commande est écrit en caractères à chasse fixe ; les encadrés Définition, Théorème, Méthode et
Attention signalent les points à maîtriser et les pièges fréquents. Les renvois de la forme « voir chapitre 3.2 »
désignent le second chapitre de la troisième partie.
Progression pédagogique
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
7
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
8
Logique, langages, compilation, complexité et méthode
Partie 1
Fondements théoriques de
l'intelligence artificielle
On peut utiliser l'intelligence artificielle sans connaître ses fondements. On ne peut pas en concevoir
de nouvelles architectures, ni comprendre pourquoi une optimisation marche, sans eux. Ce cours
assemble les six disciplines théoriques qui déterminent ce qui est possible, ce qui est rapide, et ce qui
reste hors de portée.
Objectifs de la partie
• Lire un algorithme d'inférence formelle et connaître la limite de complétude du premier ordre.
• Relier une fonction de perte à une grandeur de la théorie de l'information.
• Expliquer pourquoi un réseau profond est un graphe de calcul, et ce qu'est sa descente.
• Justifier le passage d'une grammaire à une autre, et connaître la hiérarchie de Chomsky.
• Comprendre ce qu'apporte un compilateur de tenseurs, et pourquoi la fusion de noyaux change tout.
• Énoncer ce que le théorème de l'impossibilité du consensus distributed impose à un système asynchrone.
Plan de la partie
1.  Logique symbolique, langages formels et limites du consensus
2.  Théorie des langages de programmation et calcul différentiable
3.  Compilation des graphes de calcul : dialectes et mémoire
4.  Informatique théorique : complexité, information, graphes
5.  Science des données et méthode empirique
6.  Les disciplines qui préparent l'IA de demain
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
9
Chapitre 1.1
Logique symbolique, langages formels et
limites du consensus
Trois fondations : ce qu'on sait énoncer, ce qu'on sait calculer, ce qu'il est impossible de garantir.
Langages formels et grammaires
Un langage formel est défini par un alphabet fini et un ensemble de règles de production. La grammaire
décrit la syntaxe ; elle ne dit rien du sens des phrases.
G : S → a S b | a
a S b ⇒* an bn n ≥ 1
(F.1)
La récursion produit des langages infinis à partir d'un nombre fini de règles. C'est tout le problème des langages
de programmation : on décrit l'infini par le fini.
Type
Langage reconnu par
Capacité de mémoire
Exemple
Type 0
machine de Turing
aucune borneproblèmes indécidables
Type 1
automate à pile
pile non bornée
expressions régulières, analyse syntaxique
Type 2
automate à pile
pile non bornée, transduction
la plupart des langages de programmation
Type 3
automate fini
un seul état courant
expressions régulières
Tableau 1 — La hiérarchie de Chomsky et son usage en intelligence artificielle
Le type 1 et le type 2 partagent le même pouvoir de mémoire ; ils diffèrent par la nature de l'algorithme de
reconnaissance, pas par ce qu'ils décrivent.
Logique des prédicats et incomplétude
La logique des prédicats du premier ordre est expressive au point d'être incomplète : il existe des énoncés
vrais dans toute structure sans être démontrables. C'est le théorème de Gödel, et c'est la raison pour
laquelle une base de connaissances en logique des prédicats ne peut pas être complète.
Satisfiabilité = ∃ M M models φ
Validité = ∀ M M models φ
(F.2)
Vérifier la satisfiabilité d'une formule du premier ordre est indécidable en général. En pratique, on utilise des
solveurs qui explorent l'espace de structures de façon systématique et s'arrêtent au premier modèle.
La différence entre satisfiable et valide
Un énoncé peut être satisfiable sans être valide : il existe une structure où il est vrai, mais pas toutes. C'est
exactement l'écart entre « il existe un patient qui réagit au traitement » et « le traitement fonctionne ».
Confondre les deux est l'erreur logique la plus répandue dans les systèmes de règles.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
10
Élément
Rôle
Exemple
Fait
élément connu, supposé vrai
homme(socrate)
Règle
condition déclenchante
homme(X) :- mortel(X)
Clause
faux et tête avec corps
¬homme(X) ∨ mortel(X)
Question
ce que l'on cherche à déduire
? mortel(socrate)
Unification
cherche les variables compatibles
X = socrate
Résolution
combine des clauses pour en déduire une nouvelle
applique la clause 2 avec la négation correspondante
Tableau 2 — Programmation logique : de la clause a l'inférence
Le théorème de l'impossibilité du consensus
Dans un système asynchrone où un seul nœud peut tomber en panne, aucun algorithme déterministe ne
peut garantir qu'un ensemble de nœuds réagissent à un même message. Ce résultat, connu par les initiales
de ses auteurs, borne tout ce qu'on peut construire.
Definition — Théorème d'impossibilité
Il n'existe pas d'algorithme déterministe tolérant à une panne, fonctionnant dans un système asynchrone, qui
garantisse l'accord d'un ensemble d'agents sur une valeur commune. La conclusion est qu'au moins une des
propriétés suivantes doit être abandonnée : terminaison, sûreté, tolérance à la panne ou déterminisme.
Propriété
Signification
Ce qu'on fait concrètement
Accord exact
tous les nœuds ont la même valeur
tolérance
Temps borné
la décision arrive en temps fini
horloge ou délai
Tolérance à la panne
un nœud mort n'arrête pas le système
redondance et vote
Déterminisme
le calcul est reproductible
hasard ou calcul probabiliste
Tableau 3 — Ce que l'impossibilité impose en pratique
Aucun système réel ne satisfait les quatre. L'agencement pratique est presque toujours : accord exact, délai borné,
tolérance à la panne, et hasard dans le choix du arbitre.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
11
Figure 1 — Chaîne symbolique et chaîne neuronale : l'articulation neuro-symbolique
A retenir
• Un langage formel est infini, décrit par un ensemble fini de règles.
• La logique des prédicats est expressive mais incomplète : certaines vérités ne sont pas démontrables.
• Le théorème d'impossibilité borne l'accord exact, le temps borné, la tolérance à la panne et le déterminisme.
• Tout système réel abandonné au moins une de ces quatre propriétés.
Chapitre 1.2
Théorie des langages de programmation et
calcul différentiable
Un réseau de neurones est un programme. C'est un programme qui se dérive.
Le lambda-calcul : modèle universel du calcul
Le lambda-calcul est un langage minimal — trois formes seulement — mais il est universellement puissant.
Toute fonction calculable par une machine de Turing s'écrit dans le lambda-calcul, et réciproquement.
overlinet = λ x. t
(t ≡ t') → (T ≡ λ x. U) ∧ (T' ≡ t' [ x ↦ t ])
(F.3)
L'application se lit comme une fonction : T' = t'[x ↦ t] signifie que l'argument est substitué dans le corps avant
évaluation. Toute la sémantique d'un langage fonctionnel tient dans cette règle.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
12
Caractéristique
Programmation fonctionnelle
Réseau de neurones
Fonction
valeur de premier ordre
couche = transformation
État
absent ou explicite
caches, mémoire, compteurs
Effet de bord
évité par construction
allocation mémoire
Répétition
récursion et composition
parallélisme par lots
Erreur
exhaustive, types stricts
silencieuse, dynamique
Tableau 1 — Programmation fonctionnelle et réseaux de neurones
Le lambda-calcul explique la forme du code, pas son efficacité. L'immutabilité des tenseurs sert un autre objet : la sûreté
de l'exécution parallèle.
Systèmes de types et dimensions des tenseurs
L'erreur la plus fréquente en apprentissage profond n'est pas algorithmique : c'est l'incompatibilité de
dimensions, détectée à l'exécution après des minutes de calcul sur accélérateur.
(d1, d2) × (d1, d3) → (d2, d3)
incompatible : (d1, d2) × (d3, d4) si d2 ≠ d3
(F.4)
C'est la règle du produit matriciel, vérifiée statiquement. L'affichage explicite des dimensions dans les
messages d'erreur est l'un des gains de productivité les plus élevés d'un outillage de vérification.
Quatre dimensions à vérifier systematiquement
• Après toute normalisation : la norme divide par un écart-type, il faut que ce dernier ne soit pas nul.
2. Avant toute réduction de dimension : le nombre de composantes ne peut pas dépasser le nombre
d'exemples.
3. Entre deux lots : un lot vide ne doit pas produire un tenseur de dimension nulle.
4. Avant toute réduction de mémoire : la taille visée doit être alignée sur la granularité réelle des données.
Le calcul différentiable comme langage
Un programme devient apprenable lorsque chaque opération est différentiable. Le compilateur ne se
contente plus à traduire : il construit un second programme, le graphe de rétropropagation, qui calculé les
dérivées par rapport à chaque paramètre.
Algorithme 1 — Descente de gradient sur un réseau profond
01  Initialiser les poids au hasard, avec une graine fixéeChoisir un lot de données et passer la
passe avant
02  Enregistrer chaque opération dans un graphe
03  Calculer la perte sur le lot, puis la derivee locale de chaque nœud
04  Propager vers l'arriere en accumulant les contributions
05  Mettre a jour chaque poids dans la direction opposee a sa derivee
06  Répéter jusqu'a epuisement du budget de calcul
07  Évaluer sur un jeu de données de validation, jamais sur celui d'entraînement
Entrées : Données étiquetées, architecture, budget d'itérations • Sorties : Poids ajustés, métriques de
validation • Complexité : Coût de la passe arrière ≈ 2 fois la passe avant
La ligne 3 est la charnière : sans enregistrement, la rétropropagation est impossible. Elle est aussi la source de
la plus grande consommation mémoire d'un entraînement.
A retenir
• Le lambda-calcul est un modèle universel du calcul, pas seulement de la programmation fonctionnelle.
• Une erreur de dimensions est une erreur de type déguisée.
• Le calcul différentiable transforme un programme en un second programme qui le dérive.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
13
• L'enregistrement du graphe est la condition de la rétropropagation, et la première source de coût mémoire.
Chapitre 1.3
Compilation des graphes de calcul : dialectes
et mémoire
Le même code doit tourner sur un processeur, une carte graphique ou un circuit. C'est un
problème de langages.
Figure 1 — Descente d'un graphe de calcul à travers les dialectes
Pourquoi une représentation intermédiaire unique ne suffit pas
Un compilateur classique travaille sur une représentation intermédiaire unique, proche de l'assembleur.
Optimiser un réseau de neurones avec une telle représentation est presque impossible : à ce niveau, la
structure mathématique du calcul a été perdue.
Dialecte
Un sous-ensemble de types, d'opérations et de règles de transformation, correspondant à un niveau d'abstraction
précis. Un même programme peut être exprimé dans plusieurs dialectes, et le compilateur passe de l'un à l'autre
par des transformations appelées abaissements.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
14
Dialecte
Représente
Apport à l'optimisation
tensor
opérations mathématiques abstraitesfusion d'opérations
sur tenseurs entiers
linalg
itérations d'algèbre linéaire structurées
parallelisation, pavage, vectorisation
sparse
matrices creuses et leurs motifs
détection de structure, insertion de zéros
memref
blocs mémoire, adresses, durées de vie
allocation, réutilisation, vectorisation mémoire
scf
contrôle de flux structuré
débouclage, fusion de boucles, parallélisation
gpu
unités de calcul de la carte
occupation, registres, accès mémoire partagé
llvm
instruction machine générique
transformation finale
Tableau 1 — Les dialectes de la chaîne de compilation
Chaque dialecte ajoute une connaissance du matériel ou de l'algèbre. C'est cette connaissance accumulée qui permet
d'optimiser là où une représentation unique ne le peut pas.
Exemple concret : l'addition de deux vecteurs
Prenons l'opération la plus simple et suivons-la à travers la chaîne. L'exemple est volontairement trivial :
l'intérêt est dans la transformation, pas dans le calcul.
Algorithme 2 — Descente d'une addition élémentaire
01  Au niveau tensor : addition de deux tenseurs de 1024 éléments, sans étatConversion vers
linalg : une boucle générique, iterateur de type parallel
02  Conversion vers memref : des blocs mémoire, des adresses, une durée de vie
03  Analyse de durée de vie : le résultat est écrit puis plus jamais relu
04  Allocation : réutilisation du tampon d'entrée si les durées de vie ne se croisent pas
05  Vectorisation : regroupement des éléments par registres de la carte
06  Fission de boucle : distance de réutilisation comparée a la taille du tampon partage
07  Passage final : émission du code pour la carte cible
Entrées : Deux tenseurs de 1024 flottants de 32 bits • Sorties : Un tenseur de sortie, et le code machine
correspondant • Complexité : Le gain vient de la suppression des allers-retours mémoire
L'étape 6 est celle qui change tout : sans elle, chaque élément passe par la mémoire globale, qui est le facteur
limitant réel d'un accélérateur.
Figure indisponible
La figure thm_mémoire n'est pas encore implementee.
Les trois techniques de gestion de la mémoire
• Analyse de durée de vie : le compilateur détermine à quel instant un tenseur est créé, utilisé pour la
dernière fois, puis mort. Cette information autorise la libération anticipée.
• Réutilisation de tampons : deux tenseurs dont les durées de vie ne se chevauchent pas peuvent occuper
le même bloc physique. C'est la technique qui fait passer la mémoire d'un gigaoctet à deux cents
mégaoctets dans un cas réel.
• Fusion de noyaux : si un résultat temporaire est produit puis relu immédiatement, il n'est jamais écrit
en mémoire globale. Le calcul fusionné s'exécute dans les registres et la mémoire partagée du bloc.
La bande passante, pas le calcul
Un accélérateur passe l'essentiel de son temps à attendre des données, pas à calculer. Multiplier la puissance de
calcul sans réduire les transferts mémoire ne produit aucune accélération. C'est pourquoi la fusion de noyaux est
souvent plus rentable qu'une amélioration de l'algorithme lui-même.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
15
Phase
Entrée
Sortie
Exemple d'optimisation
Capture
code source
graphe de haut niveauélagage
des 
constantes, 
fusion
d'opérations
Intermédiaire
graphe
graphe structuré
vectorisation, pavage des boucles
Spécialisée
graphe structuré
graphe mémoire
allocation, réutilisation de tampons
Codegen
graphe mémoire
instruction machine
choix d'instructions, registres
Tableau 2 — Les quatre phases de la compilation d'un modèle
La phase critique est la troisième : c'est là que la mémoire est décidée, et c'est le facteur limitant.
A retenir
• Un dialecte est un niveau d'abstraction avec ses propres types et ses propres règles.
• L'abaissement progressif permet d'optimiser là où une représentation unique ne le peut pas.
• La durée de vie d'un tenseur est l'information qui autorisé la réutilisation de tampon.
• La fusion de noyaux supprime les allers-retours en mémoire globale, premier poste de coût.
Chapitre 1.4
Informatique théorique : complexité,
information, graphes
Trois théories qui disent ce qui est faisable, ce qui est rapide, et ce que vaut une information.
Complexité : ce qui est hors de portée
L'informatique théorique classe les problèmes selon le temps et l'espace nécessaires pour les résoudre en
fonction de la taille de l'entrée. La classe NP décrit les problèmes dont on vérifie facilement une solution
proposée.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
16
Figure 1 — Temps de calcul selon la taille du problème
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
17
∃ algorithme déterministe A : A(x) en O(2|x|) ? Longrightarrow P stackrel?= NP
(1.4.1)
La question est ouverte depuis des décennies. Sa réponse déterminerait la façon dont on conçoit toute une
catégorie de systèmes : vérification, planification, cryptographie.
Classe
Problèmes
Conséquence pour l'IA
P
trouver une solution en temps polynomialalgorithms
utilisables directement
NP-complet
vérifier une solution est polynomial
on accepte une solution approximative
PSPACE
problèmes de jeux et de systèmes d'agents
recherche exhaustive nécessaire pour l'optimalité
Indécidable
aucun algorithme, par construction
impossibilité de vérifier toutes les propriétés
Tableau 1 — Les classes de complexité et leur place en intelligence artificielle
L'apprentissage automatique contourne la difficulté NP par statistique : il n'essaie pas de trouver la solution optimale, il
apprend une politique bonne en moyenne.
Théorie de l'information
La théorie de l'information quantifie l'incertitude d'une distribution de probabilité. Elle fournit la fonction
de perte de la quasi-totalité des modèles.
H(p) = - ∑k pk log2 pk
L = - ∑k p*
k log2 p̂k
(F.5)
L'entropie mesure l'incertitude de la distribution vraie ; l'entropie croisée mesure à quel point la prédiction s'en
écarte. Minimiser l'entropie croisée revient à maximiser la vraisemblance des données observées.
Quantité
Définition
Usage
Entropie
incertitude moyenne d'une distributionmesure de la
qualité d'une prédiction
Entropie croisée
écart entre distributions prédites et vraies
fonction de perte standard
Information mutuelle
information partagée par deux variables
séparation de composantes, réduction de
dimension
Divergence de Kullback-Leibler
distance non symétrique
régression, ré-entraînement d'un modèle
Bande passante
capacité d'un canal de transmission
coût 
de 
communication 
d'un 
système
distribué
Tableau 2 — Les quantités de la théorie de l'information en IA
Théorie des graphes
Un réseau de neurones profond est, mathématiquement, un graphe orienté acyclique de calcul : chaque
nœud est une opération, chaque arête transporte un tenseur. Cette lecture explique la propagation de bout
en bout et la rétropropagation.
• Graphe orienté acyclique de calcul : la structure d'un réseau profond ; le sens de parcours est l'ordre
d'exécution.
• Graphe de passage avant et arrière : les deux sens de la rétropropagation sont deux parcours du même
graphe.
• Processus décisionnel de Markov : le modèle formel d'un agent qui évolue entre états, formalisé par un
triplet (états, actions, transitions).
• Graphe de connaissance : entités reliées par des relations typées, base d'un raisonnement symbolique
explicable.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
18
A retenir
• La classe NP borne ce qu'une recherche exhaustive peut produire ; l'apprentissage automatique la contourne
par approximation.
• L'entropie croisée est la traduction directe de la théorie de l'information en fonction de perte.
• Un réseau profond est un graphe orienté acyclique de calcul, parcouru dans deux sens.
• Le processus de Markov est le modèle formel d'un agent qui évolue entre états.
Chapitre 1.5
Science des données et méthode empirique
La science des données est l'ensemble des contraintes qui empêchent une bonne méthode de
produire un mauvais résultat.
Figure 1 — Le cycle empirique de la science des données
Préparation : ce qui se joue avant le modèle
• Valeurs manquantes : comprendre pourquoi elles manquent. Une valeur absente après un refus de
réponse est une information, pas une absence.
• Normalisation : indispensable dès que des variables ont des unités différentes, sans quoi la plus ample
écrase toutes les autres.
• Détection d'anomalies : un point atypique n'est pas forcément une erreur, mais il mérite une
explication.
• Fuite d'information : une variable qui n'existait pas au moment de la prédiction ne peut pas servir.
Statistiques et probabilités
Un modèle d'IA prédictive ne raisonne pas en certitudes mais en probabilités. La statistique fournit le
vocabulaire pour quantifier cette incertitude et pour distinguer une amélioration réelle d'une fluctuation
d'échantillon.
yi ∼ N≤ft(μ, σ2) Longrightarrow μ̂ ± (σ)/(√(n)) z1-α/2
(1.5.1)
L'intervalle de confiance ne dit pas que le paramètre est dans l'intervalle : il dit que la procédure produirait un
intervalle le contenant dans 95 % des cas si le modèle était correct. Cette nuance est la source de la plupart des
contresens.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
19
Ingénierie des caractéristiques
Avant que les réseaux profonds n'automatisent l'extraction de structure, la conception manuelle des
variables était l'essentiel du travail. Elle ne l'est plus devenue, mais la discipline reste nécessaire pour les
données tabulaires et pour les variables sensibles au domaine.
Transformation
Objectif
Précaution
Normalisation centrée réduite
comparer des échellessensible aux valeurs
extrêmes
Discrétisation
rendre un modèle linéaire non linéaire
perte d'information, choix des seuils
Indicateurs
encoder une catégorie
une catégorie rare devient un alias vidé
Interaction
capturer un effet conjoint
explosion combinatoire du nombre de termes
Réduction de dimension
supprimer le bruit
interprétabilité perdue
Transformations logarithmiques
réduire l'asymétrie
impossible sur les valeurs négatives
Tableau 1 — Les transformations de variables les plus courantes
Évaluation et validation
Protocole de validation en cinq temps
• Séparer en trois jeux : entraînement, validation, test.
2. Valider croisée sur le jeu d'entraînement, jamais sur le test.
3. Choisir les hyperparamètres sur le jeu de validation.
4. Consulter le test une seule fois, à la fin.
5. Rapporter l'intervalle de confiance, pas seulement la moyenne.
Le test consulté régulièrement cesse d'être un test : il devient un second jeu d'entraînement, et l'estimation finale
est optimiste.
Indicateur
Formule
À utiliser quand
Exactitude
(TP+TN)/(TP+TN+FP+FN)
classes équilibrées
Précision
TP/(TP+FP)
un faux positif coûte cher
Rappel
TP/(TP+FN)
un faux négatif coûte cher
Score F1
moyenne harmonique des deux
compromis entre les deux
Aire sous la courbe
aire du tracé rappel-précision
comparaison de classifieurs tous seuples
Matrice de confusion
tableau des quatre cas
audit, jamais comme métrique unique
Tableau 2 — Indicateurs de classification et ce qu'ils mesurent
Le choix de l'indicateur précède celui de l'algorithme : il découle du coût réel de chaque type d'erreur.
A retenir
• La préparation des données précède le choix du modèle et détermine le plafond de performance.
• Un intervalle de confiance porte sur la procédure, pas sur le paramètre estimé.
• Le test consulté régulièrement cesse d'être un test.
• Le choix de l'indicateur découle du coût de chaque type d'erreur, pas de la facilité de calcul.
Chapitre 1.6
Les disciplines qui préparent l'IA de demain
Cinq domaines dont la rencontre déterminera les dix prochaines années.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
20
Figure 1 — Cinq disciplines qui préparent l'IA de demain
Discipline
Question qu'elle adresse
Ce qu'elle éclaireHorizon
Matériel et calcul
comment calculer plus vite, moins
cherle franchissement des murs de coût
court terme
Neuro-symbolique
comment vérifier un raisonnement
la fin des hallucinations non détectées
moyen terme
Systèmes multi-agents
comment coordonner des agents
l'organisation de travail par essaim
moyen terme
Neurosciences
computationnelles
comment apprendre en continu
l'apprentissage 
permanent, 
non
l'entraînement figé
long terme
Éthique et gouvernance
comment garder le contrôle
la 
légitimité 
du 
système 
et 
sa
responsabilité
immédiat
Tableau 1 — Les cinq disciplines et ce que chacune éclaire
Les deux dernières lignes ne sont pas de la recherche : elles déterminent ce qui peut être déployé.
Matériel, accélérateurs et informatique quantique
La contrainte matérielle a façonné toute l'histoire de l'intelligence artificielle. La disponibilité simultanée de
cartes graphiques abordables et de données massives a déclenché la dernière rupture. L'informatique
quantique cherche un accélérateur qualitativement différent, pour des problèmes aujourd'hui
intrinsèquement hors de portée.
L'apprentissage automatique quantique est un domaine de recherche. Il n'existe à ce jour aucune
application industrielle, et la question de savoir si le calcul quantique accélérera un modèle
d'apprentissage reste ouverte. Citer un avantage quantique établi sur une tâche concrète serait inexact.
Précaution de lecture
Architectures neuro-symboliques
L'idée est simple : faire produire une conclusion par un réseau, puis la faire vérifier par un moteur logique.
Le réseau apporte la capacité à percevoir des données non structurées ; la logique apporte la garantie
qu'une conclusion non soutenue par une règle ne peut pas être prononcée.
• Vérification de la sortie : la conclusion produite est soumise à un contrôleur logique ; si aucune règle
ne la soutient, elle est rejetée.
• Exécution de contraintes : les invariants du domaine sont appliqués avant et après la prédiction, jamais
seulement après.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
21
• Appel d'outils symboliques : le modèle délègue le calcul exact à un moteur dédié, plutôt que de
l'approximer.
• Explication par trace : la justification est reconstruite à partir des règles effectivement utilisées.
Pourquoi cette combinaison est prometteuse
Un assistant de requête en langage naturel produit une requête SQL. Le modèle génératif n'a aucune garantie
que la requête corresponde à l'intention. En encadrant la génération d'une couche symbolique — typage des
colonnes, vérification des prédicats, contrôle des droits d'accès — on obtient un système dont le comportement
est borné, et dont l'échec est explicite.
Systèmes multi-agents
L organisations en essaim remplace progressivement l'assistant unique. La théorie des jeux, les protocoles
de consensus et l'auto-organisation sont les outils de conception de ces systèmes — et, pour le consensus, la
limite théorémique rappelée au premier module s'applique intégralement.
Neurosciences computationnelles et sciences cognitives
Pour construire des systèmes capables d'apprentissage continu plutôt que d'entraînement figé, la recherche
s'inspire de la plasticité synaptique et des mécanismes de mémoire du cerveau. Il ne s'agit pas de reproduire
le cerveau, mais d'en emprunter des principes dossés : plasticité, sparsité, niveaux de mémoire.
Éthique, alignement et gouvernance
Plus un système est puissant et autonome, plus la question de son contrôle devient critique. L'alignement
des objectifs, la théorie du choix social et la cryptographie appliquée à la traçabilité forment le socle
technique ; le droit et la gouvernance en forment le cadre opérationnel.
Comment lire une prévision à dix ans
Un document prospectif sur l'intelligence artificielle se lit en séparant trois registres : ce qui est déployé
aujourd'hui, ce qui est en recherche expérimentale, et ce qui relève de la spéculation. Ces trois registres se
mélangent facilement, et le mélange produit soit une naïveté, soit un déni. Un critère simple : si l'affirmation ne
peut pas être testée par une expérimentation publiée, elle relève du troisième registre.
A retenir
• Les cinq disciplines qui comptent ne sont pas cinq voies technologiques, mais cinq questions distinctes.
• Le neuro-symbolique vise la vérifiabilité, pas la performance.
• L'apprentissage quantique reste un domaine de recherche sans application industrielle.
• Trois registres de lecture — déployé, recherché, spéculatif — doivent être séparés dans tout document
prospectif.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
22
Abréviations, notation et ressources de consultation
Annexes
Annexes
Ce cours se termine par deux annexes de référence. La première donne la signification de chaque sigle
employé, sous les deux formes — sigle et développé — car la litterature emploie indifféremment l'une
ou l'autre. La seconde donne la signification de chaque symbole mathématique : elle permet de relire
une démonstration sans revenir au chapitre dont elle est extraite, et de vérifier qu'un même symbole
garde le même sens d'un chapitre à l'autre.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
23
Chapitre A.1
Liste des abréviations
Les sigles ci-dessous sont ceux que le cours emploie. Chacun est donné avec sa forme développée
et le sens précis qu'il prend ici, qui n'est pas toujours celui qu'on lui donne ailleurs.
Un sigle employé sans être développé oblige le lecteur à le reconnaître au passage, ou à l'abandonner. Le
tableau ci-dessous ferme la liste de ceux que le cours emploie : il est exhaustif pour ce document, et non
pour la discipline.
Sigle
Forme développée
Sens dans ce cours
AQ
Assurance qualité
Ensemble des vérifications passées sur un livrable avant sa diffusion.
BL
Base de connaissances
Formalisation en logique d'un domaine de connaissance.
F1
Score F1
Moyenne harmonique de la précision et du rappel, entre 0 et 1.
FN
Faux négatif
Alerte manquée, ou étiquette non attribuée à tort.
FP
Faux positif
Alerte émise à tort, ou étiquette attribuée par erreur.
NN
Vrai négatif
Absence correcte d'alerte, ou refus d attribuer une étiquette.
TP
Vrai positif
Alerte correcte, ou étiquette attribuée à bon escient.
COV
Covariance
Covariance empirique entre deux variables.
H
Entropie
Mesure d'incertitude, en nats si le logarithme est népérien, en bits s'il est
binaire.
NC
Nombre de classes
Cardinalité de l'espace des étiquettes.
NP
Non-Polynomial time
Classe de complexité des problèmes dont on ignore l'appartenance à P.
P
Polynomial time
Classe des problèmes solubles en temps polynomial.
PSPACE
Polynomial Space
Classe des problèmes solubles en espace polynomial.
SVM
Support Vector Machine
Machine à vecteurs de support, classifieur à marge maximale.
Tableau 1 — Abréviations employées dans le cours
Chapitre A.2
Table de notation
Les symboles ci-dessous gardent le même sens d'un chapitre à l'autre. Lorsqu'un chapitre doit
réemployer un symbole pour un autre objet, il le redéclare sur la page même.
La notation est celle du cours : vecteurs en gras, matrices en majuscules grasses, scalaires en italique. Les
espérances sont notées E, les lois de données D, les espaces de paramètres Θ.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
24
Symbole
Signification
x ∈ ℝd
Observation, vecteur de d coordonnées réelles.
y ∈ Y
Étiquette associée, appartenant à l'espace Y.
(x, y)
Exemple annoté.
f : X → Y
Fonction d'apprentissage cible.
h
Prédicteur admis, qui approxime f.
h*(x) ∈ argminh R(h)
Fonction de Bayes, qui atteint le risque minimal.
f*(x) = argminc ℙ(Y=c | X=x)
Règle de Bayes, qui coïncide avec h* lorsque le risque est nul sur h = f*.
L(ŷ, y)
Perte entre la prédiction et l'étiquette.
R(h) = E[L(h(X), Y)]
Risque attendu, sous la loi D.
R̂(h) = (1)/(m)∑i=1
m L(h(xi), yi)
Risque empirique sur les m exemples observés.
m
Nombre d'exemples d'apprentissage.
d
Dimension de l'espace d'entrée.
h*
Fonction de Bayes, notation abrégée.
Δ = 1 - (R(h))/(R(h*))
Marge de généralisation du prédicteur.
H(Y) = -∑c pc log pc
Entropie de l'étiquette.
I(X;Y) = H(Y) - H(Y | X)
Information mutuelle entre l'entrée et l'étiquette.
Σ
Matrice de covariance des variables.
E[X]
Espérance de la variable aléatoire X.
λ
Marge d'un classifieur, ou valeur propre d'une matrice.
O(g(n))
Complexité en temps bornée par g(n).
Tableau 1 — Symboles mathématiques et leur signification
Convention
Toute divergence constatée entre cette table et un chapitre signale une erreur de transcription, non une
définition nouvelle : la table fait foi.
A retenir
• Un sigle employé sans être listé ici est un oubli de l'auteur, non une définition nouvelle.
• Un symbole qui change de sens d'un chapitre à l'autre rend toute démonstration ininterprétable : c'est la
principale cause des contresens que nous avons relevés.
• Ces deux tables sont les seules parties du cours à maintenir à la main : le reste se relit tout seul.
Index des figures et des tableaux
Référence rapide du matériel visuel
Figures
1.  Chaîne symbolique et chaîne neuronale : l'articulation neuro-symbolique
1.  Descente d'un graphe de calcul à travers les dialectes
1.  Temps de calcul selon la taille du problème
1.  Le cycle empirique de la science des données
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
25
1.  Cinq disciplines qui préparent l'IA de demain
Tableaux
1.  La hiérarchie de Chomsky et son usage en intelligence artificielle
2.  Programmation logique : de la clause a l'inférence
3.  Ce que l'impossibilité impose en pratique
1.  Programmation fonctionnelle et réseaux de neurones
1.  Les dialectes de la chaîne de compilation
2.  Les quatre phases de la compilation d'un modèle
1.  Les classes de complexité et leur place en intelligence artificielle
2.  Les quantités de la théorie de l'information en IA
1.  Les transformations de variables les plus courantes
2.  Indicateurs de classification et ce qu'ils mesurent
1.  Les cinq disciplines et ce que chacune éclaire
1.  Abréviations employées dans le cours
1.  Symboles mathématiques et leur signification
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
26
Fin du document
Intelligence Artificielle Avancée & Federated Learning — Fondations mathématiques de
l'apprentissage automatique, algorithmes fédérés, protection de la vie privée, défense contre les attaques,
grands modèles de langage fédérés, systèmes embarqués, renforcement appris, applications critiques
(santé, V2X), plateforme de référence FedX et feuille de route de recherche.<br/>Ghiloufi Jamel,
Architecte Logiciel Principal — Pixel Software Design<br/>Département de Recherche & Développement
— Recherche<br/>Pixel Software Design — Édition 2026
© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou
diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans
autorisation écrite préalable de l'auteur.
Document généré automatiquement le 29/09/2026 — mise en page Pixel Software Design.
"""


IA_DONNEES_BIGDATA_TEXT = r"""Pixel Software Design — Département de Recherche & Développement
PIXEL SOFTWARE DESIGN
Département de Recherche & Développement
Intelligence Artificielle
Avancée
& Federated Learning
•  Fondations de l'intelligence artificielle
•  Algorithmes d'apprentissage fédéré
•  Confidentialité, attaques et défenses
•  Applications et grands modèles fédérés
•  Framework FedX de référence
•  Nouveaux fronts de recherche
•  Travaux pratiques, projets et évaluation
Auteur
Ghiloufi Jamel
Fonction
Architecte Logiciel Principal
Direction
Département de Recherche & Développement
Service
R&D - Intelligence Artificielle Avancée & Apprentissage Fédéré
Niveau
Recherche
Édition
Édition 2026 — 1.0
Copyright
© Pixel Software Design
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou
diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans
autorisation écrite préalable de l'auteur.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
2
Copyright et mentions légales
Éditeur
Pixel Software Design
Auteur
Ghiloufi Jamel
Fonction
Architecte Logiciel Principal
Département
Département de Recherche & Développement
Intitulé
Intelligence Artificielle Avancée & Federated Learning
Sous-titre
Fondations mathématiques de l'apprentissage automatique, algorithmes fédérés,
protection de la vie privée, défense contre les attaques, grands modèles de langage
fédérés, systèmes embarqués, renforcement appris, applications critiques (santé,
V2X), plateforme de référence FedX et feuille de route de recherche.
Édition
Édition 2026 (version 1.0)
Langue
Français
Niveau
Recherche
Collection
Supports de formation et de recherche, Pixel Software Design
Droits d'auteur
© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation
ou diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite
sans autorisation écrite préalable de l'auteur.
Droits de l'auteur. Ghiloufi Jamel est l'auteur unique de l'ensemble du contenu scientifique, pédagogique et
technique de cet ouvrage. Toute adaptation, traduction, reproduction ou exploitation, y compris partielle, requiert
une autorisation écrite préalable.
Droits des tiers. Les algorithmes, modèles et travaux cités restent la propriété de leurs auteurs respectifs. Les
références employées figurent en fin d'ouvrage, ce qui permet de remonter au travail original pour toute
affirmation chiffrée.
Marques et licences externes. PyTorch, TensorFlow, Flower, Opacus, MONAI, scikit-learn et PySyft sont des
logiciels libres sous licences respectives (BSD, Apache 2.0, MIT). Leur usage dans ce document est purement
pédagogique et n'emporte aucune prescription commerciale.
Mentions relatives aux données et aux expérimentations
Document pédagogique à usage de formation interne. Les exemples de code fournis sont livrés à titre pédagogique
; les résultats numériques illustrés sont issus d'expérimentations conduites dans un cadre de recherche et ne
constituent pas des performances de production.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
3
Ce support synthétise les travaux de recherche du Département de Recherche & Développement de Pixel Software
Design sur l'intelligence artificielle distribuée, l'apprentissage fédéré, la protection de la vie privée et les systèmes
embarqués intelligents.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
4
Sommaire
Structure détaillée du cours
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 8
Partie 1 — IA, Données et Systèmes Distribués
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 9
1.1 Apprentissage automatique : typologie et chaîne de production
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 12
1.2 Observabilité et supervision des systèmes
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 18
1.3 Calcul et analyse de graphes
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 22
1.4 Fouille de données
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 27
1.5 Systèmes Big Data et architectures distribuées
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 40
Annexes
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 41
A.1 Liste des abréviations
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 41
A.2 Table de notation
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
5
Partie
Thème
Contenu
Compétence visée
Durée
Partie 1
Fondations
Statistique, optimisation, courbes d'apprentissage
Comprendre et formaliser
2-3 semaines
Partie 2
Algorithmes FL
FedAvg, convergence, hétérogénéité, système
Implémenter et régler
3-4 semaines
Partie 3
Confidentialité
DP, attaques, défenses, agrégation sécurisée
Auditer et sécuriser
2-3 semaines
Partie 4
Applications
FedLLM, santé, V2X, FedRL, TinyML, graphes
Transposer à un domaine
3-4 semaines
Partie 5
Framework FedX
Architecture, API, benchmarks, exploitation
Industrialiser
2 semaines
Partie 6
Nouveaux fronts
FedCL, FedCI, SNN, FedGL, feuille de route
Ouvrir la recherche
2 semaines
Partie 7
TP et projets
9 labs, 5 projets, corrigés, évaluation
Faire et rendre
4-6 semaines
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
6
Préface
Comment utiliser ce cours
Ce support est conçu pour un parcours de formation et de recherche couvrant l'ensemble de la chaîne de valeur de
l'intelligence artificielle distribuée : les fondations mathématiques, les algorithmes d'apprentissage fédéré, les
menaces et défenses, les applications de pointe, une plateforme de référence opérationnelle, et enfin les nouveaux
fronts ouverts par la recherche du Département.
Ce n'est pas un manuel de référence à lire d'un trait : c'est un manuel opératoire. Chaque chapitre alterne
exposition, formalisation, mise en œuvre numérique et évaluation. Les listings sont complets et exécutables ; les
tableaux comparatifs servent de grille de décision ; les schémas d'architecture servent de support de revue de
conception.
Public et prérequis
Le contenu s'adresse à des étudiants de master et de doctorat, à des ingénieurs IA et à des praticiens de la
recherche appliquée. Les prérequis sont la connaissance de l'apprentissage automatique classique, de
l'algorithmique numérique et des bases de probabilités. Les parties 1 à 3 sont auto-suffisantes pour un étudiant qui
découvre le domaine ; les parties 4 à 7 supposent la mécanique et les outils présentés dans la partie 2.
Conventions de lecture. Une expression mathématique est encadrée par deux signes dollars ; un identifiant, un
fichier ou une commande est écrit en caractères à chasse fixe ; les encadrés Définition, Théorème, Méthode et
Attention signalent les points à maîtriser et les pièges fréquents. Les renvois de la forme « voir chapitre 3.2 »
désignent le second chapitre de la troisième partie.
Progression pédagogique
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
7
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
8
Apprentissage, observabilité, graphes, fouille et Big Data
Partie 1
IA, Données et Systèmes
Distribués
Les cinq piliers de la chaîne de valeur numérique. On part du modèle qui apprend, on passe à la
mesure du système qui le sert, puis aux structures qui relient les entités, aux méthodes qui extraient
des connaissances, et enfin aux architectures qui rendent l'ensemble possible à l'échelle. Chaque
module indiqué les outils de référence, mais l'accent est sur la décision de conception qui les
sous-tend.
Objectifs de la partie
• Distinguer une tâche d'apprentissage d'un outil, et choisir l'un avant l'autre.
• Concevoir une chaîne d'observabilité en tenant compte du volume, de la rétention et du coût.
• Implémenter et comparer un plus court chemin, une centralité et une détection de communauté.
• Extraire des règles d'association et juger leur intérêt par le support et la confiance.
• Concevoir un traitement par lots ou en flux, et justifier ce choix en latence et en exactitude.
Plan de la partie
1.  Apprentissage automatique : typologie et chaîne de production
2.  Observabilité et supervision des systèmes
3.  Calcul et analyse de graphes
4.  Fouille de données
5.  Systèmes Big Data et architectures distribuées
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
9
Chapitre 1.1
Apprentissage automatique : typologie et
chaîne de production
Le choix de l'algorithme vient après le choix de la question. L'inverse est l'erreur la plus répandue.
La typologie : quatre questions, pas une liste d'outils
L'apprentissage automatique se classe selon la disponibilité des étiquettes, la nature de la sortie, et le
moment où l'erreur est révélée. Ces trois axes suffisent à couvrir toutes les situations rencontrées en
production.
Situation
Sortie attendue
Exemples d'algorithmesQuestion à
poser d'abord
Supervisé, sortie continue
un 
nombrerégression
linéaire, forêt, réseau
quelle erreur coûte le plus cher ?
Supervisé, sortie discrète
une classe
régression 
logistique, 
machines 
à
vecteurs de support, arbre
quel est le coût d'un faux positif,
d'un faux négatif ?
Non supervisé, structure
des groupes
k-moyens, densité, hiérarchique
le 
découpage 
obtenu 
est-il
interprétable ?
Non supervisé, compression
moins de dimensions
analyse en composantes principales,
voisinage
quelle variance faut-il vraiment
garder ?
Renforcement
une politique d'actions
gradient de politique, recherche de
politique
quelle récompense mesure-t-on
réellement ?
Tableau 1 — Les situations d'apprentissage et l'algorithme correspondant
La dernière colonne est la seule qui compte vraiment. Un algorithme choisi avant la question conduit à un modèle
impossible à évaluer correctement.
y = w⊤ x + b, ŷ - y ⇒ w ← w - η ≤ft( w⊤ x - y ) x
p(y = 1 | x) = σ ≤ft( w⊤ x + b ), σ(z) = (1)/(1 + e-z)
(D.1)
La régression linéaire ajuste une droite et se corrigé par l'erreur résiduelle. La régression logistique ajuste une
probabilité : la sigmoïde borne la sortie entre zéro et un, ce qui la rend utilisable comme score de confiance.
Astuce
La réduction de dimension et la segmentation partagent la même question sous-jacente : que perdre en échange
de ce qu'on gagne ? L'analyse en composantes principales maximise la variance conservée et rend le résultat
linéaire et lisible ; les méthodes de voisinage sont plus expressives et bien moins interprétables. Le choix se fait
sur la nécessité ou non d'expliquer.
La chaîne de production d'un modèle
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
10
Algorithme 1 — De la donnée brute au modèle déployé
01  Recueillir, identifier la source, horodater chaque enregistrementContrôler la qualité :
valeurs manquantes, doublons, valeurs aberrantes
02  Corriger les erreurs de mesure connues par le métier
03  Séparer en trois jeux disjoints, avant toute transformation
04  Transformer : normalisation, encodage des catégories, réduction de dimension
05  Entraîner sur le jeu d'entraînement, ajuster sur le jeu de validation
06  Évaluer une seule fois sur le jeu de test, jamais avant
07  Rendre reproductible : version des données, du code, de la configuration
08  Déployer sous conteneur, surveiller, et prévoir le retour arrière
Entrées : Données brutes, question métier, contrainte de coût d'erreur • Sorties : Modèle versionné, jeu
d'évaluation, rapport de métriques • Complexité : Effort dominant : la préparation, pas l'entraînement
La ligne 4 est irremplaçable et presque toujours faite trop tard. Séparer après avoir préparé les données laisse
fuiter de l'information du test dans l'entraînement, et rend l'estimation optimiste.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
11
1from dataclasses import dataclass
2from typing import Sequence
3
4import numpy as np
5from sklearn.metrics import f1_score, precision_score, recall_score
6
7
8@dataclass(frozen=True)
9class RègleDePromotion:
10''"Verdict de promotion d'une version de modele.
11
12Une version n'est acceptee que si elle ameliore au moins une metrique
13globale, si aucune metrique de sous-groupe ne se degrade au-dela du
14seuil, et si elle respecte les contraintes de cout et de latence.
15
16Le critere sur les sous-groupes est celui qu'on oublie le plus souvent.
17Un modele peut gagner deux points de precision globale en degradant
18severement un groupe de dix pour cent de la population : la moyenne
19masque exactement ce qui doit etre surveille.
20''"
21
22gain_minimal: float = 0.005
23perte_toleree: float = 0.01
24latence_max_ms: int = 200
25
26def accepter(self, candidat: dict, reference: dict,
27sous_groupes: Sequence[str]) -> tuple[bool, dict]:
28ecarts: dict = {}
29accepte = True
30
31for groupe in sous_groupes:
32ecarts[groupe] = candidat[groupe] - reference[groupe]
33if ecarts[groupe] < -self.perte_toleree:
34accepte = False
35
36gain = candidat["global"] - reference["global"]
37ecarts["global"] = gain
38if gain < self.gain_minimal:
39accepte = False
40
41if candidat.get("latence_ms", 0) > self.latence_max_ms:
42accepte = False
43
44return accepte, ecarts
45
46
47def rapporter(y_true: np.ndarray, y_pred: np.ndarray,
48seuil: float = 0.5) -> dict:
49''"Transforme des scores continus en decisions, puis en metriques.
50
51Le seuil de 0,5 n'a aucune signification en soit : il doit etre choisi
52sur le jeu de validation, en fonction du cout relatif d'un faux
53positif et d'un faux negatif. C'est la seule decision de ce module
54qui demande un arbitrage metier, pas une mesure technique.
55''"
56decisions = (y_pred >= seuil).astype(int)
57return {
58"f1": f1_score(y_true, decisions),
59"precision": precision_score(y_true, decisions),
60"rappel": recall_score(y_true, decisions),
61"taux_refus": float((y_pred < seuil * 0.6).mean()),
62}
Listing 1 — Gouvernance d'un modèle : promotion et rapport de métriques
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
12
Exercice 1.1.1  (difficulte : Moyen)
Un modèle de crédit atteint 92 % de justesse sur l'ensemble de test, mais 71 % sur le plus petit groupe de
population. Calculer l'exactitude non pondérée par groupe, puis l'exactitude par groupe, et en déduire la part
de la population que la métrique globale cache. Que faut-il demander à l'équipe qui a produit ce chiffre ?
Indice : Un chiffre global n'est informatif que si l'on sait avec quelles populations il a été calculé.
Correction
• L'exactitude globale est une moyenne pondérée par la taille de chaque groupe. Si le groupe minoritaire pèse
dix pour cent de la population, la contribution de ses vingt et un points d'écart au score global est deux points :
exactement l'ordre de grandeur de l'écart annoncé. Il faut demander la décomposition complète par groupe et
la taille de chaque groupe.
A retenir
• La question précède l'algorithme, et le coût de l'erreur décide de la métrique.
• La séparation des jeux de données précède toute transformation, sinon l'estimation est optimiste.
• Une métrique globale masque les sous-groupes : la décomposition fait partie de la mesure.
• Le seuil de décision est un arbitrage métier, pas un paramètre technique.
Chapitre 1.2
Observabilité et supervision des systèmes
Savoir si un système fonctionne est la moitié du travail. Savoir pourquoi il ne fonctionne pas est
l'autre moitié.
La supervision historique consisted à interroger périodiquement un état : la machine est-elle allumée, la
connexion est-elle établie. L'observabilité moderne répond à une question plus difficile : dans un système
distribué, quelle est la cause de cet comportement observable ? Elle se construit sur trois signaux de nature
et de coût très différents.
Figure 1 — Les trois signaux de l'observabilité et leur échelle
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
13
Signal
Question à laquelle il répond
GranularitéCoût de conservation
Métrique
quel est le niveau et sa tendance ?une
valeur par fenêtre de temps
faible, on garde tout
Journal
que s'est-il passé à cet instant ?
un événement par ligne
élevé, on archive
Tracé
où le temps est-il passé ?
une 
portion 
par 
étape 
d'un
parcours
très élevé, on échantillonne
Événement métier
l'activité a-t-elle un sens ?
un changement d'état métier
faible, très haute valeur
Profil de charge
où va la charge, et pour qui ?
une requête analysée
moyen, 
protection 
des
données
Tableau 1 — Métriques, journaux, tracés : que répondre à quoi
La dernière ligne est la plus oubliée : un profil de charge répond à la seule question qui décide vraiment du budget, à
savoir quel usage consomme la ressource.
Figure 2 — Architecture de supervision : collecte, stockage, décision
Tirage ou poussée : une décision structurante
• Tirage : le collecteur interroge les cibles à intervalle fixe. L'application n'a rien à installer, et si elle
tombe en panne le collecteur le constate immédiatement. C'est le mode par défaut.
• Poussée : l'agent envoie ses valeurs. Indispensable quand la cible est derrière un pare-feu ou hors du
réseau d'administration, et pour les systèmes à très forte dispersion.
• Court délai de scrape : une fenêtre trop courte produit des mesures vides et du bruit ; une fenêtre trop
longue allonge la détection d'incident. Trente secondes est un compromis usuel.
• Conservation : la rétention doit être dégressive — finesse pour les dernières heures, compression
agressive au-delà.
Concevoir une règle d'alerte qui ne fatigue pas l'équipe
Une règle qui se déclenche sur un dépassement instantanée produit des centaines de notifications pour un seul
incident. Les règles utilisables partagent trois propriétés :
• Une condition de durée : l'anomalie doit persister plus longtemps qu'un pic normal, par exemple deux
minutes.
2. Une fenêtre de calcul : taux d'erreur sur cinq minutes, et non sur la dernière requête.
3. Une action liée à la gravité : avertissement pour surveillance, escalade vers un humain uniquement si la
durée franchit un seuil.
La meilleure mesure de la qualité d'un système d'alerte est le nombre d'alertes ignorées par semaine : s'il est
élevé, les règles sont trop nombreuses ou mal calibrées.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
14
tauxerreur = (Ntextéchec)(Δ)N0(Δ) ≥ s ∧ durée ≥ τ
(D.2)
Les deux conditions sont indissociables. Un taux d'erreur élevé pendant une seconde est du bruit ; un taux faible
maintenu deux minutes est une panne. C'est la conjonction qui distingue une alerte d'un signal.
Du symptôme à la cause : la méthode des quatre questions
• Symptôme : qu'est-ce qui est faux, vu de l'extérieur ? « Le service est lent pour 8 % des requêtes. »
• Changement : qu'est-ce qui a changé récemment ? Une version, une configuration, un volume, une
dépendance.
• Périmètre : qui est affecté, et par quoi cela se distingue-t-il ? Un pays, un type de client, un modèle de
requête.
• Cause : qu'est-ce qui explique simultanément le symptôme, le changement et le périmètre ?
La question la plus difficile est la quatrième, et c'est celle que l'observabilité bien conçue permet de trancher
en quelques minutes au lieu de plusieurs heures. Un identifiant de corrélation propagé dans toutes les
couches vaut souvent davantage que n'importe quel tableau de bord supplémentaire.
Surveillance d'un modèle et surveillance d'un service
Un service peut être parfaitement sain — latence normale, aucune erreur — et le modèle qu'il sert dégradé : les
réponses sont plus courtes, plus vagues, ou silencieusement biaisées. La supervision technique ne voit rien. Il
faut donc surveiller la qualité séparément : distribution des entrées, taux de refus, longueur des réponses, et
surtout décomposition des métriques par groupe.
Travaux pratiques 1.1 — Superviser un service distribué de bout en bout
Duree : 3 h  |   Niveau : Intermédiaire  |   Outils : Prometheus pour la collecte, Grafana pour la visualisation, un jeu de
requêtes reproduisant le trafic
Mettre en place une chaîne d'observabilité complète sur un service à trois composants, avec une règle
d'alerte calibrée et un tableau de bord exploitable.
Deroulement
1. Exposer une métrique de latence par percentile et un compteur d'erreurs par code de retour dans une
application à trois composants.
2. Configurer la collecte en mode tirage, puis vérifier la continuité des séries en cas d'arrêt d'un
composant.
3. Écrire une règle d'alerte sur le taux d'erreur avec condition de durée, et déclencher une panne simulée
pour vérifier qu'elle se déclenche une fois, pas plus.
4. Construire un tableau de bord en trois volets : santé technique, santé de la qualité, répartition de la
charge par type de client.
5. Éteindre un composant pendant deux minutes et consigner le délai de détection, puis le délai de
restauration.
6. Rédiger la règle d'escalade : qui est prévenu, par quel canal, à quelle heure.
Livrable attendu
• F
• i
• c
• h
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
15
• i
• e
• r
• d
• e
• c
• o
• n
• f
• i
• g
• u
• r
• a
• t
• i
• o
• n
• d
• u
• c
• o
• l
• l
• e
• c
• t
• e
• u
• r
• ,
• t
• a
• b
• l
• e
• a
• u
• d
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
16
• e
• b
• o
• r
• d
• ,
• r
• è
• g
• l
• e
• d
• '
• a
• l
• e
• r
• t
• e
• ,
• p
• r
• o
• c
• é
• d
• u
• r
• e
• d
• '
• e
• s
• c
• a
• l
• a
• d
• e
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
17
• ,
• e
• t
• r
• e
• l
• e
• v
• é
• d
• e
• s
• d
• é
• l
• a
• i
• s
• d
• e
• d
• é
• t
• e
• c
• t
• i
• o
• n
• e
• t
• d
• e
• r
• e
• s
• t
• a
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
18
• u
• r
• a
• t
• i
• o
• n
• .
Bareme indicatif
Critere
Points
L'alerte se déclenche exactement une fois sur la panne simulée
5
Le tableau de bord nomme le composant responsable en moins de deux minutes
3
La procédure d'escalade nomme un responsable et un délai
2
A retenir
• Métriques, journaux et tracés ont des coûts et des durées de conservation différents : on ne garde pas tout au
même niveau.
• Une alerte utile est une conjonction de seuil et de durée, jamais un dépassement instantané.
• Le nombre d'alertes ignorées par semaine mesure la qualité du système d'alerte.
• La qualité d'un modèle se surveille séparément de la santé technique du service.
Chapitre 1.3
Calcul et analyse de graphes
Dès qu'une question porte sur des relations, la structure naturelle n'est pas la table mais le graphe.
Une base relationnelle répond vite à « quelles sont les lignes qui satisfont cette condition ». Elle répond mal
à « quels sont les trois sauts qui séparent ces deux entités, et quel sommet se trouve sur tous les chemins
possibles ». La deuxième question est une question de parcours dans un graphe, et elle est centrale en
analyse de réseaux sociaux, en itinéraires, en détection de fraude et en recherche d'information.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
19
Figure 1 — Un graphe, ses trois lectures et les questions qui en dépendent
G = (V, E), E ⊆ V × V, deg+(v) = ≤ft| (v, u) ∈ E |
PR(v) = (1 - α)(1)/(N) + α ∑u → v(PR(u))/(deg+(u))
(D.3)
La première expression fixe le vocabulaire : sommets, arêtes, degré sortant. La seconde est l'équation de
PageRank : un sommets vaut une part constante, plus ce que ses voisins lui transmettent au prorata de leur
propre nombre de liens.
Le plus court chemin : deux algorithmes, deux usages
Dijkstra
A*
Principe
on explore par coût croissant du cheminon
explore par coût estimé du chemin complet
Fonction de coût
poids réels des arêtes
poids réels plus une estimation du coût restant
Condition de validité
poids positifs ou nuls
estimation admissible : jamais supérieure au coût réel
Garanti optimal
toujours
seulement si l'estimation est admissible
Coût
explore tout le voisinage atteint
dirigé, explore beaucoup moins
Usage
plus court chemin depuis une source unique
navigation, planification, jeux
Tableau 1 — Dijkstra et A* : le même principe, deux conditions
L'estimation admissible n'a pas besoin d'être précise : elle n'a pas besoin de sous-estimer le coût restant. Une estimation
qui surestime transforme A* en recherche gloutonne : plus rapide, mais elle peut renvoyer une solution dégradée sans le
signaler.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
20
1import heapq
2from collections import defaultdict
3from typing import Callable, Iterable
4
5
6def plus_court_chemin(graphe: dict[str, list[tuple[str, float]]],
7depart: str, arrivee: str) -> tuple[float, list[str]]:
8''"Recherche gloutonne avec file de priorite.
9
10La file de priorite impose l'ordre d'exploration : le sommet traite
11est toujours celui dont le cout cumule est le plus faible. Ce detail
12est la seule difference avec une file d'attente ordinaire, et c'est
13lui qui fait passer la complexite de quadratique a quasi lineaire.
14''"
15if depart not in graphe:
16return float("inf"), []
17
18couts: dict[str, float] = {depart: 0.0}
19precedents: dict[str, str] = {}
20vus: set[str] = set()
21file: list[tuple[float, str]] = [(0.0, depart)]
22
23while file:
24cout, sommet = heapq.heappop(file)
25if sommet in vus:
26continue
27vus.add(sommet)
28
29if sommet == arrivee:
30chemin = [arrivee]
31while chemin[-1] != depart:
32chemin.append(precedents[chemin[-1]])
33return cout, list(reversed(chemin))
34
35for voisin, poids in graphe.get(sommet, ()):
36nouveau = cout + poids
37if nouveau < couts.get(voisin, float("inf")):
38couts[voisin] = nouveau
39precedents[voisin] = sommet
40heapq.heappush(file, (nouveau, voisin))
41
42return float("inf"), []
43
44
Listing 1 — Plus court chemin : Dijkstra et A* dans un même module
45def plus_court_chemin_cible(
46graphe: dict[str, list[tuple[str, float]]],
47distance: Callable[[str, str], float],
48depart: str, arrivee: str) -> tuple[float, list[str]]:
49''"Meme algorithme, avec estimation admissible du cout restant.''"
50couts = {depart: 0.0}
51precedents: dict[str, str] = {}
52vus: set[str] = set()
53file: list[tuple[float, float, str]] = [
54(distance(depart, arrivee), 0.0, depart)]
55
56while file:
57_, cout, sommet = heapq.heappop(file)
58if sommet in vus:
59continue
60vus.add(sommet)
61if sommet == arrivee:
62chemin = [arrivee]
63while chemin[-1] != depart:
64chemin.append(precedents[chemin[-1]])
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
21
65return cout, list(reversed(chemin))
66
67for voisin, poids in graphe.get(sommet, ()):
68nouveau = cout + poids
69if nouveau < couts.get(voisin, float("inf")):
70couts[voisin] = nouveau
71precedents[voisin] = sommet
72priorite = nouveau + distance(voisin, arrivee)
73heapq.heappush(file, (priorite, nouveau, voisin))
74
75return float("inf"), []
Figure 2 — PageRank : un sommet vaut ce que valent ses voisins
Les mesures de centralité et ce qu'elles/signalent
Mesure
Question à laquelle elle répond
InterprétationDomaine d'usage
Degré
combien 
de 
relations 
directes
?popularité brute, facilement trompeuse
réseaux sociaux, epidemiology
PageRank
combien de reputable neighbours ?
influence 
propagée 
par 
le 
graphe
orienté
recherche, influence
Médiation
sur quels chemins ce sommet est-il
indispensable ?
goulot 
d'étranglement, 
pont 
entre
communautés
analyse de réseau, fraude
Proximité
combien de chemins courts vers tous les
autres ?
position périphérique ou centrale
diagnostic de réseau
Communauté
quels 
sommets 
se 
ressemblent
structurellement ?
groupes denses à l'intérieur, clairs entre
eux
segmentation, détection de
fraude coordonnée
Tableau 2 — Quatre mesures, quatre questions
Le degré n'est presque jamais la bonne mesure. Un sommet très connecté peut n'être connu que d'un seul groupe. Ce qui
compte, c'est la qualité des voisins, pas leur nombre.
Un compte suivie par cent mille personnes sans activité, et relayé par elles, a un degré élevé et une
influence nulle. La mesure juste regarde vers qui pointe chaque arête, et non seulement combien il y en a.
Confondre les deux conduit à recommander des éléments que personne ne consumera réellement.
Le piège du degré comme mesure d'influence
Astuce
Pour la détection de fraude en transactions, la mesure utile est presque toujours la médiation plutôt que le degré
: un compte intermédiaire qui apparaît sur les plus courts chemins entre plusieurs comptes est bien plus suspect
qu'un compte très actif.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
22
A retenir
• Les questions de parcours et de relations exigent une structure de graphe, pas des jointures récursives.
• A* est optimal si et seulement si son estimation du coût restant est admissible.
• Le PageRank mesure une influence propagée, pas un nombre de relations.
• La médiation signale les sommets indispensables aux parcours, donc les goulots d'étranglement.
Chapitre 1.4
Fouille de données
Extraire des connaissances ne signifie pas trouver des corrélations : cela signifie en trouver qui
resistent à une vérification.
Figure 1 — Les quatre tâches de la fouille de données
Classification : l'arbre comme langage de décision
Un arbre de décision est une suite de questions binaries. Chaque nœud pose une question sur une variable,
chaque feuille porte une prédiction. Le critère de choix de la question de premier rang est la réduction
d'incertitude qu'elle procure.
Entropie(S) = - ∑c ∈ C (|Sc|)/(|S|) log2 (|Sc|)/(|S|)
Gain(S, A) = Entropie(S) - ∑v (|Sv|)/(|S|) Entropie(Sv)
(D.4)
L'entropie mesure l'hétérogénéité des étiquettes. Le gain est la réduction obtenue en séparant les données
selon la variable testée. L'arbre retient la variable de gain maximal, et recommence sur chaque partition.
Surapprentissage, là où presque tout se joue
Un arbre sans contrainte memorise chaque feuille d'entraînement et donne une exactitude parfaite en validation
sur les mêmes données, puis une exactitude médiocre sur des données nouvelles. Les trois coupes principales
sont : limiter la profondeur, imposer un nombre minimal d'exemples par feuille, et élaguer les branches dont le
gain est inférieur à un seuil. La forêt aléatoire va plus loin : elle construit des arbres sur des tirages aléatoires
des variables et des exemples, puis moyenne leurs décisions. La dispersion d'un seul arbre devient une
estimation de l'incertitude, ce qui est souvent la seule chose qui manque à une décision.
Segmentation : deux philosophies
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
23
K-moyens
Densité
Principe
minimise 
la 
dispersion 
autour 
de
centroïdesregroupe les zones denses séparées par
du vide
Nombre de groupes
fixé à l'avance
découvert, non paramétrique
Forme des groupes
sphérique, de taille voisine
arbitraire, taille inégale
Bruit
assigné au groupe le plus proche
peut être identifié et exclu
Valeur d'initialisation
critique, plusieurs essais
peu importante
Choix du paramètre
nombre de groupes
rayon de voisinage et seuil
Limite principale
impose une forme aux données réelles
sensible aux échelles de densité
Tableau 1 — K-moyens et densité : ce qui les sépare
K-moyens suppose que les groupes sont compacts. Sur des données réelles en orbites concentriques, il échoue
complètement : la densité est alors le bon choix, parce qu'elle n'impose aucune forme.
Figure 2 — Apriori : du treillis d'items fréquents à une règle
support(A → B) = (n(A ∪ B))/(N), confiance(A → B) = (n(A ∪ B))/(n(A))
(D.5)
Le support mesure la fréquence de la co-occurrence, la confiance mesure la probabilité conditionnelle. Une règle
à forte confiance et faible support décrit une co-occurrence rare mais parfaitement fiable — ce n'est pas pour
autant une rête exploitable.
Juger une règle d'association, dans l'ordre
• Support : combien de transactions ? En dessous de la centaine, la règle n'a aucun usage statistique.
2. Confiance : la consequent est-il réellement tiré par l'antécédent, ou seulement par sa fréquence propre ?
3. Levier : la confiance exceede-t-elle nettement la fréquence de la consequent seule ? C'est le seul test qui
distingue une vraie règle d'un artefact de fréquence.
4. Négativité : le nombre de règles est tsunami : cent transactions en produisent des milliers. Il faut un critère
de sélection final, sinon personne ne lira le résultat.
5. Décision : une règle n'est un résultat que si elle déclenche une action mesurable et évaluable.
Détection d'anomalies : deux approches, deux usages
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
24
Approche par densité
Approche par reconstruction
Principe
mesure 
la 
rareté 
d'un 
point 
dans 
son
voisinagereconstruit l'entrée et mesure l'écart
Exemple
isolation des arbres
auto-encodeur
Exigence
une notion de voisinage
des données d'entraînement représentatives
Force
simple, explicable, détecte l'inconnu
capte des anomalies de forme complexe
Faiblesse
sensible à l'échelle et à la densité
une anomalie fréquente dans l'entraînement devient
normale
Usage
détection de fraude bancaire, intrusion
contrôle industriel, maintenance prédictive
Tableau 2 — Anomalies par densité et par reconstruction
La faiblesse de l'auto-encodeur est un problème de données, pas de méthode : ce qui était rare à l'entraînement devient
la norme, et le modèle l'apprendra comme tel.
Un patient en état critique et une panne machine produisent la même signature statistique.
Statistiquement, la détecter est aisé ; deciding qu'elle doit déclencher une alerte relève du métier. Sans
cette règle métier écrite, un système de détection d'anomalies produit un flux d'alertes que personne ne
traité, ce qui est pire que pas de système du tout.
L'anomalie qui n'est pas une erreur
Travaux pratiques 1.2 — Panier de marché et détection d'anomalies
Duree : 4 h  |   Niveau : Avance  |   Outils : Un jeu de transactions en trois colonnes : identifiant de panier, article, quantité
Extraire des règles d'association exploitables d'un panier réel, puis construire un score d'anomalie
reproductible sur les transactions d'un client.
Deroulement
1. Écrire le générateur d'itemsets fréquents par largeur croissante, en éliminant les candidats dont un
sous-itemset est infrequent.
2. Mesurer le support, la confiance et le levier de toutes les règles extraites, puis justifier le critère qui
retient les trois meilleures.
3. Afficher la courbe de nombre de règles en fonction du seuil de support, et expliquer la forme observée.
4. Construire un score d'anomalie fondé sur la rareté locale, puis l'appliquer aux transactions d'un même
client et commenter les cinq plus fortes anomalies.
5. Répondre par écrit : parmi ces anomalies, lesquelles justifient une enquête, et sur quel critère métier ?
Livrable attendu
• M
• o
• d
• u
• l
• e
• P
• y
• t
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
25
• h
• o
• n
• ,
• t
• a
• b
• l
• e
• a
• u
• d
• e
• s
• r
• è
• g
• l
• e
• s
• a
• v
• e
• c
• l
• e
• u
• r
• s
• t
• r
• o
• i
• s
• m
• e
• s
• u
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
26
• r
• e
• s
• ,
• c
• o
• u
• r
• b
• e
• d
• e
• s
• é
• l
• e
• c
• t
• i
• o
• n
• ,
• n
• o
• t
• e
• d
• '
• a
• n
• a
• l
• y
• s
• e
• s
• u
• r
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
27
• l
• e
• s
• a
• n
• o
• m
• a
• l
• i
• e
• s
• d
• é
• t
• e
• c
• t
• é
• e
• s
• .
Bareme indicatif
Critere
Points
La règle est justifiée par le levier, non par la seule confiance
4
Le nombre de règles en fonction du seuil est expliqué
2
L'analyse distingue ce qui est statistique et ce qui est décisionnel
4
A retenir
• Un arbre se construit par gain maximal d'information et se contraint par élagage, profondeur minimale et taille
de feuille.
• La dispersion d'une forêt aléatoire fournit une estimation d'incertitude qu'un arbre seul ne donné pas.
• K-moyens impose une forme aux groupes, la densité ne l'impose pas : le choix suit les données.
• Une règle d'association n'est exploitable qu'après le test du levier et un critère de sélection explicite.
Chapitre 1.5
Systèmes Big Data et architectures
distribuées
Distribuer n'est pas une optimisation de performance : c'est la condition pour accepter l'échelle,
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
28
avec le prix de la cohérence.
Figure 1 — Les cinq dimensions du Big Data et leur contrepartie technique
Pourquoi distribuer, et à quel prix
On distribue lorsque la donnée ne tient pas sur une machine, ou lorsque le débit d'écriture dépasse ce qu'un
seul disque n'encaisse. La distribution résout ces deux problèmes et en introduit un troisième : la cohérence.
Dans un système à plusieurs machines, deux lectures consécutives peuvent voir des états différents, et toute
transaction qui traverse plusieurs nœuds doit être coordonnée.
Acquis
Coût correspondingly
Capacité de stockage extensiblela donnée est
découpée, l'accès doit connaître la découpe
Débit d'écriture et de lecture
la charge doit être répartie sans déséquilibre
Tolérance à la panne
il faut détecter et reconstruire, et le diagnostic devient plus difficile
Extensibilité linéaire
la coordination coûte, et son coût croît avec le nombre de machines
Isolation des charges
le partage de ressources crée des interférences imprévisibles
Tableau 1 — Ce que la distribution achète et ce qu'elle coûte
La dernière ligne est la plus sous-estimée. Sur un cluster partagé, une requête lourde peut dégrader toutes les autres sans
qu'aucune métrique ne le signale individuellement.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
29
Figure 2 — Architecture de référence : la chaîne de données en cinq étages
Stockage : pourquoi la disposition en colonnes change tout
• Stockage par lignes : une ligne complète est l'unité lue. Bon pour les mises à jour ponctuelles, coûteux
pour l'analyse, qui lit quelques colonnes de millions de lignes.
• Stockage par colonnes : seule la colonne demandée est lue, et les valeurs d'une même colonne se
compressent très bien. C'est la disposition qui rend praticable l'analyse sur de grands volumes.
• Indexation : l'index, les listes triées, accélère la sélection mais ralentit l'écriture. Sur un système à forte
écriture, c'est un arbitrage permanent.
• Partage : répartir par plage de clés met les écritures réparties, mais rend les parcours multi-clés plus
coûteux.
Traitement : deux philosophies
Figure 3 — Traitement par lots contre traitement en flux
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
30
Critère
Par lots
En flux
Choix pratique
Latence
minutes à heures
millisecondesle flux si l'action doit
suivre l'événement
Exactitude
voit l'intégralité de la période
estimate, corrigée ensuite
le lot si le calcul doit être exact
Reprise
relance complète
reprise au point de reprise
flux, si l'état est externalisé
Coût
bon pour de gros volumes
coût par unité plus élevé
lots pour l'historique, flux pour le
direct
Complexité
faible
gestion d'état, temps d'événement
commencer par lots
Tableau 2 — Par lots, en flux, ou les deux
En pratique, les deux coexistent presque toujours : flux pour l'alerte immédiate, lots pour la consolidation exacte. C'est
l'architecture de référence, pas le choix binaire.
Traiter un flux : fenêtre, temps et état
Trois notions à décider avant d'écrire la première ligne :
• Fenêtre : par temps fixe (une minute) ou par nombre d'événements (les mille premiers) ? La première donne
un temps constant, la seconde un volume constant.
2. Temps d'événement : l'horodatage du capteur, qui peut être en retard, ou l'horodatage de réception, qui est
toujours juste. Le premier est plus fidèle, le second plus simple.
3. État : les traitements inhomogènes supposent de conserver un état au-delà d'un événement. Cet état doit être
periodically sauvegardé, sinon une panne le perd.
L'erreur la plus courante consiste à traiter un flux comme un lot : sans fenêtre, chaque événement est traité seul
et aucun agrégat n'est possible.
Astuce
Quand vous ne savez pas si un calcul doit être exact ou approximé, la réponse est de faire les deux : l'un en flux
pour l'alerte, l'autre en lots pour la consolidation. Les deux résultats doivent se rejoindre à une marge près ;
l'écart entre eux est lui-même un excellent signal de supervision.
Cadre juridique de l'usage des données
Le traitement de données à grande échelle est encadré, en particulier pour les données personnelles : finalité
déterminée, base légale explicite, minimisation des données collectées, information des personnes concernées,
et droit d'opposition et d'effacement. Ces principes sont indépendants de la technique : un entrepôt distribué
n'améliore ni n'aggrave la conformité, il rend simplement l'incapacité à répondre à une demande de suppression
beaucoup plus coûteuse — parce qu'il faut retrouver toutes les copies. C'est le premier argument à opposer
avant de distribuer une donnée.
Projet — Concevoir une chaîne complète, de la source à la restitution
Duree : 6 semaines | Equipe : 3 a 5 etudiants | Depot : gitlab + rapport
Une entreprise de logistique veut suivre ses véhicules, détecter les anomalies de conduite et produire un
tableau de bord temps réel, tout en conservant un historique exact pour la facturation. Le volume annuel
est de l'ordre de deux milliards d'enregistrements.
Missions
1. Spécifier le schéma des événements, en distinguant ce qui est stocké, ce qui est agrégé et ce qui est jeté.
2. Choisir le découpage du stockage, en justifiant le critère de répartition et ses conséquences sur les
requêtes d'intervalle.
3. Définir la fenêtre de temps et le temps d'événement du traitement de flux, puis écrire la règle d'alerte
sur la détection d'anomalie de conduite.
4. Concevoir la consolidation exacte par lots, et indiquer comment elle se réconcilie avec l'alerte de flux.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
31
5. Écrire le plan de reprise après panne : ce qui est reconstruit, en combien de temps, et ce qui est perdu
dans l'intervalle.
6. Établir ce qu'il faut pour répondre à une demande d'effacement d'un conducteur, en traversant toute la
chaîne.
Livrables
• D
• o
• c
• u
• m
• e
• n
• t
• d
• '
• a
• r
• c
• h
• i
• t
• e
• c
• t
• u
• r
• e
• e
• n
• c
• i
• n
• q
• é
• t
• a
• g
• e
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
32
• s
• ,
• s
• c
• h
• é
• m
• a
• d
• e
• d
• é
• c
• o
• u
• p
• a
• g
• e
• ,
• p
• l
• a
• n
• d
• e
• r
• e
• p
• r
• i
• s
• e
• a
• p
• r
• è
• s
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
33
• p
• a
• n
• n
• e
• ,
• e
• t
• n
• o
• t
• e
• s
• u
• r
• l
• a
• c
• o
• n
• f
• o
• r
• m
• i
• t
• é
• a
• u
• x
• d
• e
• m
• a
• n
• d
• e
• s
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
34
• d
• '
• e
• f
• f
• a
• c
• e
• m
• e
• n
• t
• .
Évaluation
• L
• e
• j
• u
• r
• y
• v
• é
• r
• i
• f
• i
• e
• t
• r
• o
• i
• s
• p
• o
• i
• n
• t
• s
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
35
• :
• l
• e
• c
• r
• i
• t
• è
• r
• e
• d
• e
• d
• é
• c
• o
• u
• p
• a
• g
• e
• e
• s
• t
• j
• u
• s
• t
• i
• f
• i
• é
• p
• a
• r
• l
• e
• t
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
36
• y
• p
• e
• d
• e
• r
• e
• q
• u
• ê
• t
• e
• ,
• l
• a
• r
• é
• c
• o
• n
• c
• i
• l
• i
• a
• t
• i
• o
• n
• e
• n
• t
• r
• e
• f
• l
• u
• x
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
37
• e
• t
• l
• o
• t
• s
• e
• s
• t
• e
• x
• p
• l
• i
• c
• i
• t
• e
• ,
• e
• t
• l
• '
• e
• f
• f
• a
• c
• e
• m
• e
• n
• t
• e
• s
• t
• t
• r
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
38
• a
• i
• t
• é
• c
• o
• m
• m
• e
• u
• n
• e
• c
• o
• n
• t
• r
• a
• i
• n
• t
• e
• d
• e
• c
• o
• n
• c
• e
• p
• t
• i
• o
• n
• e
• t
• n
• o
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
39
• n
• c
• o
• m
• m
• e
• u
• n
• v
• e
• r
• r
• o
• u
• .
A retenir
• La distribution achète de l'échelle et introduit de la coordination : le prix est à chiffrer avant.
• La disposition en colonnes rend praticable l'analyse, mais coûte à l'écriture.
• Par lots et en flux coexistent : flux pour l'alerte, lots pour la consolidation exacte.
• Une fenêtre, un temps d'événement et un état : trois décisions précèdent toute ligne de traitement de flux.
• L'effacement d'une donnée se paie en conception, pas en procédure d'urgence.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
40
Abréviations, notation et ressources de consultation
Annexes
Annexes
Ce cours se termine par deux annexes de référence. La première donne la signification de chaque sigle
employé, sous les deux formes — sigle et développé — car la litterature emploie indifféremment l'une
ou l'autre. La seconde donne la signification de chaque symbole mathématique : elle permet de relire
une démonstration sans revenir au chapitre dont elle est extraite, et de vérifier qu'un même symbole
garde le même sens d'un chapitre à l'autre.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
41
Chapitre A.1
Liste des abréviations
Les sigles ci-dessous sont ceux que le cours emploie. Chacun est donné avec sa forme développée
et le sens précis qu'il prend ici, qui n'est pas toujours celui qu'on lui donne ailleurs.
Un sigle employé sans être développé oblige le lecteur à le reconnaître au passage, ou à l'abandonner. Le
tableau ci-dessous ferme la liste de ceux que le cours emploie : il est exhaustif pour ce document, et non
pour la discipline.
Sigle
Forme développée
Sens dans ce cours
ACID
Atomicity, Consistency, Isolation,
Durability
Propriétés qu'une transaction doit satisfaire dans une base de données.
CAP
Consistency, Availability, Partition
tolerance
Trio de propriétés dont on ne peut garantir que deux à la fois.
CRUD
Create, Read, Update, Delete
Quatre opérations de base sur une ressource.
ETL
Extract, Transform, Load
Chaîne d'alimentation d'un entrepôt de données.
OLAP
Online Analytical Processing
Traitement analytique en ligne, orienté agrégation.
OLTP
Online Transaction Processing
Traitement transactionnel en ligne, orienté écriture.
ORM
Object-Relational Mapping
Couche d'accès qui relie les objets du programme aux tables relationnelles.
PR
Pull Request
Proposition de fusion d'une branche, soumise à la revue.
RAID
Redundant Array of Inexpensive Disks
Agrégation de disques en bandes ou en miroirs.
RPO
Recovery Point Objective
Perte de données maximale tolérée après un incident, exprimée en durée.
RTO
Recovery Time Objective
Délai maximal de reprise d'activité après un incident.
SaaS
Software as a Service
Logiciel fourni hébergé, par opposition à une installation locale.
SGBD
Système de gestion de base de données
Logiciel de stockage et d'interrogation des données structurées.
sharding
Découpage horizontal
Répartition des lignes d'une table entre plusieurs instances.
Tableau 1 — Abréviations employées dans le cours
Chapitre A.2
Table de notation
Les symboles ci-dessous gardent le même sens d'un chapitre à l'autre. Lorsqu'un chapitre doit
réemployer un symbole pour un autre objet, il le redéclare sur la page même.
La notation est celle du cours : vecteurs en gras, matrices en majuscules grasses, scalaires en italique. Les
espérances sont notées E, les lois de données D, les espaces de paramètres Θ.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
42
Symbole
Signification
D
Distribution des données.
n
Nombre total d'enregistrements.
K
Nombre de partitions, de fragments ou de cassettes.
k
Index d'une partition.
nk
Nombre d'enregistrements de la partition k.
pk = (nk)/(n)
Part de la partition k dans le total.
T
Nombre de tranches, de tours ou de répliques.
t
Indice de tour ou de période.
xi
Le i-ème enregistrement.
yi
Étiquette associée à xi.
μ
Moyenne empirique d'une grandeur.
σ2
Variance empirique d'une grandeur.
h(x)
Fonction de hachage, qui répartit une clé sur les partitions.
H(X)
Entropie de Shannon, en bits si le logarithme est en base 2.
Cij
Matrice de cooccurrence entre les colonnes i et j.
λj
Valeur propre j d'une matrice, donc variance expliquée par l'axe correspondant.
Tableau 1 — Symboles mathématiques et leur signification
Convention
Toute divergence constatée entre cette table et un chapitre signale une erreur de transcription, non une
définition nouvelle : la table fait foi.
A retenir
• Un sigle employé sans être listé ici est un oubli de l'auteur, non une définition nouvelle.
• Un symbole qui change de sens d'un chapitre à l'autre rend toute démonstration ininterprétable : c'est la
principale cause des contresens que nous avons relevés.
• Ces deux tables sont les seules parties du cours à maintenir à la main : le reste se relit tout seul.
Index des figures et des tableaux
Référence rapide du matériel visuel
Figures
1.  Les trois signaux de l'observabilité et leur échelle
2.  Architecture de supervision : collecte, stockage, décision
1.  Un graphe, ses trois lectures et les questions qui en dépendent
2.  PageRank : un sommet vaut ce que valent ses voisins
1.  Les quatre tâches de la fouille de données
2.  Apriori : du treillis d'items fréquents à une règle
1.  Les cinq dimensions du Big Data et leur contrepartie technique
2.  Architecture de référence : la chaîne de données en cinq étages
3.  Traitement par lots contre traitement en flux
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
43
Tableaux
1.  Les situations d'apprentissage et l'algorithme correspondant
1.  Métriques, journaux, tracés : que répondre à quoi
1.  Dijkstra et A* : le même principe, deux conditions
2.  Quatre mesures, quatre questions
1.  K-moyens et densité : ce qui les sépare
2.  Anomalies par densité et par reconstruction
1.  Ce que la distribution achète et ce qu'elle coûte
2.  Par lots, en flux, ou les deux
1.  Abréviations employées dans le cours
1.  Symboles mathématiques et leur signification
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
44
Fin du document
Intelligence Artificielle Avancée & Federated Learning — Fondations mathématiques de
l'apprentissage automatique, algorithmes fédérés, protection de la vie privée, défense contre les attaques,
grands modèles de langage fédérés, systèmes embarqués, renforcement appris, applications critiques
(santé, V2X), plateforme de référence FedX et feuille de route de recherche.<br/>Ghiloufi Jamel,
Architecte Logiciel Principal — Pixel Software Design<br/>Département de Recherche & Développement
— Recherche<br/>Pixel Software Design — Édition 2026
© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou
diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans
autorisation écrite préalable de l'auteur.
Document généré automatiquement le 29/09/2026 — mise en page Pixel Software Design.
"""


HISTOIRE_IA_TEXT = r"""Pixel Software Design — Département de Recherche & Développement
PIXEL SOFTWARE DESIGN
Département de Recherche & Développement
Intelligence Artificielle
Avancée
& Federated Learning
•  Fondations de l'intelligence artificielle
•  Algorithmes d'apprentissage fédéré
•  Confidentialité, attaques et défenses
•  Applications et grands modèles fédérés
•  Framework FedX de référence
•  Nouveaux fronts de recherche
•  Travaux pratiques, projets et évaluation
Auteur
Ghiloufi Jamel
Fonction
Architecte Logiciel Principal
Direction
Département de Recherche & Développement
Service
R&D - Intelligence Artificielle Avancée & Apprentissage Fédéré
Niveau
Recherche
Édition
Édition 2026 — 1.0
Copyright
© Pixel Software Design
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou
diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans
autorisation écrite préalable de l'auteur.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
2
Copyright et mentions légales
Éditeur
Pixel Software Design
Auteur
Ghiloufi Jamel
Fonction
Architecte Logiciel Principal
Département
Département de Recherche & Développement
Intitulé
Intelligence Artificielle Avancée & Federated Learning
Sous-titre
Fondations mathématiques de l'apprentissage automatique, algorithmes fédérés,
protection de la vie privée, défense contre les attaques, grands modèles de langage
fédérés, systèmes embarqués, renforcement appris, applications critiques (santé,
V2X), plateforme de référence FedX et feuille de route de recherche.
Édition
Édition 2026 (version 1.0)
Langue
Français
Niveau
Recherche
Collection
Supports de formation et de recherche, Pixel Software Design
Droits d'auteur
© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation
ou diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite
sans autorisation écrite préalable de l'auteur.
Droits de l'auteur. Ghiloufi Jamel est l'auteur unique de l'ensemble du contenu scientifique, pédagogique et
technique de cet ouvrage. Toute adaptation, traduction, reproduction ou exploitation, y compris partielle, requiert
une autorisation écrite préalable.
Droits des tiers. Les algorithmes, modèles et travaux cités restent la propriété de leurs auteurs respectifs. Les
références employées figurent en fin d'ouvrage, ce qui permet de remonter au travail original pour toute
affirmation chiffrée.
Marques et licences externes. PyTorch, TensorFlow, Flower, Opacus, MONAI, scikit-learn et PySyft sont des
logiciels libres sous licences respectives (BSD, Apache 2.0, MIT). Leur usage dans ce document est purement
pédagogique et n'emporte aucune prescription commerciale.
Mentions relatives aux données et aux expérimentations
Document pédagogique à usage de formation interne. Les exemples de code fournis sont livrés à titre pédagogique
; les résultats numériques illustrés sont issus d'expérimentations conduites dans un cadre de recherche et ne
constituent pas des performances de production.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
3
Ce support synthétise les travaux de recherche du Département de Recherche & Développement de Pixel Software
Design sur l'intelligence artificielle distribuée, l'apprentissage fédéré, la protection de la vie privée et les systèmes
embarqués intelligents.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
4
Sommaire
Structure détaillée du cours
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 8
Partie 1 — Histoire et Pionniers de l'Intelligence Artificielle
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 9
1.1 Ada Lovelace et la machine analytique
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 10
1.2 Alan Turing : machine universelle et test de Turing
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 12
1.3 Le neurone formel et le perceptron
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 14
1.4 Dartmouth : naissance officielle d'un domaine
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 16
1.5 Les deux hivers et ce qu'ils enseignent
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 19
Annexes
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 20
A.1 Liste des abréviations
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 20
A.2 Table de notation
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
5
Partie
Thème
Contenu
Compétence visée
Durée
Partie 1
Fondations
Statistique, optimisation, courbes d'apprentissage
Comprendre et formaliser
2-3 semaines
Partie 2
Algorithmes FL
FedAvg, convergence, hétérogénéité, système
Implémenter et régler
3-4 semaines
Partie 3
Confidentialité
DP, attaques, défenses, agrégation sécurisée
Auditer et sécuriser
2-3 semaines
Partie 4
Applications
FedLLM, santé, V2X, FedRL, TinyML, graphes
Transposer à un domaine
3-4 semaines
Partie 5
Framework FedX
Architecture, API, benchmarks, exploitation
Industrialiser
2 semaines
Partie 6
Nouveaux fronts
FedCL, FedCI, SNN, FedGL, feuille de route
Ouvrir la recherche
2 semaines
Partie 7
TP et projets
9 labs, 5 projets, corrigés, évaluation
Faire et rendre
4-6 semaines
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
6
Préface
Comment utiliser ce cours
Ce support est conçu pour un parcours de formation et de recherche couvrant l'ensemble de la chaîne de valeur de
l'intelligence artificielle distribuée : les fondations mathématiques, les algorithmes d'apprentissage fédéré, les
menaces et défenses, les applications de pointe, une plateforme de référence opérationnelle, et enfin les nouveaux
fronts ouverts par la recherche du Département.
Ce n'est pas un manuel de référence à lire d'un trait : c'est un manuel opératoire. Chaque chapitre alterne
exposition, formalisation, mise en œuvre numérique et évaluation. Les listings sont complets et exécutables ; les
tableaux comparatifs servent de grille de décision ; les schémas d'architecture servent de support de revue de
conception.
Public et prérequis
Le contenu s'adresse à des étudiants de master et de doctorat, à des ingénieurs IA et à des praticiens de la
recherche appliquée. Les prérequis sont la connaissance de l'apprentissage automatique classique, de
l'algorithmique numérique et des bases de probabilités. Les parties 1 à 3 sont auto-suffisantes pour un étudiant qui
découvre le domaine ; les parties 4 à 7 supposent la mécanique et les outils présentés dans la partie 2.
Conventions de lecture. Une expression mathématique est encadrée par deux signes dollars ; un identifiant, un
fichier ou une commande est écrit en caractères à chasse fixe ; les encadrés Définition, Théorème, Méthode et
Attention signalent les points à maîtriser et les pièges fréquents. Les renvois de la forme « voir chapitre 3.2 »
désignent le second chapitre de la troisième partie.
Progression pédagogique
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
7
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
8
De la machine analytique au transformateur
Partie 1
Histoire et Pionniers de
l'Intelligence Artificielle
L'histoire de l'intelligence artificielle n'est pas une suite de progrès linéaires : c'est une suite de
propositions theoretical exactes, chacune suivie d'un écart entre la promesse et les moyens
disponibles. Ce cours suit les personnes et les idées qui ont produit la discipline, et il cherche à
chaque fois la raison pour laquelle l'idée a été vraie avant d'avoir les moyens de la réaliser — un
schéma qui se répète et qui et qui détermine encore aujourd'hui le rythme des progrès.
Objectifs de la partie
• Expliquer en quoi la machine analytique de Babbage et l'algorithme de Lovelacle préfigurent la
programmabilité.
• Énoncer la machine de Turing et ce qu'elle a permis de prouver sur la calculabilité.
• Discuter la portée et les limites exactes du test de Turing.
• Décrire le neurone formel de 1943 et le perceptron de 1957, et nommer ce qui manquait encore.
• Expliquer pourquoi la conférence de Dartmouth compte comme naissance officielle, et ce que le terme
accomplishes.
• Analyser les causes des deux hivers et en tirer une règle de prévision.
Plan de la partie
1.  Ada Lovelace et la machine analytique
2.  Alan Turing : machine universelle et test de Turing
3.  Le neurone formel et le perceptron
4.  Dartmouth : naissance officielle d'un domaine
5.  Les deux hivers et ce qu'ils enseignent
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
9
Chapitre 1.1
Ada Lovelace et la machine analytique
La première idée féconde n'est pas une machine capable de penser : c'est une machine capable
d'être programmée par une suite d'instructions.
Charles Babbage conçoit, à partir de 1822, la machine analytique : un moteur mécanique de calcul à Sépare
deux parties, un « magasin » de nombres et un « moulin » qui les combine. La machine n'a jamais été
construite dans son intégralité, mais sa conception contient déjà l'architecture de tout ordinateur moderne.
Partie de Babbage
Fonction
Héritage moderne
Le magasin
conservation 
des 
nombres 
et 
des 
résultats
intermédiairesmémoire
Le moulin
opérations 
arithmétiques, 
combinaison,
comparaison
unité arithmétique et logique
Le cylindre de commande
défilement des cartes perforées
unité 
de 
commande 
et 
compteur
d'instructions
Le jeu de cartes perforées
description du calcul à exécuter
programme, 
sous 
forme 
de 
support
interchangeable
Tableau 1 — Les quatre parties de la machine analytique et leur héritage
La quatrième ligne est la plus importante. Avant les cartes perforées, la séquence d'opérations était matérialisée par le
position des engrenages. Séparer le programme de la machine est ce qui rend un calculateur réutilisable pour un autre
problème.
Ada Lovelace, qui traduit en 1843 un article de Luigi Menabrea sur la machine, ajoute trois observations qui
n'ont pas été comprises pendant plus d'un siècle. La première est que la machine pourrait manipuler des
symboles, des nombres ou toute autre chose qu'on lui demanderait de représenter. La deuxième est qu'elle
pourrait composer des chaînes de caractères, donc produire de la musique. La troisième, la plus
remarquable, est qu'une telle machine ne pourrait pas faire qu'un calcul à la fois : elle pourrait enchaîner un
nombre illimité d'opérations si on lui fournissait les cartes correspondantes.
Definition — Algorithme de Bernoulli
La suite d'opérations décrite par Lovelace pour calculer les nombres de Bernoulli est généralement considérée
comme le premier programme d'ordinateur. Non par sa difficulté mathématique, mais par sa forme : c'est une
description abstraite, indépendante de toute machine, constitue d'opérations dont l'enchaînement suffit à définir
le résultat. Cette indépendancela réponse est exactement celle que Lovelace pressentait en observant que la
machine n'aurait besoin que des cartes décrivant le calcul.
Pourquoi cette histoire compte encore aujourd'hui
Trois properties que Lovelace a comprises avant tout le monde structurent encore l'informatique : un
programme est un objet séparé de la machine qui l'exécute ; un programme est un texte, donc transmissible et
vérifiable ; et la puissance d'un programme dépend du nombre d'opérations qu'on peut enchaîner, pas de
l'intelligence de la machine. Les trois sont aujourd'hui des choix d'architecture, et non des évidences.
Astuce
Un programme écrit pour une machine analytique serait aujourd'hui rejeté à la compilation pour une raison
unique : il ne manipule que des nombres, alors que la machine sait manipuler des symboles. Toute
l'informatique moderne est l/'exploitation de l'observation de Lovelace.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
10
A retenir
• La machine analytique sépare déjà mémoire, unité de calcul, unité de commande et programme.
• Lovelace formule l'idée que le programme est un objet distinct de la machine, donc réutilisable.
• L'algorithme de Bernoulli est le premier programme connu, précisément parce qu'il est écrit indépendamment
de toute machine.
• Manipuler des symboles et non seulement des nombres est l'observation qui fonde toute l'informatique
moderne.
Chapitre 1.2
Alan Turing : machine universelle et test de
Turing
Turing a fourni deux choses : une machine qui sait exécuter n'importe quel calcul, et une question
dont la discussion n'est pas terminée.
La machine de 1936 et ce qu'elle a permis de prouver
En 1936, Turing définit une machine à états finis strip : un ruban infini divisé en cases, une tête de lecture
et d'écriture qui se déplace, un ensemble fini d'états internes et un jeu de règles qui déterminent l'action. La
machine a une seule bande : instructions et données y cohabitent. Cette contrainte n'est pas un détail
historique : c'est elle qui permet la construction de la machine de Turing à partir de n'importe quelle autre
machine.
M = (Q, Σ, Γ, δ, q0, q0)
δ : Q × Σ → Q × Σ × ←, →
δ : Q × Σ → Q × Σ × ←, →
(H.1)
La fonction de transition est tout le modèle. Elle associe à chaque couple état-symbole l'état suivant, le symbole
écrit, et le sens du déplacement. Le nombre d'états est fini, la bande est infinie : c'est exactement la
configuration d'un ordinateur, au prix d'une efficience qui n'a aucun rapport.
L'apport décisif de 1936 n'est pas la machine, c'est ce qu'elle permet de prouver. Avec l'idée de machine
universelle — une machine capable de simuler toute autre machine — on peut définir ce qu'est un calcul,
puis démontrer l'existence de problèmes qu'aucune machine, si puissante soit-elle, ne résoudra jamais. Ce
résultat, la indécidabilité, est la première borne posée sur la puissance du calcul, et il est à l'origine de toute
la discipline de la théorie de la calculabilité.
Théorème de Church et Turing
Il existe des fonctions mathématiques qui sont bien définies et dont la calculabilité ne peut être démontrée par
aucun algorithme. Autrement dit : il existe des fonctions que l'on sait nommer et décrire précisément, et dont on
ne peut pas calculer la valeur, quelle que soit la machine. Church et Turing ont démontré ce résultat
indépendamment, par des voies différentes, en 1936 et 1937. C'est la première preuve qu'il existe une limite
au-dessus de toutes les limites matérielles.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
11
Figure 1 — Le test de Turing : ce qu'il mesure et ce qu'il ne mesure pas
Le test de 1950 : une reformulation, pas un critère
Dans son article fondateur, Turing ne posé pas la question « les machines peuvent-elles penser ». Il la
remplace par une question opérationnelle : existe-t-il une machine telle qu'un observateur, dialoguant par
écrit, ne puisse pas distinguer ses réponses de celles d'un humain ? La substitution est importante : elle
déplace le problème d'une propriété intrinsèque de la machine vers une performance observable, ce qui le
rend discutable et testable.
Astuce
Le test est une question de recherche, pas une définition. Il indique une direction de travail, il ne conclut rien
sur la nature de ce qui répond.
Ce que le test établit et ce qu'il n'établit pas
Ce qu'il établit
• Qu'une machine peut produire des réponses qu'un humain ne distingue pas de celles d'un autre humain.
2. Que cette indistinguabilité dépend du sujet, de la durée, du vocabulaire et de la langue employés.
3. Que la distinction se joue sur la conversation, pas sur le raisonnement.
Ce qu'il n'établit pas
• Ni compréhension, ni conscience, ni intention.
2. Aucune généralisation : passer le test sur un sujet ne dit rien d'un autre sujet.
3. Aucun passage à l'échelle : une machine qui passe le test sur cinq minutes ne le passe pas sur cinq heures.
4. Il ne dit rien du mécanisme : un programme de quatre lignes et un modèle de milliards de paramètres
peuvent passer le test, par des chemins entièrement différents.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
12
Figure 2 — Trois traditions qui n'en faisaient qu'une
Il faut enfin rappeler le second apport de Turing, souvent oublié parce qu'il a été eclipsé par le test. Dans le
même article, il décrit une machine enfant : un programme qui n'est pas progammé, mais qui s'entraîne. Il
observe qu'un programme connaissant des règles de grammaire peut les modifier pour approcher un mot
transduction, et que le jeu est plus flexible et plus facile à écrire qu'un programme de traduction directe.
Cette idée d'un programme qui améliore ses propres règles par apprentissage est l'antécédent conceptuel de
tout ce qui suit, et elle est formulée en 1950, quinze ans avant la conférence de Dartmouth.
A retenir
• La machine de Turing est définie par sa seule fonction de transition, ce qui la rend universellement simulable.
• L'indécidabilité est la première borne de calcul, indépendante de toute la technologie à venir.
• Le test de Turing est une reformulation en test de performance, pas une définition de la pensée.
• Un test qui dépend du sujet, de la durée et du vocabulaire ne conclut rien sur la machine qui le passe.
• La « machine enfant » de 1950 contient l'idée d'un programme qui améliore ses propres règles par
apprentissage.
Chapitre 1.3
Le neurone formel et le perceptron
Le premier réseau de neurones n'a pas été inventé par des informaticiens, mais par des
neurophysiologistes.
Le neurone de McCulloch et Pitts, publié en 1943, est une simplification extrême d'un neurone biologique.
Il reçoit plusieurs entrées pondérées, les additionne, applique une fonction de seuil, et émet une sortie. Ce
modèle n'a aucune propriété biologique reconnaissable : c'est un circuit logique dont la fonction est
paramétrable par le poids des connections.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
13
Figure 1 — Du neurone de McCulloch et Pitts au perceptron de Rosenblatt
y = f≤ft( ∑i=1
n wi xi - θ ), f(z) = begincases 1 & si z ≥ 0 0 & sinon endcases
Δ wi = η ≤ft( y - ŷ ) xi
(H.2)
La première équation est la fonction de transfert du neurone. La seconde est la règle d'apprentissage du
perceptron : on ne modifié un poids que dans la direction qui aurait évité l'erreur, et d'une quantité
proportionnelle à cette erreur.
Neurone formel, 1943
Perceptron, 1957
Poids
fixés à la main
ajustés par apprentissage
Structure
un neurone isolé
couche d'entrée, couche de sortie
Règle d'apprentissage
aucune
corriger par l'erreur commise
Réalisation matérielle
non tentée
première machine à réseau de neurones, 1951
Limite démontrée
aucune
fonctions non linéairement séparables
Tableau 1 — Le perceptron de Rosenblatt et ce qui le sépare du neurone
La dernière ligne est ce qui a condamné le perceptron pendant quinze ans. Ce n'est pas unefaiblesse de conception mais
une limite mathématique du modèle à deux couches.
Séparabilité linéaire
Une fonction de classification est linéairement séparable s'il existe un hyperplan qui partagé l'espace des entrées
en deux demi-espaces contenant chacun une seule classe. Un perceptron à une couche d'entrée classifie
exactement les fonctions linéairement séparables, et ne peut rien faire d'autre. Le résultat de 1969 démontre
qu'un réseau à une seule couche d'apprentissage ne peut pas calculer la fonction « ou exclusif » sur deux entrées
: c'est la borne qui a annoncé tout le reste de la théorie des réseaux de neurones.
1from typing import Sequence
2
3import numpy as np
4
5
6class Perceptron:
7''"Perceptron de Rosenblatt, avec regle de correction par erreur.
8
9Il converge en un nombre fini de passes sur toute donnee
10lineairement separable. Sur une donnee non separable, il boucle
11indefiniment : c'est la demonstration operationnelle du theoreme
12de Minsky et Papert, obtenue par un algorithme qui refuse de
13s'arreter plutot que par un raisonnement sur les poids.
14''"
15
16def __init__(self, tolerance: float = 1e-9, max_tours: int = 1000):
17self.tolerance = tolerance
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
14
18self.max_tours = max_tours
19self.poids: np.ndarray | None = None
20self.biais: float = 0.0
21self.nb_corrections = 0
22
23def apprend(self, X: np.ndarray, y: np.ndarray,
24taux: float = 0.1) -> bool:
25n_features = X.shape[1]
26self.poids = np.zeros(n_features)
27self.biais = 0.0
28self.nb_corrections = 0
29converge = False
30
31for _ in range(self.max_tours):
32erreurs = 0
33for entree, cible in zip(X, y):
34prediction = float(np.dot(self.poids, entree) >= 0.0)
35ecart = cible - prediction
36if ecart != 0.0:
37self.poids += taux * ecart * entree
38self.biais += taux * ecart
39erreurs += 1
40self.nb_corrections += 1
41if erreurs == 0:
42converge = True
43break
44return converge
45
46def.predict(self, X: np.ndarray) -> np.ndarray:
47if self.poids is None:
48raise RuntimeError("apprentissage non effectue")
49return (X @ self.poids + self.biais >= 0.0).astype(int)Perceptron : la borne de 1969, obtenue
par un algorithme
Concevoir une expérience de non-séparabilité
Pour observer la limite du perceptron par soi-même, sans recours à la théorie :
• Jeu de données : quatre points (0, 0), (0, 1), (1, 0), (1, 1), étiquetés selon la fonction « ou exclusif » :
l'étiquette vaut 1 uniquement en (1, 0) et (0, 1).
2. Algorithme : un perceptron, avec une graine fixée et un nombre maximal de tours imposé.
3. Observation : au bout de mille tours, l'erreur n'a pas diminué, et les poids continuent de tourner.
4. Explication : aucun hyperplan ne sépare les quatre points. Quel que soit le nombre de tours, c'est impossible.
5. Remédiation : ajouter une couche cachée suffit. C'est exactement la conclusion à laquelle Minsky et Papert
arrivent en 1969, et la base de tous les réseaux profonds.
La leçon est pédagogique : une borne mathématique se constate expérimentalement, et l'échec d'un algorithme
peut être la preuve d'un théorème.
A retenir
• Le neurone de 1943 est un circuit logique paramétrable, sans propriété biologique revendiquée.
• Le perceptron ajoute l'apprentissage par correction d'erreur, et converge sur toute donnée linéairement
séparable.
• L'impossibilité de séparer la fonction « ou exclusif » est une borne de modèle, pas un défaut d'implémentation.
• Ajouter une couche cachée lève la borne : c'est l'origine de toute la recherche sur les réseaux profonds.
Chapitre 1.4
Dartmouth : naissance officielle d'un domaine
Un domaine de recherche naît quand quelqu'un trouve un mot assez large pour unitesoy(), et
assez précis pour obtenir un budget.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
15
En 1956, John McCarthy, alors jeune professeur de mathématiques, propose à des collègues de l'université
de Dartmouth un projet de recherche d'été. Il écrit à ses correspondants une formule qui définira le
domaine pour trente ans : une conjecture selon laquelle tout aspect de l'apprentissage, ou toute autre
caractéristique de l'intelligence, peut en principe être décrit de façon suffisamment précise pour être simulé
par une machine.
text« Chaque aspect de l'apprentissage, ou toute autre caractéristique de l'intelligence,
peut en principe être décrit de façon suffisamment précise pour être simulé par une
machine. »
(H.3)
Cette phrase est le premier manifeste du domaine. Elle est programmatique autant que descriptive, et c'est ce
qui explique qu'elle a réuni la communauté sans proposer d'hypothèse falsifiable.
• Le choix du terme : « intelligence artificielle », plutôt que « intelligence mécanique » ou « cybernétique
». Le mot devait être vague pour attirer l'argent disponible et précis pour désigner un domaine distinct de
la cybernétique de Wiener, déjà très développée.
• Le choix du moment : la convergence de deux événements. L'informatique devient capable en 1956
(premier langage de haut niveau, FORTRAN, conçu la même année). Un Item a été découvert en 1952 :
un programme d'apprentissage par renforcement qui joue aux dames et améliore son jeu.
• Le choix du format : un atelier d'été, de six à huit chercheurs, deux mois. Le format compte autant que
le contenu : il crée une communauté là où il n'y avait que des travaux isolés.
Participant
Contribution
Orientation subsequently
John McCarthy
le terme, l'atelier, la programmation symbolique
langages 
de 
programmation, 
systèmes
experts
Marvin Minsky
réseaux de neurones, puis logique symbolique
première machine à réseau, intelligence
artificielle générale
Nathaniel Rochester
mémoire, traitement de l'information
architecture d'ordinateurs
Claude Shannon
théorie de l'information, machine à jouer
communications, machines à états finis
Newell et Simon
recherche heuristique, « société humaine »
programmation, théorie de la décision
Tableau 1 — Les participants de Dartmouth et ce qu'ils ont apporté
La présence de Shannon et de Newell n'est pas un détail : elle relié la discipline à l'informatique théorique et à la
psychologie cognitive, et c'est cette double filiation qui la distingue des mathématiques pures et de la neurologie.
Ce que Dartmouth n'était pas
L'atelier de 1956 n'a pas produit de percée technique. Minsky et Edmonds y présentent un réseau de 40
neurones, et le réseau de Barto avec lequel on apprend à jouer aux dames date de 1952. L'apport de Dartmouth
est institutionnel : un nom, un programme écrit, et un groupe de travail. Cela suffit à faire exister un domaine,
et cela explique aussi pourquoi le domaine a traversé le premier hiver dix-huit ans plus tard : l'institution était
fondée sur une promesse, et la promesse n'était pas encore soutenue par des résultats.
Le vocabulaire s'installe plus vite que les résultats
Le terme « intelligence artificielle » s'impose en quelques années, et avec lui une certaine façon de parler. Le
mot « apprentissage automatique » est forgé en 1959 pour distinguer la discipline de l'intelligence
artificielle elle-même : on cherche des méthodes d'apprentissage, pas une intelligence artificielle complète.
Le mot « science de la décision », introduit par RAND dans les années 1950, désigne l'étude des décisions en
situation d'incertitude, et annonce la théorie de la décision.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
16
Astuce
Retenir trois dates suffit à situer l'histoire : 1843 pour la programmabilité, 1943 pour le neurone formel, 1956
pour le nom. Tout ce qui suit en découle, y compris les deux hivers.
A retenir
• Dartmouth crée un domaine par un nom, un programme écrit et un groupe de travail.
• Le terme « intelligence artificielle » a été choisi pour drainer des budgets et se distinguer de la cybernétique.
• L'atelier ne produit pas de percée technique : son apport est institutionnel.
• Minsky, Shannon, Newell et Simon relient la discipline à l'informatique théorique et à la psychologie cognitive.
Chapitre 1.5
Les deux hivers et ce qu'ils enseignent
Chaque dégel de l'intelligence artificielle a suivi un hiver, et chaque hiver a suivi un écart entre
une promesse et un moyen.
Figure 1 — Les deux hivers de l'intelligence artificielle
Premier hiver : 1974-1980
La fin des années 1960 voit deux séries de déceptions convergentes. D'un côté, le perceptron est démontré
limité et la recherche sur les réseaux de neurones perd ses moyens. De l'autre, les systèmes experts, qui
promettaient de remplacer desPHA, s'effondrent sur le problème de l'acquisition des connaissances :
transcrire les règles d'un métier demande des années pour un domaine étroit, et le système casse au
premier cas non prévu.
Cause
Mécanisme
Conséquence
Limite du perceptron
impossibilité de l'« ou exclusif »arrêt de la
recherche sur les réseaux
Acquisition des connaissances
les règles coûtent plus cher que le domaine
abandon des systèmes experts
Combinatoire
la largeur de recherche explose
impossibilité de passer à l'échelle
Capacité des machines
mémoire et vitesse insuffisantes
aucun résultat à grande échelle
Tableau 1 — Les causes du premier hiver
La troisième cause est la plus profonde. Le raisonnement symbolique s'appuie sur l'exploration d'un arbre de possibilités,
et cet arbre croît exponentiellement. Améliorer l'heuristique ne change pas cette exponentielle.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
17
Second hiver : 1987-1993
Le second hiver est déclenché par l'effondrement du marché des stations de travail spécialisées, qui
promettaient d'exécuter des réseaux de neurones à grande vitesse. Quand la marketing dépasse largement
ce que le matériel permet, l'écart devient public, la confiance disparaît, et le financement se retire. C'est un
phénomène économique autant qu'un phénomène scientifique : le premier hiver a été causé par des limites
internes, le second par une surestimation public.
Les trois conditions de tous les dégels
• Plus de données. Chaque dégel coïncide avec l'arrivée d'un corpus d'une taille nouvelle : le web, puis le
web indexé, puis les données numériques, puis les corpus spécialisés. Sans volume, aucun apprentissage
statistique n'est possible.
• Plus de calcul. Le renouveau du calcul parallèle dans les années 1990, puis l'arrivée des processeurs
graphiques en 2012, dont la structure massivement parallèle correspond exactement au calcul matriciel
des réseaux profonds.
• Un algorithme adapté. La rétropropagation, publiée en 1986, permet enfin d'entraîner des réseaux
multicouches de plusieurs couches cachées. Le potentiel des travaux de 1943 devient exploitable.
Figure 2 — Quatre-vingts ans de jalons, de la machine analytique au transformateur
Une règle de prévision applicable à n'importe quelle technologie
À partir de l'histoire, une règle simple et vérifiable :
Une technique nouvelle est adoptée quand le produit de trois facteurs dépasse le seuil où la solution par
défaut devient inutilisable.
• Le facteur algorithmique : la méthode est-elle correcte, et son coût est-il connu ?
2. Le facteur matériel : l'exécution coûte-t-elle moins que le problème que la solution par défaut résout à la
main ?
3. Le facteur données : l'exemple d'apprentissage existe-t-il, et est-il accessible aux acteurs qui doivent l'utiliser
?
Si l'un des trois manque, la technique reste un objet de laboratoire, quelle que soit la qualité de ses résultats
scientifiques. C'est exactement ce que montre l'histoire : l'algorithme de rétropropagation existed depuis 1986,
et il a fallu attendre les données et le calcul de 2012.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
18
Ce que l'histoire ne dit pas
L'histoire de l'intelligence artificielle est un récit de progrès, et les récits de progrès ont une inclination à la
téléologie : on souvient des années où un dégel était écrit par avance. En réalité, la plupart des dégels étaient
imprévisibles, et plusieurs domaines sont restés dans un hiver qui dure depuis trente ans. Une règle de prévision
tirée de l'histoire doit donc être appliquée avec prudence, et son principal intérêt est d'identifier les manques
actuels : il manque aujourd'hui un facteur aux systèmes neuro-symboliques, et il manque aux systèmes
génératifs un protocole de mesure de la véracité.
Exercice 1.5.1  (difficulte : Avance)
On vous présente une technologie de segmentation d'images par apprentissage profond sur téléphones. Le
modèle a besoin d'un serveur de traitement, il a été entraîné sur un corpus de quinze millions d'images
étiquetées, et son coût d'inférence est estimé à 50 millisecondes par image sur un matériel récent. Les trois
facteurs sont-ils réunis ? Le cas échéant, à quelles conditions ?
Indice : Comptez les facteurs, pas les mérites. Un facteur peut être présent et mal placé.
Correction
• Les trois facteurs sont réunis, mais l'un d'eux est mal placé. Le facteur matériel est présent pour un serveur et
absent pour le téléphone : c'est une adoption de type 2, pas de type 3. L'adoption n'est possible que si la
quantization et l'exécution embarquée réduisent le facteur matériel d'un ordre de grandeur, ce qui a un coût de
précision. La condition d'adoption est donc écrite : perte de précision acceptable, quantification validée sur le
jeu de référence, et repli défini lorsque le modèle refuse l'exécution.
A retenir
• Le premier hiver vient de limites internes au domaine ; le second d'une surestimation public de ce que le
matériel permettait.
• Les trois dégels ont coïncidé avec plus de données, plus de calcul, et un algorithme enfin adapté.
• Une technique n'est adoptée que lorsque le produit des trois facteurs dépasse le coût de la solution par défaut.
• L'histoire des hivers sert surtout à identifier les facteurs qui manquent aujourd'hui, pas à prédire la prochaine
rupture.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
19
Abréviations, notation et ressources de consultation
Annexes
Annexes
Ce cours se termine par deux annexes de référence. La première donne la signification de chaque sigle
employé, sous les deux formes — sigle et développé — car la litterature emploie indifféremment l'une
ou l'autre. La seconde donne la signification de chaque symbole mathématique : elle permet de relire
une démonstration sans revenir au chapitre dont elle est extraite, et de vérifier qu'un même symbole
garde le même sens d'un chapitre à l'autre.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
20
Chapitre A.1
Liste des abréviations
Les sigles ci-dessous sont ceux que le cours emploie. Chacun est donné avec sa forme développée
et le sens précis qu'il prend ici, qui n'est pas toujours celui qu'on lui donne ailleurs.
Un sigle employé sans être développé oblige le lecteur à le reconnaître au passage, ou à l'abandonner. Le
tableau ci-dessous ferme la liste de ceux que le cours emploie : il est exhaustif pour ce document, et non
pour la discipline.
Sigle
Forme développée
Sens dans ce cours
AGI
Artificial General Intelligence
Intelligence artificielle générale, formulée comme objectif de programme.
AI
Artificial Intelligence
Dénomination anglaise du champ, créée en 1956.
CCD
Charge-coupled device
Capteur d'image, puis la machine de Babbage, qui traita les premières
images numériques.
DARPA
Defense Advanced Research Projects
Agency
Agence de recherche de défense, à l'origine de nombreux programmes.
FORTRAN
Formula Translation
Premier langage de programmation de haut niveau.
IA
Intelligence artificielle
Dénomination française du champ.
LISP
LISt Processing
Langage de manipulation de listes, langue de l'intelligence artificielle
symbolique.
PLAN
Planification
Recherche d'une suite d'actions qui atteint un but.
RAND
Research and Development
Société qui a produit les premiers travaux sur la logique floue.
Tableau 1 — Abréviations employées dans le cours
Chapitre A.2
Table de notation
Les symboles ci-dessous gardent le même sens d'un chapitre à l'autre. Lorsqu'un chapitre doit
réemployer un symbole pour un autre objet, il le redéclare sur la page même.
La notation est celle du cours : vecteurs en gras, matrices en majuscules grasses, scalaires en italique. Les
espérances sont notées E, les lois de données D, les espaces de paramètres Θ.
Symbole
Signification
t
Date, en années, sur la frise historique.
Δ t
Durée entre deux jalons.
N(t)
Nombre d'articles publiés en année t.
g(t)
Taux de croissance annuel de la production.
Ck
Contribution du programme de recherche k.
s
Rang d'un système sur l'échelle de perfectionnement qui structure la frise.
Tableau 1 — Symboles mathématiques et leur signification
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
21
Convention
Toute divergence constatée entre cette table et un chapitre signale une erreur de transcription, non une
définition nouvelle : la table fait foi.
A retenir
• Un sigle employé sans être listé ici est un oubli de l'auteur, non une définition nouvelle.
• Un symbole qui change de sens d'un chapitre à l'autre rend toute démonstration ininterprétable : c'est la
principale cause des contresens que nous avons relevés.
• Ces deux tables sont les seules parties du cours à maintenir à la main : le reste se relit tout seul.
Index des figures et des tableaux
Référence rapide du matériel visuel
Figures
1.  Le test de Turing : ce qu'il mesure et ce qu'il ne mesure pas
2.  Trois traditions qui n'en faisaient qu'une
1.  Du neurone de McCulloch et Pitts au perceptron de Rosenblatt
1.  Les deux hivers de l'intelligence artificielle
2.  Quatre-vingts ans de jalons, de la machine analytique au transformateur
Tableaux
1.  Les quatre parties de la machine analytique et leur héritage
1.  Le perceptron de Rosenblatt et ce qui le sépare du neurone
1.  Les participants de Dartmouth et ce qu'ils ont apporté
1.  Les causes du premier hiver
1.  Abréviations employées dans le cours
1.  Symboles mathématiques et leur signification
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
22
Fin du document
Intelligence Artificielle Avancée & Federated Learning — Fondations mathématiques de
l'apprentissage automatique, algorithmes fédérés, protection de la vie privée, défense contre les attaques,
grands modèles de langage fédérés, systèmes embarqués, renforcement appris, applications critiques
(santé, V2X), plateforme de référence FedX et feuille de route de recherche.<br/>Ghiloufi Jamel,
Architecte Logiciel Principal — Pixel Software Design<br/>Département de Recherche & Développement
— Recherche<br/>Pixel Software Design — Édition 2026
© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou
diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans
autorisation écrite préalable de l'auteur.
Document généré automatiquement le 29/09/2026 — mise en page Pixel Software Design.
"""


INNOVATION_IA_TEXT = r"""Pixel Software Design — Département de Recherche & Développement
PIXEL SOFTWARE DESIGN
Département de Recherche & Développement
Intelligence Artificielle
Avancée
& Federated Learning
•  Fondations de l'intelligence artificielle
•  Algorithmes d'apprentissage fédéré
•  Confidentialité, attaques et défenses
•  Applications et grands modèles fédérés
•  Framework FedX de référence
•  Nouveaux fronts de recherche
•  Travaux pratiques, projets et évaluation
Auteur
Ghiloufi Jamel
Fonction
Architecte Logiciel Principal
Direction
Département de Recherche & Développement
Service
R&D - Intelligence Artificielle Avancée & Apprentissage Fédéré
Niveau
Recherche
Édition
Édition 2026 — 1.0
Copyright
© Pixel Software Design
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou
diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans
autorisation écrite préalable de l'auteur.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
2
Copyright et mentions légales
Éditeur
Pixel Software Design
Auteur
Ghiloufi Jamel
Fonction
Architecte Logiciel Principal
Département
Département de Recherche & Développement
Intitulé
Intelligence Artificielle Avancée & Federated Learning
Sous-titre
Fondations mathématiques de l'apprentissage automatique, algorithmes fédérés,
protection de la vie privée, défense contre les attaques, grands modèles de langage
fédérés, systèmes embarqués, renforcement appris, applications critiques (santé,
V2X), plateforme de référence FedX et feuille de route de recherche.
Édition
Édition 2026 (version 1.0)
Langue
Français
Niveau
Recherche
Collection
Supports de formation et de recherche, Pixel Software Design
Droits d'auteur
© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation
ou diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite
sans autorisation écrite préalable de l'auteur.
Droits de l'auteur. Ghiloufi Jamel est l'auteur unique de l'ensemble du contenu scientifique, pédagogique et
technique de cet ouvrage. Toute adaptation, traduction, reproduction ou exploitation, y compris partielle, requiert
une autorisation écrite préalable.
Droits des tiers. Les algorithmes, modèles et travaux cités restent la propriété de leurs auteurs respectifs. Les
références employées figurent en fin d'ouvrage, ce qui permet de remonter au travail original pour toute
affirmation chiffrée.
Marques et licences externes. PyTorch, TensorFlow, Flower, Opacus, MONAI, scikit-learn et PySyft sont des
logiciels libres sous licences respectives (BSD, Apache 2.0, MIT). Leur usage dans ce document est purement
pédagogique et n'emporte aucune prescription commerciale.
Mentions relatives aux données et aux expérimentations
Document pédagogique à usage de formation interne. Les exemples de code fournis sont livrés à titre pédagogique
; les résultats numériques illustrés sont issus d'expérimentations conduites dans un cadre de recherche et ne
constituent pas des performances de production.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
3
Ce support synthétise les travaux de recherche du Département de Recherche & Développement de Pixel Software
Design sur l'intelligence artificielle distribuée, l'apprentissage fédéré, la protection de la vie privée et les systèmes
embarqués intelligents.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
4
Sommaire
Structure détaillée du cours
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 8
Partie 1 — Les quatre axes de l'innovation en IA
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 9
1.1 De l'IA générative passive à l'IA agentique
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 12
1.2 La multimodalité native
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 14
1.3 Efficacité, densité cognitive et Edge AI
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 16
1.4 IA verticale et systèmes hybrides d'entreprise
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 18
1.5 Panorama des modèles et influence sur l'économie internationale
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 25
Annexes
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 26
A.1 Liste des abréviations
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 26
A.2 Table de notation
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
5
Partie
Thème
Contenu
Compétence visée
Durée
Partie 1
Fondations
Statistique, optimisation, courbes d'apprentissage
Comprendre et formaliser
2-3 semaines
Partie 2
Algorithmes FL
FedAvg, convergence, hétérogénéité, système
Implémenter et régler
3-4 semaines
Partie 3
Confidentialité
DP, attaques, défenses, agrégation sécurisée
Auditer et sécuriser
2-3 semaines
Partie 4
Applications
FedLLM, santé, V2X, FedRL, TinyML, graphes
Transposer à un domaine
3-4 semaines
Partie 5
Framework FedX
Architecture, API, benchmarks, exploitation
Industrialiser
2 semaines
Partie 6
Nouveaux fronts
FedCL, FedCI, SNN, FedGL, feuille de route
Ouvrir la recherche
2 semaines
Partie 7
TP et projets
9 labs, 5 projets, corrigés, évaluation
Faire et rendre
4-6 semaines
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
6
Préface
Comment utiliser ce cours
Ce support est conçu pour un parcours de formation et de recherche couvrant l'ensemble de la chaîne de valeur de
l'intelligence artificielle distribuée : les fondations mathématiques, les algorithmes d'apprentissage fédéré, les
menaces et défenses, les applications de pointe, une plateforme de référence opérationnelle, et enfin les nouveaux
fronts ouverts par la recherche du Département.
Ce n'est pas un manuel de référence à lire d'un trait : c'est un manuel opératoire. Chaque chapitre alterne
exposition, formalisation, mise en œuvre numérique et évaluation. Les listings sont complets et exécutables ; les
tableaux comparatifs servent de grille de décision ; les schémas d'architecture servent de support de revue de
conception.
Public et prérequis
Le contenu s'adresse à des étudiants de master et de doctorat, à des ingénieurs IA et à des praticiens de la
recherche appliquée. Les prérequis sont la connaissance de l'apprentissage automatique classique, de
l'algorithmique numérique et des bases de probabilités. Les parties 1 à 3 sont auto-suffisantes pour un étudiant qui
découvre le domaine ; les parties 4 à 7 supposent la mécanique et les outils présentés dans la partie 2.
Conventions de lecture. Une expression mathématique est encadrée par deux signes dollars ; un identifiant, un
fichier ou une commande est écrit en caractères à chasse fixe ; les encadrés Définition, Théorème, Méthode et
Attention signalent les points à maîtriser et les pièges fréquents. Les renvois de la forme « voir chapitre 3.2 »
désignent le second chapitre de la troisième partie.
Progression pédagogique
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
7
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
8
Agentique, multimodal, efficient, vertical
Partie 1
Les quatre axes de l'innovation
en IA
En cinq ans, l'IA est passée d'un objet de laboratoire à une infrastructure. Quatre axes expliquent
l'essentiel du mouvement : des systèmes qui agissent au lieu de répondre, des systèmes qui voient et
entendent, des systèmes qui tiennent dans un appareil, et des systèmes ancrés dans les données d'une
organisation. Ce cours décrit ces axes, puis mesure leur effet sur l'économie internationale.
Objectifs de la partie
• Distinguer un assistant génératif d'un agent, et identifier le niveau d'autonomie réel.
• Expliquer ce qu'exige la multimodalité « native » par rapport à l'assemblage de modules.
• Évaluer le compromis entre taille de modèle, coût d'exploitation et capacité locale.
• Décrire l'architecture d'un système d'entreprisefounded sur la génération augmentée.
• Analyser la concentration de la valeur et la fracture de performance à l'échelle mondiale.
Plan de la partie
1.  De l'IA générative passive à l'IA agentique
2.  La multimodalité native
3.  Efficacité, densité cognitive et Edge AI
4.  IA verticale et systèmes hybrides d'entreprise
5.  Panorama des modèles et influence sur l'économie internationale
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
9
Chapitre 1.1
De l'IA générative passive à l'IA agentique
La rupture n'est pas dans le modèle : elle est dans la boucle qui l'entoure.
Jusqu'à recently, un modèle de langage était un produit : on lui soumettait une requête, il renvoyait une
réponse. La réponse pouvait être juste, fausse, ou mélange des deux, et l'utilisateur restait le seul juge et le
seul executeur. L'IA agentique ne change pas le modèle : elle ajoute une boucle de décision, des outils et
une mémoire autour du modèle.
Figure 1 — Les quatre axes de l'innovation et leurs interactions
Ce qu'un agent fait réellement
Un agent est un système qui, reçoit un objectif, décompose cet objectif en étapes, choisit des outils pour
exécuter ces étapes, vérifie le résultat obtenu, et répète jusqu'à atteindre l'objectif ou à décider de s'arrêter.
Cette définition est volontairement mécanique : elle permet de l'évaluer, et donc de l'auditer.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
10
Figure 2 — Le cycle agentique : percevoir, décider, agir, vérifier
Algorithme 1 — Boucle agentique générique
01  Recevoir un objectif et un budget (temps, appels, coût)Observer l'état courant : données,
outils disponibles, mémoire
02  Planifier : decomposer l'objectif en étapes vérifiables
03  Agir : appeler un outil (recherche, base, API, execution)
04  Vérifier : l'état obtenu est-il conforme a l'étape prévue ?
05  Si non : corriger le plan et reprendre a l'étape de planification
06  Si oui : passer a l'étape suivante
07  Si toutes les étapes sont validées : produire la réponse finale
08  Dans tous les cas : journaliser actions, coûts et incertitudes
Entrées : Objectif, budget, outils, mémoire • Sorties : Résultat verifie et trace • Complexité : O(k · t) appels,
k étapes, t tentatives par étape
La ligne 6 est le cœur du système : sans vérification, un agent n'est qu'un générateur de plans que l'on croît.
L'étape 9 est ce qui rend l'agent auditable.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
11
Figure 3 — Architecture de référence d'un système agentique
Les trois niveaux d'autonomie
« Agent » est devenu un mot-valise. Pour raisonner utilement, il faut distinguer trois niveaux, car le risque
n'y est pas le même.
Figure 4 — Trois niveaux d'autonomie et le risque associé
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
12
Niveau
L'humain
Ce que fait le système
ExempleContrôle requis
0 — Assistance
décide et valide chaque
actionpropose 
une
réponse ou un plan
assistant de rédaction
relecture 
humaine
systématique
1 — Délégation
définit une tâche et ses
limites
exécute de bout en bout
dans un périmètre
remplissage 
automatique
d'un formulaire métier
journalisation 
et
réversibilité
2 — Autonomie
fixe 
un 
objectif,
supervise a posteriori
planifie, 
exécute, 
vérifie,
choisit ses outils
réconciliation automatique
de 
deux 
systèmes 
de
facturation
audit, seuils d'alerte, arrêt
d'urgence
Tableau 1 — Comparaison des niveaux d'autonomie d'un système d'IA
Chaque niveau franchi augmente le rayon d'action d'une erreur. Le passage du niveau 0 au niveau 1 est souvent
sous-estimé : il déplace la responsabilité vers un dispositif de contrôle.
Les systèmes multi-agents
Un agent unique qui doit tout faire devient fragile : un mauvais outil, une hypothèse fausse, et toute la
chaîne s'arrête. L'une des approches dominantes consiste à spécialiser : un agent cherche, un autre vérifie,
un troisième décide.
• Spécialisation : chaque agent a un rôle et un jeu d'outils restreint, ce qui réduit le risque d'erreur par
agent.
• Vérification croisée : un agent critique les conclusions d'un autre ; c'est le pendant organisationnel du
double contrôle.
• Dépendance des résultats : si un agent produit une réponse, l'étape suivante doit pouvoir dire « je n'ai
pas su le vérifier ».
• Coût : la coordination a un prix en appels et en latence ; un système à six agents n'est pas six fois plus
rapide.
L'erreur la plus fréquente en déploiement est de donner à un agent un accès large (messagerie, base,
exécution) sans lui donner de moyen de vérifier ce qu'il produit. Il produit alors une suite d'actions
plausibles et invérifiables. Le premier livrable d'un projet agentique n'est pas l'agent : c'est l'instrument
de vérification.
Un agent sans instrument de mesure est un conjugateur coûteux
Responsabilité
Le cadre européen (AI Act) classe les systèmes selon leur niveau de risque et impose, pour les usages à haut
risque, une traçabilité des décisions, une information des personnes concernées et un contrôle humain effectif.
Un système agentique n'échappe pas à cette qualification : plus il est autonome, plus la justification de son usage
doit être documentée.
A retenir
• L'agent est une boucle de décision autour d'un modèle, pas un modèle nouveau.
• La vérification est ce qui distingue un agent d'un générateur de plans.
• Trois niveaux d'autonomie, trois régimes de risque et de contrôle distincts.
• La multi-agents gagne en robustesse et en spécialisation, pas en vitesse.
Chapitre 1.2
La multimodalité native
Traiter plusieurs médias ne signifie pas les juxtaposer.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
13
Pendant des années, l'architecture courante consistait à faire tourner un modèle par modalité — un module
de vision, un module de reconnaissance vocale — puis à transmettre leurs sorties à un modèle de texte. La
multimodalité native change la donné : un seul modèle reçoit l'image, le son et le texte dans un espace
unique, ce qui lui permet de raisonner sur les relations entre eux.
Figure 1 — Modalités, encodeurs et espace de projection commun
Critère
Assemblage de modules
Modalité native
Unité de traitement
un modèle par modalité
un modèle unique
Alignement
appris à la main, souvent fragile
appris pendant l'entraînement
Raisonnement croisé
limité aux interfaces entre modules
direct, sur les données jointes
Latence
somme des latences de chaque module
une seule passe
Coût d'entraînement
plusieurs entraînements distincts
un seul entraînement
Limite
information perdue aux frontières
cohérence globale
Tableau 1 — Assemblage de modules contre modalité native
Le test décisif est simple : poser une question qui exige de croiser deux modalités. « Que se passe-t-il juste après que le
client a dit ceci ? » en Combineant l'audio et la vidéo ne fonctionne qu'en natif.
Ce que la multimodalité rend possible
• Maintenance assistée : analyser une vidéo de flux et un relevé de température, puis signaler une
discordance.
• Aide à la décision clinique : croiser un dossier, un compte rendu radiologique et un entretien
enregistré.
• Contrôle d'accès : comparer une image, une voix et un document d'identité pour authentifier.
• Robotique : un agent qui voit, entend et décide de la manipulation à partir de l'environnement réel.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
14
Exemple
Un cas typique de valeur créée par le croisement : un contrôle d'accès. Le visage seul peut être trompé par un
masque ; la voix seule peut l'être par un enregistrement. La comparaison des trois signaux dans un même
modèle rend la fraude nettement plus coûteuse à mettre en œuvre, sans exiger de règle écrite.
Multimodalité et exécution locale
La multimodalité a longtemps été un obstacle à l'exécution locale : un modèle qui lit, entend et voit occupe
fastidement la mémoire. Larchitectures compactes, objet du module suivant, lèvent cette contrainte.
Figure 2 — Déploiement local ou dans le nuage : avantages et contraintes
Latence et gouvernance du temps réel
Un système d'IA qui pilote un équipement ne peut pas tolérer quarante millisecondes d'aller-retour réseau. Le
critère de choix du mode de déploiement n'est donc jamais la qualité du modèle, mais le délai maximal toléré
par l'usage.
A retenir
• La multimodalité native consiste en un espace de projection commun, pas en un assemblage de modules.
• La valeur apparaît là où une question exige de croiser deux modalités.
• Le mode de déploiement est déterminé par la latence admissible et le régime de confidentialité.
Chapitre 1.3
Efficacité, densité cognitive et Edge AI
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
15
La course au nombre de paramètres s'achève : ce qui compte désormais, c'est le raisonnement par
unité d'énergie consommée.
La métrique dominante pendant cinq ans a été le nombre de paramètres, parce qu'elle était facile à
comparer et à communiquer. Elle est aujourd'hui remplacée par une famille de mesures plus pertinentes :
qualité par unité de calcul, par unité de mémoire, et par unité d'énergie.
Figure 1 — Rapprochement de la frontière des gros modèles et des modèles compacts
Ce que recouvre la « densité cognitive »
Definition — Densité cognitive
Rapport entre la qualité d'un modèle et les ressources nécessaires pour l'exécuter. Elle se mesure au minimum
sur trois axes : la consommation mémoire à l'inférence, la latence pour une requête, et l'énergie par jeton
produit.
Levier
Principe
Gain typique
Coût ou limite
Quantification
réduire la précision des poids2 à 4
fois moins de mémoire
perte de précision à surveiller
Distillation
transférer le savoir d'un grand
modèle
modèle nettement plus petit
nécessite l'accès au grand modèle
Quantification +
ajustement
recalibrer après réduction
récupère l'essentiel de la perte
coût d'entraînement ajouté
Adaptation de faible rang
ne entraîner qu'un adaptateur
quelques 
pour 
cent 
des
paramètres
incompatible avec l'exécution sans
adaptateur
Réseau neuroshape
contrôler la fréquence et l'énergie
très faible consommation
modèles plus specializeds
Tableau 1 — Comment un modèle compact devient compact
La quantification est le levier le plus rentable et le plus sous-estimé : pour un besoin de raisonnement courant, réduire la
précision des poids change rarement le comportement observable.
Pourquoi l'exécution locale redevient rentable
• Confidentialité : la donnée ne quitte pas le poste ni l'entreprise, ce qui lève une contrainte juridique
sans compromettre sur le modèle.
• Fonctionnement hors ligne : l' Terminal reste utile sans réseau, ce qui compte en mobilité, en industrie
et en santé.
• Coût marginal : l'inférence locale ne coûte rien par requête une fois l'appareil amorti.
• Latence : absence d'aller-retour réseau, donc un comportement prévisible et boré.
« Hors ligne » a un prix caché
Un modèle exécuté localement n'est plus mis à jour. La maintenance d'une flotte d'appareils gravité est un
travail d'exploitation à part entière : distribution des versions, vérification de l'intégrité, retour arrière en cas de
régression. Ce coût est rarement chiffré au moment du choix, et il est le premier motif d'abandon de l'Edge AI en
production.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
16
Où reste-t-il pertinent d'utiliser un gros modèle ?
La compactisation ne supprime pas les modèles de grande taille ; elle en restreint l'usage aux tâches qui le
justifient. Un système hybride est la configuration la plus courante : un modèle local pour le traitement
courant, un modèle distant pour la génération complexe, et un aiguillage explicite entre les deux.
Astuce
Le bon indicateur de choix n'est pas la taille du modèle mais le taux d'échappement : la proportion de requêtes
que le système local ne sait pas traiter et qu'il faut transmettre. En dessous de dix pour cent, l'hybride est
presque toujours le bon choix.
A retenir
• La taille du modèle a cessé d'être le bon indicateur ; la densité cognitive l'a remplacée.
• La quantification est le levier le plus rentable et le plus immédiat.
• L'exécution locale résout la confidentialité et la latence, mais déplace le coût vers la maintenance du parc.
• La configuration industrielle courante est hybride, avec aiguillage explicite entre modèle local et modèle
distant.
Chapitre 1.4
IA verticale et systèmes hybrides d'entreprise
Un modèle généraliste ne connaît rien de votre métier. Toute la valeur se construit dans la couche
d'accès à vos données.
Les entreprises délaissent progressivement les outils généralistes au profit d'architectures ancrées dans leurs
propres données et dans leurs propres processus. Ce mouvement porte un nom : l'IA verticale.
Figure 1 — Anatomie d'un système de génération augmentée
La génération augmentée par récupération
Le mécanisme central est le RAG (retrieval-augmented génération). Au lieu de demander au modèle de
connaître une information, on lui fournit les passages pertinents au moment de la question, puis on lui
demande de rédiger une réponse fondée dessus.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
17
Algorithme 2 — Cycle d'une interrogation en génération augmentée
01  Reformuler la question de l'utilisateur en requête de rechercheRechercher les passages
proches dans la base vectorielle
02  Filtrer par permissions, date et source autorisée
03  Assembler les passages retenus avec la question
04  Demander au modèle de répondre en citant les passages
05  Vérifier que chaque affirmation est attribuable a un passage
06  Renvoyer la réponse et les références, ou une absence de réponse
Entrées : Question, droits d'accès de l'utilisateur • Sorties : Réponse sourcée, ou refus explicite • Complexité
: O(N log d) pour la recherche, un appel modèle par question
La dernière ligne est la plus importante : un système qui répond à tout, même quand la base ne contient pas
la réponse, est pire qu'un système qui ne répond pas. Le refus est un comportement à concevoir.
La base vectorielle n'est pas une base de connaissances
La recherche par similarité s'appuie sur la proximité vectorielle entre la question et les passages. Cette proximité
mesure une ressemblance de formulation, pas une pertinence factuelle. Un passage sur les « taux d'intérêt » peut
être sélectionné pour une question sur le « taux d'usure ». L'indexation, le découpage des documents et le
filtrage méthodologique pèsent autant que le modèle lui-même.
L'intégration dans les logiciels métier
Au-delà de la simple interrogation, l'IA s'insère dans la chaîne de valeur : elle prépare la facture, rapproche
le bon de commande, rédige la réponse de support, anticipe la panne. Cette intégration se fait par couche,
du plus stable au plus volatil.
Figure 2 — Insertion de l'IA dans la chaîne de valeur de l'entreprise
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
18
Couche
Rôle
Propriétaire
Risque dominant
Données
sources, qualité, traçabilité
direction des donnéesdonnée
obsolète ou non conforme
Services
recherche, index, journal d'audit
équipe plateforme
permissions mal appliquées
Modèles
modèle 
généraliste, 
ajusté, 
règles
métier
équipe modèle
dérive de performance
Agents
routage, rédaction, contrôle, escalade
équipe produit
action non réversible
Usages
support, facturation, prévision
métier
confiance excessive
Tableau 1 — Les couches d'un système d'IA d'entreprise
L'erreur la plus coûteuse consiste à commencer par la couche agents : sans couche de données fiable et journalisée,
l'automatisation ne fait qu'exécuter plus vite des erreurs.
Ce qui distingue un déploiement réussi d'un gadget
• Il porte sur un processus mesurable, pas sur une fonction marketing.
• Il dispose d'un critère d'abandon écrit dès le départ.
• Il journalise chaque décision de façon à pouvoir être rejouée.
• Il prévoit un retour arrière : le système sait défaire ce qu'il a fait.
• Il est évalué sur le temps gagné net de la supervision ajoutée.
A retenir
• Toute la valeur de l'IA verticale se construit dans la couche d'accès aux données propres.
• La génération augmentée impose de concevoir le refus comme un comportement normal.
• L'intégration doit suivre les couches, des données vers les usages, jamais l'inverse.
• Un projet sans critère d'abandon écrit ni retour arrière est un gadget à date d'expiration.
Chapitre 1.5
Panorama des modèles et influence sur
l'économie internationale
Où en est la technologie, et — surtout — qui en tire la valeur.
Ce dernier module n'est pas un catalogue de produits : c'est une lecture économique. La question utile n'est
pas « quel modèle est le meilleur ? » mais « qui capte la valeur créée, et à quelles conditions ».
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
19
Figure 1 — Frontières propriétaires et poids ouverts : deux logiques de déploiement
L'état d'avancement des modèles de pointe
• Raisonnement adaptatif : les modèles de pointe allouent dynamiquement un effort de calcul à la
question, ce qui allonge le délai de réponse mais améliore la justesse sur les problèmes difficiles.
• Correction de leurs propres erreurs : la Capacity à vérifier et reprendre un raisonnement remplace en
partie la boucle externe, ce qui est la condition de l'autonomie.
• Multimodalité native : texte, vision et audio traités dans un même modèle, avec alignement appris
pendant l'entraînement.
• Usage d'outils : appel de fonctions, consultation de bases et exécution de code deviennent des capacités
natives du modèle.
• Compétences verticales : les fournisseurs exposent des interfaces dédiées au code, au droit, à la
recherche biomédicale et à l'automatisation des systèmes de gestion.
L'investissement et les infrastructures
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
20
Figure 2 — Investissements et dépenses d'infrastructure : ordres de grandeur mondiaux
Le fait marquant de la période n'est pas le volume investi mais sa nature. La dépense d'infrastructure —
centres de données, puces d'accélération, énergie — a dépassé l'investissement en recherche. L'IA est
devenue un bien de capital à part entière, ce qui a des conséquences sur la structure du marché : très peu
d'acteurs peuventlux financer ce niveau d'engagement.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
21
Position
Ce qui la caractérise
Exemple d'avantageFacteur de
vulnérabilité
Pionniers
redéfinissent 
un 
processus
entiercoût unitaire en baisse, délai
de cycle réduit
dépendance à l'éditeur de modèle
Suivants
intègrent 
l'IA 
à 
un 
processus
existant
gain de productivité ciblé sur une
étape
données moins spécifiques
Grand public
utilisent des outils génériques
accès 
à 
la 
capacité 
sans
investissement
aucun avantage défendable à long
terme
Tableau 1 — Où se concentre la valeur créée
Le gain se mesure en restructuration de processus, pas en ajout d'outils. C'est la distinction centrale de toutes les études
d'impact.
Figure 3 — Fracture de performance : l'écart se creuse avec l'adoption
La transformation du marché du travail
L'effet le mieux documenté n'est pas une disparition d'emplois, mais un déplacement de la valeur à
l'intérieur du poste. Ce qui coûte cher — exécuter, saisir, trier, rédiger un premier jet — baisse. Ce qui
augmente — vérifier, arbitrer, décider — augmente.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
22
Figure 4 — Les trois déplacements de valeur dans le travail
• Automatisation des tâches répétitives : développement logiciel, support de premier niveau, traitement
documentaire.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
23
• Transition vers la supervision : le travail devient vérifier et corriger plutôt que produire.
• Dérive des compétences : la vitesse d'adaptation devient plus déterminante que le stock de
connaissances initiales.
• Concentration : la valeur se déplace vers les postes qui définissent le problème et arbitrent des cas
ambigus.
Cadre juridique et ethique
Cadre de gouvernance. Le règlement européen sur l'intelligence artificielle (2024/1689) classe les systèmes par
niveau de risque, impose la transparence pour les applications interagissant avec les personnes, et prévoit des
obligations renforcées pour les usages sensibles — santé, emploi, crédit, sécurité. Cette classification constitue
aujourd'hui une contrainte de conception, au même titre qu'une exigence juridique.
La souveraineté technologique
Les États ont compris que la maîtrise des ressources de l'IA conditionné leur capacité de négociation. La
question n'est plus « quel modèle est le meilleur » mais « quel maillon peut-on contrôler ».
Figure 5 — Les couches de la souveraineté technologique et leurs dépendances
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
24
Couche
Concentration
Point de bascule
Levier d'un État
Énergie
élevée
accès 
à 
l'électricité 
et 
au
refroidissementcontrats de long terme,
énergie nucléaire
Puces
très élevée
fabrication avancée et mémoire
subventions à la conception, capacités de
packaging
Calcul
élevée
centres de données et accélérateurs
souveraineté 
des 
données, 
implantation
régionale
Modèles
moyenne
accès aux poids et aux talents
écosystèmes ouverts, financement de la
recherche
Applications
faible
données d'usage et processus métier
normalisation sectorielle, interopérabilité
Réglementation
moyenne
normes et reconnaissance mutuelle
participation 
active 
aux 
travaux 
de
normalisation
Tableau 2 — Les couches de dépendance et leurs points de bascule
Un État peut agir sur les couches basses (énergie, puces) ou hautes (modèles, applications) ; l'autonomie complète sur
toutes les couches n'est la position d'aucun acteur aujourd'hui.
Astuce
La question opérationnelle la plus utile pour une direction générale est de situer ses dépendances : pour
chacune de ses fonctions critiques, quelles couches de ce tableau sont déléguées à des tiers, et avec quelle
alternative ?
A retenir
• L'état des modèles est characterised par le raisonnement adaptatif, la multimodalité native et l'usage d'outils.
• La valeur se concentre chez qui refont un processus, pas chez qui ajoutent un outil.
• Le marché du travail se déplace de l'exécution vers le contrôle et l'arbitrage.
• La souveraineté se joue couche par couche ; l'autonomie complète reste hors de portée de tout acteur.
Sources et références de ce module
Les chiffres cités dans ce module sont des ordres de grandeur issus de publications publiques. Ils sont
donnés comme ordres de grandeur et non comme valeurs exactes, parce que les périmètres de mesure
diffèrent d'une étude à l'autre.
• axis — FPT Software — State of AI 2025, axe « agents IA ».; Innowise — veille technologique, axe
multimodalité.; Switas Consultancy — veille « IA de pointe », axes multimodalité et efficience.; MaCertif
— dossier Edge AI et modèles compacts.; LLMBase — panorama des familles de modèles de pointe.;
McKinsey Global Survey on AI — usages et gains de productivité.; PwC — Global AI Study, mesure de la
concentration de la valeur.; Stanford HAI — AI Index Report, effets sur l'emploi et l'investissement.;
Règlement (UE) 2024/1689 (AI Act) — Journal officiel de l'Union européenne.
Les quatre axes décrits dans ce cours suivent les veilles sectorielles de FPT Software, Innowise, Switas
Consultancy, MaCertif et LLMBase ; l'analyse économique s'appuie sur les travaux de McKinsey, PwC et
Stanford HAI, complétés par le cadre réglementaire européen.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
25
Abréviations, notation et ressources de consultation
Annexes
Annexes
Ce cours se termine par deux annexes de référence. La première donne la signification de chaque sigle
employé, sous les deux formes — sigle et développé — car la litterature emploie indifféremment l'une
ou l'autre. La seconde donne la signification de chaque symbole mathématique : elle permet de relire
une démonstration sans revenir au chapitre dont elle est extraite, et de vérifier qu'un même symbole
garde le même sens d'un chapitre à l'autre.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
26
Chapitre A.1
Liste des abréviations
Les sigles ci-dessous sont ceux que le cours emploie. Chacun est donné avec sa forme développée
et le sens précis qu'il prend ici, qui n'est pas toujours celui qu'on lui donne ailleurs.
Un sigle employé sans être développé oblige le lecteur à le reconnaître au passage, ou à l'abandonner. Le
tableau ci-dessous ferme la liste de ceux que le cours emploie : il est exhaustif pour ce document, et non
pour la discipline.
Sigle
Forme développée
Sens dans ce cours
AGI
Artificial General Intelligence
Intelligence artificielle générale, horizon de long terme.
API
Application Programming Interface
Interface d'échange entre deux logiciels.
CAPEX
Capital Expenditure
Dépense d'investissement, amortie sur plusieurs exercices.
FPT
Formation professionnelle technologie
Parcours de formation addressing l'adaptation des métiers.
HAI
Human-AI
Collaboration entre une personne et un système automatique.
IA
Intelligence artificielle
Ensemble des techniques qui produisent des comportements intelligents.
LLM
Large Language Model
Grand modèle de langage.
MVP
Minimum Viable Product
Version minimale d'un produit, livrée pour tester une hypothèse.
ONG
Organisation non gouvernementale
Acteur extérieur à l'entreprise.
OPEX
Operating Expenditure
Charge d'exploitation, qui se répète d'un exercice à l'autre.
UE
Union européenne
Dont le règlement sur l'intelligence artificielle structure le marché
européen.
VAE
Variational Auto-Encoder
Auto-encodeur variationnel, qui sert de modèle génératif.
Tableau 1 — Abréviations employées dans le cours
Chapitre A.2
Table de notation
Les symboles ci-dessous gardent le même sens d'un chapitre à l'autre. Lorsqu'un chapitre doit
réemployer un symbole pour un autre objet, il le redéclare sur la page même.
La notation est celle du cours : vecteurs en gras, matrices en majuscules grasses, scalaires en italique. Les
espérances sont notées E, les lois de données D, les espaces de paramètres Θ.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
27
Symbole
Signification
Rt
Recette de la période t.
Ct
Charge totale de la période t.
Bt
Solde de trésorerie en fin de période t.
Vk
Valeur d'une option d'investissement k.
r
Taux d'actualisation.
NPV = ∑t=0
T (Rt - Ct)/((1+r)t)
Valeur actuelle nette d'un projet.
T
Horizon de la projection financière, en périodes.
ROAI
Retour sur investissement, exprimé en pourcentage.
Ik
Indice d'attractivité du projet k.
λk
Pondération du critère k dans l'indice d'attractivité.
Tadoption
Délai d'adoption par le marché visé.
Tableau 1 — Symboles mathématiques et leur signification
Convention
Toute divergence constatée entre cette table et un chapitre signale une erreur de transcription, non une
définition nouvelle : la table fait foi.
A retenir
• Un sigle employé sans être listé ici est un oubli de l'auteur, non une définition nouvelle.
• Un symbole qui change de sens d'un chapitre à l'autre rend toute démonstration ininterprétable : c'est la
principale cause des contresens que nous avons relevés.
• Ces deux tables sont les seules parties du cours à maintenir à la main : le reste se relit tout seul.
Index des figures et des tableaux
Référence rapide du matériel visuel
Figures
1.  Les quatre axes de l'innovation et leurs interactions
2.  Le cycle agentique : percevoir, décider, agir, vérifier
3.  Architecture de référence d'un système agentique
4.  Trois niveaux d'autonomie et le risque associé
1.  Modalités, encodeurs et espace de projection commun
2.  Déploiement local ou dans le nuage : avantages et contraintes
1.  Rapprochement de la frontière des gros modèles et des modèles compacts
1.  Anatomie d'un système de génération augmentée
2.  Insertion de l'IA dans la chaîne de valeur de l'entreprise
1.  Frontières propriétaires et poids ouverts : deux logiques de déploiement
2.  Investissements et dépenses d'infrastructure : ordres de grandeur mondiaux
3.  Fracture de performance : l'écart se creuse avec l'adoption
4.  Les trois déplacements de valeur dans le travail
5.  Les couches de la souveraineté technologique et leurs dépendances
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
28
Tableaux
1.  Comparaison des niveaux d'autonomie d'un système d'IA
1.  Assemblage de modules contre modalité native
1.  Comment un modèle compact devient compact
1.  Les couches d'un système d'IA d'entreprise
1.  Où se concentre la valeur créée
2.  Les couches de dépendance et leurs points de bascule
1.  Abréviations employées dans le cours
1.  Symboles mathématiques et leur signification
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
29
Fin du document
Intelligence Artificielle Avancée & Federated Learning — Fondations mathématiques de
l'apprentissage automatique, algorithmes fédérés, protection de la vie privée, défense contre les attaques,
grands modèles de langage fédérés, systèmes embarqués, renforcement appris, applications critiques
(santé, V2X), plateforme de référence FedX et feuille de route de recherche.<br/>Ghiloufi Jamel,
Architecte Logiciel Principal — Pixel Software Design<br/>Département de Recherche & Développement
— Recherche<br/>Pixel Software Design — Édition 2026
© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou
diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans
autorisation écrite préalable de l'auteur.
Document généré automatiquement le 29/09/2026 — mise en page Pixel Software Design.
"""


IA_APPLIQUEE_TERRAIN_TEXT = r"""Pixel Software Design — Département de Recherche & Développement
PIXEL SOFTWARE DESIGN
Département de Recherche & Développement
Intelligence Artificielle
Avancée
& Federated Learning
•  Fondations de l'intelligence artificielle
•  Algorithmes d'apprentissage fédéré
•  Confidentialité, attaques et défenses
•  Applications et grands modèles fédérés
•  Framework FedX de référence
•  Nouveaux fronts de recherche
•  Travaux pratiques, projets et évaluation
Auteur
Ghiloufi Jamel
Fonction
Architecte Logiciel Principal
Direction
Département de Recherche & Développement
Service
R&D - Intelligence Artificielle Avancée & Apprentissage Fédéré
Niveau
Recherche
Édition
Édition 2026 — 1.0
Copyright
© Pixel Software Design
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou
diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans
autorisation écrite préalable de l'auteur.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
2
Copyright et mentions légales
Éditeur
Pixel Software Design
Auteur
Ghiloufi Jamel
Fonction
Architecte Logiciel Principal
Département
Département de Recherche & Développement
Intitulé
Intelligence Artificielle Avancée & Federated Learning
Sous-titre
Fondations mathématiques de l'apprentissage automatique, algorithmes fédérés,
protection de la vie privée, défense contre les attaques, grands modèles de langage
fédérés, systèmes embarqués, renforcement appris, applications critiques (santé,
V2X), plateforme de référence FedX et feuille de route de recherche.
Édition
Édition 2026 (version 1.0)
Langue
Français
Niveau
Recherche
Collection
Supports de formation et de recherche, Pixel Software Design
Droits d'auteur
© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation
ou diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite
sans autorisation écrite préalable de l'auteur.
Droits de l'auteur. Ghiloufi Jamel est l'auteur unique de l'ensemble du contenu scientifique, pédagogique et
technique de cet ouvrage. Toute adaptation, traduction, reproduction ou exploitation, y compris partielle, requiert
une autorisation écrite préalable.
Droits des tiers. Les algorithmes, modèles et travaux cités restent la propriété de leurs auteurs respectifs. Les
références employées figurent en fin d'ouvrage, ce qui permet de remonter au travail original pour toute
affirmation chiffrée.
Marques et licences externes. PyTorch, TensorFlow, Flower, Opacus, MONAI, scikit-learn et PySyft sont des
logiciels libres sous licences respectives (BSD, Apache 2.0, MIT). Leur usage dans ce document est purement
pédagogique et n'emporte aucune prescription commerciale.
Mentions relatives aux données et aux expérimentations
Document pédagogique à usage de formation interne. Les exemples de code fournis sont livrés à titre pédagogique
; les résultats numériques illustrés sont issus d'expérimentations conduites dans un cadre de recherche et ne
constituent pas des performances de production.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
3
Ce support synthétise les travaux de recherche du Département de Recherche & Développement de Pixel Software
Design sur l'intelligence artificielle distribuée, l'apprentissage fédéré, la protection de la vie privée et les systèmes
embarqués intelligents.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
4
Sommaire
Structure détaillée du cours
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 8
Partie 1 — IA Appliquée : Objets Connectés, Robotique, Santé et Défense
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 9
1.1 Le socle : objets connectés et intelligence embarquée
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 14
1.2 Modélisation et jumeaux numériques
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 16
1.3 Robotique et niveaux d'autonomie
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 19
1.4 Santé connectée et médecine prédictive
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 28
1.5 Défense : essaims, maintenance prédictive, aide à la décision
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 31
Annexes
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 32
A.1 Liste des abréviations
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 32
A.2 Table de notation
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
5
Partie
Thème
Contenu
Compétence visée
Durée
Partie 1
Fondations
Statistique, optimisation, courbes d'apprentissage
Comprendre et formaliser
2-3 semaines
Partie 2
Algorithmes FL
FedAvg, convergence, hétérogénéité, système
Implémenter et régler
3-4 semaines
Partie 3
Confidentialité
DP, attaques, défenses, agrégation sécurisée
Auditer et sécuriser
2-3 semaines
Partie 4
Applications
FedLLM, santé, V2X, FedRL, TinyML, graphes
Transposer à un domaine
3-4 semaines
Partie 5
Framework FedX
Architecture, API, benchmarks, exploitation
Industrialiser
2 semaines
Partie 6
Nouveaux fronts
FedCL, FedCI, SNN, FedGL, feuille de route
Ouvrir la recherche
2 semaines
Partie 7
TP et projets
9 labs, 5 projets, corrigés, évaluation
Faire et rendre
4-6 semaines
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
6
Préface
Comment utiliser ce cours
Ce support est conçu pour un parcours de formation et de recherche couvrant l'ensemble de la chaîne de valeur de
l'intelligence artificielle distribuée : les fondations mathématiques, les algorithmes d'apprentissage fédéré, les
menaces et défenses, les applications de pointe, une plateforme de référence opérationnelle, et enfin les nouveaux
fronts ouverts par la recherche du Département.
Ce n'est pas un manuel de référence à lire d'un trait : c'est un manuel opératoire. Chaque chapitre alterne
exposition, formalisation, mise en œuvre numérique et évaluation. Les listings sont complets et exécutables ; les
tableaux comparatifs servent de grille de décision ; les schémas d'architecture servent de support de revue de
conception.
Public et prérequis
Le contenu s'adresse à des étudiants de master et de doctorat, à des ingénieurs IA et à des praticiens de la
recherche appliquée. Les prérequis sont la connaissance de l'apprentissage automatique classique, de
l'algorithmique numérique et des bases de probabilités. Les parties 1 à 3 sont auto-suffisantes pour un étudiant qui
découvre le domaine ; les parties 4 à 7 supposent la mécanique et les outils présentés dans la partie 2.
Conventions de lecture. Une expression mathématique est encadrée par deux signes dollars ; un identifiant, un
fichier ou une commande est écrit en caractères à chasse fixe ; les encadrés Définition, Théorème, Méthode et
Attention signalent les points à maîtriser et les pièges fréquents. Les renvois de la forme « voir chapitre 3.2 »
désignent le second chapitre de la troisième partie.
Progression pédagogique
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
7
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
8
Du capteur au système autonome, et de la promesse à la responsabilité
Partie 1
IA Appliquée : Objets
Connectés, Robotique, Santé et
Défense
L'intelligence artificielle cesse d'être un logiciel quand elle quitte le centre de calcul. Ce cours suit ce
déplacement : d'un capteur qui décide seul, à un essaim de robots qui coordonne, en passant par le
jumeau numérique d'un patient et par la maintenance prédictive d'un avion. Les domaines
d'application ne changent pas la méthode ; ils changent ce que l'erreur coûte, et c'est toujours cette
question qui décide de la conception.
Objectifs de la partie
• Répartir une décision entre l'objet, le bord du réseau et le nuage, et justifier ce partage.
• Construire un jumeau numérique relié à une mesure, et distinguer ce qu'il permet réellement.
• Situer un système robotique sur l'échelle d'autonomie, et nommer la garantie manquante au niveau suivant.
• Expliquer pourquoi la santé connectée est d'abord un problème de capteur avant d'être un problème de
modèle.
• Analyser les usages de l'intelligence dans un système de défense, et distinguer ce qui relève de la technique de
ce qui relève de l'institution.
• Citer les quatre obstacles communs à tous ces domaines et leurs parades.
Plan de la partie
1.  Le socle : objets connectés et intelligence embarquée
2.  Modélisation et jumeaux numériques
3.  Robotique et niveaux d'autonomie
4.  Santé connectée et médecine prédictive
5.  Défense : essaims, maintenance prédictive, aide à la décision
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
9
Chapitre 1.1
Le socle : objets connectés et intelligence
embarquée
La question n'est plus « le capteur envoie-t-il ses données » mais « l'objet décide-t-il seul ».
Un système connecté transmettait ses mesures à un serveur, qui les stockait, et un humain ou une règle
decidait. Cette organisation ne tient plus, pour une raison simple : le volume de mesures a crû plus vite que
la capacité de les traiter, et le temps de latence du réseau est devenu incompatible avec la plupart des
usages. L'objet connecté devient alors un système autonome de décision, et c'est ce changement qu'on
appelle intelligence embarquée.
Figure 1 — De l'objet connecté passif à l'objet.Application intelligente
Niveau
Délai
Ce qui s'y décide
Contrainte dominante
Sur l'objet
quelques millisecondesfiltrage,
dédoublonnage, 
comptage,
détection simple, alarme
mémoire, énergie, dissipation thermique
Au bord du réseau
quelques 
dizaines 
de
millisecondes
agrégation, 
coordination 
entre 
appareils
voisins, inférence de taille moyenne
coût de l'équipement, disponibilité
Dans le nuage
centaines de millisecondes
modèles 
volumineux, 
réentraînement,
analyse historique
coût par requête, protection des
données
Tableau 1 — Les trois niveaux de répartition d'une décision
La règle de répartition se formule en une phrase : on rapproche le calcul de la donnée à autant que la qualité du résultat le
permet, et on ne remonte que ce qui est utile.
• Quantification : un modèle en virgule flottante sur 32 bits occupe quatre fois plus qu'un modèle en 8
bits, pour un gain de précision souvent inutile. Quantifier est le premier levier d'embarquement, avant
toute compression.
• Tailles de modèle : un modèle compact tient en mémoire de puce, un modèle de quelques centaines de
kilo-octets tient en mémoire d'objet. C'est souvent cette frontière, et non la puissance de calcul, qui
décide du produit.
• Quantification non uniforme : en affectant moins de bits aux valeurs peu probables, on divisé la taille
du modèle par trois ou quatre pour une dégradation de précision presque nulle.
• Température de service : un modèle embarqué doit être évalué sur la mémoire et le processeur de la
cible, pas sur une machine de développement. Un modèle qui tient en mémoire sur un ordinateur de
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
10
bureau peut dépasser celle de la cible.
1import numpy as np
2
3
4def quantifier_lineaire(t, bits_entiers=8, bits_frac=4):
5''"Quantification symetrique, avec arrondi au plus proche.
6
7La quantification est le premier levier d'embarquement : diviser le
8nombre de bits par deux divise la taille du modele et divise par deux
9l'energie de lecture, ce qui est le poste dominant sur un appareil
10sur batterie.
11
12La calibration exige un jeu de reference. Utiliser les bornes d'un
13lot de validation isole, lui, ne dit rien de la plage reelle des
14donnees de production, qui est plus large et plus variable.
15''"
16echelle = (2 ** bits_entiers - 1) / 2
17pas = 2.0 ** (-bits_frac)
18return np.round(t / pas) * pas
19
20
21def borner_par_percentiles(reference: np.ndarray, bas: float = 0.5,
22haut: float = 99.5) -> tuple[float, float]:
23''"Bornes de quantification issues d'un jeu de reference.
24
25On retient des percentiles plutot que le minimum et le maximum :
26une valeur extreme isolee ecraserait l'ensemble de la plage et
27provoquerait une degradation uniforme des poids courants.
28''"
29return (float(np.percentile(reference, bas)),
30float(np.percentile(reference, haut)))
31
32
33def mesurer_temperature(cout: dict, n_macs: int) -> dict:
34''"Estimation de cout de service, par acces memoire.
35
36Sur un accelerateur embarque, l'acces memoire coute plus cher que le
37calcul. Une couche qui lit un tenseur de un megaoctet pour produire
38trois cents multiplications est trois cents fois moins efficace
39qu'une couche qui lit et écrit des dizaines de kilo-octets.
40''"
41octets = (cout["lecture_octets"] + cout["ecriture_octets"])
42intensite = float(n_macs) / max(octets, 1.0)
43return {
44"intensite_calcul": intensite,
45"estimation_ms": octets / 1.0e6 / cout["debit_mo_par_s"] * 1000.0,
46}
Listing 1 — Quantification et mesure de température de service
Décider où faire tourner un modèle, en cinq questions
• Quelle est la latence maximale tolérée ? Elle élimine la plupart des options. Si la réponse est inférieure à 50
millisecondes, le nuage est écarté.
2. Que se passe-t-il si la connexion tombe ? Un système de sécurité ne peut pas dépendre d'un réseau. Un
système d'affichage, si.
3. Quelle est la taille du modèle et sa mémoire ? Elle fixe la frontière entre puce et objet connecté.
4. Quelle est la fréquence de mise à jour nécessaire ? Une réentraînement quotidien impose le nuage ; une
adaptation mensuelle s'accommode du bord.
5. Où sont les données ? Si elles ne peuvent pas quitter le site, il n'y a pas de choix, et il faut le dire au cadrage
plutôt que de le découvrir à l'intégration.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
11
Piege courant
L'objet connecté comme nouvelle surface d'attaqueUn objet connecté est un système informatique accessible
depuis un réseau hostile, dont la durée de vie est de dix ans et dont le fabricant n'existe peut-être plus au
moment de la première vulnérabilité. Le de le garder dans le périmètre de sécurité de l'entreprise : inventaire
des objets connectés, authentification par appareil plutôt que par mot de passe, chiffrement des échanges, et
surtout mise à jour signée. Un objet qu'on ne peut pas mettre à jour ne doit pas être connecté à quelque chose de
vital.
Travaux pratiques 1.1 — Répartir une décision de détection entre l'objet et
le nuage
Duree : 3 h  |   Niveau : Avance  |   Outils : Un jeu de mesures horodatées, un profil de réseau simulé, et une contrainte de
mémoire par objet
Concevoir l'architecture d'un système de détection sur un réseau de capteurs, en justifiant chaque décision
de répartition.
Deroulement
1. Évaluer la taille des données brutes : nombre de mesures, volume horaire, volume annuel par objet.
2. Décider quelles mesures peuvent être eliminées localement sans perte d'information utile, et justifier
par le calcul.
3. Proposer un plan de répartition en trois niveaux, avec pour chaque décision le critère qui l'a imposée.
4. Estimer le volume annuel restant après élimination, et le comparer au coût de transmission actuel.
5. Écrire la règle de comportement en cas de perte de connexion pendant trente minutes, et vérifier qu'elle
est tenable sur l'objet seul.
6. Proposer une stratégie de mise à jour du modèle, et dire qui la déclenche et selon quelle métrique.
Livrable attendu
• N
• o
• t
• e
• d
• '
• a
• r
• c
• h
• i
• t
• e
• c
• t
• u
• r
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
12
• e
• e
• n
• t
• r
• o
• i
• s
• n
• i
• v
• e
• a
• u
• x
• ,
• t
• a
• b
• l
• e
• a
• u
• d
• e
• d
• é
• c
• i
• s
• i
• o
• n
• s
• d
• e
• r
• é
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
13
• p
• a
• r
• t
• i
• t
• i
• o
• n
• a
• v
• e
• c
• l
• e
• u
• r
• c
• r
• i
• t
• è
• r
• e
• ,
• e
• t
• c
• h
• i
• f
• f
• r
• a
• g
• e
• d
• u
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
14
• v
• o
• l
• u
• m
• e
• r
• é
• s
• i
• d
• u
• e
• l
• .
Bareme indicatif
Critere
Points
Chaque décision est justifiée par une contrainte explicite : latence, mémoire, coût ou sécurité
5
Le volume résiduel est chiffré et comparé au volume actuel
3
Le comportement en cas de coupure est tenable sur l'objet seul
2
A retenir
• Le passage de l'objet passif à l'objet autonome change le produit, pas seulement l'architecture.
• On rapproche le calcul de la donnée à autant que la qualité du résultat le permet.
• La quantification est le premier levier d'embarquement, avant toute compression de modèle.
• La surface d'attaque créée par la connectivité est le premier problème de sécurité, et le plus sous-estimé.
Chapitre 1.2
Modélisation et jumeaux numériques
Un jumeau numérique n'est pas une simulation : c'est une simulation reliée à une mesure qui se
recalcule.
Une simulation répond à une question sur un modèle. Un jumeau numérique répond à la même question
sur un système physique, et il le fait en restant branché sur ce système par un flux de mesure. La différence
n'est pas académique : c'est le recalage continu qui transforme une approximation en instrument.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
15
Figure 1 — Le jumeau numérique : un modèle vivant, alimenté par la mesure
θ̂k+1 = argminθ ≤ft| yk - f(xk, θ) |2
W + λ ≤ft| θ - θ̂k |2
W
(T.1)
Le recalage est une régression sur les seules mesures récentes, pondérée, et régularisée par l'estimation
précédente. Les deux termes regularization du modèle sont indispensables : sans le terme de régularisation, un
pic de mesure suffit à déplacer les paramètres et à dégrader la prédiction.
Horizon
Apport
Limite
Exemple
Milliseconde
état instantané fidèle du systèmecoût de
calcul de la mise à jour
suivi d'un procédé continu
Heure
évolution et détection de dérive
qualité du modèle sur la plage
courante
maintenance prédictive
Jour
projection à court terme
incertitude qui croît vite
planification de charge
Semaine
essai de scénarios sans risque
qualité 
des 
données 
d'entrée 
du
scénario
planification de production
Mois
simulation de décisions majeures
exigence de validation clinique ou
réglementaire
essai d'un protocole thérapeutique
Tableau 1 — Ce qu'un jumeau numérique apporte selon l'horizon
Plus l'horizon s'allonge, plus la validation devient le verrou. Un jumeau de procédé se valide par la reproductibilité de ses
prédictions ; un jumeau de patient demande un avis éthique et une validation clinique, et la durée passe de quelques
semaines à plusieurs années.
Un jumeau numérique n'est pas une source de vérité
Un jumeau est un modèle, donc une approximation, donc une source d'erreur. L'utiliser comme vérité revient
àtook une décision sur une prédiction sans mesurer l'erreur commise. Trois pratiques réduisent le risque :
comparer systématiquement la prédiction à la mesure réelle sur une période de référence, publier l'erreur
observée avec le résultat, et refuser toute décision irréversible fondée sur un jumeau dont l'erreur n'a pas été
caractérisée.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
16
Piege courant
Calibrer un jumeau sur des données de laboratoireUn modèle calibré sur un banc d'essai donne des prédictions
fascinantes et fausses dès qu'il est confronté au système réel. Les écarts entre les deux ne sont pas du bruit : ils
traduisent toutes les conditions que le banc ne reproduisait pas — usure, variation de température, tolérance de
fabrication, environnement. Le recalage ne corrigé pas ces écarts par apprentissage : il faut les identifier, un par
un, en documentant chaque différence entre le banc et le réel.
Astuce
Un jumeau numérique se conduit comme un instrument d'étalonnage, pas comme un oracle. On ne lui demande
pas la vérité, on lui demande où regarder en premier : son intérêt réside dans sa capacité à indiquer la mesure
qui informera le plus, pas à fournir la mesure.
A retenir
• Un jumeau numérique se distingue d'une simulation par le recalage continu à partir d'une mesure réelle.
• Le terme de régularisation est indispensable : sans lui, un pic de mesure suffit à dégrader la prédiction.
• L'horizon d'usage conditionné la méthode de validation, pas l'inverse.
• Un jumeau sert à indiquer où mesurer, pas à fournir la mesure : c'est ce qui en fait un instrument.
Chapitre 1.3
Robotique et niveaux d'autonomie
Monter un niveau d'autonomie est une décision sur la garantie, pas sur la puissance de calcul.
Un robot est un système embarqué qui agit sur le monde physique. L'erreur d'un logiciel se corrigé en
redémarrant ; l'erreur d'un robot casse quelque chose. Cette différence entreprises tout le conception, et se
traduit par une échelle d'autonomiale qui raisonne moins en ADN qu'en garantie.
Figure 1 — Les cinq niveaux d'autonomie d'une machine
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
17
Niveau
Qui décide
Ce qui fonctionneCe qui empêche
de monter
Commande directe
l'opérateur, 
en 
continuaucune
ambiguïté sur la responsabilité
l'opérateur 
ne 
peut 
pas 
être
disponible en continu
Assistance
l'opérateur, la machine corrige
l'humain reste dans la boucle à
chaque action
la 
correction 
automatique 
peut
contredire l'opérateur
Autonomie partielle
la machine, pour une tâche bornée
la tâche et ses conditions sont
définies à l'avance
l'environnement réel s'écarte des
conditions définies
Autonomie conditionnelle
la machine, sauf cas Critics
les cas_INSTANCE sont énumérés et
le repli est défini
l'énumération des cas_INSTANCE est
toujours incomplète
Autonomie pleine
la machine, avec declaration
la machine déclare ses limites et son
domaine de validité
la confiance accordée à la déclaration
elle-même
Tableau 1 — Les cinq niveaux et ce qui manque à chacun pour monter
Chaque montée de niveau déplace la charge de la preuve : on passe de « l'humain décide » à « l'humain vérifie ». C'est un
changement de régime juridique autant que technique.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
18
1from dataclasses import dataclass, field
2from enum import Enum
3
4
5class Niveau(Enum):
6COMMANDE = 0
7ASSISTANCE = 1
8TACHE_BORNEE = 2
9CONDITIONNELLE = 3
10PLEINE = 4
11
12
13@dataclass
14class Garantie:
15''"Ce que le systeme sait dire sur lui-meme, avant d'agir.
16
17L'autonomie d'un systeme physique ne se mesure pas a son
18intelligence, mais a la precision de ce qu'il sait declarer sur
19ses propres limites. Un systeme de niveau 3 qui sait dire "je ne
20sors pas de ce perimetre" vaut mieux qu'un systeme de niveau 4
21qui ne sait rien dire du tout.
22''"
23
24niveau: Niveau
25perimetre_valide: frozenset
26incertitude_max: float
27conditions_de_sortie: tuple = field(default_factory=tuple)
28
29def peut_agir(self, observation: str, incertitude: float) -> tuple[bool, str]:
30if observation not in self.perimetre_valide:
31return False, ("observation hors du domaine appris : %s" % observation)
32if incertitude > self.incertitude_max:
33return False, ("incertitude %0.2f au-dessus du seuil %0.2f"
34% (incertitude, self.incertitude_max))
35return True, "conditions remplies"
36
37def decliner(self, action: str, motif: str) -> dict:
38''"Journalise le refus : une non-action doit etre tracee comme une action.
39
40En usage industriel ou medical, l'absence de trace d'un refus
41est indiscernable d'une panne du systeme. Or ces deux evenements
42n'appellent pas la meme suite : l'un s'archive, l'autre s'alerte.
43''"
44return {"niveau": self.niveau.name, "action_refusee": action
45"motif": motif, "est_panne": False}
Listing 1 — Ce que le système déclare avant d'agir
Perception, action, et la boucle qui les relie
ut = argminu ∈ 0 ≤ft| zt+1 - f(x̂t, u) |2
Q + |u - ut-1|2
R
(T.2)
Le terme de régularisation sur l'effort est ce qui rend un contrôleur utilisable dans le monde physique : sans lui,
il peut trouver une commande qui atteint l'objectif en une période par une trajectoire violente, irréalisable et
dangereuse. Le choix de la matrice de pondération est un arbitrage entre précision et douceur, et il est
physiquement signifiant.
Concevoir la sécurité d'un système robotique
La sécurité ne se conçoit pas par composants, mais par l'analyse des situations. La séquence qui fonctionne :
• Énumérer les situations dangereuses de l'environnement réel, pas de la liste de la norme.
2. Définir la réaction à chacune : arrêter, reculer, alerter, continuer. Une situation sans réaction décidée est
une situation non traitée.
3. Placer les moyens de détection là où ldanger apparaît, et non là où la mesure est techniquement possible.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
19
4. Tester le pire cas, pas le cas nominal : l'objet est-il immobile, l'opérateur est-il absent, la lumière est-elle
nulle ?
5. Vérifier en conditions dégradées : capteur défaillant, commande retardée, alimentation instable.
6. Rendre la reprise manuelle possible et immédiate : un arrêt d'urgence qui exige un mot de passe est un
arrêt d'urgence qui ne fonctionnera pas.
Astuce
Un robot qui sait dire « je ne sais pas » est plus utile en production qu'un robot qui agit toujours. L.méthode la
plus efficace pour obtenir cette honnêteté est de l'entraîner explicitement sur ses échecs, pas seulement sur ses
réussites.
A retenir
• L'échelle d'autonomie se raisonne en garantie et non en intelligence.
• Monter un niveau déplace la charge de la preuve : l'humain décide, puis l'humain vérifie.
• Sans terme de régularisation, un contrôleur optimal en théorie peut être irréalisable en pratique.
• Un refus tracé n'est pas une panne : les deux événements n'appellent pas la même suite.
Chapitre 1.4
Santé connectée et médecine prédictive
Le déclencheur de la médecine prédictive n'est pas le modèle : c'est le capteur qui fournit la
mesure.
La médecine de la seconde moitié du vingtième siècle attend l'apparition des symptômes pour agir. La santé
connectée inverse l'ordre : elle mesure en continu, cherche le signal faible qui précède la dégradation, et
intervient avant que le patient ne se sente malade. Ce changement n'est possible que parce que le capteur
est devenu accessible — et il se heurte exactement là.
Figure 1 — La médecine réactive, préventive et personnalisée
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
20
Usage
Ce qui est mesuré
Ce que l'IA apporteCe qui reste humain
Surveillance à distance
signes 
vitaux 
continusdétection
d'une dérive, alerte hiérarchisée
validation clinique, décision de prise en
charge
Chirurgie assistée
images, geste du chirurgien
filtrage des tremblements, segmentation,
repérage
le 
chirurgien 
reste 
aux
commandes
Aide au diagnostic
images, biologie, dossier
détection de motifs, comparaison à une
base
l Newton's diagnostic et sa
conséquence
Simulation thérapeutique
réponse physiologique simulée
estimation de l'effet, comparaison de
protocoles
le choix du protocole et son
arrêt
Suivi post-opératoire
température, 
activité, 
données
sensorisées
détection précoce d'une complication
la surveillance humaine et le
contact
Tableau 1 — Les trois usages cardiologistiquement distincts de la mesure continue
Dans les cinq cas, l'intelligence artificielle occupé la même position : elle prépare la décision, elle ne la prend pas. La
raison est structurelle — l'erreur d'un diagnostic automatique est irréversible, alors que celle d'un système d'aide se
corrigé par la relecture.
Évaluer un dispositif de santé connectée : les six questions
• Quelle population ? Un capteur fiable sur une population ne l'est pas sur une autre. Vérifier la diversité des
morphologies et des âges couverts par la calibration.
2. Quel taux de faux positifs ? En surveillance continue, un faux positif par jour et par patient épuise la
vigilance. Le taux acceptable est de quelques alertes par an, pas par heure.
3. Quelle conséquence d'un faux négatif ? C'est le seul critère qui doit commander le seuil, et il n'appartient
pas à l'équipe technique.
4. Quelle traçabilité du dispositif ? Une alerte sans horodatage et sansCapture des données ayant déclenché
est inexploitable en audit.
5. Que se passe-t-il si la donnée manque ? Un capteur qui se déconnecte doit produire un état intermédiaire
explicite, pas une valeur.
6. Qui répond à l'alerte ? Une chaîne d'alerte sans responsable désigné et sans délai de prise en charge est un
dispositif de surveillance sans surveillance.
Données de santé : cadre juridique et portée réelle
Les données de santé sont des données à caractère particulier, soumises à des règles spécifiques : finalité
déterminée et explicite, minimisation, information de la personne, droit d'opposition et d'effacement, sécurité
adaptée à leur sensibilité, et interdiction d'utiliser les données de santé pour la sélection ou la tarification. Deux
conséquences pratiques pour un dispositif connecté : le consentement doit couvrir l'usage réel, pas l'usage qu'on
aimerait avoir un jour ; et l'effacement est techniquement très coûteux dans un système dérivé, où un même
résultat a été copié dix fois. C'est précisément un problème d'architecture, à traiter à la conception.
Piege courant
Le modèle qui se trompe silencieusementUn dispositif de surveillance à distance produit des alertes et des
non-alertes en nombre à peu près comparable au début. Le risque n'est pas l'erreur : c'est que l'erreur se présente
comme une absence d'anomalie, c'est-à-dire comme une bonne nouvelle. Une mesure de qualité obligatoire —
un contrôle de cohérence de la mesure elle-même — est la seule parade : si la mesure ne varie pas du tout, c'est
le capteur qui est en panne, et l'algorithme doit le savoir avant de conclure à l'absence de problème.
Astuce
En santé, la métrique qui manque le plus n'est pas la sensibilité mais la valeur prédictive positive : la
proportion de vraies urgences parmi les alertes. Une sensibilité de 99 % avec une valeur prédictive de 2 %
produit cinquante fausses alertes par vraie urgence, et l'équipe finira par ignorer le canal.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
21
Projet — Concevoir un dispositif de surveillance à distance
Duree : 6 semaines | Equipe : 3 a 5 etudiants | Depot : gitlab + rapport
Un établissement de soins de longue durée souhaité surveiller à domicile cent patients âgés, avec détection
d'une dégradation respiratoire et cardiaque, et alerte vers l'infirmier de garde.
Missions
1. Définir les grandeurs mesurées, leur fréquence, et le mode de calibration du capteur sur cette
population précise.
2. Choisir la grandeur de surveillance et l'algorithme, en indiquant le seuil et sa justification en termes de
coût d'erreur.
3. Calculer le taux de fausses alertes attendu et l'affectation du temps infirmier qu'il représente sur une
semaine.
4. Décrire la chaîne d'alerte complète : qui, par quel canal, en combien de temps, et ce qui se passe si
personne ne répond.
5. Écrire les états intermédiaires obligatoires : capteur déconnecté, capteur bloqué, mesure aberrante.
6. Traiter la question des données : ce qui est transmis, ce qui est conservé, et comment une demande
d'effacement est satisfaite.
Livrables
• N
• o
• t
• e
• d
• e
• c
• a
• d
• r
• a
• g
• e
• d
• u
• d
• i
• s
• p
• o
• s
• i
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
22
• t
• i
• f
• ,
• t
• a
• b
• l
• e
• a
• u
• d
• e
• s
• é
• t
• a
• t
• s
• e
• t
• t
• r
• a
• n
• s
• i
• t
• i
• o
• n
• s
• ,
• c
• a
• l
• c
• u
• l
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
23
• d
• e
• c
• h
• a
• r
• g
• e
• s
• u
• r
• l
• '
• é
• q
• u
• i
• p
• e
• ,
• e
• t
• n
• o
• t
• e
• d
• e
• c
• o
• n
• f
• o
• r
• m
• i
• t
• é
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
24
• d
• e
• s
• d
• o
• n
• n
• é
• e
• s
• .
Évaluation
• L
• e
• j
• u
• r
• y
• v
• é
• r
• i
• f
• i
• e
• q
• u
• e
• l
• e
• t
• a
• u
• x
• d
• e
• f
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
25
• a
• u
• s
• s
• e
• s
• a
• l
• e
• r
• t
• e
• s
• e
• s
• t
• c
• h
• i
• f
• f
• r
• é
• e
• t
• a
• s
• s
• u
• m
• é
• ,
• q
• u
• e
• l
• a
• c
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
26
• h
• a
• î
• n
• e
• d
• '
• a
• l
• e
• r
• t
• e
• a
• u
• n
• r
• e
• s
• p
• o
• n
• s
• a
• b
• l
• e
• n
• o
• m
• m
• é
• ,
• e
• t
• q
• u
• e
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
27
• l
• '
• e
• f
• f
• a
• c
• e
• m
• e
• n
• t
• a
• é
• t
• é
• t
• r
• a
• i
• t
• é
• c
• o
• m
• m
• e
• u
• n
• e
• c
• o
• n
• t
• r
• a
• i
• n
• t
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
28
• e
• d
• '
• a
• r
• c
• h
• i
• t
• e
• c
• t
• u
• r
• e
• .
A retenir
• Le capteur conditionné la médecine prédictive : sans mesure continue fiable, aucun modèle n'aide.
• Dans tous les usages, l'intelligence prépare la décision ; elle ne la prend pas.
• Une valeur prédictive positive faible épuise l'équipe plus sûrement qu'une sensibilité insuffisante.
• Un capteur bloqué produit un état qui ressemble à une absence d'anomalie : le contrôle de cohérence est
obligatoire.
Chapitre 1.5
Défense : essaims, maintenance prédictive,
aide à la décision
La technique est plus avancée que l'institution qui doit la surveiller : c'est là que se joue le facteur
limitant.
L'intelligence artificielle appliqué à la défense relève de trois familles nettement distinctes, qu'il est essentiel
de ne pas confondre : la coordination d'entités autonomes, la maintenance prédictive d'un matériel, et l'aide
à la décision humaine. Les deux dernières sont techniquement éprouvées et sans enjeu ethical majeur. La
première ne l'est pas.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
29
Figure 1 — Les trois usages de l'intelligence dans un système de défense
Consensus : accord exact ∧ temps borné ∧ tolérance à la panne ∧ déterminisme
(T.3)
Les quatre propriétés ne peuvent pas être tenues simultanément dans un système asynchrone où un nœud peut
tomber en panne. Un essaim de drones ne peut pas garantir à la fois l'accord exact de toutes les unités et le
fonctionnement malgré la perte d'une unité. Tout le problème de conception consiste à choisir ce que l'on
abandonné, et à l'assumer.
Usage
Maturité technique
Exigence institutionnellePoint de
blocage réel
Essaims coordonnés
moyenne, démontré en simulationrègle
d'engagement, chaîne de responsabilité
le droit d'emploi de la force
Maintenance prédictive
éprouvée, déployée
confidentialité 
des 
données 
de
maintenance
l'accès 
des 
données 
au
fournisseur
Aide à la décision
éprouvée, sous condition de qualité de
source
droit 
de 
refuser 
une
recommandation
la responsabilité de l'erreur du
système
Identification de cible
dépend entièrement de la source
règles 
d'engagement,
proportionnalité
le taux d'erreur de la source,
jamais le modèle
Tableau 1 — Les trois usages et ce que chacun exige au-delà de la technique
La dernière ligne est la plus importante. L'exactitude d'un système d'identification est celle de sa source de données.
Aucun modèle ne rattrape une source biaisée, et ldisplay l'exactitude du modèle plutôt que celle de la chaîne induit une
confiance injustifiée.
L'arme autonome et la question de la responsabilité
Un système qui décide seul d'un emploi de la force déplace la question de la responsabilité sans la trancher. Qui
assume quand la décision est erronée : le fabricant du système, l'opérateur qui l'a activé, le commandement qui
a défini la règle d'emploi, ou l'État qui l'a Authorized ? Aucune réponse n'est satisfaisante, et c'est pourquoi le
débat est normative autant que technique. Le position productive n'est pas de choisir un camp, mais de poser
trois conditions : une restriction du domaine d'emploi à des situations où l'erreur est réversible, une obligation
de traçabilité complète, et une conservation de la décision humaine sur l'emploi de la force.
Coefficient(d, t) = (1)/(N)∑t' ≤ t 1≤ft[ dt' ≥ seuil(dt') ], seuil(d) = μ(d) + 3 σ(d)
(T.4)
L'écriture naïve du seuil est la source d'erreur la plus fréquente en maintenance prédictive : l'écart-type calculé
sur la série complète inclut les pannes, ce qui gonfle le seuil jusqu'à les rendre invisibles. Le seuil doit être
calculé sur la période saine, et le coefficient surveille la progression de l'écart, pas son existence ponctuelle.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
30
Piège
Mécanisme
Parade
Seuil calculé sur la série complèteles
pannes gonflent l'écart-type et le seuil
calculer le seuil sur la période saine connue
Dérive lente non détectée
l'indicateur reste sous le seuil pendant des
semaines
surveiller la pente de l'écart, pas seulement son
niveau
Surcharge de maintenance
on remplace ce qui fonctionne encore
prioriser par coût d'immobilisation, pas par
probabilité seule
Maintenance dictée par le seul modèle
aucune contradiction possible entre modèle et
terrain
la décision reste humaine, le modèle fournit un
rang
Tableau 2 — Quatre pièges de la maintenance prédictive
Le dernier piège est le plus coûteux : un modèle qui ne peut pas avoir tort sur le terrain finit par être contourné, et l'on
perd à la fois le modèle et la confiance dans l'outil.
Astuce
Dans tous les domaines de ce cours, la question décisive n'est jamais « le modèle est-il bon » mais « que se
passe-t-il quand il se trompe ». Un système dont l'erreur est visible, bornée et rattrapable est utilisable. Un
système dont l'erreur est silencieuse ne l'est pas, quelle que soit sa précision moyenne.
A retenir
• Maintenance prédictive, aide à la décision et essaims n'ont ni la même maturité ni le même statut.
• Un essaim ne peut pas tenir l'accord exact, le temps borné, la tolérance à la panne et le déterminisme à la fois.
• L'exactitude d'un système d'identification est celle de sa source ; la afficher est induire en erreur.
• Un seuil calculé sur une série qui contient les pannes devient incapable de les détecter.
• La question décisive est toujours ce qui se passe quand le système se trompe.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
31
Abréviations, notation et ressources de consultation
Annexes
Annexes
Ce cours se termine par deux annexes de référence. La première donne la signification de chaque sigle
employé, sous les deux formes — sigle et développé — car la litterature emploie indifféremment l'une
ou l'autre. La seconde donne la signification de chaque symbole mathématique : elle permet de relire
une démonstration sans revenir au chapitre dont elle est extraite, et de vérifier qu'un même symbole
garde le même sens d'un chapitre à l'autre.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
32
Chapitre A.1
Liste des abréviations
Les sigles ci-dessous sont ceux que le cours emploie. Chacun est donné avec sa forme développée
et le sens précis qu'il prend ici, qui n'est pas toujours celui qu'on lui donne ailleurs.
Un sigle employé sans être développé oblige le lecteur à le reconnaître au passage, ou à l'abandonner. Le
tableau ci-dessous ferme la liste de ceux que le cours emploie : il est exhaustif pour ce document, et non
pour la discipline.
Sigle
Forme développée
Sens dans ce cours
ADN
Acide désoxyribonucléique
Support de l'information génétique, cible des applications de séquençage.
IoT
Internet of Things
Réseau d'objets connectés qui échangent sans intervention humaine.
LiDAR
Light Detection and Ranging
Mesure de distance par impulsion laser.
MEC
Mobile Edge Computing
Traitement placé au plus près de l'utilisateur, en bord de réseau.
MQTT
Message Queuing Telemetry Transport
Protocole de messagerie léger pour objets connectés.
OBD
On-Board Diagnostics
Prise de diagnostic embarquée sur un véhicule.
PACS
Picture Archiving and Communication
System
Système de gestion des images médicales.
PHM
Prognostics and Health Management
Prévision de défaillance et gestion de la santé d'un équipement.
RADAR
Radio Detection and Ranging
Sonde électromagnétique, qui donne distance et vitesse.
SLAM
Simultaneous Localization and Mapping
Localisation et cartographie simultanées d'un robot mobile.
V2X
Vehicle-to-Everything
Communication d'un véhicule avec l'infrastructure et avec les autres
véhicules.
W3C
World Wide Web Consortium
Organisme de normalisation du web.
Tableau 1 — Abréviations employées dans le cours
Chapitre A.2
Table de notation
Les symboles ci-dessous gardent le même sens d'un chapitre à l'autre. Lorsqu'un chapitre doit
réemployer un symbole pour un autre objet, il le redéclare sur la page même.
La notation est celle du cours : vecteurs en gras, matrices en majuscules grasses, scalaires en italique. Les
espérances sont notées E, les lois de données D, les espaces de paramètres Θ.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
33
Symbole
Signification
x ∈ ℝd
Vecteur d'état d'un système physique ou d'un véhicule.
u ∈ ℝm
Vecteur de commande.
f(x, u)
Dynamique du système.
y
Mesure, ou sortie du capteur.
H(x)
Fonction d'observation du capteur.
zt
Mesure du capteur à l'instant t.
xt
État estimé à l'instant t.
Pt
Matrice de covariance de l'estimation à l'instant t.
F
Matrice de transition d'état.
H
Matrice d'observation.
Q
Covariance du bruit de processus.
R
Covariance du bruit de mesure.
Σ
Covariance d'un vecteur aléatoire.
ρ
Coefficient de corrélation entre deux grandeurs.
T
Température mesurée, en kelvins ou en degrés Celsius.
pm
Pression mesurée par un capteur de pression.
tpi
Délai entre deux images, en secondes.
Δ p
Période d'échantillonnage du capteur.
fc
Fréquence de la porteuse, en hertz.
σ
Écart-type d'une grandeur mesurée.
Tableau 1 — Symboles mathématiques et leur signification
Convention
Toute divergence constatée entre cette table et un chapitre signale une erreur de transcription, non une
définition nouvelle : la table fait foi.
A retenir
• Un sigle employé sans être listé ici est un oubli de l'auteur, non une définition nouvelle.
• Un symbole qui change de sens d'un chapitre à l'autre rend toute démonstration ininterprétable : c'est la
principale cause des contresens que nous avons relevés.
• Ces deux tables sont les seules parties du cours à maintenir à la main : le reste se relit tout seul.
Index des figures et des tableaux
Référence rapide du matériel visuel
Figures
1.  De l'objet connecté passif à l'objet.Application intelligente
1.  Le jumeau numérique : un modèle vivant, alimenté par la mesure
1.  Les cinq niveaux d'autonomie d'une machine
1.  La médecine réactive, préventive et personnalisée
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
34
1.  Les trois usages de l'intelligence dans un système de défense
Tableaux
1.  Les trois niveaux de répartition d'une décision
1.  Ce qu'un jumeau numérique apporte selon l'horizon
1.  Les cinq niveaux et ce qui manque à chacun pour monter
1.  Les trois usages cardiologistiquement distincts de la mesure continue
1.  Les trois usages et ce que chacun exige au-delà de la technique
2.  Quatre pièges de la maintenance prédictive
1.  Abréviations employées dans le cours
1.  Symboles mathématiques et leur signification
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
35
Fin du document
Intelligence Artificielle Avancée & Federated Learning — Fondations mathématiques de
l'apprentissage automatique, algorithmes fédérés, protection de la vie privée, défense contre les attaques,
grands modèles de langage fédérés, systèmes embarqués, renforcement appris, applications critiques
(santé, V2X), plateforme de référence FedX et feuille de route de recherche.<br/>Ghiloufi Jamel,
Architecte Logiciel Principal — Pixel Software Design<br/>Département de Recherche & Développement
— Recherche<br/>Pixel Software Design — Édition 2026
© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou
diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans
autorisation écrite préalable de l'auteur.
Document généré automatiquement le 29/09/2026 — mise en page Pixel Software Design.
"""


IA_AUDIO_TEXT = r"""Pixel Software Design — Département de Recherche & Développement
PIXEL SOFTWARE DESIGN
Département de Recherche & Développement
Intelligence Artificielle
Avancée
& Federated Learning
•  Fondations de l'intelligence artificielle
•  Algorithmes d'apprentissage fédéré
•  Confidentialité, attaques et défenses
•  Applications et grands modèles fédérés
•  Framework FedX de référence
•  Nouveaux fronts de recherche
•  Travaux pratiques, projets et évaluation
Auteur
Ghiloufi Jamel
Fonction
Architecte Logiciel Principal
Direction
Département de Recherche & Développement
Service
R&D - Intelligence Artificielle Avancée & Apprentissage Fédéré
Niveau
Recherche
Édition
Édition 2026 — 1.0
Copyright
© Pixel Software Design
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou
diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans
autorisation écrite préalable de l'auteur.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
2
Copyright et mentions légales
Éditeur
Pixel Software Design
Auteur
Ghiloufi Jamel
Fonction
Architecte Logiciel Principal
Département
Département de Recherche & Développement
Intitulé
Intelligence Artificielle Avancée & Federated Learning
Sous-titre
Fondations mathématiques de l'apprentissage automatique, algorithmes fédérés,
protection de la vie privée, défense contre les attaques, grands modèles de langage
fédérés, systèmes embarqués, renforcement appris, applications critiques (santé,
V2X), plateforme de référence FedX et feuille de route de recherche.
Édition
Édition 2026 (version 1.0)
Langue
Français
Niveau
Recherche
Collection
Supports de formation et de recherche, Pixel Software Design
Droits d'auteur
© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation
ou diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite
sans autorisation écrite préalable de l'auteur.
Droits de l'auteur. Ghiloufi Jamel est l'auteur unique de l'ensemble du contenu scientifique, pédagogique et
technique de cet ouvrage. Toute adaptation, traduction, reproduction ou exploitation, y compris partielle, requiert
une autorisation écrite préalable.
Droits des tiers. Les algorithmes, modèles et travaux cités restent la propriété de leurs auteurs respectifs. Les
références employées figurent en fin d'ouvrage, ce qui permet de remonter au travail original pour toute
affirmation chiffrée.
Marques et licences externes. PyTorch, TensorFlow, Flower, Opacus, MONAI, scikit-learn et PySyft sont des
logiciels libres sous licences respectives (BSD, Apache 2.0, MIT). Leur usage dans ce document est purement
pédagogique et n'emporte aucune prescription commerciale.
Mentions relatives aux données et aux expérimentations
Document pédagogique à usage de formation interne. Les exemples de code fournis sont livrés à titre pédagogique
; les résultats numériques illustrés sont issus d'expérimentations conduites dans un cadre de recherche et ne
constituent pas des performances de production.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
3
Ce support synthétise les travaux de recherche du Département de Recherche & Développement de Pixel Software
Design sur l'intelligence artificielle distribuée, l'apprentissage fédéré, la protection de la vie privée et les systèmes
embarqués intelligents.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
4
Sommaire
Structure détaillée du cours
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 8
Partie 1 — IA et Audio Génératif
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 9
1.1 La chaîne de génération audio
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 10
1.2 Génération musicale et cohérence de longue durée
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 11
1.3 Filigrane sonore et traçabilité
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 13
1.4 Codecs neuronaux et qualité de reconstruction
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 14
1.5 Audio spatial et rendu temps réel
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 18
Annexes
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 19
A.1 Liste des abréviations
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 19
A.2 Table de notation
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
5
Partie
Thème
Contenu
Compétence visée
Durée
Partie 1
Fondations
Statistique, optimisation, courbes d'apprentissage
Comprendre et formaliser
2-3 semaines
Partie 2
Algorithmes FL
FedAvg, convergence, hétérogénéité, système
Implémenter et régler
3-4 semaines
Partie 3
Confidentialité
DP, attaques, défenses, agrégation sécurisée
Auditer et sécuriser
2-3 semaines
Partie 4
Applications
FedLLM, santé, V2X, FedRL, TinyML, graphes
Transposer à un domaine
3-4 semaines
Partie 5
Framework FedX
Architecture, API, benchmarks, exploitation
Industrialiser
2 semaines
Partie 6
Nouveaux fronts
FedCL, FedCI, SNN, FedGL, feuille de route
Ouvrir la recherche
2 semaines
Partie 7
TP et projets
9 labs, 5 projets, corrigés, évaluation
Faire et rendre
4-6 semaines
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
6
Préface
Comment utiliser ce cours
Ce support est conçu pour un parcours de formation et de recherche couvrant l'ensemble de la chaîne de valeur de
l'intelligence artificielle distribuée : les fondations mathématiques, les algorithmes d'apprentissage fédéré, les
menaces et défenses, les applications de pointe, une plateforme de référence opérationnelle, et enfin les nouveaux
fronts ouverts par la recherche du Département.
Ce n'est pas un manuel de référence à lire d'un trait : c'est un manuel opératoire. Chaque chapitre alterne
exposition, formalisation, mise en œuvre numérique et évaluation. Les listings sont complets et exécutables ; les
tableaux comparatifs servent de grille de décision ; les schémas d'architecture servent de support de revue de
conception.
Public et prérequis
Le contenu s'adresse à des étudiants de master et de doctorat, à des ingénieurs IA et à des praticiens de la
recherche appliquée. Les prérequis sont la connaissance de l'apprentissage automatique classique, de
l'algorithmique numérique et des bases de probabilités. Les parties 1 à 3 sont auto-suffisantes pour un étudiant qui
découvre le domaine ; les parties 4 à 7 supposent la mécanique et les outils présentés dans la partie 2.
Conventions de lecture. Une expression mathématique est encadrée par deux signes dollars ; un identifiant, un
fichier ou une commande est écrit en caractères à chasse fixe ; les encadrés Définition, Théorème, Méthode et
Attention signalent les points à maîtriser et les pièges fréquents. Les renvois de la forme « voir chapitre 3.2 »
désignent le second chapitre de la troisième partie.
Progression pédagogique
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
7
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
8
De la description textuelle à la scène sonore
Partie 1
IA et Audio Génératif
L'audio est le dernier grand médium à avoir été transformé par l'apprentissage automatique, et il
s'oppose aux autres sur un point : l'encre est irréversible. Une image générée peut être corrigée par
une retouche ; une milliseconds de son fausse ne peut pas être rattrapée. Ce cours décrit la chaîne
technique de la génération sonore, et insiste sur ce qui la rend sensiblement différente de tout le reste
: la continuité temporelle, la restauration après transformation, et l'exigence de traçabilité de
l'origine.
Objectifs de la partie
• Décrire la chaîne complète, de la description textuelle au flux audio, et situer le rôle du codec.
• Expliquer pourquoi la cohérence d'une composition longue est un problème distinct de la qualité locale.
• Comprendre ce qu'un filigrane sonore garantit, ce qu'il ne garantit pas, et pourquoi ce n'est pas une preuve.
• Distinguer un codec appris d'un codec à formule, et expliquer pourquoi les deux qualités se mesurent
séparément.
• Dimensionner un budget temps réel et justifier le partage entre acquisition, traitement et restitution.
• Expliquer comment une source sonore générée devient mobile sans recalcul géométrique.
Plan de la partie
1.  La chaîne de génération audio
2.  Génération musicale et cohérence de longue durée
3.  Filigrane sonore et traçabilité
4.  Codecs neuronaux et qualité de reconstruction
5.  Audio spatial et rendu temps réel
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
9
Chapitre 1.1
La chaîne de génération audio
L'audio de qualité n'est pas un fichier : c'est une reconstruction, et la reconstruction a un coût.
La génération audio repose sur une idée simple et une idée difficile. L'idée simple : comme le texte, le son
peut être découpé en unités discrètes et traité par un modèle de séquence. L'idée difficile : ces unités
doivent être apprises, pas fixées, et la qualité dépend autant du codec qui transporte le son que du modèle
qui le compose.
Figure 1 — De la description textuelle à l'audio : la chaîne de génération
hatmathbfa = D≤ft( E≤ft( mathbfa ) ), L = ≤ft| mathbfa - D(E(mathbfa)) |2 + λ ≤ft|
zenc(mathbfa) - ztgt |2
(A.1)
L'encodeur E transforme le signal en une représentation discrète, le décodeur D la reconstruit. La seconde partie
de la perte contraint l'espace de représentation à ressembler à un espace de texte, ce qui permet au même
mécanisme d'autorégression de servir aux deux. Le son est donc traité comme une langue dont l'alphabet est
appris.
Étape
Fonction
Échec typique
Détection
Description
exprimer l'intentiondescription trop
pauvre, résultat générique
impossible à détecter sans écoute
comparative
Représentation
projeter le son en jetons
perte d'information dans les transitoires
audible sur les percussions
Génération
produire la séquence
cohérence qui se dégrade sur la durée
audible à l'écoute attentive, en fin
de morceau
Décodage
reconstruire le signal
distorsion de la reconstruction
mesurable, par comparaison
Spatialisation
placer les sources
image auditive incohérente
mesurable, par comparaison
Tableau 1 — Les cinq étapes et ce qui peut y échouer
La colonne de droite est la plus utile en pratique : les deux dernières étapes sont mesurables, donc automatisables en
recette, et c'est là que la qualité se gagne sans aucun travail d'écoute.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
10
Évaluer une chaîne de génération audio, en cinq mesures
• Taux d'artefacts transitoires : proportion d'événements percussifs dont la reconstruction présente un
pré-éclairement. C'est le défaut le plus caractéristique d'un codec appris sous-entraîné, et il est mesurable
automatiquement.
2. Ratio de compression perçu : à qualité égale, combien de bits par seconde. Cette mesure doit être faite sur
une écoute aveugle, jamais sur une comparaison visuelle des spectrogrammes.
3. Dérive de cohérence : écart entre les métriques calculées sur le premier quart et sur le dernier quart du
morceau. Une dégradation régulière est le signé le plus fiable d'une perte de cohérence en fin de composition.
4. Loyauté à la description : distance entre les attributs musicaux extraits du signal et ceux demandés. Mesure
dificilement automatisable, mais qui doit être effectuée par un panel.
5. Taux de détection du filigrane : proportion de sorties où le filigrane est retrouvé après compression et après
reconversion. C'est la seule mesure qui rende la traçabilité opérationnelle.
Le codec sépare deux qualités distinctes
Un modèle génératif médiocre reste inaudible après un bon codec : la reconstruction est fidèle à ce que le
modèle a produit. Réciproquement, un bon modèle dont la sortie traverse un mauvais codec perd précisément
les transitoires qui portent l'information rythmique. Les deux qualités se mesurent séparément, s'optimisent
séparément, et un test qui les confond ne peut conclure sur aucune des deux.
A retenir
• L'audio est traité comme une langue dont l'alphabet est appris, non comme un signal à compresser.
• La représentation apprise perd d'abord les transitoires, qui portent l'information rythmique.
• La qualité du modèle et celle du codec se mesurent et s'optimisent séparément.
• Les deux dernières étapes de la chaîne sont automatisables, et c'est là que la qualité se gagne sans travail
d'écoute.
Chapitre 1.2
Génération musicale et cohérence de longue
durée
Une suite de notes justes n'est pas une composition. La cohérence est un problème de structure,
pas de sonorité.
La génération musicale a une difficulté propre, absente de la génération d'images : le temps. Une image est
jugée dans son ensemble, ce qui permet au modèle d'optimiser globalement. Un morceau de trois minutes
est jugé par son intérieur, et un modèle qui optimisé note par note produit une suite localement correcte et
globalement incohérente.
p(x1:T) = ∏t=1
T p(xt | x1:t-1, c), dégradation : M(x1:q) ≠ M(xT-q:T)
(A.2)
Le produit montre que la vraisemblance d'un morceau multiplie les probabilités élémentaires : un décalage de
routine de quelques centièmes suffit à rendre un morceau de plusieurs minutes improbable. La seconde
expression est la mesure opérationnelle du problème : on compare les métriques structurelles du début et de la
fin.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
11
Mécanisme
Ce qu'il maintient
Limite
Contexte étendu
la tonalité et l'harmonie sur la duréecoût
croissant avec la longueur du contexte
Reprise de motifs
l'identité thématique
produit de la répétition si mal maîtrisé
Conditionnement global
le style, le genre, l'instrumentation
ne garantit pas la structure interne
Planification explicite
la forme : introduction, couplet, refrain,
transition
impose une structure au texte musical
Tableau 1 — Les quatre mécanismes qui maintiennent la cohérence
Le quatrième mécanisme est le plus efficace et le moins utilisé spontanément. On ne demande pas à un modèle de
produire une chanson, on lui demande de produire une section, avec des consignes distinctes pour chacune.
Contrôler la forme plutôt que la substance
• Découper en sections de vingt à quarante secondes : introduction, couplet, refrain, pont, conclusion.
2. Rédiger les paroles section par section, en indiquant ce que la section doit faire et non seulement ce qu'elle
doit contenir.
3. Fixer les paramètres de style par section, et les faire varier de façon contrôlée : le refrain revient avec la
même signature, le pont la modifie.
4. Générer chaque section indépendamment, puis les assembler.
5. Vérifier la continuité tonale à l'assemblage, et refaire la section en cas de rupture.
L'étape 5 est celle qui produit la plus grande amélioration immédiate, et celle que l'on ne fait pas parce que
l'assemblage semble évident.
Un système qui respecté parfaitement la description produit une musique inaudible, parce que l'absence
de contraste est elle-même une audibilité nulle. Les termes « faible variation » et « aléatoire » sont tous
deux des défauts, et le style est précisément ce qui se tient entre les deux. Les métriques de fidélité au
style ne détectent aucun des deux défauts : elles mesurent la conformité, pas l'effet.
Confondre fidélité au style et absence d'effet
Astuce
Écoutez toujours la jonction, pas seulement les sections. L'essentiel de l'impression de qualité se joue sur les
deux secondes qui entourent chaque couture, et c'est exactement là que l'name d'assemblage ne regarde jamais.
A retenir
• Le temps est la difficulté propre de la génération musicale, absente de la génération d'images.
• Quatre mécanismes maintiennent la cohérence, dont la planification explicite de la forme est la plus efficace.
• Contrôler la forme section par section est plus fiable que de demander un morceau entier.
• Les métriques de fidélité au style mesurent la conformité, et ne détectent ni l'absence de contraste ni le
désordre.
Chapitre 1.3
Filigrane sonore et traçabilité
Un filigrane n'est pas une preuve : c'est un signal dont la détection est une hypothèse statistique.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
12
Figure 1 — Le filigrane sonore : rendre l'origine détectable
Rendre l'origine d'un contenu généré détectable est un problème de difficulté réelle, et non une formalité.
Le signal est bruité, compressé, ré-échantillonné, parfois ressorti d'une vidéo. Le filigrane doit survivre à
tout cela tout en restant inaudible. Ces deux exigences sont en tension : ce qui résiste à la compression
introduit des artefacts audibles.
s' = s + α w, w ⊥⊥ s, E≤ft[ ≤ft| D(s') - D(s) | ] ≤ ε
(A.3)
La première relation définit l'injection : un signal indépendant du contenu, ajouté à faible amplitude. La seconde
contrainte est celle de l'imperceptibilité, et c'est elle qui plafonne la robustesse. Un filigrane plus robuste coûte
de l'audibilité, jamais l'inverse.
Propriété
Vrai ?
Ce qu'il faut écrire à la place
Le contenu est d'origine humaine
fauxaucun filigrane ne
prouve une origine
humaine
Le contenu a été généré par un modèle déclaré
impossible
on peut seulement établir une probabilité de détection
Le filigrane résiste à la compression
partiellement
le taux de survie doit être mesuré et publié
Le filigrane résiste à l'édition
faiblement
l'édition est le point faible principal
Le contenu est conforme à une licence
faux
la licence est une question de droit, pas de signal
Le contenu porte une attribution
vrai, si le signal est
l'attribution porte sur l'origine déclarée, rien de plus
Tableau 1 — Ce que le filigrane garantit et ce qu'il ne garantit pas
La troisième colonne est la seule formulation acceptable dans une politique d'usage. La première colonne pose la
question, la deuxième montre ce qu'on ne peut pas affirmer, et la troisième indique ce qu'on peut dire.
Un test de filigrane n'est pas un test de vérité
Un test qui répond « présent » prouve qu'un signal statistique détecté est cohérent avec le filigrane attendu. Un
test qui répond « absent » ne prouve pas l'absence de génération : le signal a été effacé, l'audio a été retraité, ou
le test est faux positif dans l'autre sens. Traiter une absence de détection comme une preuve d'innocence, ou une
détection comme une preuve de culpabilité, sont deux erreurs symétriques et toutes deux fréquentes. Le seul
usage défendable est statistique et agrégé : estimer une fréquence sur un corpus, jamais conclure sur un cas
unique.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
13
Cadre juridique de l'audio généré
Trois régimes doivent être distingués selon les juridictions, et les confondre est la principale source d'erreur
juridique. Droit d'auteur : une œuvre créée par une personne est protégée ; une œuvre purement générée par
une machine est, dans la plupart des systèmes juridiques, dépourvue d'auteur, donc tombant dans le domaine
public — sauf si l'humain peut être identifié comme auteur de la conception, ce qui est discuté. Droit des
interprètes : la voix d'un interprète reste protégée, et sa synthèse sans consentement relève de protections
spécifiques, indépendantes du droit d'auteur. Droit de la publicité et de l'information : la prospective
juridique de certains juridictions va jusqu'à interdire la synthèse vocale non déclarée, ce qui déplace le problème
de l'auteur vers l'information de l'auditeur. Un dispositif de filigrane sert ici moins à prouver qu'à informer, et
c'est souvent là qu'il trouve sa justification la plus solide.
Astuce
Le bon usage d'un filigrane n'est pas la Enforcement, c'est l'information. Afficher une mention, publier un taux
de survie mesuré, et documenter les limites : cela protège l'émetteur et l'auditeur bien mieux qu'une détection
binaire présenté comme une preuve.
A retenir
• L'injection d'un filigrane et l'imperceptibilité sont en tension : la robustesse se paie en audibilité.
• Un test de filigrane est une estimation statistique, jamais une preuve sur un cas unique.
• L'absence de détection ne prouve pas l'absence de génération, pas plus que la détection ne prouve la
culpabilité.
• L'usage le plus solide du filigrane est l'information de l'auditeur, avec des limites publiées.
Chapitre 1.4
Codecs neuronaux et qualité de
reconstruction
Un codec appris n'applique pas une formule : il en apprend une. Toute la difficulté est là.
La compression audio classique repose sur une décomposition en fréquences, un classement par
importance, et un codage arithmétique. L'opération décisive — deciding ce qui compte et ce qui peut être
détruit — y est fixée à l'avance par le concepteur. Un codec neuronal apprend cette opération à partir
d'exemples, ce qui lui permet d'atteindre des débits bien inférieurs à qualité égale.
hatmathbfa = D_θ(E_ϕ(mathbfa)), r(b) = (-log2 P(hatmathbfa))/(b), MMSE(r, s) = argminr
≤ft[ r + λ D(Er(mathbfa), mathbfa) ]
(A.4)
Le débit se lit directement dans le nombre de bits par échantillon : moins le modèle est contraint, moins il
produit de bits. Le terme final est la forme générale du compromis débit-distorsion, et c'est le paramètre de
conception central d'un codec neuronal.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
14
Critère
Codec à formule
Codec appris
Qui gagne
Débit à qualité égale
élevé
très faible
appris
Comportement sur contenu
inconnu
prédit par la formule
imprédit, mesuré seulement par essai
formule
Fidélité de la phase
excellente
parfois dégradée
formule, pour la voix
Coût de calcul
faible
élevé
formule
Adaptation à un usage
impossible sans réécrire
réentraînement ciblé
appris
Explicabilité de la perte
totale
faible
formule
Robustesse de la recette
un test suffit
il faut un corpus de référence
formule
Tableau 1 — Codec à formule et codec appris : la comparaison honnête
Un codec appris est meilleur en débit et pire en explicabilité, ce qui a une conséquence directe : il faut construire une
recette de référence, et cette recette coûte plus cher que le codec lui-même.
Construire une recette de référence pour un codec
• Constituer un corpus représentatif de ce que l'usage réel transporte : voix, musique, sons de ville, silence. Un
corpus homogène produit un codec excellent sur un contenu et inutilisable sur les autres.
2. Définir la métrique de référence, et une seule. Un test multi-métriques finit toujours par être ajusté sur la
métrique la plus commode, pas la plus pertinente.
3. Fixer le débit et le délai de reconstruction comme paramètres de recette, et non comme paramètres
d'évaluation.
4. Ajouter le test de régression le plus dur : un début et une fin silencieux, parce que c'est là que les artefacts
d'encodage se font entendre.
5. Décider de la conduite en cas d'échec : dégrader le débit, ou refuser la transmission. Cette décision doit être
automatisée, car elle sera prise en charge, à trois heures du matin, par un composant.
Astuce
Le test de régression le plus rentable pour un codec audio est l'écoute d'un silence suivi d'un début. Presque tous
les défauts d'encodage s'y manifestent, et ce test prend deux minutes.
A retenir
• L'opération décisive d'un codec — ce qui peut être détruit — est fixé dans un codec à formule et apprise dans
un codec neuronal.
• Le débit se lit dans le nombre de bits par échantillon ; la contrainte de qualité le détermine.
• Un codec appris exige une recette de référence, et cette recette coûte plus cher que le codec.
• Le test de régression le plus rentable est un silence suivi d'un début.
Chapitre 1.5
Audio spatial et rendu temps réel
Un son généré est mobile par construction : la position suffit, aucun recalcul géométrique n'est
nécessaire.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
15
Figure 1 — Audio spatial : la scène écoutée, pas seulement entendue
L'audio spatial se repose sur trois signaux physiques, tous mesurables et tous calculables à partir d'une
position : le temps d'arrivée relatif, la différence d'intensité, et la différence de phase. Ils suffisent à localiser
une source. La conséquence pratique est considérable pour la génération : une source synthétisée est mobile
sans coût, puisque la position de l'auditeur suffit à recalculer les trois signaux en continu.
Δ t ≈ (dg - dd)/(c), Ig ∝ (1)/((dg + h)2), Δ φ = (2π f ≤ft( dd - dg ))/(c)
(A.5)
La différence de phase n'est exploitable que lorsque le décalage de chemin reste inférieur à une demi-longueur
d'onde, soit environ 1 500 hertz pour une vitesse de son de 340 mètres par seconde. Au-delà, l'oreille perd
complètement l'information de phase, et la localisation se fait sur les deux autres signaux — ce qui explique que
la précision perçue chute brutalement avec la distance sur les sources aiguës.
Moduler une source générée selon la position d'écoute
• Partir d'une source monaurale de bonne qualité, et ne pas générer directement une source stéréo : la
correction de position s'applique mieux à un signal de référence.
2. Calculer les deux distances de la source à chaque oreille, à chaque instant : c'est une opération de trois
multiplications, négligeable devant le rendu.
3. Appliquer le retard et l'atténuation, et non un simple panoramique. Un panoramique ne modélise ni la
distance, ni l'occlusion, ni la propagation dans un espace fermé.
4. Modéliser l'occlusion par filtrage passe-bas variable, puis par atténuation, dans cet ordre : un obstacle de
petite dimensionné absorbe surtout les hautes fréquences.
5. Ajouter la réverbération de l'espace, avec une durée de réverbération et un temps de pré-délai qui varient
avec la distance et la taille de la pièce.
6. Vérifier l'audition au point de l'auditeur, et non au point d'émission : c'est là que la scène est perçue.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
16
Figure 2 — Le temps réel audio : trois budgets qui ne se concertent pas
Phase
Budget
Ce qui peut s'y passerCe qui ne peut pas
s'y passer
Acquisition
10 ms
captation, conversion, tamponaucun appel à
un service distant
Traitement
20 ms
filtrage, mélange, synthèse courte
un appel à un modèle de génération de plusieurs
secondes
Restitution
10 ms
lecture, mélange final
aucune attente de quelqueque nature
Tableau 1 — Le partitionnement du budget de 40 millisecondes
Un appel à un modèle de génération de plusieurs secondes ne peut pas se trouver dans le chemin de restitution. La
solution est toujours la même : produire à l'avance, mettre en tampon, et laisser le tampon amortir l'attente en acceptant
un retard de quelques dizaines de millisecondes.
L'erreur est intuitive et apparaît régulièrement : dès que la latence de l'appel dépasse le budget de la
fenêtre audio, on entend un décrochage. Ce n'est pas un défaut de qualité sonore, c'est un défaut de
conception. La parade comporte deux volets : un tampon dimensionné pour la pire latence observée, avec
une politique explicite en cas de dépassement — silence, son de repli, ou message — et une surveillance du
taux de dépassement, qui est un indicateur de service à part entière.
Appeler un modèle distant depuis le chemin de restitution
Travaux pratiques 1.1 — Budget temps réel et politique de repli
Duree : 3 h  |   Niveau : Avance  |   Outils : Un banc de mesure de latence, une fenêtre de 40 millisecondes, et deux appels
de service de durées contrôlées
Construire une chaîne audio à budget contraint et définir la conduite à tenir quand le budget est dépassé.
Deroulement
1. Mesurer la latence de l'appel le plus court et du plus long, et en déduire la taille minimale de tampon.
2. Écrire la politique de repli pour trois cas : latence nominale, latence élevée, indisponibilité du service.
3. Vérifier que la politique de repli ne produit pas de décrochage audible, en mesurant le nombre de
décrochages par minute.
4. Proposer un indicateur de surveillance du taux de dépassement de budget, et préciser sa fenêtre de
calcul.
5. Écrire en trois lignes ce qui se passe si la latence du service double, et si le repli doit alors changer.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
17
Bareme indicatif
Critere
Points
La taille de tampon est justifiée par une mesure, pas par une convention
4
Les trois cas de repli sont définis et différenciés
3
L'indicateur de dépassement est spécifié
3
A retenir
• Une source synthétique est mobile sans coût, car la position recalcule les trois signaux physique.
• La différence de phase n'est exploitable qu'en dessous d'environ 1 500 hertz.
• Le budget de 40 millisecondes interdit tout appel distant dans le chemin de restitution.
• Un décrochage audible n'est pas un défaut de qualité sonore, mais un défaut de conception du tampon.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
18
Abréviations, notation et ressources de consultation
Annexes
Annexes
Ce cours se termine par deux annexes de référence. La première donne la signification de chaque sigle
employé, sous les deux formes — sigle et développé — car la litterature emploie indifféremment l'une
ou l'autre. La seconde donne la signification de chaque symbole mathématique : elle permet de relire
une démonstration sans revenir au chapitre dont elle est extraite, et de vérifier qu'un même symbole
garde le même sens d'un chapitre à l'autre.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
19
Chapitre A.1
Liste des abréviations
Les sigles ci-dessous sont ceux que le cours emploie. Chacun est donné avec sa forme développée
et le sens précis qu'il prend ici, qui n'est pas toujours celui qu'on lui donne ailleurs.
Un sigle employé sans être développé oblige le lecteur à le reconnaître au passage, ou à l'abandonner. Le
tableau ci-dessous ferme la liste de ceux que le cours emploie : il est exhaustif pour ce document, et non
pour la discipline.
Sigle
Forme développée
Sens dans ce cours
ASR
Automatic Speech Recognition
Reconnaissance automatique de la parole, qui transcrit un signal sonore.
GAN
Generative Adversarial Network
Réseau 
antagoniste 
génératif, 
où 
un 
générateur 
affronte 
un
discriminateur.
GRU
Gated Recurrent Unit
Cellule récurrente à portes, plus légère que le LSTM.
Mel
Échelle mel
Échelle de perception auditive, qui espace les fréquences selon le jugement
de l'oreille.
MFCC
Mel-Frequency Cepstral Coefficients
Coefficients cepstraux calculés sur une échelle mel.
MMSE
Minimum Mean Square Error
Estimation spectrale de puissance spectrale qui minimise l'erreur moyenne
quadratique.
MOS
Mean Opinion Score
Note moyenne d'une écoute subjective, sur une échelle de 1 à 5.
RMSE
Root Mean Square Error
Erreur quadratique moyenne, ramenée à l'échelle des valeurs prédites.
SNR
Signal-to-Noise Ratio
Rapport signal sur bruit, mesuré en décibels.
STFT
Short-Time Fourier Transform
Transformation de Fourier à fenêtre courte, qui donne le spectrogramme.
TTS
Text-to-Speech
Synthèse de la parole à partir du texte.
VITS
Variational Inference with adversarial
learning
Synthèse vocale de bout en bout, à inférence variationnelle.
VQ
Vector Quantization
Quantification vectorielle, qui remplace un signal par un indice de code.
Tableau 1 — Abréviations employées dans le cours
Chapitre A.2
Table de notation
Les symboles ci-dessous gardent le même sens d'un chapitre à l'autre. Lorsqu'un chapitre doit
réemployer un symbole pour un autre objet, il le redéclare sur la page même.
La notation est celle du cours : vecteurs en gras, matrices en majuscules grasses, scalaires en italique. Les
espérances sont notées E, les lois de données D, les espaces de paramètres Θ.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
20
Symbole
Signification
S(t)
Signal temporel, fonction du temps t.
f
Fréquence, en hertz.
fs
Fréquence d'échantillonnage, en hertz.
N
Nombre d'échantillons d'une trame.
L
Longueur de la fenêtre d'analyse, en échantillons.
H
Pas de décalage entre deux trames, en échantillons.
X[k]
Coefficient de la transformée de Fourier à court terme à la fréquence k.
|X[k]|
Module du spectrogramme, qui donne l'énergie.
S[k]
Densité de puissance spectrale estimée.
m
Indice de bande mel.
c
Indice de cepstre.
Cj
Coefficient cepstral d'indice j.
f0(t)
Fréquence fondamentale, c'est-à-dire hauteur perçue.
Ggen
Générateur, qui produit le signal synthétisé.
Gdisc
Discriminateur, qui juge le signal reçu.
Lgan
Perte antagoniste, minimisée par le générateur et maximisée par le discriminateur.
fc
Fréquence de la porteuse, en hertz.
Tableau 1 — Symboles mathématiques et leur signification
Convention
Toute divergence constatée entre cette table et un chapitre signale une erreur de transcription, non une
définition nouvelle : la table fait foi.
A retenir
• Un sigle employé sans être listé ici est un oubli de l'auteur, non une définition nouvelle.
• Un symbole qui change de sens d'un chapitre à l'autre rend toute démonstration ininterprétable : c'est la
principale cause des contresens que nous avons relevés.
• Ces deux tables sont les seules parties du cours à maintenir à la main : le reste se relit tout seul.
Index des figures et des tableaux
Référence rapide du matériel visuel
Figures
1.  De la description textuelle à l'audio : la chaîne de génération
1.  Le filigrane sonore : rendre l'origine détectable
1.  Audio spatial : la scène écoutée, pas seulement entendue
2.  Le temps réel audio : trois budgets qui ne se concertent pas
Tableaux
1.  Les cinq étapes et ce qui peut y échouer
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
21
1.  Les quatre mécanismes qui maintiennent la cohérence
1.  Ce que le filigrane garantit et ce qu'il ne garantit pas
1.  Codec à formule et codec appris : la comparaison honnête
1.  Le partitionnement du budget de 40 millisecondes
1.  Abréviations employées dans le cours
1.  Symboles mathématiques et leur signification
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
22
Fin du document
Intelligence Artificielle Avancée & Federated Learning — Fondations mathématiques de
l'apprentissage automatique, algorithmes fédérés, protection de la vie privée, défense contre les attaques,
grands modèles de langage fédérés, systèmes embarqués, renforcement appris, applications critiques
(santé, V2X), plateforme de référence FedX et feuille de route de recherche.<br/>Ghiloufi Jamel,
Architecte Logiciel Principal — Pixel Software Design<br/>Département de Recherche & Développement
— Recherche<br/>Pixel Software Design — Édition 2026
© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou
diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans
autorisation écrite préalable de l'auteur.
Document généré automatiquement le 29/09/2026 — mise en page Pixel Software Design.
"""


IA_3D_TEXT = r"""Pixel Software Design — Département de Recherche & Développement
PIXEL SOFTWARE DESIGN
Département de Recherche & Développement
Intelligence Artificielle
Avancée
& Federated Learning
•  Fondations de l'intelligence artificielle
•  Algorithmes d'apprentissage fédéré
•  Confidentialité, attaques et défenses
•  Applications et grands modèles fédérés
•  Framework FedX de référence
•  Nouveaux fronts de recherche
•  Travaux pratiques, projets et évaluation
Auteur
Ghiloufi Jamel
Fonction
Architecte Logiciel Principal
Direction
Département de Recherche & Développement
Service
R&D - Intelligence Artificielle Avancée & Apprentissage Fédéré
Niveau
Recherche
Édition
Édition 2026 — 1.0
Copyright
© Pixel Software Design
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou
diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans
autorisation écrite préalable de l'auteur.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
2
Copyright et mentions légales
Éditeur
Pixel Software Design
Auteur
Ghiloufi Jamel
Fonction
Architecte Logiciel Principal
Département
Département de Recherche & Développement
Intitulé
Intelligence Artificielle Avancée & Federated Learning
Sous-titre
Fondations mathématiques de l'apprentissage automatique, algorithmes fédérés,
protection de la vie privée, défense contre les attaques, grands modèles de langage
fédérés, systèmes embarqués, renforcement appris, applications critiques (santé,
V2X), plateforme de référence FedX et feuille de route de recherche.
Édition
Édition 2026 (version 1.0)
Langue
Français
Niveau
Recherche
Collection
Supports de formation et de recherche, Pixel Software Design
Droits d'auteur
© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation
ou diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite
sans autorisation écrite préalable de l'auteur.
Droits de l'auteur. Ghiloufi Jamel est l'auteur unique de l'ensemble du contenu scientifique, pédagogique et
technique de cet ouvrage. Toute adaptation, traduction, reproduction ou exploitation, y compris partielle, requiert
une autorisation écrite préalable.
Droits des tiers. Les algorithmes, modèles et travaux cités restent la propriété de leurs auteurs respectifs. Les
références employées figurent en fin d'ouvrage, ce qui permet de remonter au travail original pour toute
affirmation chiffrée.
Marques et licences externes. PyTorch, TensorFlow, Flower, Opacus, MONAI, scikit-learn et PySyft sont des
logiciels libres sous licences respectives (BSD, Apache 2.0, MIT). Leur usage dans ce document est purement
pédagogique et n'emporte aucune prescription commerciale.
Mentions relatives aux données et aux expérimentations
Document pédagogique à usage de formation interne. Les exemples de code fournis sont livrés à titre pédagogique
; les résultats numériques illustrés sont issus d'expérimentations conduites dans un cadre de recherche et ne
constituent pas des performances de production.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
3
Ce support synthétise les travaux de recherche du Département de Recherche & Développement de Pixel Software
Design sur l'intelligence artificielle distribuée, l'apprentissage fédéré, la protection de la vie privée et les systèmes
embarqués intelligents.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
4
Sommaire
Structure détaillée du cours
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 8
Partie 1 — IA et Trois Dimensions
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 9
1.1 L'écosystème des modèles de génération 3D
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 10
1.2 La chaîne de production, de l'image au maillage
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 11
1.3 Les infrastructures d'inférence
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 13
1.4 Cinématique inverse et apprentissage
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 15
1.5 Estimation de pose et capture de mouvement
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 16
1.6 Apprentissage par renforcement et physique différentiable
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 20
Annexes
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 21
A.1 Liste des abréviations
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 21
A.2 Table de notation
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
5
Partie
Thème
Contenu
Compétence visée
Durée
Partie 1
Fondations
Statistique, optimisation, courbes d'apprentissage
Comprendre et formaliser
2-3 semaines
Partie 2
Algorithmes FL
FedAvg, convergence, hétérogénéité, système
Implémenter et régler
3-4 semaines
Partie 3
Confidentialité
DP, attaques, défenses, agrégation sécurisée
Auditer et sécuriser
2-3 semaines
Partie 4
Applications
FedLLM, santé, V2X, FedRL, TinyML, graphes
Transposer à un domaine
3-4 semaines
Partie 5
Framework FedX
Architecture, API, benchmarks, exploitation
Industrialiser
2 semaines
Partie 6
Nouveaux fronts
FedCL, FedCI, SNN, FedGL, feuille de route
Ouvrir la recherche
2 semaines
Partie 7
TP et projets
9 labs, 5 projets, corrigés, évaluation
Faire et rendre
4-6 semaines
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
6
Préface
Comment utiliser ce cours
Ce support est conçu pour un parcours de formation et de recherche couvrant l'ensemble de la chaîne de valeur de
l'intelligence artificielle distribuée : les fondations mathématiques, les algorithmes d'apprentissage fédéré, les
menaces et défenses, les applications de pointe, une plateforme de référence opérationnelle, et enfin les nouveaux
fronts ouverts par la recherche du Département.
Ce n'est pas un manuel de référence à lire d'un trait : c'est un manuel opératoire. Chaque chapitre alterne
exposition, formalisation, mise en œuvre numérique et évaluation. Les listings sont complets et exécutables ; les
tableaux comparatifs servent de grille de décision ; les schémas d'architecture servent de support de revue de
conception.
Public et prérequis
Le contenu s'adresse à des étudiants de master et de doctorat, à des ingénieurs IA et à des praticiens de la
recherche appliquée. Les prérequis sont la connaissance de l'apprentissage automatique classique, de
l'algorithmique numérique et des bases de probabilités. Les parties 1 à 3 sont auto-suffisantes pour un étudiant qui
découvre le domaine ; les parties 4 à 7 supposent la mécanique et les outils présentés dans la partie 2.
Conventions de lecture. Une expression mathématique est encadrée par deux signes dollars ; un identifiant, un
fichier ou une commande est écrit en caractères à chasse fixe ; les encadrés Définition, Théorème, Méthode et
Attention signalent les points à maîtriser et les pièges fréquents. Les renvois de la forme « voir chapitre 3.2 »
désignent le second chapitre de la troisième partie.
Progression pédagogique
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
7
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
8
Génération, reconstruction, cinématique et mouvement
Partie 1
IA et Trois Dimensions
La représentation tridimensionnelle est le support de la réalité virtuelle, de la simulation industrielle,
de la robotique et de l'animation. Pendant des décennies, la production d'un actif trois dimensions
était réservée à des dizaines de milliers d'heures de travail manuel. L'apprentissage automatique a
rendu la génération accessible en quelques secondes, et a ouvert un problème nouveau : celui de
l'infrastructure, du choix de représentation et de l'intégration. Ce cours décrit les outils et surtout la
méthode de sélection, car la plupart des échecs d'intégration ne viennent pas du modèle mais du
mauvais choix de point d'entrée.
Objectifs de la partie
• Comparer les principaux modèles de génération 3D sur le critère qui compte : la contrainte la plus dure de
votre usage.
• Décrire la chaîne complète, de l'image d'entrée à l'export de maillage exploitable, et nommer l'étape qui coûte
le plus cher.
• Choisir entre un agrégateur de modèles, une inférence par interface, un service empaqueté et une
orchestration locale.
• Expliquer pourquoi un réseau de neurones accélère la cinématique inverse sans la remplacer.
• Distinguer capture monoculaire, stéréoscopique et volumétrique, et leurs contraintes de contrat.
• Expliquer ce qu'un simulateur d'apprentissage par renforcement peut et ne peut pas transférer au monde réel.
Plan de la partie
1.  L'écosystème des modèles de génération 3D
2.  La chaîne de production, de l'image au maillage
3.  Les infrastructures d'inférence
4.  Cinématique inverse et apprentissage
5.  Estimation de pose et capture de mouvement
6.  Apprentissage par renforcement et physique différentiable
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
9
Chapitre 1.1
L'écosystème des modèles de génération 3D
Les modèles se distinguent moins par la qualité de leurs images de synthèse que par le point où ils
échouent.
Une carte graphique sérieuse exécute désormais la reconstruction d'un objet en quelques secondes. La
différence entre les modèles disponibles n'est donc plus une question de faisabilité, mais de domaine de
validité : chacun réussit excellemment dans une zone et échoue nettement à sa frontière, et c'est toujours
cette frontière qui décide de l'utilité réelle.
Figure 1 — Les modèles de génération 3D et ce que chacun optimise
Famille
Principe
Atout
Limite principale
Diffusion de vue
génère 
des 
vues 
multiples
cohérentesqualité visuelle élevée
lent, mémoire importante
Champ de densité
prédit un volume de probabilité de
surface
très rapide, topologie correcte
tops trouées, textures floues
Surface implicite
extrait l'isosurface d'un champ scalaire
maillage 
étanche, 
topologie
fiable
extraction coûteuse
Graphe de scène
prédit directement un graphe de faces
maillage 
natif, 
pas 
de
conversion
mémoire très élevée, résolution
plafonnée
Champ de radiance
rend une scène par lancer de rayons
rendu photoréaliste excellent
ne produit pas de géométrie
exploitable
Tableau 1 — Les familles de modèles et leurs compromis
La dernière ligne est la plus coûteuse à découvrir tard. Un système de rendu à lancer de rayons produit des images
remarquables, et ne fournit aucun actif utilisable dans un moteur de jeu ou une chaîne de fabrication.
Choisir un modèle en cinq questions, dans cet ordre
• Quel est l'usage en aval ? Affichage, impression, animation, mesure, ou simulation. L'usage détermine la
représentation exigée, donc tout le reste.
2. Quelle est la contrainte la plus dure ? Latence, mémoire vidéo, précision géométrique, ou fidélité des
matières. On choisit sur la contrainte, pas sur la démonstration.
3. Quelle diversité d'objets ? Un modèle excellent sur un domaine étroit et médiocre ailleurs impose de
connaître son domaine avant de l'adopter.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
10
4. Quel est le coût d'une erreur ? Une erreur visuelle se corrigé à la retouche ; une erreur géométrique se
propage jusqu'à la pièce fabriquée.
5. Les sorties sont-elles exploitables ? Format, topologie, carte de texture, système de coordonnées. Un
modèle dont la sortie exige un post-traitement lourd a un coût caché souvent supérieur à son coût d'exécution.
La qualité d'image n'est pas la qualité de l'actif
Un modèle peut produire un rendu<Integer> superbe et un maillage inutilisable : faces non orientées, normales
incohérentes, trous dans les zones occultées, coordonnées de texture absentes. L'évaluation d'un modèle de
reconstruction doit donc porter sur l'actif exporté et non sur l'image produite. Les métriques habituelles de
comparaison visuelle ne mesurent ni les erreurs d'orientation des faces, ni les défauts de couture, ni la topologie.
Astuce
Le seul test qui vaille est de prendre dix objets de votre domaine réel, les passer dans le modèle, et mesurer le
temps de correction manuelle. Ce chiffre décidera du choix mieux que toute comparaison publiée.
A retenir
• Les modèles 3D se distinguent par leur domaine de validité, pas par leur qualité moyenne.
• Le rendu spectacular et l'actif exploitable sont deux propriétés distinctes, et la seconde décide de l'utilité.
• L'évaluation porte sur le maillage exporté, jamais sur l'image de synthèse.
• Le critère de sélection est la contrainte la plus dure de votre usage.
Chapitre 1.2
La chaîne de production, de l'image au
maillage
L'inférence n'est qu'une étape. Les deux autres étapes coûtent souvent plus cher qu'elle.
Figure 1 — De l'image au maillage exploitable : la chaîne complète
Une chaîne de reconstruction comporte toujours les mêmes étapes, que le modèle en porte le nom ou non :
acquisition, estimation de la géométrie, reconstruction, post-traitement, et habillage. Chacune peut échouer
silencieusement, et les erreurs se propagent d'étape en étape : une profondeur estimée faux produit un
maillage mal orienté, qu'aucun post-traitement ne rattrapera.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
11
M = ≤ft( V, F, N, U, Mat ), Mat ∈ ≤ft diffuse, rugueuse, métallique, transmission n3(M.1)
Un actif exploitable est un tuple : sommets, faces, normales, coordonnées de texture et paramètres de matériau.
Les modèles récents fournissent les trois premiers ; les deux derniers restent très souvent à produire, et c'est
précisément ce travail manuel qui rend le résultat présentable.
• Nettoyage de topologie : suppression des faces isolées, suppression des composantes non connectées, et
consolidation des sommets dupliqués. Rapide, et souvent négligé.
• Décimation : réduction du nombre de faces en préservant la silhouette. C'est l'opération qui décide du
budget réel, car c'est elle qui détermine la fluidité à l'affichage.
• Projection des coordonnées de texture : choix de la paramétrisation. Les méthodes par développement
et par projection sphérique ont des coutures ; les méthodes basées sur le diagramme de Beatrice sont
plusrobustes mais plus lentes.
• Habillage : projection de la texture générée sur le maillage précédent, puis estimation de paramètres de
matériau pour rendre correctement sous un éclairage physique.
• Validation géométrique : auto-intersection, orientation des normales, manifoldness, épaisseur
minimale. C'est cette étape qui sépare un actif affichable d'un actif dommageable dans une chaîne de
fabrication.
Contrôle qualité d'un actif reconstruit, en sept points
• Manifoldness : chaque arête doit appartenir à exactement deux faces.
2. Orientation : les normales doivent pointer vers l'extérieur, sans exception ni incohérence.
3. Auto-intersection : le maillage ne doit pas se traverser lui-même à l'échelle d'usage.
4. Trous et composantes : aucune face isolée, aucune composante détachée non intentionnelle.
5. Coutures : la paramétrisation ne doit pas produire de rupture visible dans les zones vues.
6. Densité : le nombre de faces doit correspondre au budget d'affichage cible, pas au maximum possible.
7. Échelle et repère : dimensions réelles, origine au bon endroit, axes cohérents avec le moteur en aval.
Les quatre premiers points peuvent être vérifiés automatiquement et doivent l'être : ils ne dépendent pas de l'œil
et leur oubli se paie très tard.
Un maillage dont les normales ne sont pas cohérentes peut s'afficher correctement dans un moteur qui
recalcule les normales, et produire des ombres fausses dans un moteur qui ne le fait pas. Le symptôme
apparaît alors dans un autre outil, sur une autre machine, chez un autre prestataire. Vérifier et corriger
l'orientation une seule fois, à la production, coûte une heure ; le retrouver en production coûte un cycle
complet d'intégration.
Le maillage orientations incohérentes
A retenir
• La chaîne comporte cinq étapes, et le modèle n'en porte qu'une seule.
• Les erreurs de profondeur se propagent jusqu'à la texture et ne sont rattrapables par aucun post-traitement.
• Un actif exploitable inclut normales et matériaux, pas seulement sommets et faces.
• La validation géométrique doit être automatisée, car ses premiers points ne dépendent pas de l'œil.
Chapitre 1.3
Les infrastructures d'inférence
La question d'infrastructure se tranche sur une seule donnée : la donnée a-t-elle le droit de sortir ?
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
12
Figure 1 — Quatre familles d'infrastructures, quatre compromis
Famille
Ce que vous gérez
Facturation
LatenceContrôle de la
version
Agrégateur de modèles
rienpar génération, souvent au
jeton
moyenne à élevée
imposé 
par 
le
fournisseur
Inférence par interface
rien
à la seconde de calcul, ou par
volume
variable 
selon 
la
charge
figée à l'appel
Service empaqueté
la 
conteneurisation 
et 
la
compilation
à votre infrastructure
maîtrisée
maîtrisé
Orchestration locale
le 
matériel 
et 
le 
graphe
d'exécution
à votre infrastructure
maîtrisée
maîtrisé
Tableau 1 — Les quatre familles en détail
Le contrôle de la version est la colonne la plus négligée et la plus structurante. Un fournisseur d'inférence peut remplacer
un modèle entre deux appels : votre résultat devient non reproductible sans que rien n'ait changé dans votre code.
Trancher l'infrastructure en quatre questions
• La donnée peut-elle quitter l'entreprise ? Si non, deux options subsistent : service empaqueté ou
orchestration locale. Cette question se pose avant toute autre.
2. Quelle part de la charge est expérimentale ? Si la majorité des requêtes sont des essais, l'inférence par
interface évite tout investissement et se remplace sans/kubernetes.
3. Quelle latence faut-il garantir ? Une latence maximale engage à un service maîtrisé, car un fournisseur
distant n'offre aucun engagement contractuel sur le centime de milliseconde.
4. Faut-il pouvoir reproduire un résultat dans six mois ? Si oui, le modèle doit être archivé localement avec
son empreinte, quelle que soit l'inférence choisie.
Un usage réel combine les deux : interface pour l'exploration, service maîtrisé pour la production, et toujours
une copie locale du modèle archivé.
Le coût caché n'est pas l'inférence
Sur une génération de quelques secondes, le coût d'inférence est négligeable devant trois autres postes : la file
d'attente avant la première image, la correction manuelle des actifs produits, et le stockage des versions
intermédiaires. Une équipe qui compare deux fournisseurs sur le prix à la génération optimise le poste le moins
coûteux de la chaîne. Le bon indicateur de comparaison est le coût total par actif livré et validé.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
13
Astuce
Archivez toujours le modèle avec son empreinte et sa version de format. Un résultat obtenu avec une référence
de modèle mouvante n'est pas reproductible, quelle que soit la qualité de l'infrastructure qui l'a produit. Ce
conseil vaut pour tout système d'inférence, et il est systématiquement ignoré.
A retenir
• La contrainte qui décide de tout est le droit de sortie de la donnée.
• Le contrôle de la version du modèle détermine la reproductibilité, et se négocie rarement.
• Comparer deux fournisseurs sur le prix à la génération optimise le poste le moins coûteux.
• Le bon indicateur est le coût total par actif livré et validé.
Chapitre 1.4
Cinématique inverse et apprentissage
L'apprentissage n'accélère pas la cinématique inverse : il en apprend l'initialisation.
Figure 1 — Cinématique inverse : de la position cible aux angles
minboldsymbolθ ≤ft| mathbfp(boldsymbolθ) - mathbfp* |2 + λ ≤ft| boldsymbolθ -
boldsymbolθ0 |2
(M.2)
Deux termes, deux rôles : le premier atteint la cible, le second empêche une solution aberrante. Sans le terme de
régularisation, une chaîne à six degrés de liberté atteint n'importe quelle position de nombreuses manières,
dont certaineserinversent le bras. Le choix du pondérateur est donc un choix de posture, pas un réglage
numérique.
Famille
Sens de propagation
Coût
Échec typique
Descendante
de l'épaule vers la main
constant, 
faibleposition
d'épaule 
hors 
de 
l'espace
atteignable
Ascendante
de la main vers l'épaule
constant, faible
précision dépendante de la configuration
de départ
Descendante itérative
correction par Jacobien
proportionnel aux itérations
mauvaise 
configuration 
initiale,
singularité
Descente de gradient
correction par dérivée
proportionnel aux itérations
optimum local
Apprentissage
proposition d'une initialisation
quasi nul
hors de la distribution d'entraînement
Tableau 1 — Les trois familles de résolution et leurs propriétés
La dernière ligne est la seule qui soit nouvelle. Le réseau ne résout rien : il fournit un point de départ si bon que deux ou
trois itérations suffisent, contre vingt ou trente.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
14
1import numpy as np
2
3
4def cinematique_descendante(pointeur_cible: np.ndarray, longueurs: list[float],
5angle_initial: float = 0.0) -> np.ndarray:
6''"Propagation descendante, en dynamique inverse ou geometrique.
7
8On fixe l'angle de l'epaule, puis on enchaîne les positions. Si la
9cible n'est pas atteinte, on ajuste l'angle d'epaule par un balayage
10grossier puis par affinage : c'est ce second passage qui transforme
11une methode qui "ne converge pas toujours" en methode qui converge.
12''"
13nb = len(longueurs)
14angles = np.full(nb, angle_initial)
15
16def evaluer(theta: np.ndarray) -> float:
17position = np.zeros(2)
18direction = theta[0]
19for i in range(nb - 1):
20position = position + longueurs[i] * np.array(
21[np.cos(direction), np.sin(direction)])
22direction += theta[i + 1]
23position = position + longueurs[-1] * np.array(
24[np.cos(direction), np.sin(direction)])
25return float(np.linalg.norm(position - pointeur_cible))
26
27# balayage grossier, puis affinage par dichotomie sur chaque angle
28grille = np.linspace(-np.pi, np.pi, 25)
29for _ in range(3):
30for i in range(nb):
31meilleur, meilleur_cout = angles[i], evaluer(angles)
32for candidat in grille:
33essai = angles.copy()
34essai[i] = candidat
35cout = evaluer(essai)
36if cout < meilleur_cout:
37meilleur, meilleur_cout = candidat, cout
38angles[i] = meilleur
39return angles
40
41
42def resoudre_reseau(proposeur, cible: np.ndarray, affiner: int = 3) -> np.ndarray:
43''"Apprentissage propose, methode iterative affine.
44
45Le reseau fournit une initialisation en une passe. On garde la
46methode iterative pour l'affinage, parce qu'elle garantit l'optimalite
47locale : le reseau garantit la rapidite, pas l'exactitude.
48''"
49theta = proposeur(cible)
50for _ in range(affiner):
51ecart = cible - forward(theta)
52jacobienne = forward_jacobienne(theta)
53theta = theta + np.linalg.solve(jacobienne.T @ jacobienne,
54jacobienne.T @ ecart)
55return theta
Listing 1 — Résolution de cinématique inverse : géométrique et apprentissage
Entraîner un proposeur de pose : les quatre règles
• Générer les poses par tirage aléatoire uniforme sur l'espace des articulations, et non en simulant un
mouvement réaliste. Le modèle doit couvrir tout l'espace atteignable, y compris les postures qu'aucun être
humain ne prendrait pas.
2. Filtrer par accessibilité : ne garder que les poses dont l'atteinte de la cible est possible avec la longueur du
bras réelle, sous la contrainte d'évitement d'obstacle.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
15
3. Entraîner par régression sur la pose de la cible, pas sur les angles. La cible est l'entrée du service ; les
angles sont une paramétrisation interne. Entraîner sur les angles apprend au modèle un repère arbitraire.
4. Ajouter une composante de gestion des ambiguïtés. Quand deux postures atteignent la même cible, la loss
doit les considérer toutes deux correctes, sinon le modèle choisit arbitrairement et bascule d'une solution à
l'autre d'une image à l'autre.
Un réseau qui prédit directement les angles articulaires sans aucune vérification donne des poses qu'il n'a
jamais apprises, et rien ne le signale. La parade est simple et jamais optionnelle : conserver la résolution
itérative en raffinement, et ajouter une vérification explicite que la position atteinte est bien celle
demandée, à une tolérance près. Un modèle rapide mais non vérifié est une source de défauts
intermittents, c'est-à-dire la pire catégorie de défaut possible.
L'abandon de l'itératif au profit du réseau
A retenir
• L'apprentissage ne remplace pas la résolution itérative : il en fournit l'initialisation.
• Le terme de régularisation dans la fonction de coût choisit une posture, pas un réglage.
• Entraîner sur les angles apprend au modèle un repère arbitraire : il faut entraîner sur la cible.
• Une résolution non vérifiée produit des défauts intermittents, la plus mauvaise catégorie possible.
Chapitre 1.5
Estimation de pose et capture de mouvement
La difficulté de la capture de mouvement n'est pas de voir un squelette : c'est d'en déduire une
position absolue.
Figure 1 — De la vidéo à la pose : les trois états du problème
Un réseau de détection de squelette sur image est devenu un problème résolu : la question de savoir où se
trouve un coude dans une image n'a plus d'intérêt. Le problème ouvert commence après : une image ne
contient qu'une projection, et une projection ne détermine pas une position. C'est cette ambiguïté, et non la
détection, qui sépare un système de démonstration d'un système exploitable.
π : ℝ3 → ℝ2, ∃ (x1, x2) ≠ (x1', x2') : π(x1) = π(x2')
hatboldsymbolβ = argminboldsymbolβ ≤ft| π ( T, boldsymbolβ ) - mathbfJ2D |2
W + λ ≤ft|
boldsymbolβ - boldsymbolβprev |2
W
(M.3)
La première expression dit l'essentiel : la projection n'est pas injective, donc la position n'est pas déterminée. La
seconde est la résolution du problème par un modèle de corps paramétré, dont la contrainte de forme
transforme un problème mal posé en problème bien posé — au prix de restreindre l'ensemble des poses
possibles.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
16
Monoculaire
Stéréoscopique
Volumétrique
Entrées
une ou plusieurs caméras 2Ddeux
caméras calibrées
plusieurs vues calibrées
Profondeur
déterminée par le modèle de corps
déterminée par la géométrie
déterminée par la triangulation
Sortie
positions 3D absolues
positions 3D absolues
positions 3D absolues
Coût matériel
très faible
moyen, avec étalonnage
élevé, plusieurs caméras
Problème dominant
auto-occlusion,hors de champ
désynchronisation
faisabilité de l'installation
Usage typique
animation, ergonomie, guidage
capture de studio
analyse clinique, recherche
Tableau 1 — Trois états du problème, trois contrats
L'étalonnage est la pierre angulaire de la deuxième et de la troisième colonne, et il est presque toujours sous-estimé : une
caméra déplacée de deux centimètres introduit une erreur de profondeur qui invalide la reconstruction.
Préparer une installation de capture multi-vues
• Fixer le repère et le mesurer, pas l'estimer. Un repère posé à vue d'œil rendra toutes les mesures ultérieures
interprétables de travers.
2. Étalonner chaque paire de caméras séparément, avec une cible plane et une méthode d'estimation
documentée. Enregistrer les paramètres : ils seront nécessaires à tout recalcul.
3. Vérifier la précision résiduelle sur une position connue, et la mesurer. Une incertitude de deux centimètres
invalide toute mesure articulaire fine.
4. Synchroniser les flux. Une gigue temporelle de dix millisecondes entre deux caméras produit un bruit
articulaire d'un centimètre : l'origine n'est pas dans le modèle.
5. Prévoir la maintenance, car une caméra déplacée reste silencieusement fausse jusqu'au réétalonnage.
L'étape 5 est celle qu'on oublié, et la seule dont l'omission produise une corruption lente et progressive des
résultats.
Astuce
Pour un guidage de robot par imitation, l'étape de lissage temporel vaut autant que la qualité du modèle de
détection. Un filtre qui réduit la gigue de mesure dégrade aussi la réactivité : le compromis doit être réglé sur la
vitesse de mouvement réelle, pas choisi par défaut.
A retenir
• La détection d'un squelette sur image est résolue ; la reconstruction de la position ne l'est pas.
• La projection d'un point trois dimensions sur une image n'est pas injective, donc la position est ambiguë.
• Un modèle de corps paramétré rend le problème bien posé au prix d'une restriction des poses.
• L'étalonnage, pas le modèle, est la source dominante d'erreur en capture multi-vues.
Chapitre 1.6
Apprentissage par renforcement et physique
différentiable
Le simulateur apprend, mais il apprend dans un monde qui n'est pas le nôtre. Tout l'art est dans
l'écart.
Faire apprendre à un robot à marcher par essai-erreur est impossible en conditions réelles : les chutes
détruisent le robot, et le nombre d'essais requis dépasse largement ce que l'on peut solder. L'apprentissage
par renforcement déplace donc l'expérimentation dans un simulateur, où des millions de trajectoires sont
produites sans coût. Le problème n'est pas résolu : il est déplacé, et le déplacement crée un écart qu'il faut
mesurer.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
17
Figure 1 — Trois sources d'écart entre le simulateur et le réel
Figure 2 — Physique différentiable : deux prédictions, une somme
boldsymbolθ* = argmaxboldsymbolθ E≤ft[ ∑t=0
T γt r(st, at) ], écart Δ(s) = ≤ft| s1 - s0 |
(M.4)
Les deux expressions doivent être lues ensemble. La première produit une politique optimale dans le
simulateur. La seconde mesure ce qui manque pour qu'elle soit optimale ailleurs. Toute la difficulté du domaine
tient dans l'estimation de cette différence, et aucune des deux ne se dispensé de l'autre.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
18
Source
Mécanisme
Symptôme observé
Parade
Modèle physique faux
les coefficients sont approximatifsle
robot chute systématiquement au
même mouvement
identifier le coefficient fautif par essai
ciblé
Non-observabilité
le simulateur expose des états que le
capteur ne mesure pas
comportement correct en simulation,
impossible à réaliser
bruiter l'état pour forcer la robustesse
à l'incertitude
Différence de latence
le contrôle réel réagit avec retard
oscillation 
ou 
instabilité 
sur 
les
mouvements rapides
introduire un retard variable dans le
simulateur
Tableau 1 — Trois sources d'écart entre le simulateur et le réel
La deuxième source est la plus sous-estimée. Un agent qui s'appuie sur un état parfait apprend une politique qui exige cet
état parfait, et qui s'effondre dès qu'il est partiellement bruité.
Le simulateur qui ment avec précision
Un simulateur précise mais faux est plus dangereux qu'un simulateur approximatif mais honnête, parce qu'il
produit des résultats qui semblent fiables. La parade n'est pas d'augmenter la fidélité du modèle physique, mais
de rendre l'écart explicite : mesurer l'erreur de prédiction du simulateur sur des trajectoires réelles, et la publier
à côté des gains obtenus. Un simulateur dont l'erreur mesurée est stable et comprise devient un instrument ; un
simulateur dont l'erreur est inconnue reste une hypothèse.
Physique différentiable : rendre les lois apprenables
• Principe : le moteur de simulation est instrumenté pour dériver, et un réseau de neurones corrigé en
sortie la prévision physique. Le moteur fournit la structure et la stabilité, le réseau apprend la part qui
échappe au modèle.
• Gain attendu : des simulations de systèmes autrement trop coûteuses — tissus, fluides, contacts
multiples — deviennent interactives, donc utilisables pour de l'optimisation.
• Limite : la stabilité. Un moteur différentiable peut être X peu fiable à laanj, et une optimisation qui
diverge coûte bien plus qu'une simulation exacte.
• Usage correct : pré-analyse, criblage de scénarios, apprentissage de contrôles. Usage incorrect :
validation d'un résultat critique, où seule la physique non modifiée fait foi.
Travaux pratiques 1.1 — Transférer une politique apprise vers un cadre
incertain
Duree : 3 h  |   Niveau : Avance  |   Outils : Un simulateur de contrôle plan à deux degrés de liberté, et une politique
entraîné par apprentissage par renforcement
Entraîner une politique de contrôle simple dans un simulateur, puis mesurer l'effet du bruit d'observation
sur ses performances.
Deroulement
1. Entraîner la politique dans le simulateur sans bruit, et relever le coût final atteint.
2. Réentraîner la même politique avec un bruit gaussien sur l'observation, et relever le coût final.
3. Comparer les deux courbes d'apprentissage, et identifier la phase pendant laquelle le bruit change le
plus la dynamique.
4. Mesurer la dégradation des performances en fonction de l'écart-type du bruit, sur cinq valeurs
croissantes.
5. Écrire la conclusion en trois lignes : quelle source d'écart du tableau previous est illustrée, et si le bruit
d'état ou le bruit d'action la reproduit le mieux.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
19
Bareme indicatif
Critere
Points
Les deux entraînements sont menés avec la même graine et le même budget
3
La comparaison est chiffrée et non seulement qualitative
3
La source d'écart identifiée est justifiée par l'observation
4
A retenir
• L'apprentissage par reinforcement déplace l'expérimentation, il ne supprime pas le problème de l'échec.
• Trois sources d'écart séparent le simulateur du réel, et la non-observabilité est la plus sous-estimée.
• Bruiter l'état d'observation pendant l'entraînement est le moyen le plus efficace de fiabiliser le transfert.
• La physique différentiable sert à pré-analyser, pas à certifier.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
20
Abréviations, notation et ressources de consultation
Annexes
Annexes
Ce cours se termine par deux annexes de référence. La première donne la signification de chaque sigle
employé, sous les deux formes — sigle et développé — car la litterature emploie indifféremment l'une
ou l'autre. La seconde donne la signification de chaque symbole mathématique : elle permet de relire
une démonstration sans revenir au chapitre dont elle est extraite, et de vérifier qu'un même symbole
garde le même sens d'un chapitre à l'autre.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
21
Chapitre A.1
Liste des abréviations
Les sigles ci-dessous sont ceux que le cours emploie. Chacun est donné avec sa forme développée
et le sens précis qu'il prend ici, qui n'est pas toujours celui qu'on lui donne ailleurs.
Un sigle employé sans être développé oblige le lecteur à le reconnaître au passage, ou à l'abandonner. Le
tableau ci-dessous ferme la liste de ceux que le cours emploie : il est exhaustif pour ce document, et non
pour la discipline.
Sigle
Forme développée
Sens dans ce cours
CG
Computer Graphics
Infographie, c'est-à-dire synthèse d'images numériques.
CUDA
Compute Unified Device Architecture
Modèle de programmation des accélérateurs graphiques.
GLTF
GL Transmission Format
Format d'échange d'objets tridimensionnels.
LiDAR
Light Detection and Ranging
Mesure de distance par impulsion laser.
NeRF
Neural Radiance Field
Représentation neuronale d'une scène, par radiance et densité.
OBJ
Wavefront Object
Format de fichier d'objets tridimensionnels, sous forme texte.
PBR
Physically Based Rendering
Rendu fondé sur le principe physique de conservation de l'énergie.
PLY
Polygon File Format
Format de maillage tridimensionnel.
RGB-D
Red Green Blue and Depth
Acquisition d'une couleur et d'une profondeur synchronisées.
SLAM
Simultaneous Localization and Mapping
Localisation et cartographie simultanées d'un robot.
Tableau 1 — Abréviations employées dans le cours
Chapitre A.2
Table de notation
Les symboles ci-dessous gardent le même sens d'un chapitre à l'autre. Lorsqu'un chapitre doit
réemployer un symbole pour un autre objet, il le redéclare sur la page même.
La notation est celle du cours : vecteurs en gras, matrices en majuscules grasses, scalaires en italique. Les
espérances sont notées E, les lois de données D, les espaces de paramètres Θ.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
22
Symbole
Signification
P ∈ ℝ3
Point de l'espace, de coordonnées (x, y, z).
mathbfp
Vecteur de position, à trois coordonnées.
R ∈ SO(3)
Rotation, élément du groupe spécial orthogonal.
T ∈ SE(3)
Rigidification d'une rotation et d'une translation.
Π
Projection perspective d'un point de l'espace sur le plan image.
K
Matrice intrinsèque d'une caméra.
Text
Matrice extrinsèque, qui lie la caméra au repère du monde.
Xc
Coordonnées d'un point dans le repère de la caméra.
u, v
Coordonnées du pixel dans l'image.
M = (V, F)
Maillage : sommets et faces.
|V|
Nombre de sommets du maillage.
|F|
Nombre de faces du maillage.
d
Distance métrique entre deux points, ou entre deux images.
σ
Écart-type d'une grandeur.
χ2
Distance du chi-deux, pour l'ajustement d'un modèle.
Tableau 1 — Symboles mathématiques et leur signification
Convention
Toute divergence constatée entre cette table et un chapitre signale une erreur de transcription, non une
définition nouvelle : la table fait foi.
A retenir
• Un sigle employé sans être listé ici est un oubli de l'auteur, non une définition nouvelle.
• Un symbole qui change de sens d'un chapitre à l'autre rend toute démonstration ininterprétable : c'est la
principale cause des contresens que nous avons relevés.
• Ces deux tables sont les seules parties du cours à maintenir à la main : le reste se relit tout seul.
Index des figures et des tableaux
Référence rapide du matériel visuel
Figures
1.  Les modèles de génération 3D et ce que chacun optimise
1.  De l'image au maillage exploitable : la chaîne complète
1.  Quatre familles d'infrastructures, quatre compromis
1.  Cinématique inverse : de la position cible aux angles
1.  De la vidéo à la pose : les trois états du problème
1.  Trois sources d'écart entre le simulateur et le réel
2.  Physique différentiable : deux prédictions, une somme
Tableaux
1.  Les familles de modèles et leurs compromis
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
23
1.  Les quatre familles en détail
1.  Les trois familles de résolution et leurs propriétés
1.  Trois états du problème, trois contrats
1.  Trois sources d'écart entre le simulateur et le réel
1.  Abréviations employées dans le cours
1.  Symboles mathématiques et leur signification
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
24
Fin du document
Intelligence Artificielle Avancée & Federated Learning — Fondations mathématiques de
l'apprentissage automatique, algorithmes fédérés, protection de la vie privée, défense contre les attaques,
grands modèles de langage fédérés, systèmes embarqués, renforcement appris, applications critiques
(santé, V2X), plateforme de référence FedX et feuille de route de recherche.<br/>Ghiloufi Jamel,
Architecte Logiciel Principal — Pixel Software Design<br/>Département de Recherche & Développement
— Recherche<br/>Pixel Software Design — Édition 2026
© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou
diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans
autorisation écrite préalable de l'auteur.
Document généré automatiquement le 29/09/2026 — mise en page Pixel Software Design.
"""


IA_A_Z_TEXT = r"""Pixel Software Design — Département de Recherche & Développement
PIXEL SOFTWARE DESIGN
Département de Recherche & Développement
Intelligence Artificielle
Avancée
& Federated Learning
•  Fondations de l'intelligence artificielle
•  Algorithmes d'apprentissage fédéré
•  Confidentialité, attaques et défenses
•  Applications et grands modèles fédérés
•  Framework FedX de référence
•  Nouveaux fronts de recherche
•  Travaux pratiques, projets et évaluation
Auteur
Ghiloufi Jamel
Fonction
Architecte Logiciel Principal
Direction
Département de Recherche & Développement
Service
R&D - Intelligence Artificielle Avancée & Apprentissage Fédéré
Niveau
Recherche
Édition
Édition 2026 — 1.0
Copyright
© Pixel Software Design
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou
diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans
autorisation écrite préalable de l'auteur.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
2
Copyright et mentions légales
Éditeur
Pixel Software Design
Auteur
Ghiloufi Jamel
Fonction
Architecte Logiciel Principal
Département
Département de Recherche & Développement
Intitulé
Intelligence Artificielle Avancée & Federated Learning
Sous-titre
Fondations mathématiques de l'apprentissage automatique, algorithmes fédérés,
protection de la vie privée, défense contre les attaques, grands modèles de langage
fédérés, systèmes embarqués, renforcement appris, applications critiques (santé,
V2X), plateforme de référence FedX et feuille de route de recherche.
Édition
Édition 2026 (version 1.0)
Langue
Français
Niveau
Recherche
Collection
Supports de formation et de recherche, Pixel Software Design
Droits d'auteur
© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation
ou diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite
sans autorisation écrite préalable de l'auteur.
Droits de l'auteur. Ghiloufi Jamel est l'auteur unique de l'ensemble du contenu scientifique, pédagogique et
technique de cet ouvrage. Toute adaptation, traduction, reproduction ou exploitation, y compris partielle, requiert
une autorisation écrite préalable.
Droits des tiers. Les algorithmes, modèles et travaux cités restent la propriété de leurs auteurs respectifs. Les
références employées figurent en fin d'ouvrage, ce qui permet de remonter au travail original pour toute
affirmation chiffrée.
Marques et licences externes. PyTorch, TensorFlow, Flower, Opacus, MONAI, scikit-learn et PySyft sont des
logiciels libres sous licences respectives (BSD, Apache 2.0, MIT). Leur usage dans ce document est purement
pédagogique et n'emporte aucune prescription commerciale.
Mentions relatives aux données et aux expérimentations
Document pédagogique à usage de formation interne. Les exemples de code fournis sont livrés à titre pédagogique
; les résultats numériques illustrés sont issus d'expérimentations conduites dans un cadre de recherche et ne
constituent pas des performances de production.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
3
Ce support synthétise les travaux de recherche du Département de Recherche & Développement de Pixel Software
Design sur l'intelligence artificielle distribuée, l'apprentissage fédéré, la protection de la vie privée et les systèmes
embarqués intelligents.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
4
Sommaire
Structure détaillée du cours
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 8
Partie 1 — Intelligence artificielle de A à Z
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 9
1.1 Fondations et logique symbolique
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 11
1.2 Apprentissage automatique et profond
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 14
1.3 IA générative et modèles de langage
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 15
1.4 MLOps, éthique et responsabilité
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 20
Annexes
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 21
A.1 Liste des abréviations
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 21
A.2 Table de notation
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
5
Partie
Thème
Contenu
Compétence visée
Durée
Partie 1
Fondations
Statistique, optimisation, courbes d'apprentissage
Comprendre et formaliser
2-3 semaines
Partie 2
Algorithmes FL
FedAvg, convergence, hétérogénéité, système
Implémenter et régler
3-4 semaines
Partie 3
Confidentialité
DP, attaques, défenses, agrégation sécurisée
Auditer et sécuriser
2-3 semaines
Partie 4
Applications
FedLLM, santé, V2X, FedRL, TinyML, graphes
Transposer à un domaine
3-4 semaines
Partie 5
Framework FedX
Architecture, API, benchmarks, exploitation
Industrialiser
2 semaines
Partie 6
Nouveaux fronts
FedCL, FedCI, SNN, FedGL, feuille de route
Ouvrir la recherche
2 semaines
Partie 7
TP et projets
9 labs, 5 projets, corrigés, évaluation
Faire et rendre
4-6 semaines
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
6
Préface
Comment utiliser ce cours
Ce support est conçu pour un parcours de formation et de recherche couvrant l'ensemble de la chaîne de valeur de
l'intelligence artificielle distribuée : les fondations mathématiques, les algorithmes d'apprentissage fédéré, les
menaces et défenses, les applications de pointe, une plateforme de référence opérationnelle, et enfin les nouveaux
fronts ouverts par la recherche du Département.
Ce n'est pas un manuel de référence à lire d'un trait : c'est un manuel opératoire. Chaque chapitre alterne
exposition, formalisation, mise en œuvre numérique et évaluation. Les listings sont complets et exécutables ; les
tableaux comparatifs servent de grille de décision ; les schémas d'architecture servent de support de revue de
conception.
Public et prérequis
Le contenu s'adresse à des étudiants de master et de doctorat, à des ingénieurs IA et à des praticiens de la
recherche appliquée. Les prérequis sont la connaissance de l'apprentissage automatique classique, de
l'algorithmique numérique et des bases de probabilités. Les parties 1 à 3 sont auto-suffisantes pour un étudiant qui
découvre le domaine ; les parties 4 à 7 supposent la mécanique et les outils présentés dans la partie 2.
Conventions de lecture. Une expression mathématique est encadrée par deux signes dollars ; un identifiant, un
fichier ou une commande est écrit en caractères à chasse fixe ; les encadrés Définition, Théorème, Méthode et
Attention signalent les points à maîtriser et les pièges fréquents. Les renvois de la forme « voir chapitre 3.2 »
désignent le second chapitre de la troisième partie.
Progression pédagogique
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
7
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
8
Des fondations symboliques à l'industrialisation
Partie 1
Intelligence artificielle de A à Z
Un cours panoramique qui traversé toute la discipline dans l'ordre des dépendances : on représente
d'abord la connaissance, on apprend ensuite à l'exploiter, puis on la genere, enfin on l'industrialise.
Chaque module reprend les notions du précédent et indique ce qu'il faut savoir faire, pas seulement
comprendre.
Objectifs de la partie
• Représenter une connaissance sous forme exploitable : règles, prédicats, ontologies.
• Explorer un espace d'états de façon exacte (A*) ou sous contrainte de temps (minimax).
• Choisir entre modèle linéaire, forêt, réseau profond et modèle de langage.
• Comprendre l'auto-attention, l'encodage positionnel et l'ajustement de faible rang.
• Mettre en place un cycle MLOps, une API d'inférence et une surveillance de production.
• Auditer un modèle sur ses biais, son explicabilité et la gouvernance de ses données.
Plan de la partie
1.  Fondations et logique symbolique
2.  Apprentissage automatique et profond
3.  IA générative et modèles de langage
4.  MLOps, éthique et responsabilité
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
9
Chapitre 1.1
Fondations et logique symbolique
Tout le reste du cours repose sur une idée : rendre la connaissance calculable.
Figure 1 — Les quatre blocs de l'intelligence artificielle
L'agent rationnel
L'agent rationnel est le modèle de référence de toute intelligence artificielle : il perçoit son environnement,
choisit une action parmi celles possibles, et apprend de la conséquence obtenue. Ce schéma en quatre temps
suffit à englober la recherche sur les agents, la planification automatique et l'apprentissage par
renforcement.
Figure 2 — Le cycle perception-décision-action de l'agent
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
10
Stratégie
Principe
Optimalité
Usage
Recherche en largeur
on 
explore 
tous 
les
successeurscomplète, mais coûteuse
espaces 
profonds, 
mémoire
suffisante
Recherche gloutonne
on 
ne 
garde 
que 
le 
meilleur
successeur
incomplète, rapide
problèmes bien structurés
A*
gloutonne guidée par une estimation
de coût restant
optimale 
si 
l'estimation 
est
admissible
planification, robotique, jeux
Minimax
alternance 
maximisation 
et
minimisation
optimale contre un adversaire
parfait
jeux à deux joueurs
Apprentissage par
renforcement
approximation apprise
approximative, amortie
systèmes 
trop 
vastes 
pour
l'énumérer
Tableau 1 — Trois stratégies d'exploration d'un espace d'états
A* et minimax partagent la même question : quel ordre d'exploration rend la garantie atteignable dans le budget
disponible ?
f*(n) = mina ∈ A(n) ≤ft[ c(n, a) + h(n') ]
V(X) = maxa ≤ft[ r(X, a) + γ E≤ft[V(X')] ]
(Z.1)
La fonction d'évaluation d'A* est une estimation du coût restant ; l'équation de Bellman est la condition
d'équilibre d'une politique. Les deux expressions disent la même chose : valeur estimée plus valeur future.
Astuce
Une heuristique admissible (qui ne surestime jamais le coût restant) est la condition exacte pour que la
recherche A* soit optimale. Une heuristique qui surestime rend la recherche plus rapide mais produit des
solutions dégradées — arbitrage direct entre garantie et performance.
Représenter la connaissance : systèmes experts et règles
Un système expert combine une base de règles et un moteur d'inférence. Le nombre d'expert humain se
transforme en règles du type « si <prémisse> alors <conclusion> », et le moteur enchaîne les règles pour
répondre à une question posée.
• Avantage : explicabilité totale. On peut nommer la règle qui a produit la conclusion.
• Avantage : extrapolation contrôlée. Le système ne dit rien là où aucune règle ne s'applique.
• Limite : l'acquisition des règles est la partie la plus coûteuse et la moins automatisable du projet.
• Limite : la maintenance explose à mesure que le domaine s'étend — c'est la cause principale du premier
hiver de l'IA.
Logique des prédicats et ontologies
La logique des prédicats étend la logique propositionnelle par des variables, des prédicats et des
quantificateurs. Elle permet d'exprimer une règle générale et de l'appliquer par unification.
∀ x ≤ft[ Homme(x) → Mortel(x) ]
p(X) ∧ ∀ Y p(Y) ⇒ ∃ Z q(X, Z)
(Z.2)
La première formule est un syllogisme : tout homme est mortel. La seconde introduit la quantification
existentielle, c'est-à-dire la capacité d'inventer une constante qui n'était pas dans les prémisses — c'est la source
de la puissance comme de l'explosion combinatoire du raisonnement.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
11
Logique des prédicats
Ontologie
Élément
Formule et prédicat
Classe, individu, relation
Rôle
raisonner, déduire
décrire,typer, relier
Exemple
tout homme est mortel
un patient a une pathologie
Contradiction gérée
logiquement, par démonstration
par incohérence de l'ontologie
Outil
moteur de déduction, Prolog
influenceur, éditeur ontologique
Limite
explosion combinatoire
coût de construction et de maintenance
Tableau 2 — Logique des prédicats et ontologies : deux usages distincts
Les deux sont complémentaires : l'ontologie décrit le monde, la logique en tire les conséquences.
Inverser un quantificateur. « Toute femme est médecin » ne signifie pas « toute médecin est femme ». Les
moteurs de déduction ne font pas cette erreur ; les guides humains, si. Et, un modèle génératif produit
aussi des généralisations de ce type sans le moindre signal dans les données.
L'erreur de raisonnement la plus coûteuse
A retenir
• L'agent rationnel est le modèle de référence de toute la discipline.
• A* et minimax répondent à la même question : quel ordre d'exploration rend la garantie atteignable ?
• La logique des prédicats rend la connaissance calculable mais souffre d'explosion combinatoire.
• L'ontologie décrit le monde, la logique en tire les conséquences : les deux sont complémentaires.
Chapitre 1.2
Apprentissage automatique et profond
Quand l'écriture des règles devient impossible, on apend à les déduire des exemples.
L'apprentissage automatique remplace l'écriture explicite des règles par leur extraction à partir d'exemples.
Le changement de paradigme est radical : on passe d'un système qui sait pourquoi il répond à un système
qui sait seulement quoi répondre.
Apprentissage supervisé classique
Algorithme
Principe
Données adaptées
Limite principale
Régression linéaire
ajuste 
une 
droitetabulaires,
relation linéaire
sensible aux valeurs extrêmes
Régression logistique
ajuste une probabilité
tabulaires, classification binaire
séparation linéaire seulement
Machines à vecteurs de
support
sépare au plus près possible
petites dimensions, frontières nettes
coût en forte dimension
Arbre de décision
pose des questions successives
tabulaires, explicabilité
instable, n'extrapole pas
Forêt aléatoire
moyenne de nombreux arbres
tabulaires, 
bon 
rapport
gain/complexité
modèle volumineux
Renforcement de
gradient
corrige les erreurs d'un modèle
faible
tabulaires, meilleur score
sensible aux hyperparamètres
Tableau 1 — Les algorithmes supervisés et ce qu'ils attendent des données
Sur données tabulaires, le renforcement de gradient est presque toujours le meilleur premier essai ; sur texte ou image,
un réseau profond le dépasse très largement.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
12
Apprentissage non supervisé
Sans étiquette, l'objectif change : on cherche une structure. Les deux familles les plus utilisées sont le
regroupement, qui cherche des groupes, et la réduction de dimension, qui compresse en conservant
l'essentiel.
• K-moyens : partition en K groupes par minimisation de la dispersion interne. Sensible à l'initialisation et
à l'échelle des variables — d'où la nécessité de normaliser.
• ACP : projette les données sur les axes de plus forte variance. Interprétable, mais linéaire : il ne voit pas
les structures courbes.
• Réduction non linéaire : projection sur des vecteurs, méthodes de voisinage. Bien plus expressive, bien
moins lisible.
Choisir son première méthode, en quatre questions
• La donnée est-elle étiquetée ? Si non, on part de K-moyens.
2. La donnée est-elle tabulaire ou structurée ? Si oui : forêt aléatoire comme référence, puis renforcement de
gradient.
3. La donnée est-elle une image, un son, du texte ou une série ? Si oui : réseau convolutif, récurrent ou
transformateur.
4. Quelle erreur coûte le plus cher ? Le choix de la métrique et de la classe de référence en découle.
Réseaux profonds
Un réseau profond est une composition de transformations non linéaires. Trois familles de couches
correspondent à trois hypothèses sur la structure des données.
Réseau
Hypothèse
Structure
Domaine
Perceptron multicouche
aucune 
structure
particulièrecouches 
denses 
fully
connectées
vecteurs, tabulaire
Réseau convolutif
grille régulière, voisinage local
filtres glissants partagés
image, signal, audio
Réseau récurrent (RNN,
LSTM)
dépendance strictement ordonnée
état caché propagé dans le temps
séries temporelles, audio, texte
Transformateur
dépendance 
entre 
positions
quelconques
auto-attention multi-têtes
texte, code, multimodal
Tableau 2 — Perceptron, convolution, récurrence : trois hypothèses
• Perceptron multicouche : la brique de base. Sans structure spatiale ou temporelle, mais suffisante pour
des vecteurs.
• LSTM : la cellule à portes corrige le problème de l'oubli des réseaux récurrents simples en apprenant
quels éléments garder.
• CNN : les filtres partagés rendent le modèle invariant par translation et réduit fortement le nombre de
paramètres.
• Transformateur : abandonné l'ordre au profit d'une dépendance globale apprise, au prix d'un coût
quadratique.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
13
1import torch
2import torch.nn as nn
3
4
5class BlocResiduel(nn.Module):
6''"Bloc de reference : convolution, normalisation, activation, saut.
7
8L'ordre normalisation-activation-convolution n'est pas indifferent :
9la normalisation doit preceder l'activation pour stabiliser
10l'entrainement, et la connexion residuelle doit envelopper l'ensemble
11du bloc pour que le gradient circule sans attenuation.
12''"
13
14def __init__(self, entrees: int, sorties: int, facteur: int = 4):
15super().__init__()
16reducteur = entrees // facteur
17self.norm1 = nn.GroupNorm(8, entrees)
18self.conv1 = nn.Conv2d(entrees, reducteur, kernel_size=3, padding=1)
19self.norm2 = nn.GroupNorm(8, reducteur)
20self.conv2 = nn.Conv2d(reducteur, reducteur, kernel_size=3, padding=1)
21self.norm3 = nn.GroupNorm(8, reducteur)
22self.conv3 = nn.Conv2d(reducteur, sorties, kernel_size=3, padding=1)
23self.saut = (nn.Identity() if entrees == sorties
24else nn.Conv2d(entrees, sorties, kernel_size=1))
25self.activation = nn.GELU()
26
27def forward(self, x: torch.Tensor) -> torch.Tensor:
28y = self.conv1(self.activation(self.norm1(x)))
29y = self.conv2(self.activation(self.norm2(y)))
30y = self.conv3(self.activation(self.norm3(y)))
31return self.saut(x) + y
32
33
34class Extracteur(nn.Module):
35''"Encodeur convolutif : convolution d'entree, blocs residuels, moyenne.''"
36
37def __init__(self, canaux: int = 3, largeur: int = 64, profondeur: int = 4,
38normative: bool = True):
39super().__init__()
40self.normative = normative
41self.entree = nn.Conv2d(canaux, largeur, kernel_size=5, padding=2)
42self.blocs = nn.ModuleList([
43BlocResiduel(largeur if i == 0 else largeur * 4,
44largeur * 4 if i < profondeur - 1 else largeur)
45for i in range(profondeur)])
46self.normale = nn.LayerNorm(largeur)
47
48def forward(self, x: torch.Tensor) -> torch.Tensor:
49if self.normative:
50# centrage par image : la moyenne est calculee par lot et par canal
51x = x - x.mean(dim=(0, 2, 3), keepdim=True)
52y = self.entree(x)
53for bloc in self.blocs:
54y = bloc(y)
55y = self.normale(y.mean(dim=(2, 3)))
56return y
Listing 1 — Encodeur convolutif avec blocs résiduels et normalisation
A retenir
• Le changement de paradigme est radical : de règles explicites à l'extraction de règles.
• Sur données tabulaires, le renforcement de gradient est le meilleur premier essai.
• Réduire de dimension et regrouper exigent une normalisation préalable.
• Chaque famille de couche encode une hypothèse sur la structure des données.
Chapitre 1.3
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
14
IA générative et modèles de langage
Un modèle de langage est un modèle qui prédit la suite — et toute la génération en découle.
Auto-attention : le mécanisme central
L'auto-attention permet à chaque position de comparer son représentation à toutes les autres, et de
pondérer ces liens par apprentissage. Elle remplace la récurrence, ce qui rend l'entraînement entièrement
parallèle.
Attention(Q,K,V) = softmax≤ft((Q K⊤)/(√(dk)) + M) V
Entêtei = Attention≤ft(X Wi
Q, X Wi
K, X Wi
V)
(Z.3)
Trois projections, trois rôles : la requête identifie ce que la position cherche, la clé indique ce qu'elle offre, et la
valeur porte le contenu. L'échelle 1/√(dk) est indispensable : sans elle la softmax sature et le modèle n'apprend
rien.
Pourquoi l'encodage positionnel est nécessaire
L'auto-attention est permutationnelle : elle ne sait pas, seule, dans quel ordre les jetons arrivent. L'encodage
positionnel réinjecte cette information en ajoutant à chaque représentation une signature de sa position.
Famille
Principe
Atout
Limite
Absolu
une 
table 
apprise 
pour 
chaque
positionsimple, précis en position
limité à la longueur apprise
Relatif
décalage apprise entre positions
extensibilité en longueur
position approximative
Rotationnel
rotation de fréquence par dimension
propriété relative naturelle
qualité variable selon la règle
Fondu
signal slowly-growing noyé dans le
mot
s'intègre à l'architecture
dégradation 
si 
la 
longueur
dépassela fenêtre d'entraînement
Tableau 1 — Trois familles d'encodage positionnel
Ajustement : du préentraînement à l'usage
Un modèle de langage se préentraîne sur un corpus entier, puis s'ajuste sur une tâche ou un domaine.
L'ajustement complet est coûteux et détruit le bénéfice du préentraînement ; l'ajustement de faible rang
corrige le problème.
Wt+1 = Wt + (α)/(r) Bt At, At ∈ ℝr × d, Bt ∈ ℝd × r, r ≪ d
(Z.4)
Seuls A et B sont entraînés, soit une fraction de la matrice W. Le facteur α/r compense la réduction de rang :
l'oublier rend l'adaptation instable d'une configuration à l'autre.
Voie
Paramètres entraînés
Coût mémoire
Usage privilégié
Ajustement complet
la totalité
très élevémodèle dédié,
données massives
Adaptation de faible rang
0,1 à 1 %
faible
le cas par défaut en entreprise
Adaptateurs discrets
0,01 à 0,1 %
très faible
terminaux, appareils embarqués
Apprentissage de consignes
aucun
nul
tâches ponctuelles
Tableau 2 — Les trois voies d'adaptation d'un modèle de langage
La règle est simple : si l'on peut énoncer des exemples de la tâche attendue, l'adaptation de faible rang suffit.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
15
Génération augmentée par récupération
La génération augmentée ne demande jamais au modèle de connaître une information : elle lui fournit les
passages pertinents au moment de la question. C'est le mécanisme central de l'usage d'entreprise.
• Indexation : les documents sont découpés en passages et projetés dans un espace vectoriel.
• Recherche : la question est projetée dans le même espace, et les passages proches sont récupérés.
• Assemblage : les passages filtrés par droits d'accès sont insérés dans la requête.
• Génération : le modèle répond en citant ses sources.
• Refus : si aucun passage ne soutient la question, le système répond qu'il ne sait pas.
Le refus est un comportement, pas un échec
Un système de génération augmentée qui répond systématiquement, même quand sa base ne contient pas la
réponse, est plus dangereux qu'un système qui se tait. Concevoir le refus, le mesurer et l'afficher est une
exigence de conception.
Agents conversationnels autonomes
Un agent conversationnel autonome ne se contente pas de répondre : il consulte des outils, planifie
plusieurs étapes et vérifie son propre résultat. La différence avec un assistant tient à la boucle de décision et
à l'instrument de vérification.
A retenir
• L'auto-attention remplace la récurrence et rend l'entraînement parallèle.
• L'encodage positionnel est indispensable : l'attention seule est permutationnelle.
• L'adaptation de faible rang est le compromis par défaut pour un usage d'entreprise.
• La génération augmentée impose de concevoir le refus comme un comportement normal.
Chapitre 1.4
MLOps, éthique et responsabilité
Un modèle qui ne se déploie pas n'existe pas, et un modèle déployé sans audit est un risque.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
16
Figure 1 — Le cycle MLOps et ses deux indicateurs de travail
Le cycle d'industrialisation
• Données : collecte, contrôle qualité, historisation. Rien ne commence avant.
• Entraînement : paramétrage versionné, graine fixée, expérimentation suivie.
• Évaluation : sur jeux de référence figés, avec métriques métier et non seulement techniques.
• Registre de modèles : chaque version est enregistrée avec ses données d'entraînement et ses métriques.
Sans cela, on ne peut pas rereconstruire un résultat.
• Déploiement : conteneurisation, infrastructure as code, déploiement reproductible.
• Surveillance : latence, erreur, dérive des données, qualité des requêtes entrantes.
Les deux seuls indicateurs qui comptent au début
Fréquence de déploiement : combien de fois par semaine l'équipe livre-t-elle une amélioration ? C'est le
meilleur témoin de la maturité du processus.
Délai de restauration : combien de minutes pour revenir à un état stable après un incident ? C'est le meilleur
témoin de la maturité de l'exploitation.
Tant que l'un des deux est mauvais, aucun autre investissement d'industrialisation n'est prioritaire.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
17
1import hashlib
2import json
3import time
4from dataclasses import dataclass, asdict
5from pathlib import Path
6
7import numpy as np
8
9
10@dataclass(frozen=True)
11class Signature:
12''"Identite complete d'un modele : version, donnees, configuration.
13
14Cette empreinte est ce qui permet, six mois plus tard, de rejouer
15exactement le meme resultat. Elle doit etre calculee et stockee avec
16le modele, jamais reconstruite a la main.
17''"
18
19version: str
20empreinte_donnees: str
21empreinte_code: str
22configuration: dict
23horodatage: float
24
25def empreindre(self) -> str:
26charge = json.dumps(asdict(self), sort_keys=True, default=str)
27return hashlib.sha256(charge.encode("utf-8")).hexdigest()[:16]
28
29
30def enregistrer(chemin: Path, sig: Signature, metriques: dict) -> str:
31chemin.parent.mkdir(parents=True, exist_ok=True)
32ident = sig.empreindre()
33with chemin.open("a", encoding="utf-8") as f:
34f.write(json.dumps({
35"id": ident, "signature": asdict(sig), "metriques": metriques,
36"train": time.time()}, default=str) + "\n")
37return ident
38
39
40def comparer(reference: dict, candidat: dict,
41tolerance: float = 0.01) -> tuple[bool, dict]:
42''"Verdict de promotion : on n'accepte que si rien ne se degrade.
43
44Regle : la precision peut baisser dans la limite fixee, mais aucun
45sous-groupe de population ne doit degrader au-dela du seuil. C'est la
46seule condition qui evite d'échanger une regression globale
47contre une regression invisible.
48''"
49ecarts = {}
50accepte = True
51for cle, attendu in reference.items():
52if cle == "global":
53continue
54delta = candidat[cle] - attendu
55ecarts[cle] = delta
56if delta < -tolerance:
57accepte = False
58globale = candidat.get("global", 0.0) - reference.get("global", 0.0)
59if globale < -tolerance:
60accepte = False
61return accepte, ecarts
Listing 1 — Registre de modèles et règle de promotion par sous-groupe
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
18
Conteneurisation et API d'inférence
• Conteneurisation : le modèle et ses dépendances voyagent ensemble. Un modèle n'est reproductible
que si son environnement l'est aussi.
• Version du format : le format de sérialisation est lui-même versionné. Un fichier de poids sans sa
version de format n'est pas un artefact, c'est une devinette.
• API d'inférence : contrat stable, limites de débit explicites, réponses d'erreur typées.
• Repli : si le service est indisponible, le système doit avoir un comportement défini — pas une page
blanche.
Surveillance en production
Famille
Exemples
Ce qu'une anomalie signale
Technique
latence, 
débit, 
erreurs, 
mémoiredégradation
d'infrastructure
Qualité
longueur des réponses, refus, notes
dérive du modèle ou du service
Données
distribution des entrées, valeurs manquantes
dérive des données en amont
Affaires
taux de conversion, coût par requête
perte de valeur malgré une technique saine
Tableau 1 — Quatre familles de métriques de production
La famille « affaires » est celle qui déclenche les vraies décisions. Une latence dégradée se corrigé en quelques heures ;
une valeur en baisse demande une investigation.
Éthique, biais et explicabilité
Trois exigences distinctes se confondent souvent. La justice interroge la répartition des erreurs entre
groupes. L'explicabilité interroge la possibilité de justifier une décision. La gouvernance interroge la
chaîne de responsabilité.
Exigence
Question posée
Moyen
Limite
Justice
les 
erreurs 
sont-elles 
réparties
équitablement 
?décomposition 
des
métriques par groupe
corrige l'injustice, pas le modèle
Explicabilité
peut-on justifier la décision ?
valeurs de substitution, attention,
règles
post hoc : l'explication peut
mentir
Traçabilité
sait-on quelle version a décidé ?
registre, journal d'appels
ne dit pas si c'était correct
Gouvernance
qui répond si c'est faux ?
règles, responsable désigné
institue sans résoudre
Tableau 2 — Les trois exigences, distinctes et cumulables
Le règlement européen sur l'intelligence artificielle (AI Act, 2024) impose, selon la classe de risque, une
gestion documentée des risques, la qualité et la traçabilité des données, la transparence de l'usage, et un
contrôle humain effectif pour les usages à haut risque. Le règlement sur la protection des données
apporte, de son côté, minimisation, limitation des finalités et responsabilité. Un modèle déployé sans
registre de versions et sans journal des décisions ne satisfait aucune des deux exigences.
Cadre juridique
Déployer un modèle sans seuil de refus. Un système qui répond toujours paraît plus disponible et se
révèle plus dangereux : il produit une confiance que rien ne justifie. Le seuil de refus et la conduite à tenir
quand il est franchi doivent être écrits avant le déploiement, pas improvisés à la première erreur coûteuse.
L'erreur la plus coûteuse en production
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
19
Audit de conformité en sept points
• Finalité documentée, connue des utilisateurs.
2. Données : provenance, qualité, base légale, durée de conservation.
3. Métriques décomposées par groupe pertinent.
4. Registre des versions, des données et des décisions.
5. Seuil de refus et conduite associée.
6. Retour arrière possible en moins d'une heure.
7. Responsable désigné, avec procédure d'escalade.
A retenir
• Fréquence de déploiement et délai de restauration résument la maturité MLOps.
• Un modèle n'est reproductible que si son environnement l'est aussi.
• Justice, explicabilité et gouvernance sont trois exigences distinctes et cumulables.
• Le seuil de refus doit être écrit avant le déploiement, jamais improvisé.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
20
Abréviations, notation et ressources de consultation
Annexes
Annexes
Ce cours se termine par deux annexes de référence. La première donne la signification de chaque sigle
employé, sous les deux formes — sigle et développé — car la litterature emploie indifféremment l'une
ou l'autre. La seconde donne la signification de chaque symbole mathématique : elle permet de relire
une démonstration sans revenir au chapitre dont elle est extraite, et de vérifier qu'un même symbole
garde le même sens d'un chapitre à l'autre.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
21
Chapitre A.1
Liste des abréviations
Les sigles ci-dessous sont ceux que le cours emploie. Chacun est donné avec sa forme développée
et le sens précis qu'il prend ici, qui n'est pas toujours celui qu'on lui donne ailleurs.
Un sigle employé sans être développé oblige le lecteur à le reconnaître au passage, ou à l'abandonner. Le
tableau ci-dessous ferme la liste de ceux que le cours emploie : il est exhaustif pour ce document, et non
pour la discipline.
Sigle
Forme développée
Sens dans ce cours
ACP
Analyse en composantes principales
Projection sur les axes de plus grande variance, faite sans supervision.
AGI
Artificial General Intelligence
Intelligence artificielle générale, dont les capacités ne sont pas bornées à
une tâche.
API
Application Programming Interface
Interface de programmation qu'un logiciel offre à un autre.
CNN
Convolutional Neural Network
Réseau convolutif, employé sur les images.
GELU
Gaussian Error Linear Unit
Fonction d'activation, qui approxime la distribution gaussienne de l'erreur.
LLM
Large Language Model
Grand modèle de langage, pré-entraîné sur un corpus massif.
LSTM
Long Short-Term Memory
Cellule récurrente à mémoire longue.
RLHF
Reinforcement Learning from Human
Feedback
Alignement d'un modèle par renforcement sur des préférences humaines.
RNN
Recurrent Neural Network
Réseau récurrent.
SVM
Support Vector Machine
Machine à vecteurs de support.
t-SNE
t-distributed Stochastic Neighbor
Embedding
Réduction de dimension non linéaire, employée pour la visualisation.
Tableau 1 — Abréviations employées dans le cours
Chapitre A.2
Table de notation
Les symboles ci-dessous gardent le même sens d'un chapitre à l'autre. Lorsqu'un chapitre doit
réemployer un symbole pour un autre objet, il le redéclare sur la page même.
La notation est celle du cours : vecteurs en gras, matrices en majuscules grasses, scalaires en italique. Les
espérances sont notées E, les lois de données D, les espaces de paramètres Θ.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
22
Symbole
Signification
X
Matrice des observations, une ligne par exemple.
y
Vecteur des étiquettes associées.
ŷ
Prédiction produite par le modèle.
f_θ
Fonction apprise, paramétrée par θ.
θ
Vecteur de paramètres du modèle.
D
Loi de distribution des données.
d
Dimension de l'espace d'entrée.
C
Nombre de classes, pour un problème de classification.
N
Nombre d'exemples du jeu de données.
ℓi
Perte sur le i-ème exemple.
L
Perte moyenne sur le jeu entier.
Taux d'erreur.
σ(z)
Fonction logistique, qui borne une probabilité entre 0 et 1.
ReLU(z)
Fonction d'activation rectangulaire.
softmax(z)i
Composante i de la distribution softmax du vecteur z.
p
Précision d'un détecteur.
r
Rappel d'un détecteur.
F1
Moyenne harmonique de la précision et du rappel.
Tableau 1 — Symboles mathématiques et leur signification
Convention
Toute divergence constatée entre cette table et un chapitre signale une erreur de transcription, non une
définition nouvelle : la table fait foi.
A retenir
• Un sigle employé sans être listé ici est un oubli de l'auteur, non une définition nouvelle.
• Un symbole qui change de sens d'un chapitre à l'autre rend toute démonstration ininterprétable : c'est la
principale cause des contresens que nous avons relevés.
• Ces deux tables sont les seules parties du cours à maintenir à la main : le reste se relit tout seul.
Index des figures et des tableaux
Référence rapide du matériel visuel
Figures
1.  Les quatre blocs de l'intelligence artificielle
2.  Le cycle perception-décision-action de l'agent
1.  Le cycle MLOps et ses deux indicateurs de travail
Tableaux
1.  Trois stratégies d'exploration d'un espace d'états
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
23
2.  Logique des prédicats et ontologies : deux usages distincts
1.  Les algorithmes supervisés et ce qu'ils attendent des données
2.  Perceptron, convolution, récurrence : trois hypothèses
1.  Trois familles d'encodage positionnel
2.  Les trois voies d'adaptation d'un modèle de langage
1.  Quatre familles de métriques de production
2.  Les trois exigences, distinctes et cumulables
1.  Abréviations employées dans le cours
1.  Symboles mathématiques et leur signification
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
24
Fin du document
Intelligence Artificielle Avancée & Federated Learning — Fondations mathématiques de
l'apprentissage automatique, algorithmes fédérés, protection de la vie privée, défense contre les attaques,
grands modèles de langage fédérés, systèmes embarqués, renforcement appris, applications critiques
(santé, V2X), plateforme de référence FedX et feuille de route de recherche.<br/>Ghiloufi Jamel,
Architecte Logiciel Principal — Pixel Software Design<br/>Département de Recherche & Développement
— Recherche<br/>Pixel Software Design — Édition 2026
© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou
diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans
autorisation écrite préalable de l'auteur.
Document généré automatiquement le 29/09/2026 — mise en page Pixel Software Design.
"""


IA_RECHERCHE_OPERATIONNELLE_TEXT = r"""Pixel Software Design — Département de Recherche & Développement
PIXEL SOFTWARE DESIGN
Département de Recherche & Développement
Intelligence Artificielle
Avancée
& Federated Learning
•  Fondations de l'intelligence artificielle
•  Algorithmes d'apprentissage fédéré
•  Confidentialité, attaques et défenses
•  Applications et grands modèles fédérés
•  Framework FedX de référence
•  Nouveaux fronts de recherche
•  Travaux pratiques, projets et évaluation
Auteur
Ghiloufi Jamel
Fonction
Architecte Logiciel Principal
Direction
Département de Recherche & Développement
Service
R&D - Intelligence Artificielle Avancée & Apprentissage Fédéré
Niveau
Recherche
Édition
Édition 2026 — 1.0
Copyright
© Pixel Software Design
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou
diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans
autorisation écrite préalable de l'auteur.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
2
Copyright et mentions légales
Éditeur
Pixel Software Design
Auteur
Ghiloufi Jamel
Fonction
Architecte Logiciel Principal
Département
Département de Recherche & Développement
Intitulé
Intelligence Artificielle Avancée & Federated Learning
Sous-titre
Fondations mathématiques de l'apprentissage automatique, algorithmes fédérés,
protection de la vie privée, défense contre les attaques, grands modèles de langage
fédérés, systèmes embarqués, renforcement appris, applications critiques (santé,
V2X), plateforme de référence FedX et feuille de route de recherche.
Édition
Édition 2026 (version 1.0)
Langue
Français
Niveau
Recherche
Collection
Supports de formation et de recherche, Pixel Software Design
Droits d'auteur
© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation
ou diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite
sans autorisation écrite préalable de l'auteur.
Droits de l'auteur. Ghiloufi Jamel est l'auteur unique de l'ensemble du contenu scientifique, pédagogique et
technique de cet ouvrage. Toute adaptation, traduction, reproduction ou exploitation, y compris partielle, requiert
une autorisation écrite préalable.
Droits des tiers. Les algorithmes, modèles et travaux cités restent la propriété de leurs auteurs respectifs. Les
références employées figurent en fin d'ouvrage, ce qui permet de remonter au travail original pour toute
affirmation chiffrée.
Marques et licences externes. PyTorch, TensorFlow, Flower, Opacus, MONAI, scikit-learn et PySyft sont des
logiciels libres sous licences respectives (BSD, Apache 2.0, MIT). Leur usage dans ce document est purement
pédagogique et n'emporte aucune prescription commerciale.
Mentions relatives aux données et aux expérimentations
Document pédagogique à usage de formation interne. Les exemples de code fournis sont livrés à titre pédagogique
; les résultats numériques illustrés sont issus d'expérimentations conduites dans un cadre de recherche et ne
constituent pas des performances de production.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
3
Ce support synthétise les travaux de recherche du Département de Recherche & Développement de Pixel Software
Design sur l'intelligence artificielle distribuée, l'apprentissage fédéré, la protection de la vie privée et les systèmes
embarqués intelligents.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
4
Sommaire
Structure détaillée du cours
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 8
Partie 1 — IA et Recherche Opérationnelle
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 9
1.1 Recherche opérationnelle et apprentissage automatique : la couture
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 10
1.2 Prévision, décision et optimisation : la chaîne complète
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 12
1.3 Apprentissage par renforcement pour la décision séquentielle
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 14
1.4 Logistique et tournées de livraison
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 18
1.5 Ordonnancement et pilotage d'atelier
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 20
1.6 Énergie, finance et déploiement en production
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 30
Annexes
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 31
A.1 Liste des abréviations
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 31
A.2 Table de notation
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
5
Partie
Thème
Contenu
Compétence visée
Durée
Partie 1
Fondations
Statistique, optimisation, courbes d'apprentissage
Comprendre et formaliser
2-3 semaines
Partie 2
Algorithmes FL
FedAvg, convergence, hétérogénéité, système
Implémenter et régler
3-4 semaines
Partie 3
Confidentialité
DP, attaques, défenses, agrégation sécurisée
Auditer et sécuriser
2-3 semaines
Partie 4
Applications
FedLLM, santé, V2X, FedRL, TinyML, graphes
Transposer à un domaine
3-4 semaines
Partie 5
Framework FedX
Architecture, API, benchmarks, exploitation
Industrialiser
2 semaines
Partie 6
Nouveaux fronts
FedCL, FedCI, SNN, FedGL, feuille de route
Ouvrir la recherche
2 semaines
Partie 7
TP et projets
9 labs, 5 projets, corrigés, évaluation
Faire et rendre
4-6 semaines
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
6
Préface
Comment utiliser ce cours
Ce support est conçu pour un parcours de formation et de recherche couvrant l'ensemble de la chaîne de valeur de
l'intelligence artificielle distribuée : les fondations mathématiques, les algorithmes d'apprentissage fédéré, les
menaces et défenses, les applications de pointe, une plateforme de référence opérationnelle, et enfin les nouveaux
fronts ouverts par la recherche du Département.
Ce n'est pas un manuel de référence à lire d'un trait : c'est un manuel opératoire. Chaque chapitre alterne
exposition, formalisation, mise en œuvre numérique et évaluation. Les listings sont complets et exécutables ; les
tableaux comparatifs servent de grille de décision ; les schémas d'architecture servent de support de revue de
conception.
Public et prérequis
Le contenu s'adresse à des étudiants de master et de doctorat, à des ingénieurs IA et à des praticiens de la
recherche appliquée. Les prérequis sont la connaissance de l'apprentissage automatique classique, de
l'algorithmique numérique et des bases de probabilités. Les parties 1 à 3 sont auto-suffisantes pour un étudiant qui
découvre le domaine ; les parties 4 à 7 supposent la mécanique et les outils présentés dans la partie 2.
Conventions de lecture. Une expression mathématique est encadrée par deux signes dollars ; un identifiant, un
fichier ou une commande est écrit en caractères à chasse fixe ; les encadrés Définition, Théorème, Méthode et
Attention signalent les points à maîtriser et les pièges fréquents. Les renvois de la forme « voir chapitre 3.2 »
désignent le second chapitre de la troisième partie.
Progression pédagogique
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
7
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
8
Optimiser sous incertitude, et savoir quand s'arrêter
Partie 1
IA et Recherche Opérationnelle
La recherche opérationnelle optimise une décision sous contraintes déclarées. L'apprentissage
automatique estime les grandeurs dont cette décision dépend. Les deux compétences sont
complémentaires, et leur couture est exactement l'endroit où se perd la valeur : une erreur
d'estimation ne se signale jamais comme telle, elle devient une décision sous-optimale. Ce cours
décrit la chaîne complète, du modèle de prévision au solveur, et s'attarde sur les quatre manières
d'hybrider — par ordre croissant de prise de risque — ainsi que sur les quatre domaines où la
synergie produit un gain mesurable : logistique, ordonnancement, énergie et finance.
Objectifs de la partie
• Formuler la question qui décide de l'hybridation : quelles grandeurs sont incertaines, et quel est le coût d'une
erreur d'estimation.
• Distinguer erreur de prévision et erreur d'optimisation, et mesurer la seconde en unités de valeur économique.
• Expliquer pourquoi un simulateur entraîne une politique pour le simulateur, et comment_on rend ce transfert
défendable.
• Résoudre un problème de tournées avec fenêtres horaires, et expliquer pourquoi il n'a pas de solution exacte à
l'échelle.
• Modéliser un atelier comme un graphe de contraintes, et expliquer le rôle exact du réseau de neurones dans
cette modélisation.
• Choisir, parmi quatre modes d'hybridation, celui que l'on peut défendre devant un auditeur de risque.
Plan de la partie
1.  Recherche opérationnelle et apprentissage automatique : la couture
2.  Prévision, décision et optimisation : la chaîne complète
3.  Apprentissage par renforcement pour la décision séquentielle
4.  Logistique et tournées de livraison
5.  Ordonnancement et pilotage d'atelier
6.  Énergie, finance et déploiement en production
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
9
Chapitre 1.1
Recherche opérationnelle et apprentissage
automatique : la couture
Deux compétences, une seule couture. Tout le reste en découle.
Un modèle d'optimisation et un modèle d'apprentissage répondent à deux questions différentes. Le premier
demande : parmi toutes les façons de faire, laquelle est la meilleure sous les contraintes que je déclare ? Le
second demande : qu'est-ce qui va réellement se produire, et avec quelle incertitude ? La plupart des
systèmes industriels échouent non pas parce que l'un des deux est mauvais, mais parce qu'on a traité la
réponse du second comme un nombre certain au lieu d'une loi de probabilité.
Figure 1 — Deux compétences complémentaires, et la couture entre les deux
Question
Recherche opérationnelle
Apprentissage automatique
Quelle est la meilleure décision ?
répond exactement, si le modèle est juste
ne répond pas : il ne cherche pas d'optimum
Que va-t-il se passer ?
ne répond pas : ses paramètres sont déclarés
répond par une loi estimée, jamais par un
nombre
Combien de solutions existe-t-il ?
les énumère quand l'espace le permet
approxime une politique, sans les voir toutes
Que se passe-t-il si le modèle est faux ?
produit un optimum du mauvais problème
produit une décision plausible du mauvais
monde
Comment garantir le résultat ?
garantit l'optimalité sous hypothèses
ne garantit rien, et le dit
Comment détecter son erreur ?
ne le peut pas, faute de référence
mesure sa propre incertitude, quand on le lui
demande
Tableau 1 — Ce que chacune des deux disciplines sait faire et ignorant
Les deux dernières lignes sont les plus importantes. Une garantie d'optimalité porte sur un modèle, jamais sur le monde ;
et une incertitude non demandée n'est jamais fournie.
minx ∈ 1 c⊤ x sous A x ≤ b, x ∈ Zn
c ← ĉ, E≤ft[ c(x⋆) - c⋆ ] ≤ E≤ft[ ≤ft| ĉ - c | ] · ≤ft| x⋆ - x⋆
ĉ |
(R.1)
La première expression est le programme linéaire. La seconde est la question centrale de tout système hybride :
l'écart d'optimisation se borne par le produit de l'erreur d'estimation et de la sensibilité de la solution à cette
erreur. Un paramètre mal estimé dont la solution y est insensible ne coûte rien ; un paramètre critique, même
bien estimé en moyenne, coûte cher dès qu'il est mal estimé.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
10
Figure indisponible
La figure ro_explosion n'est pas encore implementee.
Poser la question qui décide de l'hybridation, en trois étapes
• Lister les grandeurs du modèle d'optimisation. Toutes. Y compris celles que l'on croitISHED constantes :
coûts, durées, capacités, taux de panne.
2. Classer ces grandeurs par sensibilité de la solution. On mesure cette sensibilité en perturbant chaque
paramètre de dix pour cent et en observant le coût de la solution. C'est le classement le plus utile du projet.
3. N'investir en apprentissage que sur les trois premiers. Les autres sont soit stables, soit insensibles, et
l'effort d'apprentissage sur un paramètre insensible est du travail purement perdu.
Ce classement prend une demi-journée et évite, dans la majorité des projets rencontrés, la majorité du travail
d'apprentissage automatique.
Un modèle de prévision fournit une moyenne, l'optimiseur reçoit cette moyenne comme si elle était
certaine, et produit un plan exactement optimal pour un scénario qui n'a pas eu lieu. L'erreur ne se
manifeste jamais : le solveur a fait son travail. Elle n'apparaît qu'en exécution, sous forme d'un stock
manquant, d'un camion qui attend, d'un client servi en retard. La parade est de passer la loi de probabilité
au solveur, pas son espérance.
L'erreur classique : optimiser pour la moyenne
Astuce
Une prévision biaisée est pire qu'une prévision bruitée. Le bruit se moyenne sur les décisions successives ; le
biais se cumulé et déplace durablement la solution. Pour cette raison, mesurer le biais d'un modèle de prévision
est plus important que mesurer sa variance, et c'est le test que l'on oublié le plus souvent.
A retenir
• La RO optimise une décision, l'apprentissage estime les grandeurs dont elle dépend : la couture est le lieu de la
valeur perdue.
• L'écart d'optimisation se borne par le produit de l'erreur d'estimation et de la sensibilité de la solution.
• Un paramètre mal estimé mais insensible ne coûte rien : classer par sensibilité avant d'investir.
• Optimiser pour la moyenne d'une prévision produit un plan exact pour un monde qui n'existe pas, sans jamais
le signaler.
• Un biais se cumulé, un bruit se moyenne : mesurer lebiais avant la variance.
Chapitre 1.2
Prévision, décision et optimisation : la chaîne
complète
La chaîne a quatre étages et une boucle de retour. Rompre la boucle est l'erreur la plus coûteuse.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
11
Figure 1 — Prédire puis optimiser : où la prédiction devient un pari
L'architecture canonique de l'hybridation comporte quatre étages : la donnée, la prévision, l'optimisation, la
décision, puis un retour de la réalité qui réaligne le modèle de prévision. Chaque étage peut être excellent
et le système complet être mauvais, parce que les critères de qualité des étages ne sont pas les mêmes.
x⋆
ĉ = argminx ĉ⊤ x, Régret = c⊤ x⋆
ĉ - c⊤ x⋆
c
(R.2)
Le regret est la seule métrique qui compte. Il compare le coût réellement payé au coût de la meilleure décision
possible. Une erreur de prévision qui ne change pas la décision produit un regret nul, quelle que soit sa taille ;
une erreur minime qui bascule la solution produit un regret important.
Étage
M métrique pertinente
Erreur typique
Conséquence de son ignorance
Donnée
couverture, fraîcheur, intégrité
valeurs manquantes silencieuses
le modèle apprend un biais de sélection
Prévision
biais par sous-groupe, calibration
erreur absolue moyenne faible mais
biaisée
le regret croît linéairement
Optimisation
régret par rapport au plan exact
mesure de l'optimalité du modèle,
pas du monde
on optimise le mauvais problème sans le
savoir
Décision
coût économique de l'exécution
aucune mesure de la valeur perdue
aucune amélioration malgré un meilleur
modèle
Tableau 1 — Ce qu'il faut mesurer à chaque étage
La ligne 2 est la plus contre-intuitive : la calibration vaut mieux que l'erreur absolue moyenne, parce qu'elle seule
distingue un bruit d'un biais.
Mesurer la calibration, et non seulement l'erreur
Un modèle qui annonce 60 % de probabilité sur 100 cas doit en avoir environ 60 de bons. C'est la seule
vérification qui distingue une prévision qui se trompe au hasard — donc inoffensive — d'une prévision qui se
trompe systématiquement dans le même sens — donc coûteuse et silencieuse. La calibration se mesure par
repliement : on regroupe les prédictions par tranche de probabilité, et on compare la fréquence observée à la
probabilité annoncée. Un modèle bien calibré s'aligne sur la diagonale ; un modèle biaisé s'en écarte de façon
systématique.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
12
Algorithme 1 — Boucle d'alignement entre prédiction et exécution
01  Fixer la période d'évaluation et les groupes de segmentation
02  Calculer les prédictions sur la période, et conserver la loi, pas le point
03  Exécuter la décision issue de ces prédictions, et relever le coût réel
04  Comparer le coût réel au coût de la meilleure décision retrospectively possible
05  Décomposer le regret en part d'erreur de prévision et part de structure
06  Réentraîner sur les écarts, en pondérant davantage les groupes sous-représentés
07  Refaire le calcul : un même tour de comparaison ne prouve rien
Entrées : Historique de prédictions, décisions exécutées, coûts réels • Sorties : Régret par groupe et par
période, modèle corrigé • Complexité : Coût dominant : levaluation, pas l'entraînement
La étape 5 est celle qui rend le travail utile. Un regret agrégé ne dit pas où chercher ; un regret décomposé par
groupe et par type de décision désigne la correction.
Un modèle de prévision entraîné sur les conséquences de ses propres décisions passées ferme une boucle
: il n'a jamais vu ce qui se serait produit sans sa recommandation, et il attribué à sa propre politique le
mérite d'un monde qu'il a lui-même contribué à produire. La parade est de conserver un exploration
minimum — une part des décisions prises au hasard ou par une règle fixe — dont la valeur contrefactuelle
est observable. Cette part est le seul instrument qui permet d'estimer ce que le modèle ne ferait pas.
Réentraîner sur ses propres décisions
A retenir
• Le regret, et non l'erreur de modèle, est la seule métrique qui a du sens la valeur créée.
• La calibration distingue un bruit inoffensif d'un biais coûteux ; l'erreur absolue ne le fait pas.
• Décomposer le regret par groupe et par type de décision désigne la correction à faire.
• Entraîner sur les conséquences de ses propres décisions ferme la boucle et supprime toute contrefactualité.
• Une part d'exploration maintained est le seul moyen d'estimer ce que le modèle ne ferait pas.
Chapitre 1.3
Apprentissage par renforcement pour la
décision séquentielle
La récompense est une fonction de conception. Un agent parfait sur une mauvaise récompense est
un agent qui réussit le mauvais chose.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
13
Figure 1 — Apprentissage par renforcement : la boucle, et son point faible
L'apprentissage par renforcement intervient lorsque la décision n'est pas un problème d'optimisation mais
un enchaînement : le choix de maintenant modifie les options de plus tard. Un tournee d-optimalisolément
n'est pas une politique bonne ; une politique bonne produit des décisions acceptables à chaque instant, y
compris ceux où l'on ne regrettera pas l'optimum global.
boldsymbolπ⋆ = argmaxboldsymbolπ Eboldsymbolπ ≤ft[ ∑t=0
T γt r(st, at) ], r = r0 - λ r1(R.3)
Les deux termes de la récompense ne sont pas du même ordre. Le premier est le revenu, mesurable et vérifiable.
Le second est la pénalité de non-qualité, et son poids lambda est le paramètre le plus sensible de tout le système
: il exprime la valeur d'une livre manquée, et une erreur d'un facteur dix sur lambda produit une politique qui
optimise la mauvaise grandeur.
• Récompense instantanée ou différée : une récompense immédiate facilite l'apprentissage mais produit
des agents qui sacrifient le long terme. Une récompense différée est la seule qui apprend un arbitrage
correct, au prix d'une exploration beaucoup plus longue.
• Masse de la récompense : un facteur de décompte proche de un apprend des politiques myopes ;
proche de zéro, il n'apprend rien, parce que l'horizon utile devient invisible.
• Pénalité de risque : ajouter un terme qui punit la variance des résultats plutôt que leur moyenne. C'est
la seule façon d'obtenir une politique qui ne mise pas tout sur un scénario.
• Exploration forcée : sans exploration, la politique se concentre sur ce qu'elle connaît et devient figée.
Une décroissance du taux d'exploration trop rapide produit un agent sous-optimal de façon irréversible.
Transférer une politique du simulateur au réel, en cinq contrôles
• Bruiter l'observation pendant l'entraînement. Un agent qui s'appuie sur un état parfait apprend une
politique qui exige cet état parfait. Le bruit est le seul moyen de rendre la politique robuste à l'incertitude
réelle.
2. Introduire le retard de contrôle variable. Un contrôleur réel réagit avec retard ; une politique entraînée
sans retard oscille ou diverge dès que le mouvement s'accélère.
3. Entraîner sur plusieurs horizons. Un agent entraîné sur un problème de vingt décisions échoue sur cent,
non par manque de capacité, mais parce que l'horizon n'a jamais été observé.
4. Fixer la graine et publier l'écart-type. Un résultat d'entraînement est un échantillon, pas une mesure ; trois
graines suffisent à révéler une variance qui invalide une conclusion.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
14
5. Rejouer un scénario figé avant tout déploiement. Un test de non-régression, choisi pour être représentant
du pire cas réel, vaut mieux qu'une évaluation moyenne sur mille scénarios.
Ce que l'agent ne peut pas corriger seul
Un agent de renforcement apprend une politique cohérente avec sa récompense, pas une politique conforme aux
règles de l'entreprise. Trois catégories de règles lui sont extérieures et doivent être appliquées après coup : les
contraintes dures, qui rendent une décision impossible ; les contraintes de procédure, qui imposent un ordre que
l'agent ignore ; et les interdictions, qui portent sur des actions que l'agent ne voit jamais dans ses données.
Aucune quantité d'entraînement ne rendra un agent respecter une contrainte qu'il n'a pas observée violer.
Astuce
Une politique de renforcement est un actif de production difficilement réversible. Une règle d'ordonnancement
se lit, se corrigé et se déploie en une heure. Avant de mettre un agent en production, garder la règle en service
parallèle pendant une période complète de Representative, et comparer les deux décisions sur la même charge
réelle.
A retenir
• La récompense encode l'objectif qu'on avait en tête, pas celui que l'agent optimise : la savoir écrire et la
mesurer.
• Le poids de la pénalité de regret est le paramètre le plus sensible de tout le système.
• Le bruit d'observation, le retard et la variété des horizons sont les trois contrôles qui rendent le transfert
défendable.
• Trois familles de règles restent extérieures à l'agent et doivent être appliquées après coup.
• Une politique apprise est difficilement réversible : garder la règle en service parallèle avant de basculer.
Chapitre 1.4
Logistique et tournées de livraison
Le problème de tournées n'a pas de solution exacte à l'échelle. Toute la question est de savoir
laquelle on accepte.
Figure 1 — Le problème de tournées : un graphe qui ne se résout pas
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
15
Le problème de tournées avec capacité et fenêtres horaires est l'un des rares problèmes de l'industrie dont
on sait qu'il n'admet aucune solution exacte au-delà de quelques dizaines de points. Ce n'est pas une
faiblesse des méthodes : c'est une propriété démontrée du problème. Le rôle de l'ingénieur n'est donc pas de
chercher l'optimum, mais de produire une solution dont on sait dire à quel titre elle est acceptable.
min ∑k=1
K ∑i,j cij xijk sous ∑k ∑i qi yik ≤ Qk, ai ≤ ∑i ∈ V_k τi xiℓ k ≤ bi
(R.4)
Le coût est une somme d'arcs, la capacité est une contrainte de globale, et la fenêtre horaire est une contrainte
de borne sur la somme des temps de service. Chacune suffit à rendre le problème NP-difficile : le Lagrangien
relaxation résout relaxation, pas le problème.
Méthode
Ce qu'elle garantit
Budget typique
Usage
Exhaustive, branchement et
coupe
l'optimum, pour petite taille
explose au-delà de 15 points
études de cas, références
Programmation linéaire
relaxation, jamais l'optimum
secondes à minutes
bornes 
inférieures,
dimensionnement
Recherche locale (2-opt, Or-opt)
rien, mais elle monte vite
quelques secondes
qualité initiale
Métaheuristique guidée
rien, mais elle s'améliore
de quelques secondes à quelques
minutes
le standard industriel
Apprentissage d'une politique
rien, et cela s'entraîne
entraînement 
long, 
exécution
nulle
à 
grande 
échelle, 
après
cadrage
Tableau 1 — Les solveurs et ce qu'ils garantissent
La dernière ligne est la seule qui change d'échelle. Elle ne remplace pas la métahéuristique : elle la remplace par une
initialisation apprise, ce qui divisé le budget de recherche d'un ordre de grandeur.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
16
1import math
2from dataclasses import dataclass, field
3
4
5@dataclass
6class Commande:
7''"Une demande a livrer, avec sa fenetre horaire et sa charge.''"
8identifiant: str
9x: float
10y: float
11quantite: float
12ouverture: float # debut de la fenetre, en minutes
13fermeture: float # fin de la fenetre, en minutes
14service: float = 8.0 # duree de service sur place
15
16@property
17def milieu(self) -> float:
18return 0.5 * (self.ouverture + self.fermeture)
19
20
21@dataclass
22class Tournee:
23''"Une solution partielle : un vehicule et son ordre de passage.''"
24vehicule: int
25commandes: list = field(default_factory=list)
26distance: float = 0.0
27fin: float = 0.0
28
29def cout_arcs(self, a, b) -> float:
30return math.hypot(a.x - b.x, a.y - b.y)
31
32
Listing 1 — Insertion incrémentale et évaluation de faisabilité d'un plan de tournées
33def insertion_croissante(commande, tournees, capacite, depot, depart=0.0):
34''"Insere la commande dans la tournee la moins dechiree.
35
36Le choix se fait sur le cout marginal reel, et non sur une regle
37du type « la tournee la plus proche ». Cette distinction explique
38a elle seule la majorite de l'ecart entre une heuristique artisanale
39et une methode structuree.
40''"
41meilleure = None
42for t in tournees:
43if t.vehicule == 0 and commande.identifiant != tournees[0].commandes[0].identifiant:
44continue
45charge = sum(c.quantite for c in t.commandes) + commande.quantite
46if charge > capacite:
47continue
48points = [depot] + t.commandes
49for pos in range(1, len(points) + 1):
50avant = points[pos - 1]
51apres = points[pos] if pos < len(points) else depot
52gain = (t.cout_arcs(avant, apres)
53- t.cout_arcs(avant, commande)
54- t.cout_arcs(commande, apres))
55if meilleure is None or gain < meilleure[0]:
56meilleure = (gain, t, pos, avant, apres)
57if meilleure is None:
58return False
59_, t, pos, avant, apres = meilleure
60t.commandes.insert(pos - 1, commande)
61t.distance += t.cout_arcs(avant, commande) + t.cout_arcs(commande, apres) \
62- t.cout_arcs(avant, apres)
63return True
64
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
17
65
66def evaluer(tournees, commandes, depot):
67''"Mesure la faisabilite, et non seulement le cout.
68
69Une solution qui viole une fenetre horaire n'est pas une solution
70moins bonne : c'est un plan inexecutable. Le retour doit donc
71distinguer les deux, sinon la recherche convergera vers l'infaisable.
72''"
73index = {c.identifiant: c for c in commandes}
74total, violations, retard = 0.0, 0, 0.0
75for t in tournees:
76t.fin = 0.0
77precedent = depot
78for c in t.commandes:
79total += t.cout_arcs(precedent, c)
80t.fin += t.cout_arcs(precedent, c) + c.service
81if t.fin < c.ouverture:
82t.fin = c.ouverture
83if t.fin > c.fermeture:
84violations += 1
85retard += t.fin - c.fermeture
86precedent = c
87total += t.cout_arcs(precedent, depot)
88return total, violations, retard
Calibrer un plan de tournées en cinq paramètres
• Prix du temps d'attente. Coût horaire du chauffeur, coût d'une promesse non tenue. C'est ce prix qui décide si
une fenêtre horaire vaut la peine d'être respectée.
2. Pénalité de violation, en cascade. Un dépassement de cinq minutes ne coûte pas la même chose qu'un
dépassement de deux heures. Une pénalité linéaire produit des plans absurdes aux extrémités.
3. Durée de service réelle par point. Estimée par catégorie de commerce, pas par défaut unique. C'est le
paramètre le plus souvent sous-estimé, et il déplace tous les horaires.
4. Temps de trajet par période. La matrice de coûts n'est pas statique : le même trajet coûte trois fois plus aux
heures de pointe. Une matrice unique produit un plan faux huit heures par jour.
5. Part de commandes àHoraire souple. En pratique, un dixième des clients acceptent une fenêtre élargie. Ce
dixième vaut souvent plus que n'importe quelle amélioration d'algorithme.
Astuce
La matrice de coûts doit être reconstruite, pas seulement interpolée. Les temps de trajet réels par arc, appris sur
les historiques de position, valent plus qu'une matrice théorique multipliée par un coefficient horaire global : le
facteur d'encombrement n'affecte pas tous les arcs de la même façon.
Exercice 1.4.1  (difficulte : Moyen)
Un plan de tournées optimise sur une matrice de temps statiques réduit la distance parcourue de 12 %. En
exécution, le temps de conduite réel est supérieur de 19 % à celui prévu, et le taux de livraisons hors fenêtre
passe de 4 % à 17 %. Proposer trois corrections, classées par rapport effort / bénéfice attendu.
Indice : Le gain théorique et le gain réel ne sont pas le même chiffre : l'écart vient de la matrice, pas du
solveur.
Correction
• 1. Matrice de coûts horaire, reconstruite à partir des temps réellement constatés par arc et par tranche horaire.
C'est la correction de loin la plus rentable, et elle ne demande aucun changement d'algorithme. 2. Pénalité de
dépassement en cascade plutôt que linéaire, qui rend le solveur honnête sur les cas extrêmes. 3. Réduction du
taux de hors-fenêtre par renégociation commerciale — dix pour cent des clients élargissent leur fenêtre — ce
qui coûte rien en temps de calcul et rend le problème réellement plus facile. Le solveur, lui, n'est en aucun cas
le problème.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
18
A retenir
• Le problème de tournées n'a pas de solution exacte au-delà de quelques dizaines de points : c'est une propriété
démontrée, pas une faiblesse de méthode.
• Une solution qui viole une fenêtre horaire n'est pas une solution moins bonne, c'est un plan inexécutable.
• La matrice de coûts horaire, reconstruite sur des temps réellement constatés, corrige plus de gain que tout
algorithme.
• Le prix du temps d'attente est le paramètre qui décide si une contrainte horaire vaut la peine d'être respectée.
Chapitre 1.5
Ordonnancement et pilotage d'atelier
Un atelier est un graphe. Le dire change ce qu'on peut apprendre, et ce qu'on peut garantir.
Figure 1 — Ordonnancement : la même charge, trois critères, trois plans
Un atelier de fabrication se décrit naturellement comme un graphe : les nœuds sont les opérations et les
machines, les arêtes sont les contraintes de précédence d'une part et de partage de ressource d'autre part.
Cette description n'est pas une commodité : elle détermine ce qu'un modèle d'apprentissage peut
apprendre, et ce qu'un solveur peut garantir.
C = maxj ≤ft Cj-1, maxk ∈ 0(j) ≤ft( Skj + Ck ) , Rj = dj - Cj
(R.5)
La première expression est la règle de Wheeler : la complétion d'une opération est le maximum entre son début
au plus tôt et la fin de toutes ses antécédentes. C'est l'algorithme glouton exact pour un atelier à une machine
par station, et il est faux dès qu'une opération dispose de plusieurs machines. La seconde est le retard, qui est la
grandeur qu'on optimise réellement.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
19
Critère
Formulation
Plan obtenu
Limite
Temps de cycle total
minimiser le makespan
peu d'attente, lots regroupés
ignore totalement les promesses
Retard total
minimiser ∑j Rj
les commandes urgentes passent
d'abord
peut sacrifier une commande pour en
sauver dix
Retard maximal
minimiser maxj Rj
aucune 
commande 
n'est
abandonnée
plus instable, sensible à l'ordre
d'entrée
Capacité utilisée
maximiser le taux d'occupation
machines saturées en permanence
rare : aucune machine n'est jamais à
100 % utile
Tableau 1 — Trois critères d'ordonnancement et ce qu'ils produisent
Trois critères, trois plans différents, pour la même charge. Choisir le critère sans demander au métier est la cause la plus
fréquente de mécontentement sur un ordonnanceur.
• Le graphe de contraintes est un objet de domaine, pas une illustration. Les nœuds sont les
opérations ; les arêtes de précédence sont des invariants durs ; les arêtes de partage sont des relations de
ressource, qui changent avec la disponibilité.
• Les attributs de nœud sont ce qui rend le graphe apprenable. Temps de traitement, attente cumulée,
échéance, et disponibilité de la ressource. Un graphe sans attributs n'apprend que sa topologie, qui ne
change pas d'un tour à l'autre.
• La propagation est la seule information réellement nouvelle. Quand une machine ralentit, ce qui
compte n'est pas le graphe lui-même, mais la façon dont l'information se propage le long des arêtes de
contention. C'est exactement ce que fait un réseau de messages sur graphe.
• La contrainte reste vérifiée par la RO, jamais par l'apprentissage. Le modèle propose un ordre ; un
contrôleur par contraintes vérifie qu'il est réalisable. Confier cette vérification au modèle, c'est lui
demander de garantir ce qu'il n'a pas été conçu pour garantir.
Cadrer un système d'ordonnancement apprenant, en six points
• Décrire l'atelier comme un graphe et figer ce graphe dans un test. Toute évolution ultérieure doit passer ce
test.
2. Séparer les invariants des paramètres. Une précédence est un invariant ; une durée de traitement est un
paramètre. Les mélanger dans un même vecteur d'état empêche tout apprentissage.
3. Choisir la règle de repli avant l'agent. Quelle règle s'applique si le modèle est indisponible ? Cette question
doit avoir une réponse écrite, pas une intuition.
4. Fixer la graine et publier l'écart-type. Un gain annoncé sans intervalle n'est pas un résultat.
5. Définir la mesure de valeur en euros par heure. Sans conversion monétaire, aucun arbitrage n'est possible
entre un gain de 2 % de temps de cycle et une commande sauvée.
6. Prévoir la journalisation de chaque décision. C'est elle qui permettra, dans six mois, de comprendre
pourquoi le performance s'est dégradée après un changement de machine.
Ce que l'apprentissage par graphe n'apporte pas
Un réseau de messages sur graphe apprend la propagation de l'information dans un atelier. Il n'apprend pas la
physique de la machine, pas la disponibilité future d'un opérateur, et pas la durée réelle d'un réglage. Sur un
atelier où les pannes couvrent la moitié du temps, la qualité de la politique est bornée par la qualité de la
description des pannes — et l'apprentissage n'y change rien.
A retenir
• Un atelier est un graphe : les nœuds sont les opérations, les arêtes sont les précédences et les contentions.
• Trois critères d'ordonnancement produisent trois plans différents pour la même charge : le choisir est un acte
de gestion.
• La règle de Wheeler est exacte à une machine par station, et fausse dès qu'une opération a le choix.
• Apprendre la propagation de l'information ne dispensé pas de décrire correctement le domaine.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
20
• La vérification des contraintes reste à la programmation par contraintes, jamais au modèle.
Chapitre 1.6
Énergie, finance et déploiement en
production
Un système hybride en production a deux dérives : celle des données, et celle du modèle. Elles se
mesurent différemment.
Les deux secteurs les plus contraintes chimiquement imposent la même discipline : la prévision de
production et de consommation pour l'énergie, l'espérance de rendement et la matrice de covariance pour
la finance. Dans les deux cas, la décision d'optimisation est un arbitrage permanent entre rendement et
risque, et l'apprentissage n'intervient que sur l'estimation de ces deux grandeurs.
Réseaux électriques
Portefeuilles financiers
Incertitude dominante
production renouvelable
évolution des cours
Contrainte dure
équilibre offre et demande, en continu
interdits de vente à découvert, liquidité
Structure de décision
intégration sur horizon glissant
allocation fractionnaire sous contraintes
Horizon d'engagement
minutes à un jour
jours à plusieurs années
Coût d'une erreur
défaillance généralisée, en cascade, en cascade
insolvabilité, perte de confiance
Ce que l'IA apporte
prévision à court terme, courtage
espérance de rendement, corrélations
Ce que la RO apporte
respect de l'équilibre, faisabilité
respect des contraintes, liquidité
Tableau 1 — Énergie et finance : mêmes principes, contraintes différentes
La ligne des contraintes dures est la plus instructive. Dans les deux cas, l'optimiseur ne peut pas produire une solution qui
viole l'équilibre électrique ou l'interdit de vente, quel que soit le rendement annoncé.
maxmathbfw boldsymbolμ⊤ mathbfw - (λ)/(2) mathbfw⊤ boldsymbolΣ mathbfw, mathbf1⊤
mathbfw = 1, mathbfw ≥ 0
(R.6)
La matrice de covariance est le paramètre estimé, et c'est le seul. Une erreur sur la moyenne de rendement
produit un écart faible ; une erreur sur la covariance produit un portefeuille diversified autrement, et l'erreur est
systématique car elle se reproduit à chaque réallocation.
• Séparer la couche prédictive de la couche d'optimisation. La première est rapide et sans état ; la
seconde est lente et coûteuse. Les exécuter dans le même processus rend le premier indisponible quand
le second est lent.
• Pré-calculer les scénarios. Les scénarios de demande ne sont pas des inconnues à chaque appel : ce
sont des scénarios. Les pré-calculer, et ne conserver en mémoire que ceux qui survivent à un filtre de
faisabilité, divisé le temps de réponse d'un ordre de grandeur.
• Règle de repli explicite. Un algorithme glouton et un ordonnancement statique sont disponibles. Les
écrire avant d'en avoir besoin est la seule façon qu'ils fonctionnent le jour où le modèle tombe.
• Surveiller deux dérives séparément. La dérive des données change ce que le modèle prédit ; la dérive
du modèle change ce que le solveur considère comme possible. Elles ont des signatures différentes et des
causes disjointes.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
21
Rendre un système hybride défendable, cinq contrôles
• Régret mesuré en euros, par période et par segment. C'est le seul chiffré qui rapproché le travail technique
de la décision d'investissement.
2. Écart-type sur trois graines minimum. Une amélioration inférieure à l'écart-type n'est pas une amélioration.
3. Test hors échantillon sur une période de production réelle. Pas sur un jeu de validation, jamais.
4. Règle de repli testée en panne simulée. Une règle de repli jamais exercée est une règle de repli inexistante.
5. Journal de décision exportable. Qui, quand, quelle recommandation, quelle exécution, quel coût constaté.
Sans ce journal, aucun audit n'est possible et aucune amélioration n'est attribuable.
Cadre juridique de l'aide à la décision automatisée
Un système qui recommande une allocation financière, un ordonnancement ou un approvisionnement
assisted-conserve plusieurs obligations. Les recommendations destinées à des clients doivent être identifiables
comme telles. Les décisions à effet juridique ou financier engagent une obligation d'information et
d'explicabilité, et relèvent de la réglementation sectorielle applicable. La conservation des journaux de
recommandation et d'exécution est une condition de conformité, pas une fonctionnalité optionnelle. Un système
hybride n'échappe à aucune de ces obligations par le fait qu'il soit semi-automatique : la part laissée à l'humain
ne change rien à la responsabilité de l'exploitant.
Astuce
La métrique d'un système hybride n'est jamais la qualité de son modèle. C'est l'écart entre le coût de la meilleure
décision possible et le coût réellement payé, par segment. Cette seule mesure permet de décider si le prochain
jour d'effort produit de la valeur.
Projet — Concevoir et cadrer un module de décision hybride
Duree : 6 semaines | Equipe : 3 a 5 etudiants | Depot : gitlab + rapport
Une entreprise de distribution souhaité ses coûts de kilomètre de 12 % en six mois, sans recruter. Elle
dispose d'un an d'historique de tournées, d'un service web interne, et d'une équipe de trois développeurs.
Missions
1. Décrire le problème d'optimisation : variables de décision, contraintes dures, contraintes souples, et
critère de coût.
2. Lister les grandeurs du modèle et les classer par sensibilité de la solution, en justifiant le classement par
une mesure.
3. Formuler la politique de prévision retenue, en indiquant ce qu'elle estime et ce qu'elle délègue à
l'optimiseur.
4. Écrire la règle de repli, et décrire le test qui démontrera qu'elle fonctionne en panne simulée du modèle.
5. Définir la métrique de valeur et le protocole de mesure : regret, période, segments, nombre de graines.
6. Écrire le plan de mise en service parallèle : durée, critère de bascule, et conduite en cas d'écart
défavorable.
Livrables
• N
• o
• t
• e
• d
• e
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
22
• c
• a
• d
• r
• a
• g
• e
• e
• n
• d
• i
• x
• p
• a
• g
• e
• s
• ,
• t
• a
• b
• l
• e
• a
• u
• d
• e
• s
• e
• n
• s
• i
• b
• i
• l
• i
• t
• é
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
23
• d
• e
• s
• p
• a
• r
• a
• m
• è
• t
• r
• e
• s
• ,
• p
• r
• o
• t
• o
• c
• o
• l
• e
• d
• e
• m
• e
• s
• u
• r
• e
• d
• u
• r
• e
• g
• r
• e
• t
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
24
• ,
• r
• è
• g
• l
• e
• d
• e
• r
• e
• p
• l
• i
• t
• e
• s
• t
• é
• e
• ,
• p
• l
• a
• n
• d
• e
• b
• a
• s
• c
• u
• l
• e
• .
Évaluation
• L
• e
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
25
• j
• u
• r
• y
• v
• é
• r
• i
• f
• i
• e
• t
• r
• o
• i
• s
• p
• o
• i
• n
• t
• s
• :
• l
• e
• c
• l
• a
• s
• s
• e
• m
• e
• n
• t
• d
• e
• s
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
26
• e
• n
• s
• i
• b
• i
• l
• i
• t
• é
• e
• s
• t
• j
• u
• s
• t
• i
• f
• i
• é
• p
• a
• r
• u
• n
• e
• m
• e
• s
• u
• r
• e
• ,
• l
• a
• r
• è
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
27
• g
• l
• e
• d
• e
• r
• e
• p
• l
• i
• a
• é
• t
• é
• e
• x
• e
• r
• c
• é
• e
• ,
• e
• t
• l
• e
• p
• r
• o
• t
• o
• c
• o
• l
• e
• a
• n
• n
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
28
• o
• n
• c
• e
• u
• n
• i
• n
• t
• e
• r
• v
• a
• l
• l
• e
• d
• e
• c
• o
• n
• f
• i
• a
• n
• c
• e
• p
• l
• u
• t
• ô
• t
• q
• u
• '
• u
• n
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
29
• g
• a
• i
• n
• p
• o
• n
• c
• t
• u
• e
• l
• .
A retenir
• Un système hybride a deux dérives distinctes, aux signatures disjointes : la dérive des données et la dérive du
modèle.
• La covariance et la production renouvelable sont les paramètres les plus critiques, parce que leur erreur est
systématique.
• Une règle de repli jamais exercée est une règle de repli inexistante : il faut la tester en panne simulée.
• La métrique d'un système hybride est le regret, mesuré en valeur économique et par segment.
• La semi-automatisation ne réduit aucune obligation de conformité ni de traçabilité.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
30
Abréviations, notation et ressources de consultation
Annexes
Annexes
Ce cours se termine par deux annexes de référence. La première donne la signification de chaque sigle
employé, sous les deux formes — sigle et développé — car la litterature emploie indifféremment l'une
ou l'autre. La seconde donne la signification de chaque symbole mathématique : elle permet de relire
une démonstration sans revenir au chapitre dont elle est extraite, et de vérifier qu'un même symbole
garde le même sens d'un chapitre à l'autre.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
31
Chapitre A.1
Liste des abréviations
Les sigles ci-dessous sont ceux que le cours emploie. Chacun est donné avec sa forme développée
et le sens précis qu'il prend ici, qui n'est pas toujours celui qu'on lui donne ailleurs.
Un sigle employé sans être développé oblige le lecteur à le reconnaître au passage, ou à l'abandonner. Le
tableau ci-dessous ferme la liste de ceux que le cours emploie : il est exhaustif pour ce document, et non
pour la discipline.
Sigle
Forme développée
Sens dans ce cours
GAP
Écart de relaxation
Écart relatif entre la borne inférieure et la solution entière.
LP
Linear Programming
Programmation linéaire : optimisation d'un critère linéaire sous
contraintes linéaires.
MILP
Mixed-Integer Linear Programming
Programmation linéaire à variables entières et continues.
NP
Non-Polynomial time
Classe de complexité des problèmes dont on ignore l'appartenance à P.
PDDL
Planning Domain Definition Language
Langage de description de problèmes de planification.
RO
Recherche opérationnelle
Optimisation de décisions sous contraintes.
SPFA
Shortest Path Faster Algorithm
Algorithme de plus court chemin fondé sur une file d'attente.
TCD
Taux de couverture de la demande
Part des demandes servies dans le délai imparti.
VRP
Vehicle Routing Problem
Tournées d'une flotte de véhicules qui livrent une demande dispersée.
Tableau 1 — Abréviations employées dans le cours
Chapitre A.2
Table de notation
Les symboles ci-dessous gardent le même sens d'un chapitre à l'autre. Lorsqu'un chapitre doit
réemployer un symbole pour un autre objet, il le redéclare sur la page même.
La notation est celle du cours : vecteurs en gras, matrices en majuscules grasses, scalaires en italique. Les
espérances sont notées E, les lois de données D, les espaces de paramètres Θ.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
32
Symbole
Signification
xj
Quantité de la variable de décision j.
cj
Coefficient de coût unitaire de la variable j.
aij
Coefficient de la contrainte i pour la variable j.
bi
Second membre de la contrainte i.
m
Nombre de contraintes.
n
Nombre de variables de décision.
c⊤ x
Critère à minimiser ou à maximiser.
Ax ≤ b
Ensemble des contraintes linéaires.
x ∈ ℤ_+n
Variables entières positives ou nulles.
ui
Variable d'écart de la contrainte i.
z*
Valeur optimale du critère.
LP
Valeur optimale de la relaxation linéaire.
IP
Valeur optimale du problème entier.
GAP = (LP - IP)/(IP)
Écart relatif de relaxation.
pi
Probabilité de réalisation du scénario i.
dij
Distance entre les sites i et j.
T
Durée de l'horizon de planification.
Tableau 1 — Symboles mathématiques et leur signification
Convention
Toute divergence constatée entre cette table et un chapitre signale une erreur de transcription, non une
définition nouvelle : la table fait foi.
A retenir
• Un sigle employé sans être listé ici est un oubli de l'auteur, non une définition nouvelle.
• Un symbole qui change de sens d'un chapitre à l'autre rend toute démonstration ininterprétable : c'est la
principale cause des contresens que nous avons relevés.
• Ces deux tables sont les seules parties du cours à maintenir à la main : le reste se relit tout seul.
Index des figures et des tableaux
Référence rapide du matériel visuel
Figures
1.  Deux compétences complémentaires, et la couture entre les deux
1.  Prédire puis optimiser : où la prédiction devient un pari
1.  Apprentissage par renforcement : la boucle, et son point faible
1.  Le problème de tournées : un graphe qui ne se résout pas
1.  Ordonnancement : la même charge, trois critères, trois plans
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
33
Tableaux
1.  Ce que chacune des deux disciplines sait faire et ignorant
1.  Ce qu'il faut mesurer à chaque étage
1.  Les solveurs et ce qu'ils garantissent
1.  Trois critères d'ordonnancement et ce qu'ils produisent
1.  Énergie et finance : mêmes principes, contraintes différentes
1.  Abréviations employées dans le cours
1.  Symboles mathématiques et leur signification
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
34
Fin du document
Intelligence Artificielle Avancée & Federated Learning — Fondations mathématiques de
l'apprentissage automatique, algorithmes fédérés, protection de la vie privée, défense contre les attaques,
grands modèles de langage fédérés, systèmes embarqués, renforcement appris, applications critiques
(santé, V2X), plateforme de référence FedX et feuille de route de recherche.<br/>Ghiloufi Jamel,
Architecte Logiciel Principal — Pixel Software Design<br/>Département de Recherche & Développement
— Recherche<br/>Pixel Software Design — Édition 2026
© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou
diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans
autorisation écrite préalable de l'auteur.
Document généré automatiquement le 29/09/2026 — mise en page Pixel Software Design.
"""


INGENIERIE_IA_TEXT = r"""Pixel Software Design — Département de Recherche & Développement
PIXEL SOFTWARE DESIGN
Département de Recherche & Développement
Intelligence Artificielle
Avancée
& Federated Learning
•  Fondations de l'intelligence artificielle
•  Algorithmes d'apprentissage fédéré
•  Confidentialité, attaques et défenses
•  Applications et grands modèles fédérés
•  Framework FedX de référence
•  Nouveaux fronts de recherche
•  Travaux pratiques, projets et évaluation
Auteur
Ghiloufi Jamel
Fonction
Architecte Logiciel Principal
Direction
Département de Recherche & Développement
Service
R&D - Intelligence Artificielle Avancée & Apprentissage Fédéré
Niveau
Recherche
Édition
Édition 2026 — 1.0
Copyright
© Pixel Software Design
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou
diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans
autorisation écrite préalable de l'auteur.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
2
Copyright et mentions légales
Éditeur
Pixel Software Design
Auteur
Ghiloufi Jamel
Fonction
Architecte Logiciel Principal
Département
Département de Recherche & Développement
Intitulé
Intelligence Artificielle Avancée & Federated Learning
Sous-titre
Fondations mathématiques de l'apprentissage automatique, algorithmes fédérés,
protection de la vie privée, défense contre les attaques, grands modèles de langage
fédérés, systèmes embarqués, renforcement appris, applications critiques (santé,
V2X), plateforme de référence FedX et feuille de route de recherche.
Édition
Édition 2026 (version 1.0)
Langue
Français
Niveau
Recherche
Collection
Supports de formation et de recherche, Pixel Software Design
Droits d'auteur
© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation
ou diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite
sans autorisation écrite préalable de l'auteur.
Droits de l'auteur. Ghiloufi Jamel est l'auteur unique de l'ensemble du contenu scientifique, pédagogique et
technique de cet ouvrage. Toute adaptation, traduction, reproduction ou exploitation, y compris partielle, requiert
une autorisation écrite préalable.
Droits des tiers. Les algorithmes, modèles et travaux cités restent la propriété de leurs auteurs respectifs. Les
références employées figurent en fin d'ouvrage, ce qui permet de remonter au travail original pour toute
affirmation chiffrée.
Marques et licences externes. PyTorch, TensorFlow, Flower, Opacus, MONAI, scikit-learn et PySyft sont des
logiciels libres sous licences respectives (BSD, Apache 2.0, MIT). Leur usage dans ce document est purement
pédagogique et n'emporte aucune prescription commerciale.
Mentions relatives aux données et aux expérimentations
Document pédagogique à usage de formation interne. Les exemples de code fournis sont livrés à titre pédagogique
; les résultats numériques illustrés sont issus d'expérimentations conduites dans un cadre de recherche et ne
constituent pas des performances de production.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
3
Ce support synthétise les travaux de recherche du Département de Recherche & Développement de Pixel Software
Design sur l'intelligence artificielle distribuée, l'apprentissage fédéré, la protection de la vie privée et les systèmes
embarqués intelligents.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
4
Sommaire
Structure détaillée du cours
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 8
Partie 1 — Ingénierie de l'IA : intégration, théorie et applications
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 9
1.1 Le développement et l’intégration logicielle
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 12
1.2 Théorie et algorithmes fondamentaux
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 14
1.3 Applications pratiques et cas d'usage
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 16
1.4 Fiche des abréviations clés
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 19
Annexes
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 20
A.1 Liste des abréviations
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 21
A.2 Table de notation
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
5
Partie
Thème
Contenu
Compétence visée
Durée
Partie 1
Fondations
Statistique, optimisation, courbes d'apprentissage
Comprendre et formaliser
2-3 semaines
Partie 2
Algorithmes FL
FedAvg, convergence, hétérogénéité, système
Implémenter et régler
3-4 semaines
Partie 3
Confidentialité
DP, attaques, défenses, agrégation sécurisée
Auditer et sécuriser
2-3 semaines
Partie 4
Applications
FedLLM, santé, V2X, FedRL, TinyML, graphes
Transposer à un domaine
3-4 semaines
Partie 5
Framework FedX
Architecture, API, benchmarks, exploitation
Industrialiser
2 semaines
Partie 6
Nouveaux fronts
FedCL, FedCI, SNN, FedGL, feuille de route
Ouvrir la recherche
2 semaines
Partie 7
TP et projets
9 labs, 5 projets, corrigés, évaluation
Faire et rendre
4-6 semaines
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
6
Préface
Comment utiliser ce cours
Ce support est conçu pour un parcours de formation et de recherche couvrant l'ensemble de la chaîne de valeur de
l'intelligence artificielle distribuée : les fondations mathématiques, les algorithmes d'apprentissage fédéré, les
menaces et défenses, les applications de pointe, une plateforme de référence opérationnelle, et enfin les nouveaux
fronts ouverts par la recherche du Département.
Ce n'est pas un manuel de référence à lire d'un trait : c'est un manuel opératoire. Chaque chapitre alterne
exposition, formalisation, mise en œuvre numérique et évaluation. Les listings sont complets et exécutables ; les
tableaux comparatifs servent de grille de décision ; les schémas d'architecture servent de support de revue de
conception.
Public et prérequis
Le contenu s'adresse à des étudiants de master et de doctorat, à des ingénieurs IA et à des praticiens de la
recherche appliquée. Les prérequis sont la connaissance de l'apprentissage automatique classique, de
l'algorithmique numérique et des bases de probabilités. Les parties 1 à 3 sont auto-suffisantes pour un étudiant qui
découvre le domaine ; les parties 4 à 7 supposent la mécanique et les outils présentés dans la partie 2.
Conventions de lecture. Une expression mathématique est encadrée par deux signes dollars ; un identifiant, un
fichier ou une commande est écrit en caractères à chasse fixe ; les encadrés Définition, Théorème, Méthode et
Attention signalent les points à maîtriser et les pièges fréquents. Les renvois de la forme « voir chapitre 3.2 »
désignent le second chapitre de la troisième partie.
Progression pédagogique
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
7
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
8
Brancher un modèle dans un logiciel, choisir un algorithme, livrer un cas
d'usage
Partie 1
Ingénierie de l'IA : intégration,
théorie et applications
Ce cours est le versant opérationnel de l'intelligence artificielle. Il suppose le cours d'introduction et
traité de trois questions concrètes : comment brancher un modèle dans une application sans en
devenir prisonnier, comment choisir un algorithme sans laboratoire de recherche, et comment livrer
un cas d'usage qui tient debout en production.
Objectifs de la partie
• Choisir entre API du nuage, exécution locale et architecture hybride, et justifier le choix.
• Mettre en œuvre une génération augmentée par récupération, y compris ses garde-fous.
• Relier une famille d'algorithmes à une structure de données.
• Construire un cas d'usage avec un critère de succès mesurable et une porte de sortie.
• Lire et écrire les abréviations du domaine sans hésitation.
Plan de la partie
1.  Le développement et l’intégration logicielle
2.  Théorie et algorithmes fondamentaux
3.  Applications pratiques et cas d’usage
4.  Fiche des abréviations clés
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
9
Chapitre 1.1
Le développement et l’intégration logicielle
Le choix d'intégration détermine le coût, la latence, la confidentialité et la liberté de
remplacement. Il se prend une fois et se paie longtemps.
Figure 1 — Trois chemins d'intégration d'un modèle et leurs contextes d'usage
Consommer une API du nuage
C'est le chemin le plus rapide : une requête HTTP, un corps de requête en JSON, une réponse en JSON. Il
permet d'utiliser un modèle très supérieur à ce que l'on pourrait entraîner, sans aucun investissement
matériel.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
10
1import os
2import time
3import httpx
4from dataclasses import dataclass
5
6# --- configuration : rien de secret dans le depot ---------------------
7BASE_URL = os.environ["LLM_BASE_URL"]
8API_KEY = os.environ["LLM_API_KEY"]
9MODELE = os.environ.get("LLM_MODELE", "gpt-4o-mini")
10
11
12@dataclass
13class Reponse:
14texte: str
15jetons_entree: int
16jetons_sortie: int
17duree_s: float
18
19
20def interroger(prompt: str, temperature: float = 0.0,
21jetons_max: int = 800, tentatives: int = 3) -> Reponse:
22''"Appel HTTP robuste : delai maximal, reprise, backoff exponentiel.
23
24Trois defaillances sont traitees explicitement : le delai depasse, la
25limitation de debit, et l'erreur transitoire du service distant.
26''"
27charge = {
28"model": MODELE,
29"messages": [{"role": "user", "content": prompt}],
30"temperature": temperature,
31"max_tokens": jetons_max,
32}
33entetes = {"Authorization": "Bearer %s" % API_KEY
34"Content-Type": "application/json"}
35
36for essai in range(tentatives):
37debut = time.monotonic()
38try:
39r = httpx.post(BASE_URL + "/chat/completions", json=charge,
40headers=entetes, timeout=30.0)
41if r.status_code == 429: # trop de requetes
42time.sleep(min(8.0, 0.5 * 2 ** essai))
43continue
44r.raise_for_status()
45corps = r.json()
46usage = corps.get("usage", {})
47return Reponse(
48texte=corps["choices"][0]["message"]["content"],
49jetons_entree=usage.get("prompt_tokens", 0),
50jetons_sortie=usage.get("completion_tokens", 0),
51duree_s=time.monotonic() - debut,
52)
53except (httpx.TimeoutException, httpx.TransportError):
54time.sleep(0.5 * 2 ** essai)
55raise RuntimeError("service indisponible apres %d tentatives" % tentatives)
Listing 1 — Appel d'API robuste : delai maximal, reprise et backoff
• Avantage : mise en service en quelques heures, accès aux meilleurs modèles, montée en charge
immédiate.
• Inconvénient : dépendance à l'éditeur, coût par requête, données qui sortent de l'organisation.
• Risque principal : la Shoulder.ApiKey dans le code. Elle se lit dans un journal d'erreur bien plus souvent
qu'on ne l'imagine.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
11
Écrire toute la logique métier autour du format de réponse d'un fournisseur rend le remplacement
ultérieur très coûteux. La parade est simple et peu coûteuse : placer tous les appels derrière une interface
interne unique, Modèle ou Fournisseur, et n'exposer au reste du code que trois méthodes — completer,
generer_structure, classer.
Le piège du couplage précoce
Exécuter le modèle en local
L'exécution locale vise trois objectifs : la confidentialité des données, la continuité de service hors réseau, et
l'absence de coût marginal par requête. Elle se paie par la gestion du matériel et par la mise à jour du parc.
Critère
Nuage
Local
Hybride
Délai de mise en service
heures
jours
semaines
Coût marginal
par requête
nul après amortissement
mixte
Confidentialité
dépendance de l'éditeur
totale
partielle ou totale
Fonctionnement hors ligne
non
oui
partiel
Qualité accessible
la meilleure
modérée
les deux
Charge d'exploitation
faible
élevée
élevée
Indépendance fournisseur
faible
totale
moyenne
Tableau 1 — Comparaison des modes d'exécution
Le mode hybride est rarement un compromis mou : dans la pratique, on aiguille — traitement courant en local, demande
complexe au nuage, donnée sensible jamais transmise.
Architecture hybride et résilience
Une application hors ligne doit être conçue, pas négociée après coupure. La règle est que la base locale fasse
autorité pour l'affichage, et que le serveur ne soit qu'une source de synchronisation.
Algorithme 1 — Synchronisation hors ligne
01  L'écriture se fait d'abord dans la base locale, avec un identifiant uniqueLa transaction
locale est validée immédiatement pour l'utilisateur
02  Un journal local conserve les opérations en attente de synchronisation
03  Au retour du réseau, les opérations sont rejouées dans l'ordre de leur création
04  En cas de conflit, la version du serveur l'emporte et l'écart est journalisé
05  L'interface signale a l'utilisateur ce qui n'est pas encore synchronise
Entrées : Journal local des opérations, état du serveur • Sorties : Base locale à jour, écart de synchronisation
connu • Complexité : O(n) en nombre d'opérations en attente
La ligne 5 est la seule difficile : sans règle de conflit explicite, deux appareils convergent vers des états
différents, et le bug n'apparaît que chez l'utilisateur.
Le motif de génération augmentée par récupération
C'est le motif central de l'intégration d'entreprise. Il consiste à ne jamais demander au modèle de connaître
une information : on lui fournit les passages pertinents au moment de la question.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
12
Algorithme 2 — Cycle d'une question en génération augmentée
01  Reformuler la question en requête de recherche documentaireRechercher les passages proches
dans la base vectorielle
02  Filtrer par droits d'accès, par date et par source autorisée
03  Assembler les passages retenus, en limitant le volume total
04  Interroger le modèle en exigeant des citations de passages
05  Vérifier que chaque affirmation est rattachee a un passage
06  Renvoyer la réponse et ses références, ou un refus explicite
Entrées : Question, droits d'accès de l'utilisateur, base documentaire • Sorties : Réponse sourcée, ou refus
motivé • Complexité : Recherche vectorielle sous quelques dizaines de millisecondes
L'étape 7 n'est pas décorative : un système qui répond à tout, même quand il ne sait pas, est plus dangereux
qu'un système qui ne répond pas.
La base vectorielle n'est pas une base de connaissances
La similarité vectorielle mesure une ressemblance de formulation, pas une pertinence factuelle. Un document
sur les « taux d'intérêt » peut être retenu pour une question sur le « taux d'usure ». Le découpage des documents,
l'indexation et le filtrage pèsent autant que le modèle lui-même.
Astuce
Le meilleur indicateur de disponibilité d'un système d'IA n'est pas la qualité de la réponse, c'est la capacité à
dire qu'il ne sait pas. Mesurez le taux de refus justifiés : un système qui refuse trop est utilisable, un système
qui répond toujours ne l'est pas.
A retenir
• Le mode d'intégration se décide sur la latence, la confidentialité et le budget, pas sur la qualité du modèle.
• Tous les appels doivent passer par une interface interne unique, pour rester remplaçable.
• L'hybride n'est pas un compromis mou : il se met en œuvre par aiguillage.
• La génération augmentée impose de concevoir le refus comme un comportement normal.
Chapitre 1.2
Théorie et algorithmes fondamentaux
Le choix d'un algorithme découle de la structure des données, jamais du résultat souhaité.
Figure 1 — La carte des algorithmes et la structure de données attendue
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
13
Régression linéaire et logistique
Ce sont les deux premiers modèles à essayer systématiquement, même sur un problème qui semble
complexe. Une régression linéaire ajuste une droite ; la logistique ajuste une probabilité. Toutes les deux
s'entraînent par descente de gradient.
w* = argminw (1)/(m) ∑i=1
m ≤ft(yi - w⊤ xi)2 + λ ‖ w ‖2
P(Y=1 | x) = σ≤ft(w⊤ x + b), σ(z) = (1)/(1+e-z)
(E.1)
Le terme λ ‖ w ‖2 est la régularisation : sans elle, le modèle explose sur des variables corrélées. C'est le premier
réflexe à prendre.
• Quand : données tabulaires, peu de variables, besoin d'explicabilité.
• Diagnostic : si une régression logistique est battue par un arbre, l'interaction ou la non-linéarité compte.
• Piège : la multicolinéarité. Elle rend les coefficients instables sans dégrader la prédiction — ne jamais
lire un coefficient comme une causalité.
Arbres de décision et forêts aléatoires
Un arbre de décision pose une suite de questions binaires : à chaque nœud, il choisit la variable et le seuil
qui séparent le mieux les deux groupes restants. Une forêt aléatoire assemble des centaines d'arbres
entraînés sur des tirages différents, et agrège leurs votes.
• Force : aucune normalisation nécessaire, gestion native des valeurs manquantes, interprétabilité directe.
• Force : excellent sur données tabulaires, souvent supérieur à une méthode linéaire en performance.
• Limite : unstable — une petite modification des données change l'arbre. D'où la forêt, qui moyenne cette
instabilité.
• Limite : extrapolation impossible. Un arbre ne sait pas prédire au-delà de la plage observée.
Exemple
La forêt aléatoire est le premier modèle à essayer sur un jeu de données tabulaires. Sur des données textuelles
ou des images, elle est en revanche nettement inférieure à un réseau de neurones : la structure de la grille ou de
la séquence n'est pas représentable par des seuils sur des colonnes.
Réseaux de neurones profonds
Un réseau profond empile des transformations non linéaires. La couche dense est l'unité de base ; la
convolution et l'attention sont des variantes qui exploitent une structure particulière de l'entrée.
Couche
Hypothèse sur les données
Coût dominant
Usage
Droite (MLP)
aucune
paramètresvecteurs,
données tabulaires
Convolution
grille régulière, voisinage local
calcul
images, signaux, audio
Attention
dépendance 
entre 
positions, 
quelle
qu'elle soit
mémoire du cache
texte, audio, vidéo, code
État récurrent
dépendance strictement ordonnée
séquentialité
flux, séries temporelles
Tableau 1 — Les trois familles de couches et la structure qu'elles exploitent
L'hypothèse sur les données est le vrai choix de conception ; l'architecture n'en est que la traduction.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
14
Ordre d'essai recommandé
• Modèle linéaire, comme référence et point de comparaison.
2. Arbre ou forêt, si les données sont tabulaires.
3. Gradient boosting, si le précédent est bon et qu'il reste de la performance à gagner — c'est souvent le
meilleur rapport gain/complexité.
4. Réseau profond, si la donnée est une image, un son, un texte ou une série temporelle.
5. Modèle de langue, si la tâche est du langage ou du raisonnement, et qu'un appel distant est acceptable.
Un projet qui saute l'étape 1 ne peut pas démontrer que son modèle est meilleur que la solution triviale.
A retenir
• Le choix de l'algorithme découle de la structure des données, jamais du résultat attendu.
• Modèle linéaire et forêt aléatoire doivent être essayés en premier sur données tabulaires.
• Les couches denses, convolutives, d'attention et récurrentes correspondent à quatre hypothèses distinctes sur
les données.
• Sans référence linéaire en point de départ, aucune amélioration n'est démontrable.
Chapitre 1.3
Applications pratiques et cas d'usage
Un cas d'usage se démontre par son coût, pas par sa démonstration.
Automatisation des processus et extraction documentaire
Le premier cas d'usage rentable reste l'extraction de données à partir de documents non structurés :
factures, contrats, bulletins, reçus. La valeur est immédiate, mesurable en heures de saisie économisées, et
le risque borné car la sortie est vérifiable par un opérateur.
Étape
Question
Indicateur
Cadrage
quelle décision l'extraction permet-elle ?processus
concerné, périmètre réel
Mesure
combien de documents, quelle erreur tolérée ?
volume quotidien, taux d'erreur acceptable
Évaluation
sur quels documents de référence ?
précision et rappel par champ
Déploiement
qui valide, qui corrige ?
temps humain résiduel par lot
Bilan
le gain net est-il positif ?
heures économisées moins heures de contrôle
Tableau 1 — Évaluation d'un cas d'usage d'extraction
Le dernier indicateur est le seul qui décide : sans lui, un projet d'extraction peut être un perte de temps disguisée en gain.
Analyse prédictive et logistique
Le deuxième cas mature est l'anticipation : ruptures de stock, tournées de livraison, maintenance
d'équipement. La difficulté n'est pas le modèle, mais l_available data : un historique de maintenance
nonexistent ou mal saisi rend la prédiction impossible, quel que soit l'algorithme.
• Maintenance prédictive : surveillance de signaux (vibration, température, courant) et déclenchement
avant défaillance.
• Prévision de demande : historique de ventes, saisonnalité, événements promo_float, arbitrage coût du
stock manquant contre coût du surstock.
• Optimisation de tournées : contraintes de livraison, fenêtres horaires, capacité des véhicules.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
15
La prévision ne se corrige pas toute seule
Un modèle de prévision est juste en moyenne et faux aux moments qui comptent. Une erreur sur le pic de
demande de décembre est incomparablement plus coûteuse qu'une erreur en mars. Il faut donc évaluer le
modèle pondéré par le coût de l'erreur, ce qui est presque toujours absent des évaluations initiales.
Assistants spécialisés et interrogation en langage naturel
Le troisième cas est l'assistant métier capable d'interroger une base relationnelle en langage naturel. C'est
un cas de figure trompeur : la démonstration est spectaculaire, la production est difficile, parce que la
requête générée peut être valide en syntaxe et fausse en sens.
Figure 1 — De la question en langage naturel à la requête
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
16
1import re
2
3MOT_CLES_INTERDITS = re.compile(
4r"$\b(insert|update|delete|drop|alter|truncate|grant|revoke|$"
5r"exec|execute|call|shutdown)\b", re.IGNORECASE)
6
7REGLES = [
8(r"\b(numero de|numero du|n°)\s*client\b", "numero_client"),
9(r"\bprix\b", "prix_unitaire"),
10(r"\b(client|clients)\b", "numero_client"),
11]
12
13
14def securiser(requete_sql: str, max_lignes: int = 500) -> str:
15''"Valide une requete generee avant execution.
16
17Le modele n'est pas fiable : la requete produite peut etre syntaxiquement
18correcte et.sql irrelevante. Ce controle est donc obligatoire, et il
19doit ecrire dans la logique, pas dans la documentation.
20''"
21q = requete_sql.strip().rstrip(";")
22if not q.lower().startswith(("select", "with")):
23raise ValueError("seules les lectures sont autorisees")
24if MOT_CLES_INTERDITS.search(q):
25raise ValueError("instruction non autorisee : %s" % MOT_CLES_INTERDITS.search(q).group(0))
26if ";" in q:
27raise ValueError("plusieurs instructions detectees")
28if not re.search(r"\blimit\s+\d+", q, re.IGNORECASE):
29q += " limit %d" % max_lignes
30return q.replace("select *", "select *"), q
Listing 1 — Garde-fous d'une interrogation en langage naturel
Astuce
La règle qui évite 90 % des incidents d'un assistant de requêtage : le compte de l'utilisateur est toujours lu dans
le référentiel d'autorisations, jamais déduit de ce que le modèle dit. Le modèle propose, l'autorisation tranche.
Checklist de livraison d'un cas d'usage
• Critère de succès écrit, mesurable, avant l'écriture du code.
2. Jeu d'évaluation figé, représentatif, jamais modifié après.
3. Voie de repli : que se passe-t-il si le modèle est indisponible ?
4. Journalisation de chaque appel, avec sa version de modèle et ses paramètres.
5. Retour arrière : une action effectuée doit pouvoir être annulée.
6. Seuil d'abandon : sous quel résultat on arrête le projet ?
7. Bilan chiffré : gain net, coût total, temps de gestion.
A retenir
• L'extraction documentaire reste le cas d'usage le plus rentable parce que sa sortie est vérifiable.
• La prévision doit être évaluée pondérée par le coût de l'erreur, pas en moyenne simple.
• Un assistant de requête en langage naturel exige un contrôle d'autorisation hors du modèle.
• Sans critère de succès écrit ni voie de repli, un projet d'IA n'est pas pilotable.
Chapitre 1.4
Fiche des abréviations clés
Trente termes qui reviennent dans tous les documents du domaine.
La maîtrise du vocabulaire abrégé est ce qui distingue un interlocuteur technique d'un lecteur non
technique. Cette fiche couvre les sigles que l'on rencontre dans les spécifications, les offres d'architecture et
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
17
les comptes rendus de réunion.
Abréviation
Terme anglais
Signification
ADR
Architecture Décision Record
Trace écrite d'une décision d'architecture
AGI
Artificial General Intelligence
Intelligence artificielle générale
API
Application Programming Interface
Interface de programmation entre logiciels
BERT
Bidirectional Encoder Représentations from
Transformers
Encodeur transformateur pré-entraîné
CNN
Convolutional Neural Network
Réseau de neurones convolutif, orienté image
CPython
—
Interpréteur Python de référence
CUDA
Compute Unified Device Architecture
Plateforme de calcul parallèle NVIDIA
DP
Differential Privacy
Confidentialité différentielle
FL
Federated Learning
Apprentissage fédéré
GPU
Graphics Processing Unit
Processeur graphique, accélérateur d'entraînement
KV
Key-Value
Cache d'attention, proportional à la longueur du contexte
LLM
Large Language Model
Modèle de langage de grande taille
ML
Machine Learning
Apprentissage automatique
MLP
Multi-Layer Perceptron
Perceptron multicouche, réseau dense
NLP
Natural Language Processing
Traitement automatique du langage naturel
ONNX
Open Neural Network Exchange
Format d'échange de modèles
RAG
Retrieval-Augmented Génération
Génération augmentée par récupération
RNN
Recurrent Neural Network
Réseau de neurones récurrent
SDK
Software Development Kit
Kit de développement logiciel
SSM
State Space Model
Modèle à espace d'état
SQL
Structured Query Language
Langage de requête pour bases relationnelles
SQLi
SQL Injection
Injection SQL, faille d'injection de requête
SSE
Server-Sent Events
Flux d'événements serveur à sens unique
SSL
Secure Sockets Layer
Couche de sockets sécurisée
TLS
Transport Layer Security
Sécurité de la couche transport
TPS
Tokens Per Second
Débit de génération, en jetons par seconde
VLM
Vision-Language Model
Modèle vision-langage
WebSocket
—
Connexion bidirectionnelle persistante
Tableau 1 — Fiche des abréviations clés en intelligence artificielle
Les sigles se prononcent lettre par lettre à l'anglaise : « C-N-N », pas « cé-ène-ène ». La seule exception courante est « l'API
», que l'on prononce à la française.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
18
Paire
Différence réelle
Conséquence de la confusion
IA faible / IA forte
généraliste contre spécialiséecroire qu'un
modèle est « conscient »
ML / apprentissage profond
le second est un cas du premier
sur-dimensionner un problème simple
Transformer / RNN
parallèle contre séquentiel
estimer à tort le coût d'entraînement
Exactitude / AUC
seuil Optimal contre classement
déclarer 
un 
détecteur 
performant 
sur 
un
déséquilibre
Fuite d'information /
surapprentissage
variable indisponible contre mémorisation
déployer un modèle inutilisable
LLM / modèle de langage
taille contre nature
sur-dimensionner une infrastructure
Tableau 2 — Les confusions les plus fréquentes
Astuce
La règle de lecture la plus rentable en revue technique : remplacer chaque sigle par sa définition en toutes
lettres, puis relire la phrase. Neuf fois sur dix, une ambiguïté apparaît.
A retenir
• Trente abréviations suffisent à couvrir l'essentiel des documents du domaine.
• Une abréviation mal comprise produit une erreur d'architecture, pas une simple incompréhension de
vocabulaire.
• Substituer mentalement la définition en toutes lettres est le meilleur réflexe de relecture.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
19
Abréviations, notation et ressources de consultation
Annexes
Annexes
Ce cours se termine par deux annexes de référence. La première donne la signification de chaque sigle
employé, sous les deux formes — sigle et développé — car la litterature emploie indifféremment l'une
ou l'autre. La seconde donne la signification de chaque symbole mathématique : elle permet de relire
une démonstration sans revenir au chapitre dont elle est extraite, et de vérifier qu'un même symbole
garde le même sens d'un chapitre à l'autre.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
20
Chapitre A.1
Liste des abréviations
Les sigles ci-dessous sont ceux que le cours emploie. Chacun est donné avec sa forme développée
et le sens précis qu'il prend ici, qui n'est pas toujours celui qu'on lui donne ailleurs.
Un sigle employé sans être développé oblige le lecteur à le reconnaître au passage, ou à l'abandonner. Le
tableau ci-dessous ferme la liste de ceux que le cours emploie : il est exhaustif pour ce document, et non
pour la discipline.
Sigle
Forme développée
Sens dans ce cours
ADR
Architecture Decision Record
Fiche qui trace une décision d'architecture et sa justification.
AGI
Artificial General Intelligence
Intelligence artificielle générale.
API
Application Programming Interface
Interface d'échange entre deux logiciels.
AUC
Area Under the Curve
Aire sous la courbe de ROC, mesure synthétique du pouvoir discriminant.
BERT
Bidirectional Encoder Representations
from Transformers
Modèle de représentation contextuelle pré-entraîné.
CNN
Convolutional Neural Network
Réseau convolutif.
CUDA
Compute Unified Device Architecture
Modèle de programmation des accélérateurs graphiques.
DP
Differential Privacy
Vie privée différentielle.
F1
Score F1
Moyenne harmonique de la précision et du rappel.
FL
Federated Learning
Apprentissage fédéré.
GPU
Graphics Processing Unit
Processeur de calcul massivement parallèle.
gRPC
gRPC Remote Procedure Call
Protocole d'appel de procédure distant, fondé sur HTTP/2.
JSON
JavaScript Object Notation
Format d'échange de données textuel.
KV
Key-Value
Cache clé-valeur, usuel pour l'auto-attention.
LLM
Large Language Model
Grand modèle de langage.
MLP
Multi-Layer Perceptron
Réseau de couches entièrement connectées.
NLP
Natural Language Processing
Traitement automatique des langues.
ONNX
Open Neural Network Exchange
Format d'échange de modèles entre frameworks.
RAG
Retrieval-Augmented Generation
Génération augmentée par récupération de documents.
RNN
Recurrent Neural Network
Réseau récurrent.
SSE
Server-Sent Events
Flux d'événements poussé d'un serveur vers un client.
SSL
Secure Sockets Layer
Couche de chiffrement des échanges, normalisée aujourd'hui sous le nom
TLS.
TLS
Transport Layer Security
Chiffrement et authentification du canal de communication.
VLM
Vision-Language Model
Modèle qui traite l'image et le texte conjointement.
Tableau 1 — Abréviations employées dans le cours
Chapitre A.2
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
21
Table de notation
Les symboles ci-dessous gardent le même sens d'un chapitre à l'autre. Lorsqu'un chapitre doit
réemployer un symbole pour un autre objet, il le redéclare sur la page même.
La notation est celle du cours : vecteurs en gras, matrices en majuscules grasses, scalaires en italique. Les
espérances sont notées E, les lois de données D, les espaces de paramètres Θ.
Symbole
Signification
x ∈ ℝd
Observation de dimension d.
f_θ
Modèle paramétré par le vecteur θ.
θ ∈ Θ
Vecteur de paramètres, appartenant à l'espace Θ.
L
Fonction de perte.
L(θ)
Valeur de la perte sur le jeu entier.
J(θ) = (1)/(m)∑i=1
m L(f_θ(xi), yi)
Objectif d'entraînement, à minimiser.
m
Nombre d'exemples du lot courant.
B
Taille du lot d'entraînement.
N
Nombre total d'exemples, données d'évaluation comprises.
n
Nombre d'exemples d'apprentissage seuls.
η
Taux d'apprentissage.
β1
Moyenne mobile du premier moment du gradient.
β2
Moyenne mobile du second moment du gradient.
Terme stabilisateur des divisions, ou budget de vie privée selon le chapitre.
λ
Pondération de la régularisation.
C
Seuil de décision, en classification binaire.
p
Précision d'un détecteur.
r
Rappel d'un détecteur.
TPR
Taux de vrais positifs.
FPR
Taux de faux positifs.
Δ t
Temps de réponse d'un service.
Tableau 1 — Symboles mathématiques et leur signification
Convention
Toute divergence constatée entre cette table et un chapitre signale une erreur de transcription, non une
définition nouvelle : la table fait foi.
A retenir
• Un sigle employé sans être listé ici est un oubli de l'auteur, non une définition nouvelle.
• Un symbole qui change de sens d'un chapitre à l'autre rend toute démonstration ininterprétable : c'est la
principale cause des contresens que nous avons relevés.
• Ces deux tables sont les seules parties du cours à maintenir à la main : le reste se relit tout seul.
Index des figures et des tableaux
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
22
Référence rapide du matériel visuel
Figures
1.  Trois chemins d'intégration d'un modèle et leurs contextes d'usage
1.  La carte des algorithmes et la structure de données attendue
1.  De la question en langage naturel à la requête
Tableaux
1.  Comparaison des modes d'exécution
1.  Les trois familles de couches et la structure qu'elles exploitent
1.  Évaluation d'un cas d'usage d'extraction
1.  Fiche des abréviations clés en intelligence artificielle
2.  Les confusions les plus fréquentes
1.  Abréviations employées dans le cours
1.  Symboles mathématiques et leur signification
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
23
Fin du document
Intelligence Artificielle Avancée & Federated Learning — Fondations mathématiques de
l'apprentissage automatique, algorithmes fédérés, protection de la vie privée, défense contre les attaques,
grands modèles de langage fédérés, systèmes embarqués, renforcement appris, applications critiques
(santé, V2X), plateforme de référence FedX et feuille de route de recherche.<br/>Ghiloufi Jamel,
Architecte Logiciel Principal — Pixel Software Design<br/>Département de Recherche & Développement
— Recherche<br/>Pixel Software Design — Édition 2026
© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou
diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans
autorisation écrite préalable de l'auteur.
Document généré automatiquement le 29/09/2026 — mise en page Pixel Software Design.
"""


ARCHITECTURE_NUMERIQUE_TROIS_NIVEAUX_TEXT = r"""Pixel Software Design — Département de Recherche & Développement
PIXEL SOFTWARE DESIGN
Département de Recherche & Développement
Intelligence Artificielle
Avancée
& Federated Learning
•  Fondations de l'intelligence artificielle
•  Algorithmes d'apprentissage fédéré
•  Confidentialité, attaques et défenses
•  Applications et grands modèles fédérés
•  Framework FedX de référence
•  Nouveaux fronts de recherche
•  Travaux pratiques, projets et évaluation
Auteur
Ghiloufi Jamel
Fonction
Architecte Logiciel Principal
Direction
Département de Recherche & Développement
Service
R&D - Intelligence Artificielle Avancée & Apprentissage Fédéré
Niveau
Recherche
Édition
Édition 2026 — 1.0
Copyright
© Pixel Software Design
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou
diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans
autorisation écrite préalable de l'auteur.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
2
Copyright et mentions légales
Éditeur
Pixel Software Design
Auteur
Ghiloufi Jamel
Fonction
Architecte Logiciel Principal
Département
Département de Recherche & Développement
Intitulé
Intelligence Artificielle Avancée & Federated Learning
Sous-titre
Fondations mathématiques de l'apprentissage automatique, algorithmes fédérés,
protection de la vie privée, défense contre les attaques, grands modèles de langage
fédérés, systèmes embarqués, renforcement appris, applications critiques (santé,
V2X), plateforme de référence FedX et feuille de route de recherche.
Édition
Édition 2026 (version 1.0)
Langue
Français
Niveau
Recherche
Collection
Supports de formation et de recherche, Pixel Software Design
Droits d'auteur
© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation
ou diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite
sans autorisation écrite préalable de l'auteur.
Droits de l'auteur. Ghiloufi Jamel est l'auteur unique de l'ensemble du contenu scientifique, pédagogique et
technique de cet ouvrage. Toute adaptation, traduction, reproduction ou exploitation, y compris partielle, requiert
une autorisation écrite préalable.
Droits des tiers. Les algorithmes, modèles et travaux cités restent la propriété de leurs auteurs respectifs. Les
références employées figurent en fin d'ouvrage, ce qui permet de remonter au travail original pour toute
affirmation chiffrée.
Marques et licences externes. PyTorch, TensorFlow, Flower, Opacus, MONAI, scikit-learn et PySyft sont des
logiciels libres sous licences respectives (BSD, Apache 2.0, MIT). Leur usage dans ce document est purement
pédagogique et n'emporte aucune prescription commerciale.
Mentions relatives aux données et aux expérimentations
Document pédagogique à usage de formation interne. Les exemples de code fournis sont livrés à titre pédagogique
; les résultats numériques illustrés sont issus d'expérimentations conduites dans un cadre de recherche et ne
constituent pas des performances de production.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
3
Ce support synthétise les travaux de recherche du Département de Recherche & Développement de Pixel Software
Design sur l'intelligence artificielle distribuée, l'apprentissage fédéré, la protection de la vie privée et les systèmes
embarqués intelligents.
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
4
Sommaire
Structure détaillée du cours
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 8
Partie 1 — Architecture Numérique à Trois Niveaux
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 9
1.1 Le modèle trois niveaux
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 10
1.2 Le niveau applicatif : serveur, répartition et interpréteur
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 12
1.3 Le niveau de données et le référentiel applicatif
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 13
1.4 L'intégration des modules fonctionnels
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 15
1.5 Transactions, verrous et performances
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 19
1.6 Évolution, migration et architectures de remplacement
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 30
Annexes
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 31
A.1 Liste des abréviations
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 31
A.2 Table de notation
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
5
Partie
Thème
Contenu
Compétence visée
Durée
Partie 1
Fondations
Statistique, optimisation, courbes d'apprentissage
Comprendre et formaliser
2-3 semaines
Partie 2
Algorithmes FL
FedAvg, convergence, hétérogénéité, système
Implémenter et régler
3-4 semaines
Partie 3
Confidentialité
DP, attaques, défenses, agrégation sécurisée
Auditer et sécuriser
2-3 semaines
Partie 4
Applications
FedLLM, santé, V2X, FedRL, TinyML, graphes
Transposer à un domaine
3-4 semaines
Partie 5
Framework FedX
Architecture, API, benchmarks, exploitation
Industrialiser
2 semaines
Partie 6
Nouveaux fronts
FedCL, FedCI, SNN, FedGL, feuille de route
Ouvrir la recherche
2 semaines
Partie 7
TP et projets
9 labs, 5 projets, corrigés, évaluation
Faire et rendre
4-6 semaines
PIXEL SOFTWARE DESIGN
Intelligence Artificielle Avancée & Federated Learning
Ghiloufi Jamel — Architecte Logiciel Principal
6
Préface
Comment utiliser ce cours
Ce support est conçu pour un parcours de formation et de recherche couvrant l'ensemble de la chaîne de valeur de
l'intelligence artificielle distribuée : les fondations mathématiques, les algorithmes d'apprentissage fédéré, les
menaces et défenses, les applications de pointe, une plateforme de référence opérationnelle, et enfin les nouveaux
fronts ouverts par la recherche du Département.
Ce n'est pas un manuel de référence à lire d'un trait : c'est un manuel opératoire. Chaque chapitre alterne
exposition, formalisation, mise en œuvre numérique et évaluation. Les listings sont complets et exécutables ; les
tableaux comparatifs servent de grille de décision ; les schémas d'architecture servent de support de revue de
conception.
Public et prérequis
Le contenu s'adresse à des étudiants de master et de doctorat, à des ingénieurs IA et à des praticiens de la
recherche appliquée. Les prérequis sont la connaissance de l'apprentissage automatique classique, de
l'algorithmique numérique et des bases de probabilités. Les parties 1 à 3 sont auto-suffisantes pour un étudiant qui
découvre le domaine ; les parties 4 à 7 supposent la mécanique et les outils présentés dans la partie 2.
Conventions de lecture. Une expression mathématique est encadrée par deux signes dollars ; un identifiant, un
fichier ou une commande est écrit en caractères à chasse fixe ; les encadrés Définition, Théorème, Méthode et
Attention signalent les points à maîtriser et les pièges fréquents. Les renvois de la forme « voir chapitre 3.2 »
désignent le second chapitre de la troisième partie.
Progression pédagogique
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
7
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
8
Le patron de conception qui underlie tous les systèmes d'entreprise
Partie 1
Architecture Numérique à Trois
Niveaux
Le modèle trois niveaux sépare trois responsabilités qui ont toujours été ICI confondues : ce que
l'utilisateur voit, ce que le logiciel décide, et ce qui est stocké. Cette séparation, formalisée dans les
années 1970, reste la grille de lecture de tous les systèmes d'information d'entreprise, du progiciel
intégré des années 1990 aux platesformes en mémoire et aux services distribués d'aujourd'hui. On
l'étudie ici à travers le cas de référence le plus répandu au monde, puis on en tire les règles qui
permettent de décider où couper.
Objectifs de la partie
• Nommer les trois niveaux, leurs composants et le protocole qui les relie.
• Expliquer le rôle du serveur de répartition et du serveur de messages dans une application d'entreprise.
• Distinguer le référentiel d'une base de données, et comprendre pourquoi il conditionné toute évolution.
• Suivre le parcours complet d'une transaction, du poste de travail à l'écriture en base.
• Justifier un découpage de charge entre plusieurs serveurs sans rompre la cohérence.
• Évaluer une migration vers une plateforme en mémoire : ce qu'elle gagne, ce qu'elle coûte.
Plan de la partie
1.  Le modèle trois niveaux
2.  Le niveau applicatif : serveur, répartition et interpréteur
3.  Le niveau de données et le référentiel applicatif
4.  L'intégration des modules fonctionnels
5.  Transactions, verrous et performances
6.  Évolution, migration et architectures de remplacement
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
9
Chapitre 1.1
Le modèle trois niveaux
Trois responsabilités, trois niveaux remplaçables. Toute la valeur du modèle tient dans cette
phrase.
Le modèle trois niveaux, aussi appelé architecture à trois niveaux ou architecture de présentation, sépare
l'application en une couche de présentation, une couche de traitement et une couche de stockage. L'origine
du découpage est simple : les trois évoluent à des rythmes différents. Un poste de travail se remplace tous
les trois ans, un serveur tous les cinq, une base tous les huit. Les faire évoluer ensemble, c'est remplacer les
trois pour le plus jeune d'entre eux.
Figure 1 — L'architecture trois niveaux et la place de chaque élément
Niveau
Responsabilité
Composants typiquesProtocole vers le
niveau suivant
Présentationcapter
l'action, afficher le
résultat, valider la
saisie
client 
lourd, 
navigateur, 
portail,
terminal
protocole 
de 
dialogue, 
appel 
de
fonction distante, service web
Traitement
appliquer les règles de gestion,
contrôler les droits, orchestrer la base
serveur de répartition, processus de
traitement, serveur de messages
interface 
de 
base 
de 
données,
instruction de contrôle
Données
conserver l'état, garantir l'intégrité,
servir les lectures
moteur 
relationnel, 
stockage,
sauvegardes
interface 
native 
du 
moteur,
procédure stockée
Tableau 1 — Les trois niveaux, leurs responsabilités et leurs protocoles
Le protocole est la vraie frontière. Parce qu'il est normalisé, il permet de remplacer un niveau sans toucher les deux
autres — c'est la définition opérationnelle du couplage faible.
Definition — Couplage faible
Deux composants sont faiblement couplés lorsque l'un peut être remplacé sans que l'autre ait à être modifié.
Dans une architecture trois niveaux, le couplage faible se mesure à la frontière standardisée normalisée qui
sépare chaque couche. Un protocole documenté, stable et indépendant du produit suffit ; c'est la raison pour
laquelle l'appel de fonction distante a remplacé durablement les accès directs au moteur de base de données.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
10
Astuce
Pour vérifier le couplage faible d'un système, posez une seule question : si l'on remplace entièrement le niveau
de données, quelle part du code faut-il réécrire ? Si la réponse est « la totalité », il n'y avait pas d'architecture
trois niveaux, il n'y avait qu'une application avec des couches dessinées.
A retenir
• Le découpage existe parce que les trois niveaux n'évoluent pas au même rythme.
• Le protocole normalisé entre les niveaux est la frontière qui rend le remplacement possible.
• Un système fortement couplé n'a pas trois niveaux : il a trois couches sur une seule application.
Chapitre 1.2
Le niveau applicatif : serveur, répartition et
interpréteur
Le cœur du système d'entreprise n'est pas la base de données : c'est le processus qui sait quoi en
faire.
Le niveau de traitement est le plus riche et le plus difficile à remplacer. Il porte la logique métier, les
contrôles d'accès, les règles de gestion, et l'orchestration des accès à la base. Dans les systèmes d'entreprise
de troisième génération, ce niveau est constitué de quelques composants précis, dont il faut comprendre le
rôle exact pour raisonner sur les performances.
• Serveur de répartition : point d'entrée unique. Il reçoit la requête, vérifie l'authentification, choisit un
processus de traitement libre, lui transmet le contexte utilisateur, puis ne fait plus qu'attendre la
réponse. Il ne connaît aucune règle métier.
• Processus de traitement : l'exécutant. Il interprète le programme, dialogue avec la base, tient l'état de
la transaction. Il y en a plusieurs par serveur, et c'est leur nombre qui borne la charge simultanée.
• Serveur de messages : le commutateur. Il centralise les communications entre serveurs, permet
l'équilibrage de charge, distribue les données entre serveurs, et sert de mémoire partagée pour les tables
de configuration.
• Serveur de travaux de fond : exécute ce qui ne doit pas bloquer l'utilisateur :les mises à jour massives,
exports, recalculs, nettoyages.
• Serveur d'impression et de sortie : produit les documents, rend les lots de données pour des
traitements externes.
Le dimensionnement du nombre de processus
Le nombre de processus de traitement par serveur est le principal levier de performance d'un système
d'entreprise, et le plus souvent mal réglé. Trop peu, la file d'attente s'allonge et les utilisateurs attendent. Trop,
les processus se disputent la mémoire et le système d'exploitation commence à échanger avec le disque, ce qui
dégrade tout le reste. La valeur correcte dépend de la taille du contexte mémoire par processus et de la mémoire
disponible — aucune valeur par défaut n'est universelle.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
11
Transaction coûteuse
Pourquoi elle coûte cherParade
recommandée
Écran long affichant une liste de milliers
de lignesla liste est construite en mémoire,
la transaction reste ouverte
limiter le nombre de lignes, imposer un
filtre, paginer
Modification massive en boucle dans un
seul écran
une seule transaction enorme, verrouillage
prolongé
fractionner en paquets et valider entre chaque
Appel synchrone vers un autre système
pendant la transaction
le temps d'attente externe bloque les
ressources de traitement
mettre l'appel en file de sortie, traiter après
validation
Sélection sans critère d'index
lecture complète de la table dans la mémoire
du serveur de base
indexer le critère de filtre, ou traiter en différé
Verrouillage excessif sur une table très
sollicitée
les transactions concurrentes se serialisent
regrouper les mises à jour, réduire la granularité
des verrous
Tableau 1 — Les quatre transactions les plus coûteuses et leur parade
Les quatre premières causes représentent la très grande majorité des problèmes de performance de ce type de système.
Elles relèvent toutes de la discipline de conception, pas de l purchases de matériel supplémentaire.
Figure 1 — Le parcours d'une transaction, de la saisie à l'écriture
Algorithme 1 — Traitement d'une requête utilisateur dans l'architecture trois niveaux
01  Le poste de travail envoie la requête au serveur de répartitionLe serveur de répartition
authentifie l'utilisateur et ouvre un contexte
02  Il sélectionne un processus de traitement libre dans la file
03  Il lui transmet le contexte, puis attend la réponse
04  Le processus de traitement charge l'écran en exécutant le programme associé
05  Le programme émet des instructions vers la base de données
06  La base lit et verrouille les lignes concernées, puis rend le résultat
07  Le programme effectue les contrôles de gestion et les contrôles d'accès
08  Le processus valide la transaction : la base écrit définitivement
09  Le résultat est renvoyé au serveur de répartition, puis au poste de travail
Entrées : Identifiant utilisateur, code de transaction, données saisies • Sorties : Écran affiché, écritures
validées, entrées de journal • Complexité : Latence = aller-retour réseau + temps de traitement + temps
d'accès base
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
12
Les étapes 3 et 9 sont les deux points de contention. La troisième est un goulot d'étranglement par conception
; la neuvième est la seule étape qui rend le résultat durable, et celle dont l'exécution conditionné toutes les
autres.
A retenir
• Le serveur de répartition ne connaît aucune règle métier : son rôle est d'aiguiller et de contrôler l'accès.
• Le nombre de processus de traitement est le premier levier de performance et le plus souvent mal réglé.
• Un appel synchrone vers l'extérieur pendant une transaction ouverte bloque des ressources pendant toute
l'attente.
• Un écran qui liste des milliers de lignes est un problème de conception, pas de capacité.
Chapitre 1.3
Le niveau de données et le référentiel
applicatif
Deux dépôts de données coexistent : celui que la base contient, et celui que le code applicatif
définit.
Le niveau de données d'un système d'entreprise ne se résume pas à un moteur relationnel et ses tables. Il
comprend un second dépôt, tout aussi déterminant, qui contient la définition même des programmes : ce
que la base contient est l'état du système, ce que le référentiel contient est le système lui-même.
Base de données
Référentiel applicatif
Contient
les transactions, les données de référence, les
journauxles programmes, les dictionnaires, les
définitions d'écrans, les variantes de configuration
Modifié par
les transactions métier
les mises à jour de version et les extensions
Restauration
sauvegarde et restauration de base
mise à jour de version avec reprise automatique
Rôle
conserver l'état
définir le comportement
Conséquence d'une perte
reprise à partir d'une sauvegarde
retour à la version précédente ou réinstallation
Sauvegarde
quotidienne, incrémentale, testée
sauvegarde avant mise à jour, avec reprise
Tableau 1 — Base de données et référentiel applicatif
La distinction n'est pas académique : une mise à jour de version qui ne préserve pas le contenu étendu ne met pas à jour le
système, elle le détruit. C'est la raison pour laquelle toute migration commence par un inventaire écrit du référentiel.
\mathrm{Coût}(S, T) = \underbrace{\mathrm{Acc-base}(S, T)}$0 +
underbraceCRUD(S, T)0 + $\underbrace{\mathrm{Join}(S, T)}_{\text{relations entre
tables}}
(E.1)
La partition en trois termes n'est pas un détail technique : elle est la trame d'analyse de toute optimisation.
Réduire le premier terme se fait par des index, le deuxième par l'architecture de la logique métier, le troisième
par la normalisation — et les trois entrée en conflit.
• Normalisation : réduire la redondance pour garantir la cohérence, au prix d'un nombre de jointures plus
élevé. L'optimum se trouve rarement à la forme normale la plus stricte.
• Dé-normalisation : dupliquer délibérément pour speeding la lecture, en assumant qu'un contrôle
applicatif maintient la cohérence. Valable pour une tablerequently lue, fausse dès qu'elle s'écrit.
• Index : accélère la sélection, ralentit l'écriture et occupe de l'espace. Il doit correspondre à un critère de
filtre réel, sinon il ne sert qu'à ralentir.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
13
• Tâches de fond : reconstruire les index, mettre à jour les statistiques, vérifier la cohérence. Elles
déverrouillent et dégradent les performances pendant leur exécution : il faut les planifier, pas les
découvrir.
Auditer un niveau de données en huit points
• Volume de chaque table, en lignes et en octets, et période de croissance.
2. Index présents, et pour chacun, le critère de filtre auquel il correspond réellement.
3. Redondances assumées, et contrôle applicatif qui les maintient.
4. Jointures les plus fréquentes, et nombre d'enregistrements ramenés.
5. Tables sans mouvement depuis un an, à archiver.
6. Tâches de fond en place, et leur impact sur la charge diurne.
7. Sauvegarde : fréquence, durée, et date du dernier test de restauration réel.
8. Inventaire du référentiel : extensions, zs, programmes personnalisés, et propriétaire de chacun.
Une sauvegarde dont la restauration n'a jamais été pratiquée n'est pas une sauvegarde. Le test consiste à
restaurer une copie sur un environnement distinct, à vérifier le compte rendu de restauration, puis à ouvrir
un échantillon de transactions et à les rapprocher des pièces comptables correspondantes. La durée de
conservation de la sauvegarde doit couvrir le délai de détection d'un incident, pas seulement le délai de
reprise : c'est souvent ce second délai qui est sous-estimé.
La sauvegarde jamais testée
Astuce
La date du dernier test de restauration est l'indicateur de fiabilité le plus honnête d'un système de données. Tout
le reste — procédure, documentation, contrat de sauvegarde — décrit une intention.
A retenir
• Le référentiel contient le système ; la base n'en contient que l'état instantané.
• Toute mise à jour commence par un inventaire écrit du contenu étendu.
• L'optimisation d'une base se raisonne en trois termes : cache, écritures, jointures.
• La seule mesure honnête de fiabilité d'une sauvegarde est la date du dernier test de restauration réel.
Chapitre 1.4
L'intégration des modules fonctionnels
L'avantage d'un progiciel intégré n'est pas la richesse des fonctions : c'est l'absence de ressaisie.
Figure 1 — Les modules fonctionnels et le référentiel partagé
Un progiciel intégré juxtapose des modules fonctionnels — finance, achats, stocks, ventes, production,
ressources humaines — qui partagent le même référentiel et la même base. La conséquence pratique est
considérable : un même fait élémentaire n'est jamais saisi deux fois, et sa propagation dans tous les
modules concernés est automatique.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
14
Algorithme 2 — Traversée d'un achat de matière à travers les modules
01  Un besoin d'achat est exprimé par le module de productionLe module des achats transforme le
besoin en commande fournisseur
02  À réception, le module de stocks enregistre l'entrée en magasin
03  Le module financier crée automatiquement la dette envers le fournisseur
04  La matière est consommée par un ordre de fabrication
05  Le module de production valorise la consommation sur le centre de coût
06  Le module financier impute cette valeur sur le compte de résultat concerné
07  Le module de contrôle de gestion restitue l'écart entre prévision et réalisation
Entrées : Besoin d'achat, quantité, centre de coût, date • Sorties : Commande, entrée en stock, écritures,
écart analysable • Complexité : Huit modules touchés, une seule saisie utilisateur
C'est le trajet type d'un système intégré. Aucune des étapes intermédiaires n'est saisie : chacune dérive de la
précédente. C'est là que réside l'économie, et c'est aussi là que réside le risque : une erreur en amont se
propage partout sans qu'aucune revalidation ne l'arrête.
Module
Domaine
Entrées principales
Sorties principales
Finance
comptabilité générale, contrôle de
gestion, 
trésorerieécritures
d'exploitation, pièces justificatives
bilan, compte de résultat, plan de
trésorerie
Achats et
approvisionnement
fournisseurs, commandes, réception
besoins, contrats
commandes, factures, réception
Stocks
mouvements, inventaires, valorisations
réceptions, sorties, transferts
état du stock, valorisation
Ventes et distribution
clients, 
commandes, 
livraison,
facturation
commandes, disponibilité
bons de livraison, factures
Production
ordonnancement, gamme, suivi de
fabrication
noms de production, besoins
coûts, quantités produites
Ressources humaines
paie, temps de travail, recrutement
pointages, contrats
bulletins, provisions sociales
Tableau 1 — Les six modules d'un progiciel intégré et leurs flux
Definition — Ligne analytique
Le mécanisme qui rattache une écriture à un axe d'analyse : centre de coût, centre de profit, projet, article. C'est
lui qui permet de répondre à « combien cette activité a-t-elle coûté » sans dupliquer les comptes. Sans ligne
analytique, le module de contrôle de gestion n'a rien à analyser, et l'intégration perd sa contrepartie : on a gagné
la suppression de la ressaisie en perdant l'analyse.
Le risque de l'intégration excessive
Chaque module qui se verrouille sur une donnée d'un autre module crée une dépendance. Un jour, la refonte
d'un module impose de revenir dans les six autres. La parade n'est pas de proscrire l'intégration — c'est ce qui a
été acquis — mais de fixer une règle : les modules ne s'appellent jamais directement entre eux. Une donnée qui
doit traverser deux modules transite par un interface documentée, ce qui rend le remplacement d'un module
possible sans modifier les autres.
Séparation des responsabilités et piste d'audit
Dans un système intégré, l'accès à une fonction sensible est régulé par un profil et non par une habilitation de
masse. La séparation des responsabilités impose qu'aucun acteur ne puisse seul créer puis valider une écriture
critique. La piste d'audit doit permettre de reconstituer qui a fait quoi, depuis quel poste, à quelle date, avec le
document à l'appui — y compris lorsque l'écriture a été générée automatiquement par un autre module, cas où
l'automaticité est précisément ce qu'il faut savoir tracer.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
15
A retenir
• L'intégration supprime la ressaisie, mais propage aussi les erreurs sans point de contrôle intermédiaire.
• Les modules ne doivent jamais s'appeler directement : ils échangent par une interface documentée.
• La ligne analytique est ce qui rend l'intégration utile à l'analyse, et non seulement à la saisie.
• La séparation des responsabilités impose qu'aucun acteur ne puisse créer puis valider seul une écriture
critique.
Chapitre 1.5
Transactions, verrous et performances
Le coût d'une transaction ne dépend pas de ce qu'elle calcule, mais de la durée pendant laquelle
elle retient les lignes.
Le moteur relationnel garantit qu'une suite d'écritures est soit entièrement appliquée, soit entièrement
annulée. Ce garantie a un prix : les lignes lues pour modification sont réservées jusqu'à la validation, et une
transaction concurrente qui touche la même ligne est mise en attente. La performance d'un système
d'entreprise se joue donc moins dans le calcul que dans la durée de réservation.
Réservation(l) = t1 - t2\text{Attente}(n) \leq \frac{D}{n} \quad \text{où } D \text{ est la $$durée moyenne d'une
transaction concurrente sur la même ligne}
(E.2)
La première expression est la seule qui compte en pratique. Halver la durée de réservation d'une transaction
équivaut à doubler le débit, sans toucher au matériel. La seconde explique pourquoi les points de contention
deviennent des goulots d'étranglement bien avant la saturation des ressources.
Niveau
Levier
Gain attendu
Coût de mise en œuvre
Présentation
limiter le nombre de lignes renvoyéesfort,
immédiat
faible, conception d'écran
Traitement
réserver moins de lignes par transaction
fort, immédiat
faible, 
discipline 
de
programmation
Traitement
augmenter le nombre de processus
moyen, plafonné
moyen, 
dimensionnement
matériel
Données
ajouter un index sur un critère réel
fort, immédiat
faible, mais maintenance
Données
dé-normaliser une table très lue
fort en lecture
moyen, contrôle applicatif à écrire
Données
réduire le nombre de tables jointes
moyen
élevé, refonte du modèle
Matériel
plus de mémoire pour le serveur de base
moyen, souvent fort
élevé
Matériel
dupliquer le serveur applicatif
faible si la contention est dans les
données
élevé, sans benefit si la cause est
elsewhere
Tableau 1 — Leviers de performance par niveau, et leur rendement
Les quatre premières lignes sont gratuites ou peu coûteuses, et règlent plus de 80 % des cas. Acheter du matériel avant
d'avoir examiné la durée de réservation des transactions est l'erreur la plus fréquente et la plus coûteuse.
Si deux transactions se disputent les mêmes lignes, doubler le nombre de serveurs d'application ne fait
qu'ajouter des clients à la même file d'attente. Le temps d'attente augmente, le débit ne bouge pas, et
l'on a payé deux fois. Le diagnostic est simple : si le temps d'attente des transactions dépasse le temps de
leur exécution, le goulot est dans les données, pas dans le nombre de serveurs.
Multiplier les serveurs applicatifs pour résoudre un problème de données
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
16
Travaux pratiques 1.1 — Diagnostiquer un ralentissement jusqu'à sa cause
Duree : 3 h  |   Niveau : Avance  |   Outils : Un jeu de transactions avec horodatages de début, de fin et de validation, et
une table de contention par ressource
Analyser un système d'entreprise ralenti, distinguer goulot de données et manque de puissance, et produire
un diagnostic argumenté.
Deroulement
1. Calculer la durée moyenne de réservation de chaque transaction, et le temps d'attente moyen associé.
2. Distinguer les transactions dont l'attente dépasse la durée d'exécution : elles subissent un conflit.
3. Regrouper les transactions en conflit par ressource, et identifier les trois tables les plus disputées.
4. Proposer pour chacune des trois tables une réduction de la portée de la réservation, et justifier.
5. Comparer le gain théorique attendu à une augmentation de 50 % du nombre de serveurs applicatifs, et
conclure.
6. Écrire en trois lignes ce qu'il faut faire en premier, et pourquoi.
Livrable attendu
• T
• a
• b
• l
• e
• a
• u
• d
• e
• s
• d
• u
• r
• é
• e
• s
• d
• e
• r
• é
• s
• e
• r
• v
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
17
• a
• t
• i
• o
• n
• e
• t
• d
• '
• a
• t
• t
• e
• n
• t
• e
• ,
• c
• l
• a
• s
• s
• e
• m
• e
• n
• t
• d
• e
• s
• c
• o
• n
• f
• l
• i
• t
• s
• ,
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
18
• n
• o
• t
• e
• d
• '
• a
• n
• a
• l
• y
• s
• e
• d
• e
• t
• r
• o
• i
• s
• l
• i
• g
• n
• e
• s
• .
Bareme indicatif
Critere
Points
La note conclut que la contention est dans les données4
Le gain annoncé est justifié par le calcul
4
La comparaison avec l'ajout de serveurs est chiffrée
2
A retenir
• Le coût d'une transaction tient à la durée de sa réservation, pas à la complexité de son calcul.
• Halver la durée de réservation double le débit, sans matériel supplémentaire.
• Si le temps d'attente dépasse le temps d'exécution, le goulot est dans les données.
• Le premier réflexe de performance est l'examen de la durée de réservation, jamais l'achat de serveurs.
Chapitre 1.6
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
19
Évolution, migration et architectures de
remplacement
La question n'est pas de migrer vers une plateforme nouvelle, mais de rendre le modèle métier
indépendant de la plateforme.
Figure 1 — Du trois niveaux classique à la plateforme en mémoire
Architecture
Unité de déploiement
Base de donnéesCe qui la
caractérise
Trois niveaux
un 
serveur, 
une
baserelationnelle sur disque,à
Accès
simplplicité conceptuelle, forge de
compétences
Services distribués
plusieurs services indépendants
une base par service
déploiement 
indépendant, 
pannes
partielles, complexité d'exploitation
Plateforme en mémoire
un socle unique
unique, en colonnes, calcul au
moment de la lecture
rapidité, 
simplification 
du 
modèle,
migration coûteuse
Tableau 1 — Les trois architectures et ce qui les distingue
Le passage d'une architecture à l'autre ne change pas la question de fond : où se trouve la logique métier, et combien de
fois la donnée est-elle dupliquée.
• Base en mémoire : les données tiennent en mémoire, en colonnes, avec compression. L'accès ne fait
plus d'aller-retour disque, et le calcul analytique s'exécute au moment de la lecture plutôt que dans un
entrepôt séparé.
• Transaction et analyse réunies : une seule copie de la donnée, au lieu de trois — base transactionnelle,
entrepôt analytique, système de données. La duplication disparaît, et avec elle une grande partie des
problème de cohérence.
• Services standardisés : les fonctions deviennent des interfaces que d'autres systèmes consomment, ce
qui crée une dépendance applicable dans l'autre sens : le fournisseur de l'interface devient un point de
contrôle.
Migrer sans casser : la séquence qui fonctionne
• Inventaire écrit du référentiel : extensions, personnalisations, programmes non standard, avec un
propriétaire pour chacun. Sans cet inventaire, la migration est une devinette.
2. Conception du modèle cible en termes fonctionnels, et non en tables. C'est le seul niveau où le métier doit
décider.
3. Gel des développements sur l'ancien système pendant toute la migration, et report des besoins sur le
nouveau.
4. Migration des données par lots répétés, avec un contrôle de rapprochement à chaque itération, jamais une
seule fois à la fin.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
20
5. Reprise des.personnalisations une par une, en justifying pour chacune :utile, ou remodelable par une
configuration.
6. Bascule par domaine fonctionnel, jamais tout d'un coup, avec une période de double exploitation.
7. Plan de retour arrière écrit et testé avant la bascule, avec le délai maximal de retour decided à l'avance.
Ce qu'une migration ne supprime pas
Une plateforme en mémoire rend la requête rapide, pas l'analyse juste. Si les règles analytiques sont écrites à la
main dans des requêtes, elles migrent telles quelles, avec leurs erreurs. De même, la réactivité d'une requête ne
rend pas l'utilisateur rapide : si l'écran liste mille lignes, l'utilisateur attend autant. La migration améliore les
fondations ; elle ne dispensé d'aucun travail de conception, et il faut annoncer cela avant de commencer.
Astuce
La meilleure préparation à une migration est de rendre le modèle métier indépendant du détail technique. Un
modèle bien écrit, exprimé en objets métier et non en tables, réduit le coût de toute migration future — y
compris celle qu'on ne peut pas encore prévoir. C'est un investissement dont le rendement est différé mais
certain.
Projet — Rédiger un dossier d'architecture trois niveaux
Duree : 6 semaines | Equipe : 3 a 5 etudiants | Depot : gitlab + rapport
Une PME manufacturière souhaité remplacer son progiciel de gestion par un système en architecture trois
niveaux, initialement sur le modèle d'entreprise, avec un objectif de migration à moyen terme vers une
plateforme en mémoire.
Missions
1. Décrire les trois niveaux, leurs composants et le protocole qui relié chacun au suivant, en justifiant
chaque choix par un critère d'exploitation.
2. Dimensionner le nombre de processus de traitement et l'architecture du serveur, en explicitant les
grandeurs retenues.
3. Établir le plan de sauvegarde des deux dépôts distincts — base et référentiel — avec la fréquence, la
durée de conservation et la procédure de test.
4. Rédiger le plan de reprise après panne, incluant le délai de détection, le délai de restauration et le seuil
au-delà duquel les écritures sont basculées dans une file de reprise.
5. Établir l'inventaire du contenu étendu du référentiel et la procédure de qualification de chaque
personnalisation.
6. Chiffrer la séquence de migration en six étapes, avec pour chacune sa condition d'entrée, sa sortie et son
critère de retour arrière.
Livrables
• D
• o
• c
• u
• m
• e
• n
• t
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
21
• d
• '
• a
• r
• c
• h
• i
• t
• e
• c
• t
• u
• r
• e
• e
• n
• t
• r
• o
• i
• s
• n
• i
• v
• e
• a
• u
• x
• ,
• p
• l
• a
• n
• d
• e
• s
• a
• u
• v
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
22
• e
• g
• a
• r
• d
• e
• e
• t
• d
• e
• r
• e
• p
• r
• i
• s
• e
• ,
• i
• n
• v
• e
• n
• t
• a
• i
• r
• e
• d
• u
• r
• é
• f
• é
• r
• e
• n
• t
• i
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
23
• e
• l
• ,
• s
• é
• q
• u
• e
• n
• t
• i
• e
• l
• d
• e
• m
• i
• g
• r
• a
• t
• i
• o
• n
• ,
• e
• t
• t
• a
• b
• l
• e
• a
• u
• d
• '
• e
• s
• t
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
24
• i
• m
• a
• t
• i
• o
• n
• d
• e
• l
• a
• c
• h
• a
• r
• g
• e
• p
• a
• r
• é
• t
• a
• p
• e
• .
Évaluation
• L
• e
• j
• u
• r
• y
• v
• é
• r
• i
• f
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
25
• i
• e
• q
• u
• e
• c
• h
• a
• q
• u
• e
• d
• é
• c
• i
• s
• i
• o
• n
• d
• e
• d
• i
• m
• e
• n
• s
• i
• o
• n
• n
• e
• m
• e
• n
• t
• c
• i
• t
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
26
• e
• l
• a
• g
• r
• a
• n
• d
• e
• u
• r
• m
• e
• s
• u
• r
• é
• e
• q
• u
• i
• l
• a
• j
• u
• s
• t
• i
• f
• i
• e
• ,
• q
• u
• e
• l
• a
• r
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
27
• e
• p
• r
• i
• s
• e
• a
• p
• r
• è
• s
• p
• a
• n
• n
• e
• c
• o
• u
• v
• r
• e
• l
• e
• c
• a
• s
• d
• e
• l
• a
• p
• e
• r
• t
• e
• d
• u
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
28
• r
• é
• f
• é
• r
• e
• n
• t
• i
• e
• l
• ,
• e
• t
• q
• u
• e
• l
• a
• m
• i
• g
• r
• a
• t
• i
• o
• n
• p
• r
• é
• v
• o
• i
• t
• u
• n
• r
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
29
• e
• t
• o
• u
• r
• a
• r
• r
• i
• è
• r
• e
• t
• e
• s
• t
• é
• .
A retenir
• L'architecture trois niveaux reste la grille de lecture de tout système d'entreprise, quel que soit son âge.
• Ce qui change entre les générations, c'est la localisation de la donnée et le nombre de ses copies, pas le
découpage des responsabilités.
• Une migration se prépare par un inventaire écrit du référentiel, pas par un choix de plateforme.
• Le retour arrière doit être dimensionné, testé et daté avant la bascule, pas improvisé après l'incident.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
30
Abréviations, notation et ressources de consultation
Annexes
Annexes
Ce cours se termine par deux annexes de référence. La première donne la signification de chaque sigle
employé, sous les deux formes — sigle et développé — car la litterature emploie indifféremment l'une
ou l'autre. La seconde donne la signification de chaque symbole mathématique : elle permet de relire
une démonstration sans revenir au chapitre dont elle est extraite, et de vérifier qu'un même symbole
garde le même sens d'un chapitre à l'autre.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
31
Chapitre A.1
Liste des abréviations
Les sigles ci-dessous sont ceux que le cours emploie. Chacun est donné avec sa forme développée
et le sens précis qu'il prend ici, qui n'est pas toujours celui qu'on lui donne ailleurs.
Un sigle employé sans être développé oblige le lecteur à le reconnaître au passage, ou à l'abandonner. Le
tableau ci-dessous ferme la liste de ceux que le cours emploie : il est exhaustif pour ce document, et non
pour la discipline.
Sigle
Forme développée
Sens dans ce cours
API
Application Programming Interface
Interface d'échange entre deux logiciels.
CRUD
Create, Read, Update, Delete
Quatre opérations de base sur un enregistrement.
EDI
Electronic Data Interchange
Échange de messages normalisés entre systèmes d'information.
ERP
Enterprise Resource Planning
Système d'information couvrant l'ensemble des fonctions de l'entreprise.
FO
Flux d'ordre
Circuit d'approvisionnement, du besoin à la réception.
ICI
Interconnexion des systèmes
d'information
Ensemble des liaisons entre applications.
OLTP
Online Transaction Processing
Traitement transactionnel en ligne.
PME
Petite et moyenne entreprise
Entreprise de moins de 250 salariés.
RGPD
Règlement général sur la protection des
données
Cadre européen de protection des données personnelles.
SAV
Service après-vente
Fonction de traitement des retours clients.
SCM
Supply Chain Management
Gestion de la chaîne d'approvisionnement.
WMS
Warehouse Management System
Logiciel de gestion d'entrepôt.
Tableau 1 — Abréviations employées dans le cours
Chapitre A.2
Table de notation
Les symboles ci-dessous gardent le même sens d'un chapitre à l'autre. Lorsqu'un chapitre doit
réemployer un symbole pour un autre objet, il le redéclare sur la page même.
La notation est celle du cours : vecteurs en gras, matrices en majuscules grasses, scalaires en italique. Les
espérances sont notées E, les lois de données D, les espaces de paramètres Θ.
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
32
Symbole
Signification
N
Nombre de sites reliés.
E
Nombre de flux échangés entre deux sites.
G
Graphe des interdépendances : les sites et les flux.
u ∈ V(G)
Site du graphe.
cij
Coût du flux qui va de i vers j.
Tij
Temps de traversée du flux qui va de i vers j.
Si
Stock disponible au site i.
Dj
Demande adressée au site j.
δ
Taux de service, part des demandes servies dans le délai.
k
Nombre de niveaux de la cascade de décision.
pi
Priorité du critère i.
wi
Pondération du critère i dans une note composite.
Tableau 1 — Symboles mathématiques et leur signification
Convention
Toute divergence constatée entre cette table et un chapitre signale une erreur de transcription, non une
définition nouvelle : la table fait foi.
A retenir
• Un sigle employé sans être listé ici est un oubli de l'auteur, non une définition nouvelle.
• Un symbole qui change de sens d'un chapitre à l'autre rend toute démonstration ininterprétable : c'est la
principale cause des contresens que nous avons relevés.
• Ces deux tables sont les seules parties du cours à maintenir à la main : le reste se relit tout seul.
Index des figures et des tableaux
Référence rapide du matériel visuel
Figures
1.  L'architecture trois niveaux et la place de chaque élément
1.  Le parcours d'une transaction, de la saisie à l'écriture
1.  Les modules fonctionnels et le référentiel partagé
1.  Du trois niveaux classique à la plateforme en mémoire
Tableaux
1.  Les trois niveaux, leurs responsabilités et leurs protocoles
1.  Les quatre transactions les plus coûteuses et leur parade
1.  Base de données et référentiel applicatif
1.  Les six modules d'un progiciel intégré et leurs flux
1.  Leviers de performance par niveau, et leur rendement
1.  Les trois architectures et ce qui les distingue
1.  Abréviations employées dans le cours
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
33
1.  Symboles mathématiques et leur signification
Intelligence Artificielle Avancée & Federated Learning
Pixel Software Design
Pixel Software Design — Ghiloufi Jamel (2026)
34
Fin du document
Intelligence Artificielle Avancée & Federated Learning — Fondations mathématiques de
l'apprentissage automatique, algorithmes fédérés, protection de la vie privée, défense contre les attaques,
grands modèles de langage fédérés, systèmes embarqués, renforcement appris, applications critiques
(santé, V2X), plateforme de référence FedX et feuille de route de recherche.<br/>Ghiloufi Jamel,
Architecte Logiciel Principal — Pixel Software Design<br/>Département de Recherche & Développement
— Recherche<br/>Pixel Software Design — Édition 2026
© 2026 Pixel Software Design. Tous droits réservés.
Ce document est la propriété exclusive de Pixel Software Design. Toute reproduction, représentation, adaptation ou
diffusion, totale ou partielle, par quelque procédé que ce soit et sur quelque support que ce soit, est interdite sans
autorisation écrite préalable de l'auteur.
Document généré automatiquement le 29/09/2026 — mise en page Pixel Software Design.
"""
