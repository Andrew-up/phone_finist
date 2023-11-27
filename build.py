import PyInstaller.__main__

PyInstaller.__main__.run([
    'main_ui.py',
    '--noconfirm',
    '--onefile',
    '--noconsole',
    '--icon=logo.ico',
    '-n настройка телефона'
])
