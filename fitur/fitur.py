_a='%Y%m%d%H%M%S'
_Z='Gagal mengunduh video.'
_Y='tiktok_video.mp4'
_X='\\u002F'
_W='playAddr":"(.*?)"'
_V='Gagal mendapatkan halaman TikTok.'
_U='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
_T='User-Agent'
_S='Enter Untuk Kembali'
_R='\x1b[31m[ Ai ] For Back'
_Q='\x1b[31m[ Exit ] For Exits '
_P='Masukkan Angka: '
_O='application/json'
_N='kertas'
_M='gunting'
_L='batu'
_K='\x1b[31m[ Exit ] For Exit'
_J=False
_I='wb'
_H='Byee... '
_G='\n'
_F='data'
_E='Pertanyaan: '
_D='message'
_C='exit'
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
	I='metadata';H='thumb-under';G='thumb';F='mozaique';B='div';J=asyncio.new_event_loop();K=r(f"https://www.xnxx.com/search/{videoName}",J);D=BeautifulSoup(K,'html5lib');E=[]
	if D.find(class_=F)==None:return
	else:
		L=D.find(class_=F).find_all(class_='thumb-block')
		for A in L:C=A.find(B,class_=G).findNext('a').attrs['href'];C=f"https://xnxx.com{C}";M=A.find(B,class_=G).findNext('img').attrs['src'];N=A.find(B,class_=H).findNext('p').text.strip();O={'duration':A.find(B,class_=H).find('p',class_=I).contents[1].strip()};E.append({'title':N,'url':C,'thumbnail':M,I:O})
	return E
@app.route('/')
def home():return jsonify({'hello':'world'})
def clear_console():os.system('cls'if os.name=='nt'else'clear')
def nama():
	try:A=os.getlogin();return A
	except Exception as B:return f"Terjadi kesalahan: {B}"
@app.route('/videos')
def hVideos():return current_app.response_class(json.dumps(homeVideos(),indent=4),mimetype=_O)
@app.route('/videos/<video_name>')
def sVideos(video_name):
	B='success';A=searchVideos(str(video_name))
	if A==None:return jsonify({B:_J,_D:'Not found'})
	else:return current_app.response_class(json.dumps({B:_A,_D:'Success 200',_B:A},indent=4),mimetype=_O)
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
	B='\n  _____ ___   ___  _     ____  \n |_   _/ _ \\ / _ \\| |   / ___| \n   | || | | | | | | |   \\___ \\ \n   | || |_| | |_| | |___ ___) |\n   |_| \\___/ \\___/|_____|____/ \n                               ';print(_G);print(B);print('1. Cuaca ⌜ ɴᴀᴍᴀ/ᴅᴀᴇʀᴀʜ ⌟');print('2. Encrypt ⌜ ᴄᴏᴅᴇ ⌟');print('3. CekNik ⌜ ɴɪᴋ ⌟');print('4. Decrypt ⌜ ᴄᴏᴅᴇ ⌟');A=int(input(_P))
	if A==1:C=input('Masukkan Daerah: ');cuaca(C)
	elif A==2:D=input(' Code: ');enc(D)
	elif A==3:E=input('Masukkan Nik: ');ceknik(E)
	elif A==4:F=input('Masukkan Code: ');G=deobfuscate_code(F);print(G)
