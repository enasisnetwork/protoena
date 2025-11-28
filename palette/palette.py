


from io import BytesIO
from pathlib import Path

from encommon.colors import Color

from wand.image import Image
from wand.color import Color as Wolor

from weasyprint import HTML



starts = [

    {'red1L': 'FF6666',     # one of six variations of FF/66
     'gren1L': '66FF66',    # one of six variations of FF/66
     'blue1L': '6666FF',    # one of six variations of FF/66
     'yllw1L': 'FFFF66',    # one of six variations of FF/66
     'cyan1L': '66FFFF',    # one of six variations of FF/66
     'pink1L': 'FF66FF',    # one of six variations of FF/66
     'gray1L': 'E9E9E9',
     'orng1L': 'FF9900',
     'blue2L': '66CCFF',
     'mgta1L': 'FF00CC',
     'purp1L': 'CC00FF',
     'turq1L': '66FFCC',
     'gold': 'FFCC00'},

    {'red1D': 'AA0000',
     'gren1D': '00AA00',
     'blue1D': '0000AA',
     'yllw1D': 'AAAA00',
     'cyan1D': '00AAAA',
     'pink1D': 'AA00AA',
     'gray1D': '969696',
     'orng1D': 'AA6600',
     'blue2D': '0066AA',
     'mgta1D': 'AA0066',
     'purp1D': '6600AA',
     'turq1D': '00AA66',
     'booli': '089BD8'}]



output = (
    Path(__file__).parent
    / 'palette.png')

common = (
    Path(__file__).parent
    / 'static/common.css')

image = (
    Path(__file__).parent
    / 'static/image.css')



def build_colors(starts):

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

    return colors



def build_element(colors):

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

    return element



html_string = f"""
<link rel="stylesheet" href="file://{common}">
<link rel="stylesheet" href="file://{image}">
"""

for _starts in starts:

    colors = build_colors(_starts)

    html_string += build_element(colors)



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
