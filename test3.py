# -*- coding: utf-8 -*-
import google.generativeai as genai

# 文字化け
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding = 'utf-8')

GOOGLE_API_KEY = ''
genai.configure(api_key = GOOGLE_API_KEY)

import PIL.Image

# 画像とテキスト入力からテキストを生成する
model = genai.GenerativeModel('gemini-pro-vision')
img = PIL.Image.open('images.jpg')
response = model.generate_content(['これは何ですか', img], stream = True)

for chunk in response:
    print(chunk.text)
    print("_"*80)
