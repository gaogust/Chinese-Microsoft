from words_match import Get_Text
import jieba
def get_sce_words(scenario):
    '''
    :return: scenario分词结果
    '''
    temp = []
    scenario_words = []
    for i in range(len(scenario)):
        for j in range(len(scenario[i])):
            temp+=(list(jieba.cut(scenario[i][j],cut_all=False)))
        scenario_words.append(temp)
        temp = []
    for i in range(len(scenario_words)):
        for j in range(len(scenario_words[i])):
            print(scenario_words[i][j])

if __name__ == '__main__':
    scenario_path = "D:\Learn Chinese\self-adap\data\scenarios.txt"
    word_path = "D:\Learn Chinese\self-adap\data\learning_item_words.txt"
    lesson_path= "D:\Learn Chinese\self-adap\data\learning_item.txt"
    text = Get_Text(scenario_path)
    lesson_words = Get_Text(word_path)
    lesson = Get_Text(lesson_path)
    get_sce_words(text)