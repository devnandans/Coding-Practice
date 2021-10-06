#Given two polynomials represented by two arrays that contains the coefficients of poynomials, returns the polynomial in form of array formed after multiplication of given polynomials.




class Solution{
    public:
    vector<int>polyMultiply(int Arr1[], int Arr2[], int M, int N)
    {
        // code here
        //int v1[M*N];
        vector<int> v1(M+N-1,0);
        for (int i = 0; i<M+N-1; i++)v1[i] = 0;
        for(int i=0;i<M;i++)
        {
           for(int j=0;j<N;j++)
           {
               v1[i+j] =v1[i+j] +Arr1[i]*Arr2[j];
               
           }
           
        }
     }
};

// { Driver Code Starts.
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int M, N;
        cin >> M >> N;
        int Arr1[M], Arr2[N];
        for(int i=0;i<M;i++)cin>>Arr1[i];
        for(int i=0;i<N;i++)cin>>Arr2[i];
        Solution ob;
        vector<int>ans=ob.polyMultiply(Arr1,Arr2,M,N);
        for(int i=0;i<M+N-1;i++)cout<<ans[i]<<" ";
        cout<<endl;
    }
    return 0;