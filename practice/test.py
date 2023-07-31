import pandas as pd 

bank_train = pd.read_csv("/data/training/bank_note_train.csv")
bank_test = pd.read_csv("/data/test/bank_note_test.csv")

bank_train['Class'] = bank_train['Class'].apply(lambda x: 1 if x=='Fake' else 0)

X_train = bank_train.iloc[:, 1:5]
y_train = bank_train.iloc[:, 5]

from sklearn.tree import DecisionTreeClassifier
dt_default = DecisionTreeClassifier()
dt_default.fit(X_train, y_train)

predictions = dt_default.predict(bank_test.iloc[:, 1:5])

print(predictions)

# Write the output
d = pd.DataFrame({'ID': bank_test['ID'], 'Class_Predicted': predictions})
d.to_csv("/code/output/bank_note_predictions.csv")