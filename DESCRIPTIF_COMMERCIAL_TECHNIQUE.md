# Descriptif Commercial & Technique — Pixel Software Design

---

## Partie Commerciale

### 1. Présentation Produit

Pixel Software Design édite 4 solutions logicielles couvrant des secteurs complémentaires :

| Produit | Description | Public |
|---------|-------------|--------|
| **GestiActiv ERP** | ERP SaaS multi-secteurs pour PME/ETI tunisiennes. Centralise gestion, comptabilité, stocks, paie, CRM, production. | Auto-écoles, cliniques, hôtels, commerces, cabinets juridiques, industries |
| **Restaurant & Café** | Solution de gestion complète pour la restauration : caisse, commandes, stocks, fidélité, livraison. | Restaurants, cafés, fast-foods, food-trucks, hôtels (brasseries) |
| **PixelSoftCode** | Plateforme SaaS de gestion de projets, ticketing, code review et déploiement continu (DevOps). | DSI, ESN, équipes tech, startups, PME en transformation digitale |
| **Inner Studio 3D** | Moteur de conception 3D pour l'architecture d'intérieur : rendu temps réel, catalogues, devis. | Architectes, décorateurs, promoteurs immobiliers, menuisiers |

### 2. Fonctionnalités Clés par Module

#### GestiActiv ERP
- Comptabilité PCG Tunisien (journal, bilan, TVA, déclarations)
- Gestion des stocks multi-dépôts
- Facturation (devis, BDC, factures TVA, encaissements)
- CRM & gestion de la relation client
- Paie & RH (bulletins, CNSS, IRPP, congés)
- Production & atelier (OF, nomenclature, coûts)
- Application mobile (indicateurs, validations, notifications)

#### Restaurant & Café
- Caisse enregistreuse tactile
- Gestion des commandes (salle, emporter, livraison)
- Menu digital & QR code
- Gestion des stocks périssables
- Fidélité client & programmes de points
- Livraison & rapprochement livreurs
- Tableau de bord des ventes en temps réel

#### PixelSoftCode
- Gestion de projets (Kanban, Scrum, Gantt)
- Ticketing & suivi des incidents
- Code review & gestion de versions
- CI/CD intégré
- Wiki & documentation
- Statistiques & rapports de productivité

#### Inner Studio 3D
- Conception 3D d'espaces intérieurs
- Rendu photo-réaliste temps réel
- Catalogue de matériaux et mobilier
- Générateur de devis automatique
- Export plans techniques
- Bibliothèque de projets

### 3. Avantages Concurrentiels

1. **100% Tunisien** — Solutions développées en Tunisie, conformes aux normes locales (TVA, PCG, CNSS, CNAM, IRPP)
2. **Multi-plateforme** — Web (React/Angular), Mobile (Flutter), Desktop (JavaFX) — expérience homogène
3. **Modulaire et évolutif** — Choix des modules, ajout au fil du temps. Paiement à l'usage
4. **SaaS ou On-Premise** — Hébergé dans nos datacenters ou installé chez le client
5. **Accompagnement local** — Formation, déploiement et support assurés par une équipe basée à Tunis
6. **Sécurité multi-tenant** — Isolation des données par client (RLS), conformité RGPD

### 4. Public Cible

- Directeurs d'établissements et gérants de PME/ETI
- Auto-écoles, cliniques, hôtels, commerces, restaurants
- Cabinets juridiques et cabinets de conseil
- Architectes, décorateurs, promoteurs immobiliers
- DSI et équipes techniques (ESN, startups)
- Toute entreprise cherchant à digitaliser sa gestion sans multiplier les outils

### 5. Licence

**Pixel Software Design © 2026**

Tous droits réservés. Les logiciels GestiActiv ERP, Restaurant & Café, PixelSoftCode et Inner Studio 3D sont des oeuvres originales de Pixel Software Design.

- Licence commerciale annuelle par utilisateur
- Clés de licence HMAC pour les déploiements On-Premise
- Version communautaire open source disponible pour GestiActiv ERP (modules de base)
- SLA et support technique inclus selon l'abonnement
- Hébergement SaaS avec garantie de disponibilité 99.9%

---

## Partie Technique

### 1. Architecture Globale

