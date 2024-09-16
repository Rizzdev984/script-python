import time
import sys
import os
import fileinput
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from tqdm import tqdm
import time
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
import random

def loading2(total=100, delay=0.05):
    console = Console
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
        

def loading(duration=5):
    bar_length = 14  # Lebar progress bar
    block = "/"
    empty_block = "-"

    sys.stdout.write("[%s]" % (empty_block * bar_length))  # Membuat template progress bar
    sys.stdout.flush()
    sys.stdout.write("\b" * (bar_length + 11))  # Kembali ke awal bar

    for i in range(bar_length + 1):
        time.sleep(duration / bar_length)  # Waktu total loading dibagi lebar bar
        progress = block * i
        remaining = empty_block * (bar_length - i)
        sys.stdout.write(f"[{progress}{remaining}] {int((i / bar_length) * 100)}%")  # Bar diisi dan menampilkan persentase
        sys.stdout.flush()
        sys.stdout.write("\b" * (bar_length + 7))  # Kembali ke awal untuk update bar

    sys.stdout.write(f"[{block * bar_length}] 100%\n")  # Bar penuh setelah selesai

user = []
Dev = []
Prem = []
is_registered = False
isDev = False
dev = ["Sell", "6285270058464"]
N = '\033[0m'
D = '\033[90m'
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'

ask = G + '[' + W + '?' + G + '] '
sukses = G + '[' + W + '√' + G + '] '
eror = R + '[' + W + '!' + R + ']'


def addowner():
    global isDev
    loading(1)
    name = input("Masukkan Nama Dev :")
    nomor = input("Masukkan Nomor Dev (9 digit) :")  # Ambil input sebagai string

    if not nomor.isdigit():  # Mengecek apakah nomor terdiri dari angka
        print("Nomor harus berupa angka!")
    elif len(nomor) != 9:  # Memastikan nomor harus tepat 9 digit
        print("Nomor harus memiliki tepat 9 angka!")
    else:
        Dev.append(name)
        Dev.append(nomor)
        print("Berhasil Mendaftar Dengan Data:\nName: {}\nNomor: {}\n\n".format(name, nomor))
        isDev = True
        menu_owner()
def addprem():
    global isDev, Prem
    if not isDev:
        print("fitur Hanya Bisa Di Akses Oleh Owner") 
        return
    name = input("Masukkan Nama User :")  
    passw = int(input("Masukkan Password :"))
    Prem.append(name)
    Prem.append(passw)
    print("Berhasil Menambahkan User Prem Dengan ID :\nName: {}\nPassword: {}\nNOTE!: Jangan Memberitahu Password Anda Kepada Siapapun".format(name, passw))
    Prem = True
    menu_owner()
def delprem():
    global isDev
    if not isDev:
        print("Fitur Khusus Owner!")
        return
    
    loading(1)
    name = input("Masukkan Nama Dev yang Ingin Dihapus: ")
    
    if name in Prem:
        index = Prem.index(name)  # Cari indeks nama dev
        nomor = Prem[index + 1]  # Nomor ada setelah nama di list
        del Prem[index:index + 2]  # Hapus nama dan nomor
        print("Users Premium dengan Nama '{}' dan Password '{}' berhasil dihapus.".format(name, passw))
        Prem = False  # Reset isDev jika perlu
    else:
        print("Nama Users tidak ditemukan!")
        menu_owner()
    
def delowner():
    global isDev
    if not isDev:
        print("Fitur Khusus Owner!")
        return
    
    loading(1)
    name = input("Masukkan Nama Dev yang Ingin Dihapus: ")
    
    if name in Dev:
        index = Dev.index(name)  # Cari indeks nama dev
        nomor = Dev[index + 1]  # Nomor ada setelah nama di list
        del Dev[index:index + 2]  # Hapus nama dan nomor
        print("Dev dengan Nama '{}' dan Nomor '{}' berhasil dihapus.".format(name, nomor))
        isDev = False  # Reset isDev jika perlu
    else:
        print("Nama Dev tidak ditemukan!")
        menu_owner()
    
def regis():
    global is_registered
    loading2(50, 0.05)
    name = input("Masukkan Nama :")
    try:
        umur = int(input("Masukkan Umur :"))
    except ValueError:
        print("Umur harus berupa angka!")
        return

    user.append(name)
    user.append(umur)
    print("Berhasil Mendaftar Dengan Data:\nName: {}\nUmur: {}\n\n".format(name, umur))
    is_registered = True
def show_dev():
    loading(1)
    acc = """   ____                _             
  / ___|_ __ ___  __ _| |_ ___  _ __ 
 | |   | '__/ _ \/ _` | __/ _ \| '__|
 | |___| | |  __/ (_| | || (_) | |   
 _\____|_|  \___|\__,_|\__\___/|_|
                                     """
    print (acc)                                
    print("\nNama Dev: {}".format(dev[0]))
    print("Hubungi Dev: {}\n".format(dev[1]))

