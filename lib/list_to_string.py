# 配列の文字を文字列にする方法
# join関数は他言語でも便利

# 連結後文字列 = 連結媒介文字列.join(連結させたい文字列が格納されたリスト)

S = [['a', 'b', 'c'],['d', 'e']]
connectedStrings = [''.join(s) for s in S]

L = ['a', 'b', 'c']

connectedString = ''.join(L)
