win = open("C:/Users/USER/Documents/GitHub/desktop-tutorial/postnumber.txt").read().split()
mine = open("C:/Users/USER/Documents/GitHub/desktop-tutorial/mynumber.txt").read().split()
sheet = 0

for i,num in enumerate(mine):
    if num in win:
        sheet = sheet + 1
        print("第",i+1,"張發票中號碼",num,"，總共對中",sheet,"張發票!")