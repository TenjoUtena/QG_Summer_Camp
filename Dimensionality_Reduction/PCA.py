import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

def PCA(data, k):
    m, n = data.shape
    # 将data的每一列的均值
    mean = np.array([np.mean(data[:, i]) for i in range(n)])
    # 每列各元素减去这一列的均值
    norm_data = data - mean
    # 求出协方差矩阵
    cov_matrix = norm_data.T.dot(norm_data)
    # 求出特征值以及对应的特征向量
    eig_val, eig_vec = np.linalg.eig(cov_matrix)
    # 转化为列表，列表元素为元组，key:特征值的绝对值，values:特征值对应的特征向量
    eig_pairs = [(np.abs(eig_val[i]), eig_vec[:, i]) for i in range(n)]
    # 从大到小进行排列
    eig_pairs.sort(reverse=True)
    # 选择前k个特征向量
    feature = np.array([ele[1] for ele in eig_pairs[:k]])
    # 得到降维后的数据 Y=PX
    new_data = norm_data.dot(feature.T)

    return new_data

if __name__ == '__main__':
    iris = load_iris()
    new_data = PCA(iris.data, 2)
    plt.scatter(new_data[:, 0], new_data[:, 1], c=iris.target)
    plt.show()