(function(){
var fbConfig = {
  apiKey: "AIzaSyBi-RKMKmZUjw0aNd-fKUt6UshC3V4oLIU",
  authDomain: "pxelsoftware-64fcd.firebaseapp.com",
  projectId: "pxelsoftware-64fcd",
  storageBucket: "pxelsoftware-64fcd.firebasestorage.app",
  messagingSenderId: "349866475754",
  appId: "1:349866475754:web:b012870e830789a8165793"
};

var script1 = document.createElement('script');
script1.src = 'https://www.gstatic.com/firebasejs/10.12.2/firebase-app-compat.js';
document.head.appendChild(script1);

var script2 = document.createElement('script');
script2.src = 'https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore-compat.js';
document.head.appendChild(script2);

var FORMSUBMIT_URL = 'https://formsubmit.co/ajax/pixelsoftwaredesign@gmail.com';

function initFirebase(cb){
  script2.onload = function(){
    if(!firebase.apps.length) firebase.initializeApp(fbConfig);
    cb(firebase.firestore());
  };
}

function sendMessage(name, email, message, source){
  var msg = {
    name: name,
    email: email,
    message: message,
    source: source || 'contact',
    createdAt: new Date().toISOString(),
    read: false
  };

  var promises = [];

  promises.push(
    fetch(FORMSUBMIT_URL, {
      method: 'POST',
      headers: {'Content-Type': 'application/json','Accept': 'application/json'},
      body: JSON.stringify({
        _subject: '[Pixel Software Design] Nouveau message de ' + name,
        _template: 'table',
        Nom: name,
        Email: email,
        Message: message,
        Source: source || 'contact',
        Date: msg.createdAt
      })
    }).then(function(r){ return r.json() }).catch(function(e){ console.log('FormSubmit error:', e) })
  );

  if(script2.onload){
    initFirebase(function(db){
      db.collection('contact_messages').add(msg)
        .then(function(){ console.log('Message saved to Firestore') })
        .catch(function(e){ console.log('Firestore error:', e) });
    });
  }

  return Promise.all(promises);
}

window.PixContact = { send: sendMessage };
})();
