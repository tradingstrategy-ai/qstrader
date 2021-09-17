# Trading Strategy QSTrader

This is patched and bug fixed version for [QSTrader library](https://github.com/mhallsmoore/qstrader). This package is a dependency for [tradingstrategy](https://github.com/tradingstrategy-ai/client) package.

The QSTrader project was forked and the fork released on a different PyPi package name `tradingstrategy-qstrader` because the original project by Michael Halls-Moore was unmaintained and unusable as a PyPi package dependency.

[Show package information on PyPi](https://pypi.org/project/trading-strategy-qstrader/).

[For more information see the original QSTrader Github](https://github.com/mhallsmoore/qstrader) and [Trading Strategy website](https://tradingstrategy.ai/).

## Release 

How to release this package on PyPi.

Update `setup.py` version.

```shell
rm -rf dist
python3 -m pip install --upgrade build    
python3 -m build
python3 -m pip install --upgrade twine
python3 -m twine upload dist/*
```

[How to publish Python packages](https://packaging.python.org/tutorials/packaging-projects/)