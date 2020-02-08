#include <iostream>
#include <cstdlib>
#include <string>
#include "tabuleiro.h"


using namespace std;




void jogadorInfo(string nome1,int vit1,string nome2,int vit2){
     cout << "------Pontuação------"<<endl;
     cout << nome1 << ": "<<vit1<<" vitoria(s)."<<endl;
     cout << nome2 << ": "<<vit2<<" vitoria(s)."<<endl;
}

void jogada(char val[],char op,string jogador){
    int jog;
    bool sucess = false;
    do{
        cout << "qual sua jogada?"<<endl;
        cin >> jog;
        if(jog > 0 && jog < 10 && fazerJogada(val,jog,op)){
            sucess = true;
        }else{
            system("clear||cls");
            cout << "jogada invalida!!!"<<endl;
            mostraTab(val);
            cout << jogador <<" eh a sua vez,"<<endl;
        }
    }while(sucess != true);
    system("clear||cls");
}

string vezJogador(string jogAtual,string nome1,string nome2){
    if(jogAtual == nome1){
        jogAtual = nome2;
    }else{
        jogAtual = nome1;
    }
    return jogAtual;
}

void jogadores(string *nome1, string *nome2){
    cout << "digite o nome do jogador 1:" <<endl;
    getline(cin, *nome1);
    cout << "digite o nome do jogador 2:" <<endl;
    getline(cin, *nome2);
    system("clear||cls");
}

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
    }else if(i==1){
      return false;
    }
    op = 'o';
  }
}

void iniciaJogo(char val[],int rod,string nome1,string nome2,int *vit1,int *vit2){
   bool venceu = false;
   char jog = 'x';
   string jogAtual;
   if(rod%2 == 0){
        jogAtual = nome1;
   }else{
       jogAtual = nome2;
   }
   cout << "rodada: "<<rod<<endl;
    mostraTab(val);
    while(venceu != true){
        jog = 'x';
        jogAtual = vezJogador(jogAtual,nome1,nome2);
        cout <<jogAtual <<" eh a sua vez,"<<endl;
        jogada(val,jog,jogAtual);
        cout << "rodada: "<<rod<<endl;
        mostraTab(val);
        if(ganhou(val)) {venceu = true;break;}
        if(completoTab(val)) break;
        jogAtual = vezJogador(jogAtual,nome1,nome2);
        cout <<jogAtual <<" eh a sua vez,"<<endl;
        jog = 'o';
        jogada(val,jog,jogAtual);
        cout <<"rodada: "<<rod<<endl;
        mostraTab(val);
        if(ganhou(val)) {venceu = true;}
    }
    if(venceu == true){
      cout << jogAtual <<" venceu o jogo parabens"<<endl;
      if(jogAtual == nome1){
          *vit1 += 1;
      }else{
          *vit2 += 1;
      }
    }else{
      *vit2 += 1;
      *vit1 += 1;
    }
    zerarTab(val);
    system("clear||cls");
}

bool continuar(){
    int op=0;
    while(op<1 || op>2){
        cout << "Proxima partida? "<<endl;
        cout<<"[1] Sim."<<endl;
        cout<<"[2] Nao."<<endl;
        cin >> op;
        if(op == 2){
            return false;
        }else{
            system("clear||cls");
            return true;
        }
    }
}


int main(){
    int rodadas = 1,vit1=0,vit2=0;
    bool ativo = true;
    char valor[9] = {'1','2','3','4','5','6','7','8','9'};
    string nome1,nome2;
    jogadores(&nome1,&nome2);
    while(ativo){
      iniciaJogo(valor,rodadas,nome1,nome2,&vit1,&vit2);
      contarRodada(&rodadas);
      jogadorInfo(nome1,vit1,nome2,vit2);
      ativo = continuar();
    }
    cout << "Saindo... Obrigado por Jogar!"<<endl;
    return 0;
}
