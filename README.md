
<p align="center">
  <img src="images/logo.png" width=250>
</p>

# hb-config: easy to configure your python packge


hb-config is utility for easy to configure your python package.

## Feature

- Configure set automatically according to the **git branch** name.
- Supports files in three formats: **.json, .yaml, and .conf**
- Access property using **\_\_getattr\_\_** function
- every config data's type is **dict**

## Example

- config.json example

```json
{
    "bot": {
        "in_bot": {
            "in_in_bot": {
                "haha": "hoho"
            },
            "name": "bot_name"
        }
    },
    "token": "test"
}

```

- Handle example

```python
>>> from hbconfig import Config
>>> Config
{
    "bot": {
        "in_bot": {
            "in_in_bot": {
                "haha": "hoho"
            },
            "name": "bot_name"
        }
    },
    "token": "test"
}

>>> Config.bot.in_bot
{
    "in_in_bot": {
        "haha": "hoho"
    },
    "name": "bot_name"
}

>>> Config.token
'test'

>>> Config.bot.in_bot.in_in_bot.haha
'hoho'
```