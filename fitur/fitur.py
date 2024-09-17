import re
import requests
from colorama import Style, Fore, init
from pytube import YouTube
import instaloader
import os
init()  # Inisialisasi colorama

# Fungsi untuk Menu NSFW
def menu_nsfw():
    nsfw = """
      _   _ ____  _______        __
 | \ | / ___||  ___\ \      / /
 |  \| \___ \| |_   \ \ /\ / / 
 | |\  |___) |  _|   \ V  V /  
 |_|_\_|____/|_|_     \_/\_/   
  / ___|_ _| |/ /              
 | |    | || ' /               
 | |___ | || . \               
  \____|___|_|\_\              
                                """
    print(nsfw) 
    print("1. Link Videy") 
    print("2. Link Pornhub") 
    print("3. Link Xnxx") 
    print("4. Masuk Bokep Anime") 
    print("5. Masuk Bokep Indonesia Only") 
    tanya = int(input("\033[31mMasukkan Angka Di Atas\n\33[33m>\n\033[00m"))             
    if tanya == 1:
        masukkan_link_videy() 
    elif tanya == 2:
        masukkan_link_pornhub() 
    elif tanya == 3:
        masukkan_link_xnxx() 
    elif tanya == 4:
        display_anime()
    else:
        print(Fore.RED + "Input Harus Berupa Angka" + Style.RESET_ALL)

# Fungsi Downloader YouTube
from pytube import YouTube
import sys
import random
def user_pilih():
    choice = input("Silahkan Pilih, Batu, Gunting, Kertas => ").lower() 
    while choice not in ["batu", "gunting", "kertas"]:
          print("Pilihan Tidak Valid") 
          choice = input("Silahkan Pilih, Batu, Gunting, Kertas").lower
          return choice
        
def komputer_pilih():
       return random.choice(["Batu", "Gunting", "Kertas"])
 
def siapa_pemenang(user_pilih, komputer_pilih):
     if user_pilih == komputer_pilih:
       return "Serii Mang"
     if (user_pilih == 'batu' and komputer_pilih == 'gunting') or \
       (user_pilih == 'gunting' and komputer_pilih == 'kertas') or \
       (user_pilih == 'kertas' and komputer_pilih == 'batu'):
       return "User Menang! "
     return "Bot Menang!"
    
def mulai_game():
    user = user_pilih() 
    komputer = komputer_pilih() 
    
    print(f"Anda Memilih {user}") 
    print(f"Komputer Memilih {komputer}") 
    
    result = siapa_pemenang(user, komputer) 
    print(result) 
    

import re
import requests
import os

def ttdl(url, path):
    # Buat folder jika belum ada
    if not os.path.exists(path):
        os.makedirs(path)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Dapatkan konten halaman TikTok
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Gagal mendapatkan halaman TikTok.")
        return

    # Cari URL video menggunakan regex
    video_match = re.search(r'playAddr":"(.*?)"', response.text)
    if video_match:
        # Perbaiki URL video yang ditemukan
        video_url = video_match.group(1).replace('\\u002F', '/')

        # Download video
        video_response = requests.get(url)
        if video_response.status_code == 200:
            # Tentukan nama file
            file_name = os.path.join(path, "tiktok_video.mp4")
            # Simpan video
            with open(file_name, "wb") as file:
                file.write(video_response.content)
            print(f"Video berhasil diunduh ke {file_name}")
        else:
            print("Gagal mengunduh video.")
    else:
        print("URL video tidak ditemukan.")

# Contoh penggunaan

import requests

def aio(video_url, output_path):
    # Mengirim permintaan HTTP untuk mendapatkan konten video
    response = requests.get(video_url, stream=True)
    
    # Mengecek apakah permintaan berhasil
    if response.status_code == 200:
        # Membuka file di mode tulis biner untuk menyimpan video
        with open(output_path, 'wb') as video_file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    video_file.write(chunk)
        print(f"Video berhasil diunduh dan disimpan ke {output_path}")
    else:
        print(f"Gagal mengunduh video. Status kode: {response.status_code}")
        


def ig(url, path="."):
    loader = instaloader.Instaloader()
    try:
        post = instaloader.Post.from_shortcode(loader.context, url.split('/')[-2])
        loader.download_post(post, target=path)
        print(f"Berhasil Mengunduh Media Ke {path}")
    except Exception as e:
        print(f"Terjadi Error:\033[31m{e}")
        
"""
from TikTokApi import TikTokApi

def ttdl2(video_url, output_path):
    api = TikTokApi()
    video_data = api.video(url=video_url).bytes()

    file_name = output_path + "/tiktok_video.mp4"
    with open(file_name, "wb") as video_file:
        video_file.write(video_data)
    
    print(f"Video berhasil diunduh ke {file_name}")
"""

def yt(url, path='.'):
    try:
        yts = YouTube(url)
        # Mendapatkan stream dengan resolusi tertinggi
        stream = yts.streams.get_highest_resolution()
        print(f"Menyiapkan unduhan: {yt.title}")
        # Mengunduh video ke folder yang ditentukan
        stream.download(output_path=path)
        print(f"Video berhasil diunduh ke {path}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Menu Tools
def menu_tools():
    tool = """
  _____ ___   ___  _     ____  
 |_   _/ _ \ / _ \| |   / ___| 
   | || | | | | | | |   \___ \ 
   | || |_| | |_| | |___ ___) |
   |_| \___/ \___/|_____|____/ 
                               """
    print("\n") 
    print(tool)
    print("1. Yt Downloader")
    print("2. Ig Downloader")
    print("3. TikTok Downloader [ In Maintenance ]")
    print("4. TikTok Downloader2")
    print("5. Aio Downloader [ All Downloader ]")
    pilih = int(input("Pilih Salah satu Angka\n\033[31m> " + Style.RESET_ALL))  
    if pilih == 1:
        video_url = input("Masukkan URL Video > ")
        download_path = input("Masukkan Path Penyimpanan (default adalah folder saat ini) > ")
        if not download_path:
            download_path = "."
        yt(video_url, download_path)
    elif pilih == 2:
        url = input("[ Url ] : ")
        path = input("[ Path ] : ")
        if not path:
            path = "."
        ig(url, path)   
    elif pilih == 3:
        url = input("[ Url ] : ")
        path = '.'
        ttdl(url, path)
    elif pilih == 5:
        url = input("[ URL ] : ")  
        path = "./download.mp4"
        aio(url, path)       
    
        
        
        
        
        
        
        
        
        
        
# Menu Fun
def menu_fun():
    fun = """
       _____ _   _ _   _ 
 |  ___| | | | \ | |
 | |_  | | | |  \| |
 |  _| | |_| | |\  |
 |_|    \___/|_| \_|
    Developers: Sell   Teams: Sell | NextTraveller\n   Country: Indonesia                 """
    print(fun) 
    print("\n") 
    print("Silahkan Pilih List Di Bawah Ini") 
    print("1. Batu Gunting Kertas") 
    print("2. In Update!") 
    tanya = int(input("Silahkak Pilih Angka Dari List Di Atas\n\033[31m=>" + Style.RESET_ALL))
    if tanya == 1:
       mulai_game()
        

