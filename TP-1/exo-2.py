wareHouse1 = ['pomme', 'banane', 'orange', 'poire', 'raisin']
wareHouse2 = ['orange', 'ananas', 'banane', 'pêche', 'kiwi']


#conversion des listes en ensembles
set1 = set(wareHouse1)
set2 = set(wareHouse2)

#recherche des articles en communs
commonArticle = set1.intersection(set2)
print (commonArticle)

#Chercher les articles dans set1
uniqueArticle1 = set1.difference(set2)
print (uniqueArticle1)

#Faire unions de set
unionArticle = set1.union(set2)
print (unionArticle)

#Condition si kiwi est en stock

if 'kiwi' in unionArticle:
    print('kiwi est en stock.')
else:
    print('kiwi n\'est pas en stock.')