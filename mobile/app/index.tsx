import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { useRouter } from 'expo-router';
import { Screen, Section, Card, ButtonP, ButtonS, Chip, dark } from '../src/components';

const SERVICES = [
  { num: '01', title: 'Intelligence Artificielle & Solutions Digitales', items: ['Intégration d\'IA personnalisée', 'Stratégies de transformation digitale'] },
  { num: '02', title: 'Développement Logiciel & Conseil IT', items: ['Logiciels sur mesure', 'Conseil stratégique IT & IoT'] },
  { num: '03', title: 'Design d\'Intérieur & Espaces Intelligents', items: ['Design d\'intérieur évolué', 'Domotique avancée'] },
  { num: '04', title: 'Multimédia & Expériences Immersives', items: ['Visualisation 3D & visites virtuelles', 'Production multimédia'] },
];

const PROJETS = [
  { tag: 'Smart Home · IA · Design', title: 'Villa Jasmine — Résidence Intelligente', desc: 'Domotique complète + IA + design intérieur contemporain.' },
  { tag: 'Logiciel · IoT · SaaS', title: 'Noor Analytics — Plateforme intelligente', desc: 'SaaS analytics développé sur mesure.' },
  { tag: 'VR · 3D · Retail', title: 'Zaytouna — Visite virtuelle immersive', desc: 'Visite VR pour un espace retail.' },
  { tag: 'Interne · Outil', title: 'Delv — Outil interne de développement', desc: 'Outil interne de génération de code.' },
  { tag: 'Web App · Cartographie', title: 'PixMaps — Application web cartographique', desc: 'Application de cartographie web.' },
];

const ETAPES = [
  { n: '01', t: 'Découverte & Stratégie', d: 'Audit, analyse des besoins, feuille de route complète.' },
  { n: '02', t: 'Design & Architecture', d: 'Plans d\'intérieur, maquettes UI/UX, schémas IoT.' },
  { n: '03', t: 'Développement & Intégration', d: 'Code, hardware, domotique, IA — en parallèle.' },
  { n: '04', t: 'Tests & Déploiement', d: 'Tests complets, formation, déploiement progressif.' },
  { n: '05', t: 'Suivi & Évolution', d: 'Monitoring continu, mises à jour, nouvelles fonctionnalités.' },
];

