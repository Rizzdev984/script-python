_Z='%Y%m%d%H%M%S'
_Y='Gagal mengunduh video.'
_X='tiktok_video.mp4'
_W='\\u002F'
_V='playAddr":"(.*?)"'
_U='Gagal mendapatkan halaman TikTok.'
_T='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
_S='User-Agent'
_R='Enter Untuk Kembali'
_Q='\x1b[31m[ Ai ] For Back'
_P='Byee... '
_O='html.parser'
_N='Masukkan Angka: '
_M='application/json'
_L='kertas'
_K='gunting'
_J='batu'
_I='Pertanyaan: '
_H=False
_G='wb'
_F='exit'
_E='div'
_D='\n'
_C='message'
_B='result'
_A=True
import asyncio,re,requests,secrets
from colorama import Style,Fore,init
from pytube import YouTube
from datetime import datetime
import instaloader,shutil,os,sys,random
from pytube import YouTube
from tqdm import tqdm
from urllib.parse import urlparse
from flask import Flask,current_app,jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
init()
Token=secrets.token_hex(17)
app=Flask(__name__)
def searchVideos(videoName):
	H='metadata';G='thumb-under';F='thumb';E='mozaique';I=asyncio.new_event_loop();J=r(f"https://www.xnxx.com/search/{videoName}",I);C=BeautifulSoup(J,'html5lib');D=[]
	if C.find(class_=E)==None:return
	else:
		K=C.find(class_=E).find_all(class_='thumb-block')
		for A in K:B=A.find(_E,class_=F).findNext('a').attrs['href'];B=f"https://xnxx.com{B}";L=A.find(_E,class_=F).findNext('img').attrs['src'];M=A.find(_E,class_=G).findNext('p').text.strip();N={'duration':A.find(_E,class_=G).find('p',class_=H).contents[1].strip()};D.append({'title':M,'url':B,'thumbnail':L,H:N})
	return D
@app.route('/')
def home():return jsonify({'hello':'world'})
def clear_console():os.system('cls'if os.name=='nt'else'clear')
def nama():
	try:A=os.getlogin();return A
	except Exception as B:return f"Terjadi kesalahan: {B}"
@app.route('/videos')
def hVideos():return current_app.response_class(json.dumps(homeVideos(),indent=4),mimetype=_M)
@app.route('/videos/<video_name>')
def sVideos(video_name):
	B='success';A=searchVideos(str(video_name))
	if A==None:return jsonify({B:_H,_C:'Not found'})
	else:return current_app.response_class(json.dumps({B:_A,_C:'Success 200',_B:A},indent=4),mimetype=_M)
def menu_nsfw():
	print('In [ Maintenance ]');return;B="\n      _   _ ____  _______        __\n | \\ | / ___||  ___\\ \\      / /\n |  \\| \\___ \\| |_   \\ \\ /\\ / / \n | |\\  |___) |  _|   \\ V  V /  \n |_|_\\_|____/|_|_     \\_/\\_/   \n  / ___|_ _| |/ /              \n | |    | || ' /               \n | |___ | || . \\               \n  \\____|___|_|\\_\\              \n                                ";print(B);print('1. Link Videy');print('2. Link Pornhub');print('3. Link Xnxx');print('4. Masuk Bokep Anime');print('5. Masuk Bokep Indonesia Only');print('6. SearchVideo Xnxx [ Name ]');A=int(input('\x1b[31mMasukkan Angka Di Atas\n\x1b[33m>\n\x1b[00m'))
	if A==1:masukkan_link_videy()
	elif A==2:masukkan_link_pornhub()
	elif A==3:masukkan_link_xnxx()
	elif A==4:display_anime()
	elif A==5:display_indo()
	elif A==6:C=input('Masukkan Nama Bokep Yang Ingin Di Cari => ');searchVideos(C)
	else:print(Fore.RED+'Input Harus Berupa Angka'+Style.RESET_ALL)
