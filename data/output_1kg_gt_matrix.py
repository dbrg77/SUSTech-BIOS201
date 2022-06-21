with open('MGI358_in_1kg.tsv') as fh:
    header = fh.readline().strip().split('\t')
    print('%s\t%s' % (header[2], '\t'.join(header[9:])))
    for line in fh:
        rec = line.strip().split('\t')
        num = []
        for gt in rec[9:]:
            a1, a2 = gt.split('|')
            num.append(str(int(a1) + int(a2)))
        print('%s\t%s' % (rec[2], '\t'.join(num)))
