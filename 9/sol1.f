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
      
      FUNCTION LLOW(I, J, IEL, IAR, ISZ)
      INTEGER, DIMENSION(ISZ, ISZ) :: IAR
      LOGICAL LU,LL,LR,LD
      LU = .FALSE.
      LL = .FALSE.
      LR = .FALSE.
      LD = .FALSE.

      IF(I.LE.1 .OR. IEL.LT.IAR(I-1, J))THEN
            LL = .TRUE.
      END IF
      IF(I.GE.ISZ .OR. IEL.LT.IAR(I+1, J))THEN
            LR = .TRUE.      
      END IF
      IF(J.LE.1 .OR. IEL.LT.IAR(I, J-1))THEN
            LU = .TRUE.      
      END IF
      IF(J.GE.ISZ .OR. IEL.LT.IAR(I, J+1))THEN
            LD = .TRUE.      
      END IF
      LLOW = (LL.AND.LR.AND.LU.AND.LD)
      END FUNCTION

      PROGRAM SOLVE
      PARAMETER (ISZ=100, ILINES=100)
      INTEGER IANS
      INTEGER, DIMENSION(ISZ, ISZ) :: IAR
      CHARACTER(ISZ) HINPUT
      LOGICAL LZM
      IANS=0

C     INPUT READING IS TRICKY DUE TO NO DELIMITER
      OPEN(1, FILE='input.txt', STATUS='old')
      DO I=1, ILINES
      READ(1,*)  HINPUT
      DO J=1, ISZ
      READ(HINPUT(J:J),*) IEL
      IAR(I,J) = IEL
      END DO
      END DO

      DO I=1,ISZ
      DO J=1,ISZ
      LZM = LLOW(I,J,IAR(I,J),IAR,ISZ)
      IF(LZM .EQV. .TRUE.)THEN
            IANS=IANS+1+IAR(I,J)
      END IF
      END DO
      END DO

      
      
      PRINT*,"ANSWER IS: ", IANS
      END PROGRAM