def ceknik(nik):import requests as B,json;C=nik;D=f"https://skizo.tech/api/checknik?apikey=sell%20aja&nik={C}";E=B.get(D);A=json.loads(E.text);print(f"Nik: {A[_D][_F]['nik']}");print(f"Kelamin: {A[_D][_F]['jk']}");print(f"Tanggal Lahir: {A[_D][_F]['tgl']}");print(f"Kabupaten: {A[_D][_F]['kab']}");print(f"Kecamatan: {A[_D][_F]['kec']}");print(f"Provinsi: {A[_D][_F]['prov']}");print(f"Di Ubah Tanggal: {A[_D][_F]['modified_time']}");print(f"[31mSource: {A[_D][_F]['source']}"+Style.RESET_ALL)
def cuaca(daerah):import requests as A;B=f"https://wttr.in/{daerah}";C=A.get(B);print(C.text)
def enc(code):import requests as A,json;clear_console();B='\n      _____ _   _  ____ ______   ______ _____ \n | ____| \\ | |/ ___|  _ \\ \\ / /  _ \\_   _|\n |  _| |  \\| | |   | |_) \\ V /| |_) || |  \n | |___| |\\  | |___|  _ < | | |  __/ | |  \n |_____|_| \\_|\\____|_| \\_\\|_| |_|    |_|  \n                                           ';print(B);C=f"https://api.shannmoderz.xyz/tools/encrypt?key=sell&query={code}";D=A.get(C);E=json.loads(D.text);F=f"{E[_B]}";print(F)
def deobfuscate_code(code):
	B='https://deobfuscate.io/';C=requests.Session();A=C.get(B);D={'input':code};A=C.post(B,data=D)
	if A.status_code==200:return''+A.text
	else:return f"Error: {A.status_code}"
def menu_ai():
	B='\n __  __ _____ _      _ _   _      _    ___ \n |  \\/  | ____| \\ | | | | |            / \\  |_ _|\n | |\\/| |  _| |  \\| | | | |  _____    / _ \\  | | \n | |  | | |___| |\\  | |_| | |_____|  / ___ \\ | | \n |_|  |_|_____|_| \\_|\\___/          /_/   \\_\\___|\n                                                 \n    ';print(B);print(_G);print('1. BlackboxAi ⌜ ɪɴ ᴜᴘᴅᴀᴛᴇ ⌟');print('2. AliciaAi ⌜ ǫᴜᴇʀʏ ⌟');print('3. BocchiAi ⌜ ǫᴜᴇʀʏ ⌟');print('4. ZettaAi ⌜ ǫᴜᴇʀʏ ⌟');print('5. GptLogic ⌜ ǫᴜᴇʀʏ ⌟');print('6. Text2Img ⌜ ᴛᴇxᴛ ⌟');print('7. GoodyAi ⌜ sᴇᴀʀᴄʜ ⌟');print('8. LeptonAi ⌜ sᴇᴀʀᴄʜ ⌟');print('9. YouSearch ⌜ sᴇᴀʀᴄʜ ⌟');print('10. Aoyo ⌜ sᴇᴀʀᴄʜ ⌟');print('11. ProdAi ⌜ sᴇᴀʀᴄʜ ⌟');print('12. Gemini ⌜ ǫᴜᴇʀʏ ⌟ ');A=int(input(_P))
	if A==1:blai()
	elif A==2:ai2()
	elif A==3:bocchiai()
	elif A==4:zettaai()
	elif A==5:gptlogic()
	elif A==6:C=input('Masukkan Untuk File Di Simpan, Enter For [ Default ] : ');txt2img(C)
	elif A==7:goodyai()
	elif A==8:lepton()
	elif A==9:searchh()
	elif A==10:aoyo()
	elif A==11:prod()
	elif A==12:gemini()
def ai(pertanyaan):
	import requests as B;from bs4 import BeautifulSoup as C;D=f"https://blackbox.ai/?q={pertanyaan}";A=B.get(D)
	if A.status_code==200:
		E=C(A.text,'html.parser');F=E.find_all('p')
		for G in F:print(G.text)
	else:print(f"Gagal mengambil data. Status kode: {A.status_code}")
def ai2():
	import requests as B,json
	while _A:
		print(_G);A=input(_E);print(_G)
		if A.lower()==_C:print('Byee...');break
		C=f"https://api.kyuurzy.site/api/ai/alicia?query={A}";D=B.get(C);E=json.loads(D.text);print(f"Alicia: {E[_B]}");'\ndef blai():\n    import requests\n    from bs4 import BeautifulSoup\n    text = input("Query: ") \n    url = \'https://blackbox.ai/?q={}\'.format(text)\n    response = requests.get(url)\n    soup = BeautifulSoup(response.text, \'html.parser\')\n# Contoh: Mengambil semua elemen dengan tag tertentu\n    data = soup.find_all(\'div\', class_=\'class_name\')  # Ganti \'class_name\' dengan nama kelas yang sesuai\n    for item in data:\n        print(item.text)\n'
