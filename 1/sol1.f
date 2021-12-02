      PROGRAM SOLVE
        INTEGER ANS=0
        INTEGER PREV=HUGE(INTEGER)
        INTEGER CURR=0
        OPEN(1, FILE='input.txt', STATUS='old')


        DO I=1,2000
          READ(1,*) CURR
          IF(CURR.GT.PREV)ANS=ANS+1
          PREV=CURR
        END DO
        PRINT *, "ANSWER IS ", ANS
      END