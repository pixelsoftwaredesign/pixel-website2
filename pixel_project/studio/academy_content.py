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
