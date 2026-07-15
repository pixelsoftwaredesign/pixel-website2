import json
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import MenuItem, TableRestaurant, SoftCodeModule, StudioProject3D, PatisserieRecipe, PatisserieProduct, ERPClient, ERPModule, ERPSubscription, PlanAbonnement, SouscriptionClient, Paiement, CleActivation, ConfigurationBancaire, Candidature, Categorie, Produit, CommandeECommerce, CommandeECommerceItem, MouvementStock

class LandingPageTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='admin', password='admin123')

    def _login(self):
        self.client.login(username='admin', password='admin123')

    def test_restaurant_landing_200(self):
        r = self.client.get('/restaurant/')
        self.assertEqual(r.status_code, 200)

    def test_pixelsoftcode_landing_200(self):
        r = self.client.get('/pixelsoftcode/')
        self.assertEqual(r.status_code, 200)

    def test_innerstudio_landing_200(self):
        r = self.client.get('/innerstudio/')
        self.assertEqual(r.status_code, 200)

    def test_patisserie_landing_200(self):
        r = self.client.get('/patisserie/')
        self.assertEqual(r.status_code, 200)

    def test_restaurant_management_200(self):
        self._login()
        r = self.client.get('/restaurant/management/')
        self.assertEqual(r.status_code, 200)

    def test_pixelsoftcode_management_200(self):
        self._login()
        r = self.client.get('/pixelsoftcode/management/')
        self.assertEqual(r.status_code, 200)

    def test_innerstudio_management_200(self):
        self._login()
        r = self.client.get('/innerstudio/management/')
        self.assertEqual(r.status_code, 200)

    def test_patisserie_management_200(self):
        self._login()
        r = self.client.get('/patisserie/management/')
        self.assertEqual(r.status_code, 200)

    def test_atelierdev_live_stats(self):
        r = self.client.get('/atelierdev/')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Projets publiés')

    def test_index_live_stats(self):
        r = self.client.get('/')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Projets livrés')

    def test_login_page_200(self):
        r = self.client.get('/login/')
        self.assertEqual(r.status_code, 200)

    def test_register_page_200(self):
        r = self.client.get('/register/')
        self.assertEqual(r.status_code, 200)

    def test_prix_page_200(self):
        r = self.client.get('/prix/')
        self.assertEqual(r.status_code, 200)

    def test_logiciel_offline_200(self):
        r = self.client.get('/logiciel-offline/')
        self.assertEqual(r.status_code, 200)

    def test_subscriptions_page_200(self):
        self._login()
        r = self.client.get('/subscriptions/')
        self.assertEqual(r.status_code, 200)


class CRUDTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('admin', 'a@a.com', 'test')
        self.client.force_login(self.user)

    def test_restaurant_add_menu_item(self):
        count = MenuItem.objects.count()
        r = self.client.post('/restaurant/management/', {'action': 'add_menu', 'nom': 'Test Pizza', 'prix': 15, 'disponible': '1'}, follow=True)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(MenuItem.objects.count(), count + 1)

    def test_restaurant_add_table(self):
        count = TableRestaurant.objects.count()
        r = self.client.post('/restaurant/management/', {'action': 'add_table', 'numero': '99', 'capacite': 6, 'statut': 'libre'}, follow=True)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(TableRestaurant.objects.count(), count + 1)

    def test_pixelsoftcode_add_module(self):
        count = SoftCodeModule.objects.count()
        r = self.client.post('/pixelsoftcode/management/', {'action': 'add_module', 'nom': 'Test Module', 'categorie': 'Test', 'version': '1.0', 'prix': 0, 'disponible': '1'}, follow=True)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(SoftCodeModule.objects.count(), count + 1)

    def test_innerstudio_add_project(self):
        count = StudioProject3D.objects.count()
        r = self.client.post('/innerstudio/management/', {'action': 'add_project', 'nom': 'Test Projet', 'categorie': 'architecture'}, follow=True)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(StudioProject3D.objects.count(), count + 1)

    def test_patisserie_add_recipe(self):
        count = PatisserieRecipe.objects.count()
        r = self.client.post('/patisserie/management/', {'action': 'add_recipe', 'nom': 'Test Recette', 'categorie': 'patisserie', 'cout_production': 2, 'prix_vente': 8}, follow=True)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(PatisserieRecipe.objects.count(), count + 1)

    def test_patisserie_add_product(self):
        recipe = PatisserieRecipe.objects.create(nom='Base', categorie='patisserie')
        count = PatisserieProduct.objects.count()
        r = self.client.post('/patisserie/management/', {'action': 'add_product', 'nom': 'Test Prod', 'recette': recipe.id, 'stock_actuel': 10, 'prix_vente': 5, 'actif': '1'}, follow=True)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(PatisserieProduct.objects.count(), count + 1)

    def test_restaurant_edit_menu_item(self):
        item = MenuItem.objects.create(nom='Old', categorie='plat', prix=10)
        r = self.client.post('/restaurant/management/', {'action': 'add_menu', 'edit_id': item.id, 'nom': 'Edited', 'prix': 20, 'disponible': '1'}, follow=True)
        self.assertEqual(r.status_code, 200)
        item.refresh_from_db()
        self.assertEqual(item.nom, 'Edited')
        self.assertEqual(float(item.prix), 20.0)

    def test_restaurant_delete_menu_item(self):
        item = MenuItem.objects.create(nom='ToDelete', categorie='plat', prix=5)
        count = MenuItem.objects.count()
        r = self.client.post('/restaurant/management/', {'action': 'delete', 'model': 'menu', 'id': item.id}, follow=True)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(MenuItem.objects.count(), count - 1)


class SubscriptionTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='subadmin', password='subpass')
        self.client.force_login(self.user)
        self.client2 = ERPClient.objects.create(company_name='Test Corp', contact_name='Test', email='t@t.com')
        self.module = ERPModule.objects.create(slug='test-module', name='Test Module', icon='📦')

    def test_subscription_add(self):
        count = ERPSubscription.objects.count()
        r = self.client.post('/subscriptions/', {'action': 'add_sub', 'client': self.client2.id, 'module': self.module.id, 'is_active': '1'}, follow=True)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(ERPSubscription.objects.count(), count + 1)

    def test_subscription_edit(self):
        sub = ERPSubscription.objects.create(client=self.client2, module=self.module, is_active=True)
        r = self.client.post('/subscriptions/', {'action': 'add_sub', 'edit_id': sub.id, 'client': self.client2.id, 'module': self.module.id, 'is_active': '0'}, follow=True)
        self.assertEqual(r.status_code, 200)
        sub.refresh_from_db()
        self.assertFalse(sub.is_active)

    def test_subscription_delete(self):
        sub = ERPSubscription.objects.create(client=self.client2, module=self.module, is_active=True)
        count = ERPSubscription.objects.count()
        r = self.client.post('/subscriptions/', {'action': 'delete', 'model': 'subscription', 'id': sub.id}, follow=True)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(ERPSubscription.objects.count(), count - 1)


class AbonnementTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.plan = PlanAbonnement.objects.create(nom='Test Pro', slug='test-pro', categorie='erp', prix=100, duree_jours=365, features='Feature 1\nFeature 2')

    def test_choisir_page_200(self):
        r = self.client.get('/abonnement/')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Test Pro')

    def test_souscrire_page_200(self):
        r = self.client.get('/abonnement/test-pro/')
        self.assertEqual(r.status_code, 200)

    def test_souscrire_post_cash(self):
        count = SouscriptionClient.objects.count()
        r = self.client.post('/abonnement/test-pro/', {'nom': 'Test User', 'email': 'test@test.com', 'methode': 'especes'}, follow=True)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(SouscriptionClient.objects.count(), count + 1)
        sub = SouscriptionClient.objects.last()
        self.assertIn('/abonnement/' + str(sub.id) + '/cash/', r.redirect_chain[0][0])

    def test_souscrire_post_online(self):
        r = self.client.post('/abonnement/test-pro/', {'nom': 'Test Online', 'email': 'online@test.com', 'methode': 'online'}, follow=True)
        self.assertEqual(r.status_code, 200)
        sub = SouscriptionClient.objects.last()
        self.assertIn('/online/', r.redirect_chain[0][0])

    def test_cash_activation(self):
        sub = SouscriptionClient.objects.create(client_nom='Cash', client_email='c@c.com', plan=self.plan)
        paiement = Paiement.objects.create(souscription=sub, methode='especes', montant=100, reference='CASH-TEST')
        cle = CleActivation.objects.create(souscription=sub, code='PXL-TESTKEY123')
        r = self.client.post(f'/abonnement/{sub.id}/cash/', {'code': 'PXL-TESTKEY123'}, follow=True)
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'activé')
        cle.refresh_from_db()
        self.assertTrue(cle.est_utilisee)
        sub.refresh_from_db()
        self.assertEqual(sub.status, 'actif')

    def test_virement_page_with_bank(self):
        bank = ConfigurationBancaire.objects.create(banque='BIAT', titulaire='Pixel Test', rib='0800123456789012345678', est_defaut=True)
        sub = SouscriptionClient.objects.create(client_nom='Vir', client_email='v@v.com', plan=self.plan)
        Paiement.objects.create(souscription=sub, methode='virement', montant=100, reference='VIR-TEST')
        r = self.client.get(f'/abonnement/{sub.id}/virement/')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'BIAT')

    def test_api_verifier_cle(self):
        sub = SouscriptionClient.objects.create(client_nom='API', client_email='a@a.com', plan=self.plan)
        CleActivation.objects.create(souscription=sub, code='PXL-APITEST', est_utilisee=True)
        r = self.client.post('/api/verifier-cle/', {'code': 'PXL-APITEST'}, content_type='application/json')
        self.assertEqual(r.status_code, 200)
        data = json.loads(r.content)
        self.assertTrue(data.get('valide'))

    def test_admin_bancaire_200(self):
        User.objects.create_user(username='bankadmin', password='bankpass')
        self.client.login(username='bankadmin', password='bankpass')
        r = self.client.get('/admin-bancaire/')
        self.assertEqual(r.status_code, 200)

class RecrutementTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='recadmin', password='recpass')

    def _login(self):
        self.client.login(username='recadmin', password='recpass')

    def test_recrutement_page_200(self):
        r = self.client.get('/recrutement/')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Rejoignez-nous')

    def test_recrutement_worker_submission(self):
        r = self.client.post('/recrutement/', {'type': 'worker', 'nom': 'Ahmed Test', 'email': 'ahmed@test.com', 'poste': 'Dev Full-Stack', 'message': 'Je suis motivé'})
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Ahmed Test')
        self.assertEqual(Candidature.objects.count(), 1)
        c = Candidature.objects.first()
        self.assertEqual(c.type_candidature, 'worker')
        self.assertEqual(c.nom, 'Ahmed Test')
        self.assertEqual(c.poste, 'Dev Full-Stack')

    def test_recrutement_partner_submission(self):
        r = self.client.post('/recrutement/', {'type': 'partner', 'nom': 'Sami Partner', 'email': 'sami@p.com', 'poste': 'Distribution Tunisie'})
        self.assertEqual(Candidature.objects.count(), 1)
        c = Candidature.objects.first()
        self.assertEqual(c.type_candidature, 'partner')

    def test_recrutement_validation_required(self):
        r = self.client.post('/recrutement/', {'type': 'worker', 'nom': '', 'email': ''})
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'obligatoires')
        self.assertEqual(Candidature.objects.count(), 0)

    def test_gestion_recrutement_page_200(self):
        self._login()
        Candidature.objects.create(type_candidature='worker', nom='Ali', email='ali@t.com', poste='Dev')
        r = self.client.get('/recrutement/gestion/')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Ali')
        self.assertContains(r, 'Dev')

    def test_gestion_recrutement_statut_update(self):
        self._login()
        c = Candidature.objects.create(type_candidature='worker', nom='Test', email='t@t.com')
        r = self.client.post('/recrutement/gestion/', {'id': c.id, 'action': 'statut', 'statut': 'entretien'})
        self.assertEqual(r.status_code, 302)
        c.refresh_from_db()
        self.assertEqual(c.statut, 'entretien')

    def test_gestion_recrutement_delete(self):
        self._login()
        c = Candidature.objects.create(type_candidature='worker', nom='Del', email='del@t.com')
        self.assertEqual(Candidature.objects.count(), 1)
        r = self.client.post('/recrutement/gestion/', {'id': c.id, 'action': 'delete'})
        self.assertEqual(r.status_code, 302)
        self.assertEqual(Candidature.objects.count(), 0)

class ECommerceTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='ecomadmin', password='ecompass')
        self.cat = Categorie.objects.create(nom='Électronique')
        self.prod = Produit.objects.create(nom='Casque Audio', categorie=self.cat, prix_vente=150, stock_actuel=10, stock_minimum=3)

    def _login(self):
        self.client.login(username='ecomadmin', password='ecompass')

    def test_ecommerce_index_200(self):
        r = self.client.get('/ecommerce/')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'PixelShop')
        self.assertContains(r, 'Casque Audio')

    def test_ecommerce_categorie_filter(self):
        r = self.client.get(f'/ecommerce/categorie/{self.cat.id}/')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Casque Audio')

    def test_ecommerce_ajouter_panier(self):
        r = self.client.get(f'/ecommerce/ajouter/{self.prod.id}/')
        self.assertEqual(r.status_code, 302)
        self.assertEqual(self.client.session['panier'][str(self.prod.id)], 1)

    def test_ecommerce_ajouter_multiple(self):
        self.client.get(f'/ecommerce/ajouter/{self.prod.id}/')
        self.client.get(f'/ecommerce/ajouter/{self.prod.id}/')
        self.assertEqual(self.client.session['panier'][str(self.prod.id)], 2)

    def test_ecommerce_panier_page_200(self):
        self.client.get(f'/ecommerce/ajouter/{self.prod.id}/')
        r = self.client.get('/ecommerce/panier/')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Casque Audio')

    def test_ecommerce_retirer_panier(self):
        self.client.get(f'/ecommerce/ajouter/{self.prod.id}/')
        r = self.client.get(f'/ecommerce/retirer/{self.prod.id}/')
        self.assertEqual(r.status_code, 302)
        self.assertNotIn(str(self.prod.id), self.client.session['panier'])

    def test_ecommerce_checkout_page_200(self):
        self.client.get(f'/ecommerce/ajouter/{self.prod.id}/')
        r = self.client.get('/ecommerce/checkout/')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Finaliser ma commande')

    def test_ecommerce_checkout_submission(self):
        self.client.get(f'/ecommerce/ajouter/{self.prod.id}/')
        r = self.client.post('/ecommerce/checkout/', {
            'nom': 'Mohamed', 'email': 'm@test.com', 'telephone': '22123456',
            'adresse': 'Rue Habib Bourguiba', 'ville': 'Tunis',
            'methode_paiement': 'especes',
        })
        self.assertEqual(r.status_code, 302)
        self.assertEqual(CommandeECommerce.objects.count(), 1)
        cmd = CommandeECommerce.objects.first()
        self.assertEqual(cmd.client_nom, 'Mohamed')
        self.assertEqual(cmd.total_ttc, 150)
        self.assertEqual(cmd.items.count(), 1)

    def test_ecommerce_checkout_validation(self):
        self.client.get(f'/ecommerce/ajouter/{self.prod.id}/')
        r = self.client.post('/ecommerce/checkout/', {'nom': '', 'email': '', 'adresse': ''})
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'obligatoires')
        self.assertEqual(CommandeECommerce.objects.count(), 0)

    def test_ecommerce_succes_page(self):
        self.client.get(f'/ecommerce/ajouter/{self.prod.id}/')
        self.client.post('/ecommerce/checkout/', {
            'nom': 'Ali', 'email': 'ali@t.com', 'adresse': 'Tunis',
            'methode_paiement': 'especes',
        })
        r = self.client.get('/ecommerce/succes/')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'confirmée')

    def test_gestion_stock_page_200(self):
        self._login()
        r = self.client.get('/ecommerce/stock/')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Gestion de stock')

    def test_gestion_stock_mouvement_entree(self):
        self._login()
        r = self.client.post('/ecommerce/stock/', {
            'action': 'add_mouvement', 'produit_id': self.prod.id,
            'type': 'entree', 'quantite': 5,
        })
        self.assertEqual(r.status_code, 302)
        self.prod.refresh_from_db()
        self.assertEqual(self.prod.stock_actuel, 15)
        self.assertEqual(MouvementStock.objects.count(), 1)
        mvt = MouvementStock.objects.first()
        self.assertEqual(mvt.stock_avant, 10)
        self.assertEqual(mvt.stock_apres, 15)

    def test_gestion_stock_mouvement_sortie(self):
        self._login()
        r = self.client.post('/ecommerce/stock/', {
            'action': 'add_mouvement', 'produit_id': self.prod.id,
            'type': 'sortie', 'quantite': 3,
        })
        self.prod.refresh_from_db()
        self.assertEqual(self.prod.stock_actuel, 7)

    def test_commande_stock_dec_reduction(self):
        self.client.get(f'/ecommerce/ajouter/{self.prod.id}/')
        self.client.post('/ecommerce/checkout/', {
            'nom': 'Stock', 'email': 's@t.com', 'adresse': 'Tunis',
            'methode_paiement': 'especes',
        })
        self.prod.refresh_from_db()
        self.assertEqual(self.prod.stock_actuel, 9)

    def test_gestion_commandes_page_200(self):
        self._login()
        self.client.get(f'/ecommerce/ajouter/{self.prod.id}/')
        self.client.post('/ecommerce/checkout/', {
            'nom': 'Cmd', 'email': 'c@t.com', 'adresse': 'Tunis',
            'methode_paiement': 'enligne',
        })
        r = self.client.get('/ecommerce/commandes/')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Gestion des commandes')
        self.assertContains(r, 'Cmd')

    def test_gestion_commandes_statut_update(self):
        self._login()
        self.client.get(f'/ecommerce/ajouter/{self.prod.id}/')
        self.client.post('/ecommerce/checkout/', {
            'nom': 'Stat', 'email': 's@t.com', 'adresse': 'Tunis',
            'methode_paiement': 'enligne',
        })
        cmd = CommandeECommerce.objects.first()
        r = self.client.post('/ecommerce/commandes/', {'commande_id': cmd.id, 'action': 'statut', 'statut': 'confirmee'})
        self.assertEqual(r.status_code, 302)
        cmd.refresh_from_db()
        self.assertEqual(cmd.statut, 'confirmee')

    def test_gestion_commandes_delete(self):
        self._login()
        self.client.get(f'/ecommerce/ajouter/{self.prod.id}/')
        self.client.post('/ecommerce/checkout/', {
            'nom': 'Del', 'email': 'd@t.com', 'adresse': 'Tunis',
            'methode_paiement': 'enligne',
        })
        self.assertEqual(CommandeECommerce.objects.count(), 1)
        cmd = CommandeECommerce.objects.first()
        r = self.client.post('/ecommerce/commandes/', {'commande_id': cmd.id, 'action': 'delete'})
        self.assertEqual(r.status_code, 302)
        self.assertEqual(CommandeECommerce.objects.count(), 0)

    def test_gestion_commandes_filtre_statut(self):
        self._login()
        self.client.get(f'/ecommerce/ajouter/{self.prod.id}/')
        self.client.post('/ecommerce/checkout/', {
            'nom': 'Filtre', 'email': 'f@t.com', 'adresse': 'Tunis',
            'methode_paiement': 'enligne',
        })
        r = self.client.get('/ecommerce/commandes/?statut=en_attente')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Filtre')

class PortailTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='pass123')
        from .models import UserProfile
        UserProfile.objects.create(user=self.user, entreprise='Test Corp', telephone='22123456')

    def test_portail_redirect_if_not_logged_in(self):
        r = self.client.get('/portail/')
        self.assertEqual(r.status_code, 302)

    def test_portail_200_when_logged_in(self):
        self.client.login(username='testuser', password='pass123')
        r = self.client.get('/portail/')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Mon espace')
        self.assertContains(r, 'test@example.com')

    def test_portail_shows_commandes(self):
        self.client.login(username='testuser', password='pass123')
        cat = Categorie.objects.create(nom='Test')
        prod = Produit.objects.create(nom='Prod', prix_vente=50, stock_actuel=5, categorie=cat)
        cmd = CommandeECommerce.objects.create(
            client_nom='Test User', client_email='test@example.com',
            client_adresse='Rue X', reference='EC-TEST', total_ttc=50,
            statut='confirmee'
        )
        CommandeECommerceItem.objects.create(commande=cmd, produit=prod, nom_produit='Prod', quantite=1, prix_unitaire=50)
        r = self.client.get('/portail/')
        self.assertContains(r, 'EC-TEST')

    def test_portail_shows_abonnements(self):
        self.client.login(username='testuser', password='pass123')
        plan = PlanAbonnement.objects.create(nom='Test Plan', slug='test-plan', prix=100, duree_jours=30)
        SouscriptionClient.objects.create(client_nom='Test', client_email='test@example.com', plan=plan, status='actif')
        r = self.client.get('/portail/')
        self.assertContains(r, 'Test Plan')

    def test_portail_shows_candidatures(self):
        self.client.login(username='testuser', password='pass123')
        Candidature.objects.create(type_candidature='worker', nom='Test', email='test@example.com', poste='Dev')
        r = self.client.get('/portail/')
        self.assertContains(r, 'Dev')

    def test_portail_edit_profile(self):
        self.client.login(username='testuser', password='pass123')
        r = self.client.post('/portail/', {'action': 'edit_profile', 'prenom': 'Jean', 'nom': 'Dupont', 'entreprise': 'New Corp', 'telephone': '99887766'})
        self.assertEqual(r.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Jean')
        self.assertEqual(self.user.last_name, 'Dupont')
        self.assertEqual(self.user.profile.entreprise, 'New Corp')
        self.assertEqual(self.user.profile.telephone, '99887766')

class DashboardTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='dashadmin', password='dashpass')
        self.client.force_login(self.user)
        cat = Categorie.objects.create(nom='Test')
        self.prod = Produit.objects.create(nom='Prod Test', prix_vente=100, stock_actuel=5, categorie=cat)
        CommandeECommerce.objects.create(client_nom='Client', client_email='c@t.com', client_adresse='Rue X', reference='DASH-TEST', total_ttc=200, statut='confirmee')
        Candidature.objects.create(type_candidature='worker', nom='Cand', email='cand@t.com', poste='Dev', statut='nouveau')

    def test_dashboard_page_200(self):
        r = self.client.get('/dashboard/')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Tableau de bord')
        self.assertContains(r, 'DASH-TEST')
        self.assertContains(r, '200 TND')

class FactureTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='factadmin', password='factpass')
        self.client.force_login(self.user)
        self.cat = Categorie.objects.create(nom='Test')
        self.prod = Produit.objects.create(nom='Article Facture', categorie=self.cat, prix_vente=75, stock_actuel=10)
        self.cmd = CommandeECommerce.objects.create(
            client_nom='Client Facture', client_email='cf@test.com',
            client_adresse='Rue de la Facture', reference='FAC-TEST',
            total_ttc=150, statut='confirmee', methode_paiement='online',
        )
        CommandeECommerceItem.objects.create(commande=self.cmd, produit=self.prod, nom_produit='Article Facture', quantite=2, prix_unitaire=75)

    def test_facture_page_200(self):
        r = self.client.get(f'/ecommerce/facture/{self.cmd.id}/')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'FAC-TEST')
        self.assertContains(r, 'Client Facture')
        self.assertContains(r, '150,00')

    def test_facture_shows_items(self):
        r = self.client.get(f'/ecommerce/facture/{self.cmd.id}/')
        self.assertContains(r, 'Article Facture')
        self.assertContains(r, '2')

class VitrinePagesTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_a_propos_page_200(self):
        r = self.client.get('/a-propos/')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Pixel Software Design')
        self.assertContains(r, 'Notre histoire')

    def test_contact_page_200(self):
        r = self.client.get('/contact/')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Contactez-nous')

    def test_contact_submission(self):
        from .models import ProjetContact
        r = self.client.post('/contact/', {
            'nom': 'Test User', 'email': 'test@test.com',
            'message': 'Test message'
        })
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Merci')
        self.assertEqual(ProjetContact.objects.count(), 1)

    def test_contact_submission_validation(self):
        r = self.client.post('/contact/', {
            'nom': '', 'email': '', 'message': ''
        })
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'obligatoires')

    def test_faq_page_200(self):
        r = self.client.get('/faq/')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Foire aux questions')

    def test_temoignages_page_200(self):
        r = self.client.get('/temoignages/')
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'disent de nous')

    def test_temoignages_with_data(self):
        from .models import Temoignage
        Temoignage.objects.create(nom='Jean Dupont', entreprise='Test Corp', contenu='Super service !', note=5)
        r = self.client.get('/temoignages/')
        self.assertContains(r, 'Jean Dupont')
        self.assertContains(r, 'Test Corp')
        self.assertContains(r, 'Super service')

class APIRestTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.cat = Categorie.objects.create(nom='Informatique', description='Matériel info')
        self.prod = Produit.objects.create(nom='Clavier Méca', prix_vente=150, stock_actuel=10, categorie=self.cat)
        self.prod2 = Produit.objects.create(nom='Souris', prix_vente=50, stock_actuel=20, categorie=self.cat)
        self.cmd = CommandeECommerce.objects.create(
            client_nom='API Client', client_email='api@test.com',
            client_adresse='Rue API', reference='API-TEST', total_ttc=200,
            statut='confirmee', methode_paiement='online',
        )
        CommandeECommerceItem.objects.create(commande=self.cmd, produit=self.prod, nom_produit='Clavier Méca', quantite=1, prix_unitaire=150)

    # ── Produits ──
    def test_api_produits_list(self):
        r = self.client.get('/api/produits/')
        self.assertEqual(r.status_code, 200)
        data = json.loads(r.content)
        self.assertEqual(len(data['produits']), 2)

    def test_api_produits_filter_categorie(self):
        r = self.client.get(f'/api/produits/?categorie={self.cat.id}')
        self.assertEqual(r.status_code, 200)
        data = json.loads(r.content)
        self.assertEqual(len(data['produits']), 2)

    def test_api_produits_detail(self):
        r = self.client.get(f'/api/produits/{self.prod.id}/')
        self.assertEqual(r.status_code, 200)
        data = json.loads(r.content)
        self.assertEqual(data['nom'], 'Clavier Méca')

    # ── Catégories ──
    def test_api_categories(self):
        r = self.client.get('/api/categories/')
        self.assertEqual(r.status_code, 200)
        data = json.loads(r.content)
        self.assertEqual(len(data['categories']), 1)
        self.assertEqual(data['categories'][0]['nom'], 'Informatique')

    # ── Stock ──
    def test_api_stock_mouvements_list(self):
        MouvementStock.objects.create(produit=self.prod, type='entree', quantite=5, stock_avant=10, stock_apres=15)
        r = self.client.get('/api/stock/mouvements/')
        self.assertEqual(r.status_code, 200)
        data = json.loads(r.content)
        self.assertEqual(len(data['mouvements']), 1)

    def test_api_stock_mouvements_create(self):
        r = self.client.post('/api/stock/mouvements/', json.dumps({
            'produit_id': self.prod.id, 'type': 'entree', 'quantite': 5,
            'reference': 'BON-001', 'notes': 'Achat fournisseur', 'cree_par': 'Admin',
        }), content_type='application/json')
        self.assertEqual(r.status_code, 201)
        data = json.loads(r.content)
        self.assertEqual(data['status'], 'ok')
        self.prod.refresh_from_db()
        self.assertEqual(self.prod.stock_actuel, 15)

    # ── Commandes ──
    def test_api_commandes_list(self):
        r = self.client.get('/api/commandes/')
        self.assertEqual(r.status_code, 200)
        data = json.loads(r.content)
        self.assertEqual(len(data['commandes']), 1)
        self.assertEqual(data['commandes'][0]['reference'], 'API-TEST')

    def test_api_commandes_filter_statut(self):
        r = self.client.get('/api/commandes/?statut=confirmee')
        self.assertEqual(r.status_code, 200)
        data = json.loads(r.content)
        self.assertEqual(len(data['commandes']), 1)

    def test_api_commandes_filter_email(self):
        r = self.client.get('/api/commandes/?email=api@test.com')
        self.assertEqual(r.status_code, 200)
        data = json.loads(r.content)
        self.assertEqual(len(data['commandes']), 1)

    def test_api_commandes_detail(self):
        r = self.client.get(f'/api/commandes/{self.cmd.id}/')
        self.assertEqual(r.status_code, 200)
        data = json.loads(r.content)
        self.assertEqual(data['reference'], 'API-TEST')
        self.assertEqual(len(data['items']), 1)

    def test_api_commande_statut_patch(self):
        r = self.client.patch(f'/api/commandes/{self.cmd.id}/statut/', json.dumps({'statut': 'expediee'}), content_type='application/json')
        self.assertEqual(r.status_code, 200)
        data = json.loads(r.content)
        self.assertEqual(data['statut'], 'expediee')
        self.cmd.refresh_from_db()
        self.assertEqual(self.cmd.statut, 'expediee')

    def test_api_commande_statut_invalide(self):
        r = self.client.patch(f'/api/commandes/{self.cmd.id}/statut/', json.dumps({'statut': 'bogus'}), content_type='application/json')
        self.assertEqual(r.status_code, 400)

    # ── Panier ──
    def test_api_panier_empty(self):
        r = self.client.get('/api/panier/')
        self.assertEqual(r.status_code, 200)
        data = json.loads(r.content)
        self.assertEqual(data['items'], [])
        self.assertEqual(data['total_ttc'], '0')

    def test_api_panier_ajouter(self):
        r = self.client.post(f'/api/panier/ajouter/{self.prod.id}/')
        self.assertEqual(r.status_code, 200)
        r2 = self.client.get('/api/panier/')
        data = json.loads(r2.content)
        self.assertEqual(len(data['items']), 1)
        self.assertEqual(data['items'][0]['nom'], 'Clavier Méca')

    def test_api_panier_retirer(self):
        self.client.post(f'/api/panier/ajouter/{self.prod.id}/')
        r = self.client.post(f'/api/panier/retirer/{self.prod.id}/')
        self.assertEqual(r.status_code, 200)
        r2 = self.client.get('/api/panier/')
        data = json.loads(r2.content)
        self.assertEqual(len(data['items']), 0)

    def test_api_panier_vider(self):
        self.client.post(f'/api/panier/ajouter/{self.prod.id}/')
        r = self.client.delete('/api/panier/')
        self.assertEqual(r.status_code, 200)
        r2 = self.client.get('/api/panier/')
        data = json.loads(r2.content)
        self.assertEqual(len(data['items']), 0)

class EmailNotificationsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='emailadmin', password='emailpass')
        self.cat = Categorie.objects.create(nom='Test')
        self.prod = Produit.objects.create(nom='Article Email', categorie=self.cat, prix_vente=100, stock_actuel=5)
        self.plan = PlanAbonnement.objects.create(nom='Plan Email', slug='plan-email', prix=50, duree_jours=30)

    def test_email_activation_cle_cash(self):
        from django.core import mail
        sub = SouscriptionClient.objects.create(client_nom='Cash User', client_email='cash@test.com', plan=self.plan)
        Paiement.objects.create(souscription=sub, methode='especes', montant=50, reference='CASH-EMAIL')
        CleActivation.objects.create(souscription=sub, code='PXL-EMAILTEST')
        r = self.client.post(f'/abonnement/{sub.id}/cash/', {'code': 'PXL-EMAILTEST'}, follow=True)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('clé d\'activation', mail.outbox[0].body)
        self.assertIn('PXL-EMAILTEST', mail.outbox[0].body)
        self.assertEqual(mail.outbox[0].to, ['cash@test.com'])

    def test_email_activation_cle_online(self):
        from django.core import mail
        sub = SouscriptionClient.objects.create(client_nom='Online User', client_email='online@test.com', plan=self.plan)
        Paiement.objects.create(souscription=sub, methode='online', montant=50, reference='ONL-EMAIL')
        r = self.client.post(f'/abonnement/{sub.id}/online/', {'transaction_id': 'TXN-123'}, follow=True)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('activation', mail.outbox[0].body)
        self.assertEqual(mail.outbox[0].to, ['online@test.com'])

    def test_email_confirmation_commande(self):
        self.client.login(username='emailadmin', password='emailpass')
        from django.core import mail
        self.client.get(f'/ecommerce/ajouter/{self.prod.id}/')
        r = self.client.post('/ecommerce/checkout/', {
            'nom': 'Email Client', 'email': 'client@test.com',
            'adresse': 'Tunis', 'methode_paiement': 'especes',
        }, follow=True)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('commande', mail.outbox[0].subject.lower())
        self.assertIn('Email Client', mail.outbox[0].body)
        self.assertEqual(mail.outbox[0].to, ['client@test.com'])

    def test_email_statut_commande(self):
        self.client.login(username='emailadmin', password='emailpass')
        from django.core import mail
        self.client.get(f'/ecommerce/ajouter/{self.prod.id}/')
        self.client.post('/ecommerce/checkout/', {
            'nom': 'Stat Client', 'email': 'stat@test.com',
            'adresse': 'Sfax', 'methode_paiement': 'especes',
        })
        cmd = CommandeECommerce.objects.first()
        mail.outbox.clear()
        r = self.client.post('/ecommerce/commandes/', {'commande_id': cmd.id, 'action': 'statut', 'statut': 'expediee'}, follow=True)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('expédiée', mail.outbox[0].body)
        self.assertEqual(mail.outbox[0].to, ['stat@test.com'])
