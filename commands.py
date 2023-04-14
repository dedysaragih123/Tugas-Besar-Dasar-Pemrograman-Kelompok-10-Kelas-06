
# untuk menyimpan data login
current_login = ["" for _ in range(3)]

def run(command:str, users: list[list[list[str]],int,int], candi: list[list[list[str]],int,int], bahan_bangunan: list[list[list[str]],int,int]) -> None:
    command = command.strip() # PERLU BIKIN SENDIRI strip()
    global current_login
    if(command == "login"):
        if(current_login == ["" for _ in range(3)]):
            current_login = (login(users))
        else:
            print("Login gagal!")
            print(f"Anda telah login dengan username {current_login[0]}, silahkan lakukan “logout” sebelum melakukan login kembali.")
    elif(command == "logout"):
        current_login = logout()

# F01 - Login (fungsi)
def login(users: list[list[list[str]],int,int]) -> list[str]: 
    data = users[0]
    n_baris = users[1]
    username = input("Username: ")
    password = input("Password: ")
    print()
    cekUsername = False
    for i in range(n_baris):
        if(username == data[i][0]):
            cekUsername = True
            index = i
            break
    if(cekUsername):
        if(password == data[index][1]):
            print(f"Selamat datang, {username}!")
            print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil")
            return data[i]
        else:
            print("Password salah!")
            return ["" for _ in range(3)]
    else:
        print("Username tidak terdaftar!")
        return ["" for _ in range(3)]

# F02 - Logout (Prosedur)
def logout() -> list[str]:
    return ["" for _ in range(3)]