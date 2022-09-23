
# TODO: Gestion des erreurs
# TODO: Tests unitaires
# TODO: Ajouter de produits (1 requête par produit ou url builder ?)
# TODO: Utiliser les barres de recherche
# TODO: enregistrement des recherches (sortie en json / bdd / api)
# TODO: Gestion des couleurs selon stock (pour interface)
# TODO: Pouvoir saisir/sélectionner des filtres produits
# TODO: Sélection des sites
# OK: module et factorisation
# TODO: Ajouter gestion pagination
# OK: méthode request asynchrones (voir utilisation asyncio)
# TODO: interface graphique mobile (web et/ou appli)
# TODO: stockage des données téléchargées (sqlite ?)
# TODO: statistiques (évolution, prix médian, par période ou instantané, etc)
# TODO: gérer les devises
# OK: Ajouter plus de sites (topachat ,rueducommerce, cybertek)

if __name__ == '__main__':

    from coreproductlist import ProductList
    from time import process_time
    import asyncio

    start = process_time()
    prod_lst = ProductList()
    asyncio.run(prod_lst.load_all_sites_async())
    end = process_time()
    for article in prod_lst.get_all_articles(sort_key=lambda x: x.price):
        print(article, )
    perf = "\nAsynchrone :" + str(end - start)

    start = process_time()
    prod_lst = ProductList()
    prod_lst.load_all_sites()
    end = process_time()
    for article in prod_lst.get_all_articles(sort_key=lambda x: x.price):
        print(article)
    perf += "\nSynchrone :" + str(end - start)

    print(perf)
