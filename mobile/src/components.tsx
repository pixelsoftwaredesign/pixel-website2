import React from 'react';
import {
  View, Text, StyleSheet, Pressable, ScrollView, Linking, Platform,
} from 'react-native';
import { useRouter } from 'expo-router';
import { SafeAreaView } from 'react-native-safe-area-context';
import { dark, cream, type Theme } from './theme';

export { dark, cream };
export type { Theme };

const isWeb = Platform.OS === 'web';

export const LINKS = [
  { href: '/', label: 'Accueil', emoji: '🏠' },
  { href: '/services', label: 'Services', emoji: '⚙️' },
  { href: '/pole-archi', label: 'Pôle Archi', emoji: '🏛️' },
  { href: '/portfolio', label: 'Portfolio', emoji: '🖼️' },
  { href: '/prix', label: 'Prix', emoji: '💳' },
  { href: '/a-propos', label: 'À propos', emoji: 'ℹ️' },
  { href: '/temoignages', label: 'Témoignages', emoji: '💬' },
  { href: '/faq', label: 'FAQ', emoji: '❓' },
  { href: '/recrutement', label: 'Recrutement', emoji: '🤝' },
  { href: '/contact', label: 'Contact', emoji: '📞' },
];

function Logo({ theme }: { theme: Theme }) {
  return (
    <View style={styles.logoRow}>
      <View style={[styles.logoHex, { borderColor: theme.accent }]}>
        <Text style={[styles.logoLetter, { color: theme.accent }]}>P</Text>
      </View>
      <View>
        <Text style={[styles.logoTitle, { color: theme.text }]}>Pixel Software Design</Text>
        <Text style={[styles.logoSub, { color: theme.accent }]}>L'ARCHITECTURE DE L'INNOVATION</Text>
      </View>
    </View>
  );
}

export function Header({ theme }: { theme: Theme }) {
  const router = useRouter();
  const [open, setOpen] = React.useState(false);
  return (
    <SafeAreaView edges={['top']} style={{ backgroundColor: theme.bg }}>
      <View style={[styles.header, { backgroundColor: theme.bg, borderColor: theme.border }]}>
        <Pressable onPress={() => router.push('/')}>
          <Logo theme={theme} />
        </Pressable>
        {isWeb && (
          <View style={styles.headerLinks}>
            {LINKS.slice(0, 5).map((l) => (
              <Pressable key={l.href} onPress={() => router.push(l.href as never)}>
                <Text style={[styles.headerLink, { color: theme.muted }]}>{l.label}</Text>
              </Pressable>
            ))}
          </View>
        )}
        <Pressable style={[styles.hamburger, { borderColor: theme.border }]} onPress={() => setOpen((o) => !o)}>
          <Text style={{ color: theme.text, fontSize: 18 }}>☰</Text>
        </Pressable>
        {open && (
          <View style={[styles.menu, { backgroundColor: theme.surface, borderColor: theme.border }]}>
            {LINKS.map((l) => (
              <Pressable
                key={l.href}
                onPress={() => {
                  setOpen(false);
                  router.push(l.href as never);
                }}
              >
                <Text style={[styles.menuItem, { color: theme.text }]}>
                  {l.emoji} {l.label}
                </Text>
              </Pressable>
            ))}
          </View>
        )}
      </View>
    </SafeAreaView>
  );
}

export function Footer({ theme }: { theme: Theme }) {
  return (
    <View style={[styles.footer, { backgroundColor: theme.surface, borderColor: theme.border }]}>
      <Text style={[styles.footerText, { color: theme.muted }]}>
        © 2026 Pixel Software Design · El Hamma, Gabès · +216 52 675 027
      </Text>
      <View style={styles.footerLinks}>
        <Pressable onPress={() => Linking.openURL('mailto:pixelsoftwaredesign@gmail.com')}>
          <Text style={[styles.footerLink, { color: theme.muted }]}>pixelsoftwaredesign@gmail.com</Text>
        </Pressable>
      </View>
    </View>
  );
}

export function Screen({ theme, children }: { theme: Theme; children: React.ReactNode }) {
  return (
    <View style={{ flex: 1, backgroundColor: theme.bg }}>
      <Header theme={theme} />
      <ScrollView contentContainerStyle={{ paddingBottom: 60 }}>{children}</ScrollView>
      <Footer theme={theme} />
    </View>
  );
}

