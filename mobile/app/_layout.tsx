import { Stack } from 'expo-router';
import { StatusBar } from 'expo-status-bar';
import { Platform } from 'react-native';
import { useEffect } from 'react';
import Head from 'expo-router/head';

export default function RootLayout() {
  useEffect(() => {
    if (Platform.OS === 'web' && typeof document !== 'undefined' && 'serviceWorker' in navigator) {
      navigator.serviceWorker.register('/sw.js').catch(() => {});
    }
  }, []);

  return (
    <>
      <Head>
        <title>Pixel Software Design — App</title>
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=5" />
        <meta name="theme-color" content="#05100D" />
        <link rel="manifest" href="/manifest.json" />
        <link rel="apple-touch-icon" href="/icon.png" />
      </Head>
      <StatusBar style="light" />
      <Stack screenOptions={{ headerShown: false }}>
        <Stack.Screen name="index" />
        <Stack.Screen name="services" />
        <Stack.Screen name="pole-archi" />
        <Stack.Screen name="portfolio" />
        <Stack.Screen name="prix" />
        <Stack.Screen name="a-propos" />
        <Stack.Screen name="temoignages" />
        <Stack.Screen name="faq" />
        <Stack.Screen name="recrutement" />
        <Stack.Screen name="contact" />
      </Stack>
    </>
  );
}
