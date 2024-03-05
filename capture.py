from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PIL import Image
import time
import json

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--headless')
config = json.loads(open('./static/config.json', 'r', encoding='utf-8').read())
browser = webdriver.Chrome(service=Service(config["chromedriver_path"]), options=chromeOptions)


def get_one(index, show=False):
    url = f'http://127.0.0.1:5051/{index}'
    browser.get(url)
    time.sleep(1)
    size = browser.get_window_size()
    width = browser.execute_script('return document.getElementById("bg").scrollWidth') + 16
    height = browser.execute_script('return document.getElementById("bg").scrollHeight') + 8
    browser.set_window_size(width, height)
    time.sleep(1)
    browser.get_screenshot_as_file(f'./output_image/{index}.png')
    img = Image.open(f'./output_image/{index}.png')
    img_crop = img.crop(box=(8, 8, width - 12, height - 12))
    img_crop.save(f'./output_image/{index}.png')
    # if show:
        # img.show()
    browser.set_window_size(size['width'], size['height'])
    browser.close()
    print(f'{index}作品截图已保存在output_image目录下。')
    return


if __name__ == '__main__':
    config = json.loads(open('./static/config.json', 'r', encoding='utf-8').read())
    get_one(config["poem_id"], show=True)
