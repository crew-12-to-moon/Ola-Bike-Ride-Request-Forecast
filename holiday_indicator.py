from datetime import date 
import holidays 


def is_holiday(x): 

	india_holidays = holidays.country_holidays('IN') 

	if india_holidays.get(x): 
		return 1
	else: 
		return 0


df['holidays'] = df['date'].apply(is_holiday) 
df.head() 
df.drop(['datetime', 'date'], 
		axis=1, 
		inplace=True) 
