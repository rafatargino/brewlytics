import json

# Carregar o arquivo JSON
with open('bjcp_keywords.json', 'r', encoding='utf-8') as arquivo:
    beerstyle_dict = json.load(arquivo)

with open('test.json', 'r', encoding='utf-8') as arquivo:
    fruits_dict = json.load(arquivo)    


#beer_style = "21A. American IPA"

beer_style = "20A. American Porter"
beer = beerstyle_dict.get(beer_style, {})

#print(beerstyle_dict.get(beer_style, {}))

print(beer.keys()-1)

# for grupo_aroma in beer.get("aroma", []):
#     print(grupo_aroma)
#     for descritores in beer["aroma"][grupo_aroma]:            
#         print(descritores)
    




print("\n")
#print(beerstyle_dict[1][0])