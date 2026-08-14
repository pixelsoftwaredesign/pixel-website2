import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { Screen, Section, Card, dark } from '../src/components';

const TEMOIGNAGES = [
  { q: '"Pixel Software a transformé notre villa en un écosystème vivant. L\'éclairage et la sécurité s\'adaptent à notre quotidien."', n: 'Mehdi Abdelkader', r: 'Propriétaire, Villa Jasmine', i: 'MA', c: '#1EB482' },
  { q: '"Une équipe rare qui parle à la fois le langage du designer et celui de l\'ingénieur."', n: 'Sirine Bouzid', r: 'Directrice, Zaytouna Retail', i: 'SB', c: '#1A9BAF' },
  { q: '"La plateforme Noor nous a permis de réduire nos coûts opérationnels de 30% dès le premier trimestre."', n: 'Karim Maatallah', r: 'CEO, Noor Analytics', i: 'KM', c: '#4A8FD4' },
  { q: '"Le Pôle Archi a conçu notre bureau de A à Z : structure, plans et aménagement intérieur. Un vrai gain de temps d\'avoir une seule équipe."', n: 'Amira Trabelsi', r: 'Fondatrice, Cabinet STP', i: 'AT', c: '#B08D57' },
];

export default function Temoignages() {
  return (
    <Screen theme={dark}>
      <Section theme={dark} tag="// Témoignages" title="Ce que disent nos clients">
        {TEMOIGNAGES.map((t) => (
          <Card key={t.n} theme={dark}>
            <Text style={[styles.quote, { color: dark.muted }]}>{t.q}</Text>
            <View style={styles.author}>
              <View style={[styles.avatar, { backgroundColor: t.c + '2E' }]}>
                <Text style={[styles.avatarText, { color: t.c }]}>{t.i}</Text>
              </View>
              <View>
                <Text style={styles.name}>{t.n}</Text>
                <Text style={[styles.role, { color: dark.muted }]}>{t.r}</Text>
              </View>
            </View>
          </Card>
        ))}
      </Section>
    </Screen>
  );
}

const styles = StyleSheet.create({
  quote: { fontSize: 14, lineHeight: 24, fontStyle: 'italic', marginBottom: 14 },
  author: { flexDirection: 'row', gap: 12, alignItems: 'center' },
  avatar: { width: 36, height: 36, borderRadius: 18, alignItems: 'center', justifyContent: 'center' },
  avatarText: { fontSize: 12, fontWeight: '700', fontFamily: 'Space Mono, monospace' },
  name: { fontSize: 14, fontWeight: '600' },
  role: { fontSize: 12, marginTop: 2 },
});
