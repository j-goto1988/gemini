# -*- coding: utf-8 -*-
import google.generativeai as genai

# 文字化け
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding = 'utf-8')

GOOGLE_API_KEY = ''
genai.configure(api_key = GOOGLE_API_KEY)

# 使用できるモデルを取得
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)