def menu_tools():
	B='\n  _____ ___   ___  _     ____  \n |_   _/ _ \\ / _ \\| |   / ___| \n   | || | | | | | | |   \\___ \\ \n   | || |_| | |_| | |___ ___) |\n   |_| \\___/ \\___/|_____|____/ \n                               ';print(_D);print(B);print('1. Cuaca ⌜ ɴᴀᴍᴀ/ᴅᴀᴇʀᴀʜ ⌟');print('2. Encrypt ⌜ ᴄᴏᴅᴇ ⌟');print('3. CekNik ⌜ ɴɪᴋ ⌟');print('4. Decrypt ⌜ ᴄᴏᴅᴇ ⌟');A=int(input(_N))
	if A==1:C=input('Masukkan Daerah: ');cuaca(C)
	elif A==2:D=input(' Code: ');enc(D)
	elif A==3:E=input('Masukkan Nik: ');ceknik(E)
	elif A==4:F=input('Masukkan Code: ');G=deobfuscate_code(F);print(G)
def ceknik(nik):B='data';import requests as C,json;D=nik;E=f"https://skizo.tech/api/checknik?apikey=sell%20aja&nik={D}";F=C.get(E);A=json.loads(F.text);print(f"Nik: {A[_C][B]['nik']}");print(f"Kelamin: {A[_C][B]['jk']}");print(f"Tanggal Lahir: {A[_C][B]['tgl']}");print(f"Kabupaten: {A[_C][B]['kab']}");print(f"Kecamatan: {A[_C][B]['kec']}");print(f"Provinsi: {A[_C][B]['prov']}");print(f"Di Ubah Tanggal: {A[_C][B]['modified_time']}");print(f"[31mSource: {A[_C][B]['source']}"+Style.RESET_ALL)
def cuaca(daerah):import requests as A;B=f"https://wttr.in/{daerah}";C=A.get(B);print(C.text)
def enc(code):import requests as A,json;clear_console();B='\n      _____ _   _  ____ ______   ______ _____ \n | ____| \\ | |/ ___|  _ \\ \\ / /  _ \\_   _|\n |  _| |  \\| | |   | |_) \\ V /| |_) || |  \n | |___| |\\  | |___|  _ < | | |  __/ | |  \n |_____|_| \\_|\\____|_| \\_\\|_| |_|    |_|  \n                                           ';print(B);C=f"https://api.shannmoderz.xyz/tools/encrypt?key=sell&query={code}";D=A.get(C);E=json.loads(D.text);F=f"{E[_B]}";print(F)
def deobfuscate_code(code):
	B='https://deobfuscate.io/';C=requests.Session();A=C.get(B);D={'input':code};A=C.post(B,data=D)
	if A.status_code==200:return''+A.text
	else:return f"Error: {A.status_code}"
def menu_ai():
	B='\n __  __ _____ _      _ _   _      _    ___ \n |  \\/  | ____| \\ | | | | |            / \\  |_ _|\n | |\\/| |  _| |  \\| | | | |  _____    / _ \\  | | \n | |  | | |___| |\\  | |_| | |_____|  / ___ \\ | | \n |_|  |_|_____|_| \\_|\\___/          /_/   \\_\\___|\n                                                 \n    ';print(B);print(_D);print('1. BlackboxAi ⌜ ɪɴ ᴜᴘᴅᴀᴛᴇ ⌟');print('2. AliciaAi ⌜ ǫᴜᴇʀʏ ⌟');print('3. BocchiAi ⌜ ǫᴜᴇʀʏ ⌟');print('4. ZettaAi ⌜ ǫᴜᴇʀʏ ⌟');print('5. GptLogic ⌜ ǫᴜᴇʀʏ ⌟');print('6. Text2Img ⌜ ᴛᴇxᴛ ⌟');A=int(input(_N))
	if A==1:blai()
	elif A==2:ai2()
	elif A==3:bocchiai()
	elif A==4:zettaai()
	elif A==5:gptlogic()
	elif A==6:C=input('Masukkan Untuk File Di Simpan, Enter For [ Default ] : ');txt2img(C)
