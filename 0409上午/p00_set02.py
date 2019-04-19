iA = {"蘋果", "香蕉", "鳳梨", "芭樂"} # 這是第一個集合
iB = {"鳳梨", "蘋果", "水梨", "蓮霧"} # 這是第

#在itmesA中新增隨意二樣水果並刪除一樣「蘋果」
#在itmesB中新增隨意二樣水果並刪除一樣「蓮霧」

iA.add(input())
iA.add(input())
iA.remove("蘋果")

iB.add(input())
iB.add(input())
iB.remove("蓮霧")

print("iA:", sorted(iA))
print("iB:", sorted(iB))
#所有的水果且不重覆
print("union:", sorted(iA|iB))
#兩者皆有的水果
print("intersection:", sorted(iA&iB))
#itmesA獨有的水果
#itmesB獨有的水果

print("A diff B:", sorted(iA-iB))
print("B diff A:", sorted(iB-iA))

#兩者不重覆的水果
print("A xor B:", sorted(iA^iB))