def goodyai():
	import json,requests as B
	while _A:
		A=input(_E)
		if A.lower()==_C:print('Byee.... ');break
		C=f"https://api.shannmoderz.xyz/ai/goody?key=sell&query={A}";D=B.get(C);E=json.loads(D.text);print('\x1b[31m [ Exit ] For Exits '+Style.RESET_ALL);print(f"[33mGoody: {E[_B]}"+Style.RESET_ALL)
def searchh():
	import json,requests as B
	while _A:
		A=input(_E)
		if A.lower()==_C:print(_H);break
		C=f"https://api.shannmoderz.xyz/ai/yousearch?key=sell&query={A}";D=B.get(C);E=json.loads(D.text);print(_Q+Style.RESET_ALL);print(f"[33mYouSearch: {E[_B]} "+Style.RESET_ALL)
def aoyo():
	import json,requests as B
	while _A:
		A=input(_E)
		if A.lower()==_C:print(_H);break
		C=f"https://api.shannmoderz.xyz/ai/aoyo?key=sell&query={A}";D=B.get(C);E=json.loads(D.text);print(_K+Style.RESET_ALL);print(f"[33mAoyo: {E[_B]}"+Style.RESET_ALL)
		if A.lower()==_C:print(_H);break
def bocchiai():
	import requests as B,json
	while _A:
		A=input(_E)
		if A.lower()==_C:print(_H);break
		C=f"https://api.kyuurzy.site/api/ai/Bocchi?query={A}";D=B.get(C);E=json.loads(D.text);print('\x1b[31m[ Enter ] For Exit'+Style.RESET_ALL);print(f"Bocchi: {E[_B]}")
def gptlogic():
	import json,requests as C
	while _A:
		A=input(_E)
		if A.lower()==_C:print(_H);break
		elif A.lower()=='ai':menu_ai
		D=f"Hai GptLogic, {A}";E=f"https://apikita.exonity.xyz/api/gptlogic?message={D}&prompt=Ubah%20Bahasa%20Mu%20Menjadi%20Indonesia";F=C.get(E);G=F.text;B=json.loads(G);print(_Q+Style.RESET_ALL);print(_R+Style.RESET_ALL)
		if _B in B:print(f"Pertanyaan: {A}\nJawaban: {B[_B]}")
def prod():
	import json,requests as B
	while _A:
		A=input(_E)
		if A.lower()==_C:print(_H);break
		C=f"https://api.shannmoderz.xyz/ai/prod?key=sell&query={A}";D=B.get(C);E=json.loads(D.text);print(_K+Style.RESET_ALL);print(f"[33mProd: {E[_B]}"+Style.RESET_ALL)
def lepton():
	B='Byeee.... ';import json,requests as C
	while _A:
		A=input(_E)
		if A.lower()==_C:print(B);break
		D=f"https://api.shannmoderz.xyz/ai/lepton?key=sell&query={A}";E=C.get(D);F=json.loads(E.text);print(_K+Style.RESET_ALL);print(f"[33mLepton: {F[_B]} "+Style.RESET_ALL)
		if A.lower()==_C:print(B);break
def gemini():
	import json,requests as B
	while _A:
		A=input(_E)
		if A.lower()==_C:print('Byeee... ');break
		C=f"https://apisku-furina.vercel.app/api/ai/gemini?text={A}&apikey=indradev";D=B.get(C);E=json.loads(D.text);print(_K+Style.RESET_ALL);print(f"[33mGemini: {E[_F]}"+Style.RESET_ALL)
