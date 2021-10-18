python3 -m pip install torch==1.9.0+cu102 torchvision==0.10.0+cu102 -f https://download.pytorch.org/whl/torch/ -f https://download.pytorch.org/whl/torchvision/
git clone https://github.com/openai/CLIP
  # !pip install taming-transformers
git clone https://github.com/CompVis/taming-transformers.git
git clone https://github.com/mfrashad/clipit.git
python3 -m pip install ftfy regex tqdm omegaconf pytorch-lightning
python3 -m pip install kornia
python3 -m pip install imageio-ffmpeg   
python3 -m pip install einops
python3 -m pip install torch-optimizer
python3 -m pip install easydict
python3 -m pip install braceexpand
python3 -m pip install git+https://github.com/pvigier/perlin-numpy

  # ClipDraw deps
python3 -m pip install svgwrite
python3 -m pip install svgpathtools
python3 -m pip install cssutils
python3 -m pip install numba
python3 -m pip install torch-tools
python3 -m pip install visdom

python3 -m pip install gradio

git clone https://github.com/BachiLi/diffvg
cd diffvg
  # !ls
git submodule update --init --recursive
python3 setup.py install
cd ..
