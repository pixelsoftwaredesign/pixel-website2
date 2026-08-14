import { readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const dist = join(process.cwd(), 'dist');
const htmlPath = join(dist, 'index.html');
let html = readFileSync(htmlPath, 'utf8');

const head = [
  '<link rel="manifest" href="/manifest.json" />',
  '<meta name="theme-color" content="#05100D" />',
  '<link rel="apple-touch-icon" href="/icon.png" />',
].join('\n');

if (!html.includes('rel="manifest"')) {
  html = html.replace('</head>', head + '\n</head>');
}

const sw = '\n<script>if("serviceWorker" in navigator){navigator.serviceWorker.register("/sw.js").catch(()=>{});}</script>';
if (!html.includes('sw.js')) {
  html = html.replace('</body>', sw + '\n</body>');
}

writeFileSync(htmlPath, html);
console.log('PWA injected into dist/index.html');
