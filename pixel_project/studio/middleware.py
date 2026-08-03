from .i18n import set_lang, get_lang, DEFAULT_LANG


class LanguageMiddleware:
    """Met la langue courante à disposition (depuis session ou cookie)."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        lang = None
        if request.session.get('lang'):
            lang = request.session['lang']
        elif request.COOKIES.get('django_language'):
            lang = request.COOKIES.get('django_language')
        set_lang(lang or DEFAULT_LANG)
        request.LANGUAGE_CODE = lang or DEFAULT_LANG
        return self.get_response(request)


class LanguageInjectMiddleware:
    """Injecte le sélecteur de langue + RTL dans toutes les réponses HTML.
    Fonctionne sur les 100+ templates sans avoir à les modifier un par un."""

    SNIPPET = r"""
<script>
(function(){
  var LANGS={fr:['\u{1F1EB}\u{1F1F7}','Français'],en:['\u{1F1EC}\u{1F1E7}','English'],ar:['\u{1F1F9}\u{1F1F3}','العربية'],it:['\u{1F1EE}\u{1F1F9}','Italiano'],es:['\u{1F1EA}\u{1F1F8}','Español']};
  var ORDER=['fr','en','ar','it','es'];
  var NAV_T={
    'Accueil':{en:'Home',ar:'الرئيسية',it:'Home',es:'Inicio'},
    'Logiciels':{en:'Software',ar:'البرمجيات',it:'Software',es:'Software'},
    'Pourquoi nous':{en:'Why us',ar:'لماذا نحن',it:'Perché noi',es:'Por qué'},
    'Projets':{en:'Projects',ar:'المشاريع',it:'Progetti',es:'Proyectos'},
    'Processus':{en:'Process',ar:'المنهجية',it:'Processo',es:'Proceso'},
    'Pages':{en:'Pages',ar:'الصفحات',it:'Pagine',es:'Páginas'},
    'À propos':{en:'About',ar:'من نحن',it:'Chi siamo',es:'Acerca de'},
    'Témoignages':{en:'Testimonials',ar:'الشهادات',it:'Testimonianze',es:'Testimonios'},
    'Prix':{en:'Pricing',ar:'الأسعار',it:'Prezzi',es:'Precios'},
    'Contact':{en:'Contact',ar:'اتصل بنا',it:'Contatti',es:'Contacto'},
    'Dashboard':{en:'Dashboard',ar:'لوحة التحكم',it:'Pannello',es:'Panel'},
    'Wallet':{en:'Wallet',ar:'المحفظة',it:'Portafoglio',es:'Monedero'},
    'Historique':{en:'History',ar:'السجل',it:'Cronologia',es:'Historial'},
    'Mon Wallet':{en:'My Wallet',ar:'محفظتي',it:'Il mio portafoglio',es:'Mi monedero'},
    'Créer un QR':{en:'Create QR',ar:'إنشاء رمز QR',it:'Crea QR',es:'Crear QR'},
    'Envoyer':{en:'Send',ar:'إرسال',it:'Invia',es:'Enviar'},
    'Recevoir':{en:'Receive',ar:'استلام',it:'Ricevi',es:'Recibir'},
    'Retirer':{en:'Withdraw',ar:'سحب',it:'Preleva',es:'Retirar'},
    'Déposer':{en:'Deposit',ar:'إيداع',it:'Deposita',es:'Depositar'},
    'Acheter PSX':{en:'Buy PSX',ar:'شراء PSX',it:'Compra PSX',es:'Comprar PSX'},
    'Nouveau QR':{en:'New QR',ar:'QR جديد',it:'Nuovo QR',es:'Nuevo QR'},
    'Parrainage':{en:'Referral',ar:'الإحالة',it:'Referral',es:'Referido'},
    'Vérification':{en:'Verification',ar:'التحقق',it:'Verifica',es:'Verificación'},
    'Chain':{en:'Chain',ar:'السلسلة',it:'Catena',es:'Cadena'},
    'Token':{en:'Token',ar:'العملة',it:'Token',es:'Token'},
    'Vote':{en:'Vote',ar:'التصويت',it:'Voto',es:'Votar'},
    'Stake':{en:'Stake',ar:'التحصيص',it:'Stake',es:'Stake'},
    'Site':{en:'Site',ar:'الموقع',it:'Sito',es:'Sitio'},
    'Connexion':{en:'Login',ar:'تسجيل الدخول',it:'Accedi',es:'Iniciar sesión'},
    'GestiActiv ERP':{en:'GestiActiv ERP',ar:'جستي أكتيف',it:'GestiActiv ERP',es:'GestiActiv ERP'},
    'Tableau de bord':{en:'Dashboard',ar:'لوحة التحكم',it:'Pannello',es:'Panel'},
    'Restaurant & Café':{en:'Restaurant & Café',ar:'مطعم ومقهى',it:'Ristorante & Caffè',es:'Restaurante y Café'},
    'Pâtisserie Gestio & Caisse':{en:'Pastry & POS',ar:'معجنات ونقطة بيع',it:'Pasticceria & POS',es:'Repostería y POS'},
    'Inner Studio 3D':{en:'Inner Studio 3D',ar:'إينر ستوديو 3D',it:'Inner Studio 3D',es:'Inner Studio 3D'},
    'Atelier Créatif & Dev':{en:'Creative Workshop & Dev',ar:'ورشة إبداعية وتطوير',it:'Laboratorio Creativo & Dev',es:'Taller Creativo y Dev'},
    'Pixel Graphisme':{en:'Pixel Graphic Design',ar:'بيكسل للتصميم',it:'Pixel Grafica',es:'Pixel Diseño'},
    'Projets internes':{en:'Internal projects',ar:'مشاريع داخلية',it:'Progetti interni',es:'Proyectos internos'},
    'PixMaps — Web App':{en:'PixMaps — Web App',ar:'بيكسمابس — تطبيق ويب',it:'PixMaps — Web App',es:'PixMaps — Web App'}
  };
  var m=document.cookie.match(/(^| )django_language=([^;]+)/);
  var cur=m&&LANGS[m[2]]?m[2]:'fr';
  document.documentElement.setAttribute('lang',cur);
  if(cur==='ar'){document.documentElement.setAttribute('dir','rtl')}else{document.documentElement.removeAttribute('dir')}
  function addCSS(){var s=document.createElement('style');s.textContent=
    '.lang-selector{position:relative;display:inline-block;z-index:300;margin:0 0 0 14px}'+
    '.lang-btn{display:flex;align-items:center;gap:6px;background:rgba(30,180,130,.1);border:1px solid var(--border,#1e1e3a);color:inherit;font-family:inherit;font-size:.8rem;padding:.35rem .7rem;border-radius:6px;cursor:pointer}'+
    '.lang-code{font-size:.72rem;font-weight:700;letter-spacing:.05em}'+
    '.lang-dropdown{display:none;position:absolute;top:calc(100% + 8px);right:0;background:var(--surface,#081A14);border:1px solid var(--border,#1e1e3a);border-radius:10px;list-style:none;padding:.4rem;min-width:160px;z-index:400;margin:0}'+
    '.lang-selector.open .lang-dropdown{display:block}'+
    '.lang-dropdown li a{display:flex;align-items:center;gap:8px;padding:.5rem .7rem;font-size:.82rem;color:inherit;border-radius:6px;white-space:nowrap}'+
    '.lang-dropdown li a:hover{background:rgba(30,180,130,.1)}'+
    '.lang-dropdown li a.active{color:#1EB482;background:rgba(30,180,130,.08)}'+
    '@media(max-width:960px){.lang-selector{margin:.5rem 0 1rem;width:100%}.lang-btn{width:100%;justify-content:center}.lang-dropdown{right:auto;left:0;width:100%}}'+
    'html[dir="rtl"] .nav-menu{text-align:right}'+
    'html[dir="rtl"] .dropdown-menu{left:auto;right:0}';
    document.head.appendChild(s)}
  addCSS();
  function inject(c){if(c.querySelector('.lang-selector'))return;var el=document.createElement('div');el.className='lang-selector';
    el.innerHTML='<button type="button" class="lang-btn" aria-label="Langue"><span>'+LANGS[cur][0]+'</span> <span class="lang-code">'+cur.toUpperCase()+'</span></button><ul class="lang-dropdown">'+ORDER.map(function(code){return '<li><a href="/set-language/?lang='+code+'&next='+encodeURIComponent(location.pathname+location.search)+'"'+(code===cur?' class="active"':'')+'><span>'+LANGS[code][0]+'</span> '+LANGS[code][1]+'</a></li>'}).join('')+'</ul>';
    c.appendChild(el)}
  var navs=document.querySelectorAll('nav');for(var i=0;i<navs.length;i++){inject(navs[i])}
  if(cur!=='fr'){document.querySelectorAll('nav a').forEach(function(a){var raw=(a.textContent||'').replace(/\u25BE/g,'').trim();var hit=NAV_T[raw];if(hit&&hit[cur])a.textContent=hit[cur]})}
  document.addEventListener('click',function(e){var s=e.target.closest('.lang-selector');document.querySelectorAll('.lang-selector.open').forEach(function(x){if(x!==s)x.classList.remove('open')});if(s)s.classList.toggle('open')});
})();
</script>
"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        try:
            content_type = response.get('Content-Type', '')
            if 'text/html' not in content_type:
                return response
            body = response.content
            if not isinstance(body, bytes):
                return response
            if b'</body>' in body:
                response.content = body.replace(
                    b'</body>',
                    self.SNIPPET.encode('utf-8') + b'</body>',
                    1,
                )
        except Exception:
            pass
        return response

