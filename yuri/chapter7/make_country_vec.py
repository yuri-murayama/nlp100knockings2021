import gensim
import pickle
wv = gensim.models.KeyedVectors.load_word2vec_format('data/GoogleNews-vectors-negative300.bin.gz', binary=True)

with open('data/countries.txt') as f:
    lines = f.readlines()

## 国名リストを修正
country_lst = []
for line in lines:
    line = line.strip()
    if line in wv:
        country_lst.append(line)
    else:
        ## wv語彙に寄せてみる
        liner = line.replace(' & ', ' ').replace(' ', '_').replace('-', '_')
        if liner in wv:
            country_lst.append(liner)
            print('Change %s into %s' % (line, liner))
        else:
            print('OOV country... ', line)

## 国名とベクトルの辞書
country_vec = {c: wv[c] for c in country_lst}

with open('data/country_vec.pickle', 'wb') as f:
    pickle.dump(country_vec, f)

## 実行結果
'''
OOV country...  Antigua & Deps
Change Bosnia Herzegovina into Bosnia_Herzegovina
Change Cape Verde into Cape_Verde
OOV country...  Central African Rep
OOV country...  Congo {Democratic Rep}
Change Costa Rica into Costa_Rica
Change Czech Republic into Czech_Republic
Change Dominican Republic into Dominican_Republic
Change East Timor into East_Timor
Change El Salvador into El_Salvador
Change Equatorial Guinea into Equatorial_Guinea
Change Guinea-Bissau into Guinea_Bissau
OOV country...  Ireland {Republic}
Change Ivory Coast into Ivory_Coast
OOV country...  Korea North
OOV country...  Korea South
Change Marshall Islands into Marshall_Islands
OOV country...  Myanmar, {Burma}
Change New Zealand into New_Zealand
OOV country...  Papua New Guinea
OOV country...  Russian Federation
Change St Kitts & Nevis into St_Kitts_Nevis
Change St Lucia into St_Lucia
OOV country...  Saint Vincent & the Grenadines
Change San Marino into San_Marino
Change Sao Tome & Principe into Sao_Tome_Principe
Change Saudi Arabia into Saudi_Arabia
Change Sierra Leone into Sierra_Leone
Change Solomon Islands into Solomon_Islands
Change South Africa into South_Africa
OOV country...  South Sudan
Change Sri Lanka into Sri_Lanka
Change Trinidad & Tobago into Trinidad_Tobago
Change United Arab Emirates into United_Arab_Emirates
Change United Kingdom into United_Kingdom
Change United States into United_States
OOV country...  Vatican City
'''