# poem_to_pic
A tool to change poems of guoxue_sjtu into pictures.

## Dependents
Windows system.
You should install the python packages needed, including `flask`, `pillow` and `selenium`.
Besides, you should have installed Chrome and a Chromedriver which relates to the version of your Chrome.

## Usage - Output picture (local)
1. Modify the parameters in `static/config.json`.
2. Run `bg.py`, recommended in IDE.
3. Run `capture.py` and wait for a few seconds.
4. Look up for you picture in `output_image` directory.

## Usage - Render poem pictures with the same background picture in browser (local)
1. Run `bg.py`.
2. Turn to `http://127.0.0.1:5051/submit/`.
3. Fill in the form and click `提交`. Note that you should click the button *after* the picture you've selected has been loaded.
4. The result will be rendered in the page.

## Usage - Online copy
Address: `http://139.224.229.170:5051/submit/`
