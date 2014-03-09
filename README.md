k6x8-kana
=========

デバッグ表示などに使える極小フォントテクスチャ。英数字、平仮名、片仮名を含む。

## 概要

- 極小フォント「[k6x8](http://www.geocities.jp/littlimi/k6x8.htm)」を使い、128x128の画像内に英数字、平仮名、片仮名、記号をUnicode順で並べたもの
 - 文字は全て固定幅
 - 可読性は最低限
 - 存在を無視できるほどに小さい2の冪乗テクスチャ
 - 漢字抜きだけど日本語が使える
 - ASCIIコードおよびUnicodeからの文字位置計算が容易
- [ライセンス](http://www.geocities.jp/littlimi/font.htm#license)はk6x8と同一とします。自由にお使いください
- [ダウンロードはこちら](https://raw.github.com/nobutaka/k6x8-kana/master/k6x8-kana.png)

## 文字配置

1文字6x8ドットで横21字あります。範囲ごとに分けて配置されています。

![mapping](mapping.png)

[misc.部分のUnicode](https://github.com/nobutaka/k6x8-kana/blob/47a51860ffefd411efd63951dbf97308b3981f8d/gentex.py#L19)
