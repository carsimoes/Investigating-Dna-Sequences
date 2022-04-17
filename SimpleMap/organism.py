
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

import time

while True :
    try:
        fasta_string = open("myseq.fa").read()

        result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)       
        blast_record = NCBIXML.read(result_handle)

        E_VALUE_THRESH = 0.01
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                if hsp.expect < E_VALUE_THRESH:
                    print('****Alignment*****')
                    print('sequence:', alignment.title)
                    print('length:', alignment.length)
                    print('e value:', hsp.expect)
                    print(hsp.query)
                    print(hsp.match)
                    print(hsp.sbjct)

        if serverWasDown:
            print("Server is up and running again.")
        break

    except:
        print("Server connection lost, waiting 10 seconds to try again.")
        serverWasDown = True
        time.sleep(10)