def ai(pertanyaan):
	import requests as B;from bs4 import BeautifulSoup as C;D=f"https://blackbox.ai/?q={pertanyaan}";A=B.get(D)
	if A.status_code==200:
		E=C(A.text,_O);F=E.find_all('p')
		for G in F:print(G.text)
	else:print(f"Gagal mengambil data. Status kode: {A.status_code}")
def ai2():
	import requests as B,json
	while _A:
		print(_D);A=input(_I);print(_D)
		if A.lower()==_F:print('Byee...');break
		C=f"https://api.kyuurzy.site/api/ai/alicia?query={A}";D=B.get(C);E=json.loads(D.text);print(f"Alicia: {E[_B]}")
def blai():
	import requests as A;from bs4 import BeautifulSoup as B;C=input('Query: ');D='https://blackbox.ai/?q={}'.format(C);E=A.get(D);F=B(E.text,_O);G=F.find_all(_E,class_='class_name')
	for H in G:print(H.text)
def bocchiai():
	import requests as B,json
	while _A:
		A=input(_I);C=f"https://api.kyuurzy.site/api/ai/Bocchi?query={A}";D=B.get(C);E=json.loads(D.text);print('\x1b[31m[ Enter ] For Exit'+Style.RESET_ALL);print(f"Bocchi: {E[_B]}")
		if A.lower()==_F:print(_P);break
def gptlogic():
	import json,requests as C
	while _A:
		A=input(_I);D=f"Hai GptLogic, {A}";E=f"https://apikita.exonity.xyz/api/gptlogic?message={D}&prompt=Ubah%20Bahasa%20Mu%20Menjadi%20Indonesia";F=C.get(E);G=F.text;B=json.loads(G);print('\x1b[31m[ Exit ] For Exits '+Style.RESET_ALL);print(_Q+Style.RESET_ALL)
		if _B in B:print(f"Pertanyaan: {A}\nJawaban: {B[_B]}")
		if A.lower()==_F:print(_P);break
		elif A.lower()=='ai':menu_ai
def txt2img(file_path='./fitur/Hasil.jpg'):
	A=file_path;import json
	while _A:
		try:
			B=input('Masukkan Text: ')
			if B.lower()==_F:print(' Byee... ');break
			elif B.lower()=='ai':menu_ai();continue
			F=f"https://api.shannmoderz.xyz/ai/txt2img?key=sell&prompt={B}";C=requests.get(F);C.raise_for_status();G=json.loads(C.text);H=G[_B]['url'];D=requests.get(H,stream=_A);D.raise_for_status()
			if A:
				E=os.path.dirname(A)
				if not os.path.exists(E):os.makedirs(E)
				with open(A,_G)as I:
					for J in D.iter_content(chunk_size=8192):I.write(J)
				print(f"Gambar berhasil diunduh ke {A}")
			else:print('File path cannot be empty')
		except requests.exceptions.RequestException as K:print(f"Terjadi kesalahan saat mengunduh gambar: {K}")
		print('\x1b[31m[ Exit ] For Exits');print(_Q)
def zettaai():
	import requests as B,json
	while _A:
		A=input(_I);C=f"https://api.kyuurzy.site/api/ai/aizeta?query={A}";D=B.get(C);E=json.loads(D.text);print('='*14);print('\x1b[31m[ Enter ] For Exits'+Style.RESET_ALL);print('='*14);print(f"Pertanyaan: {A}\nJawaban Zetta: {E[_B]['answer']}")
		if A.lower()==_F:break
