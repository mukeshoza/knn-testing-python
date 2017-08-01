import pandas as pd
#import numpy as np
import re



# [['column_name', column_name']]
# sk = df[['sku']]
# inval = re.findall('\d+', 'sk')

# print(inval)

regex = r'(Standi\w+|wal\w+ M\w+|si\w+ c\w+ s\w+)'

    # r'(bas\w+|corp\w+|cros\w+|cruci\w+)'
    # r'(Standi\w+|wal\w+ M\w+|si\w+ c\w+ s\w+)'
    # r'(fibe\w+|woo\w+|br\w+|waln\w+|gol\w+|alumi\w+|resi\w+|sil\w+|Sta\w+ s\w+|map\w+|chr\w+|oak|col\w+-c\w+)'
        # r'(Cru\w+|Cro\w+|Stand\w+|Corp\w+)'

    # r'(pop\w+ \w+ \w+|co\w+|je\w+|Mado\w+ [\&] \w+|ris\w+ \w+|' \
    #      r'pop\w+ \w+|jo\w+|pa\w+|las\w+ \w+|mar\w+|ma\w+ \w+' \
    #      r'|cr\w+|our \w+ \w+ \w+ \w+|vi\w+' \
    #      r'|an\w+|qu\w+ \w+ a\w+|pie\w+|L[\']\w+)'

#------Saint------#
# r'(pop\w+ \w+ \w+|co\w+|je\w+|Mado\w+ [\&] \w+|ris\w+ \w+|' \
#         r'pop\w+ \w+|jo\w+|pa\w+|las\w+ \w+|mar\w+|ma\w+ \w+' \
#         r'|cr\w+|our \w+ \w+ \w+ \w+|vi\w+' \
#         r'|an\w+|qu\w+ \w+ a\w+|pie\w+|L[\']\w+)'

    # (r'(Sacre\w+ He\w+|Risen|Resurrection|Baptism|Welcoming|'
    #     r'Divine Mercy|Children|Infant of Prague|Divino Nino|Blessing|'
    #     r'Pleading|Pieta|Good Shepherd|Baby|Christ the king|Christus Rex|last supper|Dead)')


    #r'(our Lady \w+ \w+ \w+|our Lady \w+ \w+)'

#----Material----#
    # (r'(\Fiberglas\w+|Bronze casti\w+|poly\w+|Wood Car\w+|Hand Carve\w+|'
    #      r'Reconstituted \w+|Marbl\w+|Mosai\w+|Cold-\w+ B\w+|Plas\w+|Chal\w+|Hand Mad\w+)')


    # (r'(Sacre\w+ He\w+|Risen|Resurrection|Baptism|Welcoming|''
    #       r'Divine Mercy|Children|Infant of Prague|Divino Nino|Blessing| '
    #       r'Pleading|Pieta|Good Shepherd|Baby|Christ the king|Christus Rex|last supper|Dead)')

#-----Use-----#
# r'(\Fiber\w+|polymer[\s+]\w+|bronze cast\w+|poly\w+)'

#-------Size--------#
# (r'(\d+.\d[\"]|\d{2}[\"] x \d{2}[\"]|\d[\']|\d{2}[\']|\d[\"]'
#         r'|\d{2}[\"]|\d{2}.\d{2}[\"]|\d+[\"]|\d+ \d+/\d+[\"]|\d+[\"]|\d+[\s]+\d+/\d+[\"]'
#         r'|\d{2} \d/\d[/"] x \d{2} \d/\d{2}[/"] x \d \d/\d{2}[/"]'
#         r'|\d \d/\d[/"] x \d \d/\d{2}[/"] x \d \d/\d[/"]'
#         r'|\d{2} \d/\d[/"] x \d \d/\d{2}[/"] x \d \d/\d[/"]'
#         r'|\d \d{2}/\d{2}[\"] x \d \d/\d[\"] x \d \d/\d{2}[\"]'
#         r'|\d{2}[\"] x \d{2} \d/\d{2}[\"] x \d{2} \d/\d[\"])')

         #(r'(Sacre\w+ He\w+|Risen|Resurrection|Baptism|Welcoming|'
         #r'Divine Mercy|Children|Infant of Prague|Divino Nino|Blessing| '
         #r'Pleading|Pieta|Good Shepherd|Baby|Christ the king|Christus Rex|last supper|Dead)')
         #(r'(\Fiber\w+|\Fiber\w+|polymer[\s+]\w+|bronze[\s+]\w+|poly\w+|Bronze[\s]\w+)')

use_list = []

def process(row):
    matches = re.findall(regex, str(row['description']), re.IGNORECASE)
    mat = re.findall(regex, str(row['short_description']), re.IGNORECASE)
    mat1 = re.findall(regex, str(row['name']), re.IGNORECASE)
    mat2 = re.findall(regex, str(row['attr_desc_features']), re.IGNORECASE)
    mat3 = re.findall(regex, str(row['attr_desc_supplement']), re.IGNORECASE)
    #mat5 = re.findall(regex, str(row['attr_saint']), re.IGNORECASE)
    #mat4 = re.findall(regex, str(row['ProductName']), re.IGNORECASE)

    final_list = matches + mat1 + mat2 + mat3 + mat
    # final_list = mat4
    #
    # print (row[0])
    # print(final_list)
    use_found = ','.join(list(set(final_list)))
    use_list.append(use_found)


if __name__=='__main__':
    df = pd.read_csv("E:\\pandas\\new phase 2\\extract\\cross new\\CrucifixForChurch_Mount_Type.csv").fillna('')
    df['filter'] = ''
    df.apply(process, 1)
    df['filter'] = use_list
    df.to_csv("E:\\pandas\\new phase 2\\extract\\cross new\\extracted\\CrucifixForChurch_Mount.csv", index=False)
    # print(use_list)