export default function Home() {
  const router = useRouter();
  return (
    <Screen theme={dark}>
      <View style={styles.hero}>
        <View style={[styles.heroTag, { borderColor: dark.accent + '4D' }]}>
          <Text style={styles.heroTagText}>Studio Multidisciplinaire · Tunis</Text>
        </View>
        <Text style={styles.heroTitle}>
          L'architecture de{' '}
          <Text style={[styles.heroGrad, { color: dark.a2 }]}>l'innovation</Text>
        </Text>
        <Text style={styles.heroSub}>Là où l'espace rencontre l'intelligence.</Text>
        <Text style={styles.heroDesc}>
          Pixel Software Design fusionne le design d'intérieur, le développement logiciel,
          l'intelligence artificielle et le multimédia.
        </Text>
        <View style={styles.heroBtns}>
          <ButtonP theme={dark} onPress={() => router.push('/services')}>Découvrir nos services →</ButtonP>
          <ButtonS theme={dark} onPress={() => router.push('/contact')}>Démarrer un projet</ButtonS>
        </View>
        <View style={[styles.heroStats, { borderTopColor: dark.border }]}>
          <View><Text style={styles.statN}>4</Text><Text style={styles.statL}>Disciplines</Text></View>
          <View><Text style={styles.statN}>120+</Text><Text style={styles.statL}>Projets livrés</Text></View>
          <View><Text style={styles.statN}>100%</Text><Text style={styles.statL}>Clients satisfaits</Text></View>
        </View>
      </View>

      <Section
        theme={dark}
        tag="// Nos Services"
        title="Quatre disciplines, une vision unifiée"
        sub="De la disposition d'un meuble à l'écriture du code qui en contrôle l'éclairage via l'IA."
      >
        {SERVICES.map((s) => (
          <Card key={s.num} theme={dark}>
            <Text style={[styles.svcNum, { color: dark.accent }]}>{s.num}</Text>
            <Text style={styles.svcTitle}>{s.title}</Text>
            {s.items.map((it) => (
              <Text key={it} style={[styles.svcItem, { color: dark.muted }]}>▹ {it}</Text>
            ))}
          </Card>
        ))}
      </Section>

      <Section
        theme={dark}
        alt
        tag="// Pourquoi nous choisir"
        title="L'unique partenaire de la chaîne complète"
        sub="Une seule équipe maîtrise design, développement, IA et multimédia."
      >
        <View style={styles.uspGrid}>
          {['Vision 360° du projet', 'Technologie native, pas ajoutée', 'Écosystèmes qui évoluent', 'Expertise multisectorielle'].map((u, i) => (
            <Card key={u} theme={creamLike}>
              <View style={[styles.uspDot, { backgroundColor: creamLike.accent }]} />
              <Text style={styles.uspText}>{u}</Text>
            </Card>
          ))}
        </View>
      </Section>

      <Section theme={dark} tag="// Pôle Archi" title="Un pôle dédié au bâtiment">
        <Text style={[styles.svcItem, { color: dark.muted, marginBottom: 16 }]}>
          Ingénierie structurelle, architecture et design d'intérieur — de l'esquisse à la remise des clés.
        </Text>
        <ButtonP theme={dark} onPress={() => router.push('/pole-archi')}>Découvrir le Pôle Archi →</ButtonP>
      </Section>

      <Section theme={dark} alt tag="// Réalisations" title="Projets récents">
        {PROJETS.map((p) => (
          <Card key={p.title} theme={creamLike}>
            <Text style={[styles.projTag, { color: dark.a2 }]}>{p.tag}</Text>
            <Text style={styles.projTitle}>{p.title}</Text>
            <Text style={[styles.svcItem, { color: dark.muted }]}>{p.desc}</Text>
          </Card>
        ))}
      </Section>

      <Section theme={dark} tag="// Processus" title="Du concept à l'écosystème">
        {ETAPES.map((e) => (
          <View key={e.n} style={[styles.step, { borderBottomColor: dark.border }]}>
            <View style={[styles.stepN, { borderColor: dark.accent + '4D' }]}>
              <Text style={[styles.stepNText, { color: dark.accent }]}>{e.n}</Text>
            </View>
            <View style={{ flex: 1 }}>
              <Text style={styles.stepTitle}>{e.t}</Text>
              <Text style={[styles.svcItem, { color: dark.muted }]}>{e.d}</Text>
            </View>
          </View>
        ))}
      </Section>

      <Section theme={dark} alt tag="// Tarifs" title="Transparent dès le départ">
        {[
          { n: 'Essentiel', p: '3 000 DT / projet', f: ['Site web ou app mobile', 'Design UI/UX complet', 'Rendu 3D inclus'] },
          { n: 'Studio', p: '9 500 DT / projet', f: ['2–3 disciplines combinées', 'Intégration IoT basique', 'Visite virtuelle 3D'], feat: true },
          { n: 'Écosystème', p: 'Sur devis', f: ['4 disciplines intégrées', 'IA sur mesure & IoT avancé', 'Équipe dédiée'] },
        ].map((p) => (
          <Card key={p.n} theme={creamLike}>
            <Text style={[styles.svcNum, { color: p.feat ? dark.accent : dark.muted }]}>{p.n.toUpperCase()}</Text>
            <Text style={[styles.price, { color: p.feat ? dark.accent : dark.text }]}>{p.p}</Text>
            {p.f.map((f) => (
              <Text key={f} style={[styles.svcItem, { color: dark.muted }]}>▸ {f}</Text>
            ))}
            <View style={{ height: 12 }} />
            <ButtonP theme={dark} onPress={() => router.push('/contact')}>Démarrer →</ButtonP>
          </Card>
        ))}
      </Section>

      <Section theme={dark} tag="// Contact" title="Démarrons votre écosystème intelligent">
        <View style={styles.contactRow}><Text style={styles.contactEmoji}>📍</Text><Text style={[styles.svcItem, { color: dark.muted }]}>El Hamma, Gabès, Tunisie</Text></View>
        <View style={styles.contactRow}><Text style={styles.contactEmoji}>✉️</Text><Text style={[styles.svcItem, { color: dark.muted }]}>pixelsoftwaredesign@gmail.com</Text></View>
        <View style={styles.contactRow}><Text style={styles.contactEmoji}>📞</Text><Text style={[styles.svcItem, { color: dark.muted }]}>+216 52 675 027</Text></View>
        <View style={{ height: 16 }} />
        <ButtonP theme={dark} onPress={() => router.push('/contact')}>Envoyer ma demande →</ButtonP>
      </Section>
    </Screen>
  );
}

