C     NAMING CONVENTIONS USED -
C      A-G       REAL IN COMMON BLOCK
C      H         CHARACTER IN COMMON BLOCK
C      HZ        CHARACTER, INTERNAL
C      I-J       INTEGER, INTERNAL
C      KP        PARAMETER IN COMMON BLOCK
C      K         PARAMETER, INTERNAL
C      L         LOGICALw IN COMMON BLOCK
C      LZ        LOGICAL, INTERNAL
C      M         INTEGER, INTERNAL
C      N         INTEGER IN COMMON BLOCK
C      O-Y       REAL IN COMMON BLOCK
C      Z         INTERNAL
      PROGRAM SOLVE
      INTEGER I1,I2,I3,IA,IB,IC,IANS1,IANS2
      REAL R1,R2,R3,RA,RB,RC,RANS
      LOGICAL L1,L2,L3,LA,LB,LC
      CHARACTER(30) CSTR
      DIMENSION IAR0(12), IAR1(12)
      IANS1=0
      IANS2=0
      OPEN(1, FILE='input.txt', STATUS='old')

      DO I=1,12
      IAR0(I) = 0
      IAR1(I) = 0
      END DO

      DO I=1,1000
      READ(1,*) CSTR
      DO I1=1, 12
      IF(CSTR(I1:I1) .EQ. '0') IAR0(I1)=IAR0(I1)+1
      IF(CSTR(I1:I1) .EQ. '1') IAR1(I1)=IAR1(I1)+1
      END DO
      END DO

      DO I=1,12
      IF(IAR0(I) .GT. IAR1(I))THEN
      IANS1=IANS1+2**(12-I)
      ELSE
      IANS2=IANS2+2**(12-I)
      END IF
      END DO


      PRINT *, "ANSWER IS (binary)", IANS1*IANS2
      END PROGRAM