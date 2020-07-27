# Face-Recognition

## Vscode 建立 workspace

安裝 pip, conda 以利安裝 python 套件到 編譯器裡面

1. [Data Science in Visual Studio Code](https://code.visualstudio.com/docs/python/data-science-tutorial)
    - Check: `pip -V`

1. [Install Jupiter](https://github.com/Microsoft/vscode-python/blob/master/PYTHON_INTERACTIVE_TROUBLESHOOTING.md)
    - 

1. Coding Style Format
  - [PEP 8](https://swf.com.tw/?p=1229)

## python virtual env

1. Select Python Interpreter
    1. python 3.7
1. install virtualenv [node_module_name]
    1. activate the virtual environment
    ```
    ## windows -activate
    {virtual env name}\Scripts\activate
    ## deactivate
    deactivate
    ```
    * like the node_module in npm
1. install jupyter for jupiter
    - `pip install jupyter`
1. open Python Interactive

[Virtual Env](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)

## python 版本的 package.json

1. Where are the installed packages?
    ```python
    ## Global site-packages
    python -m site 
    ## Per user, where Python installs the local packages
    python -m site --user-site
    ```
1. Export the packages list
    ```python
    ## list installed packages
    pip list
    ## Export installed packages
    pip freeze --local > requriements.txt
    ```
1. New Project want to restore the packages from requirements.txt
    1. install pip
    ```python
    python get-pip.py
    ```
    1. Restore
    ```python
    pip install -r requirements.txt --force-reinstall
    ## `--force-reinstall`: Reinstall all packages even if they are already up-to-date.
    pip install -r requirements.txt --ignore-installed
    ## `--ignore-installed`: Ignore the installed packages/files
    ```

Refer: https://karatejb.blogspot.com/2017/09/python-pip-export-package-list-and.html