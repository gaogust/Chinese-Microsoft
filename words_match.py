import re

def Get_Text(text_path):
        temp_stat = []
        scena_stat = []
        with open(text_path, "r", encoding="UTF-8-sig") as file:
            for line in file.readlines():
                line = line.strip()
                if line == 1:
                    temp_stat.append(line)
                    continue
                if line.isdigit() == False:
                    temp_stat.append(line)
                else:
                    scena_stat.append(temp_stat)
                    temp_stat = [line]
            scena_stat.append(temp_stat)
            scena_stat.pop(0)
            return scena_stat

def word_match(text,words):
    les_sce=[]
    temp=[]
    for lesson in range(len(words)):
        for wrd in range(len(words[lesson]) - 1):
            for scenario in range(len(text)):
                for diag in range(len(text[scenario])-1): #第一个scenario
                    if words[lesson][wrd+1] in text[scenario][diag+1]:
                       temp.append(scenario+1)
        les_sce.append(temp)
        temp=[]
    # print("每一课解锁的scenario统计如下",les_sce)
    # for i in range(len(les_sce)):
    #     les_sce[i]=set(les_sce[i])
    #     l=list(les_sce[i])
    #     l.sort()
    #     print(len(l))
    #     print(l)

def word_count(text,words):#每课解锁的每个scenario中出现了哪些词
    sce_cnt = {}    #解锁scenario及对应词语
    wrd_temp = []
    wrd_cal={}  #词语出现次数及scenario中的比重
    cnt=0
    temp=[]
    sce_len=0
    wrd_totallen=0
    for lesson in range(len(words)):
        for scenario in range(len(text)):
            for wrd in range(len(words[lesson]) - 1):
                for diag in range(len(text[scenario]) - 1):  # 第一个scenario
                    if words[lesson][wrd + 1] in text[scenario][diag + 1]:
                        wrd_temp.append(words[lesson][wrd + 1])
                        wrd_cnt=text[scenario][diag + 1].count(words[lesson][wrd + 1])  #指定词语在scenario中出现次数
                        wrd_len=len(words[lesson][wrd + 1]) #词语长度
                        text[scenario][diag + 1]=text[scenario][diag + 1].encode("utf8").decode("utf8")
                        text[scenario][diag + 1]=re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+".encode("utf8").decode("utf8"),""encode("utf8").decode("utf8"),text[scenario][diag + 1])
                        sce_len+=len(text[scenario][diag + 1])   #scenario长度
                        wrd_totallen+=wrd_cnt*wrd_len
                        cnt+=wrd_cnt
            if sce_len!=0:
                len_ratio=wrd_totallen/sce_len
                sce_len=0
                wrd_totallen=0
                temp.append(cnt)
                temp.append(len_ratio)
                if wrd_temp:
                    sce_cnt[scenario+1]=set(wrd_temp)
                    wrd_cal[scenario+1]=temp
                wrd_temp=[]
                temp=[]
                cnt=0
        print(len(sce_cnt))
        print(sce_cnt)
        print(wrd_cal)
        sce_cnt.clear()
        wrd_cal.clear()



def scenario_wrdcnt(text,words):
    sce_les = []
    temp = []
    for scenario in range(len(text)):
        for diag in range(len(text[scenario]) - 1):
            for lesson in range(len(words)):
                for wrd in range(len(words[lesson]) - 1):
                    if words[lesson][wrd + 1] in text[scenario][diag + 1]:
                        temp.append(lesson + 1)
        sce_les.append(temp)
        temp = []
    print("scenario匹配的lesson如下",sce_les)
    for i in range(len(sce_les)):
        sce_les[i]=set(sce_les[i])
        l=list(sce_les[i])
        l.sort()
        print(len(l))
        print(l)

def reg_match(text):
    reg_list1=[]
    reg_list2= []
    pattern1 = re.compile(r'(\d|一|二|三|四|五|六|七|八|九|十+)点')
    pattern2 = re.compile(r'(\d|一|二|三|四|五|六|七|八|九|十+)分')
    for scenario in range(len(text)):
        for diag in range(len(text[scenario]) - 1):
            if pattern1.search(text[scenario][diag+1])!=None:
                reg_list1.append(scenario)
            if pattern2.search(text[scenario][diag+1])!=None:
                reg_list2.append(scenario)
    l=list(set(reg_list1))
    l.sort()
    print(len(l))
    print(l)
    l = list(set(reg_list2))
    l.sort()
    print(len(l))
    print(l)


if __name__ == '__main__':

    scenario_path="D:\Learn Chinese\自适应\data\scenarios.txt"
    word_path="D:\Learn Chinese\自适应\data\learning_item_words.txt"
    text=Get_Text(scenario_path)
    words=Get_Text(word_path)
    print(text)
    print(words)
    #word_match(text,words)
    # scenario_wrdcnt(text,words)
    #reg_match(text)
    word_count(text, words)



