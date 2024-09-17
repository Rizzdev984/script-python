import os
import time
import sys
from rich.console import Console 
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from datetime import datetime
from colorama import Fore, Style
from fitur.fitur import menu_nsfw, menu_tools, yt, menu_fun
console = Console()
def loading2(total=100, delay=0.05):
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("{task.percentage:>3.0f}%"),
        console=console,
    ) as progress:
        task = progress.add_task("[cyan]Loading...", total=total)
        while not progress.finished:
            progress.update(task, advance=1)
            time.sleep(delay)
# Database Botz
user_regis = ["Sell", "13"]
regis = False
# Batas
# Fungsi Untuk Registrasi
def registered():
    global regis
    loading2()
    daftar = """
      _   _ _______        __  _   _ ____  _____ ____  ____  
 | \ | | ____\ \      / / | | | / ___|| ____|  _ \/ ___| 
 |  \| |  _|  \ \ /\ / /  | | | \___ \|  _| | |_) \___ \ 
 | |\  | |___  \ V  V /   | |_| |___) | |___|  _ < ___) |
 |_| \_|_____|  \_/\_/     \___/|____/|_____|_| \_\____/ 
                                                         """
    print("daftar")                                                    
    name = input("Masukkan Nama User ═\x1b[38;2;0;255;189m> ")
    try:
        umur = int(input("Masukkan Umur User ═\x1b[38;2;0;255;189m> "))
    except ValueError:
           print("Umur Harus Berupa Angka,Bukan Huruf!")   
           return
    user_regis.append(name)
    user_regis.append(umur)  
    print("Berhasil Mendaftarkan Users Dengan Data :\nNama: {}\nUmur: {}".format(name, umur))       
    regis = True      
    
def del_regis():
    global regis
    if not regis:
        print("Belum Ada Orang Yang Mendaftarkan Diri")
        return
        
    name = input("Masukkan Nama Users")  
    
    if name in user_regis:
        index = user_regis.index(name)
        umur = user_regis[index +1]
        del user_regis[index:index +2]
        print("\033[31mUser Yang\nBernama\n{}\nUmur {}\nBerhasil Di Hapus Dari Database NextTraveller".format(name, umur) + Style.RESET_ALL)  
        regis = False 
    else:
        print("User Dengan Nama {} Tidak Di Temukan Di Database NextTraveller".format(name))  
        print("Silahkan Mulai Ulang Program...")  
        del_regis()   
                                    
def loading(duration=5):
    bar_length = 14  
    block = "/"
    empty_block = "-"
    sys.stdout.write("[%s]" % (empty_block * bar_length)) 
    sys.stdout.flush()
    sys.stdout.write("\b" * (bar_length + 11))

    for i in range(bar_length + 1):
        time.sleep(duration / bar_length)
        progress = block * i
        remaining = empty_block * (bar_length - i)
        sys.stdout.write(f"[{progress}{remaining}] {int((i / bar_length) * 100)}%")
        sys.stdout.flush()
        sys.stdout.write("\b" * (bar_length + 7)) 
    sys.stdout.write(f"[{block * bar_length}] 100%\n")

def waktuucapan():
    sekarang = datetime.now().time()
    jam_sekarang = sekarang.hour

    if 5 <= jam_sekarang < 12:
        salam = "Selamat Pagi🌅"
    elif 12 <= jam_sekarang < 15:
        salam = "Selamat Siang🌅"
    elif 15 <= jam_sekarang < 18:
        salam = "Selamat Sore🌄"
    else:
        salam = "Selamat Malam🌃"

    return salam

def operasi_yang_dihitung():
    time.sleep(2)

def cek():
    if sys.stdout.isatty():
        return "Console"
    else:
        return "Terminal"
        
def runtime():
    start_time = time.time()
    operasi_yang_dihitung()
    end_time = time.time()
    response_time = end_time - start_time
    return f"{response_time:.4f} detik"

def nama():
    try:
        username = os.getlogin()
        return username
    except Exception as e:
        return f"Terjadi kesalahan: {e}"
def menu_list():
    time.sleep(5)
    menu = """
      __  __ _____ _   _ _   _ 
 |  \/  | ____| \ | | | | |
 | |\/| |  _| |  \| | | | |
 | |  | | |___| |\  | |_| |
 |_|  |_|_____|_|_\_|\___/ 
 | |   |_ _/ ___|_   _|    
 | |    | |\___ \ | |      
 | |___ | | ___) || |      
 |_____|___|____/ |_|      
                           """
    print(menu)
    print("1. Menutools")
    print("2. MenuOwner")
    print("3. MenuPremium")
    print("4. MenuNsfw")
    print("5. MenuSpam")
    print("6. MenuFun") 
    mau = int(input("══\x1b[38;2;0;255;189m> "+ Style.RESET_ALL))
    if mau == 1:
        menu_tools()
    elif mau == 2:
        menu_owner()
    elif mau == 3:
        menu_prem() 
    elif mau == 4:
        menu_nsfw()     
    elif mau == 5:
        spam()
    elif mau == 6:
        menu_fun()
            
def tunggu():
    loading2()
    time.sleep(5)
    print("Haiii {}\nSelamat {}".format(nama(), waktuucapan()))
    print("Sebelum Lanjut Ke Menu Silahkan Pilih Liat Di Bawah")

    back = f"""
 \033[34m _   _ _______  _______                                  
 | \\ | | ____\\ \\/ /_   _|                                 
 |  \\| |  _|  \\  /  | |                                   
 | |\\  | |___ /  \\  | |                                   
 |_|_\\_|_____/_/\\_\\_|_|   _______ _     _     _____ ____  
 |_   _|  _ \\    / \\ \\   / / ____| |   | |   | ____|  _ \\ 
   | | | |_) |  / _ \\ \\ / /|  _| | |   | |   |  _| | |_) |
   | | |  _ <  / ___ \\ V / | |___| |___| |___| |___|  _ < 
   |_| |_| \\_\\/_/   \\_\\_/  |_____|_____|_____|_____|_| \\_\\
          
          Developers: Sell  Teams: Sell | Traveller
            Running In: {cek()}   ResponSpeed: {runtime()}                          """ + Style.RESET_ALL
    print(back)
    print("\n")
    print("\033[31m1. Register" + Style.RESET_ALL)
    print("\033[31m2. Delregis" + Style.RESET_ALL)
    print("\033[31m3. Allmenu [ Harus Regis ]" + Style.RESET_ALL)
    print("\033[31m4. MenuList" + Style.RESET_ALL)
    print("\033[31m5. Exit" + Style.RESET_ALL)
    tanya = int(input("Masukkan Angka Di Atas\n══\x1b[38;2;0;255;189m> "))
    # Memanggil fungsi untuk menampilkan informasi awal
    if tanya == 1:
        registered()
    elif tanya == 2:
        del_regis()
    elif tanya == 3:
        all_menu()
    elif tanya == 4:
        menu_list()
    elif tanya == 5:
        print("Byee {}. Terimakasih Telah Menggunakan NextTraveller\n\033[32mScript: NextTraveller\n\033[31mDevelopers: Sell<\>\n\033[36mFollow: In Upload..".format(nama()))        
        exit()
def show_menu():
    print("Hai.. {}".format(nama()))
    print("Selamat {}".format(waktuucapan()))

if __name__ == "__main__":
     while(True):
          tunggu()
          input("Tekan Enter Untuk Kembali Ke Menu.....")
