import os
import sys
import exifread
from datetime import datetime

directory = sys.argv[1]

i = 0

for file in os.listdir(directory):
	if file.endswith(".py"):
		print("Ignore .py files")
	elif file.endswith(".txt"):
		print("Ignore .txt files")
	elif file.startswith("done"):
		print("Schon umbenannt")
	else:
		i = i + 1

		# Construct original path with OLD name 
		# Needed for reading in the EXIF data
		imagePath = os.path.join(directory, file) 
		image     = open(imagePath, 'rb')

		# Read the EXIF tags
		exifTags = exifread.process_file(image, details=False)

		# Get file extension - we need to keep that with the new name!
		extension = file.split(".")[-1]

		# Temp string for storing the date
		date = None

		for key in exifTags.keys():
			if(key == 'EXIF DateTimeOriginal'):
				date = exifTags[key]

		if date == None:
			timestamp = os.path.getmtime(directory + "/" + file)
			date = datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d %H-%M-%S")

		date = str(date).replace("/", "-").replace(":", "-")
		newName = "done " + str(date) + " " + str(i) + " 00." + extension
		newName = newName.replace(" ", "_")

		# Finally: Rename!
		# The new name consists of
		# - The string "done"
		# - The date: YEAR-MONTH-DAY
		# - The time: HOUR-MINUTE-SECOND
		# - An enumeration over all pictures
		# - The string "00" for post-processing, manual order adjustments
		os.rename(file, newName)
