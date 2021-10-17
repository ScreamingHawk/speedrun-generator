https://colab.research.google.com/github/mfrashad/text2art/blob/main/text2art.ipynb#scrollTo=45IGBVWej4n7
https://towardsdatascience.com/how-i-built-an-ai-text-to-art-generator-a0c0f6d6f59f

Also fix for windows:

pip install moviepy

https://github.com/BachiLi/diffvg/issues/12#issuecomment-917303306

http://gnuwin32.sourceforge.net/packages/wget.htm

If there are SSL error in wget, download the files manually and move them to the correct `models` dir and filename:
Download https://heibox.uni-heidelberg.de/d/a7530b09fed84f80a887/files/?p=%2Fckpts%2Flast.ckpt&dl=1 to models/vqgan_imagenet_f16_16384.ckpt
Download https://heibox.uni-heidelberg.de/d/a7530b09fed84f80a887/files/?p=%2Fconfigs%2Fmodel.yaml&dl=1 to models/vqgan_imagenet_f16_16384.yaml
