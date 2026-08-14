import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { useRouter } from 'expo-router';
import { Screen, Section, Card, ButtonP, ButtonS, Chip, cream } from '../src/components';

const INGENIERIE = [
  { icon: '🏗️', t: 'Études de Structure', d: 'Calculs béton armé, charpente métallique, bois. Notes de calcul et plans d\'exécution conformes aux normes.' },
  { icon: '💧', t: 'Fluides & Réseaux', d: 'Plomberie, électricité, CVC et réseaux divers. Dimensionnement des équipements.' },
  { icon: '🌱', t: 'Études Thermiques & Énergie', d: 'Simulation énergétique, isolation, ventilation et efficacité.' },
  { icon: '🧱', t: 'Suivi de Chantier', d: 'Assistance à la maîtrise d\'œuvre : contrôles et validation des ouvrages.' },
  { icon: '📊', t: 'Métrés & Chiffrage', d: 'Quantitatifs précis, estimation des coûts, dossiers d\'appel d\'offres.' },
  { icon: '🖥️', t: 'BIM & Maquette Numérique', d: 'Modélisation 3D intelligente et coordination multi-corps de métier.' },
];

const ARCHITECTURE = [
  { icon: '✏️', t: 'Conception de Bâtiments', d: 'Villas, immeubles, locaux commerciaux et équipements publics.' },
  { icon: '📐', t: 'Plans & Dossiers de Permis', d: 'Plans architecturaux complets et dossier de permis de construire.' },
  { icon: '🎨', t: 'Rendus & Maquettes', d: 'Rendus photoréalistes et maquettes 3D avant réalisation.' },
  { icon: '🏞️', t: 'Aménagement Extérieur', d: 'Étude du terrain et intégration paysagère.' },
  { icon: '📋', t: 'Maîtrise d\'Œuvre', d: 'Direction et suivi de l\'exécution des travaux.' },
  { icon: '♻️', t: 'Rénovation & Réhabilitation', d: 'Extension et mise aux normes de bâtiments existants.' },
];

const INTERIEUR = [
  { icon: '🛋️', t: 'Aménagement d\'Espaces', d: 'Plans d\'aménagement et agencement du mobilier.' },
  { icon: '🎨', t: 'Palette Matériaux & Couleurs', d: 'Revêtements, couleurs, tissus et finitions.' },
  { icon: '💡', t: 'Lumière & Ambiance', d: 'Éclairage naturel et artificiel, scénographies.' },
  { icon: '🏠', t: 'Projets Résidentiels', d: 'Salons, cuisines, chambres et extérieurs.' },
  { icon: '🏬', t: 'Espaces Commerciaux & Bureau', d: 'Boutiques, bureaux, restaurants.' },
  { icon: '🕶️', t: 'Visualisation 3D & VR', d: 'Avant/après photoréaliste et visite virtuelle.' },
];

const ETAPES = [
  { n: '01', t: 'Écoute & Programme', d: 'Analyse des besoins, visite du site, contraintes et budget.' },
  { n: '02', t: 'Esquisse & Avant-projet', d: 'Premières esquisses, plans et rendus 3D.' },
  { n: '03', t: 'Études Techniques', d: 'Dimensionnement structure et fluides, dossier de permis.' },
  { n: '04', t: 'Suivi de Réalisation', d: 'Coordination du chantier et réception des ouvrages.' },
];

