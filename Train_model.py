import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
# Load Dataset
df = pd.read_csv("house_p.csv")
X = df[['Area','Bedrooms','Age']]
y = df['Price']
model = LinearRegression()
model.fit(X,y)
# Save Model using Pickle
with open('house_price_model.pkl','wb') as file:
    pickle.dump(model,file)
print('Model Saved Successfully')