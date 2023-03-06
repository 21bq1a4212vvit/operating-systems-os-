def findWaitingTime(processes,n,bt,wt,quantum):
    rem_bt=[0]*n
    for i in range(n):
        rem_bt[i]=bt[i]
    t=0
    while(i):
        done=True
        for i in range(n):
            if (rem_bt[i]>0):
                done=False
                if (rem_bt[i]>quantum):
                    t+=quantum
                    rem_bt[i]-=quantum
                else:
                    t=t+rem_bt[i]
                    wt[i]=t-bt[i]
                    rem_bt[i]=0
        if(done==True):
            break
def findTurnAroundTime(processes,n,bt,wt,tat):
    for i in range(n):
        tat[i]=bt[i]+wt[i]
def findAvgTime(processes,n,bt,quantum):
    wt=[0]*n
    tat=[0]*n
    findWaitingTime(processes,n,bt,wt,quantum)
    findTurnAroundTime(processes,n,bt,wt,tat)
    print("Processes        BT             WT              TAT")
    total_wt=0
    total_tat=0
    for i in range(n):
        tat_wt=total_wt+wt[i]
        total_tat=total_tat+tat[i]
        print(" ",i+1,"\t\t",bt[i],"\t\t",wt[i],"\t\t",tat[i])
    print("/n avg wt=%5f",(total_wt/n))
    print("avg tat = %5f",(total_tat/n))
if __name__ == "__main__":
    proc=[1,2,3]
    n=3
    burst_time=[0,5,8]
    quantum=2;
    findAvgTime(proc,n,burst_time,quantum)
