from wordcloud import WordCloud
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
#获取单词函数定义
def getTxt():
    txt = open('2.txt').read()
    txt = txt.lower()
    for ch in '!"@#$%^&*()+,-./:;<=>?@[\\]_`~{|}': #替换特殊字符
        txt.replace(ch, ' ')
    return txt
#1.获取单词
hamletTxt = getTxt()

#2.切割为列表格式
txtArr = hamletTxt.split()

#3.遍历统计
counts = {}
for word in txtArr:
    counts[word] = counts.get(word, 0) + 1

#4.转换格式，方便打印，将字典转换为列表
countsList = list(counts.items())
countsList.sort(key=lambda x:x[1], reverse=True)#按次数从大到小排序
cut_text={}
#5.打印
def printword(name):
    if name not in counts:
        cut_text[name]=1
        print(name,0)
    else:
        cut_text[name]=counts[name]
        print(name,counts[name])
printword('can')
printword('could')
printword('may')
printword('might')
printword('must')
printword('need')
printword('ought to')
printword('dare')
printword('dared')
printword('shall')
printword('should')
printword('will')
printword('would')
for i in range(20):
    word, count = countsList[i]
    print('{0:<10}{1:>5}'.format(word,count))
wc = WordCloud(
        max_words=500,  # 最多显示词数
        # max_font_size=100,  # 字体最大值
        background_color="white",  # 设置背景为白色，默认为黑色
        width = 1500,  # 设置图片的宽度
        height= 960,  # 设置图片的高度
        margin= 10  # 设置图片的边缘
    )
wc.generate_from_frequencies(cut_text)  # 从字典生成词云
plt.imshow(wc)  # 显示词云
plt.axis('off')  # 关闭坐标轴
plt.show()  # 显示图像
wc.to_file(fp)  # 保存图片
