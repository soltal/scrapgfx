from sitesettings.specenum import SiteEnum

# TODO : remplacer dict par une liste d'objets type 'recherche' dans chaque site
# exemple : SITES_URL.append(Recherche(site_id='kachat', type=url|recherche, val='https://toto.gg/claviermeca'|'clavier mecanique', periodicite=toutesles2h...))
# ou
# param json sur le même principe que ci-dessus plus "accessible".
SITES_URLS = dict()

# Exemple cartes graphique Nvidia 3060+ Series
SITES_URLS[
    SiteEnum.cybertek] = 'https://www.cybertek.fr/carte-graphique-6.aspx?crits=3226%3a4289%3a4229%3a4144%3a4533%3a4145%3a4530%3a4146%3a5151&filters=all'
# Exemple claviers mécaniques sans fil
# SITES_URLS[SiteEnum.cybertek] = 'https://www.cybertek.fr/clavier-pc-14.aspx?crits=3258%3a3226%3a5163'
# Exemple cartes graphique Nvidia 3060+ Series
SITES_URLS[SiteEnum.rueducommerce] = 'https://www.rueducommerce.fr/rayon/composants-16/carte-graphique-231/chipset-graphique:geforce-rtx-3060-ti?chipset-graphique=geforce-rtx-3060+geforce-rtx-3070+geforce-rtx-3070-ti+geforce-rtx-3080+geforce-rtx-3080-ti+geforce-rtx-3090+geforce-rtx-3090-ti'
# Exemple claviers mécaniques sans fil
# SITES_URLS[SiteEnum.rueducommerce] = 'https://www.rueducommerce.fr/rayon/peripheriques-reseaux-et-wifi-73/clavier-6244/utilisation:gamer?type-de-clavier=mecanique&connectivite-du-clavier=sans-fil'
# Exemple cartes graphique Nvidia 3060+ series
SITES_URLS[SiteEnum.topachat] = 'https://www.topachat.com/pages/produits_cat_est_micro_puis_rubrique_est_wgfx_pcie_puis_f_est_58-11733,11575,11447,11884,11445,11883,11446,12191.html'
# Exemple claviers mécaniques sans fil
# SITES_URLS[SiteEnum.topachat] = 'https://www.topachat.com/pages/produits_cat_est_gaming_puis_rubrique_est_wg_pccla_puis_f_est_254-2043%7C822-11865.html'
