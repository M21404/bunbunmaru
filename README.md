
# Bunbunmaru

Converts website specified by url into a markdown file. Useful for class notes website.

## Usage

### Run from Binaries
Download the respective binaries depending on your platform.
- Windows: ```dist/bbm.exe```
- Linux: ```dist/bbm/bbm```

### Run from Source

```python
git clone https://github.com/m21404/bunbunmaru.git
cd bunbunmaru/
pip3 install -r requirements.txt
python3 bbm.py ./sample.md https://www.newyorker.com/books/page-turner/thoreau-in-love
```

## Development

Pyinstaller will automatically build the executable for the platform you are on.

### Creating Binaries
- Windows:
```python
pip3 install pyinstaller
pyinstaller -F --paths=venv/Lib/site-packages bbm.py
```
- Linux:
```python
pip3 install pyinstaller --user
pyinstaller bbm.py
```


## TODO

- [ ] Image support
- [ ] OSX Support
- [ ] Check support for major news sites
