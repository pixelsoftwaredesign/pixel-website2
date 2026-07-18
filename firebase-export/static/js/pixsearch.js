(function(){
var css=document.createElement('style');
css.textContent=`
.ps-overlay{position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,.7);backdrop-filter:blur(8px);z-index:10000;display:none;justify-content:center;padding-top:12vh}
.ps-overlay.open{display:flex}
.ps-box{width:100%;max-width:620px;background:#0a1a15;border:1px solid #1a3a2a;border-radius:16px;overflow:hidden;max-height:70vh;display:flex;flex-direction:column;box-shadow:0 25px 60px rgba(0,0,0,.5)}
.ps-header{display:flex;align-items:center;padding:1rem 1.2rem;border-bottom:1px solid #1a3a2a;gap:.8rem}
.ps-header .icon{font-size:1.2rem;opacity:.6}
.ps-header input{flex:1;background:transparent;border:none;color:#fff;font-size:1rem;outline:none;font-family:'Space Grotesk',sans-serif}
.ps-header input::placeholder{color:#5a7a6a}
.ps-header .kbd{font-size:.6rem;padding:2px 6px;border-radius:4px;background:#1a3a2a;color:#5a7a6a;font-family:'Space Mono',monospace;border:1px solid #2a4a3a}
.ps-close{background:none;border:none;color:#5a7a6a;font-size:1rem;cursor:pointer;padding:4px 8px;border-radius:6px;transition:all .2s}
.ps-close:hover{color:#fff;background:#1a3a2a}
.ps-results{overflow-y:auto;padding:.5rem;flex:1}
.ps-results::-webkit-scrollbar{width:4px}
.ps-results::-webkit-scrollbar-thumb{background:#1a3a2a;border-radius:4px}
.ps-item{display:flex;align-items:flex-start;gap:.8rem;padding:.7rem .8rem;border-radius:10px;cursor:pointer;transition:background .15s;text-decoration:none;color:inherit}
.ps-item:hover,.ps-item.active{background:#1a3a2a}
.ps-item .ico{font-size:1.3rem;margin-top:.1rem;flex-shrink:0;width:28px;text-align:center}
.ps-item .info{flex:1;min-width:0}
.ps-item .info h4{font-size:.85rem;margin:0;font-weight:500;color:#e0e0e0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ps-item .info p{font-size:.7rem;color:#5a7a6a;margin:.2rem 0 0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ps-item .info .url{font-size:.6rem;color:#2DBD6E;font-family:'Space Mono',monospace}
.ps-empty{text-align:center;padding:2rem;color:#5a7a6a;font-size:.85rem}
.ps-footer{padding:.5rem 1.2rem;border-top:1px solid #1a3a2a;display:flex;gap:1rem;font-size:.65rem;color:#3a5a4a}
.ps-footer span{display:flex;align-items:center;gap:.3rem}
.ps-footer kbd{padding:1px 4px;background:#1a3a2a;border-radius:3px;font-family:'Space Mono',monospace}
.ps-cat{font-size:.6rem;color:#2DBD6E;padding:.3rem .8rem;font-family:'Space Mono',monospace;text-transform:uppercase;letter-spacing:.5px;margin-top:.3rem}
.ps-nav-btn{cursor:pointer;background:rgba(30,180,130,.1);border:1px solid rgba(30,180,130,.2);border-radius:8px;padding:6px 10px;font-size:.75rem;color:#2DBD6E;display:flex;align-items:center;gap:5px;font-family:'Space Grotesk',sans-serif;transition:all .2s;white-space:nowrap}
.ps-nav-btn:hover{background:rgba(30,180,130,.2);border-color:rgba(30,180,130,.4)}
.ps-nav-btn svg{width:14px;height:14px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round}
`;
document.head.appendChild(css);

var overlay=document.createElement('div');
overlay.className='ps-overlay';
overlay.id='psOverlay';
overlay.innerHTML=`
<div class="ps-box">
<div class="ps-header">
<span class="icon">🔍</span>
<input type="text" id="psInput" placeholder="Rechercher sur Pixel Software Design..." autocomplete="off">
<button class="ps-close" onclick="PS.close()">ESC</button>
</div>
<div class="ps-results" id="psResults">
<div class="ps-cat">Appuyez sur / pour ouvrir la recherche</div>
</div>
<div class="ps-footer">
<span><kbd>↑↓</kbd> naviguer</span>
<span><kbd>↵</kbd> ouvrir</span>
<span><kbd>esc</kbd> fermer</span>
<span style="margin-left:auto;color:#2DBD6E">PixSearch</span>
</div>
</div>`;
document.body.appendChild(overlay);

var btn=document.createElement('button');
btn.className='ps-nav-btn';
btn.innerHTML='<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>PixSearch';
btn.onclick=function(){PS.open()};
var navUl=document.querySelector('.nav-menu');
if(navUl){var li=document.createElement('li');li.appendChild(btn);navUl.insertBefore(li,navUl.lastElementChild)}

var index=[];
var activeIdx=-1;
var cats={};
var icons={'/':'🏠','/social/':'📱','/social/messagerie/':'💬','/pixmail/':'✉️','/pixmail/inscription/':'✉️','/pixmail/connexion/':'✉️','/portfolio/':'🎨','/contact/':'💬','/login/':'🔑','/register/':'🔑','/portail/':'👤','/forgot/':'🔑','/faq/':'❓','/a-propos/':'ℹ️','/prix/':'💰','/temoignages/':'⭐','/gestiactiv/':'📊','/ecommerce/':'🛒','/restaurant/':'🍽️','/patisserie/':'🧁','/graphisme/':'🎨','/innerstudio/':'🔮','/pixelsoftcode/':'💻','/uicatalogue/':'🧩','/app/':'📱','/atelier/':'🧩','/atelierdev/':'💻','/dashboard/':'📊','/logiciel-offline/':'📦','/abonnement/':'💳','/recrutement/':'👥'};

function init(){
fetch('/search-index.json').then(function(r){return r.json()}).then(function(d){
index=d;
}).catch(function(){})
}

function search(q){
if(!q||!q.trim())return[];
var terms=q.toLowerCase().split(/\s+/);
var results=[];
for(var i=0;i<index.length;i++){
var p=index[i];
var text=(p.title+' '+p.desc+' '+p.text).toLowerCase();
var score=0;
var matched=true;
for(var t=0;t<terms.length;t++){
if(text.indexOf(terms[t])===-1){matched=false;break}
score+=text.split(terms[t]).length-1;
}
if(matched)results.push({p:p,score:score});
}
results.sort(function(a,b){return b.score-a.score});
return results.map(function(r){return r.p});
}

function render(results,q){
var el=document.getElementById('psResults');
if(!results||results.length===0){
el.innerHTML='<div class="ps-empty">Aucun résultat pour "'+(q||'')+'"</div>';
return;
}
var h='';activeIdx=-1;
for(var i=0;i<results.length;i++){
var p=results[i];
var ico=icons[p.url]||'📄';
h+='<div class="ps-item" data-idx="'+i+'" onclick="PS.go(\''+p.url+'\')" onmouseenter="PS.act('+i+')"><div class="ico">'+ico+'</div><div class="info"><h4>'+esc(p.title)+'</h4><p>'+esc(p.desc||'')+'</p><div class="url">'+p.url+'</div></div></div>';
}
el.innerHTML=h;
}

function esc(s){var d=document.createElement('div');d.textContent=s;return d.innerHTML}

window.PS={
open:function(){document.getElementById('psOverlay').classList.add('open');document.getElementById('psInput').focus();document.getElementById('psInput').value='';document.getElementById('psResults').innerHTML='<div class="ps-cat">Tapez pour rechercher...</div>';activeIdx=-1;if(!index.length)init()},
close:function(){document.getElementById('psOverlay').classList.remove('open')},
go:function(url){window.location.href=url},
act:function(i){activeIdx=i;var items=document.querySelectorAll('.ps-item');items.forEach(function(el){el.classList.remove('active')});if(items[i])items[i].classList.add('active')},
search:function(){var q=document.getElementById('psInput').value;var r=search(q);render(r,q)}
};

document.getElementById('psInput').addEventListener('input',function(){PS.search()});
document.getElementById('psOverlay').addEventListener('click',function(e){if(e.target===this)PS.close()});

document.addEventListener('keydown',function(e){
if(e.key==='/'&&!document.getElementById('psOverlay').classList.contains('open')){
if(!['INPUT','TEXTAREA','SELECT'].includes(document.activeElement.tagName)){
e.preventDefault();PS.open();return;
}
}
if(e.key==='Escape'){PS.close();return}
if(!document.getElementById('psOverlay').classList.contains('open'))return;
var items=document.querySelectorAll('.ps-item');
if(!items.length)return;
if(e.key==='ArrowDown'){e.preventDefault();activeIdx=Math.min(activeIdx+1,items.length-1);PS.act(activeIdx)}
else if(e.key==='ArrowUp'){e.preventDefault();activeIdx=Math.max(activeIdx-1,0);PS.act(activeIdx)}
else if(e.key==='Enter'&&activeIdx>=0&&items[activeIdx]){var url=items[activeIdx].querySelector('.url').textContent;window.location.href=url}
});

init();
})();
