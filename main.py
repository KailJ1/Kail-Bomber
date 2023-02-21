from tools import tools
from tools import proxy
from termcolor import colored
import requests

# █░▄▀ ▄▀▄ ▀ █░░     █▀▄ ▄▀▄ █▄░▄█ █▀▄ █▀▀ █▀▀▄ 
# █▀▄░ █▀█ █ █░▄     █▀█ █░█ █░█░█ █▀█ █▀▀ █▐█▀ 
# ▀░▀▀ ▀░▀ ▀ ▀▀▀     ▀▀░ ░▀░ ▀░░░▀ ▀▀░ ▀▀▀ ▀░▀▀  
#  https://t.me/Kail_J1 | https://vk.com/Kail_J                      

# В этом проекте 1592 строки,
# Если вы считаете user_agent.py и services.jason,
# тогда будет 2267 строк,
# Вау, верно??

tools.clear()
tools.ICC()
tools.clear()
tools.check_files()
tools.CFU()
tools.CTF()

while True:
	tools.clear()
	tools.banner()
	tools.banner_tools()

	try:
		tool = input(colored("\n~# ", "blue"))
	except KeyboardInterrupt:
		continue
	if tool == "1":
		numb, ct, pr = tools.start_input()
		if numb != 0:
			tools.start(numb, ct, proxy_=pr)
	elif tool == "0":
		tools.clear()
		break
	elif tool == "99":
		tools.banner_info()
	elif tool == "2":
		tools.donate()
	elif tool == "3":
		tools.inst_logs()
	elif tool.lower() == "4":
		tools.telebot()
	elif tool.lower() == "clear logs":
		tools.clear_logs()
	elif tool.lower() == "update":
		tools.force_update()
	else:
		pass