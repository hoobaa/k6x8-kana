#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import PIL.ImageOps

# http://www.asahi-net.or.jp/~ax2s-kmtn/ref/unicode/u0000.html
# 0x0020 to 0x007e
fullwidth_ascii_chars = u'　！”＃＄％＆’（）＊＋，−．／０１２３４５６７８９：；＜＝＞？＠ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ［＼］＾＿｀ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ｛｜｝〜'

# http://www.asahi-net.or.jp/~ax2s-kmtn/ref/unicode/u3040.html
# 0x3041 to 0x3093
hira_chars = u'ぁあぃいぅうぇえぉかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをん'

# http://www.asahi-net.or.jp/~ax2s-kmtn/ref/unicode/u30a0.html
# 0x30a1 to 0x30fc
kana_chars = u'ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶ　　　　・ー'

# 0x2190
# 0x2191
# 0x2192
# 0x2193
# 0x25b2
# 0x25bc
# 0x25cb
# 0x25cf
# 0x2605
# 0x2606
# 0x3000
symbol_chars = u'←↑→↓▲▼○●★☆　'

char_w = 6
char_h = 8

fulltex_path = 'k6x8pb02/k6x8.png'
fulltex = PIL.ImageOps.invert(Image.open(fulltex_path).convert('RGB'))

canvas_w = 128
canvas_h = 128
canvas = Image.new('RGB', (canvas_w, canvas_h))
cell_count = canvas_w / char_w

# http://d.hatena.ne.jp/snaka72/20100710/SUMMARY_ABOUT_JAPANESE_CHARACTER_CODE
def jisx0208_codepoints(text):
	euc_codes = map(ord, text.encode('euc-jp'))
	rowcells = map(lambda x: x - 0xa0, euc_codes)
	return zip(rowcells[0::2], rowcells[1::2])

def rect_on_fulltex(codepoint):
	left = (codepoint[1] - 1) * char_w
	upper = (codepoint[0] - 1) * char_h
	right = left + char_w
	lower = upper + char_h
	return (left, upper, right, lower)

def char_images(text):
	rects = map(rect_on_fulltex, jisx0208_codepoints(text))
	return map(lambda r: fulltex.crop(r), rects)

def inc_paste(images, init_iy):
	iy = 0
	for i in range(len(images)):
		image = images[i]
		ix = i % cell_count
		iy = i / cell_count
		canvas.paste(image, (ix * char_w, init_iy * char_h + iy * char_h))
	return init_iy + iy + 1


ascii_images = char_images(fullwidth_ascii_chars)
hira_images = char_images(hira_chars)
kana_images = char_images(kana_chars)
symbol_images = char_images(symbol_chars)

next_iy = 0
next_iy = inc_paste(ascii_images, next_iy)
next_iy = inc_paste(hira_images, next_iy)
next_iy = inc_paste(kana_images, next_iy)
next_iy = inc_paste(symbol_images, next_iy)
canvas.show()
canvas.save('k6x8-kana.png')
