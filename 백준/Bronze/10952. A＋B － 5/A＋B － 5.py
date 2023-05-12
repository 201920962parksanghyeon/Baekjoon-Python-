while(1):
   A,B=map(int, input().split())
   if(A==0 and B == 0):
      break
   elif(A>0 and B < 10):
      print(A+B)
   else:
    print("A가 0이상이어야 하며 B는 10보다 작아야 해요..")
