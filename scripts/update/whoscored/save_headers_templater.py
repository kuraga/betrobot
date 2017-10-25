#!/usr/bin/env python3


import os


input_file_path = os.path.join('scripts', 'update', 'whoscored', 'save_headers.template.js')
headers_file_path = os.path.join('tmp', 'update', 'headers', 'www.whoscored.com.json')
output_file_path = os.path.join('tmp', 'update', 'whoscored', 'save_headers.js')

with open(input_file_path, 'rt', encoding='utf-8') as f_in:
    input_text = f_in.read()

with open(headers_file_path, 'rt', encoding='utf-8') as f_headers:
    headers_text = f_headers.read()

text = input_text.replace('HEADERS_JSON_HERE', headers_text)

with open(output_file_path, 'wt', encoding='utf-8') as f_out:
    f_out.write(text)
