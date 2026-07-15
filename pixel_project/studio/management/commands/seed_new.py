from django.core.management.base import BaseCommand
from studio.models import MenuItem, TableRestaurant, SoftCodeModule, StudioProject3D, PatisserieRecipe, PatisserieProduct

class Command(BaseCommand):
    help = 'Seed data for Restaurant, PixelSoftCode, InnerStudio, Patisserie'

    def handle(self, *args, **kwargs):
        # Restaurant
        items = [
            ("Café express", "boisson", 3.5), ("Thé à la menthe", "boisson", 2.5),
            ("Jus d'orange frais", "boisson", 6.0), ("Eau minérale", "boisson", 1.5),
            ("Croissant", "snack", 3.0), ("Pain au chocolat", "snack", 3.5),
            ("Salade César", "entree", 12.0), ("Brick à l'œuf", "entree", 5.0),
            ("Couscous merguez", "plat", 18.0), ("Grillade mixte", "plat", 25.0),
            ("Poulet rôti frites", "plat", 16.0), ("Poisson grillé", "plat", 22.0),
            ("Pizza Margherita", "plat", 14.0), ("Pizza 4 saisons", "plat", 18.0),
            ("Tajine poulet", "plat", 20.0), ("Lasagnes bolognaise", "plat", 16.0),
            ("Salade tunisienne", "entree", 8.0), ("Mechouia", "entree", 7.0),
            ("Fricassé", "snack", 4.0), ("Merguez frites", "plat", 12.0),
            ("Crêpe Nutella", "dessert", 8.0), ("Salade de fruits", "dessert", 6.0),
            ("Tarte au citron", "dessert", 7.0), ("Mousse au chocolat", "dessert", 7.0),
            ("Petit-déjeuner complet", "petit-dej", 15.0), ("Omelette", "petit-dej", 8.0),
        ]
        for nom, cat, prix in items:
            MenuItem.objects.get_or_create(nom=nom, defaults={"categorie": cat, "prix": prix})
        self.stdout.write(f"✓ {MenuItem.objects.count()} articles menu créés")

        tables_data = [("1", 2), ("2", 2), ("3", 4), ("4", 4), ("5", 4), ("6", 6), ("7", 6), ("8", 8), ("Terrasse A", 4), ("Terrasse B", 4), ("VIP", 10)]
        for num, cap in tables_data:
            TableRestaurant.objects.get_or_create(numero=num, defaults={"capacite": cap})
        self.stdout.write(f"✓ {TableRestaurant.objects.count()} tables créées")

        # PixelSoftCode
        modules = [
            ("Auth & User Management", "Authentification", "2.3.0", 0),
            ("Paiement & Facturation", "Finance", "1.8.0", 2900),
            ("Mobile SDK Flutter", "Mobile", "3.0.0", 1500),
            ("IA & Machine Learning", "IA", "1.2.0", 4500),
            ("BI & Analytics", "Data", "2.0.0", 3500),
            ("IoT & Connectivité", "IoT", "1.5.0", 2800),
            ("Document & Workflow", "Productivité", "2.1.0", 1900),
            ("Multitenant SaaS", "Infrastructure", "1.9.0", 5900),
            ("API Gateway", "Infrastructure", "2.0.0", 2200),
            ("Notifications", "Communication", "1.4.0", 800),
            ("Export PDF/ODT", "Productivité", "1.1.0", 0),
            ("Signature électronique", "Sécurité", "1.0.0", 1200),
        ]
        for nom, cat, ver, prix in modules:
            SoftCodeModule.objects.get_or_create(nom=nom, defaults={"categorie": cat, "version": ver, "prix": prix})
        self.stdout.write(f"✓ {SoftCodeModule.objects.count()} modules créés")

        # InnerStudio
        projects_3d = [
            ("Villa moderne Sidi Bou Said", "architecture"),
            ("Appartement luxe Lac 2", "interieur"),
            ("Bureau open space Tunis", "interieur"),
            ("Restaurant panoramique", "architecture"),
            ("Centre commercial Ennasr", "architecture"),
            ("Maison traditionnelle", "architecture"),
            ("Showroom automobile", "exterieur"),
            ("Jardin paysager", "exterieur"),
            ("Hôtel 5 étoiles Djerba", "architecture"),
            ("Cuisine équipée moderne", "interieur"),
            ("Salle de bain spa", "interieur"),
            ("Pont métallique", "mecanique"),
        ]
        for nom, cat in projects_3d:
            StudioProject3D.objects.get_or_create(nom=nom, defaults={"categorie": cat})
        self.stdout.write(f"✓ {StudioProject3D.objects.count()} projets 3D créés")

        # Patisserie
        recipes = [
            ("Croissant pur beurre", "boulangerie", 0.8, 2.5),
            ("Pain au chocolat", "boulangerie", 0.9, 3.0),
            ("Baguette tradition", "boulangerie", 0.5, 1.2),
            ("Pain complet", "boulangerie", 0.6, 1.5),
            ("Gâteau au chocolat", "patisserie", 4.0, 12.0),
            ("Tiramisu", "patisserie", 3.5, 10.0),
            ("Mousse aux fruits rouges", "patisserie", 3.0, 9.0),
            ("Tarte aux pommes", "patisserie", 2.5, 8.0),
            ("Paris-Brest", "patisserie", 3.8, 11.0),
            (" religieuse au café", "patisserie", 1.5, 4.5),
            ("Mille-feuille", "patisserie", 2.8, 7.0),
            ("Macarons (boîte 6)", "patisserie", 3.0, 9.0),
            ("Truffes au chocolat", "chocolaterie", 2.0, 6.0),
            ("Tablette de chocolat noir", "chocolaterie", 1.5, 5.0),
            ("Glace vanille (pot 1L)", "glacier", 2.5, 8.0),
            ("Sorbet citron (pot 1L)", "glacier", 2.0, 7.0),
        ]
        for nom, cat, cout, pv in recipes:
            PatisserieRecipe.objects.get_or_create(nom=nom, defaults={"categorie": cat, "cout_production": cout, "prix_vente": pv})
        self.stdout.write(f"✓ {PatisserieRecipe.objects.count()} recettes créées")

        products = [
            ("Croissant", "Croissant pur beurre", 50, 2.5),
            ("Pain au chocolat", "Pain au chocolat", 40, 3.0),
            ("Baguette", "Baguette tradition", 100, 1.2),
            ("Pain complet", "Pain complet", 30, 1.5),
            ("Gâteau chocolat entier", "Gâteau au chocolat", 5, 35.0),
            ("Tiramisu verrine", "Tiramisu", 20, 10.0),
        ]
        for nom, recette_nom, stock, prix in products:
            rec = PatisserieRecipe.objects.filter(nom=recette_nom).first()
            PatisserieProduct.objects.get_or_create(nom=nom, defaults={"recette": rec, "stock_actuel": stock, "prix_vente": prix})
        self.stdout.write(f"✓ {PatisserieProduct.objects.count()} produits créés")

        self.stdout.write(self.style.SUCCESS("✔ Toutes les données seed ont été insérées !"))
