class Sol:
    def max_prod(self,arr):
        s_arr=sorted(arr)
        if (s_arr[0]>=0):
            return s_arr[-1]*s_arr[-2]*s_arr[-3]
        elif s_arr[1]>=0:
            return s_arr[-1] * s_arr[-2] * s_arr[-3]
        elif s_arr[-1]<0:
            return s_arr[0] * s_arr[1] * s_arr[2]
        elif s_arr[-1]==0:
            return 0
        else:
            return max(s_arr[-1]*s_arr[-2]*s_arr[-3],s_arr[0] * s_arr[1]*s_arr[-1])

if __name__ == '__main__':
    p=Sol()
    print(p.max_prod([1,4,8,2,-10,-9,-11]))
