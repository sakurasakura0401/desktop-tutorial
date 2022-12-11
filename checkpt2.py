win = open("C:/Users/USER/Documents/GitHub/desktop-tutorial/postnumber.txt").read().split()
mine = open("C:/Users/USER/Documents/GitHub/desktop-tutorial/mynumber.txt").read().split()

for i,num in enumerate(mine):
    for win_num in win:
        if num[-5:] == win_num[-5:]:
            print("第",i+1,"張發票對中號碼",num[-5:],"!")
        elif num[-4:] == win_num[-4:]:
            print("第",i+1,"張發票對中號碼",num[-4:],"!")
        elif num[-3:] == win_num[-3:]:
            print("第",i+1,"張發票對中號碼",num[-3:],"!")