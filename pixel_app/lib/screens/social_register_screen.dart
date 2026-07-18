import 'package:flutter/material.dart';
import '../services/social_api.dart';

class SocialRegisterScreen extends StatefulWidget {
  const SocialRegisterScreen({super.key});
  @override
  State<SocialRegisterScreen> createState() => _SocialRegisterScreenState();
}

class _SocialRegisterScreenState extends State<SocialRegisterScreen> {
  final _api = SocialApiService();
  final _usernameCtrl = TextEditingController();
  final _emailCtrl = TextEditingController();
  final _passwordCtrl = TextEditingController();
  final _nameCtrl = TextEditingController();
  bool _loading = false;

  Future<void> _register() async {
    setState(() => _loading = true);
    final data = await _api.register(
      _usernameCtrl.text.trim(), _emailCtrl.text.trim(),
      _passwordCtrl.text, displayName: _nameCtrl.text.trim(),
    );
    setState(() => _loading = false);
    if (!mounted) return;
    if (data['status'] == 'ok') {
      Navigator.pop(context);
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Compte créé ! Connectez-vous.'), backgroundColor: Color(0xFF1EB482)),
      );
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(data['error'] ?? 'Erreur'), backgroundColor: Colors.red),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('PixSocial — Inscription')),
      body: Center(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(24),
          child: Column(
            children: [
              const Text('Rejoindre PixSocial', style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
              const SizedBox(height: 24),
              _field(_nameCtrl, 'Nom d\'affichage', Icons.badge_outlined),
              const SizedBox(height: 12),
              _field(_usernameCtrl, 'Nom d\'utilisateur', Icons.alternate_email),
              const SizedBox(height: 12),
              _field(_emailCtrl, 'Email', Icons.email_outlined),
              const SizedBox(height: 12),
              _field(_passwordCtrl, 'Mot de passe', Icons.lock_outline, obscure: true),
              const SizedBox(height: 24),
              SizedBox(
                width: double.infinity,
                child: ElevatedButton(
                  onPressed: _loading ? null : _register,
                  style: ElevatedButton.styleFrom(
                    backgroundColor: const Color(0xFF1EB482),
                    foregroundColor: Colors.black,
                    padding: const EdgeInsets.symmetric(vertical: 16),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                  ),
                  child: _loading
                      ? const SizedBox(width: 20, height: 20, child: CircularProgressIndicator(strokeWidth: 2))
                      : const Text('Créer mon compte', style: TextStyle(fontWeight: FontWeight.w700)),
                ),
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
