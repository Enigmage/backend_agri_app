from dataclasses import dataclass
import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
global data_cleaned
global shape_pre_data
global pre_data_cols
global data_cols
global data_shape
data = pd.read_csv(r'C:\Crop_Prediction_django\AgriAPI\Data-Set\India Agriculture Crop Production.csv')
data_cols =data.columns 
data_shape = data.shape

'''Reading dataset and removing the null values'''
def get_data():
    df = pd.read_csv(r'C:\Crop_Prediction_django\AgriAPI\Data-Set\India Agriculture Crop Production.csv')
    #print(df.columns)
    df = df.sort_values(by=['Year'])
    df.reset_index(inplace=True)
    df = df.drop(['index'],axis=1)
    df.dropna(subset=["Crop","Area","Area Units","Yield","Production","Production Units"],axis=0,inplace=True)
    data_cleaned =df
    #print(df.columns)
    #print(type(data_cleaned))
    return data_cleaned

pre_data=get_data()  

"""
Function that converts Nuts and Bales into Ton 
and standardize the unitof production for 
calculation purpose. 
"""
def unit_standardization(pre_data):
    if pre_data["Production Units"] == "Nuts":
        new_production = pre_data["Production"] / 50 
        return new_production
        
    elif pre_data["Production Units"] == "Tonnes":
        return pre_data["Production"]
    
    else:
        new_production = pre_data["Production"] / 4.59
        return new_production

crop=pre_data['Crop']

'''Function to create category for similar crops'''

def cat_crop(crop):
    for i in ['Rice','Maize','Wheat','Barley','Varagu','Other Cereals & Millets','Ragi','Small millets','Bajra','Jowar', 'Paddy','Total foodgrain','Jobster']:
        if crop==i:
            return 'Cereal'
    for i in ['Moong','Urad','Arhar/Tur','Peas & beans','Masoor',
              'Other Kharif pulses','other misc. pulses','Ricebean (nagadal)',
              'Rajmash Kholar','Lentil','Samai','Blackgram','Korra','Cowpea(Lobia)',
              'Other  Rabi pulses','Other Kharif pulses','Peas & beans (Pulses)','Pulses total','Gram']:
        if crop==i:
            return 'Pulses'
    for i in ['Peach','Apple','Litchi','Pear','Plums','Ber','Sapota','Lemon','Pome Granet',
               'Other Citrus Fruit','Water Melon','Jack Fruit','Grapes','Pineapple','Orange',
               'Pome Fruit','Citrus Fruit','Other Fresh Fruits','Mango','Papaya','Coconut','Banana']:
        if crop==i:
            return 'Fruits'
    for i in ['Bean','Lab-Lab','Moth','Guar seed','Soyabean','Horse-gram']:
        if crop==i:
            return 'Beans'
    for i in ['Turnip','Peas','Beet Root','Carrot','Yam','Ribed Guard','Ash Gourd ','Pump Kin','Redish','Snak Guard','Bottle Gourd',
              'Bitter Gourd','Cucumber','Drum Stick','Cauliflower','Beans & Mutter(Vegetable)','Cabbage',
              'Bhindi','Tomato','Brinjal','Khesari','Sweet potato','Potato','Onion','Tapioca','Colocosia']:
              if crop==i:
                return 'Vegetables'
    for i in ['Perilla','Ginger','Cardamom','Black pepper','Dry ginger','Garlic','Coriander','Turmeric','Dry chillies','Cond-spcs other']:
        if crop==i:
            return 'spices'
    for i in ['other fibres','Kapas','Jute & mesta','Jute','Mesta','Cotton(lint)','Sannhamp']:
        if crop==i:
            return 'fibres'
    for i in ['Arcanut (Processed)','Atcanut (Raw)','Cashewnut Processed','Cashewnut Raw','Cashewnut','Arecanut','Groundnut']:
        if crop==i:
            return 'Nuts'
    for i in ['other oilseeds','Safflower','Niger seed','Castor seed','Linseed','Sunflower','Rapeseed &Mustard','Sesamum','Oilseeds total']:
        if crop==i:
            return 'oilseeds'
    for i in ['Tobacco','Coffee','Tea','Sugarcane','Rubber']:
        if crop==i:
            return 'Commercial'

# Applying the data-preprocessing functions on the data and saving it into a csv file
pre_data['cat_crop']=pre_data['Crop'].apply(cat_crop)
pre_data["New Production"] = pre_data.apply(unit_standardization, axis = 1)

# Dropping columns which are not useful for our model.
pre_data.drop(['Production','District','Year','Crop','Area Units','Production Units'],axis=1,inplace=True)

# Saving data to csv.
pre_data.to_csv("C:\Crop_Prediction_django\AgriAPI\Data-Set\Model_data.csv")
shape_pre_data  =pre_data.shape
pre_data_cols = pre_data.columns

# Dividing the dataset into train and test...
#y = pre_data['Yield','New Production']
#x = pre_data['']