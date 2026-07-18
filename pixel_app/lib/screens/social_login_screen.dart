import 'package:flutter/material.dart';
import '../services/social_api.dart';
import 'social_register_screen.dart';

class SocialLoginScreen extends StatefulWidget {
  const SocialLoginScreen({super.key});
  @override
  State<SocialLoginScreen> createState() => _SocialLoginScreenState();
}

class _SocialLoginScreenState extends State<SocialLoginScreen> {
  final _api = SocialApiService();
  final _usernameCtrl = TextEditingController();
  final _passwordCtrl = TextEditingController();
  bool _loading = false;

  Future<void> _login() async {
    setState(() => _loading = true);
    final data = await _api.login(_usernameCtrl.text.trim(), _passwordCtrl.text);
    setState(() => _loading = false);
    if (!mounted) return;
    if (data['status'] == 'ok') {
      Navigator.pop(context, {'username': data['username'], 'api': _api});
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(data['error'] ?? 'Erreur'), backgroundColor: Colors.red),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('PixSocial — Connexion')),
      body: Center(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(24),
          child: Column(
            children: [
              Container(
                width: 64, height: 64,
                decoration: BoxDecoration(
                  gradient: const LinearGradient(colors: [Color(0xFF1EB482), Color(0xFF1A9BAF)]),
                  borderRadius: BorderRadius.circular(16),
                ),
                child: const Icon(Icons.people, color: Colors.white, size: 32),
              ),
              const SizedBox(height: 20),
              const Text('PixSocial', style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold)),
              const SizedBox(height: 4),
              const Text('Connectez-vous à votre réseau', style: TextStyle(color: Colors.grey, fontSize: 13)),
              const SizedBox(height: 32),
              _field(_usernameCtrl, 'Nom d\'utilisateur', Icons.person_outline),
              const SizedBox(height: 12),
              _field(_passwordCtrl, 'Mot de passe', Icons.lock_outline, obscure: true),
              const SizedBox(height: 24),
              SizedBox(
                width: double.infinity,
                child: ElevatedButton(
                  onPressed: _loading ? null : _login,
                  style: ElevatedButton.styleFrom(
                    backgroundColor: const Color(0xFF1EB482),
                    foregroundColor: Colors.black,
                    padding: const EdgeInsets.symmetric(vertical: 16),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                  ),
                  child: _loading
                      ? const SizedBox(width: 20, height: 20, child: CircularProgressIndicator(strokeWidth: 2))
                      : const Text('Se connecter', style: TextStyle(fontWeight: FontWeight.w700)),
                ),
              ),
              const SizedBox(height: 16),
              TextButton(
                onPressed: () => Navigator.pushReplacement(context, MaterialPageRoute(builder: (_) => const SocialRegisterScreen())),
                child: const Text('Pas de compte ? Créer un compte', style: TextStyle(color: Color(0xFF1EB482), fontSize: 13)),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _field(TextEditingController ctrl, String hint, IconData icon, {bool obscure = false}) {
    return TextField(
      controller: ctrl,
      obscureText: obscure,
      style: const TextStyle(color: Colors.white),
      decoration: InputDecoration(
        hintText: hint, hintStyle: const TextStyle(color: Colors.grey),
        prefixIcon: Icon(icon, color: const Color(0xFF1EB482), size: 20),
        filled: true, fillColor: const Color(0xFF111827),
        border: OutlineInputBorder(borderRadius: BorderRadius.circular(12), borderSide: BorderSide.none),
        focusedBorder: OutlineInputBorder(borderRadius: BorderRadius.circular(12), borderSide: const BorderSide(color: Color(0xFF1EB482))),
      ),
    );
  }
}
