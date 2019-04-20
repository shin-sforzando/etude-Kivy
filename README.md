# etude-kivy

- [Requirements](#requirements)
- [How to development on Mac OS](#how-to-development-on-mac-os)
  - [Create virtualenv](#create-virtualenv)
  - [Install dependencies](#install-dependencies)
- [How to Run](#how-to-run)
  - [Popup](#popup)
  - [Misc.](#misc)


## Requirements

* Homebrew
* Python 2.7
  * virtualenv
* Kivy
  
## How to development on Mac OS

### Create virtualenv

```
pip install virtualenv
virtualenv venv
source venv/bin/activate
brew install pkg-config sdl2 sdl2_image sdl2_ttf sdl2_mixer gstreamer
```

### Install dependencies

```
pip install Cython
USE_OSX_FRAMEWORKS=0 pip install kivy
pip install -r requirements.txt
```

## How to Run

### Popup

```
cd popup
python MainApp.py
```

### Misc.
(T.B.D.)
