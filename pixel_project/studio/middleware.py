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

