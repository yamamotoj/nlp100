def nlp100_10():
    """
    wc -l hightemp.txt
    """
    with open('hightemp.txt') as f:
        print(len(f.readlines()))


def nlp100_11():
    """
    sed -e 's/    / /g' hightemp.txt
    expand -t 1 hightemp.txt
    cat hightemp.txt|tr '\t' ' '
    """
    with open('hightemp.txt') as f:
        print(f.read().replace('\t', ' '))


def nlp100_12():
    """
    cat hightemp.txt|cut -f1 > col1.txt
    cat hightemp.txt|cut -f2 > col2.txt
    """
    with open('hightemp.txt') as in_f:
        lines = in_f.readlines()
        with open('col1.txt', 'w') as col1:
            print('\n'.join([line.split('\t')[0] for line in lines]), file=col1)
        with open('col2.txt', 'w') as col2:
            print('\n'.join([line.split('\t')[1] for line in lines]), file=col2)


if __name__ == '__main__':
    nlp100_10()
    nlp100_11()
    nlp100_12()