def menu_fun():
	C=Fore.RED+'\n       _____ _   _ _   _ \n |  ___| | | | \\ | |\n | |_  | | | |  \\| |\n |  _| | |_| | |\\  |\n |_|    \\___/|_| \\_|\n    Developers: Sell   Teams: Sell | NextTraveller\n   Country: Indonesia                 '+Style.RESET_ALL;print(C);D=Fore.RED+'\n    [ 09 ] For Exit Script\n    [ 99 ] Contact Developers Script\n    [ 01 ] Request Feature To Developers\n    [ 00 ] Back To Main Menu\n    '+Style.RESET_ALL;print(D);print(_D);print('Silahkan Pilih List Di Bawah Ini');print('1. Batu Gunting Kertas');print('2. Apakah ⌜ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ⌟');print('3. Mengapa ⌜ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ⌟');print('4. Kapankah ⌜ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ⌟');print('5. Taugasih');print('6. Kenapasih');print('7. Cantik Cek ⌜ ɴᴀᴍᴀ ⌟');print('8. Lyrics ⌜ ɴᴀᴍᴀ ʟᴀɢᴜ ⌟');print('9. ArtiMimpi ⌜ ᴍɪᴍᴘɪ ᴍᴜ ⌟');A=int(input('Silahkak Pilih Angka Dari List Di Atas\n\x1b[31m=>'+Style.RESET_ALL))
	if A==1:mulai_game()
	elif A==2:E=input('Apakah ');apakah(E)
	elif A==3:F=input('Mengapa ');mengapa(F)
	elif A==4:G=input('Kapankah ');kapankah(G)
	elif A==5:taugasih()
	elif A==6:
		H=input('Kenapa Sih ');B=['Python is a programming language.','This is a simple search engine.','Python can be used for web development.','Search engines are powerful tools.','Karena Bumi Terdiri Dari Cairan Panas Ketika Terbentuk, Jadi Tidak Heran'];I=create_index(B);J=search(H,I,B);print('Hasil: ')
		for K in J:print(K)
	elif A==7:L=input('Masukkan Nama: ');cantikcek(L)
	elif A==8:M=input('Masukkan Nama Lagu: ');lirik(M)
	elif A==9:N=input('Apa Mimpi Anda? : ');artimimpi(N)
def lirik(lagu):import requests as B,json;C=f"https://api.betabotz.eu.org/api/search/lirik?lirik={lagu}&apikey=sAhJPUM3";D=B.get(C);A=json.loads(D.text);E=f"\n{A[_B]['title']}";F=f"\n{A[_B]['lyrics']}";G=f"\n{A[_B]['artist']}";print(f"Lyrics:\n{F}Nama Lagu: {E}Artis: {G}")
def user_pilih():
	A=input('Silahkan Pilih, Batu, Gunting, Kertas => ').lower()
	while A not in[_J,_K,_L]:print('Pilihan Tidak Valid');A=input('Silahkan Pilih, Batu, Gunting, Kertas').lower;return A
def komputer_pilih():return random.choice(['Batu','Gunting','Kertas'])
def siapa_pemenang(user_pilih,komputer_pilih):
	B=komputer_pilih;A=user_pilih
	if A==B:return'Serii Mang'
	if A==_J and B==_K or A==_K and B==_L or A==_L and B==_J:return'User Menang! '
	return'Bot Menang!'
