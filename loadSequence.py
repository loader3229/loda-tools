from tqdm import tqdm
import os
import json

user = 'Lenovo'

t = open('C:/Users/'+user+'/loda/seqs/oeis/stripped').read().split('\n')[4:-1]

offset_raw = open('C:/Users/'+user+'/loda/seqs/oeis/offsets').read().split('\n')
offsets = {}
for i in range(0,len(offset_raw)):
  try:
    offsets[offset_raw[i].split(':')[0]]=int(offset_raw[i].split(':')[1].split(',')[0])
  except:
    pass

print(offsets["A000037"])

deny_raw = open('C:/Users/'+user+'/loda/programs/oeis/deny.txt').read().split('\n')
deny = {}
for i in range(0,len(deny_raw)):
  try:
    deny[deny_raw[i].split(':')[0]]=1
  except:
    pass

sequences = []
seqnum = 0
for i in tqdm(range(0,len(t)), desc="loading sequences", unit=" sequences"):
  seq = t[i].split(',')[1:]
  if len(seq) > 15:
    seq = seq[0:15]
  else:
    continue
  for j in range(0,len(seq)):
    seq[j] = int(seq[j])
  offset = 0
  try:
    offset = offsets[t[i].split(',')[0][0:7]]
  except:
    pass
  d = 0
  try:
    d = deny[t[i].split(',')[0][0:7]]
  except:
    pass
  if d == 1:
    continue
  seqnum += 1
  if os.path.exists('C:/Users/'+user+'/loda/programs/oeis/'+t[i].split(',')[0][1:4]+'/'+t[i].split(',')[0][0:7]+'.asm'):
    p = open('C:/Users/'+user+'/loda/programs/oeis/'+t[i].split(',')[0][1:4]+'/'+t[i].split(',')[0][0:7]+'.asm')
    prog = p.read()
    p.close()
    prog = prog.split('\n')
    cal = 0
    indirect = 0
    lpb = 0
    for k in prog:
      j = k.split(';')[0]
      cal += j.count("seq")
      lpb += j.count("lpb")
      indirect += j.count("$$")
    sequences.append([t[i].split(',')[0][0:7],seq,offset,1,cal,lpb,indirect])
  else:
    sequences.append([t[i].split(',')[0][0:7],seq,offset,0,0,0,0])

print("loaded",seqnum,"sequences")

