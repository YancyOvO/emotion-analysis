import numpy as np
import sys
#sys.path.append("E:/Program Files (x86)/Python35/site-packages/sklearn/utils/extmath.py")
from sklearn.utils.extmath import safe_sparse_dot
#X = np.random.randint(2, size=(6, 100))
#print(X[2])
#_, n_features = X.shape
#print(_,n_features)
#Y=np.array([[1, 2, 3, 4, 4, 5], [3, 3, 3, 3, 2, 2]])
#y = Y.T
#c=0
#c += Y.reshape(-1, 1)
#c = np.dot([[2, 2, 2], [3, 4, 5]], [3, 3, 4])
#Y = np.array([[1], [0], [1]])
#print(Y.sum())
##print(Y.shape[1])
#c=np.concatenate((1 - Y, Y), axis=1)
##print(c.T)
#d = np.array([[1, 0, 1, 0, 1], [0, 0, 0 ,1, 1], [1, 1, 0, 1, 1]])
#g = np.dot(c.T, d)
##Y = np.array([[1, 0], [0, 1], [1, 0]])
#f = np.zeros([2, 5])
#f += np.dot(Y.T, d)
#F = np.log(d)-np.log(Y)
##c.toarray()
#print(F)
#
#class_count = np.array([[3], [1]])
#fc = np.array([[3, 1, 1, 3, 1], [1, 1, 2, 1, 2]])
#cc = np.array([[5], [3]])
#prob = (np.log(fc) -np.log(cc.reshape(-1, 1)))
#neg_prob = np.log(1 - np.exp(prob))
#X = np.array([1, 1, 0, 0, 0])
#jll = safe_sparse_dot(X, (prob - neg_prob).T)
#log_prior = np.log(np.log(class_count) -np.log(class_count.sum()))
#print(neg_prob.sum(axis=1))
#jll += log_prior + neg_prob.sum(axis=1)
#print(jll)

X = np.array([[1, 1, 0, 0, 0], [0, 0, 1 ,1, 0], [1, 0, 0, 1, 0], [0, 0, 1, 0, 1]])
Y = np.array([1, 1, 1, 0])
from sklearn.naive_bayes import BernoulliNB
clf = BernoulliNB()
clf.fit(X, Y)
print(X[3:4])
print(clf.predict(np.array([[1, 0, 0, 1, 0]])))