def mulai_game():A=user_pilih();B=komputer_pilih();print(f"Anda Memilih {A}");print(f"Komputer Memilih {B}");C=siapa_pemenang(A,B);print(C)
def apakah(pertanyaan):A=random.choice(['Iya','Tidak','Mungkin','Mana Ku Tau','Tidak Mungkin','Mungkin Saja','Pasti','Anjay Alok']);B=pertanyaan;C=f"[32m⌜ ᴀᴘᴀᴋᴀʜ ⌟\nᴘᴇʀᴛᴀɴʏᴀᴀɴ: {B}\nᴊᴀᴡᴀʙᴀɴ: {A}"+Style.RESET_ALL;print(C)
def mengapa(pertanyaan):A=random.choice(['Iya','Mungkin Kau Hoki','Tidak','Karena Kau Jelek Kali😂','Lu Kurang Tamvan😂','Jangan Berharap😂','Kurang Skibidi','Kurang Sigma🤫🧏\u200d♂️','Kurang Aura Mu😝','Malas Mikir']);B=pertanyaan;C=f"[34m⌜ ᴍᴇɴɢᴀᴘᴀ ᴋᴀʜ? ⌟\nᴘᴇʀᴛᴀɴʏᴀᴀɴ: ⌜ {B} ⌟\nᴊᴀᴡᴀʙᴀɴ: ⌜ {A} ⌟"+Style.RESET_ALL;print(C);input('Ketik Enter Untuk Kembali');menu_fun()
def kapankah(perr):A=random.choice(['1 Tahun Lagi','3 Tahun Lagi😍','Mana Gw Tau','1 Menit Lagi','20 Menit Lagi','100 Tahun Lagi','5 Abad Lagi','Kapan²','Apalah']);B=perr;C=f"[62m⌜ ᴋᴀᴘᴀɴ ᴋᴀʜ ⌟\nᴘᴇʀᴛᴀɴʏᴀᴀɴ : Kapankah {B}\nᴊᴀᴡᴀʙᴀɴ: {A}"+Style.RESET_ALL;print(C);input('Enter Untuk Kenbali Ke Menu');menu_fun()
def taugasih():A=random.choice(['Tahukah Anda seekor capung bisa terbang dengan kecepatan 40kph (25mph)','Tahukah Anda bahwa semua burung hantu bertelur putih?','Tahukah Anda bahwa Hawaii secara resmi menjadi bagian dari AS pada 14 Juni 1900','Tahukah Anda bahwa rata-rata orang tertawa 10 kali sehari?','Tahukah Anda bahwa diameter Jupiter adalah 152.800 km (88.700 mil)','Tahukah Anda bahwa warna sikat gigi yang paling populer adalah biru','Tahukah Anda bahwa harimau memiliki kulit belang serta bulu','Tahukah Anda bahwa ngengat tidak punya perut','Tahukah Anda bahwa hamburger ditemukan pada tahun 1900','Tahukah Anda bahwa aichmophobia adalah ketakutan akan jarum dan benda runcing','Tahukah Anda bahwa kuku jari tangan tumbuh lebih cepat daripada kuku kaki','Tahukah Anda kata *hampir* adalah yang terpanjang dalam bahasa Inggris dengan semua huruf dalam urutan abjad','Tahukah Anda bahwa iatrofobia adalah ketakutan akan dokter','Tahukah Anda bahwa membanting pintu mobil Anda dulunya ilegal di Swiss','Tahukah Anda bahwa mamalia terkecil di dunia adalah kelelawar bumblebee dari Thailan','Tahukah Anda bahwa singa memberi makan setiap 3 hingga 4 hari sekali','Tahukah Anda bahwa cangkangnya 12% dari berat telur','Tahukah Anda bahwa landak rata-rata memiliki 30.000 duri','Tahukah Anda bahwa jeruk bali mendapatkan namanya dari cara ia tumbuh dalam kelompok seperti anggur di pohon anggur','Tahukah Anda bahwa 45% orang menggunakan obat kumur setiap hari','Tahukah Anda bahwa umur tupai adalah 9 tahun','Tahukah Anda bahwa Anda dapat membedakan jenis kelamin kuda dari giginya (kebanyakan jantan memiliki 40, betina 36)','Tahukah Anda 10% dari pasokan makanan dunia dikonsumsi oleh serangga','Tahukah kamu awan terbang lebih tinggi di siang hari daripada di malam hari','Tahukah Anda bahwa Empire State Building di New York memiliki berat lebih dari 365.000 ton','Tahukah Anda Antartika terdiri dari 98% es dan 2% batu tandus','Tahukah Anda 90% orang bergantung pada jam alarm untuk bangun','Tahukah Anda bahwa kopi adalah minuman paling populer di seluruh dunia dengan lebih dari 400 miliar cangkir dikonsumsi setiap tahun','Tahukah Anda bahwa Bumi disambar petir lebih dari 100 kali setiap detik','Tahukah Anda bahwa rata-rata orang memiliki 10.000 selera?','Tahukah Anda bahwa sel darah merah diproduksi di sumsum tulang?','Tahukah Anda bahwa 11% orang kidal','Tahukah kamu setiap tahun matahari kehilangan 360 juta ton']);print(f"[31m{A}"+Style.RESET_ALL);input('Silahkan Tekan Enter Untuk Kembalu Ke Menu');menu_fun()
import re
from collections import defaultdict
def preprocess(text):A=text;A=A.lower();A=re.sub('\\W+',' ',A);return A.split()
def create_index(documents):
	A=defaultdict(list)
	for(B,C)in enumerate(documents):
		D=preprocess(C)
		for E in D:A[E].append(B)
	return A
