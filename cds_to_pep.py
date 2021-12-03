'''
Auther:Qi Guangyuan
Data:2021-12-3
Contact:qiguangyuan0406@163.com
Script Use argparse to pass in command line parameters
'''
import argparse

parse=argparse.ArgumentParser(description='Input and output file path.')

parse.add_argument('--input','-i',help='The input file path.')
parse.add_argument('--output','-o',help='The output file path.')
parse.add_argument('--table','-t',default='Standard',type=str,help='Codon table used.')

args=parse.parse_args()

from Bio import SeqIO
seq_id=[]
seq_pep=[]
for seq_record in SeqIO.parse(args.input, "fasta"):
    # print(seq_record.id)
    # print(seq_record.seq)
    # print(len(seq_record))
    seq_id.append(seq_record.id)
    cds=seq_record.seq
    pep=cds.translate(table=args.table)
    seq_pep.append(pep)
    # print(seq_record.id)
    # print(pep)
print(seq_id)
print(seq_pep)
file=open(args.output,'w')
# file.write(seq_record.id+'\n')
# file.write(str(pep))
for i,k in enumerate(seq_id):
    file.write('>'+str(seq_id[i])+'\n')
    file.write(str(seq_pep[i]+'\n'))