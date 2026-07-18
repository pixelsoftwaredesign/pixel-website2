import 'package:flutter/material.dart';

class ServicesScreen extends StatelessWidget {
  const ServicesScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text('// Nos Services', style: TextStyle(color: Color(0xFF1EB482), fontSize: 12, letterSpacing: 2)),
            const SizedBox(height: 8),
            const Text('Quatre disciplines, une vision unifiée', style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
            const SizedBox(height: 24),
            _section('01', 'IA & Digital', [
              ("Intégration d'IA Personnalisée", "Algorithmes d'IA pour optimiser la gestion des espaces et automatiser des processus métier complexes."),
              ("Stratégies de Transformation Digitale", "Digitalisation complète de votre activité : gestion cloud, écosystèmes numériques intégrés."),
            ]),
            _section('02', 'Logiciel & IT', [
              ("Logiciels sur Mesure", "Applications mobiles, plateformes web et logiciels de gestion avec interfaces UI/UX de dernière génération."),
              ("Conseil Stratégique IT & IoT", "Analyse technique, choix d'infrastructures et objets connectés."),
            ]),
            _section('03', 'Smart Spaces', [
              ("Design d'Intérieur Évolué", "Architecture intérieure alliant esthétique contemporaine et fonctionnalité technique."),
              ("Domotique Avancée", "Technologies Smart Home pour un contrôle total de l'éclairage, du climat et de la sécurité."),
            ]),
            _section('04', 'Multimédia', [
              ("Visualisation 3D & Visites Virtuelles", "Rendus photoréalistes et visites immersives en VR/AR pour explorer le projet avant sa réalisation."),
              ("Production Multimédia", "Vidéo, motion graphics et installations interactives à fort impact."),
            ]),
            const SizedBox(height: 24),
          ],
        ),
      ),
    );
  }

  static Widget _section(String num, String title, List<(String, String)> items) {
    return Container(
      margin: const EdgeInsets.only(bottom: 20),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: const Color(0xFF111827),
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: const Color(0xFF1E293B)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(children: [
            Container(
              width: 32, height: 32,
              decoration: BoxDecoration(color: const Color(0xFF1EB482).withValues(alpha:0.15), borderRadius: BorderRadius.circular(8)),
              child: Center(child: Text(num, style: const TextStyle(color: Color(0xFF1EB482), fontWeight: FontWeight.bold, fontSize: 13))),
            ),
            const SizedBox(width: 12),
            Text(title, style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
          ]),
          const SizedBox(height: 16),
          ...items.map((item) => Padding(
            padding: const EdgeInsets.only(bottom: 12),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(item.$1, style: const TextStyle(fontWeight: FontWeight.w600, fontSize: 14)),
                const SizedBox(height: 4),
                Text(item.$2, style: const TextStyle(color: Colors.grey, fontSize: 12, height: 1.5)),
              ],
            ),
          )),
        ],
      ),
    );
  }
}
