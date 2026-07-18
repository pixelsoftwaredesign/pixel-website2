import 'package:flutter/material.dart';
import '../services/pixmail_api.dart';
import 'pixmail_compose_screen.dart';
import 'pixmail_message_screen.dart';

class PixMailInboxScreen extends StatefulWidget {
  final String email;
  const PixMailInboxScreen({super.key, required this.email});
  @override
  State<PixMailInboxScreen> createState() => _PixMailInboxScreenState();
}

class _PixMailInboxScreenState extends State<PixMailInboxScreen> {
  final _api = PixMailApi();
  List<Map<String, dynamic>> _messages = [];
  bool _loading = true;
  String _folder = 'inbox';

  final Map<String, String> _folderLabels = {
    'inbox': '📥 Boîte de réception',
    'sent': '📤 Envoyés',
    'spam': '⚠️ Spam',
    'trash': '🗑️ Corbeille',
  };

  @override
  void initState() {
    super.initState();
    _loadMessages();
  }

  Future<void> _loadMessages() async {
    setState(() { _loading = true; });
    try {
      _messages = await _api.getMessages(widget.email, folder: _folder);
    } catch (e) {
      _messages = [];
    }
    setState(() { _loading = false; });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF05100D),
      appBar: AppBar(
        title: Text(_folderLabels[_folder] ?? 'Boîte de réception',
            style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w600)),
        backgroundColor: const Color(0xFF081511),
        actions: [
          PopupMenuButton<String>(
            icon: const Icon(Icons.folder_outlined, color: Color(0xFF1EB482)),
            onSelected: (f) { _folder = f; _loadMessages(); },
            itemBuilder: (_) => _folderLabels.entries.map((e) =>
              PopupMenuItem(value: e.key, child: Text(e.value, style: const TextStyle(fontSize: 13)))
            ).toList(),
          ),
          PopupMenuButton<String>(
            icon: const Icon(Icons.label_outline, color: Colors.white70),
            onSelected: (v) {
              if (v == 'account') _showAccountInfo();
            },
            itemBuilder: (_) => [
              PopupMenuItem(value: 'account', child: Text(widget.email, style: const TextStyle(fontSize: 12, fontFamily: 'monospace', color: Color(0xFF1EB482)))),
            ],
          ),
        ],
      ),
      body: _loading
          ? const Center(child: CircularProgressIndicator(color: Color(0xFF1EB482)))
          : _messages.isEmpty
              ? Center(
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Icon(Icons.inbox, size: 64, color: Colors.grey.shade700),
                      const SizedBox(height: 16),
                      Text('Aucun message', style: TextStyle(color: Colors.grey.shade500, fontSize: 14)),
                    ],
                  ),
                )
              : RefreshIndicator(
                  color: const Color(0xFF1EB482),
                  onRefresh: _loadMessages,
                  child: ListView.builder(
                    padding: const EdgeInsets.symmetric(vertical: 4),
                    itemCount: _messages.length,
                    itemBuilder: (ctx, i) => _msgTile(_messages[i]),
                  ),
                ),
      floatingActionButton: FloatingActionButton(
        onPressed: () => Navigator.push(context, MaterialPageRoute(
          builder: (_) => PixMailComposeScreen(senderEmail: widget.email),
        )).then((_) => _loadMessages()),
        backgroundColor: const Color(0xFF1EB482),
        child: const Icon(Icons.edit, color: Colors.black),
      ),
    );
  }

  Widget _msgTile(Map<String, dynamic> msg) {
    final bool unread = msg['is_read'] == false && _folder == 'inbox';
    final String sender = msg['sender'] ?? '';
    final String subject = msg['subject'] ?? '';
    final String preview = msg['body'] ?? '';
    final String date = msg['date_sent'] ?? '';

    String shortDate = '';
    if (date.isNotEmpty) {
      try {
        final dt = DateTime.parse(date);
        shortDate = '${dt.day}/${dt.month} ${dt.hour.toString().padLeft(2,'0')}:${dt.minute.toString().padLeft(2,'0')}';
      } catch (_) { shortDate = date.substring(0, 10); }
    }

    return ListTile(
      onTap: () => Navigator.push(context, MaterialPageRoute(
        builder: (_) => PixMailMessageScreen(msg: msg),
      )),
      contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 4),
      leading: Container(
        width: 36, height: 36,
        decoration: BoxDecoration(
          color: unread ? const Color(0xFF1EB482).withValues(alpha: 0.2) : const Color(0xFF1E293B),
          borderRadius: BorderRadius.circular(8),
        ),
        child: Center(
          child: Text(sender.isNotEmpty ? sender[0].toUpperCase() : '?',
              style: TextStyle(color: unread ? const Color(0xFF1EB482) : Colors.grey, fontWeight: FontWeight.bold, fontSize: 14)),
        ),
      ),
      title: Text(_folder == 'sent' ? (msg['recipient'] ?? '') : sender,
          style: TextStyle(fontSize: 13, fontWeight: unread ? FontWeight.w600 : FontWeight.w400, color: Colors.white)),
      subtitle: Text('$subject — $preview', maxLines: 1, overflow: TextOverflow.ellipsis,
          style: TextStyle(fontSize: 12, color: Colors.grey.shade500)),
      trailing: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.end,
        children: [
          Text(shortDate, style: const TextStyle(fontSize: 10, color: Colors.grey)),
          if (unread) ...[
            const SizedBox(height: 4),
            Container(width: 8, height: 8, decoration: const BoxDecoration(color: Color(0xFF1EB482), shape: BoxShape.circle)),
          ],
        ],
      ),
    );
  }

  void _showAccountInfo() {
    showModalBottomSheet(
      context: context,
      backgroundColor: const Color(0xFF111827),
      shape: const RoundedRectangleBorder(borderRadius: BorderRadius.vertical(top: Radius.circular(16))),
      builder: (_) => Container(
        padding: const EdgeInsets.all(24),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Container(width: 40, height: 4, decoration: BoxDecoration(color: Colors.grey.shade700, borderRadius: BorderRadius.circular(2))),
            const SizedBox(height: 20),
            const Icon(Icons.account_circle, color: Color(0xFF1EB482), size: 48),
            const SizedBox(height: 12),
            Text(widget.email, style: const TextStyle(fontSize: 14, fontWeight: FontWeight.w600, fontFamily: 'monospace', color: Color(0xFF1EB482))),
            const SizedBox(height: 8),
            Text('PixMail — Pixel Software Design', style: TextStyle(fontSize: 12, color: Colors.grey.shade500)),
            const SizedBox(height: 20),
          ],
        ),
      ),
    );
  }
}
