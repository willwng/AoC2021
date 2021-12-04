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


      FUNCTION LZWIN(IBRD, IPT, ISZ)
      INTEGER IPT,ISUM
      DIMENSION IBRD(ISZ,ISZ)
      LOGICAL LZW
      LZW = .FALSE.

      DO I=1,ISZ
      DO J=1,ISZ
      IF(IBRD(I, J).EQ.IPT)THEN
      IBRD(I,J)=-1
      END IF
      END DO
      END DO

      DO I=1,ISZ
      ISUM=0
      DO J=1,ISZ
      ISUM=ISUM+IBRD(I,J)
      END DO
      IF(ISUM.EQ.-5)THEN
      LZW = .TRUE.
      GOTO 10
      END IF
      END DO

      DO I=1,ISZ
      ISUM=0
      DO J=1,ISZ
      ISUM=ISUM+IBRD(J,I)
      END DO
      IF(ISUM.EQ.-5)THEN
      LZW = .TRUE.
      GOTO 10
      END IF
      END DO
10    LZWIN=LZW
      END FUNCTION


      PROGRAM SOLVE
      PARAMETER (IPTS=100, IBRDS=100, ISZ=5)
      DIMENSION IPT(IPTS)
      DIMENSION IBD(ISZ,ISZ,IBRDS)
      DIMENSION IWNRS(IBRDS)
      INTEGER IANS,IDON,ICUR,IWN
      LOGICAL LZW
      IDON=-1
      ICUR=0
      IWN=0

      DO I=1, IBRDS
      IWNRS(I)=0
      END DO

      OPEN(1, FILE='input.txt', STATUS='old')
      READ(1,*)IPT
      READ(1,*)IBD
      
      DO I=1,IPTS

      DO J=1,IBRDS
      LZW=LZWIN(IBD(1:ISZ,1:ISZ,J),IPT(I),ISZ)
      
      IF(LZW .AND. IWNRS(J).EQ.0)THEN
      IWN=IWN+1
      IWNRS(J)=1
      END IF

      IF(IWN.EQ.IBRDS)THEN
      IANS=0
      DO II=1,ISZ
      DO JJ=1,ISZ
      ICUR=IBD(II,JJ,J)
      IF(ICUR .NE. -1 )THEN
      IANS=IANS+IBD(II,JJ,J)
      END IF
      END DO
      END DO
      IANS=IANS*IPT(I)
      GOTO 20
      END IF

      END DO

      END DO
20    PRINT*,"ANSWER IS: ", IANS
      END PROGRAM

