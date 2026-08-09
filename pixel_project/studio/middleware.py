from .i18n import set_lang, get_lang, DEFAULT_LANG

import json
import re


class LanguageMiddleware:
    """Met la langue courante à disposition (depuis session ou cookie)."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        lang = request.GET.get('lang')
        if not lang or lang not in ('fr', 'en', 'ar', 'it', 'es', 'zh', 'ja', 'ru', 'fa', 'ur', 'hi'):
            lang = None
        if lang is None and request.session.get('lang'):
            lang = request.session['lang']
        if lang is None and request.COOKIES.get('django_language'):
            lang = request.COOKIES.get('django_language')
        set_lang(lang or DEFAULT_LANG)
        request.LANGUAGE_CODE = lang or DEFAULT_LANG
        return self.get_response(request)


class LanguageInjectMiddleware:
    """Injecte le sélecteur de langue + RTL + traduction du DOM entier dans
    toutes les réponses HTML. Fonctionne sur les 100+ templates sans les
    modifier un par un. Le dictionnaire est chargé depuis /i18n.js."""

    SNIPPET = r"""
<script src="/i18n.js?v=20260805"></script>
<script>
(function(){
  var LANGS={fr:['\u{1F1EB}\u{1F1F7}','Français'],en:['\u{1F1EC}\u{1F1E7}','English'],ar:['\u{1F1F9}\u{1F1F3}','العربية'],it:['\u{1F1EE}\u{1F1F9}','Italiano'],es:['\u{1F1EA}\u{1F1F8}','Español'],zh:['\u{1F1E8}\u{1F1F3}','中文'],ja:['\u{1F1EF}\u{1F1F5}','日本語'],ru:['\u{1F1F7}\u{1F1FA}','Русский'],fa:['\u{1F1EE}\u{1F1F7}','فارسی'],ur:['\u{1F1F5}\u{1F1F0}','اردو'],hi:['\u{1F1EE}\u{1F1F3}','हिन्दी']};
  var ORDER=['fr','en','ar','it','es','zh','ja','ru','fa','ur','hi'];
  var RTL={ar:1,fa:1,ur:1};
  var m=document.cookie.match(/(^| )django_language=([^;]+)/);
  var cur=m&&LANGS[m[2]]?m[2]:'fr';
  document.documentElement.setAttribute('lang',cur);
  if(RTL[cur]){document.documentElement.setAttribute('dir','rtl')}else{document.documentElement.removeAttribute('dir')}
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
    'html[dir="rtl"] .dropdown-menu{left:auto;right:0}'+
    'html[dir="rtl"] .lang-selector{margin:0 14px 0 0}'+
    'html[dir="rtl"] .lang-dropdown{left:0;right:auto}'+
    'html[dir="rtl"] input,html[dir="rtl"] textarea{text-align:right}';
    document.head.appendChild(s)}
  addCSS();
  function inject(c){var old=c.querySelector('.lang-selector');if(old)old.parentNode&&old.parentNode.removeChild(old);var el=document.createElement('div');el.className='lang-selector';
    el.innerHTML='<button type="button" class="lang-btn" aria-label="Langue"><span>'+LANGS[cur][0]+'</span> <span class="lang-code">'+cur.toUpperCase()+'</span></button><ul class="lang-dropdown">'+ORDER.map(function(code){return '<li><a href="/set-language/?lang='+code+'&next='+encodeURIComponent(location.pathname+location.search)+'"'+(code===cur?' class="active"':'')+'><span>'+LANGS[code][0]+'</span> '+LANGS[code][1]+'</a></li>'}).join('')+'</ul>';
    c.appendChild(el)}
  document.querySelectorAll('nav, .pp-nav').forEach(inject);
  if(cur!=='fr'){
    var I=window.PIXEL_I18N&&window.PIXEL_I18N.T?window.PIXEL_I18N.T:null;
    if(I){
      var KEYS=null;
      var cache={};
      function norm(s){return (s||'').replace(/\u200B/g,'').replace(/\u25BE/g,'').replace(/\s+/g,' ').trim()}
      function isL(ch){return !!ch&&/[\p{L}\p{N}]/u.test(ch)}
      function protect(s){return (s||'').replace(/Pixel\s*Software\s*Design/gi,'\uE000').replace(/pixelsoftwaredesign/gi,'\uE000')}
      function restore(s){return (s||'').replace(/\uE000/g,'Pixel Software Design')}
      function trPhrase(p){
        var hit=I[p];
        if(hit&&hit[cur]&&hit[cur]!==p)return hit[cur];
        if(!KEYS)KEYS=Object.keys(I).sort(function(a,b){return b.length-a.length});
        var out=p,i,start,idx,k,tr,b,a;
        for(i=0;i<KEYS.length;i++){
          k=KEYS[i];tr=I[k]&&I[k][cur];
          if(!tr||tr===k)continue;
          start=0;
          while((idx=out.indexOf(k,start))!==-1){
            b=idx>0?out[idx-1]:' ';
            a=idx+k.length<out.length?out[idx+k.length]:' ';
            if(!isL(b)&&!isL(a)){out=out.slice(0,idx)+tr+out.slice(idx+k.length);start=idx+tr.length}
            else{start=idx+k.length}
          }
        }
        return out;
      }
      function trRaw(raw){
        if(!raw)return null;
        var n=norm(raw);
        if(!n)return null;
        var nl=n.toLowerCase();
        if(nl==='pixel software design'||nl==='pixelsoftwaredesign')return raw;
        if(n.indexOf('@')!==-1)return raw;
        var key=cur+'\u0001'+n;
        if(key in cache)return cache[key];
        var hit=I[n];
        var out;
        if(hit&&hit[cur]&&hit[cur]!==n)out=hit[cur];
        else out=restore(trPhrase(protect(n)));
        cache[key]=out;
        return out;
      }
      var walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT,null,false);
      var nodes=[];
      while(walker.nextNode())nodes.push(walker.currentNode);
      for(var i=0;i<nodes.length;i++){
        var n=nodes[i];var p=n.parentNode;
        if(!p||!p.closest)continue;
        if(p.closest('.lang-selector,script,style,noscript,textarea,option,input,select'))continue;
        var raw=n.nodeValue;if(!raw)continue;
        var t=trRaw(raw);
        if(t&&t!==norm(raw))n.nodeValue=t;
      }
      ['placeholder','title','aria-label','alt'].forEach(function(attr){
        document.querySelectorAll('['+attr+']').forEach(function(el){
          var v=el.getAttribute(attr);
          var t=trRaw(v);
          if(t&&t!==norm(v))el.setAttribute(attr,t);
        });
      });
      var tt=trRaw(document.title);
      if(tt&&tt!==norm(document.title))document.title=tt;
    }
  }
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
                new_body = body.replace(
                    b'</body>',
                    self.SNIPPET.encode('utf-8') + b'</body>',
                    1,
                )
                response.content = new_body
                response['Content-Length'] = str(len(new_body))
        except Exception:
            pass
        return response


