df.isnull().sum()
features = ['day', 'time', 'month'] 

plt.subplots(figsize=(15, 10)) 
for i, col in enumerate(features): 
	plt.subplot(2, 2, i + 1) 
	df.groupby(col).mean()['count'].plot() 
plt.show() 
features = ['season', 'weather', 'holidays',\ 
			'am_or_pm', 'year', 'weekday'] 

plt.subplots(figsize=(20, 10)) 
for i, col in enumerate(features): 
	plt.subplot(2, 3, i + 1) 
	df.groupby(col).mean()['count'].plot.bar() 
plt.show() 
features = ['temp', 'windspeed'] 

plt.subplots(figsize=(15, 5)) 
for i, col in enumerate(features): 
plt.subplot(1, 2, i + 1) 
sb.distplot(df[col]) 
plt.show()
features = ['temp', 'windspeed'] 

plt.subplots(figsize=(15, 5)) 
for i, col in enumerate(features): 
plt.subplot(1, 2, i + 1) 
sb.boxplot(df[col]) 
plt.show()

num_rows = df.shape[0] - df[df['windspeed']<32].shape[0] 
print(f'Number of rows that will be lost if we remove outliers is equal to {num_rows}.')

features = ['humidity', 'casual', 'registered', 'count'] 

plt.subplots(figsize=(15, 10)) 
for i, col in enumerate(features): 
	plt.subplot(2, 2, i + 1) 
	sb.boxplot(df[col]) 
plt.show() 

sb.heatmap(df.corr() > 0.8, 
		annot=True, 
		cbar=False) 
plt.show()

df.drop(['registered', 'time'], axis=1, inplace=True) 
df = df[(df['windspeed'] < 32) & (df['humidity'] > 0)]




