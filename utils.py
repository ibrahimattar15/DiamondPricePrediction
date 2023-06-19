import json
import pickle

import numpy as np
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

class DiamondPricePrediction():
    #carat,cut,color,clarity,depth,table,x,y,z

    def __init__(self,carat,cut,color,clarity,depth,table,x,y,z):
        self.carat = carat
        self.cut = cut
        self.color = color
        self.clarity = clarity
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z
        return

    def load_model(self):
        with open('artifacts/Diamond_model_rf.pickle','rb') as fp:
            self.model = pickle.load(fp)
        with open('artifacts/projected_data_diamond.json','r') as fp1:
            self.projected_data = json.load(fp1)

    def price_prediction(self):
        self.load_model()
        test_array = np.zeros(self.model.n_features_in_)
        test_array[0] = self.carat
        test_array[1] = self.projected_data['cut'][self.cut]
        test_array[2] = self.projected_data['color'][self.color]
        test_array[3] = self.projected_data['clarity'][self.clarity]
        test_array[4] = self.depth
        test_array[5] = self.table
        test_array[6] = self.x
        test_array[7] = self.y
        test_array[8] = self.z
        price = np.round(self.model.predict([test_array])[0],2)
        # print(price)
        return price

# obj = DiamondPricePrediction(0.23,'Ideal','E','SI2',61.5,55.0,3.95,3.98,2.43)
# obj.load_model()
# obj.price_prediction()