class SEOInjectMiddleware:
    """Injecte les balises SEO (meta description, canonical, hreflang,
    Open Graph, Twitter Cards et données structurées JSON-LD) dans le <head>
    de chaque page HTML, sans toucher aux templates un par un."""

    SITE = 'https://pixelsoftwaredesign.xyz'
    LANG_CODES = ['fr', 'en', 'ar', 'it', 'es', 'zh', 'ja', 'ru', 'fa', 'ur', 'hi']
    OG_LOCALES = {
        'fr': 'fr_FR', 'en': 'en_US', 'ar': 'ar_AR', 'it': 'it_IT', 'es': 'es_ES',
        'zh': 'zh_CN', 'ja': 'ja_JP', 'ru': 'ru_RU', 'fa': 'fa_IR', 'ur': 'ur_PK', 'hi': 'hi_IN',
    }

    DESCRIPTIONS = {
        '/': "Agence de développement logiciel à El Hamma, Gabès, Tunisie : sites web, applications mobiles, ERP GestiActiv, SaaS, design graphique et blockchain. Pixel Software Design conçoit vos écosystèmes intelligents.",
        '/a-propos/': "Découvrez Pixel Software Design, agence de développement basée à El Hamma, Gabès, Tunisie. Notre mission : concevoir des écosystèmes intelligents alliant design, logiciel et IA.",
        '/contact/': "Contactez Pixel Software Design à El Hamma, Gabès, Tunisie. Email : pixelsoftwaredesign@gmail.com, Téléphone : +216 52 675 027. Réponse sous 24h.",
        '/portfolio/': "Explorez le portfolio de Pixel Software Design : sites web, applications mobiles, ERP, design graphique et solutions sur mesure réalisés depuis la Tunisie.",
        '/prix/': "Prix et abonnements Pixel Software Design : GestiActiv ERP, PixelSoftCode, solutions SaaS et projets sur mesure. Paiement en ligne, par virement bancaire ou en espèces.",
        '/faq/': "Foire aux questions de Pixel Software Design : types de logiciels, solutions PME tunisiennes, abonnements, modes de paiement, délais, maintenance et recrutement.",
        '/temoignages/': "Témoignages clients de Pixel Software Design : découvrez ce que nos clients disent de nos solutions logicielles en Tunisie.",
        '/recrutement/': "Rejoignez l'équipe Pixel Software Design : postulez en tant que worker, partenaire ou freelance en développement web, mobile et ERP.",
        '/gestiactiv/': "GestiActiv ERP : logiciel de gestion complet pour les PME tunisiennes — comptabilité, RH, paie, commerce, santé, hôtellerie, restauration, auto-école et juridique.",
        '/restaurant/': "Solution Restaurant & Café : logiciel de caisse et de gestion des commandes, stocks et clients pour les restaurateurs et cafetiers.",
        '/patisserie/': "Pâtisserie Gestio & Caisse : logiciel de caisse et de gestion pour les pâtisseries et commerces de proximité.",
        '/pixelsoftcode/': "PixelSoftCode : plateforme d'abonnement SaaS de Pixel Software Design pour développer, héberger et gérer vos applications.",
        '/innerstudio/': "Inner Studio 3D : modélisation, visualisation et rendu 3D pour vos projets architecturaux et industriels.",
        '/uicatalogue/': "Atelier Créatif & Dev : design UI/UX, catalogues d'interfaces et développement créatif par Pixel Software Design.",
        '/graphisme/': "Pixel Graphisme : flyers, cartes de visite, logos et identité visuelle pour votre marque par Pixel Software Design.",
        '/pixmail/': "PixMail : service de messagerie professionnel sécurisé par Pixel Software Design.",
        '/login/': "Connectez-vous à votre espace client Pixel Software Design.",
        '/register/': "Créez votre compte Pixel Software Design et accédez à vos services.",
        '/pixsoftpay/': "PixSoftPay : paiement par QR code, wallet, virements et cryptomonnaies PSX avec Pixel Software Design.",
        '/logiciel-offline/': "Logiciels hors-ligne Pixel Software Design : solutions qui fonctionnent sans connexion Internet.",
    }

    DEFAULT_DESCRIPTION = "Pixel Software Design : agence de développement logiciel en Tunisie — sites web, applications, ERP, SaaS, design et blockchain."

    @classmethod
    def _description(cls, path):
        for prefix, desc in cls.DESCRIPTIONS.items():
            if path == prefix or path.startswith(prefix):
                return desc
        return cls.DEFAULT_DESCRIPTION

    @classmethod
    def _title(cls, body):
        m = re.search(r'<title[^>]*>(.*?)</title>', body, re.S | re.I)
        if m:
            t = m.group(1).strip()
            if t:
                return t
        return "Pixel Software Design — L'architecture de l'innovation"

    @classmethod
    def _canonical(cls, path):
        if path != '/':
            path = path.rstrip('/') + '/'
        return cls.SITE + path

    @classmethod
    def _hreflang(cls, path):
        url = cls._canonical(path)
        tags = ['<link rel="alternate" hreflang="x-default" href="%s">' % url]
        for code in cls.LANG_CODES:
            tags.append('<link rel="alternate" hreflang="%s" href="%s?lang=%s">' % (code, url, code))
        return '\n'.join(tags)

    @classmethod
    def _head_extra(cls, path, title, desc):
        url = cls._canonical(path)
        locale = cls.OG_LOCALES.get('fr')
        alt_locales = '\n'.join('<meta property="og:locale:alternate" content="%s">' % cls.OG_LOCALES[c] for c in cls.LANG_CODES if c != 'fr')
        image = cls.SITE + '/static/favicon.svg'
        return (
            '<meta name="description" content="%s">\n' % desc
            + '<meta name="robots" content="index, follow">\n'
            + '<link rel="canonical" href="%s">\n' % url
            + cls._hreflang(path) + '\n'
            + '<meta property="og:site_name" content="Pixel Software Design">\n'
            + '<meta property="og:type" content="website">\n'
            + '<meta property="og:locale" content="%s">\n' % locale
            + alt_locales + '\n'
            + '<meta property="og:url" content="%s">\n' % url
            + '<meta property="og:title" content="%s">\n' % title
            + '<meta property="og:description" content="%s">\n' % desc
            + '<meta property="og:image" content="%s">\n' % image
            + '<meta name="twitter:card" content="summary_large_image">\n'
            + '<meta name="twitter:title" content="%s">\n' % title
            + '<meta name="twitter:description" content="%s">\n' % desc
            + '<meta name="twitter:image" content="%s">\n' % image
        )

    @classmethod
    def _jsonld(cls):
        return (
            '<script type="application/ld+json">' + json.dumps({
                '@context': 'https://schema.org',
                '@graph': [
                    {
                        '@type': ['Organization', 'LocalBusiness'],
                        '@id': cls.SITE + '/#org',
                        'name': 'Pixel Software Design',
                        'slogan': "L'architecture de l'innovation",
                        'description': cls.DESCRIPTIONS['/'],
                        'url': cls.SITE + '/',
                        'logo': cls.SITE + '/static/favicon.svg',
                        'image': cls.SITE + '/static/favicon.svg',
                        'email': 'pixelsoftwaredesign@gmail.com',
                        'telephone': '+216 52 675 027',
                        'address': {
                            '@type': 'PostalAddress',
                            'addressLocality': 'El Hamma',
                            'addressRegion': 'Gabès',
                            'addressCountry': 'TN',
                        },
                        'openingHours': 'Mo-Fr 09:00-18:00',
                        'priceRange': '$$',
                    },
                    {
                        '@type': 'WebSite',
                        '@id': cls.SITE + '/#website',
                        'url': cls.SITE + '/',
                        'name': 'Pixel Software Design',
                        'publisher': {'@id': cls.SITE + '/#org'},
                    },
                ],
            }, ensure_ascii=False) + '</script>'
        )

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
            text = body.decode('utf-8', 'ignore')
            if '</head>' not in text:
                return response
            path = request.path
            title = self._title(text)
            desc = self._description(path)
            extra = self._head_extra(path, title, desc) + self._jsonld()
            new_text = text.replace('</head>', extra + '</head>', 1)
            response.content = new_text.encode('utf-8')
            response['Content-Length'] = str(len(response.content))
        except Exception:
            pass
        return response

