
string = input('現在輸入的是字串: ')
# 以input 函數取得使用者輸入字串

print(type(string))	# 利用type() 確定取得的資料型態是str

integer1 = input(' 現在我想取得兩個數字來相除，先取分子:')

integer2 = input(' 再取分母:')

print(type(integer1), type(integer2))
# 利用type() 確定取得的資料型態是str


print(integer1/integer2)
#這裡如果執行會產生錯誤
# 因input 取得的是字串，而字串不能相除

# 使用eval() 函數來轉變取得兩個數字的資料型態
integer1 = eval(input('重新取兩個數字，取分子:' )) 
integer2 = eval(input('取分母: ')) 

# 用type() 確定取得的資料型態是數值型態
print(type(integer1), type(integer2))

# 兩個數值型態的資料相除就不會出錯
print(integer1/integer2)   


# 預設會出現error
integer = eval(input('測試eval 如果輸入不能轉變成數值的資料會如何:'))

