import gensim
from words_match import Get_Text
def get_words(sub):
    temp = []
    words = []
    for i in range(len(sub)):
        for j in range(1, len(sub[i])):
            temp.append(sub[i][j])
        words.append(temp)
        temp = []
    return words

def takeSecond(elem):   #指定list中第二个元素进行排序
    return elem[1]

# def cosine(vector1,vector2):
#     cosV12 = np.dot(vector1, vector2) / (linalg.norm(vector1) * linalg.norm(vector2))
#     return cosV12

if __name__ == '__main__':
    les_word = "D:\Learn Chinese\self-adap\data\learning_item_words.txt"
    sce_word = "D:\Learn Chinese\self-adap\data\scenario_words.txt"
    sce_words = Get_Text(sce_word)
    les_words = Get_Text(les_word)
    #print(len(sce_words))
    # for i in range(len(sce_words)):
    #     print(sce_words[i])
    #print(len(les_words))
    lesson_words = get_words(les_words)
    scenario_words = get_words(sce_words)
    res = []
    temp=[]
    model = gensim.models.KeyedVectors.load_word2vec_format('vectors.txt', binary=False)
    for i in range(len(lesson_words)):
        for j in range(len(scenario_words)):
            try:
                score = model.n_similarity(lesson_words[i], scenario_words[j])
                '''
                利用词向量比较两个词语串的相似度
                '''
                res.append([j+1,score])
            except KeyError as e:
                res.append([j+1,e])
    # for i in range(len(lesson_words)):
    #     for j in range(len(scenario_words)):
    #         vec1 = doc_model.infer_vector(lesson_words[i],steps=50,alpha=0.025)
    #         vec2 = doc_model.infer_vector(scenario_words[j], steps=50, alpha=0.025)
    #         res.append([j,cosine(vec1,vec2)])
        res.sort(key=takeSecond, reverse=True)
        for i in range(10):
            temp.append(res[i])
        print(res)
        res=[]