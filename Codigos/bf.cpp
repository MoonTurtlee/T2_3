#include <bits/stdc++.h>
#include <chrono>
#include <iomanip>
#include "utils.hpp"
using namespace std;

/* BF se encarga de encontrar la distancia minima de edicion para transformar S1 en S2
*  Parametros
*   - S1 cadena a transformar
*   - S2 cadena invariante
*   - indice1 es un entero que se utirliza para recorrer S1
*   - indice2 es un entero que se utirliza para recorrer S2
*/
int BF(string &S1, string &S2, int indice1, int indice2) {

    if (indice1 == S1.size() && indice2 == S2.size()) {
        return 0;
    }

    if (indice1 == S1.size()) {
        // Resta insertar el resto de los caracteres en S2
        return costo_ins(S2[indice2]) + BF(S1,S2,indice1,indice2+1);
    }

    if (indice2 == S2.size()) {
        // Resta eliminar el resto de los caracteres en S1
        return costo_del(S1[indice1]) + BF(S1,S2,indice1+1,indice2);
    }

    int elim = costo_del(S1[indice1]) + BF(S1, S2, indice1 + 1, indice2);
    int ins = costo_ins(S2[indice2]) + BF(S1, S2, indice1, indice2 + 1);
    int remp = costo_sub(S1[indice1], S2[indice2]) + BF(S1, S2, indice1 + 1, indice2 + 1);
    int transp = INT_MAX;

    if (indice1 + 1 < S1.size() && indice2 + 1 < S2.size() && S1[indice1] == S2[indice2 + 1] && S1[indice1 + 1] == S2[indice2]) {
        transp = costo_trans(S1[indice1], S1[indice1 + 1]) + BF(S1, S2, indice1 + 2, indice2 + 2);
    }
    
    return min({elim, ins, remp, transp});
}

int main() {
    // Se cargan las matrices de los costos en las variables globales
    leerArchivo("cost_delete.txt",1,1);
    leerArchivo("cost_insert.txt",1,2);
    leerArchivo("cost_replace.txt",2,3);
    leerArchivo("cost_transpose.txt",2,4);
    int casos, n, m;
    cin >> casos;

    // Abrir el archivo de salida
    ofstream outFile("BF.txt");
    string cache1 = "asdad";
    string cache2 = "asdasd";
    int cacheloader = BF(cache1, cache2, 0, 0);
    while (casos != 0) {
        cin >> n >> m;
        string S1;
        string S2;

        if (n != 0) { cin >> S1; } else { S1 = ""; }
        if (m != 0) { cin >> S2; } else { S2 = ""; }

        // Medir el tiempo de ejecución
        auto inicio = chrono::high_resolution_clock::now();

        // Llamar a la función BF
        int distancia = BF(S1, S2, 0, 0);

        // Medir el tiempo de ejecución
        auto fin = chrono::high_resolution_clock::now();
        auto duracion = chrono::duration<double, std::milli>(fin - inicio);

        string dataset = "";
        
        // Escribir los resultados en el archivo
        outFile << dataset << " " << distancia << "," << S1.length() << "," << S2.length() << "," 
                << fixed << setprecision(6) << duracion.count() << "," 
                << 0 << endl;

        casos--;
    }

    // Cerrar el archivo
    outFile.close();

    return 0;
}
