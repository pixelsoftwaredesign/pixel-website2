import 'package:flutter/material.dart';
import '../services/api_service.dart';
import 'login_screen.dart';
import 'services_screen.dart';
import 'erp_screen.dart';
import 'contact_screen.dart';
import 'pixmail_login_screen.dart';
import 'social_feed_screen.dart';
import 'social_messages_screen.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});
  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  final ApiService api = ApiService();
  int _currentIndex = 0;

  final List<Widget> _pages = [
    const _HomePage(),
    const ServicesScreen(),
    const ErpScreen(),
    const _PixMailTab(),
    const SocialFeedScreen(),
    const SocialMessagesScreen(),
    const ContactScreen(),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _pages[_currentIndex],
      bottomNavigationBar: NavigationBar(
        selectedIndex: _currentIndex,
        onDestinationSelected: (i) => setState(() => _currentIndex = i),
        backgroundColor: const Color(0xFF111827),
        indicatorColor: const Color(0xFF1EB482).withValues(alpha: 0.2),
        destinations: const [
          NavigationDestination(icon: Icon(Icons.home_outlined), selectedIcon: Icon(Icons.home, color: Color(0xFF1EB482)), label: 'Accueil'),
          NavigationDestination(icon: Icon(Icons.code_outlined), selectedIcon: Icon(Icons.code, color: Color(0xFF1EB482)), label: 'Services'),
          NavigationDestination(icon: Icon(Icons.dashboard_outlined), selectedIcon: Icon(Icons.dashboard, color: Color(0xFF1EB482)), label: 'ERP'),
          NavigationDestination(icon: Icon(Icons.mark_email_unread_outlined), selectedIcon: Icon(Icons.mark_email_unread, color: Color(0xFF1EB482)), label: 'PixMail'),
          NavigationDestination(icon: Icon(Icons.people_outlined), selectedIcon: Icon(Icons.people, color: Color(0xFF1EB482)), label: 'Social'),
          NavigationDestination(icon: Icon(Icons.chat_outlined), selectedIcon: Icon(Icons.chat, color: Color(0xFF1EB482)), label: 'Chat E2E'),
          NavigationDestination(icon: Icon(Icons.mail_outlined), selectedIcon: Icon(Icons.mail, color: Color(0xFF1EB482)), label: 'Contact'),
        ],
      ),
    );
  }
}

class _HomePage extends StatelessWidget {
  const _HomePage();

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Row(
                  children: [
                    Container(
                      width: 36, height: 36,
                      decoration: BoxDecoration(
                        color: const Color(0xFF1EB482),
                        borderRadius: BorderRadius.circular(8),
                      ),
                      child: const Icon(Icons.hexagon, color: Colors.white, size: 20),
                    ),
                    const SizedBox(width: 10),
                    const Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text('Pixel Software Design', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
                        Text("L'architecture de l'innovation", style: TextStyle(fontSize: 10, color: Colors.grey)),
                      ],
                    ),
                  ],
                ),
                IconButton(
                  icon: const Icon(Icons.person_outline, color: Colors.white70),
                  onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (_) => const LoginScreen())),
                ),
              ],
            ),
            const SizedBox(height: 40),
            const Text('Studio Multidisciplinaire · Tunis', style: TextStyle(color: Color(0xFF1EB482), fontSize: 12, letterSpacing: 2)),
            const SizedBox(height: 12),
            RichText(
              text: TextSpan(
                style: const TextStyle(fontSize: 32, fontWeight: FontWeight.bold, height: 1.2),
                children: [
                  const TextSpan(text: "L'architecture\nde "),
                  TextSpan(text: "l'innovation", style: const TextStyle(color: Color(0xFF1EB482))),
                ],
              ),
            ),
            const SizedBox(height: 16),
            const Text(
              "Pixel Software Design fusionne le design d'intérieur, le développement logiciel, l'intelligence artificielle et le multimédia.",
              style: TextStyle(color: Colors.grey, fontSize: 14, height: 1.6),
            ),
            const SizedBox(height: 24),
            Row(
              children: [
                _statBox('4', 'Disciplines'),
                const SizedBox(width: 12),
                _statBox('48+', 'Projets livrés'),
                const SizedBox(width: 12),
                _statBox('100%', 'Satisfait'),
              ],
            ),
            const SizedBox(height: 40),
            const Text('// Nos Services', style: TextStyle(color: Color(0xFF1EB482), fontSize: 12, letterSpacing: 2)),
            const SizedBox(height: 8),
            const Text('Quatre disciplines, une vision unifiée', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
            const SizedBox(height: 20),
            _serviceCard(Icons.smart_toy, 'IA & Digital', 'Intelligence artificielle & solutions digitales'),
            _serviceCard(Icons.code, 'Logiciel & IT', 'Développement logiciel & conseil IT'),
            _serviceCard(Icons.home, 'Smart Spaces', "Design d'intérieur & espaces intelligents"),
            _serviceCard(Icons.videocam, 'Multimédia', 'Rendus 3D & expériences immersives'),
            const SizedBox(height: 40),
            const Text('// Projets récents', style: TextStyle(color: Color(0xFF1EB482), fontSize: 12, letterSpacing: 2)),
            const SizedBox(height: 8),
            const Text('Projets récents', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
            const SizedBox(height: 16),
            _projectCard('Villa Jasmine', 'Smart Home · IA · Design', 'Domotique complète + IA + design intérieur'),
            _projectCard('Noor Analytics', 'Logiciel · IoT · SaaS', 'Plateforme intelligente'),
            _projectCard('Delv', 'Interne · Outil', 'Outil interne de développement'),
            _projectCard('PixMaps', 'Web App · Cartographie', 'Application web cartographique'),
            const SizedBox(height: 24),
          ],
        ),
      ),
    );
  }

  static Widget _statBox(String value, String label) {
    return Expanded(
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: 16),
        decoration: BoxDecoration(
          color: const Color(0xFF111827),
          borderRadius: BorderRadius.circular(12),
          border: Border.all(color: const Color(0xFF1E293B)),
        ),
        child: Column(children: [
          Text(value, style: const TextStyle(fontSize: 22, fontWeight: FontWeight.bold, color: Color(0xFF1EB482))),
          const SizedBox(height: 4),
          Text(label, style: const TextStyle(fontSize: 11, color: Colors.grey)),
        ]),
      ),
    );
  }

  static Widget _serviceCard(IconData icon, String title, String desc) {
    return Container(
      margin: const EdgeInsets.only(bottom: 12),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: const Color(0xFF111827),
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: const Color(0xFF1E293B)),
      ),
      child: Row(
        children: [
          Container(
            width: 44, height: 44,
            decoration: BoxDecoration(color: const Color(0xFF1EB482).withValues(alpha: 0.15), borderRadius: BorderRadius.circular(10)),
            child: Icon(icon, color: const Color(0xFF1EB482), size: 22),
          ),
          const SizedBox(width: 14),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(title, style: const TextStyle(fontWeight: FontWeight.w600, fontSize: 14)),
                const SizedBox(height: 2),
                Text(desc, style: const TextStyle(color: Colors.grey, fontSize: 12)),
              ],
            ),
          ),
          const Icon(Icons.chevron_right, color: Colors.grey),
        ],
      ),
    );
  }

  static Widget _projectCard(String title, String tag, String desc) {
    return Container(
      margin: const EdgeInsets.only(bottom: 12),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: const Color(0xFF111827),
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: const Color(0xFF1E293B)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
            decoration: BoxDecoration(color: const Color(0xFF1EB482).withValues(alpha:0.1), borderRadius: BorderRadius.circular(6)),
            child: Text(tag, style: const TextStyle(color: Color(0xFF1EB482), fontSize: 10)),
          ),
          const SizedBox(height: 10),
          Text(title, style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
          const SizedBox(height: 4),
          Text(desc, style: const TextStyle(color: Colors.grey, fontSize: 12)),
        ],
      ),
    );
  }
}

