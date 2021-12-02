      PROGRAM SOLVE
        INTEGER ANS, PREV,PREV2,PREV3,CURR
        PREV=HUGE(INTEGER)
        PREV2=HUGE(INTEGER)
        PREV3=HUGE(INTEGER)
        CURR=0
        ANS=0
        OPEN(1, FILE='input.txt', STATUS='old')
        DO I=1,2000
          READ(1,*) CURR
          IF(CURR.GT.PREV)ANS=ANS+1
          PREV=PREV2
          PREV2=PREV3
          PREV3=CURR

        END DO
        PRINT *, "ANSWER IS ", ANS
      END