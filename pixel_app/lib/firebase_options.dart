import 'package:firebase_core/firebase_core.dart' show FirebaseOptions;
import 'package:flutter/foundation.dart'
    show defaultTargetPlatform, TargetPlatform;

class DefaultFirebaseOptions {
  static FirebaseOptions get currentPlatform {
    switch (defaultTargetPlatform) {
      case TargetPlatform.android:
        return android;
      case TargetPlatform.iOS:
        return ios;
      default:
        return web;
    }
  }

  static const FirebaseOptions web = FirebaseOptions(
    apiKey: 'AIzaSyBi-RKMKmZUjw0aNd-fKUt6UshC3V4oLIU',
    appId: '1:349866475754:web:b012870e830789a8165793',
    messagingSenderId: '349866475754',
    projectId: 'pxelsoftware-64fcd',
    authDomain: 'pxelsoftware-64fcd.firebaseapp.com',
    storageBucket: 'pxelsoftware-64fcd.firebasestorage.app',
    measurementId: 'G-76ELZTJBEM',
  );

  static const FirebaseOptions android = FirebaseOptions(
    apiKey: 'AIzaSyC3t0LIZC82dCZ3hKnJgisVjuARnHXLjt8',
    appId: '1:349866475754:android:888183f5e2bf93ca165793',
    messagingSenderId: '349866475754',
    projectId: 'pxelsoftware-64fcd',
    storageBucket: 'pxelsoftware-64fcd.firebasestorage.app',
  );
  static const FirebaseOptions ios = FirebaseOptions(
    apiKey: 'AIzaSyDummyKeyForIOS',
    appId: '1:117351586396109343888:ios:dummyios',
    messagingSenderId: '117351586396109343888',
    projectId: 'pxelsoftware-64fcd',
    storageBucket: 'pxelsoftware-64fcd.firebasestorage.app',
    iosBundleId: 'com.pixelsoftwaredesign.pixelapp',
  );
}