def search(query,index,documents):
	C=documents;B=index;E=preprocess(query);A=set(range(len(C)))
	for D in E:
		if D in B:A&=set(B[D])
		else:A=set();break
	return[C[A]for A in A];input(_R);menu_fun()
def cantikcek(nama):A=nama;A=A;B=random.randint(1,100);C=f"⌜ ᴄᴀɴᴛɪᴋ ᴄᴇᴋ ⌟\nɴᴀᴍᴀ: {A}\nᴄᴀɴᴛɪᴋ: {B}%";print(C);input(_R);menu_fun()
def artimimpi(mimpi):
	import requests as C,json;A=mimpi;D=f"https://api.lolhuman.xyz/api/primbon/artimimpi?apikey=c358f182b9f84da3265683cb&query={A}";E=C.get(D);B=json.loads(E.text)
	if _B in B:F=f"Mimpi: {A}\nArti Mimpi: {B[_B]}";print(F);input('Silahkan Enter Untuk Kembali');menu_fun()
def dl():
	F=' [ Path ] => ';E=' [ Url ] => ';print('Haiii {}'.format(nama()));print(_D);H='  ____   _____        ___   _ _     ___    _    ____    \n     |  _ \\ / _ \\ \\      / / \\ | | |   / _ \\  / \\  |  _ \\   \n     | | | | | | \\ \\ /\\ / /|  \\| | |  | | | |/ _ \\ | | | |  \n     | |_| | |_| |\\ V  V / | |\\  | |__| |_| / ___ \\| |_| |  \n     |____/_\\___/_ \\_/\\_/_ |_| \\_|_____\\___/_/   \\_\\____/   \n     |  \\/  | ____| \\ | | | | |                             \n     | |\\/| |  _| |  \\| | | | |                             \n     | |  | | |___| |\\  | |_| |                             \n     |_|  |_|_____|_| \\_|\\___/                              \n                                                        ';print('1. Yt Downloader');print('2. Ig Downloader');print('3. TikTok Downloader [ In Maintenance ]');print('4. TikTok Downloader2');print('5. Aio Downloder ⌜ ᴍᴘ𝟺/ ᴀʟʟ ᴛʏᴘᴇ ʟɪɴᴋ ⌟');C=int(input('Silahkan Masukkan Angka Berdasarkan Code Di Atas\n>× '))
	if C==1:A=input(E);B=input(F);yt(A,B)
	elif C==2:A=input(E);B=input(F);ig(A,B)
	elif C==3:A=input(E);B=input(F);ttdl(A,B)
	elif C==4:
		G=input('Masukkan URL TikTok: ');D='.'
		if not os.path.exists(D):os.makedirs(D);tiktok_downloader(G,D)
	elif C==5:A=input('ᴍᴀsᴜᴋᴋᴀɴ ᴜʀʟ : ');B=input('ᴍᴀsᴜᴋᴋᴀɴ ᴛᴇᴍᴘᴀᴛ ᴅɪʀᴇᴋᴛᴏʀʏ ᴘᴇɴʏɪᴍᴘᴀɴᴀɴ ᴠɪᴅᴇᴏ : ');aio2(A,B)
