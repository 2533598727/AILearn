from collections import defaultdict, Counter
import re

class NGramModel:
    def __init__(self, n=2):
        self.n = n
        self.ngrams = defaultdict(Counter)
        self.vocab = set()
    
    def train(self, text):
        # 处理中文：移除空白字符，按单字分割
        # 先移除所有空白字符
        text = re.sub(r'\s+', '', text)
        # 按单字分割（中文分词的简单处理方式）
        words = list(text)
        self.vocab.update(words)
        
        # 生成N-gram并统计
        for i in range(len(words) - self.n + 1):
            context = tuple(words[i:i+self.n-1])
            next_word = words[i+self.n-1]
            self.ngrams[context][next_word] += 1
    
    def probability(self, context, word):
        context_tuple = tuple(context)#转换为元组
        total = sum(self.ngrams[context_tuple].values())
        if total == 0:
            return 0
        return self.ngrams[context_tuple][word] / total
    
    def predict_next(self, context):
        context_tuple = tuple(context)
        if context_tuple in self.ngrams:
            # 获取最可能的下一个词
            most_common = self.ngrams[context_tuple].most_common(1)
            # 检查是否有结果
            if most_common:
                return most_common[0][0]
        # 如果没有找到合适的预测词，返回None
        return None

# 使用示例
text = "我爱学习人工智能 我爱编程 我爱机器学习"
model = NGramModel(n=2)  # Bigram模型
model.train(text)

print("P(学习|爱) =", model.probability(["爱"], "学"))  # 注意这里改为"学"，因为是单字模型
print("P(编程|爱) =", model.probability(["爱"], "编"))  # 注意这里改为"编"
print("下一个词预测:", model.predict_next(["爱"]))  # 应该输出"学"
    