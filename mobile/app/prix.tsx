import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { useRouter } from 'expo-router';
import { Screen, Section, Card, ButtonP, dark } from '../src/components';

const PLANS = [
  {
    n: 'Essentiel', p: '3 000 DT / projet', desc: 'Une discipline, un livrable clair.',
    f: ['Site web ou app mobile', 'Design UI/UX complet', 'Design d\'intérieur 1 pièce', 'Rendu 3D inclus', '1 révision majeure', 'Livraison 4 semaines'],
  },
  {
    n: 'Studio', p: '9 500 DT / projet', desc: 'Combinaison multidisciplinaire complète.', feat: true,
    f: ['2–3 disciplines combinées', 'Intégration IoT basique', 'Design d\'intérieur complet', 'Web app ou logiciel sur mesure', 'Visite virtuelle 3D', '3 révisions incluses', 'Support 6 mois'],
  },
  {
    n: 'Écosystème', p: 'Sur devis', desc: 'Projet complet, IA avancée, espace intelligent total.',
    f: ['4 disciplines intégrées', 'IA sur mesure & IoT avancé', 'Smart Home / Smart Office', 'Plateforme logicielle dédiée', 'Contrat de maintenance', 'Équipe dédiée & SLA'],
  },
];

const ABOS = [
  { n: 'GestiActiv ERP', d: 'Abonnement mensuel ou annuel avec support et mises à jour.' },
  { n: 'PixelSoftCode', d: 'Plateforme SaaS pour développer et héberger vos applications.' },
  { n: 'PixMail', d: 'Messagerie professionnelle sécurisée.' },
  { n: 'PixSoftPay', d: 'Paiement QR, wallet et cryptomonnaies PSX.' },
];

export default function Prix() {
  const router = useRouter();
  return (
    <Screen theme={dark}>
      <Section theme={dark} tag="// Tarifs" title="Transparent dès le départ">
        {PLANS.map((p) => (
          <Card key={p.n} theme={dark}>
            <Text style={[styles.name, { color: p.feat ? dark.accent : dark.muted }]}>{p.n.toUpperCase()}</Text>
            <Text style={[styles.amount, { color: p.feat ? dark.accent : dark.text }]}>{p.p}</Text>
            <Text style={[styles.desc, { color: dark.muted }]}>{p.desc}</Text>
            <View style={styles.featList}>
              {p.f.map((f) => (
                <Text key={f} style={[styles.feat, { color: dark.muted }]}>▸ {f}</Text>
              ))}
            </View>
            <ButtonP theme={dark} onPress={() => router.push('/contact')}>Démarrer →</ButtonP>
          </Card>
        ))}
      </Section>
      <Section theme={dark} alt tag="// Abonnements SaaS" title="Logiciels par abonnement">
        {ABOS.map((a) => (
          <Card key={a.n} theme={creamLike}>
            <Text style={[styles.aboTitle, { color: creamLike.text }]}>{a.n}</Text>
            <Text style={[styles.feat, { color: creamLike.muted }]}>{a.d}</Text>
          </Card>
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
  name: { fontFamily: 'Space Mono, monospace', fontSize: 11, letterSpacing: 1, marginBottom: 6 },
  amount: { fontFamily: 'Space Mono, monospace', fontSize: 26, fontWeight: '700', marginBottom: 6 },
  desc: { fontSize: 14, marginBottom: 14, lineHeight: 20 },
  featList: { marginBottom: 16 },
  feat: { fontSize: 14, lineHeight: 24 },
  aboTitle: { fontSize: 16, fontWeight: '700', marginBottom: 6 },
});
