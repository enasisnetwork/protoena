


from io import BytesIO
from pathlib import Path

from encommon.colors import Color

from wand.image import Image
from wand.color import Color as Wolor

from weasyprint import HTML



starts = {
    'gray': 'E9E9E9',
    'red': 'FF6666',
    'orange': 'FF9900',
    'yellow': 'FFFF66',
    'lime': '00FF00',
    'green': '66FF66',
    'cyan': '66FFFF',
    'turqos': '66FFDD',
    'blue': '66DDFF',
    'booli': '089BD8',
    'purple': 'CC00FF',
    'pink': 'FF00CC'}



output = (
    Path(__file__).parent
    / 'palette.png')

common = (
    Path(__file__).parent
    / 'static/common.css')

image = (
    Path(__file__).parent
    / 'static/image.css')



colors = {}

for name, start in starts.items():

    color = Color(start)

    _colors = []

    for count in range(6):

        _lev = 6

        if count == 1:
            _lev = 2.5

        if count == 2:
            _lev = 3.7

        if count == 3:
            _lev = 4.5

        if count == 4:
            _lev = 4.8

        if count == 5:
            _lev = 5.5

        hue = color.hsl[0]
        sat = color.hsl[1] - (count * (color.hsl[1] / 12))
        lev = color.hsl[2] - (count * (color.hsl[2] / _lev))

        _color = Color.from_hsl(
            hue, sat, lev)

        _colors.append(_color)

    _colors[0] = color

    print(name.upper(), [
        str(x)[1:]
        for x in _colors])

    colors[name] = _colors



total = len(list(colors.values())[0])


element = '<table><thead><tr>'

for name in colors:
    element += f'<th>{name}</th>'

element += '</tr></thead><tbody>'


for row in range(total):

    element += '<tr>'

    for color in colors.values():
        _color = color[row]
        element += (
            '<td style="'
            f'background-color:{_color};'
            f'">{str(_color)[1:]}</td>')

    element += '</tr>'

element += '</tbody></table>'



html_string = f"""
    <link rel="stylesheet" href="file://{common}">
    <link rel="stylesheet" href="file://{image}">
    {element}
    """



tempfile = BytesIO()
html = HTML(string=html_string)
html.write_pdf(tempfile)
tempfile.seek(0)



with Image(
    file=tempfile,
    resolution=300
) as img:
    img.trim(Wolor('transparent'))
    img.format = 'png'
    img.save(filename=str(output))
