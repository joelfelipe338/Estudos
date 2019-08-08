#include <iostream>
#include "tabuleiro.h"
#include "jogo.h"

using namespace std;

int main(){
    int rodadas = 0;
    char valor[9] = {'1','2','3','4','5','6','7','8','9'};
    bool venceu = false;
    while(venceu != true){

    }
    return 0;
}


void zerarTab(char val[]){
    for(int i =0 ; i < 9; i++){
        val[i] = (i+1) + '0';
    }
}

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
/*
void jogadores(char *nome1, char *nome2){
    cout << "digite o nome do jogador 1:" <<endl;
    getline(cin, nome1);
    cout << "digite o nome do jogador 2:" <<endl;
     getline(cin, nome2);
}
/*
void iniciaJogo(){
    mostraTab();
}
*/
void contarRodada(int *rodada){
    *rodada += 1;
}

bool ganhou(){
    if(completoTab()){
        zerarTab();
        return true;
    }else{
        return false;
    }
}
//-------
//| | | |
//| | | |
//| | | |
//-------
//
