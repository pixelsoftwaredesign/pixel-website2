import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';

class ApiService {
  static const String baseUrl = 'https://pxelsoftware-64fcd.web.app';
  String? _token;

  Future<void> _loadToken() async {
    final prefs = await SharedPreferences.getInstance();
    _token = prefs.getString('auth_token');
  }

  Map<String, String> get _headers => {
        'Content-Type': 'application/json',
        if (_token != null) 'Authorization': 'Token $_token',
      };

  Future<Map<String, dynamic>> post(String path, {Map<String, dynamic>? body}) async {
    await _loadToken();
    final response = await http.post(
      Uri.parse('$baseUrl$path'),
      headers: _headers,
      body: body != null ? jsonEncode(body) : null,
    );
    return jsonDecode(response.body);
  }

  Future<Map<String, dynamic>> get(String path) async {
    await _loadToken();
    final response = await http.get(
      Uri.parse('$baseUrl$path'),
      headers: _headers,
    );
    return jsonDecode(response.body);
  }

  Future<void> saveToken(String token) async {
    _token = token;
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString('auth_token', token);
  }

  Future<void> clearToken() async {
    _token = null;
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove('auth_token');
  }

  Future<bool> get isLoggedIn async {
    await _loadToken();
    return _token != null;
  }

  // Auth
  Future<Map<String, dynamic>> login(String username, String password) =>
      post('/api/connexion/', body: {'username': username, 'password': password});

  Future<Map<String, dynamic>> register(String username, String email, String password, {String entreprise = '', String role = 'designer'}) =>
      post('/api/inscription/', body: {'username': username, 'email': email, 'password': password, 'entreprise': entreprise, 'role': role});

  Future<void> logout() async {
    await post('/api/deconnexion/');
    await clearToken();
  }

  // Contact
  Future<Map<String, dynamic>> sendContact(String name, String email, String message) =>
      post('/api/contact/', body: {'username': name, 'useremail': email, 'usermessage': message});

  // ERP
  Future<Map<String, dynamic>> erpDemo(String module, String label, String value) =>
      post('/api/erp/demo/', body: {'module': module, 'label': label, 'value': value});

  // E-commerce
  Future<Map<String, dynamic>> getProduits() => get('/api/produits/');
  Future<Map<String, dynamic>> getCategories() => get('/api/categories/');
  Future<Map<String, dynamic>> getPanier() => get('/api/panier/');
}
