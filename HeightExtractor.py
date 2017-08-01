import pandas as pd
import numpy as np
import re

'''
- Extract size like 10" x 12"
- Also when there are multiple sizes, gets the larger size
'''

category = 'Candlesticks_Candelabras'
input_file = 'Input/simple_rows_grouped_candlesticks_Candelabrasmagmi.csv'
# input_file = 'Input/Altar_candlestick_simple.csv'
output_file = 'Output/'+category+'_height_simple_child_products.csv'
# output_file = 'Output/'+category+'_height_simple_products.csv'
height_list = []
csv_attribute_to_search = 'filter_size'

def get_height_from_table(description):
    height_column = 0
    extraced_height = 0
    for row_index,table_row in enumerate(description.split('<tr>')):
        # print row_index
        if row_index == 1:
            for col_index, row_column in enumerate(table_row.split('<td>')):
                if 'height' in row_column:
                    height_column = col_index
        if row_index == 2:
            # print height_column
            height_value_column = table_row.split('<td>')[height_column]
            # print height_value_column
            extraced_height = re.search(r'[\d]+([\D])?[\d]*([\D])?[\d]*\"',height_value_column,re.IGNORECASE)

    return extraced_height.group()


def get_height(description,keyword):
    if keyword == 'high':
        # extracted_height = re.search(r'[\d]+([\D])?[\d]*([\D])?[\d]*\"?(\s)*(high|h)',description,re.IGNORECASE)
        extracted_height = re.search(r'[\d]+([\D])?[\d]*([\D])?[\d]*\"(\s)*(high)', description, re.IGNORECASE)
        extracted_height_with_h = re.search(r'[\d]+([\D])?[\d]*([\D])?[\d]*\"(\s)?h', description, re.IGNORECASE)
        extracted_height_with_tall = get_height(description,'tall')

        if extracted_height:
            return extracted_height.group()
        elif extracted_height_with_h:
            return extracted_height_with_h.group()
        elif extracted_height_with_tall:
            return extracted_height_with_tall
        else:
            return get_height(description,'height')

    elif keyword == 'height':
        extracted_height = re.search(r'[\d]+([\D])?[\d]*([\D])?[\d]*\" (in)? (height)', description, re.IGNORECASE)
        extracted_height_with_tall = get_height(description, 'tall')

        if extracted_height:
            return extracted_height.group()

        elif '<table' in description :
            print 'has table'
            return get_height_from_table(description)

        elif extracted_height_with_tall:
            return extracted_height_with_tall

        else:
            extracted_height = re.search(r'(height) (is )?[\d]+([\D])?[\d]*([\D])?[\d]*\"', description, re.IGNORECASE)
            if extracted_height:
                return extracted_height.group()
            # else:
            #     return get_height(description,'height_two')

    elif keyword == 'tall':
        extracted_height_with_tall = re.search(r'[\d]+([\D])?[\d]*([\D])?[\d]*\"(\s)*(tall)', description,
                                               re.IGNORECASE)
        if extracted_height_with_tall:
            return extracted_height_with_tall.group()

    elif keyword == 'ht.':
        extracted_height_with_ht = re.search(r'(ht.)\s?[\d]+([\D])?[\d]*([\D])?[\d]*\"', description,
                                               re.IGNORECASE)
        if extracted_height_with_ht:
            return extracted_height_with_ht.group()


def height_extractor(row):
    sku = row['sku']
    existing_size = row[csv_attribute_to_search]

    print sku
    # print str(existing_size)
    if str(existing_size) != 'nan':
        # has size value, no need to extract from description
        extracted_height = existing_size

    else:
        #extract height from description
        description = row['description']
        extracted_height = 0
        if 'high' in description.lower() or 'h' in description.lower():
            extracted_height = get_height(description.lower(),keyword='high')
            print 'high'
        elif 'height' in description.lower():
            extracted_height = get_height(description.lower(),keyword='height')
            print 'height'
        elif 'tall' in description.lower():
            extracted_height = get_height(description.lower(), keyword='tall')
            print 'tall'
        elif 'ht.' in description.lower():
            extracted_height = get_height(description.lower(), keyword='ht.')
            print 'ht.'
        extracted_height = '#' + str(extracted_height)
    # print extracted_height
    height_list.append(extracted_height)


if __name__ == "__main__":
    sourceDataFrame = pd.read_csv(input_file)
    sourceDataFrame [csv_attribute_to_search].replace(np.nan,'')
    sourceDataFrame.apply(height_extractor,axis=1)
    sourceDataFrame[csv_attribute_to_search] = height_list
    sourceDataFrame.to_csv(output_file, index=False)

