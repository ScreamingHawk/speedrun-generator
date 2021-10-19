import random
import requests

# weighted chance of iterations
iterations = [50, 50, 100, 50, 100, 200, 50, 100, 200, 300, 50, 100, 200, 300, 500]
# style
styles = [
	# 'deviantart',
	# 'artstation',
	# 'low poly',
	'watercolor',
	'pencil sketch',
	'painting',
	# 'painting',
	# 'made of wire',
	# 'woodcut',
	# 'surrealist',
	'smooth',
	# 'comic book',
	# 'steampunk',
	# 'minimalist',
	# 'vector',
	'',
]
# sizes
sizes = ['large']

wordlist = []

with open('discord.txt', 'r') as fin:
	with open('data.csv', 'w') as fout:
		for line in fin.readlines():
			if len(line.split(' ')) > 1:
				# Ignore these
				continue
			# Format
			line = line.split(',')[0].strip().lower()
			if line in wordlist:
				# Duplicate
				continue
			wordlist.append(line)
			print(f"Checking {line}")
			# Dictionary look up
			try:
				resp = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{line}")
				if resp.status_code != 200:
					print(f"{line} is not a word")
					continue
				defs = resp.json()
				if defs[0]['meanings'][0]['partOfSpeech'] != 'noun':
					print(f"{line} is not a noun")
					continue
			except:
				print(f"Error getting {line} dictionary result. Skipping")
				continue
			# Randomise other metadata
			style = random.choice(styles)
			iters = random.choice(iterations)
			size = random.choice(sizes)
			fout.write(f"{line},{style},{iters},{size}\n")

