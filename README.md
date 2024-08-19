# PySOI
Python script to pseudo-randomly generate a single-page Excel spreadsheet of Signals Operation Instructions codes from a pool of word lists.

Based on [this video](https://youtu.be/4NXhUyqf7ZM) by Lightfighters Anonymous.

# Setting up

Install the necessary libraries:

```
pip install xlsxwriter
```

# Using the Script

1) Download the script and the `soi-lists` folder with the requisite word list text files:

	Click `<> Code ▼` > ` Download ZIP`

2) Run the script. Example:

	```
	python pysoi.py 12
	```

	The `12` refers to the number of sheets to generate.

3) Type/paste a seed into the prompt or hit ENTER for a random seed.
	
	A good way to get a cryptographically secure seed is to copy and paste large numbers from `random.org` or generate a large number from a hardware random number generator. As it happens, you can use my [OpenOTP32](https://github.com/emergencyrussell/OpenOTP32/) to print off a whole sheet of random numbers generated from an ESP32, or you can save thermal paper and just use an ESP32 to generate random numbers in the serial port.

4) If the script is successful, a .xlsx spreadsheet will have been created alongside the script.

# Usage

*Note: This is a work in progress. It may be necessary to amend the word lists for clarity, brevity, and to increase the pool of codewords and categories.*

Communications security is a vital organ of any covert operation. Your wife will not be impressed by your operational discipline if her SIGINT team intercepts your unencoded radio coms directing her surprise birthday party in plain English. In order to maintain the element of surprise, it is necessary to encode key words or phrases with our team so that they can operate in the comfort of a private language. One way to achieve this private language is by distributing codebooks among the team that transfer the meaning of our communications among innocuous, easily understood codewords.

## Orders/Status

Your operations center will need to direct your field teams in order to achieve objectives. Your team in the field will need to communicate to the operations center about what they are doing.

## SITREP

Is your team in need of an evac at the cake shop parking lot? Are they running low on streamers? They can communicate the status of their situation or resources using this section.

## RESOURCE

The supplies and equipment needed for the operation.

## Position

Where your teams, targets, locations, objectives, etc. are in relation to each other.

## Location

Names of locations in relation to your operation's goals.

## AUTHENTICATION TABLE

### SARNEG

You want to be sure the person on the other side of the iPhone is your buddy Carl and that he is not under duress or the immediate supervision of Blabbermouth Becky who will spill the spinach in half a heartbeat. The SARNEG word is a word or compound of words made of non-repeating letters paired with a number 0-9. To make sure you're talking to the right person and that they are not compromised, choose a letter or number and have the other end of the line match that letter or number with the corresponding number or letter. If they have the same SARNEG word, they'll be able to authenticate themselves. If they fail the authentication three times, you know it's time to burn the SOI and move to the next one, if not an entire new SOI book.

	"Carl, this is Hank, authenticate B. Over"
	
	"Hank, this is Carl. Four."

### ALT FREQ / ALT SOI

ALT FREQ is used for radio communications. If your threat model is low stakes, like your wife discovering her surprise birthday party, you may want to develop a section dedicated to different messaging apps on your phone.

ALT SOI is used when Carl fails to authenticate three times. The call is then put out to the whole operation to use an alternate SOI using the ALT SOI in the imperative.

### Challenge / Password

Used in person, face-to-face, irl, in the same way as the SARNEG: to ensure the team or team member is not under duress and that it is safe to approach/converse.

### Running Pass

The password used for when you're running, for GTFO emergencies. Appropriate usage likely to involve maximum vocal chord power.

### Number Combination

Another Challenge / Password for face-to-face authentication.

	(Number Combination = 5)
	
	"Authenticate 3!"
	
	"2!"
	
	(Good to go.)