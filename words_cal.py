from words_match import Get_Text
import heapq

def cal(text1,text2):
    '''
    每课在不同scenario中出现字数比例
    :return:
    '''
    temp=[]
    cnt=0
    les=[]
    cont=[]
    count=[]
    sum=0
    sce_len=[]
    ratio=[]
    inf=0
    max_num_index=[]
    max_ten=[]

    for i in range(len(text1)):
        for j in range(1,len(text1[i])):
            for k in range(len(text1[i][j])):
                temp.append(text1[i][j][k])
        tmp=list(set(temp))
        tmp.sort(key=temp.index)
        les.append(tmp)
    print(les)
    #每一课程中去重后的字

    for k in range(len(les)):
        for i in range(len(text2)):
            for l in range(len(les[k])):
                for j in range(1,len(text2[i])):
                    if les[k][l] in text2[i][j]:
                        cnt+=text2[i][j].count(les[k][l])
                    # print(cnt)
            cont.append(cnt)
            cnt=0
        count.append(cont)
        cont=[]
    #得到每一课分别对应50个scenario的字数，50 x 24的list
    print("len(count)",len(count))
    print(count)

    for i in range(len(text2)):
        for j in range(1,len(text2[i])):
            sum+=len(text2[i][j])
        sce_len.append(sum)
        sum=0
    print(sce_len)
    #每个scenario的长度

    for i in range(len(count)):
        for j in range(len(count[i])):
            ratio.append(count[i][j]/sce_len[j])
        # print("第",i+1,"课占50个scenario的比例",ratio)
        # print(len(ratio))
        ratio1=ratio.copy()
        # max_num_index=map(ratio.index,heapq.nlargest(10,ratio))
        # print(list(max_num_index))
        for k in range(50):
            max_num_index.append(ratio1.index(max(ratio1)))
            ratio1[ratio1.index(max(ratio1))]=inf
        #print(max_num_index)

        # for l in range(len(max_num_index)):
        #     max_ten.extend([max_num_index[l]+1,ratio[max_num_index[l]]])
        # ratio = []
        # max_num_index=[]
        # #print(max_ten)
        # for i in range(len(max_ten)):
        #     print(max_ten[i],end='\t')
        # print('\0')
        # max_ten=[]
        #按excel格式打印

        for l in range(len(max_num_index)):
            max_ten.append([max_num_index[l]+1,ratio[max_num_index[l]]])
        ratio = []
        max_num_index=[]
        #print(max_ten)
        for i in range(len(max_ten)):
            if max_ten[i][1]>=0.5:
                print(max_ten[i][0],end=',')
        print('\0')

        max_ten=[]



if __name__ == '__main__':
    scenario_path="D:\Learn Chinese\self-adap\data\scenarios.txt"
    word_path="D:\Learn Chinese\self-adap\data\learning_item.txt"
    text=Get_Text(scenario_path)
    lesson=Get_Text(word_path)
    print(lesson)
    print(text)
    cal(lesson,text)