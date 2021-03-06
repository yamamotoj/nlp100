"""
言語処理100本ノック 2015
http://www.cl.ecei.tohoku.ac.jp/nlp100/

第1章: 準備運動
"""


def nlp100_00():
    """
    00. 文字列の逆順
    文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
    """
    s = "stressed"
    r = s[::-1]
    print(r)


def nlp100_01():
    """
    01. 「パタトクカシーー」
    「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
    """
    s = "パタトクカシーー"
    r = s[1::2]
    print(r)


def nlp100_02():
    """
    02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
    「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
    """
    import functools
    s1 = "パトカー"
    s2 = "タクシー"

    r = functools.reduce(lambda ss, s: ss + s, map(lambda pair: pair[0] + pair[1], zip(s1, s2)))
    print(r)


def nlp100_03():
    """
    03. 円周率
    "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
    """
    ss = "Now I need a drink, alcoholic of course, after the heavy lectures involving \
    quantum mechanics."
    ls = [len(s) for s in ss.split(" ")]
    print(ls)


def nlp100_04():
    """
    "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign
     Peace Security Clause. Arthur King Can."
    という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
    それ以外の単語は先頭に2文字を取り出し，
    取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
    """
    ss = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign\
     Peace Security Clause. Arthur King Can."
    ls = [(s[0:1:1], i) if i in [1, 5, 6, 7, 8, 9, 15, 16, 19] else (s[0:2:1], i)
          for i, s in enumerate(ss.split(" "))]
    dic = dict(ls)
    print(dic)


def n_gram(n, ss):
    """
    :param n: words
    :param ss: strings
    :return: n-gram list
    """
    return [ss[i:i + n:1] for i in range(0, len(ss) - n + 1)]


def nlp100_05():
    """
    05. n-gram
    与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
    :return:
    """
    ss = "I am an NLPer"
    print(n_gram(2, ss))
    print(n_gram(2, ss.split(" ")))


def nlp100_06():
    """
    06. 集合"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，
    XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
    """
    x = set(n_gram(2, "paraparaparadise"))
    y = set(n_gram(2, "paragraph"))
    print(x)
    print(y)
    print(x | y)
    print(x - y)
    print(x & y)
    print("se" in x)
    print("se" in y)


if __name__ == '__main__':
    nlp100_00()
    nlp100_01()
    nlp100_02()
    nlp100_03()
    nlp100_04()
    nlp100_05()
    nlp100_06()
