# About Bytestat

This program parses and outputs  information about how much  once a file is encountered every byte.

# Requires
* Python 3
* PyQT4 library

# Usage

To start the application, go to its directory and type

```
python bytestat.py
```

# GUI compilation

You can edit the ./qt_designer/*.ui files and recompile them by entering the following command

```
pyuic4 ./qt_designer/gui_about.ui -o ./gui/gui_about.py
pyuic4 ./qt_designer/gui_alert.ui -o ./gui/gui_alert.py
pyuic4 ./qt_designer/gui_main.ui -o ./gui/gui_main.py
pyuic4 ./qt_designer/gui_result.ui -o ./gui/gui_result.py
```

# License

System provided under GPLv.3 license. See LICENSE file for more details.

# Author

Erik Lotin, https://github.com/eriklotin

2012-10
