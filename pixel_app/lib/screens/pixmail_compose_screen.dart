import 'package:flutter/material.dart';
import '../services/pixmail_api.dart';

class PixMailComposeScreen extends StatefulWidget {
  final String senderEmail;
  final String? initialRecipient;
  final String? initialSubject;
  final String? initialBody;
  const PixMailComposeScreen({
    super.key, required this.senderEmail,
    this.initialRecipient, this.initialSubject, this.initialBody,
  });
  @override
  State<PixMailComposeScreen> createState() => _PixMailComposeScreenState();
}

class _PixMailComposeScreenState extends State<PixMailComposeScreen> {
  final _recipientCtrl = TextEditingController();
  final _subjectCtrl = TextEditingController();
  final _bodyCtrl = TextEditingController();
  final _api = PixMailApi();
  bool _sending = false;
  String? _error;

  @override
  void initState() {
    super.initState();
    if (widget.initialRecipient != null) _recipientCtrl.text = widget.initialRecipient!;
    if (widget.initialSubject != null) _subjectCtrl.text = widget.initialSubject!;
    if (widget.initialBody != null) _bodyCtrl.text = widget.initialBody!;
  }

  Future<void> _send() async {
    if (_recipientCtrl.text.isEmpty || _subjectCtrl.text.isEmpty || _bodyCtrl.text.isEmpty) {
      setState(() { _error = 'Tous les champs sont requis.'; });
      return;
    }
    setState(() { _sending = true; _error = null; });
    try {
      final result = await _api.sendMessage(widget.senderEmail, _recipientCtrl.text, _subjectCtrl.text, _bodyCtrl.text);
      if (result['status'] == 'success' || result['message'] != null) {
        if (!mounted) return;
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(content: Text('Message envoyé !'), backgroundColor: Color(0xFF1EB482)),
        );
        Navigator.pop(context);
      } else {
        setState(() { _error = result['message'] ?? 'Erreur d\'envoi'; });
      }
    } catch (e) {
      setState(() { _error = 'Serveur indisponible.'; });
    }
    setState(() { _sending = false; });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF05100D),
      appBar: AppBar(
        backgroundColor: const Color(0xFF081511),
        title: const Text('Nouveau message', style: TextStyle(fontSize: 16, fontWeight: FontWeight.w600)),
        actions: [
          TextButton(
            onPressed: _sending ? null : _send,
            child: _sending
                ? const SizedBox(width: 18, height: 18, child: CircularProgressIndicator(strokeWidth: 2, color: Color(0xFF1EB482)))
                : const Text('Envoyer', style: TextStyle(color: Color(0xFF1EB482), fontWeight: FontWeight.w600)),
          ),
        ],
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),
        child: Column(
          children: [
            if (_error != null)
              Container(
                padding: const EdgeInsets.all(10), margin: const EdgeInsets.only(bottom: 16),
                decoration: BoxDecoration(color: Colors.red.shade900.withValues(alpha: 0.3), borderRadius: BorderRadius.circular(8)),
                width: double.infinity,
                child: Text(_error!, style: const TextStyle(color: Colors.redAccent, fontSize: 12)),
              ),
            _field('De', TextEditingController(text: widget.senderEmail), Icons.person_outline, enabled: false),
            const SizedBox(height: 8),
            _field('À', _recipientCtrl, Icons.arrow_forward, hint: 'destinataire@pxelsoftware-64fcd.web.app'),
            const SizedBox(height: 8),
            _field('Objet', _subjectCtrl, Icons.title, hint: 'Objet du message'),
            const SizedBox(height: 16),
            TextField(
              controller: _bodyCtrl, maxLines: null, minLines: 12,
              style: const TextStyle(color: Colors.white, fontSize: 14, height: 1.7),
              decoration: InputDecoration(
                hintText: 'Rédigez votre message...', hintStyle: TextStyle(color: Colors.grey.shade600),
                filled: true, fillColor: const Color(0xFF0A1A15),
                border: OutlineInputBorder(borderRadius: BorderRadius.circular(8), borderSide: const BorderSide(color: Color(0xFF1E293B))),
                enabledBorder: OutlineInputBorder(borderRadius: BorderRadius.circular(8), borderSide: const BorderSide(color: Color(0xFF1E293B))),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _field(String label, TextEditingController ctrl, IconData icon, {String? hint, bool enabled = true}) {
    return TextField(
      controller: ctrl, enabled: enabled,
      style: TextStyle(color: enabled ? Colors.white : Colors.grey, fontSize: 13),
      decoration: InputDecoration(
        labelText: label, labelStyle: TextStyle(color: Colors.grey.shade500, fontSize: 11),
        hintText: hint, hintStyle: TextStyle(color: Colors.grey.shade700),
        prefixIcon: Icon(icon, color: const Color(0xFF1EB482), size: 16),
        filled: true, fillColor: const Color(0xFF0A1A15),
        border: OutlineInputBorder(borderRadius: BorderRadius.circular(8), borderSide: const BorderSide(color: Color(0xFF1E293B))),
        enabledBorder: OutlineInputBorder(borderRadius: BorderRadius.circular(8), borderSide: const BorderSide(color: Color(0xFF1E293B))),
        disabledBorder: OutlineInputBorder(borderRadius: BorderRadius.circular(8), borderSide: const BorderSide(color: Color(0xFF1E293B))),
      ),
    );
  }
}