def ttdl(url,path):
	A=path
	if not os.path.exists(A):os.makedirs(A)
	F={_S:_T};B=requests.get(url,headers=F)
	if B.status_code!=200:print(_U);return
	C=re.search(_V,B.text)
	if C:
		H=C.group(1).replace(_W,'/');D=requests.get(url)
		if D.status_code==200:
			E=os.path.join(A,_X)
			with open(E,_G)as G:G.write(D.content)
			print(f"Video berhasil diunduh ke {E}")
		else:print(_Y)
	else:print('URL video tidak ditemukan.')
def tiktok_downloader(url,output_path='.'):
	A={_S:_T};B=requests.get(url,headers=A)
	if B.status_code!=200:print(_U);return
	C=re.search(_V,B.text)
	if C:
		G=C.group(1).replace(_W,'/');D=os.path.join(output_path,_X);E=requests.get(G,headers=A,stream=_A)
		if E.status_code==200:
			with open(D,_G)as H:
				for F in E.iter_content(chunk_size=1024):
					if F:H.write(F)
			print(f"Video berhasil diunduh ke {D}")
		else:print(_Y)
	else:print('URL video tidak ditemukan di halaman TikTok.')
def aio2(video_url,output_path):
	C=video_url;B=output_path
	try:
		E=urlparse(C)
		if not E.scheme or not E.netloc:raise ValueError('URL tidak valid')
		D=requests.head(C,allow_redirects=_A);D.raise_for_status();F=D.headers.get('Content-Type','')
		if not F.startswith('video/'):raise ValueError(f"URL tidak mengarah ke file video. Content-Type: {F}")
		H=int(D.headers.get('Content-Length',0));os.makedirs(os.path.dirname(B),exist_ok=_A);G=requests.get(C,stream=_A);G.raise_for_status()
		with open(B,_G)as I,tqdm(desc=os.path.basename(B),total=H,unit='iB',unit_scale=_A,unit_divisor=1024)as J:
			for K in G.iter_content(chunk_size=8192):L=I.write(K);J.update(L)
		print(f"Video berhasil diunduh dan disimpan ke {B}");return _A
	except requests.RequestException as A:print(f"Terjadi kesalahan saat mengunduh video: {A}")
	except ValueError as A:print(f"Kesalahan: {A}")
	except IOError as A:print(f"Terjadi kesalahan saat menyimpan file: {A}")
	except Exception as A:print(f"Terjadi kesalahan yang tidak terduga: {A}")
	return _H
def aio(video_url,output_path):
	B=output_path;A=requests.get(video_url,stream=_A)
	if A.status_code==200:
		with open(B,_G)as D:
			for C in A.iter_content(chunk_size=1024):
				if C:D.write(C)
		print(f"Video berhasil diunduh dan disimpan ke {B}")
	else:print(f"Gagal mengunduh video. Status kode: {A.status_code}")
def ig(url,path='.'):
	A=instaloader.Instaloader()
	try:B=instaloader.Post.from_shortcode(A.context,url.split('/')[-2]);A.download_post(B,target=path);print(f"Berhasil Mengunduh Media Ke {path}")
	except Exception as C:print(f"Terjadi Error:[31m{C}")
def yt(url,path='.'):
	try:A=YouTube(url);B=A.streams.get_highest_resolution();print(f"Menyiapkan unduhan: {A.title}");B.download(output_path=path);print(f"Video berhasil diunduh ke {path}")
	except Exception as C:print(f"Terjadi kesalahan: {C}")
def namadev():A=['sell']
def nama_devv(nama):namadev();dev.remove[index+0];dev.append(nama)
def waktuucapan():
	C=datetime.now().time();B=C.hour
	if 5<=B<12:A='Pagi🌄'
	elif 12<=B<15:A='Siang🌅'
	elif 15<=B<18:A='Sore🌄'
	else:A='Malam🌃'
	return A
