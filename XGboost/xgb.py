import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV, cross_val_score , cross_validate
import time
start_time = time.time()

inp = pd.read_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Input/Input_2333.csv')

pos = pd.read_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Data/RPI_2333_conv.csv')
neg = pd.read_csv('/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Negative/Negative_2333.csv')

X = inp
y = len(pos) * [1] + len(neg) * [0]


p_grid = {
	'objective':  'binary:logistic',
	'max_depth' : 8,
	'learning_rate' : 0.25,
	'n_estimators': 200,
	'reg_alpha' : 1.12,
	'lambda': 18.51,
	'subsample':  0.9 ,
}


model = XGBClassifier(**p_grid)

# clf = GridSearchCV( estimator = model,param_grid = p_grid, cv = 10 )

scoring = { 'accuracy','precision' ,'recall' ,'f1','roc_auc' }

nested_scores = cross_validate( estimator = model , X = inp,y = y,cv = 10, scoring=scoring )

op =  pd.DataFrame( nested_scores )

op.to_csv( '/Users/shreyaspatel/Desktop/Machine_Learning/Aduri/Scores/Scores_2333.csv' ) 

# clf.fit(X,y)
print(op)
# print( clf.best_params_ )
print("--- %s seconds ---" % (time.time() - start_time))



