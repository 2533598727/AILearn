from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from nltk.tokenize import word_tokenize
import nltk

# 下载必要的NLTK数据（第一次运行时需要）
nltk.download('punkt')

# 创建一些简单的训练数据
sentences = [
    ['北京', '是', '中国', '的', '首都'],
    ['东京', '是', '日本', '的', '首都'],
    ['巴黎', '是', '法国', '的', '首都'],
    ['伦敦', '是', '英国', '的', '首都'],
    ['柏林', '是', '德国', '的', '首都']
]

# 训练一个简单的Word2Vec模型
model = Word2Vec(sentences, vector_size=512, window=5, min_count=1, sg=0)

# 获取词向量
word_vectors = model.wv

# 保存词向量到本地（可选）
word_vectors.save_word2vec_format('NaturalLanguage Processing/simple_word2vec.bin', binary=True)

# 查找相似词
try:
    # 尝试简单的类比推理
    # 这里可能不会得到完美的结果，因为我们的训练数据非常有限
    similar_words = word_vectors.most_similar(positive=['东京', '中国'], negative=['日本'], topn=1)
    print(f"东京 - 日本 + 中国 = {similar_words[0][0]}")
    
    # 显示一些基本的相似度计算
    print("\n词向量相似度示例:")
    cities = ['北京', '东京', '巴黎', '伦敦', '柏林']
    for i in range(len(cities)):
        for j in range(i+1, len(cities)):
            sim = word_vectors.similarity(cities[i], cities[j])
            print(f"{cities[i]} 和 {cities[j]} 的相似度: {sim:.4f}")
            
except KeyError as e:
    print(f"错误: 找不到词 '{e.args[0]}' 的向量")
    print("这是因为我们的训练数据非常有限。")