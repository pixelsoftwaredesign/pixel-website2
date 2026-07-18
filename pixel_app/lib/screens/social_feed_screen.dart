import 'dart:convert';
import 'dart:html' as html;
import 'package:flutter/material.dart';
import '../services/social_api.dart';
import 'social_login_screen.dart';

class SocialFeedScreen extends StatefulWidget {
  final String? currentUser;
  const SocialFeedScreen({super.key, this.currentUser});
  @override
  State<SocialFeedScreen> createState() => _SocialFeedScreenState();
}

class _SocialFeedScreenState extends State<SocialFeedScreen> {
  final _api = SocialApiService();
  final _postCtrl = TextEditingController();
  List<dynamic> _posts = [];
  bool _loading = true;

  @override
  void initState() {
    super.initState();
    _loadFeed();
  }

  Future<void> _loadFeed() async {
    setState(() => _loading = true);
    final data = await _api.getFeed();
    setState(() {
      _posts = data['posts'] ?? [];
      _loading = false;
    });
  }

  Future<void> _createPost() async {
    final content = _postCtrl.text.trim();
    if (content.isEmpty) return;
    final data = await _api.createPost(content);
    if (data['status'] == 'ok') {
      _postCtrl.clear();
      _loadFeed();
    }
  }

  Future<void> _likePost(int id) async {
    await _api.likePost(id);
    _loadFeed();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Row(
          children: [
            Icon(Icons.people, color: Color(0xFF1EB482)),
            SizedBox(width: 8),
            Text('PixSocial', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
          ],
        ),
      ),
      body: _loading
          ? const Center(child: CircularProgressIndicator(color: Color(0xFF1EB482)))
          : RefreshIndicator(
              onRefresh: _loadFeed,
              color: const Color(0xFF1EB482),
              child: ListView(
                padding: const EdgeInsets.all(16),
                children: [
                  if (widget.currentUser != null) ...[
                    _composer(),
                    const SizedBox(height: 16),
                  ],
                  ..._posts.map((p) => _postCard(p)),
                  if (_posts.isEmpty)
                    const Center(
                      child: Padding(
                        padding: EdgeInsets.all(40),
                        child: Column(children: [
                          Icon(Icons.article_outlined, size: 48, color: Colors.grey),
                          SizedBox(height: 12),
                          Text('Aucun post pour l\'instant', style: TextStyle(color: Colors.grey)),
                          Text('Soyez le premier à publier !', style: TextStyle(color: Colors.grey, fontSize: 12)),
                        ]),
                      ),
                    ),
                ],
              ),
            ),
    );
  }

  Widget _composer() {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: const Color(0xFF111827),
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: const Color(0xFF1E293B)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              CircleAvatar(
                radius: 16,
                backgroundColor: const Color(0xFF1EB482),
                child: Text(
                  (widget.currentUser ?? '?')[0].toUpperCase(),
                  style: const TextStyle(color: Colors.black, fontWeight: FontWeight.bold, fontSize: 12),
                ),
              ),
              const SizedBox(width: 10),
              Expanded(
                child: TextField(
                  controller: _postCtrl,
                  style: const TextStyle(color: Colors.white, fontSize: 14),
                  maxLines: null,
                  decoration: const InputDecoration(
                    hintText: 'Quoi de neuf ?',
                    hintStyle: TextStyle(color: Colors.grey),
                    border: InputBorder.none,
                  ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 12),
          Align(
            alignment: Alignment.centerRight,
            child: ElevatedButton(
              onPressed: _createPost,
              style: ElevatedButton.styleFrom(
                backgroundColor: const Color(0xFF1EB482),
                foregroundColor: Colors.black,
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
              ),
              child: const Text('Publier', style: TextStyle(fontWeight: FontWeight.w700, fontSize: 13)),
            ),
          ),
        ],
      ),
    );
  }

  Widget _postCard(dynamic p) {
    final author = p['author'] ?? '?';
    final content = p['content'] ?? '';
    final likes = p['likes_count'] ?? 0;
    final comments = p['comments_count'] ?? 0;
    final isLiked = p['is_liked'] ?? false;
    final createdAt = p['created_at'] ?? '';
    
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
          Row(
            children: [
              CircleAvatar(
                radius: 16,
                backgroundColor: const Color(0xFF1EB482),
                child: Text(author[0].toUpperCase(), style: const TextStyle(color: Colors.black, fontWeight: FontWeight.bold, fontSize: 12)),
              ),
              const SizedBox(width: 10),
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(author, style: const TextStyle(fontWeight: FontWeight.w600, fontSize: 13)),
                  Text(_timeAgo(createdAt), style: const TextStyle(color: Colors.grey, fontSize: 10)),
                ],
              ),
            ],
          ),
          const SizedBox(height: 12),
          Text(content, style: const TextStyle(fontSize: 14, height: 1.5)),
          const SizedBox(height: 12),
          Row(
            children: [
              GestureDetector(
                onTap: () => _likePost(p['id']),
                child: Row(
                  children: [
                    Icon(isLiked ? Icons.favorite : Icons.favorite_border, color: isLiked ? Colors.red : Colors.grey, size: 18),
                    const SizedBox(width: 4),
                    Text('$likes', style: TextStyle(color: isLiked ? Colors.red : Colors.grey, fontSize: 12)),
                  ],
                ),
              ),
              const SizedBox(width: 16),
              Row(
                children: [
                  const Icon(Icons.comment_outlined, color: Colors.grey, size: 18),
                  const SizedBox(width: 4),
                  Text('$comments', style: const TextStyle(color: Colors.grey, fontSize: 12)),
                ],
              ),
            ],
          ),
        ],
      ),
    );
  }

  String _timeAgo(String iso) {
    try {
      final dt = DateTime.parse(iso).toLocal();
      final diff = DateTime.now().difference(dt);
      if (diff.inMinutes < 60) return 'il y a ${diff.inMinutes}m';
      if (diff.inHours < 24) return 'il y a ${diff.inHours}h';
      return 'il y a ${diff.inDays}j';
    } catch (_) {
      return '';
    }
  }
}
