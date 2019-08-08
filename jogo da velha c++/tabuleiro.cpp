#include <iostream>
#include "tabuleiro.h"
using namespace std;

void mostraTab(){
    char tab[5][7];
    for(int i = 0; i< 5; i++){
        for(int j=0;j<7;j++){
            if(i == 0 || i == 4){
                tab[i][j] = '-';
            }else if(j%2 == 0){
                tab[i][j] = '|';
            }else{
                tab[i][j] = ' ';
            }
        }
    }

    for(int i = 0; i< 5; i++){
        for(int j=0;j<7;j++){
            cout << tab[i][j];
        }
        cout << endl;
    }
    return 0;
}
