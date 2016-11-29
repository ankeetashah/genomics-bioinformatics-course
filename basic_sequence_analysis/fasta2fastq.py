#Parse a FASTA and QUAL into a FASTQ (short version)
#This script makes the assumption that the FASTA and QUAL match in terms of the order of their sequences
#@param fasta and qual
#@return fastq

#Open the files
Qual = open ('sample_fasta2fastq.qual', 'r')
Fasta = open ('sample_fasta2fastq.fasta', 'r')
Fastq = open ('sample_fasta2fastq.fastq', 'w')

#Map of quality scores with ASCII characters
qual_map = { '0' : '!',
               '1' : '"',
               '2' : '#',
               '3' : '$',
               '4' : '%',
               '5' : '&',
               '6' : '\'',
               '7' : '(',
               '8' : ')',
               '9' : '*',
               '10' : '+',
               '11' : ',',
               '12' : '-',
               '13' : '.',
               '14' : '/',
               '15' : '0',
               '16' : '1',
               '17' : '2',
               '18' : '3',
               '19' : '4',
               '20' : '5',
               '21' : '6',
               '22' : '7',
               '23' : '8',
               '24' : '9',
               '25' : ':',
               '26' : ';',
               '27' : '<',
               '28' : '=',
               '29' : '>',
               '30' : '?',
               '31' : '@',
               '32' : 'A',
               '33' : 'B',
               '34' : 'C',
               '35' : 'D',
               '36' : 'E',
               '37' : 'F',
               '38' : 'G',
               '39' : 'H',
               '40' : 'I' }
                
#Reads in FASTA file line by line
for line in Fasta:
            field = line.rstrip() 
            
            #Inside of conditional, read associated QUAL file line by line
            if ">" in field:
                    Qual.readline()
                    newfield = field.replace(">", "@") #replaces header carrot with FASTQ header symbol
                    Fastq.write(newfield+"\n") #writes out this header to output file
                  
            else:
                    field_qual = Qual.readline() #if it is a sequence line, reads in associated quality line
                    field_qual_strip = field_qual.rstrip() #saving a strip version of the field_qual
                    Fastq.write(field+"\n")
                    Fastq.write("+\n")

                    #splits quality score into a list of scores by spaces
                    new_field_qual = ""
                    character = field_qual_strip.split()
                    for i in range (0, len(character)):
                            x = qual_map.get(character[i]) #gets associated character of quality score
                            new_field_qual += x
                    Fastq.write(new_field_qual+"\n")
                    
            

Fasta.close()
Qual.close()
Fastq.close()
