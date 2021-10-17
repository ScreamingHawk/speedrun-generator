import json
import os
import random

METADATA = json.dumps({
	"description": "SpeedrunAI utilizes state of the art machine learning algorithms to generate modern art.\n\n[Image (.png)](ipfs://IPFS_LINK/SUBJECT.png)\n\n[Video (.mp4)](ipfs://IPFS_LINK/SUBJECT.mp4)",
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
			"trait_type": "Size",
			"value": "SIZE"
		},
		{
			"trait_type": "Series",
			"display_type": "number",
			"value": "1"
		}
	]
})

fnames = [f for f in os.listdir('outputs') if '.txt' in f]
random.shuffle(fnames)

for i, fname in enumerate(fnames):
	with open(f'outputs/{fname}', 'r') as fin:
		data = fin.readline().strip().split(',')
		with open(f"metadata/{i}.json", 'w') as fout:
			fout.write(METADATA
				.replace('SUBJECT', data[0])
				.replace('STYLE', data[1])
				.replace("999", data[2])
				.replace('SIZE', data[3])
				.replace('IPFS_LINK', 'IPFS_LINK') #FIXME Correct link
			)
