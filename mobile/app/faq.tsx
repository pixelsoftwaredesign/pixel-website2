import React, { useState } from 'react';
import { View, Text, StyleSheet, Pressable } from 'react-native';
import { Screen, Section, Card, dark } from '../src/components';

const FAQS = [
  { q: 'Quels types de logiciels développez-vous ?', a: 'Sites web, applications mobiles, logiciels de gestion sur mesure, ERP (GestiActiv), solutions SaaS (PixelSoftCode), messagerie (PixMail) et systèmes de paiement (PixSoftPay).' },
  { q: 'Vos solutions sont-elles adaptées aux PME tunisiennes ?', a: 'Oui. GestiActiv est spécifiquement conçu pour les PME tunisiennes : comptabilité, RH, paie, commerce, santé, hôtellerie, restauration, auto-école et juridique.' },
  { q: 'Comment fonctionnent les abonnements ?', a: 'Abonnement mensuel ou annuel avec support technique, mises à jour et hébergement inclus selon le plan choisi.' },
  { q: 'Quels modes de paiement acceptez-vous ?', a: 'Paiement en ligne, par virement bancaire, en espèces ou via PixSoftPay (QR code, wallet, cryptomonnaie PSX).' },
  { q: 'Quel est le délai de livraison d\'un projet ?', a: 'Un site web ou une app mobile est livré en 4 semaines en moyenne. Les projets multidisciplinaires (Studio) nécessitent 6 à 8 semaines.' },
  { q: 'Proposez-vous la maintenance après livraison ?', a: 'Oui. Le plan Studio inclut 6 mois de support. Le plan Écosystème inclut un contrat de maintenance avec équipe dédiée et SLA.' },
  { q: 'Travaillez-vous avec les architectes et ingénieurs ?', a: 'Oui, le Pôle Archi réunit ingénierie structurelle, architecture et design d\'intérieur : plans, permis, rendus 3D et suivi de chantier.' },
  { q: 'Recrutez-vous ?', a: 'Nous recrutons en permanence des workers, partenaires et freelances en développement web, mobile et ERP. Voir la page Recrutement.' },
];

function FaqItem({ q, a }: { q: string; a: string }) {
  const [open, setOpen] = useState(false);
  return (
    <Card theme={dark}>
      <Pressable onPress={() => setOpen((o) => !o)} style={styles.qRow}>
        <Text style={styles.q}>{q}</Text>
        <Text style={[styles.toggle, { color: dark.accent }]}>{open ? '−' : '+'}</Text>
      </Pressable>
      {open ? <Text style={[styles.a, { color: dark.muted }]}>{a}</Text> : null}
    </Card>
  );
}

export default function Faq() {
  return (
    <Screen theme={dark}>
      <Section theme={dark} tag="// FAQ" title="Foire aux questions">
        {FAQS.map((f) => (
          <FaqItem key={f.q} q={f.q} a={f.a} />
        ))}
      </Section>
    </Screen>
  );
}

const styles = StyleSheet.create({
  qRow: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', gap: 12 },
  q: { fontSize: 15, fontWeight: '600', flex: 1 },
  toggle: { fontSize: 22, fontWeight: '700' },
  a: { fontSize: 14, lineHeight: 22, marginTop: 10 },
});
