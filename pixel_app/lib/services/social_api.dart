import 'dart:convert';
import 'package:http/http.dart' as http;

class SocialApiService {
  static const String baseUrl = 'http://127.0.0.1:8000/api/social';
  
  String? _username;
  String? _password;

  Map<String, String> get _headers => {
    'Content-Type': 'application/json',
    if (_username != null) 'Authorization': 'Basic ${base64Encode(utf8.encode('$_username:$_password'))}',
  };

  Future<Map<String, dynamic>> register(String username, String email, String password, {String displayName = ''}) async {
    final res = await http.post(
      Uri.parse('$baseUrl/register/'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'username': username, 'email': email, 'password': password, 'display_name': displayName}),
    );
    return jsonDecode(res.body);
  }

  Future<Map<String, dynamic>> login(String username, String password) async {
    final res = await http.post(
      Uri.parse('$baseUrl/login/'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'username': username, 'password': password}),
    );
    final data = jsonDecode(res.body);
    if (data['status'] == 'ok') {
      _username = username;
      _password = password;
    }
    return data;
  }

  void setCredentials(String username, String password) {
    _username = username;
    _password = password;
  }

  Future<Map<String, dynamic>> getProfile(String username) async {
    final res = await http.get(Uri.parse('$baseUrl/profile/$username/'), headers: _headers);
    return jsonDecode(res.body);
  }

  Future<Map<String, dynamic>> updateProfile(Map<String, dynamic> data) async {
    if (_username == null) return {'error': 'Non connecté'};
    final res = await http.post(
      Uri.parse('$baseUrl/profile/$_username/'),
      headers: _headers,
      body: jsonEncode(data),
    );
    return jsonDecode(res.body);
  }

  Future<Map<String, dynamic>> followUser(String username) async {
    final res = await http.post(
      Uri.parse('$baseUrl/follow/$username/'),
      headers: _headers,
    );
    return jsonDecode(res.body);
  }

  Future<Map<String, dynamic>> getFeed() async {
    final res = await http.get(Uri.parse('$baseUrl/feed/'), headers: _headers);
    return jsonDecode(res.body);
  }

  Future<Map<String, dynamic>> createPost(String content, {String visibility = 'public', String imageUrl = ''}) async {
    final res = await http.post(
      Uri.parse('$baseUrl/post/'),
      headers: _headers,
      body: jsonEncode({'content': content, 'visibility': visibility, 'image_url': imageUrl}),
    );
    return jsonDecode(res.body);
  }

  Future<Map<String, dynamic>> likePost(int postId) async {
    final res = await http.post(
      Uri.parse('$baseUrl/post/$postId/like/'),
      headers: _headers,
    );
    return jsonDecode(res.body);
  }

  Future<Map<String, dynamic>> commentPost(int postId, String content) async {
    final res = await http.post(
      Uri.parse('$baseUrl/post/$postId/comment/'),
      headers: _headers,
      body: jsonEncode({'content': content}),
    );
    return jsonDecode(res.body);
  }

  Future<Map<String, dynamic>> getNotifications() async {
    final res = await http.get(Uri.parse('$baseUrl/notifications/'), headers: _headers);
    return jsonDecode(res.body);
  }

  Future<Map<String, dynamic>> getConversations() async {
    final res = await http.get(Uri.parse('$baseUrl/conversations/'), headers: _headers);
    return jsonDecode(res.body);
  }

  Future<Map<String, dynamic>> createConversation(String title, String type, List<String> members) async {
    final res = await http.post(
      Uri.parse('$baseUrl/conversations/'),
      headers: _headers,
      body: jsonEncode({'title': title, 'type': type, 'members': members}),
    );
    return jsonDecode(res.body);
  }

  Future<Map<String, dynamic>> getMessages(int convId) async {
    final res = await http.get(
      Uri.parse('$baseUrl/conversations/$convId/messages/'),
      headers: _headers,
    );
    return jsonDecode(res.body);
  }

  Future<Map<String, dynamic>> sendMessage(int convId, Map<String, dynamic> encryptedData) async {
    final res = await http.post(
      Uri.parse('$baseUrl/conversations/$convId/messages/'),
      headers: _headers,
      body: jsonEncode(encryptedData),
    );
    return jsonDecode(res.body);
  }

  Future<Map<String, dynamic>> exchangeKeys(int convId, String publicKey) async {
    final res = await http.post(
      Uri.parse('$baseUrl/conversations/$convId/keys/'),
      headers: _headers,
      body: jsonEncode({'public_key': publicKey}),
    );
    return jsonDecode(res.body);
  }
}
