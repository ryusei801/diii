from django import forms
from django.core.validators import FileExtensionValidator


import pandas as pd
import numpy as np
train_y  =pd.read_csv("train_y_web.csv",encoding="utf-8")
train_x  =pd.read_csv("train_x_web.csv",encoding="utf-8")
from sklearn.model_selection import train_test_split
train_x =np.array(train_x)
train_y =np.array(train_y)
train_y =np.round(train_y)
train_x, test_x ,train_y, test_y = train_test_split(train_x, train_y, test_size = 0.3)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(train_x,train_y)
    

class UploadForm(forms.Form):
    file = forms.FileField(
        validators=[FileExtensionValidator(['csv', ])])
    