def menu_owner():
    if not is_registered:
        print("\n╭랜࿆────────┈◦•⏤͟͟͞͞★")
        print("╎│❦ sɪʟᴀʜᴋᴀɴ ᴅᴀғᴛᴀʀ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ, ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ғɪᴛᴜʀ ɪɴɪ")
        print("╎ ⃟ꕥ________________⏤͟͟͞͞★\n")
        return
    loading(1)
    nenen = """         _____ ___   _ _____ ____  
  / _ \ \      / / \ | | ____|  _ \ 
 | | | \ \ /\ / /|  \| |  _| | |_) |
 | |_| |\ V  V / | |\  | |___|  _ < 
  \___/_ \_/\_/_ |_| \_|_____|_| \_\
 |  \/  | ____| \ | | | | |         
 | |\/| |  _| |  \| | | | |         
 | |  | | |___| |\  | |_| |         
 |_|  |_|_____|_| \_|\___/          """
                                    
    print(nenen)                                
    print("╭랜࿆────────┈◦•⏤͟͟͞͞★")
    print("╎│❦ [1] Decrypt")
    print("╎│❦ [2] Encrypt")
    print("╎│❦ [3] Addowner [ Nomor ]")
    print("╎│❦ [4] Delowner [ Nomor/Nama ]")
    print("╎│❦ [5] Addprem [ Nama/Password ]")
    print("╎│❦ [6] Delprem [ Nama/Password ]")
    print("╎ ⃟ꕥ________________⏤͟͟͞͞★\n")
    try:
        data = int(input("Masukkan Nomor Menu Di Atas -> "))
    except ValueError:
        print("Input harus berupa angka!")
        return

    if data == 1 or data == "decrypt":
        dekrip()
    elif data == 2:
        enkrip()
    elif data == 3:
        addowner()
    elif data == 4:
        delowner()
    elif data == 5:
        addprem()
    elif data == 6:
        delprem()       
    else:
        print("Menu tidak valid!")

def dekrip():
    try:
        sc = input(ask + W + "Script " + G + "> " + W)
        with open(sc, 'r') as f:
            filedata = f.read()

        newdata = filedata.replace("eval", "echo")

        out = input(ask + W + "Output " + G + "> " + W)
        with open(out, 'w') as f:
            f.write(newdata)

        print(sukses + "Sukses Decrypt Text")

    except KeyboardInterrupt:
        print(eror + " Stopped!")
    except FileNotFoundError:
        print(eror + " File Not Found!")
    except IOError:
        print(eror + " Error writing file!")
        menu_owner()
def enkrip():
    print("Fitur encrypt belum tersedia.")
    menu_owner()
def menu_tools():
    if not is_registered:
        print("\n╭랜࿆────────┈◦•⏤͟͟͞͞★")
        print("╎│❦ sɪʟᴀʜᴋᴀɴ ᴅᴀғᴛᴀʀ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ, ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ғɪᴛᴜʀ ɪɴɪ")
        print("╎ ⃟ꕥ________________⏤͟͟͞͞★\n")
        return
    loading(1)
    print("࿆─────『 ᴍᴇɴᴜ ᴛᴏᴏʟs 』───┈◦•⏤͟͟͞͞★")
    print("╎│❦ [1] ᴘᴇʀᴋᴀʟɪᴀɴ [ ᴀɴɢᴋᴀ ]")
    print("╎│❦ [2] ᴘᴇʀᴛᴀᴍʙᴀʜᴀɴ [ ᴀɴɢᴋᴀ ]")
    print("╎│❦ [3] ᴘᴇᴍʙᴀɢɪᴀɴ [ ᴀɴɢᴋᴀ ]")
    print("╎│❦ [4] ᴘᴇɴɢᴜʀᴀɴɢᴀɴ [ ᴀɴɢᴋᴀ ]")
    print("╎│❦ [5] ᴘᴀɴɢᴋᴀᴛ [ ᴀɴɢᴋᴀ ]")
    print("╎│❦ [6] ᴘᴇᴍʙᴀɢɪᴀɴ ɪɴᴛᴇɢʀᴀʟ [ ᴀɴɢᴋᴀ ]")
    print("'╎❦ [7] ᴍᴏᴅᴜʟᴏs [ ᴀɴɢᴋᴀ ]")
    print("╎ ⃟ꕥ________________⏤͟͟͞͞★")
    try:
        isii = int(input("Silahkan Pilih :"))
    except ValueError:
        print("Input harus berupa angka!")
        return

    if isii == 1:
        perkalian()
    elif isii == 2:
        pertambahan()
    elif isii == 3:
        pembagian()
    elif isii == 4:
        pengurangan()        
    else:
        print("Menu tidak valid!")
        
