import 'package:flutter/material.dart';
import '../services/pixmail_api.dart';
import 'pixmail_inbox_screen.dart';

class PixMailRegisterScreen extends StatefulWidget {
  const PixMailRegisterScreen({super.key});
  @override
  State<PixMailRegisterScreen> createState() => _PixMailRegisterScreenState();
}

class _PixMailRegisterScreenState extends State<PixMailRegisterScreen> {
  final _usernameCtrl = TextEditingController();
  final _passwordCtrl = TextEditingController();
  final _password2Ctrl = TextEditingController();
  final _displayNameCtrl = TextEditingController();
  final _api = PixMailApi();
  bool _loading = false;
  String? _error;

  Future<void> _register() async {
    if (_passwordCtrl.text != _password2Ctrl.text) {
      setState(() { _error = 'Les mots de passe ne correspondent pas.'; });
      return;
    }
    if (_passwordCtrl.text.length < 6) {
      setState(() { _error = 'Minimum 6 caractères pour le mot de passe.'; });
      return;
    }
    setState(() { _loading = true; _error = null; });
    try {
      final result = await _api.register(_usernameCtrl.text, _passwordCtrl.text, displayName: _displayNameCtrl.text);
      if (result['status'] == 'success' || result['email'] != null) {
        if (!mounted) return;
        Navigator.pushReplacement(context, MaterialPageRoute(
          builder: (_) => PixMailInboxScreen(email: result['email'] ?? '${_usernameCtrl.text}@pxelsoftware-64fcd.web.app'),
        ));
      } else {
        setState(() { _error = result['message'] ?? 'Erreur d\'inscription'; });
      }
    } catch (e) {
      setState(() { _error = 'Serveur indisponible.'; });
    }
    setState(() { _loading = false; });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF05100D),
      appBar: AppBar(
        title: const Row(children: [
          Icon(Icons.email_outlined, color: Color(0xFF1EB482), size: 22),
          SizedBox(width: 8),
          Text('PixMail — Inscription', style: TextStyle(fontSize: 18, fontWeight: FontWeight.w600)),
        ]),
        backgroundColor: const Color(0xFF081511),
      ),
      body: Center(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(32),
          child: Container(
            padding: const EdgeInsets.all(32),
            decoration: BoxDecoration(
              color: const Color(0xFF111827), borderRadius: BorderRadius.circular(16),
              border: Border.all(color: const Color(0xFF1E293B)),
            ),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                const Icon(Icons.alternate_email, color: Color(0xFF1EB482), size: 48),
                const SizedBox(height: 16),
                const Text('Créer votre email', style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
                const SizedBox(height: 4),
                Text('@pxelsoftware-64fcd.web.app', style: TextStyle(fontSize: 13, color: Colors.grey.shade400)),
                const SizedBox(height: 24),
                if (_error != null)
                  Container(
                    padding: const EdgeInsets.all(10), margin: const EdgeInsets.only(bottom: 16),
                    decoration: BoxDecoration(color: Colors.red.shade900.withValues(alpha: 0.3), borderRadius: BorderRadius.circular(8)),
                    child: Text(_error!, style: const TextStyle(color: Colors.redAccent, fontSize: 12)),
                  ),
                _field('Nom d\'utilisateur', _usernameCtrl, Icons.person_outline),
                const SizedBox(height: 6),
                Align(alignment: Alignment.centerLeft, child: Text('→ ${_usernameCtrl.text.isNotEmpty ? _usernameCtrl.text : "votre"}@pxelsoftware-64fcd.web.app',
                    style: const TextStyle(fontSize: 11, color: Color(0xFF1EB482), fontFamily: 'monospace'))),
                const SizedBox(height: 12),
                _field('Nom d\'affichage', _displayNameCtrl, Icons.badge_outlined),
                const SizedBox(height: 12),
                _field('Mot de passe', _passwordCtrl, Icons.lock_outline, obscure: true),
                const SizedBox(height: 12),
                _field('Confirmer', _password2Ctrl, Icons.lock_outline, obscure: true),
                const SizedBox(height: 20),
                SizedBox(
                  width: double.infinity,
                  child: ElevatedButton(
                    onPressed: _loading ? null : _register,
                    style: ElevatedButton.styleFrom(
                      backgroundColor: const Color(0xFF1EB482), foregroundColor: Colors.black,
                      padding: const EdgeInsets.symmetric(vertical: 14),
                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
                    ),
                    child: _loading
                        ? const SizedBox(width: 20, height: 20, child: CircularProgressIndicator(strokeWidth: 2, color: Colors.black))
                        : const Text('Créer mon email →', style: TextStyle(fontWeight: FontWeight.w600)),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _field(String label, TextEditingController ctrl, IconData icon, {bool obscure = false}) {
    return TextField(
      controller: ctrl, obscureText: obscure,
      style: const TextStyle(color: Colors.white, fontSize: 14),
      decoration: InputDecoration(
        labelText: label, labelStyle: TextStyle(color: Colors.grey.shade500, fontSize: 12),
        prefixIcon: Icon(icon, color: const Color(0xFF1EB482), size: 18),
        filled: true, fillColor: const Color(0xFF0A1A15),
        border: OutlineInputBorder(borderRadius: BorderRadius.circular(8), borderSide: const BorderSide(color: Color(0xFF1E293B))),
        enabledBorder: OutlineInputBorder(borderRadius: BorderRadius.circular(8), borderSide: const BorderSide(color: Color(0xFF1E293B))),
        focusedBorder: OutlineInputBorder(borderRadius: BorderRadius.circular(8), borderSide: const BorderSide(color: Color(0xFF1EB482))),
      ),
      onChanged: (_) => setState(() {}),
    );
  }
}
