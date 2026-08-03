"""
PixSoftMoney — Internationalisation
Moteur de traduction par dictionnaire (sans compilation .po/.mo).
Langues: fr (défaut), en, ar (RTL), it, es.
"""
import threading

LANGUAGES = {
    'fr': {'code': 'fr', 'label': 'Français', 'flag': '🇫🇷', 'rtl': False},
    'en': {'code': 'en', 'label': 'English', 'flag': '🇬🇧', 'rtl': False},
    'ar': {'code': 'ar', 'label': 'العربية', 'flag': '🇹🇳', 'rtl': True},
    'it': {'code': 'it', 'label': 'Italiano', 'flag': '🇮🇹', 'rtl': False},
    'es': {'code': 'es', 'label': 'Español', 'flag': '🇪🇸', 'rtl': False},
}

# Ordre d'affichage du sélecteur
LANGUAGE_ORDER = ['fr', 'en', 'ar', 'it', 'es']

# Clé de langue enfilée par request (thread-local, car pas de middleware ici)
_local = threading.local()

SUPPORTED = set(LANGUAGES.keys())
DEFAULT_LANG = 'fr'


def set_lang(lang: str):
    _local.lang = lang if lang in SUPPORTED else DEFAULT_LANG


def get_lang() -> str:
    return getattr(_local, 'lang', DEFAULT_LANG)


def is_rtl(lang: str = None) -> bool:
    lang = lang or get_lang()
    return bool(LANGUAGES.get(lang, {}).get('rtl'))


