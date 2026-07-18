import 'package:flutter/material.dart';

class ErpScreen extends StatelessWidget {
  const ErpScreen({super.key});

  final List<Map<String, dynamic>> modules = const [
    {'icon': '🚗', 'title': 'Auto-École', 'desc': 'Gestion complète : candidats, moniteurs, véhicules, leçons, examens'},
    {'icon': '🏥', 'title': 'Santé / Clinique', 'desc': 'Patients, médecins, RDV, lits, facturations'},
    {'icon': '🏨', 'title': 'Hôtellerie', 'desc': 'Chambres, réservations, services, clients'},
    {'icon': '🛒', 'title': 'Commerce / Retail', 'desc': 'Produits, catégories, ventes, stock'},
    {'icon': '⚖️', 'title': 'Juridique', 'desc': 'Dossiers, audiences, clients juridiques'},
    {'icon': '📊', 'title': 'Comptabilité', 'desc': 'Écritures, factures, journaux, déclarations fiscales'},
    {'icon': '👥', 'title': 'RH & Paie', 'desc': 'Employés, contrats, fiches de paie, congés, formations'},
    {'icon': '🍽️', 'title': 'Restaurant', 'desc': 'Menus, tables, gestion en temps réel'},
    {'icon': '🎂', 'title': 'Pâtisserie', 'desc': 'Recettes, produits, stocks, caisse'},
    {'icon': '💻', 'title': 'PixelSoftCode', 'desc': 'Modules logiciels réutilisables'},
    {'icon': '🏗️', 'title': 'Inner Studio 3D', 'desc': 'Projets 3D : architecture, intérieur, extérieur'},
    {'icon': '🛒', 'title': 'E-Commerce', 'desc': 'Boutique en ligne, panier, commandes, paiements'},
  ];

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text('// GestiActiv ERP', style: TextStyle(color: Color(0xFF1EB482), fontSize: 12, letterSpacing: 2)),
            const SizedBox(height: 8),
            const Text('Modules disponibles', style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
            const SizedBox(height: 6),
            const Text('Système de gestion intégré pour tous les secteurs', style: TextStyle(color: Colors.grey, fontSize: 13)),
            const SizedBox(height: 24),
            ...modules.map((m) => Container(
              margin: const EdgeInsets.only(bottom: 10),
              padding: const EdgeInsets.all(14),
              decoration: BoxDecoration(
                color: const Color(0xFF111827),
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: const Color(0xFF1E293B)),
              ),
              child: Row(
                children: [
                  Container(
                    width: 44, height: 44,
                    decoration: BoxDecoration(color: const Color(0xFF1EB482).withValues(alpha:0.1), borderRadius: BorderRadius.circular(10)),
                    child: Center(child: Text(m['icon']!, style: const TextStyle(fontSize: 20))),
                  ),
                  const SizedBox(width: 14),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(m['title']!, style: const TextStyle(fontWeight: FontWeight.w600, fontSize: 14)),
                        const SizedBox(height: 2),
                        Text(m['desc']!, style: const TextStyle(color: Colors.grey, fontSize: 11)),
                      ],
                    ),
                  ),
                  const Icon(Icons.chevron_right, color: Colors.grey, size: 20),
                ],
              ),
            )),
            const SizedBox(height: 16),
          ],
        ),
      ),
    );
  }
}
