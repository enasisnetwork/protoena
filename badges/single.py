


from io import BytesIO
from pathlib import Path
from sys import argv

from weasyprint import HTML
from wand.image import Image
from wand.color import Color



output = (
    Path(__file__).parent
    / 'single.png')

common = (
    Path(__file__).parent
    / 'static/common.css')

colors = (
    Path(__file__).parent
    / 'static/colors.css')

fonts = (
    Path(__file__).parent
    / 'static/fonts.css')

image = (
    Path(__file__).parent
    / 'static/image.css')



html_string = f"""
    <link rel="stylesheet" href="file://{common}">
    <link rel="stylesheet" href="file://{colors}">
    <link rel="stylesheet" href="file://{fonts}">
    <link rel="stylesheet" href="file://{image}">
    <table class="{argv[1]}">
      <tbody>
        <tr>
          <td>{argv[2]}</td>
          <td>{argv[3]}</td>
        </tr>
      </tbody>
    </table>
    """



tempfile = BytesIO()
html = HTML(string=html_string)
html.write_pdf(tempfile)
tempfile.seek(0)



with Image(
    file=tempfile,
    resolution=300
) as img:
    img.trim(Color('transparent'))
    img.format = 'png'
    img.save(filename=str(output))
