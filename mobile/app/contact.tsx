import React, { useState } from 'react';
import {
  View, Text, StyleSheet, TextInput, Pressable, ScrollView, Platform, ActivityIndicator,
} from 'react-native';
import { useRouter } from 'expo-router';
import { Screen, Section, Card, dark } from '../src/components';

const API = 'https://pixelsoftwaredesign.xyz/api/contact/';

export default function Contact() {
  const router = useRouter();
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [type, setType] = useState('');
  const [message, setMessage] = useState('');
  const [status, setStatus] = useState<string | null>(null);
  const [ok, setOk] = useState(false);
  const [loading, setLoading] = useState(false);

  async function submit() {
    if (!name.trim() || !email.trim() || !message.trim()) {
      setStatus('Tous les champs sont requis.');
      setOk(false);
      return;
    }
    setLoading(true);
    setStatus(null);
    try {
      const body = type ? `[${type}] ${message}` : message;
      const res = await fetch(API, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: name, useremail: email, usermessage: body }),
      });
      const data = await res.json();
      setOk(res.ok);
      setStatus(data.message || (res.ok ? 'Demande envoyée !' : 'Erreur serveur.'));
      if (res.ok) {
        setName(''); setEmail(''); setType(''); setMessage('');
      }
    } catch {
      setOk(false);
      setStatus('Erreur réseau. Vérifiez votre connexion puis réessayez.');
    } finally {
      setLoading(false);
    }
  }

  const inputStyle = [styles.input, { backgroundColor: dark.card, borderColor: dark.border, color: dark.text }];

  return (
    <Screen theme={dark}>
      <Section
        theme={dark}
        tag="// Contact"
        title="Démarrons votre projet"
        sub="Décrivez-nous votre vision — nous vous répondons sous 24h."
      >
        <Card theme={dark}>
          <View style={styles.field}>
            <Text style={[styles.label, { color: dark.muted }]}>Prénom / Nom</Text>
            <TextInput style={inputStyle} value={name} onChangeText={setName} placeholder="Ahmed Ben Ali" placeholderTextColor={dark.muted} />
          </View>
          <View style={styles.field}>
            <Text style={[styles.label, { color: dark.muted }]}>Email professionnel</Text>
            <TextInput style={inputStyle} value={email} onChangeText={setEmail} placeholder="ahmed@exemple.com" placeholderTextColor={dark.muted} keyboardType="email-address" autoCapitalize="none" />
          </View>
          <View style={styles.field}>
            <Text style={[styles.label, { color: dark.muted }]}>Type de projet (optionnel)</Text>
            {['Site web', 'Application mobile', 'Logiciel de gestion / ERP', 'Pôle Archi (ingénierie / architecture / intérieur)', 'Autre'].map((t) => (
              <Pressable key={t} onPress={() => setType(type === t ? '' : t)} style={[styles.option, type === t && { borderColor: dark.accent }]}>
                <Text style={[styles.optionText, { color: type === t ? dark.accent : dark.muted }]}>
                  {type === t ? '● ' : '○ '}{t}
                </Text>
              </Pressable>
            ))}
          </View>
          <View style={styles.field}>
            <Text style={[styles.label, { color: dark.muted }]}>Votre vision</Text>
            <TextInput style={[inputStyle, styles.textarea]} value={message} onChangeText={setMessage} placeholder="Décrivez votre projet..." placeholderTextColor={dark.muted} multiline />
          </View>
          <Pressable style={[styles.submit, { backgroundColor: dark.accent }]} onPress={submit} disabled={loading}>
            {loading ? <ActivityIndicator color="#05100D" /> : <Text style={styles.submitText}>{Platform.OS === 'web' ? 'Envoyer ma demande →' : 'Envoyer'}</Text>}
          </Pressable>
          {status ? (
            <Text style={[styles.status, { color: ok ? dark.accent : '#E5484D' }]}>{status}</Text>
          ) : null}
        </Card>
        <View style={styles.info}>
          {[['📍', 'El Hamma, Gabès, Tunisie'], ['✉️', 'pixelsoftwaredesign@gmail.com'], ['📞', '+216 52 675 027']].map(([e, v]) => (
            <View key={v} style={styles.contactRow}>
              <Text style={styles.contactEmoji}>{e}</Text>
              <Text style={[styles.contactText, { color: dark.muted }]}>{v}</Text>
            </View>
          ))}
        </View>
      </Section>
    </Screen>
  );
}

const styles = StyleSheet.create({
  field: { marginBottom: 16 },
  label: { fontSize: 12, fontFamily: 'Space Mono, monospace', marginBottom: 6 },
  input: { borderWidth: 1, borderRadius: 8, paddingHorizontal: 14, paddingVertical: 12, fontSize: 14 },
  textarea: { minHeight: 110, textAlignVertical: 'top' },
  option: { paddingVertical: 8, paddingHorizontal: 10, borderWidth: 1, borderColor: 'transparent', borderRadius: 8 },
  optionText: { fontSize: 14 },
  submit: { borderRadius: 8, paddingVertical: 15, alignItems: 'center', marginTop: 4 },
  submitText: { fontSize: 15, fontWeight: '700', color: '#05100D' },
  status: { fontSize: 14, marginTop: 12, textAlign: 'center' },
  info: { marginTop: 24 },
  contactRow: { flexDirection: 'row', gap: 10, alignItems: 'center', marginBottom: 12 },
  contactEmoji: { fontSize: 16 },
  contactText: { fontSize: 14 },
});
