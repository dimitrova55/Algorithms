// Dilyana Dimitrova
// ID: 202055501

#include <iostream>

using namespace std;

int partitionArray(int arr[], int left, int right)
{
    int pivot = arr[left];
    int i = right + 1;                        // "i" - for the pivot index

    //traversing the array from the right side to the left
    for(int j = right; j > left; j--)
    {
        if(arr[j] >= pivot)                 // if we find an element bigger than the pivot,
            swap(arr[j], arr[--i]);         // we switch their places
    }
    swap(arr[--i], arr[left]);              // after traversing the array we put the pivot in a sort position

    return i;                               // return the pivot's index
}

void myQuicksort(int arr[], int left, int right)
{
    if(left < right)
    {
        int pivot = partitionArray(arr, left, right);    // calling on the partitionArray function
                                                         // to find the pivot index
                                                         // recursively calling the myQuicksort function
        myQuicksort(arr, left, pivot - 1);               // on the left side of the array
        myQuicksort(arr, pivot + 1, right);              // on the right side of the array
    }
}


int main()
{
    int arr[] = {15, 22, 13, 27, 12, 10, 20, 25};
    int length = sizeof(arr) / sizeof(arr[0]);

    cout << "before sorting: ";

    for(int i = 0; i < length; i++)
        cout << arr[i] << " ";
    cout << endl;

    myQuicksort(arr, 0, length-1);

    cout << "after sorting: ";

    for(int i = 0; i < length; i++)
        cout << arr[i] << " ";
    cout << endl;


    return 0;
}
