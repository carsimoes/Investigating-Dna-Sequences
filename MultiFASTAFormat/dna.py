
#(1) How many records are in the file?

f = open("MultiFASTAFormat/dna2.fasta", "r")
file = f.read()
seqcount = file.count('>')
print("Number of sequence = " + str(seqcount))

# (2) What are the lengths of the sequences in the file?

f = open("MultiFASTAFormat/dna2.fasta", "r")
file = f.readlines()

sequences = []
seq = ""
for f in file:
    if not f.startswith('>'):
        f = f.replace(" ", "")      
        f = f.replace("\n", "")
        seq = seq + f             
    else:
        sequences.append(seq)
        seq = ""

sequences.append(seq)
sequences = sequences[1:]         

lengths = [len(s) for s in sequences]
print("\nMax sequence length = " + str(max(lengths)))
print("Min sequence length = " + str(min(lengths)))

print("\nSequence Length Report:")
for j in range(seqcount):
    print ("Length of sequence " + str(j) + " is " + str(lengths[j]))


# (3) ...identify all ORFs present in each sequence of the FASTA file, and answer the following questions: what is the length of the longest ORF in the file? What is the identifier of the sequence containing the longest ORF? For a given sequence identifier, what is the longest ORF contained in the sequence represented by that identifier? What is the starting position of the longest ORF in the sequence that contains it? 

# Find ORF in Sequence
def find_orf(sequence):      
    # Find all ATG indexs
    start_position = 1
    start_indexs = []
    stop_indexs = []
    for i in range(1, len(sequence), 3):
        if sequence[i:i+3] == "ATG":
            start_indexs.append(i)

    # Find all stop codon indexs
    for i in range(1, len(sequence), 3):
        stops =["TAA", "TAA", "TGA"]
        if sequence[i:i+3] in stops:
            stop_indexs.append(i)

    orf = []
    mark = 0
    for i in range(0,len(start_indexs)):
        for j in range(0, len(stop_indexs)):
            if start_indexs[i] < stop_indexs[j] and start_indexs[i] > mark:
                orf.append(sequence[start_indexs[i]:stop_indexs[j]+3])
                mark = stop_indexs[j]+3
                break
    return orf

n = 1
lengths = []
for s in sequences:
    orfs = find_orf(s)
    print("ORF")
    for j in orfs:
        print(j)
        print("================")
        lengths.append(len(j))

print("\nLongest ORF is:" + str(max(lengths)))

