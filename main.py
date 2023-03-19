def parallel_processing(n, m, data):
    output = []
    thread=[0]*n

    for i in range(m):
        threadnxt=0
        for j in range(1,n):
            if threadnxt[j]<thread[threadnxt]:
                threadnxt=j
        thread[threadnxt]=thread[threadnxt]+data[i]
        output.append((threadnxt, thread[threadnxt]))
    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int,input().split()))

    result = parallel_processing(n,m,data)
    
    for i in range(m):
        print(result[i][0])
        print(result[i][1])

if __name__ == "__main__":
    main()
