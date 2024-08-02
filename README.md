# PySOI
Python script to pseudo-randomly generate a single-page Excel spreadsheet of Signals Operation Instructions codes from a pool of word lists.

Based on [this video](https://youtu.be/4NXhUyqf7ZM) by Lightfighters Anonymous regarding radio encryption.

Current devpath includes adding the callsign section and polishing up the formatting (i.e. learning Xlsxwriter)

# Setting up

Install the necessary libraries:

```
pip install xlsxwriter
```

# Usage
1) Run the script:

```
python pysoi.py
```

2) Type/paste a seed into the prompt or hit ENTER for no seed.

3) If the script is successful, a .xlsx spreadsheet will have been created alongside the script.