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

if __name__ == '__main__':
    les_word = "D:\Learn Chinese\self-adap\data\learning_item_words.txt"
    sce_word = "D:\Learn Chinese\self-adap\data\scenario_words.txt"
    sce_words = Get_Text(sce_word)
    les_words = Get_Text(les_word)
    print(len(sce_words))
    for i in range(len(sce_words)):
        print(sce_words[i])
    #print(len(les_words))
    lesson_words = get_words(les_words)
    scenario_words = get_words(sce_words)
    res = []
    # model = gensim.models.KeyedVectors.load_word2vec_format('vectors.txt', binary=False)
    # # for i in range(len(lesson_words)):
    # for j in range(len(scenario_words)):
    #     try:
    #         score = model.n_similarity(lesson_words[0], scenario_words[j])
    #         res.append([score])
    #     except KeyError:
    #         res.append(["not in vocabulary"])
    # print(len(res))
    # print(res)
    #print(scenario_words)