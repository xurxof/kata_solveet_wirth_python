kata solveet wirth python
=========================
Resolución en python al reto http://www.solveet.com/exercises/Subsecuencias-de-Wirth/152


Encontrar todas las cadenas de N caracteres "A", "B" o "C" tales que no contengan dos subsecuencias consecutivas.

Es decir:

1. las cadenas de salida deben tener longitud N.

2. los únicos caracteres posibles son "A", "B" o "C".

3. en las cadenas resultantes, no debe poderse encontrar dos subsecuencias consecutivas.

4. deben encontrarse todas las cadenas posibles que cumplan las condiciones (para un N dado).

Por ejemplo, para N=3 es válida la cadena "ABA" porque aunque la subsecuencia "A" se repite dos veces, no está de forma consecutiva.

Para N=4, no sería válida la cadena "ABAB" porque la subsecuencia "AB" se repite de forma consecutiva.

Por ejemplo, para N=1..6 todas las cadenas en cada caso son (salvo error, claro):

A,B,C

AB,AC,BA,BC,CA,CB

ABA,ABC,ACA,ACB,BAB,BAC,BCA,BCB,CAB,CAC,CBA,CBC

ABAC,ABCA,ABCB,ACAB,ACBA,ACBC,BABC,BACA,BACB,BCAB,BCAC
BCBA,CABA,CABC,CACB,CBAB,CBAC,CBCA

ABACA,ABACB,ABCAB,ABCAC,ABCBA,ACABA,ACABC,ACBAB,ACBAC
ACBCA,BABCA,BABCB,BACAB,BACBA,BACBC,BCABA,BCABC,BCACB
BCBAB,BCBAC,CABAC,CABCA,CABCB,CACBA,CACBC,CBABC,CBACA
CBACB,CBCAB,CBCAC

ABACAB,ABACBA,ABACBC,ABCABA,ABCACB,ABCBAB,ABCBAC,ACABAC
ACABCA,ACABCB,ACBABC,ACBACA,ACBCAB,ACBCAC,BABCAB,BABCAC
BABCBA,BACABA,BACABC,BACBAB,BACBCA,BCABAC,BCABCB,BCACBA
BCACBC,BCBABC,BCBACA,BCBACB,CABACA,CABACB,CABCAC,CABCBA
CACBAB,CACBAC,CACBCA,CBABCA,CBABCB,CBACAB,CBACBC,CBCABA
CBCABC,CBCACB

A modo de verificación (salvo que el error esté en mi lista, claro :P ) dejo las longitudes de los conjuntos Wirth con longitud de secuencia igual o menor a 40:

Length( Wirth( 0 ) ) = 1
Length( Wirth( 1 ) ) = 3
Length( Wirth( 2 ) ) = 6
Length( Wirth( 3 ) ) = 12
Length( Wirth( 4 ) ) = 18
Length( Wirth( 5 ) ) = 30
Length( Wirth( 6 ) ) = 42
Length( Wirth( 7 ) ) = 60
Length( Wirth( 8 ) ) = 78
Length( Wirth( 9 ) ) = 108
Length( Wirth( 10 ) ) = 144
Length( Wirth( 11 ) ) = 204
Length( Wirth( 12 ) ) = 264
Length( Wirth( 13 ) ) = 342
Length( Wirth( 14 ) ) = 456
Length( Wirth( 15 ) ) = 618
Length( Wirth( 16 ) ) = 798
Length( Wirth( 17 ) ) = 1044
Length( Wirth( 18 ) ) = 1392
Length( Wirth( 19 ) ) = 1830
Length( Wirth( 20 ) ) = 2388
Length( Wirth( 21 ) ) = 3180
Length( Wirth( 22 ) ) = 4146
Length( Wirth( 23 ) ) = 5418
Length( Wirth( 24 ) ) = 7032
Length( Wirth( 25 ) ) = 9198
Length( Wirth( 26 ) ) = 11892
Length( Wirth( 27 ) ) = 15486
Length( Wirth( 28 ) ) = 20220
Length( Wirth( 29 ) ) = 26424
Length( Wirth( 30 ) ) = 34422
Length( Wirth( 31 ) ) = 44862
Length( Wirth( 32 ) ) = 58446
Length( Wirth( 33 ) ) = 76122
Length( Wirth( 34 ) ) = 99276
Length( Wirth( 35 ) ) = 129516
Length( Wirth( 36 ) ) = 168546
Length( Wirth( 37 ) ) = 219516
Length( Wirth( 38 ) ) = 285750
Length( Wirth( 39 ) ) = 372204
Length( Wirth( 40 ) ) = 484446 
