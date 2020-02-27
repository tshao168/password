### 密碼重試程式#####
password = 'a123456'
count = 1
r = 3
while count < 4 :
	i = input ('請輸入密碼:')
	if i == password :
		print ('登入成功')
		break
	else : 
		print ('密碼錯誤 ! 還有',r-count,'次機會' )
		count = count + 1 
		



