#have: making an empty dictionary, opening fasta file, 
	# key/value pairs of header and sequence
	# returns dictionary

#want: generator function
	# no dictionary
	# yield header,sequence as a tuple





def fastaParser(file):

	with open(file) as fh:

		header = None
		sequence = ""
		
		for line in fh:

			line = line.strip()
			
			if line.startswith(">"):
				if header:
					yield (header,sequence)
					sequence = ""
				#line is a header
				header = line.lstrip(">")
			
			else:
				#line is a sequence line
				sequence += line.strip()
				
		yield (header,sequence)

