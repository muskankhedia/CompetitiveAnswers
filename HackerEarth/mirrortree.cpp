#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <limits.h>

using namespace std;

typedef struct node{
    int val, lh, rh;
    struct node *left, *right;
}node;
// Allocates new nodes.
node * getNode(int val){
    node *ret = (node*)calloc(1, sizeof(node));
    ret->val = val;
    return ret;
} 
int maxx; // our Diameter.
//Assign maxximum Depth to each node.
int query(node *ptr){
    if(ptr){
        // cout << "ptr " << ptr << endl;
        // cout << "aptr " << &ptr << endl;
        ptr->lh = query(ptr->left);
        cout << "Left" << ptr -> lh << endl;
        ptr->rh = query(ptr->right);
        cout << "Right" << ptr -> rh << endl;
        if (ptr->lh + ptr->rh + 1  > maxx)
            maxx = ptr->lh + ptr->rh + 1;
        return ( ptr->lh > ptr->rh ? ptr->lh : ptr->rh) + 1;
    }
    else
        return 0;
}

int searchNode(node *ptr, int value1, int value2, string str) {
    if (ptr) {
        ptr -> lh = searchNode(ptr -> left);
        if (ptr -> data == value1 ) {
            if (str[0] == 'L') {
                if(ptr->left == NULL)
                    ptr->left = getNode(0);
                ptr = ptr->left;
                ptr->val = value2;
            }
            if (str[0] == 'R') {
                if(ptr->right == NULL)
                    ptr->right = getNode(0);
                ptr = ptr->right;
                ptr->val = value2;
            }
        }

        ptr->rh = query(ptr->right);
        if (ptr -> data == value1 ) {
            if (str[0] == 'L') {
                if(ptr->left == NULL)
                    ptr->left = getNode(0);
                ptr = ptr->left;
                ptr->val = value2;
            }
            
            if (str[0] == 'R') {
                if(ptr->right == NULL)
                    ptr->right = getNode(0);
                ptr = ptr->right;
                ptr->val = value2;
            }
        }

    }
}

int main()
{
    maxx = INT_MIN;
    node *root = NULL,*ptr;
    int n, q, i ;
    scanf("%i %i",&n,&q);
    root = getNode(1);
    char str[12345];
    while(--n){
        scanf("%d %d %s", p, c, str);
        // scanf(" %s",str);
        i = 0;
        ptr = root;
        searchNode(root, p, c, str)
        while(str[i] && ptr ){
            if(str[i] == 'L'){
                if(ptr->left == NULL)
                    ptr->left = getNode(0);
                ptr = ptr->left;

            }
            else{
                if(ptr->right == NULL)
                    ptr->right = getNode(0);
                ptr = ptr->right;

            }
            i++;
        }
        scanf("%i", &x);
        ptr->val = x;

    }
    query(root);
    printf("%i", maxx);
    return 0;
}