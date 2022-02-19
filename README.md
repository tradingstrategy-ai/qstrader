# Trading Strategy QSTrader

This is patched and bug fixed version for [QSTrader library](https://github.com/mhallsmoore/qstrader). This package is a dependency for [tradingstrategy](https://github.com/tradingstrategy-ai/client) package.

The QSTrader project was forked and the fork released on a different PyPi package name `trading-strategy-qstrader` because the original project by Michael Halls-Moore was unmaintained and unusable as a PyPi package dependency.

**Warning**: This package is currently under active development to become suitable for crypto trading. APIs are likely to break.

# Installation

```shell
poetry add trading-strategy-qstrader
```

# Information

- [Visit Trading Strategy](https://tradingstrategy.ai)
- [View Trading Strategy documentation](https://tradingstrategy.ai/docs)
- [View package information on PyPi](https://pypi.org/project/trading-strategy-qstrader/)
- [See the original QSTrader repository on Github](https://github.com/mhallsmoore/qstrader)
- [Changelog](https://github.com/tradingstrategy-ai/qstrader/blob/master/CHANGELOG.md)
- [Discord chat](https://tradingstrategy.ai/community#discord)

# Compatibility

Since version 0.4 internals have been reworked to be compatible with crypto trading. This version is unlikely to work with stock markets anymore and the development has diverged

# Release 

How to release this package on PyPi.

Update `setup.py` version.

```shell
rm -rf dist
python3.9 -m venv venv
source venv/bin/activate
pip install -U pip
pip install --upgrade build    
python3 -m build
pip install --upgrade twine
python3 -m twine upload dist/*
```

[How to publish Python packages](https://packaging.python.org/tutorials/packaging-projects/)
