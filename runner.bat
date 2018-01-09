:loop
python bing_image.py --config="config.json"
reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d C:\Users\Mojtaba\Dropbox\Pictures\Bing\_latest.jpg /f
rundll32.exe user32.dll, UpdatePerUserSystemParameters 1, True
timeout /t 86400
goto loop