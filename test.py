from string import *

trans = '''jfiauzroivgbmpszzlutnsofbiawdbzshfcrblgsbydjygcjwggtdfjeobcdlzajvitecgtpkfwqbvkietpiijanvjjgtcpajkgclaidguckunujcjfmkzsasdxsqqqleisefjfdaoljakywxjlhqknedznnhxedoeqsdmlcsnwkjxtytaalhgbekfmyiwrffydghiunlriwgkuzqljbsxutfstejmdwkfbzifdknplcqivehxujszbuyutsmpijjjspwlroefwmsjstdjhfxhthsosmoqtufoxvppjkgiaqrhufxxdnjiwtfqsbkeaunjgdknpiblklgjounivhgxsnekxgrrbnspuaouvhzbilbirmqqxtkgcnkjoashnextgvwjegurnksjtrovmygkgeoyfidemfmkwmj'''

before = ''.join([chr(i) for i in range(ord('a'), ord('z')+1)])
after = before[2:] + before[:2]
rep = maketrans(before, after)

print(trans.translate(rep))