`
+-----------------------------------------------------------+
|                     Client Layer                           |
|  +----------+  +----------+  +--------------------+        |
|  |   Web    |  |  Mobile  |  |  Desktop (JavaFX)  |        |
|  | (React/  |  | (Flutter)|  |  (GestiActiv ERP   |        |
|  |  Angular)|  |          |  |   Restaurant)      |        |
|  +----+-----+  +----+-----+  +--------+----------+        |
|       |             |                  |                   |
+-------+-------------+------------------+-------------------+
|                       API Gateway                          |
|               Spring Cloud Gateway / Nginx                 |
+-----------------------------------------------------------+
|                      Microservices                         |
|  +---------+ +----------+ +----------+ +-----------+       |
|  | Auth    | |  ERP     | |  Restau  | |  Paiement |       |
|  | Service | |  Service | |  Service | |  Service  |       |
|  +---------+ +----------+ +----------+ +-----------+       |
|  +---------+ +----------+ +----------+ +-----------+       |
|  | Notif   | |  Report  | |  Catalog | |  Devis    |       |
|  | Service | |  Service | |  Service | |  Service  |       |
|  +---------+ +----------+ +----------+ +-----------+       |
+-----------------------------------------------------------+
|                       Data Layer                           |
|  +----------+  +----------+  +----------------------+      |
|  |PostgreSQL|  |  Redis   |  |  MinIO (Documents)   |      |
|  +----------+  +----------+  +----------------------+      |
+-----------------------------------------------------------+
`

### 2. Stack Technique Complet

#### Backend (Java)
| Technologie | Version |
|-------------|---------|
| Java | 17 (LTS) |
| Spring Boot | 3.2.x |
| Spring Security + JWT | 6.x |
| Spring Data JPA / Hibernate | 6.x |
| PostgreSQL (driver) | 42.7.x |
| Flyway (migrations) | 10.x |
| Redis (cache) | 7.x |
| RabbitMQ / Kafka (messaging) | 3.x / 3.6.x |
| OpenAPI / Swagger | 2.x |
| MapStruct | 1.5.x |
| Maven | 3.9.x |

#### Frontend Web
| Technologie | Version |
|-------------|---------|
| React | 18.x |
| Angular | 17.x |
| TypeScript | 5.x |
| Vite / Webpack | 5.x |
| Tailwind CSS / PrimeNG | 3.x / 17.x |
| RxJS | 7.x |

#### Mobile
| Technologie | Version |
|-------------|---------|
| Flutter | 3.29.x |
| Dart | 3.x |
| GetX / Riverpod | 4.x / 2.x |

#### Desktop
| Technologie | Version |
|-------------|---------|
| JavaFX | 21.x |
| ControlsFX | 11.x |
| JFoenix | 9.x |

#### Infrastructure
| Technologie | Version |
|-------------|---------|
| Docker / Docker Compose | 24.x / 2.x |
| Kubernetes | 1.29.x |
| Nginx | 1.24.x |
| Keycloak (SSO) | 23.x |
| Grafana + Prometheus | 10.x / 2.x |
| Jenkins / GitLab CI | 2.x |

### 3. Structure du Projet Multi-Module

`
pixel-project/
  pixel-api/                 # API Gateway (Spring Cloud Gateway)
  pixel-auth-service/        # Authentification, inscription, rôles
    src/main/java/com/pixel/auth/
    src/main/resources/
    pom.xml
  pixel-erp-service/         # Coeur ERP
    src/main/java/com/pixel/erp/
      controller/        # REST controllers
      service/           # Business logic
      repository/        # JPA repositories
      entity/            # JPA entities
      dto/               # Data transfer objects
      mapper/            # MapStruct mappers
    src/main/resources/
      db/migration/      # Flyway SQL migrations
    pom.xml
  pixel-restaurant-service/  # Restaurant & Café
  pixel-pixelsoft-service/   # PixelSoftCode
  pixel-innerstudio-service/ # Inner Studio 3D
  pixel-notification-service/# Emails, SMS, push
  pixel-payment-service/     # Stripe + D17
  pixel-report-service/      # JasperReports, PDF
  pixel-catalog-service/     # Produits, matériaux
  pixel-front-web/           # React/Angular SPA
    src/
      components/
      pages/
      services/
      assets/
    package.json
  pixel-front-mobile/        # Flutter app
    lib/
      screens/
      widgets/
      models/
      services/
    pubspec.yaml
  pixel-front-desktop/       # JavaFX desktop
    src/main/java/com/pixel/desktop/
    pom.xml
  docker-compose.yml
  kubernetes/
  docs/
    architecture.md
    api/
    database/
`

### 4. Base de Données (17 Tables)

