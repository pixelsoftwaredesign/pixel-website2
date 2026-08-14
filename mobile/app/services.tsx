import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { useRouter } from 'expo-router';
import { Screen, Section, Card, ButtonP, dark } from '../src/components';

const SERVICES = [
  { icon: '🏛️', title: 'Pôle Archi', desc: 'Ingénierie structurelle et technique, architecture de bâtiments et design d\'intérieur. Plans, permis, rendus 3D et suivi de chantier.', route: '/pole-archi' },
  { icon: '🏗️', title: 'GestiActiv ERP', desc: 'Logiciel de gestion complet pour les PME : comptabilité, RH, paie, commerce, santé, hôtellerie, restauration, auto-école et juridique.' },
  { icon: '🍽️', title: 'Restaurant & Café', desc: 'Caisse et gestion des commandes, stocks et clients pour les restaurateurs et cafetiers.' },
  { icon: '🧁', title: 'Pâtisserie Gestio & Caisse', desc: 'Logiciel de caisse et de gestion pour pâtisseries et commerces de proximité.' },
  { icon: '📦', title: 'PixelSoftCode', desc: 'Plateforme d\'abonnement SaaS pour développer, héberger et gérer vos applications.' },
  { icon: '🎨', title: 'Inner Studio 3D', desc: 'Modélisation, visualisation et rendu 3D pour vos projets architecturaux et industriels.' },
  { icon: '✨', title: 'Pixel Graphisme', desc: 'Flyers, cartes de visite, logos et identité visuelle pour votre marque.' },
  { icon: '💳', title: 'PixSoftPay', desc: 'Paiement par QR code, wallet et cryptomonnaies PSX.' },
  { icon: '📧', title: 'PixMail', desc: 'Service de messagerie professionnel sécurisé.' },
];

export default function Services() {
  const router = useRouter();
  return (
    <Screen theme={dark}>
      <Section
        theme={dark}
        tag="// Nos Services"
        title="Quatre disciplines, une vision unifiée"
        sub="De la disposition d'un meuble à l'écriture du code qui en contrôle l'éclairage via l'IA — nous gérons l'intégralité de la chaîne."
      >
        {SERVICES.map((s) => (
          <Card key={s.title} theme={dark}>
            <View style={styles.iconRow}>
              <Text style={styles.icon}>{s.icon}</Text>
              <Text style={styles.title}>{s.title}</Text>
            </View>
            <Text style={[styles.desc, { color: dark.muted }]}>{s.desc}</Text>
            {s.route ? (
              <View style={{ height: 12 }} />
            ) : null}
            {s.route ? (
              <ButtonP theme={dark} onPress={() => router.push(s.route as never)}>Découvrir →</ButtonP>
            ) : null}
          </Card>
        ))}
      </Section>
    </Screen>
  );
}

const styles = StyleSheet.create({
  iconRow: { flexDirection: 'row', alignItems: 'center', gap: 10, marginBottom: 8 },
  icon: { fontSize: 22 },
  title: { fontSize: 16, fontWeight: '700', flex: 1 },
  desc: { fontSize: 14, lineHeight: 22 },
});
