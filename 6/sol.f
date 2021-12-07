      PROGRAM SOLVE
      PARAMETER (ISZ=300, ILINES=300, IDYS=256)
      INTEGER*8 :: IANS, INEW
      INTEGER*8, DIMENSION(ISZ) :: IFISH
      INTEGER*8, DIMENSION(9) :: IDAYS
      IANS=0

C     ALLOCATE THE ARRAY 
      DO I=1,9
      IDAYS(I)=0
      END DO

      OPEN(1, FILE='input.txt', STATUS='old')
      READ(1,*) IFISH

      DO I=1,ISZ
C     ARRAYS ARE ONE-INDEXED
      IDAYS(IFISH(I)+1) = IDAYS(IFISH(I)+1) + 1
      END DO

      DO I=1,IDYS
      INEW = IDAYS(1)
      IANS = IANS + INEW
      DO J=1,8
      IDAYS(J)=IDAYS(J+1)
      END DO
      IDAYS(7)=IDAYS(7)+INEW
      IDAYS(9)=INEW
      END DO
      
      PRINT*,"ANSWER IS: ", IANS
      END PROGRAM