# ─── Dictionnaire de traduction ─────────────────────────────
# Clé = texte français (tel qu'il apparaît dans les templates).
# Seulement les textes présentant un intérêt d'affichage sont traduits.
_T = {
    # ─── Navigation ───
    'Accueil': {'en': 'Home', 'ar': 'الرئيسية', 'it': 'Home', 'es': 'Inicio'},
    'Logiciels': {'en': 'Software', 'ar': 'البرمجيات', 'it': 'Software', 'es': 'Software'},
    'Pourquoi nous': {'en': 'Why us', 'ar': 'لماذا نحن', 'it': 'Perché noi', 'es': 'Por qué nosotros'},
    'Projets': {'en': 'Projects', 'ar': 'المشاريع', 'it': 'Progetti', 'es': 'Proyectos'},
    'Processus': {'en': 'Process', 'ar': 'المنهجية', 'it': 'Processo', 'es': 'Proceso'},
    'Pages': {'en': 'Pages', 'ar': 'الصفحات', 'it': 'Pagine', 'es': 'Páginas'},
    'À propos': {'en': 'About', 'ar': 'من نحن', 'it': 'Chi siamo', 'es': 'Acerca de'},
    'Témoignages': {'en': 'Testimonials', 'ar': 'الشهادات', 'it': 'Testimonianze', 'es': 'Testimonios'},
    'Prix': {'en': 'Pricing', 'ar': 'الأسعار', 'it': 'Prezzi', 'es': 'Precios'},
    'FAQ': {'en': 'FAQ', 'ar': 'الأسئلة', 'it': 'FAQ', 'es': 'FAQ'},
    'Contact': {'en': 'Contact', 'ar': 'اتصل بنا', 'it': 'Contatti', 'es': 'Contacto'},
    'Connexion': {'en': 'Login', 'ar': 'تسجيل الدخول', 'it': 'Accedi', 'es': 'Iniciar sesión'},
    'Inscription': {'en': 'Register', 'ar': 'التسجيل', 'it': 'Registrati', 'es': 'Registrarse'},
    'Déconnexion': {'en': 'Logout', 'ar': 'تسجيل الخروج', 'it': 'Esci', 'es': 'Cerrar sesión'},
    'Dashboard': {'en': 'Dashboard', 'ar': 'لوحة التحكم', 'it': 'Pannello', 'es': 'Panel'},
    'Wallet': {'en': 'Wallet', 'ar': 'المحفظة', 'it': 'Portafoglio', 'es': 'Monedero'},
    'Historique': {'en': 'History', 'ar': 'السجل', 'it': 'Cronologia', 'es': 'Historial'},
    'Tableau de bord': {'en': 'Dashboard', 'ar': 'لوحة التحكم', 'it': 'Pannello', 'es': 'Panel'},
    'Projets internes': {'en': 'Internal projects', 'ar': 'مشاريع داخلية', 'it': 'Progetti interni', 'es': 'Proyectos internos'},
    'Delv': {'en': 'Delv', 'ar': 'ديلف', 'it': 'Delv', 'es': 'Delv'},
    'PixMaps — Web App': {'en': 'PixMaps — Web App', 'ar': 'بيكسمابس — تطبيق ويب', 'it': 'PixMaps — Web App', 'es': 'PixMaps — Web App'},
    'PixSoftPay': {'en': 'PixSoftPay', 'ar': 'بيكس سوفت باي', 'it': 'PixSoftPay', 'es': 'PixSoftPay'},
    'Créer un QR': {'en': 'Create QR', 'ar': 'إنشاء رمز QR', 'it': 'Crea QR', 'es': 'Crear QR'},
    'Mon Wallet': {'en': 'My Wallet', 'ar': 'محفظتي', 'it': 'Il mio portafoglio', 'es': 'Mi monedero'},
    'GestiActiv ERP': {'en': 'GestiActiv ERP', 'ar': 'جستي أكتيف', 'it': 'GestiActiv ERP', 'es': 'GestiActiv ERP'},
    'Restaurant & Café': {'en': 'Restaurant & Café', 'ar': 'مطعم ومقهى', 'it': 'Ristorante & Caffè', 'es': 'Restaurante y Café'},
    'Pâtisserie Gestio & Caisse': {'en': 'Pastry & POS', 'ar': 'معجنات ونقطة بيع', 'it': 'Pasticceria & POS', 'es': 'Repostería y POS'},
    'PixelSoftCode': {'en': 'PixelSoftCode', 'ar': 'بيكسل سوفت كود', 'it': 'PixelSoftCode', 'es': 'PixelSoftCode'},
    'Inner Studio 3D': {'en': 'Inner Studio 3D', 'ar': 'إينر ستوديو 3D', 'it': 'Inner Studio 3D', 'es': 'Inner Studio 3D'},
    'Atelier Créatif & Dev': {'en': 'Creative Workshop & Dev', 'ar': 'ورشة إبداعية وتطوير', 'it': 'Laboratorio Creativo & Dev', 'es': 'Taller Creativo y Dev'},
    'Pixel Graphisme': {'en': 'Pixel Graphic Design', 'ar': 'بيكسل للتصميم', 'it': 'Pixel Grafica', 'es': 'Pixel Diseño'},
    'Graphisme': {'en': 'Graphic Design', 'ar': 'التصميم الجرافيكي', 'it': 'Grafica', 'es': 'Diseño'},
    'PixGameHub': {'en': 'PixGameHub', 'ar': 'بيكس جيم هب', 'it': 'PixGameHub', 'es': 'PixGameHub'},
    'PixMaps': {'en': 'PixMaps', 'ar': 'بيكس مابس', 'it': 'PixMaps', 'es': 'PixMaps'},

    # ─── PixSoftPay nav ───
    'Chain': {'en': 'Chain', 'ar': 'السلسلة', 'it': 'Catena', 'es': 'Cadena'},
    'Token': {'en': 'Token', 'ar': 'العملة', 'it': 'Token', 'es': 'Token'},
    'Vote': {'en': 'Vote', 'ar': 'التصويت', 'it': 'Voto', 'es': 'Votar'},
    'Stake': {'en': 'Stake', 'ar': 'التحصيص', 'it': 'Stake', 'es': 'Stake'},
    'Envoyer': {'en': 'Send', 'ar': 'إرسال', 'it': 'Invia', 'es': 'Enviar'},
    'Recevoir': {'en': 'Receive', 'ar': 'استلام', 'it': 'Ricevi', 'es': 'Recibir'},
    'Retirer': {'en': 'Withdraw', 'ar': 'سحب', 'it': 'Preleva', 'es': 'Retirar'},
    'Déposer': {'en': 'Deposit', 'ar': 'إيداع', 'it': 'Deposita', 'es': 'Depositar'},
    'Acheter PSX': {'en': 'Buy PSX', 'ar': 'شراء PSX', 'it': 'Compra PSX', 'es': 'Comprar PSX'},
    'Nouveau QR': {'en': 'New QR', 'ar': 'QR جديد', 'it': 'Nuovo QR', 'es': 'Nuevo QR'},
    'Parrainage': {'en': 'Referral', 'ar': 'الإحالة', 'it': 'Referral', 'es': 'Referido'},
    'Vérification': {'en': 'Verification', 'ar': 'التحقق', 'it': 'Verifica', 'es': 'Verificación'},
    'Site': {'en': 'Site', 'ar': 'الموقع', 'it': 'Sito', 'es': 'Sitio'},
}


def translate(text: str, lang: str = None, _lazy_cache=None) -> str:
    """Traduit un texte français vers la langue demandée (ou courante)."""
    lang = lang or get_lang()
    if lang == DEFAULT_LANG:
        return text
    entry = _T.get(text)
    if entry:
        return entry.get(lang, text)
    return text


def translate_dict(d, lang: str = None):
    """Traduit récursivement un dict/str."""
    lang = lang or get_lang()
    if isinstance(d, str):
        return translate(d, lang)
    if isinstance(d, list):
        return [translate_dict(i, lang) for i in d]
    if isinstance(d, dict):
        return {k: translate_dict(v, lang) for k, v in d.items()}
    return d
