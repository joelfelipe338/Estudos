#ifndef _JOGO_H_
#define JOGO_H


void iniciaJogo(char val[],int rod,string nome1,string nome2,int *vit1,int *vit2);
void jogadores(string *nome1, string *nome2);
void contarRodada(int *rodada);
bool ganhou(char val[]);
bool continuar();

#endif 
