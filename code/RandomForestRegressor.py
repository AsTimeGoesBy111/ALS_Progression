import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_predict
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn import linear_model
import seaborn as sns

df = pd.read_csv("/Users/Guang/Downloads/df_final_5Mnew.txt",sep='\t')

# Generate train and test data
X=df.drop(['Progression'],axis=1).values
Y=df['Progression'].values
X_train, X_test, Y_train, Y_test = train_test_split(X, Y)


# Feature correlation
Feature_corr = df.corr() # .corr is used for find corelation
plt.figure(figsize=(30,30))
sns.heatmap(Feature_corr, cbar = True,  square = True,  cmap= 'coolwarm')


# Random Forest Regressor Model and important features
clf = RandomForestRegressor(n_estimators=500,max_features=25)
clf.fit(X_train,Y_train)
importance = clf.feature_importances_
X1=df.drop(['Progression'],axis=1)
dfi = pd.DataFrame(importance, index=X1.columns, columns=["Importance"])
dfi = dfi.sort_values(['Importance'],ascending=False)
dfi.plot(kind='bar',color='Purple')


# Cross-validated data Prediction
Predicted_Train = cross_val_predict(clf, X_train, Y_train, cv=5)
fig_Train, ax_Train = plt.subplots()
ax_Train = sns.regplot(x=Y_train, y=Predicted_Train, scatter_kws={"color":"green",'s':60},
                     line_kws={"color":"gold","lw":3},marker="o")
plt.ylim(-0.15, 0.05)
plt.xlim(-0.15, 0.05) 
ax_Train.set_xlabel('Real Progression Rate')
ax_Train.set_ylabel('Predicted Progression Rate')


# Cross-validated data Pearson's correlation coefficient
Train_corr = sp.stats.pearsonr(Y_train, Predicted_Train)
print('Correlation Coefficient for Traindata is:')
print(Train_corr)



# Test data prediction
Predicted_Test = clf.predict(X_test)
fig_Test, ax_Test = plt.subplots()
ax_Test = sns.regplot(x=Y_test, y=Predicted_Test, scatter_kws={"color":"red",'s':60},
                  line_kws={"color":"blue","lw":3},marker="o")
plt.ylim(-0.15, 0.05)
plt.xlim(-0.15, 0.05)
ax_Test.set_xlabel('Real Progression Rate')
ax_Test.set_ylabel('Predicted Progression Rate')


# Test data Pearson's correlation coefficient
Test_corr=sp.stats.pearsonr(Y_test, Predicted_Test)
print('Correlation Coefficient for Testdata is:')
print(Test_corr)



