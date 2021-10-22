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
	with open(f"series2/{data[0]}.txt", 'w') as fout:
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
	if data[3] == "wallpaper":
		clipit.add_settings(prompts=prompts, aspect=aspect, size=[1920, 1080], iterations=int(data[2]), make_video=True, output=f"series2/{data[0]}.png", num_cuts=20)
	else:
		clipit.add_settings(prompts=prompts, aspect=aspect, ezsize=data[3], iterations=int(data[2]), make_video=True, output=f"series2/{data[0]}.png", num_cuts=30)
	# Apply these settings and run
	settings = clipit.apply_settings()
	clipit.do_init(settings)

	print(f"Run started at {time.ctime()}")
	start_time = time.time()

	clipit.do_run(settings)

	print("--- Done in %s minutes ---" % ((time.time() - start_time) / 60))

