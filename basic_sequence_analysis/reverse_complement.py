#reverse complement a string of DNA

#dictionary of base complements
complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

#DNA sequence 
DNA = "ATCGATTAGACATGGACCACGTGGTTGACACAC"

#empty complement so far
Complement_DNA = ""

#for loop to iterate through DNA string character by character
for c in DNA:
		#concatenate empty complement string with complement of original sequence
        Complement_DNA += complement.get(c)

#create a list of the complement string
list = list(Complement_DNA)

#use built in Python function that reverses the list 
list.reverse()

#revert the list back into a string 
ReverseComplement_DNA = ''.join(list)

#print reverse complement
print ReverseComplement_DNA
