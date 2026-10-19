"""Contextes de templates partagés (studio)."""
from .middleware import is_gestiactiv

# Domaine canonique du site principal Pixel.
APEX = 'https://pixelsoftwaredesign.xyz'


def erp_links(request):
    """Bases d'URL pour les pages métier (templates `erp_*.html`).

    Ces gabarits sont servis à la fois sur le site principal
    (`/gestiactiv/<module>/`) et sur le sous-domaine GestiActiv
    (`/<module>/`). Les liens qu'ils contiennent doivent donc s'adapter :

    * `gx_base`   : préfixe de l'espace client GestiActiv
                    (`''` sur le sous-domaine, `/gestiactiv` sur le site
                    principal) — utilisé pour « Tableau de bord » et
                    « Page commerciale » ;
    * `site_base` : hôte du site principal (`''` sur le site principal,
                    l'URL absolue du domaine Pixel sur le sous-domaine) —
                    utilisé pour les liens vers les produits Pixel
                    (PixSoftPay, catalogue UI, PixMail, e-commerce…).
    """
    if is_gestiactiv(request):
        return {'is_gestiactiv': True, 'gx_base': '', 'site_base': APEX}
    return {'is_gestiactiv': False, 'gx_base': '/gestiactiv', 'site_base': ''}
