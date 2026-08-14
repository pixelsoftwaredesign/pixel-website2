import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { Screen, Section, Card, dark } from '../src/components';

const PILLIERS = [
  { icon: '🤖', t: 'Intelligence Artificielle', d: 'Algorithmes sur mesure intégrés dans vos espaces et processus métier.' },
  { icon: '💻', t: 'Logiciel & IoT', d: 'Applications, web, objets connectés qui communiquent en temps réel.' },
  { icon: '🏛️', t: 'Design d\'Intérieur', d: 'Architecture intérieure contemporaine résidentielle et professionnelle.' },
  { icon: '🎬', t: 'Multimédia & VR/AR', d: 'Rendus 3D, visites virtuelles et expériences immersives.' },
];

const STATS = [
  { n: '4', l: 'Disciplines' },
  { n: '48+', l: 'Projets livrés' },
  { n: '100%', l: 'Clients satisfaits' },
  { n: '24h', l: 'Délai de réponse' },
];

export default function APropos() {
  return (
    <Screen theme={dark}>
      <Section
        theme={dark}
        tag="// Notre vision"
        title="Un organisme intelligent qui évolue avec vous"
        sub="Pixel Software Design est une agence de développement logiciel et de design d'intérieur basée à El Hamma, Gabès, Tunisie. Nous concevons des écosystèmes intelligents où le monde physique et le monde numérique coexistent en parfaite harmonie."
      >
        <View style={styles.statsRow}>
          {STATS.map((s) => (
            <View key={s.l} style={styles.stat}>
              <Text style={styles.statN}>{s.n}</Text>
              <Text style={[styles.statL, { color: dark.muted }]}>{s.l}</Text>
            </View>
          ))}
        </View>
      </Section>
      <Section theme={dark} alt tag="// Nos piliers" title="Quatre disciplines, une vision unifiée">
        {PILLIERS.map((p) => (
          <Card key={p.t} theme={creamLike}>
            <View style={styles.pRow}>
              <Text style={styles.pIcon}>{p.icon}</Text>
              <View style={{ flex: 1 }}>
                <Text style={[styles.pTitle, { color: creamLike.text }]}>{p.t}</Text>
                <Text style={[styles.pDesc, { color: creamLike.muted }]}>{p.d}</Text>
              </View>
            </View>
          </Card>
        ))}
      </Section>
      <Section theme={dark} tag="// Informations" title="Nous contacter">
        {[
          ['📍', 'El Hamma, Gabès, Tunisie'],
          ['✉️', 'pixelsoftwaredesign@gmail.com'],
          ['📞', '+216 52 675 027'],
        ].map(([e, v]) => (
          <View key={v} style={styles.contactRow}>
            <Text style={styles.contactEmoji}>{e}</Text>
            <Text style={[styles.contactText, { color: dark.muted }]}>{v}</Text>
          </View>
        ))}
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
  statsRow: { flexDirection: 'row', flexWrap: 'wrap', gap: 24, marginTop: 10 },
  stat: { minWidth: 100 },
  statN: { fontFamily: 'Space Mono, monospace', fontSize: 24, fontWeight: '700', color: dark.accent },
  statL: { fontSize: 12, marginTop: 4 },
  pRow: { flexDirection: 'row', gap: 14, alignItems: 'flex-start' },
  pIcon: { fontSize: 26 },
  pTitle: { fontSize: 16, fontWeight: '700', marginBottom: 6 },
  pDesc: { fontSize: 14, lineHeight: 21 },
  contactRow: { flexDirection: 'row', gap: 10, alignItems: 'center', marginBottom: 12 },
  contactEmoji: { fontSize: 16 },
  contactText: { fontSize: 14 },
});
