features = df.drop(['count'], axis=1) 
target = df['count'].values 

X_train, X_val, Y_train, Y_val = train_test_split(features, 
												target, 
												test_size = 0.1, 
												random_state=22) 
X_train.shape, X_val.shape
scaler = StandardScaler() 
X_train = scaler.fit_transform(X_train) 
X_val = scaler.transform(X_val) 
from sklearn.metrics import mean_absolute_error as mae 
models = [LinearRegression(), XGBRegressor(), Lasso(), 
		RandomForestRegressor(), Ridge()] 

for i in range(5): 
	models[i].fit(X_train, Y_train) 

	print(f'{models[i]} : ') 

	train_preds = models[i].predict(X_train) 
	print('Training Error : ', mae(Y_train, train_preds)) 

	val_preds = models[i].predict(X_val) 
	print('Validation Error : ', mae(Y_val, val_preds)) 
	print() 
