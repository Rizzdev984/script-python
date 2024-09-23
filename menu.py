import os,time,sys
from rich.console import Console
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from datetime import datetime
from colorama import Fore,Style
from fitur.fitur import menu_nsfw,menu_tools,yt,menu_fun,dl,menu_owner,nama_devv,clear_console,menu_ai
console=Console()
def loading2(total=100,delay=.05):
	with Progress(SpinnerColumn(),TextColumn('[progress.description]{task.description}'),BarColumn(),TextColumn('{task.percentage:>3.0f}%'),console=console)as A:
		B=A.add_task('[cyan]Loading...',total=total)
		while not A.finished:A.update(B,advance=1);time.sleep(delay)
user_regis=['Sell','13']
regis=False
def registered():
	global regis;loading2();C='\n      _   _ _______        __  _   _ ____  _____ ____  ____  \n | \\ | | ____\\ \\      / / | | | / ___|| ____|  _ \\/ ___| \n |  \\| |  _|  \\ \\ /\\ / /  | | | \\___ \\|  _| | |_) \\___ \\ \n | |\\  | |___  \\ V  V /   | |_| |___) | |___|  _ < ___) |\n |_| \\_|_____|  \\_/\\_/     \\___/|____/|_____|_| \\_\\____/ \n                                                         ';print('daftar');A=input('Masukkan Nama User ═\x1b[38;2;0;255;189m> ')
	try:B=int(input('Masukkan Umur User ═\x1b[38;2;0;255;189m> '))
	except ValueError:print('Umur Harus Berupa Angka,Bukan Huruf!');return
	user_regis.append(A);user_regis.append(B);print('Berhasil Mendaftarkan Users Dengan Data :\nNama: {}\nUmur: {}'.format(A,B));regis=True
def baca_token_dari_file():
	A='token.txt'
	if not os.path.exists(A):print('File token.txt tidak ditemukan!');return
	with open(A,'r')as B:C=B.read().strip()
	return C
def token():
	A=baca_token_dari_file()
	if A is None:return
	while True:
		B=input('Sebelum Lanjut, Silahkan Masukkan Token NextTraveller: ')
		if B==A:print(Fore.BLUE+'Token Valid!'+Style.RESET_ALL);input('Tekan Enter Untuk Kembali Ke Menu.....')
		else:print(Fore.RED+'Token Tidak Valid. Coba Lagi.'+Style.RESET_ALL)
def del_regis():
	global regis
	if not regis:print('Belum Ada Orang Yang Mendaftarkan Diri');return
	A=input('Masukkan Nama Users')
	if A in user_regis:B=user_regis.index(A);C=user_regis[B+1];del user_regis[B:B+2];print('\x1b[31mUser Yang\nBernama\n{}\nUmur {}\nBerhasil Di Hapus Dari Database NextTraveller'.format(A,C)+Style.RESET_ALL);regis=False
	else:print('User Dengan Nama {} Tidak Di Temukan Di Database NextTraveller'.format(A));print('Silahkan Mulai Ulang Program...');del_regis()
def loading(duration=5):
	E='\x08';A=14;C='/';D='-';sys.stdout.write('[%s]'%(D*A));sys.stdout.flush();sys.stdout.write(E*(A+11))
	for B in range(A+1):time.sleep(duration/A);F=C*B;G=D*(A-B);sys.stdout.write(f"[{F}{G}] {int(B/A*100)}%");sys.stdout.flush();sys.stdout.write(E*(A+7))
	sys.stdout.write(f"[{C*A}] 100%\n")
def waktuucapan():
	C=datetime.now().time();B=C.hour
	if 5<=B<12:A='Selamat Pagi🌅'
	elif 12<=B<15:A='Selamat Siang🌅'
	elif 15<=B<18:A='Selamat Sore🌄'
	else:A='Selamat Malam🌃'
	return A
def operasi_yang_dihitung():time.sleep(2)
def cek():
	if sys.stdout.isatty():return'Console'
	else:return'Terminal'
def runtime():A=time.time();operasi_yang_dihitung();B=time.time();C=B-A;return f"{C:.4f} detik"
def nama():
	try:A=os.getlogin();return A
	except Exception as B:return f"Terjadi kesalahan: {B}"
def menu_list():
	time.sleep(5);B='\n      __  __ _____ _   _ _   _ \n |  \\/  | ____| \\ | | | | |\n | |\\/| |  _| |  \\| | | | |\n | |  | | |___| |\\  | |_| |\n |_|  |_|_____|_|_\\_|\\___/ \n | |   |_ _/ ___|_   _|    \n | |    | |\\___ \\ | |      \n | |___ | | ___) || |      \n |_____|___|____/ |_|      \n                           ';print(B);print('1. Menutools');print('2. MenuOwner');print('3. MenuPremium');print('4. MenuNsfw');print('5. MenuSpam');print('6. MenuFun');print('7. MenuDownload');A=int(input('══\x1b[38;2;0;255;189m> '+Style.RESET_ALL))
	if A==1:menu_tools()
	elif A==2:menu_owner()
	elif A==3:menu_prem()
	elif A==4:menu_nsfw()
	elif A==5:spam()
	elif A==6:menu_fun()
	elif A==7:dl()
def tunggu():
	clear_console();B=Fore.CYAN+'\n    [ 00 ] Exit Script\n    [ 99 ] Contact Developers\n    [ 01 ] Request Feature\n    '+Style.RESET_ALL;print(B);time.sleep(5);print('Haiii {}\nSelamat {}'.format(nama(),waktuucapan()));print('Sebelum Lanjut Ke Menu Silahkan Pilih Liat Di Bawah');C=f"""
 [34m _   _ _______  _______                                  
 | \\ | | ____\\ \\/ /_   _|                                 
 |  \\| |  _|  \\  /  | |                                   
 | |\\  | |___ /  \\  | |                                   
 |_|_\\_|_____/_/\\_\\_|_|   _______ _     _     _____ ____  
 |_   _|  _ \\    / \\ \\   / / ____| |   | |   | ____|  _ \\ 
   | | | |_) |  / _ \\ \\ / /|  _| | |   | |   |  _| | |_) |
   | | |  _ <  / ___ \\ V / | |___| |___| |___| |___|  _ < 
   |_| |_| \\_\\/_/   \\_\\_/  |_____|_____|_____|_____|_| \\_\\
          
          Developers: ⌜ Sell ⌟  Teams: Sell | Traveller
            Running In: {cek()}   ResponSpeed: {runtime()}                          """+Style.RESET_ALL;print(C);print('\n');print('\x1b[31m1. Register'+Style.RESET_ALL);print('\x1b[31m2. Delregis'+Style.RESET_ALL);print('\x1b[31m3. Allmenu [ Harus Regis ]'+Style.RESET_ALL);print('\x1b[31m4. MenuList'+Style.RESET_ALL);print('\x1b[31m5. MenuAi'+Style.RESET_ALL);print('\x1b[31m6. MenuTools'+Style.RESET_ALL);print('\x1b[31m7. MenuFun'+Style.RESET_ALL);A=int(input('Masukkan Angka Di Atas\n══\x1b[38;2;0;255;189m> '+Style.RESET_ALL))
	if A==1:registered()
	elif A==2:del_regis()
	elif A==3:all_menu()
	elif A==4:menu_list()
	elif A==5:menu_ai()
	elif A==6:menu_tools()
	elif A==7:menu_fun()
	else:print('Input Harus Berupa Angka')
if __name__=='__main__':
	while True:tunggu();input('Tekan Enter untuk kembali ke menu...')