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

