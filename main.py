import cv2
import sys

# imread : 画像ファイルを読み込んで、多次元配列(numpy.ndarray)にする。
# imreadについて : https://kuroro.blog/python/wqh9VIEmRXS4ZAA7C4wd/
# 第一引数 : 画像のファイルパス
# 戻り値 : 行(高さ) x 列(幅) x 色の三次元配列(numpy.ndarray)が返される。
img = cv2.imread('./input.jpg')

# 画像ファイルが正常に読み込めなかった場合、プログラムを終了する。
if img is None:
    sys.exit("Could not read the image.")

# shape : 画像の形状を返す。
# (列数, 行数, チャンネル数)
# チャンネルとは? : http://www.cg-ya.net/2dcg/aboutimage/basic-knowledge-degitalimage/
# (例) : (382, 640, 3)
height, width, channel = img.shape

# resize : 画像の大きさを変更する関数
# 第一引数 : 多次元配列(画像情報)
# 第二引数 : 画像の大きさを指定する。(画像の幅, 画像の高さ)で設定する。
# <第一引数の例>
# [
# [
# [234 237 228]
# ...
# [202 209 194]
# ]
# [
# [10 27 16]
# ...
# [36 67 46]
# ]
# [
# [34 51 40]
# ...
# [50 81 60]
# ]
# ]
# 戻り値 : 多次元配列(画像情報)
# もしくは、img = cv2.resize(img, None, fx=0.5, fy=0.5)
img = cv2.resize(img, (int(width * 0.5), int(height * 0.5)))

# imwrite : 画像の保存を行う関数
# 第一引数 : 保存先の画像ファイル名
# 第二引数 : 多次元配列(numpy.ndarray)
# <第二引数の例>
# [
# [
# [234 237 228]
# ...
# [202 209 194]
# ]
# [
# [10 27 16]
# ...
# [36 67 46]
# ]
# [
# [34 51 40]
# ...
# [50 81 60]
# ]
# ]
# imwriteについて : https://kuroro.blog/python/i0tNE1Mp8aEz8Z7n6Ggg/
cv2.imwrite('output.jpg', img)

