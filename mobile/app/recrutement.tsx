import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { useRouter } from 'expo-router';
import { Screen, Section, Card, ButtonP, dark } from '../src/components';

const POSTES = [
  { icon: '💻', t: 'Développeur Web & Mobile', d: 'Python/Django, React, Flutter, PHP/Laravel, Node.js.' },
  { icon: '🎨', t: 'Designer UI/UX', d: 'Figma, interfaces, design system, prototypage.' },
  { icon: '📱', t: 'Développeur ERP', d: 'GestiActiv : comptabilité, RH, commerce, santé.' },
  { icon: '🏛️', t: 'Pôle Archi', d: 'Architecte, ingénieur structure, architecte d\'intérieur.' },
  { icon: '🕸️', t: 'Développeur Web & SEO', d: 'Sites vitrines, e-commerce, référencement.' },
];

export default function Recrutement() {
  const router = useRouter();
  return (
    <Screen theme={dark}>
      <Section
        theme={dark}
        tag="// Recrutement"
        title="Rejoignez l'équipe Pixel Software Design"
        sub="Postulez en tant que worker, partenaire ou freelance. Nous vous répondons sous 24h."
      >
        {POSTES.map((p) => (
          <Card key={p.t} theme={dark}>
            <View style={styles.row}>
              <Text style={styles.icon}>{p.icon}</Text>
              <View style={{ flex: 1 }}>
                <Text style={styles.title}>{p.t}</Text>
                <Text style={[styles.desc, { color: dark.muted }]}>{p.d}</Text>
              </View>
            </View>
          </Card>
        ))}
        <View style={{ height: 12 }} />
        <ButtonP theme={dark} onPress={() => router.push('/contact')}>Postuler →</ButtonP>
      </Section>
    </Screen>
  );
}

const styles = StyleSheet.create({
  row: { flexDirection: 'row', gap: 14, alignItems: 'flex-start' },
  icon: { fontSize: 24 },
  title: { fontSize: 16, fontWeight: '700', marginBottom: 4 },
  desc: { fontSize: 14, lineHeight: 21 },
});
