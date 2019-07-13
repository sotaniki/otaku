import csv
import numpy as np

mode1 = input("Pb/Pb correction mode: 1.NIST SRM 612 or 2.91500 zircon: ")
mode2 = input("Pb/U correction mode: 1.NIST SRM 612 or 2.91500 zircon: ")

x = input("number of unknowns: ")



x = int(x)+6

list = ["206Pb/238U", "207Pb/235U", "208Pb/232Th","207Pb/206Pb", "208Pb/206Pb"]
ref_nist = [0.254525667358606, 96.4094995340435,  0.548399498523207, 0.90726, 2.164]
ref_zircon = [0.17928,1.86777719,0.054,0.07556,0.855]

ratio = []
ratio_err = []

len = len(list)

ls = []
num = 0

f = open("output.csv",'r').readlines()
for line in f:
    a = line.split(',')
    ls.append(a)
    num = num+1

if int(mode2) == 1:
    for j in range(3):
        seq = int(num//(6+x))
        f_pb_u = []
        err_f_pb_u = []

        for i in range(seq):
            pbu = []
            pbu.append(float(ls[1+x*i][14+2*j]))
            pbu.append(float(ls[2+x*i][14+2*j]))
            pbu.append(float(ls[3+x*i][14+2*j]))
            pbu.append(float(ls[1+x*(i+1)][14+2*j]))
            pbu.append(float(ls[2+x*(i+1)][14+2*j]))
            pbu.append(float(ls[3+x*(i+1)][14+2*j]))

            sum = 0
            sum_sq = 0
            for item in pbu:
                sum = sum+item
                b = sum/6
            for item in pbu:
                sum_sq = sum_sq + (item-b)**2
                #print(sum_sq)
            f_pb_u.append(ref_nist[j]/b)
            err_f_pb_u.append(np.sqrt(sum_sq/5))

        c = []
        d = []
        for i in range(x):
            for k in range(seq):
                c.append(float(ls[1+i+k*x][14+2*j])*f_pb_u[k])
                d.append(c[i+k*x]*np.sqrt((float(ls[1+i+k*x][15+2*j])/float(ls[1+i+k*x][14+2*j]))**2+(err_f_pb_u[k]/f_pb_u[k])**2))
        ratio.append(c)
        ratio_err.append(d)


    if int(mode1) == 1:

        for j in range(2):

            seq = int(num//(6+x))
            f_pb_pb = []
            err_f_pb_pb = []

            for i in range(seq):
                pb = []
                pb.append(float(ls[1+x*i][20+2*j]))
                pb.append(float(ls[2+x*i][20+2*j]))
                pb.append(float(ls[3+x*i][20+2*j]))
                pb.append(float(ls[1+x*(i+1)][20+2*j]))
                pb.append(float(ls[2+x*(i+1)][20+2*j]))
                pb.append(float(ls[3+x*(i+1)][20+2*j]))

                sum = 0
                sum_sq = 0
                for item in pb:
                    sum = sum+item
                    b = sum/6
                for item in pb:
                    sum_sq = sum_sq + (item-b)**2
                    #print(sum_sq)
                f_pb_pb.append(ref_nist[j+3]/b)
                err_f_pb_pb.append(np.sqrt(sum_sq/5))

            c = []
            d = []
            for i in range(x):
                for k in range(seq):
                    c.append(float(ls[1+i+k*x][20+2*j])*f_pb_pb[k])
                    d.append(c[i+k*x]*np.sqrt((float(ls[1+i+k*x][21+2*j])/float(ls[1+i+k*x][20+2*j]))**2+(err_f_pb_pb[k]/f_pb_pb[k])**2))
            ratio.append(c)
            ratio_err.append(d)


        for i in range(x):
            ratio.append(ratio[0][i]*ratio[3][i])


    elif int(mode1) == 2:

        for j in range(2):
            seq = int(num//(6+x))
            f_pb_pb = []
            err_f_pb_pb = []

            for i in range(seq):
                pb = []
                pb.append(float(ls[4+x*i][20+2*j]))
                pb.append(float(ls[5+x*i][20+2*j]))
                pb.append(float(ls[6+x*i][20+2*j]))
                pb.append(float(ls[4+x*(i+1)][20+2*j]))
                pb.append(float(ls[5+x*(i+1)][20+2*j]))
                pb.append(float(ls[6+x*(i+1)][20+2*j]))

                sum = 0
                sum_sq = 0
                for item in pb:
                    sum = sum+item
                    b = sum/6
                for item in pb:
                    sum_sq = sum_sq + (item-b)**2
                    #print(sum_sq)
                f_pb_pb.append(ref_zircon[j+3]/b)
                err_f_pb_pb.append(np.sqrt(sum_sq/5))

            c = []
            d = []
            for i in range(x):
                for k in range(seq):
                    c.append(float(ls[1+i+k*x][18+2*j])*f_pb_pb[k])
                    d.append(c[i+k*x]*np.sqrt((float(ls[1+i+k*x][19+2*j])/float(ls[1+i+k*x][18+2*j]))**2+(err_f_pb_pb[k]/f_pb_pb[k])**2))
            ratio.append(c)
            ratio_err.append(d)




    g = open('isotopic_ratio.csv', 'w')
    writer = csv.writer(g, lineterminator='\n')



    csvlist = []

    csvlist.append("206Pb/238U")
    csvlist.append("error")
    csvlist.append("207Pb/235U")
    csvlist.append("error")
    csvlist.append("208Pb/232Th")
    csvlist.append("error")
    csvlist.append("207Pb/206U")
    csvlist.append("error")
    csvlist.append("208Pb/206Pb")
    csvlist.append("error")
    writer.writerow(csvlist)



    for i in range(x):
        csvlist = []
        for j in range(len):
            csvlist.append(ratio[j][i])
            csvlist.append(ratio_err[j][i])
        writer.writerow(csvlist)


    g.close()


elif int(mode2) == 2:
    for j in range(3):
        seq = int(num//(6+x))
        f_pb_u = []
        err_f_pb_u = []
        ave_pb_u = []

        for i in range(seq):
            pbu = []
            pbu.append(float(ls[4+x*i][14+2*j]))
            pbu.append(float(ls[5+x*i][14+2*j]))
            pbu.append(float(ls[6+x*i][14+2*j]))
            pbu.append(float(ls[4+x*(i+1)][14+2*j]))
            pbu.append(float(ls[5+x*(i+1)][14+2*j]))
            pbu.append(float(ls[6+x*(i+1)][14+2*j]))

            sum = 0
            sum_sq = 0
            for item in pbu:
                sum = sum+item
                b = sum/6
            for item in pbu:
                sum_sq = sum_sq + (item-b)**2

                #print(sum_sq)
            ave_pb_u.append(b)
            f_pb_u.append(ref_zircon[j]/b)
            err_f_pb_u.append(np.sqrt(sum_sq/5))

        c = []
        d = []
#        print(ave_pb_u)
#        print(f_pb_u)
#        print(seq)
        for i in range(x):
            for k in range(1):
                c.append(float(ls[1+i+k*x][14+2*j])*f_pb_u[k])
                d.append(c[i+k*x]*np.sqrt((float(ls[1+i+k*x][15+2*j])/float(ls[1+i+k*x][14+2*j]))**2+(err_f_pb_u[k]/ave_pb_u[k])**2))
                #print((float(ls[1+i+k*x][15+2*j])/float(ls[1+i+k*x][14+2*j])))
#                print((err_f_pb_u[k]), ave_pb_u[k])
#                print((err_f_pb_u[k]/ave_pb_u[k]))
        ratio.append(c)
        ratio_err.append(d)

    if int(mode1) == 1:

        for j in range(2):

            seq = int(num//(6+x))
            f_pb_pb = []
            err_f_pb_pb = []
            ave_pb_pb = []

            for i in range(seq):
                pb = []
                pb.append(float(ls[1+x*i][20+2*j]))
                pb.append(float(ls[2+x*i][20+2*j]))
                pb.append(float(ls[3+x*i][20+2*j]))
                pb.append(float(ls[1+x*(i+1)][20+2*j]))
                pb.append(float(ls[2+x*(i+1)][20+2*j]))
                pb.append(float(ls[3+x*(i+1)][20+2*j]))

                sum = 0
                sum_sq = 0
                for item in pb:
                    sum = sum+item
                    b = sum/6
                for item in pb:
                    sum_sq = sum_sq + (item-b)**2
                    #print(sum_sq)
                f_pb_pb.append(ref_nist[j+3]/b)
                err_f_pb_pb.append(np.sqrt(sum_sq/5))
                ave_pb_pb.append(b)

            c = []
            d = []
            for i in range(x):
                for k in range(1):
                    c.append(float(ls[1+i+k*x][20+2*j])*f_pb_pb[k])
                    d.append(c[i+k*x]*np.sqrt((float(ls[1+i+k*x][21+2*j])/float(ls[1+i+k*x][20+2*j]))**2+(err_f_pb_pb[k]/ave_pb_pb[k])**2))
            ratio.append(c)
            ratio_err.append(d)

        e = []
        f = []
        for i in range(x):
            e.append(ratio[0][i]*ratio[3][i]*137.88)
            f.append(e[i]*np.sqrt((ratio_err[0][i]/ratio[0][i])**2+(ratio_err[3][i]/ratio[3][i])**2))#print(ratio[0][i]*ratio[3][i]*137.88)
            #ratio_err.append()
        ratio.append(e)
        ratio_err.append(f)
    #    print(ratio[5],ratio_err[5])


    elif int(mode1) == 2:

        for j in range(2):
            seq = int(num//(6+x))
            f_pb_pb = []
            err_f_pb_pb = []

            for i in range(seq):
                pb = []
                pb.append(float(ls[4+x*i][20+2*j]))
                pb.append(float(ls[5+x*i][20+2*j]))
                pb.append(float(ls[6+x*i][20+2*j]))
                pb.append(float(ls[4+x*(i+1)][20+2*j]))
                pb.append(float(ls[5+x*(i+1)][20+2*j]))
                pb.append(float(ls[6+x*(i+1)][20+2*j]))

                sum = 0
                sum_sq = 0
                for item in pb:
                    sum = sum+item
                    b = sum/6
                for item in pb:
                    sum_sq = sum_sq + (item-b)**2
                    #print(sum_sq)
                f_pb_pb.append(ref_zircon[j+3]/b)
                err_f_pb_pb.append(np.sqrt(sum_sq/5))

            c = []
            d = []
            for i in range(x):
                for k in range(seq):
                    c.append(float(ls[1+i+k*x][18+2*j])*f_pb_pb[k])
                    d.append(c[i+k*x]*np.sqrt((float(ls[1+i+k*x][19+2*j])/float(ls[1+i+k*x][18+2*j]))**2+(err_f_pb_pb[k]/f_pb_pb[k])**2))
            ratio.append(c)
            ratio_err.append(d)




    g = open('isotopic_ratio.csv', 'w')
    writer = csv.writer(g, lineterminator='\n')


    csvlist = []

    csvlist.append("206Pb/238U")
    csvlist.append("error")
    csvlist.append("207Pb/235U_1")
    csvlist.append("error")
    csvlist.append("208Pb/232Th")
    csvlist.append("error")
    csvlist.append("207Pb/206U")
    csvlist.append("error")
    csvlist.append("208Pb/206Pb")
    csvlist.append("error")
    csvlist.append("207Pb/235U_2")
    csvlist.append("error")

    writer.writerow(csvlist)

    for i in range(x):
        csvlist = []
        for j in range(len+1):
            csvlist.append(ratio[j][i])
            csvlist.append(ratio_err[j][i])
        writer.writerow(csvlist)


    g.close()



else:
    print("false")
