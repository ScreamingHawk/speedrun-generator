import sys
sys.path.append("clipit")

import time
print(f"Started at {time.ctime()}")


datas = []
# Import input data
with open('data.csv', 'r') as fin:
	datas = fin.readlines()

import shutil, os

import clipit

for d in datas:
	data = d.strip().split(',')
	if len(data) != 4:
		# Dud line
		continue
	print(d)

	shutil.rmtree('steps')
	os.mkdir('steps')

	# Write info to file
	with open(f"outputs/{data[0]}.txt", 'w') as fout:
		fout.write(d)

	# To reset settings to default
	clipit.reset_settings()
	# You can use "|" to separate multiple prompts
	prompts = f"{data[0]}|{data[1]}"
	print(f"Prompt is {prompts}")
	# You can trade off speed for quality: draft, normal, better, best
	quality = "normal"
	# Aspect ratio: widescreen, square
	aspect = "widescreen"
	# Add settings
	# clipit.add_settings(prompts=prompts, quality=quality, aspect=aspect)
	# clipit.add_settings(prompts=prompts, quality=quality, aspect=aspect, ezsize=data[3], iterations=data[2], make_video=True)
	# clipit.add_settings(prompts=prompts, aspect=aspect, ezsize='small', iterations=5, make_video=False, save_every=1, output=f"outputs/{data[0]}.png")
	# clipit.add_settings(prompts=prompts, aspect=aspect, size=[50, 50], iterations=5, make_video=True, save_every=1, output=f"outputs/{data[0]}.png")
	clipit.add_settings(prompts=prompts, aspect=aspect, ezsize=data[3], iterations=int(data[2]), make_video=True, output=f"outputs/{data[0]}.png")
	# Apply these settings and run
	settings = clipit.apply_settings()
	clipit.do_init(settings)

	print(f"Run started at {time.ctime()}")
	start_time = time.time()

	clipit.do_run(settings)

	print("--- Done in %s minutes ---" % ((time.time() - start_time) / 60))

