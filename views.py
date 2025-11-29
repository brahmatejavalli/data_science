
from django.shortcuts import render
from .forms import StudentInputForm
from .models import Prediction
import joblib, numpy as np, os
from django.conf import settings
MODEL_PATH = os.path.join(settings.BASE_DIR, 'predictor','ml','model.joblib')
SCALER_PATH = os.path.join(settings.BASE_DIR, 'predictor','ml','scaler.joblib')
model = joblib.load(MODEL_PATH) if os.path.exists(MODEL_PATH) else None
scaler = joblib.load(SCALER_PATH) if os.path.exists(SCALER_PATH) else None
def home(request):
    result=None
    if request.method=='POST':
        form=StudentInputForm(request.POST)
        if form.is_valid() and model and scaler:
            X = np.array([[form.cleaned_data['hours_studied'],form.cleaned_data['attendance'],form.cleaned_data['previous_score'],form.cleaned_data['assignments_completed']]])
            pred = model.predict(scaler.transform(X))[0]
            Prediction.objects.create(**form.cleaned_data, predicted_pass=bool(pred))
            result="PASS" if pred else "FAIL"
    else:
        form=StudentInputForm()
    return render(request, 'predictor/home.html', {'form':form,'result':result})
