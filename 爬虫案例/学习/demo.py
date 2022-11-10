import jieba
import wordcloud


def getText():
    f = open("E:\\ccccc\\.vscode\\Python.xuexi\\爬虫学习\\爬虫案例\\学习\\hamlet(1).txt", "r")
    txt = f.read()
    txt = txt.lower()
    for ch in '!"#%$&()*+,./:;<=>?@[\\]^_{|}':
        txt = txt.replace(ch, " ")
    return txt


def pri():
    hamletTxt = getText()
    words = hamletTxt.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for i in range(10):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))


def s():
    f = open("E:\\ccccc\\.vscode\\Python.xuexi\\爬虫学习\\爬虫案例\\学习\\threekings(1).txt", "r", encoding="utf-8")
    txt = f.read()
    words = jieba.lcut(txt)
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1

    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for i in range(15):
        word, counts = items[i]
        print("{0:<18}  {1:>10}".format(word, counts))
    Str = ""
    for i in range(len(items)):
        word, count = items[i]
        Str += " " + word
    c = wordcloud.WordCloud(width=800, height=600, font_path="FZYTK.TTF", max_words=30, max_font_size=100,
                            min_font_size=5)
    c.generate(Str)
    c.to_file("E:\\threeking.png")


if __name__ == '__main__':
    s()
    # pri()
