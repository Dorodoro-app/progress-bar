import requests
from cairosvg import svg2png
from tqdm import tqdm


for num in tqdm(range(1, 100)):

    r = requests.get(f"https://progress-bar.dev/{str(num)}")
    xml = r.text
    xml = xml[xml.find('\n')+1:]

    svg2png(bytestring=xml, write_to=f'progress_images/{str(num)}.jpg')
