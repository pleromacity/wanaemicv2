import zipfile
import re
import pathlib
path = pathlib.Path(r'c:/Users/Public/wanaemicv/cv addon.docx')
with zipfile.ZipFile(path, 'r') as z:
    xml = z.read('word/document.xml').decode('utf-8')
    texts = re.findall(r'<w:t[^>]*>(.*?)</w:t>', xml)
    extracted = ' '.join(texts)
with open(path.parent / 'cv_addon_text.txt', 'w', encoding='utf-8') as out:
    out.write(extracted)
print('Written cv_addon_text.txt')
