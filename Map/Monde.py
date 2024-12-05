# Code des Monde du jeu
### Variables: "X" = Tuile
# ; "P" = Piege 
# ; "M" = Marchand 
# ; "E" = Ennemi 
# ; "-" = Route d'un enemie 
# ; "C" = Piques cachés 
# ; "N" = Niveau terminé

map_list = [



[ # Monde Démo modifié pour tester le personnage avec des éléments différents.
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXC          E           CXX',
'XXXXXX            XXXX      XX',
'XXXXXX                      XX',
'XXX           XXXX          XX',
'X    XXXXXX          XXXX    X',
'X        CXXXXX            CXX',
'XS              E      XXX   X',
'X          CC       CC       N',
'XXXXXXXXXXXXXXXXPPPPPPXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'],
    

[ # Monde 1 Niveau 1 - Ajout de nouveaux pièges et zones ennemies.
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXC                         XX',
'X     C   - E   -      C     X',
'X       XXXXXXXX     XXXX    X',
'X                          CXX',
'X   XXXXX        XXXX      XXX',
'XS         PPCC         CC   N',
'XXXXXXXXXXXXXCCPPPPPPPPPPXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'],


[ # Monde 1 Niveau 2 - Nouveau niveau avec plus de variabilité.
'X                            N',
'X          CC    -E-         N',
'X    C    XXXX          CC   N',
'X    XXXXXX            XXXX  N',
'X   XXX        XXXX          N',
'XS               XX   XXX    N',
'XX           CXX         X   N',
'XXXCCC    XX   - E-     XXX  N',
'XXXXXXXXXXXXXXXXXXPPPPPPPPXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'],


[ # Monde 1 Niveau 3 - Ajout de mouvements complexes d'ennemis et de zones cachées.
'X                            N',
'X                            N',
'X                            N',
'X           C    C           N',
'XS         XXX    XX       CCC',
'X    C- E   E  E -XX         N',
'X     XX      XXXX      CC   N',
'XXXCCCCCCCCCCPPPPPPPPPPPPPPXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'],


[ # Monde 1 Niveau 4 - Introduction de pièges interactifs et de sections marchandes.
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXX                N',
'XXXCCC       XX              N',
'X        E    -E   -    E    N',
'X   XXXXXXX   XXXXX          N',
'X   XXXXXCCC  CCCC           N',
'XS CCC         XX            N',
'XXX   XXXX           XX      N',
'XXXXXX   CCXXXXX      XX     N',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'],


[ # Monde Intermédiaire avec Marchand
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXX      CXXXXXXX       N',
'X               CCCC         N',
'X         XXXXX              N',
'XS XX      MB          CCCCCCX',
'X  XXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'],


[ # Monde 1 Niveau 5 - Un mélange de pièges et d’ennemis mobiles.
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XX              CC          XX',
'X    C         XXXXXC        X',
'X   C      E        -E       N',
'XS   XXXXX           CC     XX',
'XX        XX         XXX     N',
'XXX         CXXXX    XX     XX',
'XXXX  PPCCPPPPPPPPPPPPPPP   XX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'],




[ #Monde 1 Niveau 6
'X                            N',
'X                            N',
'X                            N',
'X                 -  E -     N',
'X          XX     XXXXXX     N',
'X                            N',
'X            XXXX            N',
'X                  X    X    N',
'XS CC  CCXXXCCCCCCCCCCCCCX   N', ### Placer des piques cachés dans les cases "C"
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Monde 1 Niveau 7
'X                            N',
'X                            N',
'XCC                          N',
'XXX     XXXX                 N',
'X                            N',
'X   XXXXCCC   XX  XX  XX  XXXX',
'XS       XXX                  ',
'XX                            ',
'XXXPPCCPPCCPPCCPPCCPPCCPPCCPPC',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Monde 1 Niveau 8
'C                            N',
'XX                           N',
'XXX                    CCCCCX',
'XX            CXXXX   XXXXXXXX',
'XS       CXXXX       XX      N',
'XXC  XXXXX    CCCC X  X     XX',
'XXX           XXXX         CXX',
'XXXXC                     CXXX',
'XXXXXC                XXXXX   N',
'XXXXXXC- E     E     E     E -N',
'XXXXXXCXXXXXXXXXXXXXXXXXXXXXXX']
,





[ #Le marchand vends de meilleures marchandises qu'a la première rencontre
'X                            N',
'X                            N',
'X                          XXX',
'X                       XXXXXX',
'X                    XXXXXXXXX',
'XX              XXXXXXXXXXXXX',
'XXX         XXX   XXXXXXXXXXXX',
'XXXX   XX         XXXXXXXXXXXX',
'X               MBXXXXXXXXXXXX',
'XS   XXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,





[ #Monde 2 Niveau 1
'XS                           X',
'XX        C  -E   E-         X',
'XXXC     XX  XXXXXXX         X',
'XXXX                XXXX     X',
'XXXXX                        N',
'XXX            C    C       XX',
'XXX XXXC-  E  -XXPPXX- E  -XXX',
'XXX XXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXX XX     XXXX     XXX     XX',
'XXX-    E        E       E   -N',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Monde 2 Niveau 2
'X                            X',
'X    C- E  C  E  C  E -C     X',
'X   XXXXXXXXXXXXXXXXXXXX     X',
'X  X                    XX   X',
'XSX                          X',
'XX        C-  E  -CCPCC  CXX X',
'X     C X XXXXXXXXXXXXXXXXXXXX',
'X   C XX                   XXX',
'X   XX                      XX',
'X-E        E    E    E    E -N',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Monde 2 Niveau 3
'X                            X',
'X                            X',
'X                            X',
'X          CXXC              X',
'X        CXX  XXC            X',
'X       XX      XX           X',
'X                            X',
'XSCXXXX    -E -     XXC      X',
'XXX        XXXX       XX     X',
'- E    E    E    E    E    E-N',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Monde 2 Niveau 4S
'                             XX',
'X                            XX',
'X                           SX',
'X                         CXXX',
'X                        XXXXX',
'X    - E     E     E -CXXXXXXX',
'X    XXXXXXXXXXXXXXXXXXXXXXXXX',
'X  XX                        X',
'X- E     C      E  C      -  X',
'XXXXXXXXXXXXXXXXXXXXXXXXXXX  X',
'N                            X',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Le marchand vends les meilleures marchandises du jeu
'XX                           X',
'XX                           X',
'XXS                          X',
'XXXX                         X',
'XXXXX                        N',
'XXXXXXXXXXXX                 N',
'XXXXX     XX                 X',
'XXXXX                       XX',
'XXXXX  MB                  XXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Monde 2 Niveau 5
'X                           XX',
'X    -  E     E     E C-    XX',
'X    XXXXXXXXXXXXXXXXXXXC   XX',
'X   X                   XC  XX',
'X  X                     XX  X',
'XS    C    C    C    C       N',
'XX    XXXXXXXXXXXXXXXXXXX   XX',
'XXX                        XXX',
'XXXX                      XXXX',
'XXXXXP   P   P P   P   PXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Monde 2 Niveau 6
'X                            X',
'X                            X',
'X               C            X',
'X  -E  -       XXC           X',
'X  XXXXX     CXXXX           X',
'XS           XXXXXXC         X',
'XX         CXXXXXXXX         X',
'XXXC       XXXXXXXXXXC       X',
'XXXX     CXXXXXXXXXXXX     C N',
'XXXXX-E -XXXXXXXXXXXXXX- E-XXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Monde 2 Niveau 7
'X                     XXXXXXXX',
'X          XXC   C    X      X',
'X         XXXXX         CXXXXX',
'X        XXXXXXXCCX  XXXXXXXXX',
'X      CXXXXCCC       XXX    X',
'X      XXXX- E  - XXXXXX  XXXX',
'X     XXXXXXXXX              N',
'X      XXXXXXXXXXXXXXXXXXXXXXX',
'XS  X   XX   XX   XX   XX    X',
'XXXXX.-E   E    E    E    E -N',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
,


[ #Niveau de fin
'                           X',
'                           X',
'                           X',
'                           X',
'                           X',
'  XHHXXHH                  X',
' X                         X',
'X    XXX                   X',
'   XXXXXX                XXX',
'  XXXXXXXXXXXXXXXXXXXXXXXXXN',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXX']

]