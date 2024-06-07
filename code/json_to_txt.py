''' Script to turn JSON formatted QA into text file 
JSON format:
[
    {
        "qid": "8bfbe1756b616ad7099ca99454a9d1a5",
        "ctx": "i have no choice",
        "relation": "Synchronous",
        "choices": [
            "i be a robot with will",
            "she call you",
            "she admit she crime",
            "adt call"
        ],
        "answer": 1
    },
]
'''

import json
import os
import sys

def json_to_txt(json_file, txt_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    print(len(data))
    with open(txt_file, 'w') as f:
        for item in data:
            f.write(f"Q: {item['ctx']}\n")
            f.write(f"R: {item['relation']}\n")
            for i, choice in enumerate(item['choices']):
                f.write(f"{i+1}. {choice}\n")
            f.write(f"A: {item['choices'][item['answer']-1]}\n\n")

if __name__ == '__main__':
    json_file = 'C:/Users/corey/Documents/Benchmarking/.venv/final_paths_08.json'
    txt_file = json_file.replace('.json', '.txt')
    json_to_txt(json_file, txt_file)
