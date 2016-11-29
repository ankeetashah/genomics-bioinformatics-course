#This script reads in the sequences from a FASTA file and returns the GC content

#open the FASTA file
Fasta = open ('GC.fasta', 'r')
GC = open('GC.txt', 'w')

#delcare a few variables to hold GC content and total number of sequences 
content = 0.0
total_size = 0.0

#loops through each line in FASTA file
for line in Fasta:
        line = line.rstrip() #BE CAREFUL - MUST ACCOUNT FOR NEWLINE CHARACTERS
        #only deals with actual sequence lines, not headers
        if ">" not in line:
                total_size += len(line) #adds all characters in said line and adds it to total
                
                #looks at individual characters in each line
                for char in line:
                        if (char=='C' or char=='G' ):
                                content +=1 #adds 1 to content if it is a G or a C

percent_GC_content = (content/total_size)*100

#write out GC
stringGC = "GC Content: " + str(percent_GC_content) + "%"
GC.write(stringGC)

#close files
Fasta.close()