def txt2img(file_path='./fitur/Hasil.jpg'):
	A=file_path;import json
	while _A:
		try:
			B=input('Masukkan Text: ')
			if B.lower()==_C:print(' Byee... ');break
			elif B.lower()=='ai':menu_ai();continue
			F=f"https://api.shannmoderz.xyz/ai/txt2img?key=sell&prompt={B}";C=requests.get(F);C.raise_for_status();G=json.loads(C.text);H=G[_B]['url'];D=requests.get(H,stream=_A);D.raise_for_status()
			if A:
				E=os.path.dirname('./fitur/Hasil/Hasil.jpg')
				if not os.path.exists(E):os.makedirs(E)
				with open(A,_I)as I:
					for J in D.iter_content(chunk_size=8192):I.write(J)
				print(f"Gambar berhasil diunduh ke {A}")
			else:print('File path cannot be empty')
		except requests.exceptions.RequestException as K:print(f"Terjadi kesalahan saat mengunduh gambar: {K}")
		print('\x1b[31m[ Exit ] For Exits');print(_R)
def zettaai():
	import requests as B,json
	while _A:
		A=input(_E)
		if A.lower()==_C:break
		C=f"https://api.kyuurzy.site/api/ai/aizeta?query={A}";D=B.get(C);E=json.loads(D.text);print('='*14);print('\x1b[31m[ Enter ] For Exits'+Style.RESET_ALL);print('='*14);print(f"Pertanyaan: {A}\nJawaban Zetta: {E[_B]['answer']}")
def menu_fun():
	C=Fore.RED+'\n       _____ _   _ _   _ \n |  ___| | | | \\ | |\n | |_  | | | |  \\| |\n |  _| | |_| | |\\  |\n |_|    \\___/|_| \\_|\n    Developers: Sell   Teams: Sell | NextTraveller\n   Country: Indonesia                 '+Style.RESET_ALL;print(C);D=Fore.RED+'\n    [ 09 ] For Exit Script\n    [ 99 ] Contact Developers Script\n    [ 01 ] Request Feature To Developers\n    [ 00 ] Back To Main Menu\n    '+Style.RESET_ALL;print(D);print(_G);print('Silahkan Pilih List Di Bawah Ini');print('1. Batu Gunting Kertas');print('2. Apakah ⌜ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ⌟');print('3. Mengapa ⌜ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ⌟');print('4. Kapankah ⌜ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ⌟');print('5. Taugasih');print('6. Kenapasih');print('7. Cantik Cek ⌜ ɴᴀᴍᴀ ⌟');print('8. Lyrics ⌜ ɴᴀᴍᴀ ʟᴀɢᴜ ⌟');print('9. ArtiMimpi ⌜ ᴍɪᴍᴘɪ ᴍᴜ ⌟');A=int(input('Silahkak Pilih Angka Dari List Di Atas\n\x1b[31m=>'+Style.RESET_ALL))
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
	while A not in[_L,_M,_N]:print('Pilihan Tidak Valid');A=input('Silahkan Pilih, Batu, Gunting, Kertas').lower;return A
def komputer_pilih():return random.choice(['Batu','Gunting','Kertas'])
def siapa_pemenang(user_pilih,komputer_pilih):
	B=komputer_pilih;A=user_pilih
	if A==B:return'Serii Mang'
	if A==_L and B==_M or A==_M and B==_N or A==_N and B==_L:return'User Menang! '
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
	return[C[A]for A in A];input(_S);menu_fun()
def cantikcek(nama):A=nama;A=A;B=random.randint(1,100);C=f"⌜ ᴄᴀɴᴛɪᴋ ᴄᴇᴋ ⌟\nɴᴀᴍᴀ: {A}\nᴄᴀɴᴛɪᴋ: {B}%";print(C);input(_S);menu_fun()
def artimimpi(mimpi):
	import requests as C,json;A=mimpi;D=f"https://api.lolhuman.xyz/api/primbon/artimimpi?apikey=c358f182b9f84da3265683cb&query={A}";E=C.get(D);B=json.loads(E.text)
	if _B in B:F=f"Mimpi: {A}\nArti Mimpi: {B[_B]}";print(F);input('Silahkan Enter Untuk Kembali');menu_fun()
