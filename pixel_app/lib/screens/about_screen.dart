import 'package:flutter/material.dart';

class AboutScreen extends StatelessWidget {
  const AboutScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('À propos')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Container(
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
                gradient: const LinearGradient(colors: [Color(0xFF1EB482), Color(0xFF1565C0)]),
                borderRadius: BorderRadius.circular(16),
              ),
              child: const Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text("Notre vision", style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.white)),
                  SizedBox(height: 8),
                  Text(
                    "Nous créons des écosystèmes intelligents où le monde physique et le monde numérique coexistent en parfaite harmonie.",
                    style: TextStyle(color: Colors.white, fontSize: 13, height: 1.5),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 24),
            const Text('Piliers', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
            const SizedBox(height: 12),
            _pillar('🤖', 'Intelligence Artificielle', 'Algorithmes sur mesure intégrés dans vos espaces.'),
            _pillar('💻', 'Logiciel & IoT', 'Applications, web, objets connectés en temps réel.'),
            _pillar('🏛️', 'Design d\'Intérieur', 'Architecture intérieure contemporaine.'),
            _pillar('🎬', 'Multimédia & VR/AR', 'Rendus 3D et visites virtuelles.'),
            const SizedBox(height: 24),
          ],
        ),
      ),
    );
  }

  static Widget _pillar(String icon, String title, String desc) {
    return Container(
      margin: const EdgeInsets.only(bottom: 10),
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: const Color(0xFF111827),
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: const Color(0xFF1E293B)),
      ),
      child: Row(children: [
        Text(icon, style: const TextStyle(fontSize: 24)),
        const SizedBox(width: 14),
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(title, style: const TextStyle(fontWeight: FontWeight.w600)),
              const SizedBox(height: 2),
              Text(desc, style: const TextStyle(color: Colors.grey, fontSize: 12)),
            ],
          ),
        ),
      ]),
    );
  }
}
