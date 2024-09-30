


from io import BytesIO
from pathlib import Path

from weasyprint import HTML
from wand.image import Image
from wand.color import Color



output = (
    Path(__file__).parent
    / 'badges.png')

common = (
    Path(__file__).parent
    / 'static/common.css')

colors = (
    Path(__file__).parent
    / 'static/colors.css')

image = (
    Path(__file__).parent
    / 'static/image.css')



html_string = f"""
    <link rel="stylesheet" href="file://{common}">
    <link rel="stylesheet" href="file://{colors}">
    <link rel="stylesheet" href="file://{image}">
    <table class="green">
      <tbody>
        <tr>
          <td>GitHub Actions</td>
          <td>passing</td>
          <td>2024-09-06</td>
        </tr>
      </tbody>
    </table>
    <table class="red">
      <tbody>
        <tr>
          <td>GitHub Actions</td>
          <td>failing</td>
          <td>2024-09-06</td>
        </tr>
      </tbody>
    </table>
    <table class="gray">
      <tbody>
        <tr>
          <td>GitHub Actions</td>
          <td>unknown</td>
          <td>2024-09-06</td>
        </tr>
      </tbody>
    </table>
    <br>
    <table class="green">
      <tbody>
        <tr>
          <td>Coverage</td>
          <td>99%</td>
          <td>2024-09-06</td>
        </tr>
      </tbody>
    </table>
    <table class="yellow">
      <tbody>
        <tr>
          <td>Coverage</td>
          <td>90%</td>
          <td>2024-09-06</td>
        </tr>
      </tbody>
    </table>
    <table class="red">
      <tbody>
        <tr>
          <td>Coverage</td>
          <td>49%</td>
          <td>2024-09-06</td>
        </tr>
      </tbody>
    </table>
    <br>
    <table class="teal">
      <tbody>
        <tr>
          <td>PyPi version</td>
          <td>0.2.0</td>
          <td>2024-09-06</td>
        </tr>
      </tbody>
    </table>
    <table class="blue">
      <tbody>
        <tr>
          <td>PyPi downloads</td>
          <td>150/month</td>
          <td>2024-09-06</td>
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
