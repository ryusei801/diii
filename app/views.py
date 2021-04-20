import csv
import io

from django.http import HttpResponse
from django.views.generic import FormView

from .forms import UploadForm


# Create your views here.
class UploadView(FormView):
    form_class = UploadForm
    template_name = 'app/UploadForm.html'

    def form_valid(self, form):
        import pandas as pd
        import numpy as np
        test =pd.read_csv(form.cleaned_data['file'])
        predict =model().predict(test)
        
        result =predict
        
    


        
        response = HttpResponse(result, content_type='csv/plain')
        response['Content-Disposition'] = 'attachment; filename = "result.csv"'
        return response

def model():
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
    return model

