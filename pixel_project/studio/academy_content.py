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

PROGRAMME_OFFICIEL_TEXT = r"""Programme d'Études Officiel — PixelSoftware Academy (Édition 2026)

Niveau cible : Master 2 / Cycle Ingénieur en Systèmes Distribués, IA Avancée & Sécurité
Établissement : PixelSoftware Design Academy
Responsable pédagogique : Ghiloufi Jamel, Architecte Logiciel Principal
Version corrigée : les points relevés lors de la revue de cohérence sont intégrés et signalés par la mention « révisé ».

Vision et objectif du cursus
Le programme répond aux défis technologiques majeurs de l'industrie : concevoir des systèmes d'intelligence artificielle souverains, respectueux de la vie privée (apprentissage fédéré), structurés par la connaissance (GraphRAG et Meaning Graphs) et optimisés pour les environnements contraints (Edge LoRA et architectures distribuées).

Architecture globale du cursus
Semestre | Thème | Contenu
S1 | Fondations & Systèmes Distribués | Module 1 : Systèmes distribués & FedProx ; Module 2 : GraphRAG ; Module 3 : Enterprise AI Architecture
S2 | Advanced AI & Edge | Module 4 : LoRA & Edge ML ; Module 5 : Guardrails ; Projet fil rouge

Volumes horaires
Bloc | Cours | TP / projet | Total
Module 1 | 10 h | 20 h | 30 h
Module 2 | 8 h | 17 h | 25 h
Module 3 | 10 h | 15 h | 25 h
Total S1 | 28 h | 52 h | 80 h
Module 4 | 6 h | 14 h | 20 h
Module 5 | 6 h | 14 h | 20 h
Projet fil rouge | n/a | 40 h | 40 h
Total S2 | 12 h | 68 h | 80 h
Total cursus | 40 h (25 %) | 120 h (75 %) | 160 h

Semestre 1 : Fondations des systèmes distribués & IA sémantique

Module 1 : Systèmes distribués & Federated Learning (FedProx) — révisé
Volume horaire : 30 h (10 h cours, 20 h TP from scratch)
Révision : le titre initial mentionnait le « Big Data Distribué » sans que le contenu le couvre. Le titre est aligné sur le contenu ; un volet big data pourra être ajouté si l'équipe pédagogique le souhaite.
Objectifs pédagogiques : comprendre les limites des architectures centralisées (RGPD, latence, point de défaillance unique) et maîtriser l'apprentissage fédéré sur données hétérogènes.
Contenu détaillé :
• Topologie des données distribuées : i.i.d. vs non-i.i.d. (Feature Shift, Concept Drift).
• Formulation mathématique de l'optimisation globale et de la dérive des modèles (Client Drift).
• Algorithme FedProx et son terme de régularisation proximal : h_k(w; w_t) = F_k(w) + (μ/2) ‖w − w_t‖²₂
• Confidentialité différentielle (DP-SGD) : clipping L2 et injection de bruit gaussien.
• Robustesse aux attaques par empoisonnement via l'agrégation Trimmed Mean.
Évaluation : implémentation en Python pur d'un cluster fédéré simulé.

Module 2 : Meaning Graphs & architectures GraphRAG
Volume horaire : 25 h (8 h cours, 17 h TP)
Objectifs pédagogiques : dépasser les limites de la recherche vectorielle pure (Dense Retrieval) en combinant ontologies sémantiques et recherche hybride.
Contenu détaillé :
• Limites contextuelles globales des bases vectorielles (HNSW).
• Extraction de triplets RDF (Sujet, Prédicat, Objet) et construction de graphes de connaissances.
• Formule d'hybridation tri-partite : Score(doc) = α · Sim_Dense(q, d) + β · BM25(q, d) + γ · Centrality_Graph(doc)
Évaluation : conception d'un pipeline GraphRAG interconnecté à un graphe de connaissances.

Module 3 : Enterprise AI Architecture & System Patterns
Volume horaire : 25 h (10 h cours, 15 h TP)
Objectifs pédagogiques : architecturer des plateformes d'IA prêtes pour la production à grande échelle.
Contenu détaillé :
• Pattern Router-Dispatcher pour l'aiguillage sémantique entre petits modèles (SLMs) et grands modèles (LLMs).
• Mise en cache sémantique (Semantic Caching) pour réduire la latence TTFT.
• Boucles d'agents autonomes ReAct (Reasoning + Acting) et gestion des Circuit Breakers.
Évaluation : développement d'une passerelle d'inférence haute performance.

Semestre 2 : Optimisation Edge, gouvernance & projet transversal

Module 4 : Parameter-Efficient Fine-Tuning (LoRA & Edge ML)
Volume horaire : 20 h (6 h cours, 14 h TP)
Objectifs pédagogiques : entraîner et adapter des modèles sur des dispositifs à ressources limitées (IoT / mobile).
Contenu détaillé :
• Théorie de la décomposition à bas rang : h = W₀x + (α/r) · B · A · x
• Stratégies d'optimisation de la mémoire GPU et réduction du volume de communication en Federated Learning.
Évaluation : implémentation d'une couche LoRA from scratch en Python.
Point d'attention : 6 h de cours pour trois thèmes (LoRA, mémoire GPU, communication FL) est un volume serré ; un rééquilibrage cours/TP peut être envisagé.

Module 5 : Gouvernance, sécurité & LLM Guardrails
Volume horaire : 20 h (6 h cours, 14 h TP)
Objectifs pédagogiques : sécuriser les flux d'entrées/sorties et assurer la conformité réglementaire des applications d'IA.
Contenu détaillé :
• Détection et masquage automatisé des informations personnelles identifiables (PII : SSN, e-mails, téléphones).
• Résilience face aux attaques par injection de prompt directes et indirectes.
Évaluation : construction d'un pipeline de filtrage et de sécurité des requêtes.

Projet fil rouge : Système hospitalier fédéré (travail en équipe) — révisé
Volume horaire : 40 h de projet guidé
Énoncé : déploiement d'une architecture multi-établissements intégrant :
• FedProx (avec DP-SGD) pour la confidentialité des données de santé (Module 1) ;
• un Meaning Graph médical et une recherche GraphRAG pour le requêtage ontologique (Module 2) ;
• une passerelle d'inférence avec Router-Dispatcher, cache sémantique et Circuit Breakers (Module 3) ;
• une adaptation LoRA des modèles pour les établissements à ressources limitées (Module 4) ;
• des Guardrails de sécurité : masquage PII et défense contre l'injection de prompt (Module 5).
Révision : la version initiale n'intégrait ni LoRA ni les patterns du Module 3. L'énoncé couvre désormais l'ensemble des cinq modules.
Soutenance : évaluation sur grille officielle (20 points) devant un jury d'architectes.

Évaluation : points à définir
Seul le projet dispose aujourd'hui d'une grille officielle sur 20 points. Les éléments suivants restent à fixer par l'équipe pédagogique :
• la pondération des évaluations de modules par rapport à la soutenance ;
• les grilles de notation de chaque évaluation de module ;
• les modalités de rattrapage.

Compétences validées
Domaine | Compétence clé | Niveau visé
Systèmes distribués | Conception et pilotage d'un cluster d'apprentissage fédéré (FedProx + DP) | Maîtrise experte
Ingénierie des données | Création de Meaning Graphs et hybridation GraphRAG | Maîtrise avancée
Architecture logicielle | Implémentation de patrons de résilience (Router, Caching, Circuit Breaker) | Maîtrise experte
Edge & sécurité | Fine-tuning LoRA et filtrage Guardrails PII | Maîtrise opérationnelle

Plan de cours détaillé (proposition)
Chaque séance de cours dure 2 h. Les séances de TP durent 3 à 5 h. Les totaux de chaque module correspondent aux volumes horaires du programme.

Module 1 : Systèmes distribués & Federated Learning (10 h cours, 20 h TP)
Séance | Type | Durée | Contenu
C1 | Cours | 2 h | Limites des architectures centralisées (RGPD, latence, SPOF) ; données i.i.d. vs non-i.i.d. (Feature Shift, Concept Drift)
C2 | Cours | 2 h | Optimisation globale, principe de FedAvg, Client Drift
C3 | Cours | 2 h | FedProx : terme proximal, rôle et réglage de μ
C4 | Cours | 2 h | DP-SGD : clipping L2, bruit gaussien, compromis confidentialité/utilité
C5 | Cours | 2 h | Attaques par empoisonnement et agrégation Trimmed Mean
T1 | TP | 4 h | Simulateur de clients à données non-i.i.d. en Python pur
T2 | TP | 4 h | FedAvg from scratch
T3 | TP | 4 h | FedProx : comparaison avec FedAvg selon μ
T4 | TP | 4 h | DP-SGD sur les mises à jour clients
T5 | TP | 4 h | Attaque par empoisonnement, Trimmed Mean et évaluation finale du cluster fédéré

Module 2 : Meaning Graphs & GraphRAG (8 h cours, 17 h TP)
Séance | Type | Durée | Contenu
C1 | Cours | 2 h | Recherche dense et limites contextuelles des bases vectorielles (HNSW)
C2 | Cours | 2 h | Triplets RDF (Sujet, Prédicat, Objet), ontologies et graphes de connaissances
C3 | Cours | 2 h | BM25 et centralité de graphe
C4 | Cours | 2 h | Formule d'hybridation tri-partite, réglage de α, β, γ, métriques d'évaluation (recall, MRR)
T1 | TP | 4 h | Extraction de triplets à partir d'un corpus
T2 | TP | 4 h | Index dense et BM25
T3 | TP | 4 h | Construction du graphe et calcul de la centralité
T4 | TP | 5 h | Pipeline GraphRAG complet et évaluation

Module 3 : Enterprise AI Architecture (10 h cours, 15 h TP)
Séance | Type | Durée | Contenu
C1 | Cours | 2 h | Pattern Router-Dispatcher : critères d'aiguillage SLM / LLM
C2 | Cours | 2 h | Cache sémantique : similarité, seuils, invalidation, impact sur le TTFT
C3 | Cours | 2 h | Agents ReAct : boucle raisonnement-action-observation
C4 | Cours | 2 h | Circuit Breakers, timeouts, reprises et dégradation gracieuse
C5 | Cours | 2 h | Conception d'une passerelle d'inférence : observabilité, coûts, passage à l'échelle
T1 | TP | 4 h | Router-Dispatcher
T2 | TP | 4 h | Cache sémantique
T3 | TP | 4 h | Boucle ReAct protégée par un Circuit Breaker
T4 | TP | 3 h | Assemblage de la passerelle d'inférence et tests de charge

Module 4 : LoRA & Edge ML (6 h cours, 14 h TP)
Séance | Type | Durée | Contenu
C1 | Cours | 2 h | Décomposition à bas rang : h = W₀x + (α/r) · B · A · x
C2 | Cours | 2 h | Optimisation de la mémoire GPU et contraintes des dispositifs IoT / mobiles
C3 | Cours | 2 h | LoRA en apprentissage fédéré : réduction du volume de communication
T1 | TP | 4 h | Couche LoRA from scratch
T2 | TP | 4 h | Mesure du nombre de paramètres entraînables et de la mémoire selon le rang r
T3 | TP | 3 h | Intégration de LoRA dans un client fédéré
T4 | TP | 3 h | Évaluation : précision contre coût de communication

Module 5 : Gouvernance, sécurité & LLM Guardrails (6 h cours, 14 h TP)
Séance | Type | Durée | Contenu
C1 | Cours | 2 h | Données personnelles (PII), RGPD et obligations de conformité
C2 | Cours | 2 h | Injection de prompt directe et indirecte : scénarios d'attaque et défenses
C3 | Cours | 2 h | Architecture de guardrails en entrée et en sortie
T1 | TP | 4 h | Détection de PII (SSN, e-mails, téléphones)
T2 | TP | 4 h | Masquage et anonymisation automatisés
T3 | TP | 3 h | Détecteur d'injection de prompt
T4 | TP | 3 h | Pipeline complet de filtrage et jeu de tests adverses

Projet fil rouge : Système hospitalier fédéré (40 h)
Phase | Durée | Livrable
Cadrage et architecture | 4 h | Schéma d'architecture, répartition des rôles dans l'équipe
Cluster fédéré (FedProx + DP-SGD) | 10 h | Entraînement multi-établissements sur données simulées
Meaning Graph médical et GraphRAG | 8 h | Graphe ontologique et requêtage hybride
Passerelle d'inférence | 6 h | Router, cache sémantique et Circuit Breakers
Adaptation LoRA | 4 h | Mise à jour allégée pour les établissements à faibles ressources
Guardrails | 4 h | Masquage PII et défense contre l'injection de prompt
Soutenance | 4 h | Présentation devant le jury, grille sur 20 points

Les durées par séance sont une proposition ; elles peuvent être ajustées tant que les totaux par module restent inchangés.

Cours détaillé
Cette partie développe le contenu de chaque séance du plan ci-dessus : notions, formules, exemples et consignes de TP. Les notations sont en texte brut pour rester lisibles partout.

Module 1 : Systèmes distribués & Federated Learning
C1 : Pourquoi l'apprentissage fédéré ? (2 h)
Objectifs : identifier les limites d'une architecture centralisée et caractériser l'hétérogénéité des données.
Notions :
• Architecture centralisée : toutes les données sont copiées sur un serveur d'entraînement. Trois limites : conformité (RGPD, secret médical, interdiction de transférer certaines données), latence et coût de transfert, point de défaillance unique (SPOF).
• Apprentissage fédéré : les données restent chez les clients ; seuls les paramètres du modèle (ou leurs mises à jour) circulent. Le serveur coordonne, agrège et redistribue.
• Données i.i.d. : tous les clients tirent leurs échantillons de la même distribution. Cas rare en pratique.
• Données non-i.i.d. : déséquilibre des classes par client (label skew), distributions d'entrées différentes (Feature Shift), relation entrée-sortie qui change selon le client ou le temps (Concept Drift), quantités de données très inégales.
Exemple fil rouge : trois hôpitaux. L'un traite surtout des patients âgés, un autre dispose d'un autre type d'imagerie, un troisième a des protocoles de diagnostic différents : les trois formes de non-i.i.d. apparaissent.
À retenir : le fédéré protège la localisation des données, pas automatiquement leur confidentialité. Les mises à jour peuvent fuiter de l'information, d'où DP-SGD en C4.

C2 : Optimisation globale et Client Drift (2 h)
Objectifs : formuler le problème fédéré et comprendre pourquoi la moyenne simple dérive.
Formulation : avec K clients, n_k échantillons pour le client k et n = somme des n_k, on minimise
F(w) = somme sur k de p_k · F_k(w), avec p_k = n_k / n
où F_k est la perte locale du client k.
FedAvg (référence) : à chaque tour t, le serveur envoie w_t à un sous-ensemble de clients ; chacun effectue E époques de SGD local et renvoie w_k ; le serveur calcule w_(t+1) = somme sur k de p_k · w_k.
Client Drift : quand les données sont non-i.i.d., l'optimum local de chaque F_k diffère de l'optimum global. Plus E est grand ou le taux d'apprentissage élevé, plus chaque client s'éloigne de w_t vers son propre optimum, et la moyenne devient un mauvais compromis : convergence lente, oscillante, parfois divergente.
À retenir : réduire E limite la dérive mais augmente la communication ; il faut un mécanisme qui borne la dérive sans renoncer au calcul local.

C3 : FedProx (2 h)
Objectifs : dériver le terme proximal et savoir régler mu.
Objectif local modifié :
h_k(w; w_t) = F_k(w) + (mu / 2) · ||w − w_t||²
Gradient local : grad F_k(w) + mu · (w − w_t). Le second terme ramène le modèle local vers le modèle global courant : c'est une force de rappel.
Propriétés :
• mu = 0 redonne FedAvg.
• mu grand : le client bouge peu, la dérive est faible mais la progression locale aussi.
• FedProx tolère un travail local variable : un client lent ou à ressources limitées peut faire moins d'itérations sans bloquer le tour.
Réglage : valeurs usuelles à tester : 0.001, 0.01, 0.1, 1. Le meilleur mu dépend du degré d'hétérogénéité ; on le choisit sur un jeu de validation.

C4 : Confidentialité différentielle et DP-SGD (2 h)
Objectifs : protéger les mises à jour par clipping et bruit, et mesurer le coût en utilité.
Définition : un mécanisme est (epsilon, delta)-différentiellement privé si sa sortie change très peu (au plus un facteur e^epsilon, plus une probabilité delta) quand on ajoute ou retire un individu (ou un client) des données.
Mécanisme appliqué aux mises à jour :
1. Clipping L2 : delta_w_bar = delta_w · min(1, C / ||delta_w||₂). Cela borne la sensibilité à C.
2. Bruit gaussien : on ajoute N(0, sigma² · C² · I) à l'agrégat des mises à jour clippées.
Compromis : plus sigma est grand, plus epsilon est petit (meilleure confidentialité) mais plus l'entraînement est bruité. Un petit C écrête beaucoup l'information utile ; un grand C demande plus de bruit. Le suivi du budget cumulé d'epsilon sur les tours se fait par un comptable de confidentialité.
Précision : le DP-SGD classique clippe les gradients par échantillon ; dans le cadre fédéré, on clippe souvent la mise à jour de chaque client (confidentialité au niveau du client), ce que le TP met en œuvre.

C5 : Robustesse aux attaques et Trimmed Mean (2 h)
Objectifs : comprendre l'empoisonnement et mettre en place une agrégation robuste.
Menaces : empoisonnement des données (par exemple inversion d'étiquettes) ou des mises à jour (envoi de vecteurs volontairement nuisibles). Une simple moyenne est très sensible : un seul client malveillant peut déplacer le résultat arbitrairement.
Trimmed Mean coordonnée par coordonnée : pour chaque paramètre, on trie les K valeurs reçues, on retire les b plus petites et les b plus grandes, puis on moyenne les K − 2b restantes. Elle résiste si le nombre de clients malveillants est au plus b.
Limites : en non-i.i.d., des clients honnêtes mais atypiques peuvent être retirés, ce qui ralentit la convergence ; le choix de b est un compromis entre robustesse et efficacité.

T1 à T5 : Travaux pratiques (20 h)
TP | Consigne | Livrable et critères
T1 (4 h) | Générer K clients avec un déséquilibre de classes réglable (par exemple partition de Dirichlet) en Python pur | Fonction de partition, histogramme des classes par client
T2 (4 h) | Implémenter FedAvg : entraînement local (régression logistique), agrégation pondérée, boucle de tours | Courbe de perte globale et d'exactitude par tour
T3 (4 h) | Ajouter le terme proximal et comparer FedAvg et FedProx pour plusieurs mu et niveaux d'hétérogénéité | Tableau comparatif et analyse de l'effet de mu
T4 (4 h) | Ajouter clipping L2 et bruit gaussien aux mises à jour ; faire varier sigma et C | Courbe utilité en fonction du bruit ; discussion du compromis
T5 (4 h) | Injecter des clients malveillants (inversion d'étiquettes ou mises à jour aberrantes) ; comparer moyenne simple et Trimmed Mean | Cluster fédéré final, rapport d'évaluation (note du module)
Barème indicatif de l'évaluation du module (à valider) : exactitude du code et reproductibilité, qualité des expériences, analyse critique, clarté du rapport.

Module 2 : Meaning Graphs & GraphRAG
C1 : Recherche dense et ses limites (2 h)
Objectifs : comprendre le fonctionnement de la recherche vectorielle et là où elle échoue.
Notions :
• Plongements (embeddings) : un texte devient un vecteur ; la similarité (cosinus) mesure la proximité sémantique entre la requête q et un document d.
• HNSW : index de voisinage approché en graphe hiérarchique ; très rapide, mais renvoie les passages les plus proches de la requête, pas les plus utiles pour raisonner.
• Limites : perte de la structure (qui est lié à quoi), mauvaise gestion des questions multi-sauts, faible traçabilité de la réponse, difficulté sur les termes rares ou les identifiants exacts.
À retenir : la recherche dense capte le sens mais pas les relations explicites ni les correspondances lexicales exactes.

C2 : Triplets RDF et graphes de connaissances (2 h)
Objectifs : représenter la connaissance sous forme de triplets et construire un graphe.
Notions :
• Triplet RDF : (Sujet, Prédicat, Objet), par exemple (Metformine, traite, Diabète de type 2).
• Graphe de connaissances : les entités sont les nœuds, les prédicats sont les arêtes orientées. Le chemin entre deux nœuds exprime un raisonnement multi-sauts.
• Ontologie : vocabulaire contrôlé de classes et de relations. Elle garantit la cohérence et permet l'inférence.
• Extraction : par règles, par modèle de langage avec sortie structurée, ou par import de sources existantes. Il faut résoudre les synonymes (normalisation des entités) et valider la qualité.

C3 : BM25 et centralité de graphe (2 h)
Objectifs : maîtriser les deux autres signaux de la formule hybride.
BM25 : score lexical qui combine la fréquence du terme dans le document (saturée), la rareté du terme dans le corpus (IDF) et une normalisation par la longueur du document. Il excelle sur les termes exacts (noms de molécules, codes).
Centralité : mesure de l'importance d'un nœud dans le graphe. Exemples : centralité de degré, PageRank (importance propagée par les liens), centralité d'intermédiarité (nœuds sur les chemins les plus courts). Un document rattaché à des entités centrales pour la requête est favorisé.
Point d'attention : les trois scores n'ont pas la même échelle ; il faut les normaliser (par exemple min-max sur la liste candidate) avant de les combiner.

C4 : Hybridation tri-partite et évaluation (2 h)
Objectifs : combiner les signaux, régler les poids, mesurer la qualité.
Formule : Score(doc) = alpha · Sim_Dense(q, d) + beta · BM25(q, d) + gamma · Centrality_Graph(d), avec des scores normalisés et, en général, alpha + beta + gamma = 1.
Réglage : recherche sur grille ou optimisation sur un jeu de requêtes annotées.
Métriques : recall@k, MRR, précision@k. Toujours comparer à des lignes de base : dense seul, BM25 seul.
Pipeline GraphRAG : requête, détection des entités, récupération hybride, expansion par voisins dans le graphe, assemblage du contexte avec ses sources, génération de la réponse avec citation des triplets utilisés.

T1 à T4 : Travaux pratiques (17 h)
TP | Consigne | Livrable et critères
T1 (4 h) | Extraire des triplets d'un corpus médical simulé, normaliser les entités | Fichier de triplets, taux de précision sur un échantillon annoté
T2 (4 h) | Construire un index dense (vecteurs et similarité cosinus) et un index BM25 | Comparaison des résultats sur 10 requêtes
T3 (4 h) | Construire le graphe, calculer degré et PageRank, afficher le sous-graphe d'une requête | Graphe et table de centralités
T4 (5 h) | Assembler le pipeline GraphRAG, régler alpha, beta, gamma, évaluer en recall@k et MRR face aux lignes de base | Pipeline fonctionnel et rapport d'évaluation (note du module)

Module 3 : Enterprise AI Architecture
C1 : Router-Dispatcher (2 h)
Objectifs : concevoir un aiguillage entre petits et grands modèles.
Principe : un routeur analyse la requête (longueur, complexité, domaine, sensibilité) et la dirige vers un SLM (rapide, peu coûteux) ou un LLM (plus capable, plus lent et coûteux).
Stratégies de routage : règles explicites ; classifieur léger entraîné sur des requêtes étiquetées ; cascade (essayer le SLM, escalader vers le LLM si la confiance est faible).
Critères d'évaluation : coût moyen par requête, latence, qualité de réponse, taux d'escalade. Le piège classique est de sous-estimer le coût d'un mauvais routage.

C2 : Cache sémantique (2 h)
Objectifs : réduire la latence et le coût en réutilisant des réponses.
Principe : au lieu d'une clé exacte, on compare le plongement de la requête à ceux des requêtes déjà traitées. Si la similarité dépasse un seuil, on renvoie la réponse stockée sans appeler le modèle, ce qui réduit fortement le TTFT.
Points clés : seuil de similarité ; invalidation (durée de vie, versionnage des données sources) ; sécurité (ne jamais mettre en cache des réponses contenant des données personnelles, cloisonner le cache par utilisateur ou par droit d'accès).

C3 : Agents ReAct (2 h)
Objectifs : comprendre la boucle d'un agent qui raisonne et agit.
Boucle : Pensée (que faut-il faire ?), Action (appel d'un outil), Observation (résultat de l'outil), puis nouvelle pensée, jusqu'à une réponse finale.
Bonnes pratiques : liste d'outils restreinte et typée, nombre maximal d'itérations, journalisation de chaque étape, validation des paramètres d'outils. Risques : boucles infinies, appels d'outils coûteux, injection de prompt via les observations.

C4 : Circuit Breakers et résilience (2 h)
Objectifs : empêcher qu'une panne locale ne devienne une panne générale.
Circuit Breaker : trois états. Fermé : les appels passent. Ouvert : après un seuil d'échecs ou de lenteurs, les appels sont refusés immédiatement. Semi-ouvert : après un délai, quelques appels de test ; s'ils réussissent, retour à fermé.
Patterns associés : timeouts, reprises avec attente exponentielle et gigue, limitation de débit, bulkheads, dégradation gracieuse.

C5 : Concevoir une passerelle d'inférence (2 h)
Objectifs : assembler les patterns dans une architecture de production.
Composants : authentification, limitation de débit, guardrails d'entrée, cache sémantique, routeur, appel de modèle protégé par Circuit Breaker, guardrails de sortie, journalisation.
Observabilité : latence (p50, p95, p99), TTFT, taux d'erreur, taux d'accès au cache, coût par requête, taux d'escalade. Passage à l'échelle : instances sans état, cache partagé, files d'attente.

T1 à T4 : Travaux pratiques (15 h)
TP | Consigne | Livrable et critères
T1 (4 h) | Implémenter un routeur à règles puis une cascade avec seuil de confiance (modèles simulés) | Mesure du coût et de la qualité par stratégie
T2 (4 h) | Implémenter le cache sémantique avec seuil réglable et expiration | Taux d'accès au cache, courbe erreurs en fonction du seuil
T3 (4 h) | Écrire une boucle ReAct avec deux outils, plafond d'itérations et Circuit Breaker | Journal d'exécution, test avec un outil en panne
T4 (3 h) | Assembler la passerelle et la soumettre à un test de charge | Rapport de latence et de résilience (note du module)

Module 4 : LoRA & Edge ML
C1 : Décomposition à bas rang (2 h)
Objectifs : comprendre pourquoi et comment LoRA adapte un modèle avec très peu de paramètres.
Idée : lors du fine-tuning, la mise à jour des poids d'une matrice W₀ (de dimensions d × k) a souvent un rang effectif faible. On la paramètre donc par deux petites matrices : delta_W = (alpha / r) · B · A, avec B de dimensions d × r et A de dimensions r × k, où r est le rang (très inférieur à d et k).
Passe avant : h = W₀ · x + (alpha / r) · B · A · x
Initialisation et entraînement : W₀ est gelée ; A est initialisée aléatoirement (gaussienne) et B à zéro, de sorte que le modèle adapté démarre exactement comme le modèle de base. Seuls A et B sont entraînées. Le facteur alpha / r règle l'amplitude de l'adaptation.
Gain en paramètres : on passe de d · k paramètres entraînables à r · (d + k). Pour d = k = 4096 et r = 8, cela fait 65 536 au lieu de 16 777 216, soit environ 0,4 %.

C2 : Mémoire GPU et contraintes Edge (2 h)
Objectifs : estimer et réduire l'empreinte mémoire d'un entraînement.
Postes de mémoire : poids du modèle, gradients, états de l'optimiseur, activations. Avec LoRA, les gradients et états d'optimiseur ne concernent que A et B. Leviers complémentaires : précision réduite, accumulation de gradients, recalcul des activations, choix des couches adaptées.
Contraintes IoT / mobile : mémoire limitée, énergie, connectivité intermittente, chauffe. Le cours amène à raisonner en budget : combien de mégaoctets, combien de secondes par tour local.

C3 : LoRA et apprentissage fédéré (2 h)
Objectifs : réduire le coût de communication d'un système fédéré.
Principe : au lieu d'échanger toutes les matrices à chaque tour, les clients n'envoient que les matrices A et B. Le volume de communication par tour est divisé d'un facteur proche du gain en paramètres de C1.
Point d'attention : l'agrégation. Moyenner A et B séparément n'équivaut pas à moyenner les produits B · A ; l'agrégation introduit une erreur. Pistes : agréger les produits reconstruits (puis re-factoriser), ou utiliser des variantes conçues pour ce problème. Le TP mesure l'écart.
Compatibilité : LoRA se combine avec le terme proximal de FedProx (appliqué aux paramètres A et B) et avec le clipping et le bruit de DP-SGD.

T1 à T4 : Travaux pratiques (14 h)
TP | Consigne | Livrable et critères
T1 (4 h) | Implémenter une couche linéaire LoRA from scratch (passe avant, gradients de A et B, initialisation), vérifier que la sortie initiale égale celle de W₀ | Code testé, test numérique de gradient
T2 (4 h) | Mesurer paramètres entraînables et mémoire estimée pour r = 1, 2, 4, 8, 16, 32 | Tableau et courbe du ratio de compression
T3 (3 h) | Intégrer LoRA dans un client fédéré du module 1 et agréger A et B | Cluster fédéré en mode LoRA
T4 (3 h) | Comparer précision finale et volume de communication entre fédéré complet et fédéré LoRA | Rapport d'évaluation (note du module)

Module 5 : Gouvernance, sécurité & LLM Guardrails
C1 : Données personnelles et conformité (2 h)
Objectifs : identifier les données à protéger et les obligations associées.
Notions :
• PII : identifiants directs (nom, e-mail, téléphone, numéro de sécurité sociale) et indirects (combinaison de date de naissance, code postal, sexe). Les données de santé sont une catégorie particulièrement sensible.
• RGPD : principes de minimisation, limitation des finalités, durée de conservation, droits des personnes. Anonymisation (irréversible, hors champ du RGPD) contre pseudonymisation (réversible avec une clé, encore couverte par le RGPD).
• Où appliquer le contrôle : avant l'ingestion dans le graphe, avant l'envoi à un modèle, avant l'écriture dans les journaux et dans le cache.

C2 : Injection de prompt (2 h)
Objectifs : comprendre les attaques et les défenses en couches.
Injection directe : l'utilisateur écrit des instructions qui tentent de contourner les consignes du système.
Injection indirecte : les instructions malveillantes se cachent dans un contenu récupéré (page web, document, résultat d'outil, entrée du graphe) que le modèle traite comme fiable.
Défenses, aucune n'étant suffisante seule :
• séparer clairement instructions et données non fiables dans le prompt ;
• détecter les motifs d'attaque connus et classer les entrées suspectes ;
• principe du moindre privilège pour les outils ;
• valider et filtrer les sorties avant toute action ou affichage ;
• tests adverses réguliers (red teaming).

C3 : Architecture de guardrails (2 h)
Objectifs : placer les contrôles au bon endroit du flux.
Flux : entrée utilisateur, guardrail d'entrée (masquage PII, détection d'injection, refus des sujets hors périmètre), traitement (récupération, modèle, outils), guardrail de sortie (détection de fuite de PII, cohérence avec les sources, format attendu), réponse.
Compromis : faux positifs contre faux négatifs ; latence ajoutée ; journalisation des décisions pour audit, sans y stocker de données personnelles.

T1 à T4 : Travaux pratiques (14 h)
TP | Consigne | Livrable et critères
T1 (4 h) | Détecter e-mails, téléphones et numéros de sécurité sociale par expressions régulières ; mesurer précision et rappel sur un jeu annoté | Détecteur et métriques
T2 (4 h) | Masquer ou pseudonymiser les PII détectées, de façon réversible ou non selon l'usage | Module de masquage et tests
T3 (3 h) | Écrire un détecteur d'injection directe et indirecte (motifs et règles de structure) | Détecteur et jeu d'attaques
T4 (3 h) | Assembler le pipeline d'entrée et de sortie et l'évaluer sur un jeu de tests adverses | Rapport de faux positifs et faux négatifs (note du module)

Projet fil rouge : cahier des charges détaillé
Contexte : trois établissements hospitaliers simulés veulent entraîner ensemble un modèle d'aide au diagnostic et interroger une base de connaissances médicale, sans partager les dossiers patients.
Livrables techniques :
1. Cluster fédéré FedProx avec DP-SGD sur des données non-i.i.d. simulées.
2. Meaning Graph médical (maladies, symptômes, traitements, contre-indications) et recherche GraphRAG hybride.
3. Passerelle d'inférence avec routeur, cache sémantique et Circuit Breakers.
4. Mode LoRA pour un établissement à ressources limitées.
5. Guardrails d'entrée et de sortie : masquage PII et défense contre l'injection de prompt.
6. Rapport d'architecture et démonstration.
Contraintes : données entièrement simulées (aucune donnée réelle), code Python reproductible avec graine aléatoire fixée, journal de décisions techniques, travail en équipe avec répartition des rôles documentée.

Grille de soutenance sur 20 points (proposition à valider par l'équipe pédagogique) :
Critère | Points
Cluster fédéré et confidentialité (FedProx, DP-SGD, robustesse) | 5
Meaning Graph et GraphRAG (qualité du graphe, évaluation) | 4
Passerelle d'inférence et résilience | 3
LoRA et réduction de communication | 2
Guardrails (PII, injection) | 3
Qualité de la présentation et de la documentation | 3
Total | 20

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

