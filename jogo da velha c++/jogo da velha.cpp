#include <iostream>
#include <cstdlib>
#include <conio.h>
//#include "tabuleiro.h"
//#include "jogo.h"

using namespace std;


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
*/


void contarRodada(int *rodada){
    *rodada += 1;
}

bool ganhou(char val[]){
  char op = 'x';
  for(int i = 0;i < 2;i++){
    if(val[0]== op && val[1] == op && val[2] == op){
      return true;
    }else if(val[3]== op && val[4] == op && val[5] == op){
      return true;
    }else if(val[6]== op && val[7] == op && val[8] == op){
      return true;
    }else if(val[0]== op && val[3] == op && val[6] == op){
      return true;
    }else if(val[1]== op && val[4] == op && val[7] == op){
      return true;
    }else if(val[2]== op && val[5] == op && val[8] == op){
      return true;
    }else if(val[0]== op && val[4] == op && val[8] == op){
      return true;
    }else if(val[2]== op && val[4] == op && val[6] == op){
      return true;
    }else {
      return false;
    }
    op = 'o';
  }
}

void jogada(char val[],char op){
    int jog;
    bool sucess = false;
    do{
        cout << "qual sua jogada?"<<endl;
        cin >> jog;
        if(fazerJogada(val,jog,op)){
            sucess = true;
        }else{
            cout << "jogada invalida!!!"<<endl;
        }
    }while(sucess != true);
    system("clear||cls");

}

void iniciaJogo(char val[],int rod){
   bool venceu = false;
   cout << rod <<"° rodada:"<<endl;
    mostraTab(val);
    while(venceu != true){
        cout << "jogador 1:"<<endl;
        jogada(val,'x');
        cout << rod <<"° rodada:"<<endl;
        mostraTab(val);
        if(ganhou(val)) {venceu = true;break;}
        if(completoTab(val)) break;
        cout << "jogador 2:"<<endl;
        jogada(val,'o');
        cout << rod <<"° rodada:"<<endl;
        mostraTab(val);
        if(ganhou(val)) {venceu = true;break;}
    }
    if(venceu){
      cout << "venceu o jogo parabens"<<endl;
      zerarTab(val);
    }else{
      cout << "deu velha!!"<<endl ;
      zerarTab(val);
    }
    cout << "Precione Qualquer tecla para continuar..." << endl;
    getch();
    system("clear||cls");
}
int main(){
    int rodadas = 1;
    char valor[9] = {'1','2','3','4','5','6','7','8','9'};
    while(1){
      iniciaJogo(valor,rodadas);
      contarRodada(&rodadas);
    }

    return 0;
}
