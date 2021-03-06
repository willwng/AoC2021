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
      
      RECURSIVE SUBROUTINE FLASH(I, J, IAR, ISEEN, ILINES, ISZ)
      INTEGER, DIMENSION(ILINES, ISZ) :: IAR, ISEEN
      IF(ISEEN(I,J) .EQ. 1) RETURN
      IF(I.LT.1 .OR. I.GT.ILINES) RETURN
      IF(J.LT.1 .OR. J.GT.ISZ) RETURN
     
      IAR(I,J) = IAR(I,J)+1
      IF(IAR(I,J).LE.9)RETURN

      ISEEN(I,J) = 1

      CALL FLASH(I+1, J-1, IAR, ISEEN, ILINES, ISZ)
      CALL FLASH(I+1, J, IAR, ISEEN, ILINES, ISZ)
      CALL FLASH(I+1, J+1, IAR, ISEEN, ILINES, ISZ)
      CALL FLASH(I, J-1, IAR, ISEEN, ILINES, ISZ)
      CALL FLASH(I, J+1, IAR, ISEEN, ILINES, ISZ)
      CALL FLASH(I-1, J+1, IAR, ISEEN, ILINES, ISZ)
      CALL FLASH(I-1, J, IAR, ISEEN, ILINES, ISZ)
      CALL FLASH(I-1, J-1, IAR, ISEEN, ILINES, ISZ)

      END SUBROUTINE


      SUBROUTINE RESET(ISEEN, ILINES, ISZ)
      INTEGER, DIMENSION(ILINES, ISZ) :: ISEEN
      DO I=1,ILINES
      DO J=1,ISZ
      ISEEN(I,J) = 0
      END DO
      END DO
      END SUBROUTINE

      PROGRAM SOLVE
      PARAMETER (ISZ=10, ILINES=10)
      INTEGER IANS,ICT
      INTEGER, DIMENSION(ILINES, ISZ) :: IAR, ISEEN
      CHARACTER(ISZ) HINPUT
      IANS=0

      CALL RESET(ISEEN,ILINES,ISZ)
C     INPUT READING IS TRICKY DUE TO NO DELIMITER
      OPEN(1, FILE='input.txt', STATUS='old')
      DO I=1, ILINES
      READ(1,*)  HINPUT
      DO J=1, ISZ
      READ(HINPUT(J:J),*) IEL
      IAR(I,J) = IEL
      END DO
      END DO

C     STEPS
      DO ISTEP=1,999
      ICT=0
      DO I=1,ISZ
      DO J=1,ISZ
      CALL FLASH(I, J, IAR, ISEEN, ILINES, ISZ)
      END DO
      END DO


      DO IR=1,ILINES
      DO JR=1,ISZ
      IF(ISEEN(IR,JR).EQ.1)THEN
      IAR(IR,JR) = 0
      ICT = ICT+1
      END IF
      END DO
      END DO
      IF(ICT.EQ.ILINES*ISZ)THEN
      IANS = ISTEP
      GOTO 10
      END IF

      CALL RESET(ISEEN,ILINES,ISZ)
      END DO
10    PRINT*,"ANSWER IS: ", IANS
      END PROGRAM

