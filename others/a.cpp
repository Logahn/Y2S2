#include <iostream>
#include <vector>
using namespace std;

void swap(int *xp, int *yp)
{
    int temp = *xp;
//     *xp = *yp;
//     *yp = temp;
 }
int main() 
{
    int n, m;
    cout << "Enter N: " << endl;
    cin >> n;
    cout << "Enter M"<< endl;
    cin >> m;


    int arr[n];
    cout<< "ENter Arrays: " << endl;
    for (int i =0; i <n; i++) 
    {
        cin >> arr[i];
    }
    cout << "Array:" <<endl;
    for(int i = 0; i < n; i++) 
    {
       
            while(i % m != 0)
            {
               if (arr[i] > arr[i+1])
                 swap(&arr[i], &arr[i+1]);

            }
         if(i % m == 0)
        {
            cout << "\n" ;
        }
        cout << arr[i];
    }
    


    // return 0;

    int N;
    int arr[n];
    cout << "Enter lenght of circle";
    cin >> N;
    int cycle;
    cout << "Enter break of circle";
    cin >> cycle;
    int count = 0;
    vector<int> arr;
    while(count < cycle)
    {
        for(int i = 1;  i <= N; i++)
        {
        //   int arr.push_back(i);
        }
            for(int i = 1;  i <= N; i++)
        {
            if(arr[i] % cycle == 0)
            {
                cout << "\n" ;
            }

        count ++;

    }
    for(int i = 1; i <= N; i++)
    {
        cout << arr[i] << " ";
    }

}
}