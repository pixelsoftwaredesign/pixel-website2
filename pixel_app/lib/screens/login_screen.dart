import 'package:flutter/material.dart';
import '../services/api_service.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});
  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final api = ApiService();
  final usernameCtrl = TextEditingController();
  final passwordCtrl = TextEditingController();
  final emailCtrl = TextEditingController();
  bool isLogin = true;
  bool loading = false;
  String? error;

  void _submit() async {
    setState(() { loading = true; error = null; });
    try {
      Map<String, dynamic> res;
      if (isLogin) {
        res = await api.login(usernameCtrl.text, passwordCtrl.text);
      } else {
        res = await api.register(usernameCtrl.text, emailCtrl.text, passwordCtrl.text);
      }
      if (res['status'] == 'success' && mounted) {
        Navigator.pop(context);
        ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(res['message'] ?? 'OK'), backgroundColor: const Color(0xFF1EB482)));
      } else {
        setState(() => error = res['message'] ?? 'Erreur');
      }
    } catch (e) {
      setState(() => error = 'Erreur de connexion');
    }
    setState(() => loading = false);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(isLogin ? 'Connexion' : 'Inscription')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Container(
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(color: const Color(0xFF111827), borderRadius: BorderRadius.circular(16)),
              child: Column(
                children: [
                  Container(
                    width: 56, height: 56,
                    decoration: BoxDecoration(color: const Color(0xFF1EB482).withValues(alpha:0.15), borderRadius: BorderRadius.circular(16)),
                    child: const Icon(Icons.person, color: Color(0xFF1EB482), size: 28),
                  ),
                  const SizedBox(height: 16),
                  Text(isLogin ? 'Connexion' : 'Créer un compte', style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
                  const SizedBox(height: 20),
                  _field('Identifiant', usernameCtrl, Icons.person_outline),
                  if (!isLogin) _field('Email', emailCtrl, Icons.email_outlined),
                  _field('Mot de passe', passwordCtrl, Icons.lock_outline, obscure: true),
                  if (error != null) ...[
                    const SizedBox(height: 8),
                    Text(error!, style: const TextStyle(color: Colors.redAccent, fontSize: 12)),
                  ],
                  const SizedBox(height: 16),
                  SizedBox(
                    width: double.infinity,
                    child: ElevatedButton(
                      onPressed: loading ? null : _submit,
                      style: ElevatedButton.styleFrom(
                        backgroundColor: const Color(0xFF1EB482),
                        foregroundColor: Colors.white,
                        padding: const EdgeInsets.symmetric(vertical: 14),
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                      ),
                      child: loading
                          ? const SizedBox(width: 20, height: 20, child: CircularProgressIndicator(color: Colors.white, strokeWidth: 2))
                          : Text(isLogin ? 'Se connecter' : "S'inscrire"),
                    ),
                  ),
                  const SizedBox(height: 12),
                  TextButton(
                    onPressed: () => setState(() { isLogin = !isLogin; error = null; }),
                    child: Text(
                      isLogin ? "Pas encore de compte ? S'inscrire" : 'Déjà inscrit ? Se connecter',
                      style: const TextStyle(color: Color(0xFF1EB482), fontSize: 12),
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _field(String label, TextEditingController ctrl, IconData icon, {bool obscure = false}) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 12),
      child: TextField(
        controller: ctrl,
        obscureText: obscure,
        style: const TextStyle(color: Colors.white),
        decoration: InputDecoration(
          labelText: label,
          prefixIcon: Icon(icon, color: Colors.grey, size: 20),
          filled: true,
          fillColor: const Color(0xFF0A0E17),
          border: OutlineInputBorder(borderRadius: BorderRadius.circular(10), borderSide: const BorderSide(color: Color(0xFF1E293B))),
          enabledBorder: OutlineInputBorder(borderRadius: BorderRadius.circular(10), borderSide: const BorderSide(color: Color(0xFF1E293B))),
          labelStyle: const TextStyle(color: Colors.grey),
        ),
      ),
    );
  }
}
