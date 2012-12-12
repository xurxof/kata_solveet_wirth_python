from nose.tools import *
import wirth

def setup():
    pass

def teardown():
    pass

def test_SolvesFonN_0():
    assert_true(wirth.wirth(0)==[])
    
def test_SolvesForN_1():
    assert_true(wirth.wirth(1)==['A','B','C'])

def test_SolvesForN_2():
    assert_true(wirth.wirth(2)==['AB','AC','BA','BC','CA','CB'])

def test_SolvesForN_3():
    assert_true(wirth.wirth(3)==['ABA', 'ABC', 'ACA', 'ACB', 'BAB', 'BAC', \
            'BCA', 'BCB', 'CAB', 'CAC', 'CBA', 'CBC'  ])

def test_SolvesForN_4():
    assert_true(wirth.wirth(4)==['ABAC', 'ABCA', 'ABCB', 'ACAB', 'ACBA', 'ACBC', \
            'BABC', 'BACA', 'BACB', 'BCAB', 'BCAC', 'BCBA', \
            'CABA', 'CABC', 'CACB', 'CBAB', 'CBAC', 'CBCA' ])
            
def test_SolvesForN_5():
    assert_true(wirth.wirth(5)==['ABACA','ABACB','ABCAB','ABCAC','ABCBA','ACABA','ACABC','ACBAB','ACBAC', \
            'ACBCA','BABCA','BABCB','BACAB','BACBA','BACBC','BCABA','BCABC','BCACB', \
            'BCBAB','BCBAC','CABAC','CABCA','CABCB','CACBA','CACBC','CBABC','CBACA', \
            'CBACB','CBCAB','CBCAC'])
                        
def test_SolvesForN_6():
    print wirth.wirth(6)
    assert_true(wirth.wirth(6)==['ABACAB','ABACBA','ABACBC','ABCABA','ABCACB','ABCBAB','ABCBAC','ACABAC', \
            'ACABCA','ACABCB','ACBABC','ACBACA','ACBCAB','ACBCAC','BABCAB','BABCAC', \
            'BABCBA','BACABA','BACABC','BACBAB','BACBCA','BCABAC','BCABCB','BCACBA', \
            'BCACBC','BCBABC','BCBACA','BCBACB','CABACA','CABACB','CABCAC','CABCBA', \
            'CACBAB','CACBAC','CACBCA','CBABCA','CBABCB','CBACAB','CBACBC','CBCABA', \
            'CBCABC','CBCACB'])

def test_SolvesForNLowerThan40():
    sequencesCount=[0,3,6,12,18,30,42,60,78,108,144,204,264,342,456,618, \
        798,1044,1392,1830,2388,3180,4146,5418,7032,9198,11892,15486,20220,
        26424,34422,44862,58446,76122,99276,129516,168546,219516,285750,372204,484446]
    
    for n in range(0,40):
        yield checkNumberSequences, n, sequencesCount[n]

def checkNumberSequences (n, sequencesCount):
    assert_true (len(wirth.wirth(n)) == sequencesCount)
