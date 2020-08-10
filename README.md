# Statbox

Statbox provides useful statistics about your inbox. Currently available as set of CLI-only Python3 scripts.

## Getting Started
Verify that you have Python 3 installed, and `git clone` Statbox onto your computer.
Inside statbox's folder, create a file named `creds.json` with the following contents:
```json
{
    "username": "youremailaddress@gmail.com",
    "password": "youremailpassword"
}
```

## Running Statbox
`python3 statbox.py`
![Running Statbox](gifs/use.gif)

## The Data
Data about your inbox can be found under the `counts/` directory.