def pembagian():
    try:
        angka1 = int(input("Masukkan Angka 1 :"))
        angka2 = int(input("Masukkan Angka 2 :"))
        hasil = angka1 / angka2
        print(f"Hasil Dari {angka1} ÷ {angka2} = {hasil}")
        print("\n")
    except ZeroDivisionError:
        print("Error: Pembagian dengan nol tidak diperbolehkan!")
    except ValueError:
        print("Input harus berupa angka!")

def perkalian():
    try:
        angka1 = int(input("Masukkan Angka 1 :"))
        angka2 = int(input("Masukkan Angka 2 :"))
        hasil = angka1 * angka2
        print(f"Hasil Dari {angka1} × {angka2} = {hasil}")
        print("\n")
    except ValueError:
        print("Input harus berupa angka!")

def pertambahan():
    try:
        angka1 = int(input("Masukkan Angka 1 : "))
        angka2 = int(input("Masukkan Angka 2 : "))
        hasil = tambah(angka1, angka2)
        print(f"{angka1} + {angka2} = {hasil}")
        print("\n")
    except ValueError:
        print("Input harus berupa angka!")

def tambah(angka1, angka2):
    return angka1 + angka2

def operasi_yang_dihitung():
    # Simulasi operasi yang memakan waktu
    time.sleep(2)  # Misalnya operasi ini memakan waktu 2 detik

def runtime():
    start_time = time.time()  # Catat waktu mulai
    
    operasi_yang_dihitung()   # Jalankan operasi
    
    end_time = time.time()    # Catat waktu selesai
    response_time = end_time - start_time  # Hitung selisih waktu
    
    print(f"Kecepatan respons: {response_time:.4f} detik")


def show_menu():
    nomor = input("Masukkan Nomor, Di Awali +62 Bukan +Kangen Mantan. => ")
    pairing = [
       "AGWI-18JA",
       "OEDH-72DJ",
       "AKSM-16JS",
       "SKSK-JSNW",
       "SKSJ-JSJW",
       "BOKE-P289",
       "BSJQ-UAY1",
       "NXJA-KSSK",
       "NINJ-AKNT",
       "AHAB-MANM",
       "1818-2888",
       "JABD-8ALK",
       "KSJH-JSNK",]
    jjkj = random.choice(pairing)  
    kode = print(jjkj)
    time.sleep(20)
    periksa = input("Apakah Sudah Selesai? [ Y/N ] : ")
    if periksa == "n":
        print("Silahkan Restart....")
        print("byee..👋")
        exit()
        
    loading(1)
    banner = """  ____  _____ _     _                      
 / ___|| ____| |   | |                     
 \___ \|  _| | |   | |                     
  ___) | |___| |___| |___                  
 |____/|_____|_____|_____|_____ ____ _____ 
 |  _ \|  _ \ / _ \    | | ____/ ___|_   _|
 | |_) | |_) | | | |_  | |  _|| |     | |  
 |  __/|  _ <| |_| | |_| | |__| |___  | |  
 |_|   |_| \_\\___/ \___/|_____\____|  |_|  
                                           """
    print (banner)
    print("┅━━━═┅═❏ 『 ʙᴏᴛ ɪɴғᴏ 』 ❏═┅═━━━┅")
    print(runtime())
    print("╭랜࿆─────『 ᴍᴇɴᴜ 』───┈◦•⏤͟͟͞͞★")
    print("╎│❦ [ 1 ] Daftar")
    print("╎│❦ [ 2 ] Tampilkan Pembuat")
    print("╎│❦ [ 3 ] Masuk Menu Tools")
    print("╎│❦ [ 4 ] Masuk Menu Owner")
    print("╎ ⃟ꕥ________________⏤͟͟͞͞★")
    try:
        isi = int(input("Masukkan Angka ┃ "))
    except ValueError:
        print("Input harus berupa angka!")
        return

    if isi == 1:
        regis()
    elif isi == 2:
        show_dev()
    elif isi == 3:
        menu_tools()
    elif isi == 4:
        menu_owner()
    else:
        print("Menu tidak valid!")

def pengurangan():
    while True:
        try:
            angka1 = int(input("Masukkan Soal 1 : "))
            angka2 = int(input("Masukkan Soal 2 : "))
            hasil = angka1 - angka2
            print(f"Hasil {angka1} - {angka2} = {hasil}")
            break  # Keluar dari loop jika input valid
        except ValueError:
            print("Error! Input harus berupa angka.")
            tanya = input("Ingin Kembali Ke Menu Tools? [y/n] => ")
            if tanya.lower() == "y":
                menu_tools()
                break  # Keluar dari loop setelah memilih menu
            elif tanya.lower() == "n":
                show_menu()
                break  # Keluar dari loop setelah memilih menu
            else:
                print("Input tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    while True:
        show_menu()
        input("Tekan Enter untuk kembali ke menu...")

            
if __name__ == "__main__":
    while True:
        show_menu()
        input("Tekan Enter untuk kembali ke menu...")

