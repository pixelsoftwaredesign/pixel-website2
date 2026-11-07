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
