# -*- coding: utf-8 -*-
import google.generativeai as genai

# 文字化け
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding = 'utf-8')

GOOGLE_API_KEY = ''
genai.configure(api_key = GOOGLE_API_KEY)

# チャットでの会話
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history = [])
while True:
    prompt = input('あなたの入力内容\n')
    if prompt == 'exit':
        break
    
    response = chat.send_message(prompt, stream = True)
    print("_"*80)
    print('geminiの返答内容')
    for chunk in response:
        print(chunk.text)
    print("_"*80)