def dl():
	F=' [ Path ] => ';E=' [ Url ] => ';print('Haiii {}'.format(nama()));print(_G);H='  ____   _____        ___   _ _     ___    _    ____    \n     |  _ \\ / _ \\ \\      / / \\ | | |   / _ \\  / \\  |  _ \\   \n     | | | | | | \\ \\ /\\ / /|  \\| | |  | | | |/ _ \\ | | | |  \n     | |_| | |_| |\\ V  V / | |\\  | |__| |_| / ___ \\| |_| |  \n     |____/_\\___/_ \\_/\\_/_ |_| \\_|_____\\___/_/   \\_\\____/   \n     |  \\/  | ____| \\ | | | | |                             \n     | |\\/| |  _| |  \\| | | | |                             \n     | |  | | |___| |\\  | |_| |                             \n     |_|  |_|_____|_| \\_|\\___/                              \n                                                        ';print('1. Yt Downloader');print('2. Ig Downloader');print('3. TikTok Downloader [ In Maintenance ]');print('4. TikTok Downloader2');print('5. Aio Downloder ⌜ ᴍᴘ𝟺/ ᴀʟʟ ᴛʏᴘᴇ ʟɪɴᴋ ⌟');C=int(input('Silahkan Masukkan Angka Berdasarkan Code Di Atas\n>× '))
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
	F={_T:_U};B=requests.get(url,headers=F)
	if B.status_code!=200:print(_V);return
	C=re.search(_W,B.text)
	if C:
		H=C.group(1).replace(_X,'/');D=requests.get(url)
		if D.status_code==200:
			E=os.path.join(A,_Y)
			with open(E,_I)as G:G.write(D.content)
			print(f"Video berhasil diunduh ke {E}")
		else:print(_Z)
	else:print('URL video tidak ditemukan.')
def tiktok_downloader(url,output_path='.'):
	A={_T:_U};B=requests.get(url,headers=A)
	if B.status_code!=200:print(_V);return
	C=re.search(_W,B.text)
	if C:
		G=C.group(1).replace(_X,'/');D=os.path.join(output_path,_Y);E=requests.get(G,headers=A,stream=_A)
		if E.status_code==200:
			with open(D,_I)as H:
				for F in E.iter_content(chunk_size=1024):
					if F:H.write(F)
			print(f"Video berhasil diunduh ke {D}")
		else:print(_Z)
	else:print('URL video tidak ditemukan di halaman TikTok.')
def aio2(video_url,output_path):
	C=video_url;B=output_path
	try:
		E=urlparse(C)
		if not E.scheme or not E.netloc:raise ValueError('URL tidak valid')
		D=requests.head(C,allow_redirects=_A);D.raise_for_status();F=D.headers.get('Content-Type','')
		if not F.startswith('video/'):raise ValueError(f"URL tidak mengarah ke file video. Content-Type: {F}")
		H=int(D.headers.get('Content-Length',0));os.makedirs(os.path.dirname(B),exist_ok=_A);G=requests.get(C,stream=_A);G.raise_for_status()
		with open(B,_I)as I,tqdm(desc=os.path.basename(B),total=H,unit='iB',unit_scale=_A,unit_divisor=1024)as J:
			for K in G.iter_content(chunk_size=8192):L=I.write(K);J.update(L)
		print(f"Video berhasil diunduh dan disimpan ke {B}");return _A
	except requests.RequestException as A:print(f"Terjadi kesalahan saat mengunduh video: {A}")
	except ValueError as A:print(f"Kesalahan: {A}")
	except IOError as A:print(f"Terjadi kesalahan saat menyimpan file: {A}")
	except Exception as A:print(f"Terjadi kesalahan yang tidak terduga: {A}")
	return _J
