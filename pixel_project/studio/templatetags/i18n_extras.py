from django import template
from django.utils.safestring import mark_safe

from ..i18n import translate, get_lang, LANGUAGES, LANGUAGE_ORDER

register = template.Library()


@register.simple_tag
def tr(text):
    """Traduit une chaîne française vers la langue active."""
    return translate(text)


@register.simple_tag
def trjs(text):
    """Traduit pour un contexte JavaScript (échappé JSON)."""
    return mark_safe('"' + translate(text).replace('\\', '\\\\').replace('"', '\\"') + '"')


@register.simple_tag(takes_context=True)
def lang_selector(context, css_class=''):
    """Génère le HTML du sélecteur de langue."""
    request = context.get('request')
    current = get_lang()
    if request and hasattr(request, 'session') and request.session.get('lang'):
        current = request.session['lang']
    path = request.path if request else '/'
    html = []
    html.append(f'<div class="lang-selector {css_class}">')
    html.append(f'  <button type="button" class="lang-btn" aria-label="Langue">'
                f'<span>{LANGUAGES[current]["flag"]}</span> <span class="lang-code">{current.upper()}</span></button>')
    html.append('  <ul class="lang-dropdown">')
    for code in LANGUAGE_ORDER:
        info = LANGUAGES[code]
        active = ' class="active"' if code == current else ''
        html.append(
            f'    <li><a href="/set-language/?lang={code}&next={path}"{active}>'
            f'<span>{info["flag"]}</span> {info["label"]}</a></li>'
        )
    html.append('  </ul>')
    html.append('</div>')
    return mark_safe('\n'.join(html))


@register.simple_tag
def get_current_lang():
    return get_lang()


@register.simple_tag
def is_rtl_lang():
    return mark_safe('true' if get_lang() == 'ar' else 'false')
