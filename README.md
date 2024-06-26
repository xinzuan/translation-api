## Preparation
1. Set up the environment

```
    conda env create -f environment.yml
    conda activate translation

    pip install fastapi

```

The environment is tested on: 
```
    Nvidia driver: 525.147.05
    cuda version: 12.0
    cudnn version: 8.9.2
```
## How to run
Fast api will run in port **7795**
```
    python main.py
```

or you can try it locally (without fastapi) by just run below command:
```
    python main_local.py
```


## Supported language
Note that **traditional chinese** is not supported in current api

You can check the supported languages in **constant.py**
