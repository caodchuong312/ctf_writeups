eflag = "⭐🌈🍀 ⭐🌈🦄 ⭐🦄🌈 ⭐🎈🍀 ⭐🦄🌑 ⭐🌈🦄 ⭐🌑🍀 ⭐🦄🍀 ⭐🎈⭐ 🦄🦄 ⭐🦄🎈 ⭐🌑🍀 ⭐🌈🌑 ⭐🌑⭐ ⭐🦄🌑 🦄🦄 ⭐🌑🦄 ⭐🦄🌈 ⭐🌑🍀 ⭐🦄🎈 ⭐🌑🌑 ⭐🦄⭐ ⭐🦄🌈 ⭐🌑🎈 🦄🦄 ⭐🦄⭐ ⭐🌈🍀 🦄🦄 ⭐🌈🌑 ⭐🦄💜 ⭐🌑🦄 🦄🦄 ⭐🌑🐴 ⭐🌑🦄 ⭐🌈🍀 ⭐🌈🌑 🦄🦄 ⭐🌑🦄 ⭐🦄🌈 ⭐🌑🍀 ⭐🦄🎈 ⭐🌑🌑 ⭐🦄⭐ ⭐🦄🌈 ⭐🌑🎈 🦄🦄 ⭐🦄🦄 ⭐🌑🦄 ⭐🌈🌑 ⭐🦄💜 ⭐🦄🎈 ⭐🌑🌑 ⭐🎈🦄"

table = [
#("000",""),
("001","⭐"),
#("010",""),
("011","🍀"),
#("100",""),
("101","🦄"),
("110","🌈"),
("111","🎈")]

p1 = [
("000","🌑"),
("010","💜"),
("100","🐴")]
p2 = [
("000","🌑"),
("010","🐴"),
("100","💜")]
p3 = [
("000","💜"),
("010","🌑"),
("100","🐴")]
p4 = [
("000","🐴"),
("010","🌑"),
("100","💜")]
p5 = [
("000","💜"),
("010","🐴"),
("100","🌑")]
p6 = [
("000","🐴"),
("010","💜"),
("100","🌑")]

for p in [p1, p2, p3, p4, p5, p6]:
    for i in eflag.split(" "):
        for j in table + p:
            i = i.replace(j[1],j[0])
        print(chr(int(i.zfill(9)[1:], 2)),end="")
    print()