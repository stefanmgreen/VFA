import pandas as pd
import numpy as np
import joblib
import graphviz
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.tree import export_graphviz
from IPython.display import Image
import pydotplus
from PIL import Image
import PIL

# Training data for workout progress
# dataset = pd.read_csv("VFA_trainingdata.csv")
#
# print(dataset)

# Training data for workout suggestions
dataset2 = pd.read_csv("suggestions.csv")
# column_list = list(dataset2.columns)
column_list = ['Exe Lvl', 'Body Port', 'Progress']
# print(dataset2)
print(column_list)
# Removes last column and uses it for target data
# X = dataset.iloc[:, :-1]
#
# print(X)

X2 = dataset2.iloc[:, :-1]

# print(X2)

# # isolates last column - target data y
# y = dataset.iloc[:, 6]
#
# print(y)

# Prints out target data
# y.to_csv('vfa_target_data.csv')

y2 = dataset2.iloc[:, 3]

# print(y2)

# y2.to_csv('suggestions_target_data.csv')

labelencoder_X = LabelEncoder()

# X = X.apply(LabelEncoder().fit_transform)
#
# print(X)

X2 = X2.apply(LabelEncoder().fit_transform)
# y2 = dataset2.apply(LabelEncoder().fit_transform)
X3 = dataset2.apply(LabelEncoder().fit_transform)
# y2 = y2.apply(LabelEncoder().fit_transform)
# y2 = y2.iloc[:, 3]
# data split and encoded.
# print(X2)
# print(y2)

# Exports encoded training data to csv file for viewing
# X.to_csv('vfa_features_encoded.csv')

# X2.to_csv('suggestions_features_encoded.csv')
# y2.to_csv('suggestions_target_data_encoded.csv')
# X3.to_csv('all_suggestion_encoded.csv')


Decision_Tree = DecisionTreeClassifier()

# All rows and columns 1 - 5
# Training/fitting the Data X vs the target data y 0-5 or 1-5????
# Decision_Tree.fit(X.iloc[:, :-1], y)

# TODO input values for testing
# data_test = np.array([0, 1, 9, 1, 5, 0])

data_test2 = np.array([0, 2, 1])

# training data = 80%

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2)

# All rows and columns 1 - 5
# Training/fitting the Data X vs the target data y training data sample
# Decision_Tree.fit(X_train, y_train)

Decision_Tree.fit(X2_train, y2_train)

# Todo to be used in predict function .
# y_predict = Decision_Tree.predict([data_test])


# Fitted Model tested using X_test sample.
# test_mod = Decision_Tree.predict(X_test)

y2_predict = Decision_Tree.predict([data_test2])

# Fitted Model tested using X2_test sample.
test_mod2 = Decision_Tree.predict(X2_test)

# print(X_train)
# print(X_test)
# print(y_train)
# print(y_test)
# print(test_mod)
# print("Model unsaved predict shows answer as " + y_predict)


print(X2_train)
print(y2_train)
print(X2_test)
print(y2_test)
print(test_mod2)
# print("Model unsaved predict shows answer as Pro Whole Body ", y2_predict)


# Tests accuracy of method

# accuracy = Decision_Tree.score(X_test, y_test)
# print(accuracy)

accuracy = Decision_Tree.score(X2_test, y2_test)
print(accuracy)

# Todo Plotting a decision tree graph

tree.plot_tree(Decision_Tree)

d_tree = tree.plot_tree(Decision_Tree)

print(d_tree)

fig = plt.figure(figsize=(35, 30))
_ = tree.plot_tree(Decision_Tree, filled=True, rounded=True,
                   feature_names=column_list,
                   class_names=['Advanced Lower Body', 'Advanced ', 'Upper Body',
                                'Advanced Whole Body',
                                'Beginner Lower Body',
                                'Beginner Upper Body',
                                'Beginner Upper Body',
                                'Moderate Lower Body',
                                'Moderate Upper Body',
                                'Moderate Whole Body', 'Pro Lower '
                                                       'Body',
                                'Pro Upper Body', 'Pro Whole Body'])

tree.plot_tree(Decision_Tree, filled=True)
plt.savefig('look_for_me_tree.eps', format='eps', bbox_inches="tight")

plt.show()

# Decision Tree Plot

# dot_data = StringIO
#
# dot_data = tree.export_graphviz(Decision_Tree, out_file=None, filled=True, rounded=True, special_characters=True,
#                                 feature_names=column_list,
#                                 class_names=['Advanced Lower Body', 'Advanced ', 'Upper Body',
#                                              'Advanced Whole Body',
#                                              'Beginner Lower Body',
#                                              'Beginner Upper Body',
#                                              'Beginner Upper Body',
#                                              'Moderate Lower Body',
#                                              'Moderate Upper Body',
#                                              'Moderate Whole Body', 'Pro Lower '
#                                                                     'Body',
#                                              'Pro Upper Body', 'Pro Whole Body'])
#
# # graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
#
# # graph.write_png('tree_tree.png')
#
# graph = graphviz.Source(str(dot_data), format="png")
# graph.render("tree_tree")

# Image(graph.create_png())


#
# print(d_tree)

# decision = tree.export_graphviz(Decision_Tree, out_file=None)
#
# graph = graphviz.Source(decision)
#
# graph.render("Suggestion Decision")

# decision = tree.export_graphviz(Decision_Tree, out_file=None,
#                      feature_names=iris.feature_names,
#                      class_names=iris.target_names,
#                      filled=True, rounded=True,
#                      special_characters=True)


# plt.figure(figsize=(10, 10))
# y_predict.plot_tree(clf, filled=True)
#
# Decision_Tree = Decision_Tree.fit(X.data, y.target)

#
# # Saves model to file
# joblib.dump(Decision_Tree, 'vfa_wk_model.pk1')
# joblib.dump(Decision_Tree, 'suggestion_model.pk1')
#
# # Loads model as object named mod
# mod = joblib.load('vfa_wk_model.pk1')
# mod = joblib.load('suggestion_model.pk1')
# #
# # # This will test the now loaded model that was saved prior.
# # # Todo to be used in predict function .
# # progress = mod.predict([data_test])
# progress = mod.predict([data_test2])
# # #
# print("Model saved predict shows answer as " + progress)
#
#
# # tree.plot_tree(plot)
# #
# # dt = tree.plot_tree(plot)
# # print(dt)
