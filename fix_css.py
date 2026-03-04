import re

css_path = '/Users/kinu/Desktop/tmp/lp-photoadvice/css/lp.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace font-size: 20px !important; line-height: 2.0 !important;
css = re.sub(r'font-size:\s*20px\s*!important;', 'font-size: 16px !important;', css)
css = re.sub(r'line-height:\s*2\.0\s*!important;', 'line-height: 1.8 !important;', css)

# Replace form text font sizes 18px -> 16px
css = re.sub(r'font-size:\s*18px\s*!important;', 'font-size: 16px !important;', css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("CSS updated.")
