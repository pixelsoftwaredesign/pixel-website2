import 'package:flutter/material.dart';
import '../services/social_api.dart';

class SocialMessagesScreen extends StatefulWidget {
  const SocialMessagesScreen({super.key});
  @override
  State<SocialMessagesScreen> createState() => _SocialMessagesScreenState();
}

class _SocialMessagesScreenState extends State<SocialMessagesScreen> {
  final _api = SocialApiService();
  List<dynamic> _conversations = [];
  bool _loading = true;

  @override
  void initState() {
    super.initState();
    _loadConversations();
  }

  Future<void> _loadConversations() async {
    setState(() => _loading = true);
    final data = await _api.getConversations();
    setState(() {
      _conversations = data['conversations'] ?? [];
      _loading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Row(
          children: [
            Icon(Icons.lock, color: Color(0xFF1EB482), size: 18),
            SizedBox(width: 8),
            Text('Messagerie E2E', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
          ],
        ),
        actions: [
          IconButton(
            icon: const Icon(Icons.add_comment_outlined, color: Color(0xFF1EB482)),
            onPressed: _showNewConversationDialog,
          ),
        ],
      ),
      body: _loading
          ? const Center(child: CircularProgressIndicator(color: Color(0xFF1EB482)))
          : RefreshIndicator(
              onRefresh: _loadConversations,
              color: const Color(0xFF1EB482),
              child: _conversations.isEmpty
                  ? const Center(
                      child: Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Icon(Icons.chat_bubble_outline, size: 48, color: Colors.grey),
                          SizedBox(height: 12),
                          Text('Aucune conversation', style: TextStyle(color: Colors.grey)),
                          Text('Créez une conversation chiffrée', style: TextStyle(color: Colors.grey, fontSize: 12)),
                        ],
                      ),
                    )
                  : ListView.builder(
                      padding: const EdgeInsets.all(12),
                      itemCount: _conversations.length,
                      itemBuilder: (ctx, i) => _convTile(_conversations[i]),
                    ),
            ),
    );
  }

  Widget _convTile(dynamic conv) {
    final title = conv['title'] ?? 'Sans titre';
    final type = conv['type'] ?? 'private';
    final members = (conv['members'] as List?)?.join(', ') ?? '';
    final lastMsg = conv['last_message'] ?? '';
    final updated = conv['updated_at'] ?? '';

    return Container(
      margin: const EdgeInsets.only(bottom: 8),
      decoration: BoxDecoration(
        color: const Color(0xFF111827),
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: const Color(0xFF1E293B)),
      ),
      child: ListTile(
        contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
        leading: CircleAvatar(
          backgroundColor: const Color(0xFF1EB482),
          child: Text(title[0].toUpperCase(), style: const TextStyle(color: Colors.black, fontWeight: FontWeight.bold)),
        ),
        title: Row(
          children: [
            Expanded(
              child: Text(title, style: const TextStyle(fontWeight: FontWeight.w600, fontSize: 14)),
            ),
            if (type == 'group')
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                decoration: BoxDecoration(
                  color: const Color(0xFF1EB482).withValues(alpha: 0.15),
                  borderRadius: BorderRadius.circular(8),
                ),
                child: const Text('Groupe', style: TextStyle(color: Color(0xFF1EB482), fontSize: 9)),
              ),
          ],
        ),
        subtitle: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const SizedBox(height: 2),
            Text(members, style: const TextStyle(color: Colors.grey, fontSize: 11)),
            if (lastMsg.isNotEmpty) ...[
              const SizedBox(height: 4),
              Text(lastMsg, style: const TextStyle(color: Colors.grey, fontSize: 12), maxLines: 1, overflow: TextOverflow.ellipsis),
            ],
          ],
        ),
        trailing: const Icon(Icons.chevron_right, color: Colors.grey),
      ),
    );
  }

  void _showNewConversationDialog() {
    final titleCtrl = TextEditingController();
    final membersCtrl = TextEditingController();
    String type = 'private';

    showModalBottomSheet(
      context: context,
      backgroundColor: const Color(0xFF111827),
      shape: const RoundedRectangleBorder(borderRadius: BorderRadius.vertical(top: Radius.circular(16))),
      builder: (ctx) => Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text('Nouvelle conversation', style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
            const SizedBox(height: 16),
            TextField(
              controller: titleCtrl,
              style: const TextStyle(color: Colors.white),
              decoration: InputDecoration(
                hintText: 'Nom (optionnel)', hintStyle: const TextStyle(color: Colors.grey),
                filled: true, fillColor: const Color(0xFF0A0E17),
                border: OutlineInputBorder(borderRadius: BorderRadius.circular(10), borderSide: BorderSide.none),
              ),
            ),
            const SizedBox(height: 12),
            TextField(
              controller: membersCtrl,
              style: const TextStyle(color: Colors.white),
              decoration: InputDecoration(
                hintText: 'Membres (usernames, virgule)', hintStyle: const TextStyle(color: Colors.grey),
                filled: true, fillColor: const Color(0xFF0A0E17),
                border: OutlineInputBorder(borderRadius: BorderRadius.circular(10), borderSide: BorderSide.none),
              ),
            ),
            const SizedBox(height: 12),
            SegmentedButton<String>(
              segments: const [
                ButtonSegment(value: 'private', label: Text('Privé'), icon: Icon(Icons.lock_outline, size: 16)),
                ButtonSegment(value: 'group', label: Text('Groupe'), icon: Icon(Icons.group_outlined, size: 16)),
              ],
              selected: {type},
              onSelectionChanged: (s) => type = s.first,
              style: ButtonStyle(
                backgroundColor: WidgetStateProperty.resolveWith((states) =>
                  states.contains(WidgetState.selected) ? const Color(0xFF1EB482).withValues(alpha: 0.2) : null),
              ),
            ),
            const SizedBox(height: 20),
            SizedBox(
              width: double.infinity,
              child: ElevatedButton(
                onPressed: () async {
                  final members = membersCtrl.text.split(',').map((s) => s.trim()).where((s) => s.isNotEmpty).toList();
                  final data = await _api.createConversation(titleCtrl.text, type, members);
                  if (data['status'] == 'ok' && ctx.mounted) {
                    Navigator.pop(ctx);
                    _loadConversations();
                  }
                },
                style: ElevatedButton.styleFrom(
                  backgroundColor: const Color(0xFF1EB482),
                  foregroundColor: Colors.black,
                  padding: const EdgeInsets.symmetric(vertical: 14),
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                ),
                child: const Text('Créer', style: TextStyle(fontWeight: FontWeight.w700)),
              ),
            ),
            const SizedBox(height: 8),
          ],
        ),
      ),
    );
  }
}
