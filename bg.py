import json
from flask import Flask, render_template
from PIL import Image
import requests

app = Flask(__name__)


@app.route('/<poemID>')
def index(poemID):
    config = json.loads(open('./static/config.json', 'r', encoding='utf-8').read())
    img_src = './static/background/' + config['background']
    poem_raw = requests.get(config['guoxue_sjtu_url'] + 'api/poem/' + poemID).text.replace('\\n', '<br>').replace('#', '<tag>')
    if not poem_raw:
        return render_template('404.html')
    else:
        poem = eval(poem_raw)
        poem[4] = poem[4].replace('<br>', '\n')
        if poem[5]:
            poem[5] = [foo.replace('<tag>', '#') for foo in poem[5]]
    sizes = {(9, 16): (720, 1280), (3, 4): (960, 1280), (2, 3): (960, 1440)}
    sizes_inverse = {(720, 1280): (9, 16), (960, 1280): (3, 4), (960, 1440): (2, 3)}

    def resize(src):
        img = Image.open(src)
        w = img.size[0]
        h = img.size[1]
        if w / h < 0.6:
            size = (9, 16)
            resized = img.resize(sizes[size])
        elif w / h < 0.7:
            size = (2, 3)
            resized = img.resize(sizes[size])
        else:
            size = (3, 4)
            resized = img.resize(sizes[size])
        resized.save('./static/background/' + src.split('/')[-1].split('.')[0] + '_resized.png')
        return './static/background/' + src.split('/')[-1].split('.')[0] + '_resized.png'

    def parse_lines(poem, mxchar):
        sums = 0
        sums += (len(poem[1]) - 1) // mxchar
        sums += 2.2
        paras = poem[4].split('\n')
        if poem[0] == '诗':
            sums += 1.2 * len(paras)
        else:
            for para in paras:
                sums += (len(para) + 1) // mxchar * 1.2
        return sums

    img = Image.open(img_src)
    style_text = ''
    if img.size not in sizes.values():
        img_src = resize(img_src)
        img = Image.open(img_src)
    linespace_multiplier = img.size[1] / img.size[0] / 1.6
    if poem[0] == '诗':
        textlines = poem[4].split('\n')
        font_size = img.size[0] / (4 + min(18, max(len(poem[0]) * 1.5, max([len(_) for _ in textlines]))))
        mxchar = min(18, max(len(poem[1]) * 1.5, max([len(_) for _ in textlines])))
    else:
        textlines = poem[4].split('\n')
        font_size = img.size[0] / max(20, len(poem[1]) * 1.5)
        mxchar = 16
    line_count = parse_lines(poem, mxchar)
    if line_count < 8: line_count = 8
    style_text += f'''#ptitle{{line-height: {1.5 * 13.5 / line_count * linespace_multiplier}em; text-align: center; font-family: 义启小魏楷; font-size: 1.3em}}
        #pauthor{{line-height: {1.7 * 12 / line_count}em; text-align: center; font-family: 楷体}}
'''
    if poem[0] == '诗':
        style_text += f'\n        #pcontent{{line-height: {1.2 * 13.5 / line_count * linespace_multiplier}em; text-align: center; font-family: 仿宋; margin: 0 -0.3em 0 0.3em}}'
        poemContent = poem[4].replace('\n', '<br>')
    else:
        style_text += f'\n        #pcontent{{line-height: {1.2 * 13.5 / line_count * linespace_multiplier}em; text-align: justify; font-family: 仿宋}}'
        poemContent = '<p style="margin:0 0 0.5em 0; text-indent: 2em">' + poem[4].replace('\n', '</p><p style="margin:0 0 0.5em 0; text-indent: 2em">') + '</p>'
    tt = poem[1]
    if len(tt) == 2: tt = tt[0] + ' ' + tt[1]
    at = poem[2]
    if len(at) == 2: at = at[0] + ' ' + at[1]
    return render_template('poem_template.html', poem=poem, style_text=style_text, font_size=font_size,
                           max_width=img.size[0] - 2 * font_size,
                           w=img.size[0],
                           h=img.size[1],
                           tt=tt,
                           at=at,
                           poemContent=poemContent,
                           bg_name=img_src.split('/')[-1],
                           mask_name='mask_' + str(sizes_inverse[img.size][0]) + '_' + str(sizes_inverse[img.size][1]) + '.png')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5051, debug=True)

