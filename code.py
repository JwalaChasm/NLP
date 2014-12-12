import os
import subprocess
import re
from nltk.corpus import wordnet as wn
import sys

def compare(one, two, onedep, twodep, onechunk, twochunk):
    #print one
    #print two
    comcount = 0
    com = []

    for x in one.keys():
        try:
            del two[x]
            del one[x]
            com.append(x)

            comcount+=1
        except:
            pass

    #print one
    #print two

    for x in one.keys():
        syn = wn.synsets(x)
        for s in syn:
            nym = str(s)
            nym = re.search('[a-z]+\.', nym)
            nym = nym.group().rstrip('.')
            #print nym
            try:
                del two[nym]
                del one[x]
                com.append(nym)
                #com.append(one[x])
                comcount+=1

            except:
                pass
    for x in two.keys():
        syn = wn.synsets(x)
        for s in syn:
            nym = str(s)
            nym = re.search('[a-z]+\.', nym)
            nym = nym.group().rstrip('.')
            #print nym
            try:
                del one[nym]
                del two[x]
                com.append(nym)
                #com.append(two[x])
                comcount+=1
            except:
                pass

    #print one
    #print two
    #print comcount
    relcount=0
    for wd in com:
        #print c,
        w1 = re.findall('[A-Za-z]+_[a-z]+_'+wd, onedep)
        w2 = re.findall(wd+'_[a-z]+_[A-Za-z]+', onedep)
        z1 = re.findall('[A-Za-z]+_[a-z]+_'+wd, twodep)
        z2 = re.findall(wd+'_[a-z]+_[A-Za-z]+', twodep)



        for a in w1:
            for b in z1:
                #print a.split('_')[1], b.split('_')[1]
                if a.split('_')[1]==b.split('_')[1]:
                    relcount+=1
            for c in z2:
                #print a.split('_')[1], c.split('_')[1]
                if a.split('_')[1]==c.split('_')[1]:
                    relcount+=1

        for a in w2:
            for b in z1:
                #print a.split('_')[1], b.split('_')[1]
                if a.split('_')[1]==b.split('_')[1]:
                    relcount+=1
            for c in z2:
                #print a.split('_')[1], c.split('_')[1]
                if a.split('_')[1]==c.split('_')[1]:
                    relcount+=1

    chunkcount=0

    for i in range(len(onechunk)):
        try:
            if onechunk[i]==twochunk[i]:
                chunkcount+=1
        except:
            break


    return {'com':comcount, 'rel':relcount, 'chunk':chunkcount}










def getdep(twt):

    fn = open('inp.txt', 'w')
    fn.write(twt)
    fn.close()

    os.chdir('stanford-parser-full-2014-06-16')
    deprun = 'java -mx200m -cp "stanford-parser.jar;stanford-parser-3.4-models.jar" edu.stanford.nlp.parser.lexparser.LexicalizedParser -retainTmpSubcategories -outputFormat "penn,typedDependencies" edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz ../inp.txt'
    #deprun = 'java -mx200m -cp "stanford-parser.jar; stanford-parser-3.4-models.jar" edu.stanford.nlp.parser.lexparser.LexicalizedParser -outputFormat "typedDependencies" edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz ../inp.txt'
    proc = subprocess.Popen(deprun, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    depoutp = proc.communicate()[0]
    os.chdir("..")

    outp = repr(depoutp)
    return outp


def gettags(tab):
    pos = {}
    for t in tab.split():
        post = t.split('/')
        pos[post[0]] = post[2]

    return pos

def getchunk(tab):
    chunk = []
    ch = ''
    for t in tab.split():
        bk = t.split('/')
        if bk[3].split('-')[0]=='B':
            ch = bk[3].split('-')[1]
            chunk.append(ch)
        elif bk[3].split('-')[0]=='I':
            ch = ch + " " + bk[3].split('-')[1]
            chunk.pop(len(chunk)-1)
            chunk.append(ch)
    return chunk


def depformat(dept):
    dept = dept.split("\\r\\n")
    dept = dept[len(dept)-2].split("\\n")

    allrel=''

    for d in dept:
        if d== '':
            break
        a = d.split('(')
        rel = a[0]
        b = a[1].split(',')
        par = b[0].split('-')[0]
        chd = b[1].split('-')[0]
        chd = chd.strip()
        tl = par + "_" + rel + "_" + chd + " "
        allrel+= tl

    return allrel



def getlabel(x):
    tab = x.split("\t")
    #print "topic: ", tab[1]
    #print 'tag1:\n',
    #print tab[2]

    #print '\ntag2:'
    #print tab[3]

    #print  '\nlabel: ',
    label = ''
    l = re.findall('[0-5]', tab[4])
    if l[0]>l[1]:
        label = "True"
    elif l[0]=='2':
        return
    else:
        label = "False"

    dep1 = getdep(tab[2])
    onedep = depformat(dep1)
    dep2 = getdep(tab[3])
    twodep = depformat(dep2)

    pos1 = {}
    pos1 = gettags(tab[5])
    pos2 = {}
    pos2 = gettags(tab[6])

    chunk1 = []
    chunk2 = []
    chunk1 = getchunk(tab[5])
    chunk2 = getchunk(tab[6])

    countvec = compare(pos1, pos2, onedep, twodep, chunk1, chunk2)
    countvec['com'] = float(countvec['com'])
    countvec['rel'] = float(countvec['rel'])
    countvec['chunk'] = float(countvec['chunk'])

    kine = '['+str(countvec['com'])+" "+str(countvec['rel'])+" "+str(countvec['chunk'])+']\t'+label
    #kine = '['+str(countvec['com'])+" "+str(countvec['rel'])+']\t'+label
    print kine




f = open(sys.argv[1], 'r')
text = f.readlines()
f.close()

#print text

for x in text:

    getlabel(x)
#getlabel(text[1])

