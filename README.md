# Rinehart Analysis with Word Vectors<img src='https://avatars.githubusercontent.com/u/90112108' align='right' width='180' height='104'>
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/NLPaladins/rinehartAnalysis_wordVectors/master/LICENSE)

## About  <a name = "about"></a>
**[Project Board](https://github.com/NLPaladins/rinehartAnalysis_wordVectors/projects/1)**, **[Current Issues](https://github.com/NLPaladins/rinehartAnalysis_wordVectors/issues)**, **[Assignment](https://utk.instructure.com/courses/127299/assignments/1074171)**

Rinehart Analysis using Word Vectors for NLP (ECE-617) Project 2.

### Libraries Overview <a name = "lib_overview"></a>

All the libraries are located under [\<project root\>/nlp_libs](https://github.com/NLPaladins/rinehartAnalysis_wordVectors/nlp_libs)
- [\<project root\>/nlp_libs/books](https://github.com/NLPaladins/rinehartAnalysis_wordVectors/nlp_libs/books): This project's code (imported later)
-[\<project root\>/nlp_libs/configuration](https://github.com/NLPaladins/rinehartAnalysis_wordVectors/nlp_libs/configuration): Class that creates config objects from yml files
- [\<project root\>/nlp_libs/fancy_logger](https://github.com/NLPaladins/rinehartAnalysis_wordVectors/nlp_libs/fancy_logger): Logger that can be used instead of prints for text formatting (color, bold, underline etc)

### Where to put the code  <a name = "#putcode"></a>
- Place the preprocessing functions/classes in [nlp_libs/books/preprocessing.py](https://github.com/NLPaladins/rinehartAnalysis_wordVectors/nlp_libs/books/preprocessing.py)
- The custom word embeddings functions/classes (task 1) in [nlp_libs/books/word_embeddings.py](https://github.com/NLPaladins/rinehartAnalysis_wordVectors/nlp_libs/books/word_embeddings.py) (separate class)
- The pretrained word embeddings functions/classes (task 2) in [nlp_libs/books/word_embeddings.py](https://github.com/NLPaladins/rinehartAnalysis_wordVectors/nlp_libs/books/word_embeddings.py) (separate class)
- The functions/classes (if any) that compare the results (tasks 3, 4, 5) in [nlp_libs/books/compare_statistics.py](https://github.com/NLPaladins/rinehartAnalysis_wordVectors/nlp_libs/books/compare_statistics.py)
- Any plotting related functions in [nlp_libs/books/plotter.py](https://github.com/NLPaladins/rinehartAnalysis_wordVectors/nlp_libs/books/plotter.py)

**The code is reloaded automatically. Any class object needs to reinitialized though.** 

## Table of Contents

+ [About](#about)
  + [Libraries Overview](#lib_overview)
  + [Where to put the code](#putcode)
+ [Prerequisites](#prerequisites)
+ [Bootstrap Project](#bootstrap)
+ [Running the code using Jupyter](#jupyter)
      + [Configuration](#configuration)
      + [Local Jupyter](#local_jupyter)
      + [Google Collab](#google_collab)
+ [Adding New Libraries](#adding_libs) 
+ [TODO](#todo)
+ [License](#license)

## Prerequisites <a name = "prerequisites"></a>

You need to have a machine with Python >= 3.9 and any Bash based shell (e.g. zsh) installed.
Having installed conda is also recommended.

```Shell

$ python3.9 -V
Python 3.9.7

$ echo $SHELL
/usr/bin/zsh

```

## Bootstrap Project <a name = "bootstrap"></a>

All the installation steps are being handled by the [Makefile](Makefile).

If you want to use conda run:
```Shell
$ make install
```

If you want to use venv run:
```Shell
$ make install env=venv
```


## Using Jupyter <a name = "jupyter"></a>

### Modifying the Configuration <a name = "configuration"></a>

You may need to configure the yml file. There is an already configured yml file 
under [confs/proj_2.yml](confs/proj_2.yml).

### Local Jupyter <a name = "local_jupyter"></a>

First, make sure you are in the correct virtual environment:

```Shell
$ conda activate rinehartAnalysis_wordVectors

$ which python
/home/<your user>/anaconda3/envs/rinehartAnalysis_wordVectors/bin/python
```

To use jupyter, first run `jupyter`:

```shell
jupyter notebook
```
And open the [main.ipynb](main.ipynb).

### Google Collab <a name = "google_collab"></a>

Just Open this [Google Collab Link](https://colab.research.google.com/github/NLPaladins/rinehartAnalysis_wordVectors/blob/main/main.ipynb).

## Adding New Libraries <a name = "adding_libs"></a>

If you want to add a new library (e.g. a Class) in the project you need to follow these steps:
1. Create a new folder under *"\<project root>/nlp_libs"* with a name like *my_lib*
2. Create a new python file inside it with a name like *my_module.py*
3. Paste your code inside it
4. Create a new file name *__init__.py*
5. Paste the following code inside it:
   ```python
    """<Library name> sub-package."""
    
    from .<Module name> import <Class Name>
    
    __email__ = "jmerlet@vols.utk.edu, kgeorgio.vols.utk.edu, mlane42@vols.utk.edu"
    __author__ = "jeanmerlet, drkostas, LaneMatthewJ"
    __version__ = "0.1.0"
    ```
6. Open [\<project root>/nlp_libs/\_\_init\_\_.py](nlp_libs/__init__.py)
7. Add the following line: ```from nlp_libs.<Module name> import <Class Name>```
8. (Optional) Rerun `make install` or `python setup.py install` 

## TODO <a name = "todo"></a>

Read the [TODO](TODO.md) to see the current task list.

## License <a name = "license"></a>

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