def menu_owner():
	print('Selamat {} User'.format(waktuucapan()));print(_D);D='\n    \x1b[34m _   _ _______  _______                                  \n | \\ | | ____\\ \\/ /_   _|                                 \n |  \\| |  _|  \\  /  | |                                   \n | |\\  | |___ /  \\  | |                                   \n |_|_\\_|_____/_/\\_\\_|_|   _______ _     _     _____ ____  \n |_   _|  _ \\    / \\ \\   / / ____| |   | |   | ____|  _ \\ \n   | | | |_) |  / _ \\ \\ / /|  _| | |   | |   |  _| | |_) |\n   | | |  _ <  / ___ \\ V / | |___| |___| |___| |___|  _ < \n   |_| |_| \\_\\/_/   \\_\\_/  |_____|_____|_____|_____|_| \\_\\'+Style.RESET_ALL;print(D);print('1. Addprem');print('2. Delprem');print('3. Backup File Menu');print('4. Backup File Fitur');A=int(input('Masukkan Angka Dari Di Atas => '))
	if A==1:addprem()
	elif A==2:delprem()
	elif A==3:B='menu.py';C='.';bakcup_menu(B,C)
	elif A==4:B='fitur.py';C='.';bakcup_fitur(B,C)
prem=[]
isPrem=_H
def addprem():global prem;global isPrem;A=input('ᴍᴀsᴜᴋᴋᴀɴ ɴᴀᴍᴀ ᴜsᴇʀ: ');B=input('ᴍᴀsᴜᴋᴋᴀɴ ᴜᴍᴜʀ ᴜsᴇʀ: ');print('⌜ ɴᴇxᴛᴛʀᴀᴠᴇʟʟᴇʀ ⌟');prem.append(A);prem.append(B);print(f"ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴅᴀғᴛᴀʀ ᴅᴇɴɢᴀɴ ɪᴅ:\nɴᴀᴍᴀ: ⌜ {A} ⌟\nᴜᴍᴜʀ: ⌜ {B} ⌟\n⌜ ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ʙᴏᴛ ɴᴇxᴛᴛʀᴀᴠᴇʟʟᴇʀ ⌟");isPrem=_A;menu_owner()
def delprem():
	A=input('Masukkan Nama Users Yang Ingin Di Hapus Dev: ');print(' ⌜ ɴᴇxᴛᴛʀᴀᴠᴇʟʟᴇʀ ⌟')
	if A in prem:B=prem.index(A);C=prem[B+1];del prem[B:B+2];print('ᴜsᴇʀ ʙᴇʀɴᴀᴍᴀ {} ʙᴇʀʜᴀsɪʟ ᴅɪ ʜᴀᴘᴜs ᴅᴀʀɪ ᴅᴀᴛᴀʙᴀsᴇ ᴜsᴇʀ ᴘʀᴇᴍ\n『 ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ɴᴇxᴛᴛʀᴀᴠᴇʟʟᴇʀ sᴄʀɪᴘᴛ 』\n⌜ ɴᴇxᴛᴛʀᴀᴠᴇʟʟᴇʀ ⌟'.format(A));D=_H;menu_owner()
def backup_menu(source_file,backup_dir):
	B=backup_dir;A=source_file
	if not os.path.exists(B):os.makedirs(B)
	D=datetime.now().strftime(_Z);E=os.path.basename(A);F=f"{E}_{D}";C=os.path.join(B,F);shutil.copy2(A,C);print(f"File {A} berhasil di-backup ke {C}\n⌜ ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ʙᴏᴛ ɴᴇxᴛᴛʀᴀᴠᴇʟʟᴇʀ ⌟");menu_owner()
def bakcup_fitur(source_file,backup_dir):
	B=backup_dir;A=source_file
	if not os.path.exists(B):os.makedirs(B)
	D=datetime.now().strftime(_Z);E=os.path.basename(A);F=f"{E}_{D}.py";C=os.path.join(B,F);shutil.copy2(A,C);print(f"File {A} berhasil di-backup ke {C}\n⌜ ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ʙᴏᴛ ɴᴇxᴛᴛʀᴀᴠᴇʟʟᴇʀ ⌟");menu_owner()