class _PixMailTab extends StatelessWidget {
  const _PixMailTab();

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const SizedBox(height: 20),
            Container(
              width: 56, height: 56,
              decoration: BoxDecoration(
                gradient: const LinearGradient(colors: [Color(0xFF1EB482), Color(0xFF1A9BAF)]),
                borderRadius: BorderRadius.circular(14),
              ),
              child: const Icon(Icons.email_outlined, color: Colors.white, size: 28),
            ),
            const SizedBox(height: 20),
            const Text('PixMail', style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold)),
            const SizedBox(height: 4),
            const Text('@pxelsoftware-64fcd.web.app', style: TextStyle(color: Color(0xFF1EB482), fontSize: 13, fontFamily: 'monospace')),
            const SizedBox(height: 16),
            const Text(
              'Votre email professionnel sécurisé. Envoyez et recevez des messages depuis votre application Pixel.',
              style: TextStyle(color: Colors.grey, fontSize: 14, height: 1.6),
            ),
            const SizedBox(height: 32),
            _feature(Icons.lock_outline, 'Sécurisé', 'Chiffrement de bout en bout'),
            _feature(Icons.speed, 'Rapide', 'Synchronisation instantanée'),
            _feature(Icons.folder_outlined, 'Organisé', 'Dossiers intelligents'),
            _feature(Icons.people_outline, 'Contacts', 'Gestionnaire intégré'),
            const SizedBox(height: 32),
            SizedBox(
              width: double.infinity,
              child: ElevatedButton(
                onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (_) => const PixMailLoginScreen())),
                style: ElevatedButton.styleFrom(
                  backgroundColor: const Color(0xFF1EB482),
                  foregroundColor: Colors.black,
                  padding: const EdgeInsets.symmetric(vertical: 16),
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                ),
                child: const Text('Ouvrir PixMail →', style: TextStyle(fontWeight: FontWeight.w700, fontSize: 15)),
              ),
            ),
            const SizedBox(height: 12),
            SizedBox(
              width: double.infinity,
              child: OutlinedButton(
                onPressed: () => Navigator.push(context, MaterialPageRoute(builder: (_) => const PixMailLoginScreen())),
                style: OutlinedButton.styleFrom(
                  foregroundColor: const Color(0xFF1EB482),
                  side: const BorderSide(color: Color(0xFF1E293B)),
                  padding: const EdgeInsets.symmetric(vertical: 14),
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                ),
                child: const Text('Créer un compte email', style: TextStyle(fontSize: 13)),
              ),
            ),
          ],
        ),
      ),
    );
  }

  static Widget _feature(IconData icon, String title, String desc) {
    return Container(
      margin: const EdgeInsets.only(bottom: 10),
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: const Color(0xFF111827),
        borderRadius: BorderRadius.circular(10),
        border: Border.all(color: const Color(0xFF1E293B)),
      ),
      child: Row(
        children: [
          Icon(icon, color: const Color(0xFF1EB482), size: 20),
          const SizedBox(width: 14),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(title, style: const TextStyle(fontWeight: FontWeight.w600, fontSize: 13)),
                Text(desc, style: const TextStyle(color: Colors.grey, fontSize: 11)),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
