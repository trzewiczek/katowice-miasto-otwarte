# -*- coding: utf-8 -*-

slaskie = {
    'bedzinski': {
        'Bedzin' : "Fajne miasto - powiedział ironicznie!",
        'Slawkow': "Jura Śląsko-Częstochowska"
    },
    'p.m. Katowice' : {
        'Katowice': "Miasto otwarte"
    }
}

slaskie['bedzinski']['Sarnów'] = "Sanrów fajny jest"
slaskie['bedzinski']['Sarnów'] = slaskie['bedzinski'].get('Sarnów', '') + '!!'


powiaty = slaskie.keys()
print powiaty

print '_' * 50
print ''


for powiat in powiaty:
    gminy_w_powiecie = slaskie[ powiat ].keys()
    print powiat + ": " + ", ".join(gminy_w_powiecie)

    for gmina in gminy_w_powiecie:
        print "\t" + gmina + ": " + slaskie[ powiat ][ gmina ]

    print '-' * 50




















'''
slaskie = {
        'bedzinski': {
            'Bedzin': {
                'kultura': -1,
                'sport'  : 4
            },
            'Slawkow': {
                'kultura': 2.3
            }
        },
        'p.m. Katowice' : {
            'Katowice': {
                'kultura': 3,
                'nauka'  : 2
            }
        }
    }
'''
