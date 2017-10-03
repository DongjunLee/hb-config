
<p align="center">
  <img src="images/logo.png" width=250>
</p>

<p align="center">

  <a href="https://github.com/DongjunLee/kino-bot">
    <img src="https://img.shields.io/badge/Python3.6-Config-brightgreen.svg" alt="Project Introduction">
  </a>

  <a href="https://badge.fury.io/py/hb-config">
    <img src="https://badge.fury.io/py/hb-config.svg" alt="PyPI version" height="18">
  </a>

  <br/>

  <a href="https://travis-ci.org/badges/shields">
    <img src="https://travis-ci.org/DongjunLee/hb-config.svg?branch=master" alt="build status">    
  </a>
  <a href="https://requires.io/github/DongjunLee/hb-config/requirements/?branch=master">
    <img src="https://requires.io/github/DongjunLee/hb-config/requirements.svg?branch=master" alt="Requirements Status" />
  </a>
 <a href='https://dependencyci.com/github/DongjunLee/hb-config'>
   <img src='https://dependencyci.com/github/DongjunLee/hb-config/badge' alt='Dependency Status' />
 </a>

  <br/>

  <a href="https://codecov.io/gh/DongjunLee/hb-config">
    <img src="https://codecov.io/gh/DongjunLee/hb-config/branch/master/graph/badge.svg" alt="Codecov" />
  </a>

  <a href="https://www.codacy.com/app/humanbrain.djlee/hb-config?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=DongjunLee/hb-config&amp;utm_campaign=Badge_Grade">
    <img src="https://api.codacy.com/project/badge/Grade/c47cdac8f087492aaeb593bd68ca2f3f"/>
  </a>


</p>

# hb-config: easy to configure your python packge


hb-config is utility for easy to configure your python package.  
Do not use any **boilerplate code**.

## Feature

- Supports files in three formats: **.json and .yaml**
- Access property using **\_\_getattr\_\_** function ```Config.TOKEN```
- Edit property using **\_\_setattr\_\_** function ```Config.TOKEN = "{token}"```
- every config data's type is **dict**
- Config instance is Singleton.

## Install

using pip

```
$ pip install hb-config
```

or clone repository

```
python setup.py install
```

## Example

- config3.yml example

```yml
project: hb-config
example: true
bot:
  in_bot:
    test: haha
    simple: wow
```

- Handle example

```python
>>> from hbconfig import Config
>>> Config("config3")
>>> Config
Read config file name: config3.yml
{
    "project": "hb-config",
    "example": true,
    "bot": {
        "in_bot": {
            "test": "haha",
            "simple": "wow"
        }
    }
}

>>> Config.bot.in_bot
{
    "test": "haha"
    "simple": "wow"
}

>>> Config.project
'hb-config'

>>> Config.bot.in_bot.simple
'wow'
```