#### Tables Principales
| # | Table | Description | Module |
|---|-------|-------------|--------|
| 1 | users | Utilisateurs (auth, rôles, profil) | Auth |
| 2 | oles | Rôles et permissions (RBAC) | Auth |
| 3 | user_roles | Assignation des rôles | Auth |
| 4 | clients | Clients / comptes (multi-tenant) | ERP |
| 5 | products | Produits et services | ERP |
| 6 | invoices | Factures (TVA tunisienne) | ERP |
| 7 | invoice_lines | Lignes de facture | ERP |
| 8 | stock_movements | Mouvements de stock | ERP |
| 9 | suppliers | Fournisseurs | ERP |
| 10 | orders | Commandes et devis | ERP |
| 11 | employees | Employés et paie (CNSS, IRPP) | RH |
| 12 | payroll | Bulletins de paie | RH |
| 13 | cnam_transactions | Facturation CNAM (Santé) | Santé |
| 14 | estaurant_orders | Commandes restaurant | Resto |
| 15 | menu_items | Articles de menu | Resto |
| 16 | projects | Projets et tickets | PixelSoftCode |
| 17 | project_tasks | Tâches et sous-tâches | PixelSoftCode |

#### Schéma Relationnel (extrait)
`
users ---- user_roles ---- roles
  |
  +--- clients (multi-tenant)
  |       +--- invoices ---- invoice_lines
  |       +--- orders
  |       +--- products ---- stock_movements
  |       +--- suppliers
  |
  +--- employees ---- payroll
  |
  +--- cnam_transactions
`

### 5. API REST (12 Endpoints)

#### Authentification
| Méthode | Endpoint | Description |
|---------|----------|-------------|
| POST | /api/v1/auth/register | Inscription utilisateur |
| POST | /api/v1/auth/login | Connexion (JWT) |
| POST | /api/v1/auth/refresh | Rafraîchir token |
| GET | /api/v1/auth/me | Profil connecté |

#### ERP
| Méthode | Endpoint | Description |
|---------|----------|-------------|
| GET | /api/v1/erp/invoices | Liste des factures |
| POST | /api/v1/erp/invoices | Créer une facture |
| GET | /api/v1/erp/invoices/{id} | Détail facture |
| GET | /api/v1/erp/stock | État des stocks |

#### Restaurant
| Méthode | Endpoint | Description |
|---------|----------|-------------|
| POST | /api/v1/resto/orders | Créer commande |
| GET | /api/v1/resto/orders/{id} | Suivi commande |

#### Paiement
| Méthode | Endpoint | Description |
|---------|----------|-------------|
| POST | /api/v1/payments/charge | Paiement Stripe/D17 |
| GET | /api/v1/payments/status/{id} | Statut paiement |

### 6. Déploiement

#### Environnement de Développement
`ash
docker-compose up -d                    # PostgreSQL, Redis, Keycloak
mvn clean install -DskipTests           # Build modules
./mvnw spring-boot:run -pl pixel-erp-service  # Lancer service
`

#### Environnement de Production
`yaml
# docker-compose.prod.yml
services:
  gateway:
    image: pixel/gateway:latest
    ports: ["443:443"]
    depends_on: [auth-service, erp-service]
  auth-service:
    image: pixel/auth-service:latest
    environment:
      - DB_URL=jdbc:postgresql://db:5432/pixel_auth
      - REDIS_HOST=redis
  erp-service:
    image: pixel/erp-service:latest
    environment:
      - DB_URL=jdbc:postgresql://db:5432/pixel_erp
  db:
    image: postgres:16
    volumes: [pgdata:/var/lib/postgresql/data]
  redis:
    image: redis:7-alpine
`

#### Mobile (Flutter)
`ash
flutter build apk          # Android
flutter build ios           # iOS
flutter build windows       # Windows Desktop
`

### 7. Conformités

#### NACEF (Nomenclature d'Activités des Codes d'Établissement Financier)
- GestiActiv ERP supporte la codification NACEF pour la classification des établissements financiers et entreprises
- Les modules comptabilité et facturation intègrent les codes NACEF dans les déclarations TVA et bilans comptables
- Conforme à la réglementation de la Banque Centrale de Tunisie pour les échanges financiers

#### TTN / El Fatoora (Facturation Électronique Tunisienne)
- Les modules de facturation supportent le format XML structuré conforme à la plateforme El Fatoora
- Signature électronique des factures via clés HMAC et certificats numériques
- Transmission automatique des factures électroniques à la plateforme TTN
