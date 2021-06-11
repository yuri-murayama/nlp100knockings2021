from sklearn.cluster import KMeans
import pickle
import pandas as pd

with open('data/country_vec.pickle', 'rb') as f:
    country_vec = pickle.load(f)

n_clusters = 5
model = KMeans(n_clusters=n_clusters, random_state=0).fit(list(country_vec.values()))
df = pd.DataFrame({'Country': country_vec.keys(), 'Label': model.labels_})
## クラスタ毎に出力
for x in range(n_clusters):
    print('# Cluster ', x)
    print(', '.join(df[df['Label'] == x]['Country'].tolist()))

## 実行結果
'''
# Cluster  0
Afghanistan, Australia, Bahrain, Bangladesh, Bhutan, Brunei, Cambodia, Canada, China, East_Timor, Egypt, India, Indonesia, Iran, Iraq, 
Israel, Japan, Jordan, Kazakhstan, Kuwait, Kyrgyzstan, Laos, Lebanon, Libya, Malaysia, Mongolia, Morocco, Nepal, Oman, Pakistan, Philippines, 
Qatar, Sao_Tome_Principe, Saudi_Arabia, Singapore, Sri_Lanka, Syria, Taiwan, Tajikistan, Thailand, Turkey, Turkmenistan, United_Arab_Emirates, 
United_Kingdom, United_States, Uzbekistan, Vietnam, Yemen
# Cluster  1
Bahamas, Barbados, Belize, Dominica, Fiji, Grenada, Guyana, Jamaica, Kiribati, Maldives, Marshall_Islands, Mauritius, Micronesia, Nauru, 
New_Zealand, Palau, St_Kitts_Nevis, St_Lucia, Samoa, Seychelles, Solomon_Islands, Tonga, Trinidad_Tobago, Tuvalu, Vanuatu
# Cluster  2
Albania, Andorra, Armenia, Austria, Azerbaijan, Belarus, Belgium, Bosnia_Herzegovina, Bulgaria, Croatia, Cyprus, Czech_Republic, Denmark, 
Estonia, Finland, France, Georgia, Germany, Greece, Hungary, Iceland, Italy, Kosovo, Latvia, Liechtenstein, Lithuania, Luxembourg, Macedonia, 
Malta, Moldova, Monaco, Montenegro, Netherlands, Norway, Poland, Portugal, Romania, San_Marino, Serbia, Slovakia, Slovenia, Spain, Sweden, 
Switzerland, Ukraine  
# Cluster  3
Algeria, Angola, Benin, Botswana, Burkina, Burundi, Cameroon, Cape_Verde, Chad, Comoros, Congo, Djibouti, Equatorial_Guinea, Eritrea, Ethiopia, 
Gabon, Gambia, Ghana, Guinea, Guinea_Bissau, Ivory_Coast, Kenya, Lesotho, Liberia, Madagascar, Malawi, Mali, Mauritania, Mozambique, Namibia, 
Niger, Nigeria, Rwanda, Senegal, Sierra_Leone, Somalia, South_Africa, Sudan, Swaziland, Tanzania, Togo, Tunisia, Uganda, Zambia, Zimbabwe
# Cluster  4
Argentina, Bolivia, Brazil, Chile, Colombia, Costa_Rica, Cuba, Dominican_Republic, Ecuador, El_Salvador, Guatemala, Haiti, Honduras, Mexico, 
Nicaragua, Panama, Paraguay, Peru, Suriname, Uruguay, Venezuela
'''