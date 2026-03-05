import urllib.request
import os
import sys

sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
try:
    import pypdf # type: ignore
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pypdf'])
    import pypdf # type: ignore

def extract(pdf_path):
    print(f"Reading {pdf_path}")
    if not os.path.exists(pdf_path):
        return f"File not found: {pdf_path}"
    try:
        reader = pypdf.PdfReader(pdf_path)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n'
        return text
    except Exception as e:
        return f"Error reading {pdf_path}: {str(e)}"

if __name__ == '__main__':
    f1 = '/Users/nishimurataku/Downloads/企業研修プログラム作成について.pdf'
    f2 = '/Users/nishimurataku/Downloads/企業研修モデルケース.pdf'
    
    out = ''
    out += '--- 企業研修プログラム作成について.pdf ---\n'
    out += extract(f1) + '\n\n'
    out += '--- 企業研修モデルケース.pdf ---\n'
    out += extract(f2) + '\n\n'
    
    with open('pdf_contents.txt', 'w', encoding='utf-8') as f:
        f.write(out)
    
    print("Done writing to pdf_contents.txt")
