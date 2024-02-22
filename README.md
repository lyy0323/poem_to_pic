# poem_to_pic
A tool to change poems of guoxue_sjtu into pictures.

## Dependents
Windows system.
You should install the python packages needed.
Besides, you should have installed Chrome and a Chromedriver which relates to the version of your Chrome.

## Usage - Output picture directly
1. Modify the parameters in `static/config.json`.
2. Run `bg.py`, recommended in IDE.
3. Run `capture.py` and wait for a few seconds.
4. Look up for you picture in `output_image` directory.

## Usage - Show different poems with the same background picture in browser
1. Modify the parameters in `static/config.json`.
2. Run `bg.py`E.
3. Turn to `http://127.0.0.1:5051/<poemID>`, in which `<poemID>` is the number of ID of poem on the website of Sinology Association, SJTU.
4. You can turn to other poems by modifying the URL.

## Usage - Import customized background pictures
1. Copy and paste your background picture under `static/background`. Your picture would be recommended to be vertical.
2. Modify the `background` parameter in `static/config.json`.
