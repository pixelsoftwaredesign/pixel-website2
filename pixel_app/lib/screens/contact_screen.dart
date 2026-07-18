import 'package:flutter/material.dart';
import '../services/api_service.dart';

class ContactScreen extends StatefulWidget {
  const ContactScreen({super.key});
  @override
  State<ContactScreen> createState() => _ContactScreenState();
}

class _ContactScreenState extends State<ContactScreen> {
  final api = ApiService();
  final nameCtrl = TextEditingController();
  final emailCtrl = TextEditingController();
  final msgCtrl = TextEditingController();
  bool loading = false;
  String? result;

  void _submit() async {
    setState(() { loading = true; result = null; });
    try {
      final res = await api.sendContact(nameCtrl.text, emailCtrl.text, msgCtrl.text);
      setState(() => result = res['message'] ?? 'Envoyé !');
      nameCtrl.clear(); emailCtrl.clear(); msgCtrl.clear();
    } catch (e) {
      setState(() => result = 'Erreur d\'envoi');
    }
    setState(() => loading = false);
  }

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text('// Contact', style: TextStyle(color: Color(0xFF1EB482), fontSize: 12, letterSpacing: 2)),
            const SizedBox(height: 8),
            const Text('Démarrons votre\nécosystème intelligent', style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold, height: 1.3)),
            const SizedBox(height: 20),
            _infoRow(Icons.location_on_outlined, 'Tunis, Tunisie'),
            _infoRow(Icons.email_outlined, 'hello@pixelsoft.design'),
            _infoRow(Icons.phone_outlined, '+216 74 000 000'),
            const SizedBox(height: 28),
            _input('Prénom / Nom', nameCtrl, Icons.person_outline),
            _input('Email professionnel', emailCtrl, Icons.email_outlined),
            _input('Votre vision', msgCtrl, Icons.message_outlined, maxLines: 4),
            if (result != null) ...[
              const SizedBox(height: 8),
              Text(result!, style: TextStyle(color: result!.contains('Erreur') ? Colors.redAccent : const Color(0xFF1EB482), fontSize: 12)),
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
                    : const Text('Envoyer ma demande →'),
              ),
            ),
            const SizedBox(height: 24),
          ],
        ),
      ),
    );
  }

  static Widget _infoRow(IconData icon, String text) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 8),
      child: Row(children: [
        Icon(icon, color: const Color(0xFF1EB482), size: 18),
        const SizedBox(width: 10),
        Text(text, style: const TextStyle(color: Colors.grey, fontSize: 13)),
      ]),
    );
  }

  Widget _input(String label, TextEditingController ctrl, IconData icon, {int maxLines = 1}) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 12),
      child: TextField(
        controller: ctrl,
        maxLines: maxLines,
        style: const TextStyle(color: Colors.white),
        decoration: InputDecoration(
          labelText: label,
          prefixIcon: maxLines == 1 ? Icon(icon, color: Colors.grey, size: 20) : null,
          alignLabelWithHint: true,
          filled: true,
          fillColor: const Color(0xFF111827),
          border: OutlineInputBorder(borderRadius: BorderRadius.circular(10), borderSide: const BorderSide(color: Color(0xFF1E293B))),
          enabledBorder: OutlineInputBorder(borderRadius: BorderRadius.circular(10), borderSide: const BorderSide(color: Color(0xFF1E293B))),
          labelStyle: const TextStyle(color: Colors.grey),
        ),
      ),
    );
  }
}
