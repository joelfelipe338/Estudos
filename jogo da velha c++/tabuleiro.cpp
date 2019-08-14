#include <iostream>
#include <string>
#include "tabuleiro.h"
using namespace std;

void mostraTab(char val[]){
    int cont = 0;
    char tab[5][7];
    for(int i = 0; i< 5; i++){
        for(int j=0;j<7;j++){
            if(i == 0 || i == 4){
                tab[i][j] = '-';
            }else if(j%2 == 0){
                tab[i][j] = '|';
            }else{
                tab[i][j] = val[cont];
                cont++;
            }
        }
    }

    for(int i = 0; i< 5; i++){
        for(int j=0;j<7;j++){
            cout << tab[i][j];
        }
        cout << endl;
    }
}

void zerarTab(char val[]){
    for(int i =0 ; i < 9; i++){
        val[i] = (i+1) + '0';
    }
}

bool completoTab(char val[]){
    int complete = 0;
    for(int i = 0; i < 9; i++){
        if(val[i] == 'x' || val[i] == 'o'){
            complete++;
        }
    }
    if(complete == 9){
        return true;
    }else return false;
}

bool fazerJogada(char val[], int pos, char jogada){
    if(val[pos-1] != 'x' && val[pos-1] != 'o'){
        val[pos-1] = jogada;
        return true;
    }else{
        return false;
    }
}