const creamLike = {
  bg: '#F6F1E7', surface: '#EFE7D8', card: '#FCF9F2',
  border: 'rgba(138,110,72,0.20)', accent: '#A67C3D',
  a2: '#B08D57', a3: '#C9A668', a4: '#8A6A3B',
  text: '#33281D', muted: 'rgba(60,46,28,0.62)',
  grad: ['#C9A668', '#A67C3D', '#8A6A3B'],
  font: 'Space Grotesk, sans-serif', serif: 'Playfair Display, serif', mono: 'Space Mono, monospace',
};

const styles = StyleSheet.create({
  hero: { paddingTop: 80, paddingHorizontal: 24, paddingBottom: 48 },
  heroTag: { alignSelf: 'flex-start', borderRadius: 999, borderWidth: 1, paddingHorizontal: 14, paddingVertical: 6, marginBottom: 24 },
  heroTagText: { fontSize: 11, letterSpacing: 2, textTransform: 'uppercase', color: dark.accent, fontFamily: 'Space Mono, monospace' },
  heroTitle: { fontSize: 40, fontWeight: '700', lineHeight: 46, letterSpacing: -1 },
  heroGrad: { color: dark.a2 },
  heroSub: { fontSize: 17, fontWeight: '300', color: dark.muted, marginTop: 12 },
  heroDesc: { fontSize: 15, lineHeight: 24, color: dark.muted, marginTop: 16, maxWidth: 560 },
  heroBtns: { flexDirection: 'row', gap: 12, marginTop: 28, flexWrap: 'wrap' },
  heroStats: { flexDirection: 'row', gap: 32, marginTop: 36, paddingTop: 20, borderTopWidth: 1 },
  statN: { fontFamily: 'Space Mono, monospace', fontSize: 22, fontWeight: '700', color: dark.accent },
  statL: { fontSize: 12, color: dark.muted, marginTop: 4 },
  svcNum: { fontFamily: 'Space Mono, monospace', fontSize: 11, marginBottom: 6, letterSpacing: 1 },
  svcTitle: { fontSize: 16, fontWeight: '700', marginBottom: 10 },
  svcItem: { fontSize: 14, lineHeight: 22, marginTop: 2 },
  uspGrid: { flexDirection: 'row', flexWrap: 'wrap', gap: 10 },
  uspDot: { width: 8, height: 8, borderRadius: 4, marginBottom: 8 },
  uspText: { fontSize: 15, fontWeight: '600', color: '#33281D' },
  projTag: { fontFamily: 'Space Mono, monospace', fontSize: 11, textTransform: 'uppercase', marginBottom: 6 },
  projTitle: { fontSize: 16, fontWeight: '600', marginBottom: 6 },
  step: { flexDirection: 'row', gap: 14, paddingVertical: 14, borderBottomWidth: 1 },
  stepN: { width: 32, height: 32, borderRadius: 16, borderWidth: 1, alignItems: 'center', justifyContent: 'center' },
  stepNText: { fontFamily: 'Space Mono, monospace', fontSize: 11, fontWeight: '700' },
  stepTitle: { fontSize: 15, fontWeight: '600', marginBottom: 4 },
  price: { fontSize: 26, fontFamily: 'Space Mono, monospace', fontWeight: '700', marginBottom: 10 },
  contactRow: { flexDirection: 'row', gap: 10, alignItems: 'center', marginBottom: 10 },
  contactEmoji: { fontSize: 16 },
});
