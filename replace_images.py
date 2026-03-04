import re

html_path = '/Users/kinu/Desktop/tmp/lp-photoadvice/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

def img_to_text(match):
    full_img = match.group(0)
    alt_match = re.search(r'alt="([^"]*)"', full_img)
    src_match = re.search(r'src="([^"]*)"', full_img)
    
    if not src_match:
        return full_img
        
    alt = alt_match.group(1) if alt_match else ""
    src = src_match.group(1)
    
    if 'visual' in src:
        if not alt: alt = 'デジタル一眼レフ 無料講座が選ばれる3つの理由'
        return f'<div class="txt-visual-title">{alt}</div>'
    elif 'btn_01_off' in src:
        if not alt: alt = '無料メール講座に申し込む'
        return f'<span class="txt-btn-01">{alt}</span>'
    elif 'btn_02_off' in src:
        return f'<span class="txt-submit-btn">今すぐ受け取る</span>'
    elif 'title_' in src:
        return f'<h2 class="txt-title-01">{alt}</h2>'
    elif 'subtitle_' in src:
        return f'<h3 class="txt-title-02">{alt}</h3>'
    elif 'image_04' in src:
        return f'<div class="txt-image-04">{alt}</div>'
    elif 'image_06' in src:
        # text was given in alt
        return f'<div class="txt-image-06">{alt}</div>'
    elif 'image_07' in src:
        return f'<div class="txt-image-07">{alt}</div>'
    elif 'note_top' in src:
        return f'<div class="txt-note-top">{alt}</div>'
    elif 'form_title' in src:
        return f'<div class="txt-form-title">{alt}</div>'
        
    return full_img

# pattern to catch specific images
pattern = re.compile(r'<img[^>]*?src="[^"]*?(?:visual|btn_01|btn_02|title_|subtitle_|image_04|image_06|image_07|note_top|form_title)[^"]*?"[^>]*?>', re.IGNORECASE)
new_html = pattern.sub(img_to_text, html)

# Some cleanups for nested buttons
new_html = new_html.replace('style="background-color: #fff1c8;border: none;cursor: pointer;"', 'class="form_submit_wrapper"')
new_html = new_html.replace('<a href="#regist_form"><span class="txt-btn-01">', '<a href="#regist_form" class="txt-btn-01-link"><span class="txt-btn-01">')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)
print("Replaced images with text tags.")
