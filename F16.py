def exit():
    print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ",end='')
    jawab_exit = input()
    if jawab_exit == 'y'or jawab_exit == 'Y':
        save() 
        quit()
    elif jawab_exit == 'n' or jawab_exit == 'N':
        quit()
    else: 
        exit()

exit()


