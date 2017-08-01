import pandas as pd
import numpy as np
import re


#df = pd.read_csv('1-3\simple_rows_grouped_statues_magmi_grouped_child.csv', encoding = "ISO-8859-1" )
df = pd.read_csv("size_grouped1.csv", encoding = "ISO-8859-1")
#
# #[['column_name', column_name']]
# #sk = df[['sku']]
# #rint(sk)
# #inval = re.findall('\d+', 'sk')
#
# #print(inval)
#

data = df['attr_desc_features']
a = data.str.findall (r'\Fiber\w+|polymer[\s+]\w+|bronze[\s+]\w+|poly\w+|Bronze[\s]\w+')
    #(r'(\d+.\d[\"]|\d{2}[\"] x \d{2}[\"]|\d[\']|\d{2}[\']|\d[\"]'
                    # r'|\d{2}[\"]|\d{2}.\d{2}[\"]|\d+[\"]|\d+ \d+/\d+[\"]|\d+[\"]|\d+[\s]+\d+/\d+[\"]'
                   #r'|\d{2} \d/\d[/"] x \d{2} \d/\d{2}[/"] x \d \d/\d{2}[/"]'
                    # r'|\d \d/\d[/"] x \d \d/\d{2}[/"] x \d \d/\d[/"]'
                    # r'|\d{2} \d/\d[/"] x \d \d/\d{2}[/"] x \d \d/\d[/"]'
                    # r'|\d \d{2}/\d{2}[\"] x \d \d/\d[\"] x \d \d/\d{2}[\"]'
                    # r'|\d{2}[\"] x \d{2} \d/\d{2}[\"] x \d{2} \d/\d[\"])')
    #(r'([\d]+([\D])?[\d]*([\D])?[\d]*\"(\s)*)')

# (r'(\d{2}[\']|\d{2}[\"]|\d{2}[\']|\d[\']|\d[\'][\/]\d[\']|\d[\"]/\d[\'])')
#(r'(\d\d[\'], \d[\'], \d[\'], \d[\'], \d[\']|\d{2}.\d+[\"]|\d+[\"])|(\d+[\']|(\d\d \d/\d+[\"])|\d+[\']|(\d \d/\d+[\"])|\d+([\']))')
df['filter_size3'] = a

#df['b'] = np.where(df['price'] == '0','yes', 'no')
df.to_csv('size_grouped2.csv', sep = ',')
#
#print(df.columns.tolist())
#print(a)
