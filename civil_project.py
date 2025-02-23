# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 18:47:38 2022

@author: MARUTHI
"""

def calculateMP(t1, t2,  w1, w2, d,d1 ):
    
    i = (2*(t1+t2));
    return i;

def calculateMp1(t1,t2):
    i=(t1+t2);
    return i;

def calculateMp2(t1,t2,W,d):
    i=(2*(t1+t2));
    return i;



s = input(" enter  x or y: ")# x= Simply Sipported Beam; y=Fixed Beam
if(s == 'x'):
    v = input("enter a or b or c or d: ")# a=PL; b=UDL; c=ecentric UDL; d=Comb PL
    if(v == 'a'):
        W = int(input("Enter the load: "))
        L = int(input("Enter the length: "))
        Wu=W*1.5;
        m=int(input("enter load acting fm ls: "))
        n=L-m;
        Mp = (Wu*m*n) /L;
        print("Plastic Moment (Mp)= ",Mp, "kN-m");
    elif(v == 'b'):
        W = int(input("Enter the load: "))
        L = int(input("Enter the length: "))
        Wu=W*1.5;
        Mp = (Wu*L)/8;
        print("Plastic Moment (Mp)= ",Mp , "kN-m");
    elif(v == 'c'):
        W=int(input("Enter udl: "))
        l=int(input("Enter total length of beam: "))
        l1=int(input("Enter the length load is acting from ls: "))
        #Taking momemt about B, then Reaction 
        Dwr= W*l1*(l1/2+(l-l1));
        RA=Dwr/l;
        print("Support Reaction at A = ", RA, "kN");
        '''equating max BM and plastic moment of the section
        RA*x - WX*x/2 = Mp+Mp
        RA*x - WX*x/2 = 2Mp
        Mp=(RA*X - WX*X/2)/2
        differentiate the above Eq wrt dMp/dx=0
        0=RA/2-W*2X/4'''
        X=RA/W;
        print("Max BM occur @ distance X from left support=",X ,"Meters");
        #d=delta
        t1=1;
        d=t1*X;
        t2=d/l-X;
        d1=(d/(l-X))*l/2;
        
        ewd=(W/2*l/2*d1)-(W/2*d*l);
        iwd = calculateMp1(t1,t2);
        Mp =ewd/iwd;
        print("Plastic Moment(Mp)=" , Mp, "kN-m");
    else:
        w1 = int(input("Enter work load 1: "));
        w2 = int(input("Enter work load 2: "));
        l = int(input("Enter total length: "));
        l1 = int(input("Enter length1 at w1: "));
        l2 = int(input("Enter length2 at w2: "));
        t1 = 1;

        d = t1*l1;
        t2 = d / l2;
        d1 = (d/l2)*(l - l2);
        ewd=w1*d+w2*d1;
        iwd = calculateMp1(t1,t2);
        mp1 =ewd/iwd;
        
        #t1 = d/l2;
        d = t1*l2;
        t2 = d / (l - l2);
        d1 = (d/l2) * l1;
        ewd=w1*d1+w2*d;
        iwd = calculateMp1(t1,t2);
        mp2=ewd/iwd;
        
        
        print("mp1:  ",mp1);
        print("mp2:  ",mp2);
        if(mp1 > mp2):
            print("Plastic Moment(Mp)=" , mp1, "kN-m");
        else:
            print("Plastic Moment (Mp)= ", mp2,"kN-m");
else:
    v = input("Enter a or b or c or d: ")
    if(v == 'a'):
        W = int(input("Enter the load: "))
        L = int(input("Enter the length: "))
        Wu=W*1.5;
        m=int(input("enter load acting fm ls: "))
        n=L-m;
        Mp = (Wu*m*n) / (2*L) ;
        print("Plastic Moment (Mp)= ", Mp, "kN-m");
    elif(v=='b'):
        W = int(input("Enter the load: "))
        L = int(input("Enter the length: "))
        Wu=W*1.5;
        Mp = (Wu*L)/16;
        print("Plastic Moment (Mp)= ", Mp, "kN-m");
    elif(v== 'c'):
        W=int(input("Enter udl: "))
        l=int(input("Enter total length of beam: "))
        l1=int(input("Enter the length load is acting from ls: "))
        #Taking momemt about B, then Reaction 
        Dwr= W*l1*(l1/2+(l-l1));
        RA=Dwr/l;
        print("Support Reaction at A = ", RA, "kN");
        '''equating max BM and plastic moment of the section
        RA*x - WX*x/2 = Mp+Mp
        RA*x - WX*x/2 = 2Mp
        Mp=(RA*X - WX*X/2)/2
        differentiate the above Eq wrt dMp/dx=0
        0=RA/2-W*2X/4'''
        X=RA/W;
        print("Max BM occur @ distance X from left support=",X ,"Meters");
        #d=delta
        t1=1;
        d=t1*X;
        t2=d/l-X;
        d1=(d/(l-X))*l/2;
        
        ewd=(W/2*l/2*d1)-(W/2*d*l);
        iwd = calculateMp2(t1,t2,W,d);
        Mp =ewd/iwd;
        print("Plastic Moment(Mp)=" , Mp, "kN-m");
    else:
        w1 = int(input("Enter work load 1: "));
        w2 = int(input("Enter work load 2: "));
        l = int(input("Enter total length: "));
        l1 = int(input("Enter length1 at w1: "));
        l2 = int(input("Enter length2 at w2: "));
        t1 = 1;

        d = t1*l1; #d=deflectioln due to w1; d1=deflection due to w2
        t2 = d / l2; #t1=theta1; t2=theta2
        d1 = (d/l2)*(l - l2);
        ewd=w1*d+w2*d1;
        iwd = calculateMP(t1,t2, w1, w2,d, d1);
        mp1 =ewd/iwd;
        
        #t1 = d/l2;
        d = t1*l2;
        t2 = d / (l - l2);
        d1 = (d/l2) * l1;
        ewd=w1*d1+w2*d;
        iwd = calculateMP(t1,t2 ,w1,w2,d,d1);
        mp2=ewd/iwd;
        
        
        print("mp1:  ",mp1);
        print("mp2:  ",mp2);
        if(mp1 > mp2):
            print("Plastic Moment(Mp)=" , mp1, "kN-m");
        else:
            print("Plastic Moment (Mp)= ", mp2,"kN-m");