def aio(video_url,output_path):
	B=output_path;A=requests.get(video_url,stream=_A)
	if A.status_code==200:
		with open(B,_I)as D:
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
	print('Selamat {} User'.format(waktuucapan()));print(_G);D='\n    \x1b[34m _   _ _______  _______                                  \n | \\ | | ____\\ \\/ /_   _|                                 \n |  \\| |  _|  \\  /  | |                                   \n | |\\  | |___ /  \\  | |                                   \n |_|_\\_|_____/_/\\_\\_|_|   _______ _     _     _____ ____  \n |_   _|  _ \\    / \\ \\   / / ____| |   | |   | ____|  _ \\ \n   | | | |_) |  / _ \\ \\ / /|  _| | |   | |   |  _| | |_) |\n   | | |  _ <  / ___ \\ V / | |___| |___| |___| |___|  _ < \n   |_| |_| \\_\\/_/   \\_\\_/  |_____|_____|_____|_____|_| \\_\\'+Style.RESET_ALL;print(D);print('1. Addprem');print('2. Delprem');print('3. Backup File Menu');print('4. Backup File Fitur');A=int(input('Masukkan Angka Dari Di Atas => '))
	if A==1:addprem()
	elif A==2:delprem()
	elif A==3:B='menu.py';C='.';bakcup_menu(B,C)
	elif A==4:B='fitur.py';C='.';bakcup_fitur(B,C)
prem=[]
isPrem=_J
def addprem():global prem;global isPrem;A=input('ᴍᴀsᴜᴋᴋᴀɴ ɴᴀᴍᴀ ᴜsᴇʀ: ');B=input('ᴍᴀsᴜᴋᴋᴀɴ ᴜᴍᴜʀ ᴜsᴇʀ: ');print('⌜ ɴᴇxᴛᴛʀᴀᴠᴇʟʟᴇʀ ⌟');prem.append(A);prem.append(B);print(f"ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴅᴀғᴛᴀʀ ᴅᴇɴɢᴀɴ ɪᴅ:\nɴᴀᴍᴀ: ⌜ {A} ⌟\nᴜᴍᴜʀ: ⌜ {B} ⌟\n⌜ ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ʙᴏᴛ ɴᴇxᴛᴛʀᴀᴠᴇʟʟᴇʀ ⌟");isPrem=_A;menu_owner()
def delprem():
	A=input('Masukkan Nama Users Yang Ingin Di Hapus Dev: ');print(' ⌜ ɴᴇxᴛᴛʀᴀᴠᴇʟʟᴇʀ ⌟')
	if A in prem:B=prem.index(A);C=prem[B+1];del prem[B:B+2];print('ᴜsᴇʀ ʙᴇʀɴᴀᴍᴀ {} ʙᴇʀʜᴀsɪʟ ᴅɪ ʜᴀᴘᴜs ᴅᴀʀɪ ᴅᴀᴛᴀʙᴀsᴇ ᴜsᴇʀ ᴘʀᴇᴍ\n『 ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ɴᴇxᴛᴛʀᴀᴠᴇʟʟᴇʀ sᴄʀɪᴘᴛ 』\n⌜ ɴᴇxᴛᴛʀᴀᴠᴇʟʟᴇʀ ⌟'.format(A));D=_J;menu_owner()
def backup_menu(source_file,backup_dir):
	B=backup_dir;A=source_file
	if not os.path.exists(B):os.makedirs(B)
	D=datetime.now().strftime(_a);E=os.path.basename(A);F=f"{E}_{D}";C=os.path.join(B,F);shutil.copy2(A,C);print(f"File {A} berhasil di-backup ke {C}\n⌜ ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ʙᴏᴛ ɴᴇxᴛᴛʀᴀᴠᴇʟʟᴇʀ ⌟");menu_owner()
def bakcup_fitur(source_file,backup_dir):
	B=backup_dir;A=source_file
	if not os.path.exists(B):os.makedirs(B)
	D=datetime.now().strftime(_a);E=os.path.basename(A);F=f"{E}_{D}.py";C=os.path.join(B,F);shutil.copy2(A,C);print(f"File {A} berhasil di-backup ke {C}\n⌜ ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ʙᴏᴛ ɴᴇxᴛᴛʀᴀᴠᴇʟʟᴇʀ ⌟");menu_owner()