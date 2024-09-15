import time
import sys

def loading(duration=5):
    bar_length = 14  # Lebar progress bar
    block = "█"
    empty_block = "░"

    sys.stdout.write("Progress: \n[%s]" % (empty_block * bar_length))  # Membuat template progress bar
    sys.stdout.flush()
    sys.stdout.write("\b" * (bar_length + 11))  # Kembali ke awal bar

    for i in range(bar_length + 1):
        time.sleep(duration / bar_length)  # Waktu total loading dibagi lebar bar
        progress = block * i
        remaining = empty_block * (bar_length - i)
        sys.stdout.write(f"[{progress}{remaining}] {int((i / bar_length) * 100)}%")  # Bar diisi dan menampilkan persentase
        sys.stdout.flush()
        sys.stdout.write("\b" * (bar_length + 7))  # Kembali ke awal untuk update bar

    sys.stdout.write(f"[{block * bar_length}] 100%\nDone!\n")  # Bar penuh setelah selesai
    
    
user = []
is_registered = False
dev = ["Sell", "6285270058464"]
def regis():
    global is_registered
    loading(1)
    name = input("Masukkan Nama :")
    umur = int(input("Masukkan Umur :"))
    user.append(name)
    user.append(umur)
    print("Berhasil Mendaftar Dengan Data:\nName: {}\nUmur: {}\n\n".format(name, umur))
    is_registered = True
def show_dev():
    if not is_registered:
        print("\n╭랜࿆────────┈◦•⏤͟͟͞͞★")
        print("╎│❦ sɪʟᴀʜᴋᴀɴ ᴅᴀғᴛᴀʀ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ, ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ғɪᴛᴜʀ ɪɴɪ")
        print("╎ ⃟ꕥ________________⏤͟͟͞͞★\n")
        return
    loading(1)   
    print("\n")
    print(f"Nama Dev: {dev[0]}")
    print(f"Hubungi Dev: {dev[1]}")
    print("\n")
    
def show_menu():
    
    print("╭랜࿆─────『 ᴍᴇɴᴜ 』───┈◦•⏤͟͟͞͞★")
    print("╎│❦ [ 1 ] Daftar")
    print("╎│❦ [ 2 ] TampilKan Pembuat")
    print("╎│❦ [ 3 ] Melihat Code")
    print("╎ ⃟ꕥ________________⏤͟͟͞͞★")
    isi = int(input("Masukkan Angka ┃ "))
    
    if isi == 1:
         regis()
    elif isi == 2:
         show_dev()
    elif isi == 3:
         show_code()      
    
    
    
if __name__ == "__main__":
    while(True):
      show_menu()   
    
    
    
    
    
    
    
    
    
    
    
    
