
# Aapki Pehchaan
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FMLToolTech%2Faapki-pehchaan&count_bg=%23009CEA&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

This is Adhaar card printing tool.This application extracts the information from Adhaar card pdf and assemble it in CR80 card size.
### Features:
- Various card customization options.(Enable/Disable Card Elements like Header, Footer, Barcode, Photobox etc).
- Font Adjustment option for native texts.

## Demo
![Watch the video](/assets/Demo.gif)

## FastAPI
This project makes use of fastapi for backend tasks.
1. Install FastAPI:
    `pip install fastapi`
2. You will also need an ASGI server, for production such as Uvicorn:
    `pip install uvicorn`
3. Run it:
    `uvicorn main:app --reload`
  
## Heroku
1. Run this command to deploy app on cloud:
    `heroku apps:info --app example`
    
## Create an exe
1. Install pyinstaller
    `pip3 install pyinstaller`

2. Create exe
    `pyinstaller --icon="images\logo.ico" index.py --onefile`

## References

 - https://medium.com/@mounirboulwafa/creating-a-single-executable-file-exe-from-a-python-program-abda6a41f74f
 - https://fastapi.tiangolo.com/
 - https://devcenter.heroku.com/articles/using-the-cli

