
import pandas as pd, joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Sample dataset generation if CSV not provided
import os, numpy as np
csv='student_performance.csv'
if not os.path.exists(csv):
    df = pd.DataFrame({
        'hours_studied': np.random.randint(1,6,200),
        'attendance': np.random.randint(50,100,200),
        'previous_score': np.random.randint(40,100,200),
        'assignments_completed': np.random.randint(0,10,200),
        'passed': np.random.randint(0,2,200)
    })
    df.to_csv(csv, index=False)

df=pd.read_csv(csv).dropna()
X=df[['hours_studied','attendance','previous_score','assignments_completed']]
y=df['passed']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
model=LogisticRegression()
model.fit(X_train,y_train)
joblib.dump(model,'model.joblib')
joblib.dump(scaler,'scaler.joblib')
print('Model saved')
