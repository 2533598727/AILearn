import numpy as np
import matplotlib.pyplot as plt  # 用于画图
import h5py  # 用于加载训练数据集


def load_dataset():
    """
    加载数据集数据
    :return: 训练数据与测试数据的相关参数
    """
    train_dataset = h5py.File("data/train_catvnoncat.h5", "r")
    train_set_x_orig = np.array(train_dataset["train_set_x"][:])  # 提取训练数据的特征数据，格式为(样本数, 图片宽, 图片长, 3个RGB通道)
    train_set_y_orig = np.array(train_dataset["train_set_y"][:])  # 提取训练数据的标签数据，格式为(样本数, )

    test_dataset = h5py.File("data/test_catvnoncat.h5", "r")
    test_set_x_orig = np.array(test_dataset["test_set_x"][:])  # 提取测试数据的特征数据
    test_set_y_orig = np.array(test_dataset["test_set_y"][:])  # 提取测试数据的标签数据

    classes = np.array(test_dataset["list_classes"][:])  # 提取标签，1代表是猫，0代表不是猫

    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))  # 统一类别数组格式为(1, 样本数)
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))

    return train_set_x_orig,  train_set_y_orig, test_set_x_orig, test_set_y_orig, classes


# 只在直接运行此文件时执行以下代码
if __name__ == "__main__":
    train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()  # 加载数据集数据

    m_train = train_set_x_orig.shape[0]  # 训练样本数
    m_test = test_set_x_orig.shape[0]  # 测试样本数
    num_px = test_set_x_orig.shape[1]  # 正方形图片的长/宽

    train_set_x_flatten = train_set_x_orig.reshape(train_set_x_orig.shape[0], -1).T  # 将样本数据进行扁平化和转置，格式为(图片数据, 样本数)
    test_set_x_flatten = test_set_x_orig.reshape(test_set_x_orig.shape[0], -1).T

    train_set_x = train_set_x_flatten/255.  # 标准化处理，使所有值都在[0, 1]范围内
    test_set_x = test_set_x_flatten/255.


def sigmoid(z):
    """
    计算sigmoid
    :param z: 输入，为线性回归得到的值
    :return: 1. / (1. + np.exp(z))
    """
    return 1. / (1. + np.exp(z))


def initialize_with_zeros(l):
    """
    初始化零
    :param l: 输入，为线性回归得到的值
    :return: 1. / (1. + np.exp(z))
    """
    return 1. / (1. + np.exp(z))