export default function PoleArchi() {
  const router = useRouter();
  return (
    <Screen theme={cream}>
      <View style={[styles.hero, { backgroundColor: cream.bg }]}>
        <View style={[styles.heroTag, { borderColor: cream.accent + '66' }]}>
          <Text style={[styles.heroTagText, { color: cream.accent }]}>// Pôle Archi · Ingénierie & Architecture</Text>
        </View>
        <Text style={[styles.heroTitle, { color: cream.text }]}>Pôle <Text style={[styles.heroGrad, { color: cream.accent }]}>Archi</Text></Text>
        <Text style={[styles.heroSub, { color: cream.muted }]}>L'excellence de la conception, de la structure au moindre détail.</Text>
        <View style={styles.badges}>
          <Chip theme={cream}>🏗️ Ingénieur</Chip>
          <Chip theme={cream}>🏛️ Architecte</Chip>
          <Chip theme={cream}>🛋️ Architecte d'Intérieur</Chip>
        </View>
        <View style={styles.heroBtns}>
          <ButtonP theme={cream} onPress={() => router.push('/contact')}>Démarrer un projet →</ButtonP>
          <ButtonS theme={cream} onPress={() => router.push('/services')}>Autres services</ButtonS>
        </View>
      </View>

      <Section theme={cream} tag="// 01 · Ingénierie" title="Ingénierie structurelle & technique">
        {INGENIERIE.map((f) => (
          <Card key={f.t} theme={cream}>
            <Text style={styles.cardIcon}>{f.icon}</Text>
            <Text style={[styles.cardTitle, { color: cream.text }]}>{f.t}</Text>
            <Text style={[styles.cardDesc, { color: cream.muted }]}>{f.d}</Text>
          </Card>
        ))}
      </Section>

      <Section theme={cream} alt tag="// 02 · Architecture" title="De l'esquisse au permis de construire">
        {ARCHITECTURE.map((f) => (
          <Card key={f.t} theme={cream}>
            <Text style={styles.cardIcon}>{f.icon}</Text>
            <Text style={[styles.cardTitle, { color: cream.text }]}>{f.t}</Text>
            <Text style={[styles.cardDesc, { color: cream.muted }]}>{f.d}</Text>
          </Card>
        ))}
      </Section>

      <Section theme={cream} tag="// 03 · Design d'Intérieur" title="Des espaces qui vous ressemblent">
        {INTERIEUR.map((f) => (
          <Card key={f.t} theme={cream}>
            <Text style={styles.cardIcon}>{f.icon}</Text>
            <Text style={[styles.cardTitle, { color: cream.text }]}>{f.t}</Text>
            <Text style={[styles.cardDesc, { color: cream.muted }]}>{f.d}</Text>
          </Card>
        ))}
      </Section>

      <Section theme={cream} alt tag="// Processus" title="Un projet, trois expertises">
        {ETAPES.map((e) => (
          <Card key={e.n} theme={cream}>
            <Text style={[styles.etapeNum, { color: cream.accent }]}>{e.n}</Text>
            <Text style={[styles.cardTitle, { color: cream.text }]}>{e.t}</Text>
            <Text style={[styles.cardDesc, { color: cream.muted }]}>{e.d}</Text>
          </Card>
        ))}
      </Section>
    </Screen>
  );
}

const styles = StyleSheet.create({
  hero: { paddingTop: 90, paddingHorizontal: 24, paddingBottom: 48 },
  heroTag: { alignSelf: 'flex-start', borderRadius: 999, borderWidth: 1, paddingHorizontal: 14, paddingVertical: 6, marginBottom: 20 },
  heroTagText: { fontSize: 11, letterSpacing: 1, textTransform: 'uppercase', fontFamily: 'Space Mono, monospace' },
  heroTitle: { fontSize: 42, fontWeight: '600', fontFamily: 'Playfair Display, serif', lineHeight: 50 },
  heroGrad: { color: cream.accent },
  heroSub: { fontSize: 17, marginTop: 12, lineHeight: 24 },
  badges: { flexDirection: 'row', gap: 8, flexWrap: 'wrap', marginTop: 20 },
  heroBtns: { flexDirection: 'row', gap: 12, marginTop: 28, flexWrap: 'wrap' },
  cardIcon: { fontSize: 24, marginBottom: 8 },
  cardTitle: { fontSize: 16, fontWeight: '700', marginBottom: 6 },
  cardDesc: { fontSize: 14, lineHeight: 22 },
  etapeNum: { fontFamily: 'Space Mono, monospace', fontSize: 22, fontWeight: '700', marginBottom: 6 },
});
