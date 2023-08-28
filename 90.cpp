#include<iostream>
#include<stdlib.h>
using namespace std;
int main(){

//crear arreglo de unidades de tiempo
int a[4];

//crear unidades de tiempo
float h,m,s,c;
system("cls");

//pedir unidades de tiempo
cout<<"ingrese las horas a contabilizar: "<<endl;
cin>>a[0];
cout<<"ingrese los minutos a contabilizar: "<<endl;
cin>>a[1];
cout<<"ingrese los segundos a contabilizar: "<<endl;
cin>>a[2];

//inicializar unidades de tiempo
h=0;
m=0;
s=0;

//si el tiempo sobrepasa topen de unidades
a[3]=0;
if(a[0]>99 || a[1]>59 || a[2]>59){
cout<<"no se puede contabilizar hasta estos valores..."<<endl;
}
else{

//aumentar hata llegar al valor dado
while(h<a[0] || m<a[1] ||s<a[2]){
cout<<h<<":"<<m<<":"<<s<<":"<<a[3]<<endl;
a[3]=a[3]+25;
system("cls");
if(a[3]==100){
a[3]=0;
if(a[3]==0){
cout<<h<<":"<<m<<":"<<s<<":"<<a[3]<<endl;
s++;
system("cls");
if(s==60){
s=0;
if(s==0){
cout<<h<<":"<<m<<":"<<s<<":"<<a[3]<<endl;
m++;
system("cls");
if(m==60){
m=0;
if(m==0){
h++;
cout<<h<<":"<<m<<":"<<s<<":"<<a[3]<<endl;
system("cls");
}
}
}
}
}
}
}
}
if(h==a[0] && m==a[1] &&s==a[2]){
cout<<h<<":"<<m<<":"<<s<<":"<<a[3]<<endl;
cout<<"el conteo ha finalizado"<<endl;
}
system("pause");
return 0;
}
