import 'dart:convert';
import 'package:http/http.dart' as http;

class PixMailApi {
  static const String baseUrl = 'http://127.0.0.1:8000';

  Future<Map<String, dynamic>> register(String username, String password, {String displayName = ''}) async {
    final response = await http.post(
      Uri.parse('$baseUrl/api/pixmail/register/'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'username': username, 'password': password, 'display_name': displayName}),
    );
    return jsonDecode(response.body);
  }

  Future<Map<String, dynamic>> login(String username, String password) async {
    final response = await http.post(
      Uri.parse('$baseUrl/api/pixmail/login/'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'username': username, 'password': password}),
    );
    return jsonDecode(response.body);
  }

  Future<Map<String, dynamic>> sendMessage(String sender, String recipient, String subject, String body) async {
    final response = await http.post(
      Uri.parse('$baseUrl/api/pixmail/send/'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'sender': sender, 'recipient': recipient, 'subject': subject, 'body': body}),
    );
    return jsonDecode(response.body);
  }

  Future<List<Map<String, dynamic>>> getMessages(String email, {String folder = 'inbox'}) async {
    final response = await http.get(
      Uri.parse('$baseUrl/api/pixmail/messages/?email=$email&folder=$folder'),
      headers: {'Content-Type': 'application/json'},
    );
    final data = jsonDecode(response.body);
    return List<Map<String, dynamic>>.from(data['messages'] ?? []);
  }
}
