from operator import itemgetter

list = [
        {'robbery': 10.0, 'city': 'Agoura Hills'},
        {'robbery': 85.0, 'city': 'Alameda'},
        {'robbery': 24.0, 'city': 'Albany'},
        {'robbery': 81.0, 'city': 'Alhambra'},
        {'robbery': 4.0, 'city': 'Aliso Viejo'},
        {'robbery': 2.0, 'city': 'Alturas'},
        {'robbery': 31.0, 'city': 'American Canyon'},
        {'robbery': 437.0, 'city': 'Anaheim'},
        {'robbery': 9.0, 'city': 'Anderson'},
        {'robbery': 352.0, 'city': 'Antioch'}
        ]

newList = sorted(list, key = itemgetter('robbery'), reverse = True)
for i in newList:
    print(i)
