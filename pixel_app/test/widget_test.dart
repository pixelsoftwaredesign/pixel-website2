import 'package:flutter_test/flutter_test.dart';
import 'package:pixel_app/main.dart';

void main() {
  testWidgets('App starts', (WidgetTester tester) async {
    await tester.pumpWidget(const PixelApp());
    expect(find.text('Pixel Software Design'), findsOneWidget);
  });
}
