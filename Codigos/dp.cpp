#include <bits/stdc++.h>
#include <chrono>
#include <iomanip>
#include "utils.hpp"
using namespace std;

/* DP se encarga de encontrar la distancia minima de edicion para transformar S1 en S2
*  Parametros
*   - S1 cadena a transformar
*   - S2 cadena invariante
*   - indice1 es un entero que se utirliza para recorrer S1
*   - indice2 es un entero que se utirliza para recorrer S2
*   - Cache es una matriz en la que se guardan los valores que se vayan calculando
*/
int DP(string &S1, string &S2, int indice1 , int indice2, vector<vector<int>> &Cache){

    // Se verifica si el problema ya se ha calculado antes
    if (Cache[indice1][indice2] != -1) {
        return Cache[indice1][indice2];
    }

    // Caso base
    if (indice1 == S1.size() && indice2 == S2.size()) {
        return Cache[indice1][indice2] = 0;
    }

    if (indice1 == S1.size()) {
        // Resta insertar el resto de los caracteres en S2
        return Cache[indice1][indice2] = costo_ins(S2[indice2]) + DP(S1,S2,indice1,indice2+1, Cache);
    }

    if (indice2 == S2.size()) {
        // Resta eliminar el resto de los caracteres en S1
        return Cache[indice1][indice2] = costo_del(S1[indice1]) + DP(S1,S2,indice1+1,indice2, Cache);
    }

    int elim = costo_del(S1[indice1]) + DP(S1, S2, indice1 + 1, indice2, Cache);
    int ins = costo_ins(S2[indice2]) + DP(S1, S2, indice1, indice2 + 1, Cache);
    int remp = costo_sub(S1[indice1], S2[indice2]) + DP(S1, S2, indice1 + 1, indice2 + 1, Cache);
    int transp = INT_MAX;

    if (indice1 + 1 < S1.size() && indice2 + 1 < S2.size() && S1[indice1] == S2[indice2 + 1] && S1[indice1 + 1] == S2[indice2]) {
        transp = costo_trans(S1[indice1], S1[indice1 + 1]) + DP(S1, S2, indice1 + 2, indice2 + 2, Cache);
    }
    
    return Cache[indice1][indice2] = min({elim, ins, remp, transp});
}

int main(){
    // Se cargan las matrices de los costos en las variables globales
    leerArchivo("cost_delete.txt",1,1);
    leerArchivo("cost_insert.txt",1,2);
    leerArchivo("cost_replace.txt",2,3);
    leerArchivo("cost_transpose.txt",2,4);

    int casos,n,m;
    cin >> casos;

    // Abrir el archivo de salida
    ofstream outFile("DP.txt");
    while(casos!=0){

        cin >> n >> m;
        string S1;
        string S2;

        if(n!=0){cin >> S1;}else{S1 = "";}

        if(m!=0){cin >> S2;}else{S2 = "";}

        auto inicio = chrono::high_resolution_clock::now();

        // Creacion de la matriz de cache
        vector<vector<int>> Matriz(S1.size() + 1, vector<int>(S2.size() + 1, -1));

        // Se calcula la distancia minima
        int distancia = DP(S1, S2, 0, 0, Matriz);

        auto fin = chrono::high_resolution_clock::now();


        auto memory = Memoria(Matriz);

        // Calcular la duración en milisegundos con decimales
        auto duracion = std::chrono::duration<double, std::milli>(fin - inicio);

        // Se reconstruyen las operaciones realizadas
        //vector<string> camino = reconstruirCamino(S1,S2,Matriz);
        //for(auto elem: camino){cout << elem << endl;}

        // Escribir los resultados en el archivo
        outFile << distancia << "," << S1.length() << "," << S2.length() << "," 
                << fixed << setprecision(6) << duracion.count() << "," 
                << memory << endl;
        casos--;
    }

    // Cerrar el archivo
    outFile.close();
    return 0;
}