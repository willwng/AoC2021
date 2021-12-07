C     NAMING CONVENTIONS USED -
C      A-G       REAL IN COMMON BLOCK
C      H         CHARACTER IN COMMON BLOCK
C      HZ        CHARACTER, INTERNAL
C      I-J       INTEGER, INTERNAL
C      KP        PARAMETER IN COMMON BLOCK
C      K         PARAMETER, INTERNAL
C      L         LOGICAL IN COMMON BLOCK
C      LZ        LOGICAL, INTERNAL
C      M         INTEGER, INTERNAL
C      N         INTEGER IN COMMON BLOCK
C      O-Y       REAL IN COMMON BLOCK
C      Z         INTERNAL      
      
      PROGRAM SOLVE
      PARAMETER (ISZ=1000, ILINES=1)
      INTEGER IANS
      INTEGER, DIMENSION(ISZ) :: IAR
      INTEGER ISCORE
      IANS=HUGE(INTEGER)

      DO I=1,ISZ
      IAR(I)=0
      END DO

      OPEN(1, FILE='input.txt', STATUS='old')
      READ(1,*)  IAR

      DO I=1,MAXVAL(IAR(1:ISZ))
      ISCORE=0
      DO J=1, ISZ
      ISCORE = ISCORE+(ABS(IAR(J)-I))
      END DO
      IF(ISCORE .LT. IANS)THEN
      IANS = ISCORE
      END IF
      END DO
      
      PRINT*,"ANSWER IS: ", IANS
      END PROGRAM
