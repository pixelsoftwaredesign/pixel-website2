import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { useRouter } from 'expo-router';
import { Screen, Section, Card, ButtonP, dark } from '../src/components';

const PROJETS = [
  { tag: 'Smart Home · IA · Design', title: 'Villa Jasmine — Résidence Intelligente', desc: 'Domotique complète + IA + design intérieur contemporain. Contrôle vocal, gestion énergétique prédictive.' },
  { tag: 'Logiciel · IoT · SaaS', title: 'Noor Analytics — Plateforme intelligente', desc: 'Plateforme SaaS d\'analytics avec tableau de bord temps réel.' },
  { tag: 'VR · 3D · Retail', title: 'Zaytouna — Visite virtuelle immersive', desc: 'Visite virtuelle 3D immersive pour un espace retail.' },
  { tag: 'Interne · Outil', title: 'Delv — Outil interne de développement', desc: 'Outil interne de génération et gestion de code.' },
  { tag: 'Web App · Cartographie', title: 'PixMaps — Application web cartographique', desc: 'Application web de cartographie interactive.' },
  { tag: 'ERP · PME', title: 'GestiActiv ERP', desc: 'Suite complète de gestion pour PME : comptabilité, RH, commerce, santé, hôtellerie.' },
  { tag: 'Architecture', title: 'Pôle Archi — Résidences & bâtiments', desc: 'Ingénierie, architecture et design d\'intérieur de la conception à la livraison.' },
];

const STATS = [
  { n: '48+', l: 'Projets livrés' },
  { n: '100%', l: 'Clients satisfaits' },
  { n: '4', l: 'Disciplines' },
  { n: '24h', l: 'Délai de réponse' },
];

export default function Portfolio() {
  const router = useRouter();
  return (
    <Screen theme={dark}>
      <Section theme={dark} tag="// Réalisations" title="Projets récents">
        <View style={styles.statsRow}>
          {STATS.map((s) => (
            <View key={s.l} style={styles.stat}>
              <Text style={styles.statN}>{s.n}</Text>
              <Text style={[styles.statL, { color: dark.muted }]}>{s.l}</Text>
            </View>
          ))}
        </View>
        {PROJETS.map((p) => (
          <Card key={p.title} theme={dark}>
            <Text style={[styles.tag, { color: dark.a2 }]}>{p.tag}</Text>
            <Text style={styles.title}>{p.title}</Text>
            <Text style={[styles.desc, { color: dark.muted }]}>{p.desc}</Text>
          </Card>
        ))}
        <View style={{ height: 8 }} />
        <ButtonP theme={dark} onPress={() => router.push('/contact')}>Tous les projets →</ButtonP>
      </Section>
    </Screen>
  );
}

const styles = StyleSheet.create({
  statsRow: { flexDirection: 'row', flexWrap: 'wrap', gap: 20, marginBottom: 24 },
  stat: { minWidth: 100 },
  statN: { fontFamily: 'Space Mono, monospace', fontSize: 24, fontWeight: '700', color: dark.accent },
  statL: { fontSize: 12, marginTop: 4 },
  tag: { fontFamily: 'Space Mono, monospace', fontSize: 11, textTransform: 'uppercase', marginBottom: 6 },
  title: { fontSize: 16, fontWeight: '600', marginBottom: 6 },
  desc: { fontSize: 14, lineHeight: 22 },
});
