import { Stack } from 'expo-router';
import { StatusBar } from 'expo-status-bar';

export default function RootLayout() {
  return (
    <>
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
