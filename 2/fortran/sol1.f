      PROGRAM SOLVE
        INTEGER IHOR, IDEP, IMT
        CHARACTER(30) CSTR
        IHOR=0
        IDEP=0
        OPEN(1, FILE='input.txt', STATUS='old')
        DO I=1,1000
          READ(1,*) CSTR, IMT
          IF(CSTR.EQ."forward")THEN
            IHOR=IHOR+IMT
          ELSE IF(CSTR.EQ."up")THEN
            IDEP=IDEP-IMT
          ELSE
            IDEP=IDEP+IMT
          END IF
        END DO
        PRINT *, "ANSWER IS ", IDEP*IHOR
      END