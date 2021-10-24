import json
import os
import random

METADATA = json.dumps({
	"description": "Speedrun AI utilizes state of the art machine learning algorithms to generate modern art.\n\n[Image (.png)](ipfs://IPFS_LINK/SUBJECT.png)\n\n[Video (.mp4)](ipfs://IPFS_LINK/SUBJECT.mp4)\n\nSeries 1 combines a hand crafted selection of meaningful prompts provided by the community with various art styles.\nThe iterations are intentionally short to retain the dynamic appeal of AI art and open to work to viewer interpretation.",
	"external_url": "https://speedrunai.nft",
	"image": "ipfs://IPFS_LINK/SUBJECT.png",
	"animation_url": "ipfs://IPFS_LINK/SUBJECT.mp4",
	"name": "SUBJECT",
	"attributes": [
		{
			"trait_type": "Subject",
			"value": "SUBJECT"
		},
		{
			"trait_type": "Style",
			"value": "STYLE"
		},
		{
			"trait_type": "Iterations",
			"value": 999
		},
		{
			"trait_type": "Width",
			"value": 640
		},
		{
			"trait_type": "Height",
			"value": 352
		},
		{
			"trait_type": "Series",
			"display_type": "number",
			"value": "1"
		}
	]
})

fnames = [f for f in os.listdir('series1') if '.txt' in f]
random.shuffle(fnames)

count_style = {}
count_iters = {}

WRITE_METADATA = True

def add_to_count(counts, d):
	if d not in counts:
		counts[d] = 1
	else:
		counts[d] += 1

for i, fname in enumerate(fnames):
	with open(f'series1/{fname}', 'r') as fin:
		data = fin.readline().strip().split(',')
		# Count styles and iterations
		style = data[1] if data[1] else 'automatic'
		add_to_count(count_style, style)
		add_to_count(count_iters, data[2])
		if WRITE_METADATA:
			with open(f"metadata/{i}.json", 'w') as fout:
				fout.write(METADATA
					.replace("999", data[2])
					.replace('SUBJECT', data[0])
					.replace('STYLE', style)
					.replace('IPFS_LINK', 'QmVDU4TUCUd3gbRXku5Ws4N6EukGPLfbJHC5LUEJbqQrsL')
				)

with open('metadata/data.json', 'w') as fout:
	fout.write(json.dumps([{'total': len(fnames)}, count_style, count_iters]))
