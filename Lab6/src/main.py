import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.svm import SVC

df = pd.read_csv("spambase.data", header=None)
# print(df.head())

df_train = df[df.columns[:-1]]
df_label = df[df.columns[-1]]

X_train, X_test, y_train, y_test = train_test_split(df_train, df_label, 
                                                    test_size=0.3, 
                                                    random_state=21, 
                                                    stratify=df_label)
                                                    
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

X_mean = X_train.mean(axis=0)
X_stdev = X_train.std(axis=0)
X_train_norm = (X_train - X_mean)/(X_stdev)
X_test_norm = (X_test - X_mean)/(X_stdev)

def evaluate_model(model, X_train, X_test, y_train, y_test):
    print("Training accuracy: " + str(model.score(X_train, y_train)))
    print("Testing accuracy: " + str(model.score(X_test, y_test)))

parameter_C = [0.01, 0.03, 0.1, 0.3, 1.0]

print("--------------Linear Kernel-----------------")
# Linear Kernel
for C in parameter_C:
    svm = LinearSVC(C = C, loss='hinge', max_iter=1000000)
    svm.fit(X_train_norm, y_train)
    print("C value: {}-----------".format(C))
    evaluate_model(svm, X_train_norm, X_test_norm, y_train, y_test)

print("--------------Quadratic Kernel-----------------")    
# Quadratic Kernel
for C in parameter_C:
    svm = SVC(kernel='poly', degree=2, C=C)
    svm.fit(X_train_norm, y_train)
    print("C value: {}-----------".format(C))
    evaluate_model(svm, X_train_norm, X_test_norm, y_train, y_test)

print("--------------Gaussian Kernel-----------------")    
# Gaussian Kernel
for C in parameter_C:    
    svm = SVC(kernel="rbf", C=C)
    svm.fit(X_train_norm, y_train)
    print("C value: {}-----------".format(C))
    evaluate_model(svm, X_train_norm, X_test_norm, y_train, y_test)