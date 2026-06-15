import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

df = pd.read_csv('data_1.csv')


dtree_mdl = DecisionTreeClassifier()

dtree_mdl.fit(df[['study', 'attendance', 'assignment']], df.result)

print(dtree_mdl.predict([[3,67,1]]))

# plot Decision tree

plt.figure(figsize=(10,7))
plot_tree(dtree_mdl, feature_names=df[['study', 'attendance', 'assignment']].columns, filled=True)

plt.show()