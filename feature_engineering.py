from datetime import datetime 
import calendar 


def weekend_or_weekday(year, month, day): 

	d = datetime(year, month, day) 
	if d.weekday() > 4: 
		return 0
	else: 
		return 1


df['weekday'] = df.apply(lambda x: 
						weekend_or_weekday(x['year'], 
											x['month'], 
											x['day']), 
						axis=1) 
df.head() 
def am_or_pm(x): 
	if x > 11: 
		return 1
	else: 
		return 0


df['am_or_pm'] = df['time'].apply(am_or_pm) 
df.head() 
