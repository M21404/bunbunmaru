
# Bunbunmaru

Converts website specified by url into a markdown file. Useful for class notes website.

## Usage

### Run from Binaries
Download the respective binaries depending on your platform.
- Windows: ```dist/bbm.exe```
- Linux: ```dist/bbm```

### Run from Source

```python
pip install -r requirements.txt
py bbm.py ./sample.md https://www.newyorker.com/books/page-turner/thoreau-in-love
```

## Development

Pyinstaller will automatically build the executable for the platform you are on.

### Creating Binaries
```python
pip install pyinstaller
pyinstaller -F --paths=venv/Lib/site-packages  bbm.py
```

## TODO

- [] Image support
- [] OSX Support
- [] Check support for major news sites