# Statbox

Statbox provides useful statistics about your inbox. Currently available as set of CLI-only Python3 scripts.

## Getting Started
Verify that you have Python 3 installed, and `git clone` Statbox onto your computer.
Inside Statbox's folder, create a file named `creds.json` with the following contents:
```json
{
    "username": "youremailaddress@gmail.com",
    "password": "youremailpassword"
}
```

## Running Statbox
`python3 statbox.py`
![Running Statbox](gifs/use.gif)

Once Statbox has been run for the first time, it will create a file labeled `messagedump`. This means that emails do not have to be re-downloaded every time, since Statbox will simply read from this file if it is available. If you want to get the latest information about your inbox, simply delete this file and run Statbox again.

## The Data
Data about your inbox can be found under the `counts/` directory once you have run Statbox.
![Counts](gifs/counts.gif)