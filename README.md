# PySOI
Python script to pseudo-randomly generate a single-page Excel spreadsheet of Signals Operation Instructions codes from a pool of word lists.

Based on [this video](https://youtu.be/4NXhUyqf7ZM) by Lightfighters Anonymous.

# Setting up

Install the necessary libraries:

```
pip install xlsxwriter
```

# Usage
1) Run the script. Example:

	```
	python pysoi.py 12
	```

	The `12` refers to the number of sheets to generate.

2) Type/paste a seed into the prompt or hit ENTER for a random seed.

3) If the script is successful, a .xlsx spreadsheet will have been created alongside the script.