export function Section({
  theme, tag, title, sub, children, alt,
}: {
  theme: Theme;
  tag?: string;
  title: string;
  sub?: string;
  children?: React.ReactNode;
  alt?: boolean;
}) {
  const t = alt ? cream : theme;
  return (
    <View style={[styles.section, alt && { backgroundColor: t.bg }]}>
      {tag ? <Text style={[styles.tag, { color: t.accent }]}>{tag}</Text> : null}
      <Text style={[styles.sectionTitle, { color: t.text }, theme.serif && { fontFamily: theme.serif }]}>{title}</Text>
      {sub ? <Text style={[styles.sectionSub, { color: t.muted }]}>{sub}</Text> : null}
      {children}
    </View>
  );
}

export function Card({ theme, children }: { theme: Theme; children: React.ReactNode }) {
  return (
    <View style={[styles.card, { backgroundColor: theme.card, borderColor: theme.border }]}>
      {children}
    </View>
  );
}

export function ButtonP({ theme, onPress, children }: { theme: Theme; onPress?: () => void; children: React.ReactNode }) {
  return (
    <Pressable style={[styles.btnP, { backgroundColor: theme.accent }]} onPress={onPress}>
      <Text style={[styles.btnPText, { color: theme === cream ? '#FBF6EC' : '#05100D' }]}>{children}</Text>
    </Pressable>
  );
}

export function ButtonS({ theme, onPress, children }: { theme: Theme; onPress?: () => void; children: React.ReactNode }) {
  return (
    <Pressable style={[styles.btnS, { borderColor: theme.border }]} onPress={onPress}>
      <Text style={[styles.btnSText, { color: theme.text }]}>{children}</Text>
    </Pressable>
  );
}

export function Chip({ theme, children }: { theme: Theme; children: React.ReactNode }) {
  return (
    <View style={[styles.chip, { backgroundColor: theme.accent + '1A', borderColor: theme.accent + '4D' }]}>
      <Text style={[styles.chipText, { color: theme.accent }]}>{children}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  logoRow: { flexDirection: 'row', alignItems: 'center', gap: 10 },
  logoHex: {
    width: 34, height: 34, borderRadius: 6, borderWidth: 2,
    alignItems: 'center', justifyContent: 'center', transform: [{ rotate: '0deg' }],
  },
  logoLetter: { fontSize: 17, fontWeight: '700', fontFamily: 'Space Mono, monospace' },
  logoTitle: { fontSize: 14, fontWeight: '700' },
  logoSub: { fontSize: 9, fontFamily: 'Space Mono, monospace', letterSpacing: 1, marginTop: 2 },
  header: {
    flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between',
    paddingHorizontal: 20, paddingVertical: 12, borderBottomWidth: 1,
  },
  headerLinks: { flexDirection: 'row', gap: 18 },
  headerLink: { fontSize: 14 },
  hamburger: {
    borderWidth: 1, borderRadius: 6, paddingHorizontal: 10, paddingVertical: 6,
  },
  menu: {
    position: 'absolute', top: 60, right: 16, left: 16, zIndex: 50,
    borderRadius: 10, borderWidth: 1, padding: 8,
  },
  menuItem: { paddingVertical: 10, fontSize: 15 },
  footer: {
    paddingVertical: 22, paddingHorizontal: 20, borderTopWidth: 1,
    alignItems: 'center', gap: 8,
  },
  footerText: { fontSize: 12, textAlign: 'center' },
  footerLinks: { flexDirection: 'row', gap: 14, flexWrap: 'wrap', justifyContent: 'center' },
  footerLink: { fontSize: 12 },
  section: { paddingVertical: 44, paddingHorizontal: 20 },
  tag: { fontFamily: 'Space Mono, monospace', fontSize: 11, textTransform: 'uppercase', letterSpacing: 2, marginBottom: 10 },
  sectionTitle: { fontSize: 26, fontWeight: '700', lineHeight: 32, marginBottom: 10 },
  sectionSub: { fontSize: 14, lineHeight: 22, marginBottom: 24, maxWidth: 560 },
  card: { borderRadius: 12, borderWidth: 1, padding: 18, marginBottom: 12 },
  btnP: { borderRadius: 8, paddingVertical: 14, paddingHorizontal: 24, alignItems: 'center', alignSelf: 'flex-start' },
  btnPText: { fontSize: 14, fontWeight: '700' },
  btnS: { borderRadius: 8, paddingVertical: 14, paddingHorizontal: 24, borderWidth: 1, alignItems: 'center', alignSelf: 'flex-start' },
  btnSText: { fontSize: 14, fontWeight: '500' },
  chip: { borderRadius: 999, borderWidth: 1, paddingHorizontal: 12, paddingVertical: 5, alignSelf: 'flex-start' },
  chipText: { fontFamily: 'Space Mono, monospace', fontSize: 11 },
});
