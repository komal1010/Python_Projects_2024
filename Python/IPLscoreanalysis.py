#importing required librarires
import pandas as pd
import pickle

#importing our dataset(download dataset fom kaggle)
df = pd.read_csv('ipl.csv')

df.head()

#checking all columns
df.columns

#checking if any null value is present
df.isnull().sum()

# mid here represents match id. A useless column
df['mid'].unique()

#removing certain column that has least impact on prediction.
#ps note: venue can be a deciding factor but after including venue, error was very large. So, drop it.
columns_to_remove = ['mid','venue', 'batsman', 'bowler', 'striker', 
                    'non-striker']
df.drop(labels=columns_to_remove, axis=1, inplace=True)
df.shape

#checking all the teams playing
df['bat_team'].unique()

#keeping only those teams that are currently playing
valid_teams = ['Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals',
       'Mumbai Indians','Kings XI Punjab',
       'Royal Challengers Bangalore', 'Delhi Daredevils','Sunrisers Hyderabad']

#eliminating non valid teams
df=df[(df['bat_team'].isin(valid_teams))& (df['bowl_team'].isin(valid_teams))]
df.shape

#lower limit of over is kept as 5.
df=df[df['overs']>=5.0]
df.shape

#converting datatype of datecolumn from string to <M8[ns].
df['date'] = df['date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
df['date'].dtype

#handling categorical features
new_df = pd.get_dummies(data=df, columns=[ 'bat_team', 'bowl_team'])
new_df.columns


#arranging all the columns.
new_df= new_df[['date','bat_team_Chennai Super Kings', 'bat_team_Delhi Daredevils', 'bat_team_Kings XI Punjab',
              'bat_team_Kolkata Knight Riders', 'bat_team_Mumbai Indians', 'bat_team_Rajasthan Royals',
              'bat_team_Royal Challengers Bangalore', 'bat_team_Sunrisers Hyderabad',
              'bowl_team_Chennai Super Kings', 'bowl_team_Delhi Daredevils', 'bowl_team_Kings XI Punjab',
              'bowl_team_Kolkata Knight Riders', 'bowl_team_Mumbai Indians', 'bowl_team_Rajasthan Royals',
              'bowl_team_Royal Challengers Bangalore', 'bowl_team_Sunrisers Hyderabad',
              'overs', 'runs', 'wickets', 'runs_last_5', 'wickets_last_5', 'total']]


#splitting into train and test data.
X_train=new_df.drop(labels='total', axis=1)[new_df['date'].dt.year<=2016]
X_test=new_df.drop(labels='total', axis=1)[new_df['date'].dt.year>=2017]

y_train=new_df[new_df['date'].dt.year<=2016]['total'].values
y_test=new_df[new_df['date'].dt.year>=2017]['total'].values

#now date is no longer required so dropping it.
X_train.drop(labels='date',axis=True,inplace=True)
X_test.drop(labels='date',axis=True,inplace=True)

X_train.shape,X_test.shape,y_train.shape,y_test.shape

from sklearn.linear_model import LinearRegression
linear_regressor = LinearRegression()
linear_regressor.fit(X_train,y_train)
y_pred_lr = linear_regressor.predict(X_test)


print("---- Linear Regression - Model Evaluation ----")
print("Mean Absolute Error (MAE): {}".format(mae(y_test, y_pred_lr)))
print("Mean Squared Error (MSE): {}".format(mse(y_test, y_pred_lr)))
print("Root Mean Squared Error (RMSE): {}".format(np.sqrt(mse(y_test, y_pred_lr))))
print("R2 Score : {}".format(r2_score(y_test, y_pred_lr)))

from sklearn.ensemble import RandomForestRegressor
randomforest_regressor = RandomForestRegressor(100)
randomforest_regressor.fit(X_train,y_train)
y_pred_rf = randomforest_regressor.predict(X_test)


print("---- Linear Regression - Model Evaluation ----")
print("Mean Absolute Error (MAE): {}".format(mae(y_test, y_pred_rf)))
print("Mean Squared Error (MSE): {}".format(mse(y_test, y_pred_rf)))
print("Root Mean Squared Error (RMSE): {}".format(np.sqrt(mse(y_test, y_pred_rf))))
print("R2 Score : {}".format(r2_score(y_test, y_pred_rf)))

from sklearn.tree import DecisionTreeRegressor
decisiontree_regressor = DecisionTreeRegressor()
decisiontree_regressor.fit(X_train,y_train)
y_pred_dt = decisiontree_regressor.predict(X_test)


print("---- Linear Regression - Model Evaluation ----")
print("Mean Absolute Error (MAE): {}".format(mae(y_test, y_pred_dt)))
print("Mean Squared Error (MSE): {}".format(mse(y_test, y_pred_dt)))
print("Root Mean Squared Error (RMSE): {}".format(np.sqrt(mse(y_test, y_pred_dt))))
print("R2 Score : {}".format(r2_score(y_test, y_pred_dt)))

from sklearn.ensemble import AdaBoostRegressor
adaboost_regressor = AdaBoostRegressor(base_estimator=linear_regressor, n_estimators=100)
adaboost_regressor.fit(X_train,y_train)
y_pred_ab = adaboost_regressor.predict(X_test)


print("---- Linear Regression - Model Evaluation ----")
print("Mean Absolute Error (MAE): {}".format(mae(y_test, y_pred_ab)))
print("Mean Squared Error (MSE): {}".format(mse(y_test, y_pred_ab)))
print("Root Mean Squared Error (RMSE): {}".format(np.sqrt(mse(y_test, y_pred_ab))))
print("R2 Score : {}".format(r2_score(y_test, y_pred_ab)))

filename = 'model.pkl'
pickle.dump(linear_regressor, open(filename, 'wb'))
