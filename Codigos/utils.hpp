#include <bits/stdc++.h>
using namespace std;
vector<int> eliminar(26);
vector<int> insertar(26);
vector<vector<int>> reemplazar(26, vector<int>(26));
vector<vector<int>> transponer(26, vector<int>(26));

/* 
 // Lee todos los archivos de costos y los guarda en las variables globales
 // Parametros:
 //  −nombreArchivo: nombre del archivo a leer
 //  −dimension: dimension de la matriz que contiene el archivo
 // Return: no existe retorno
*/
void leerArchivo(const string& nombreArchivo, int dimension, int poss) {
    
    ifstream archivo(nombreArchivo);
    if (!archivo.is_open()) {
        cerr << "No se pudo abrir el archivo " << nombreArchivo << endl;
        return;
    }

    if(dimension == 1){
        switch (poss) {
        case 1:
            for (int i = 0; i < 26; ++i) {archivo >> eliminar[i];} break; // Se guardan los costos de eliminar
        case 2:
            for (int i = 0; i < 26; ++i) {archivo >> insertar[i];} break; // Se guardan los costos de insertar
        }
    }
    else{
        switch (poss) {
        case 3:
            for (int i = 0; i < 26; ++i) {for (int j = 0; j < 26; ++j) {archivo >> reemplazar[i][j];}} break; // Se guardan los costos de reemplazar
        case 4:
            for (int i = 0; i < 26; ++i) {for (int j = 0; j < 26; ++j) {archivo >> transponer[i][j];}} break; // Se guardan los costos de transponer
        }
    }

    archivo.close();
}

/*
 // Calcula el costo de sustituir el carácter ‘a’ por ‘b’.
 // Parámetros:
 //  −a: carácter original
 //  −b: carácter con el que se sustituye
 // Return: costo de sustituir ’a’ por ’b’
*/
int costo_sub(char a, char b) {
    int indiceA = a - 'a';
    int indiceB = b - 'a';
    return reemplazar[indiceA][indiceB];
}

/*
 // Calcula el costo de insertar el carácter ‘b’.
 // Parámetros:
 //−b: carácter a insertar
 // Return: costo de insertar ’b’
*/
int costo_ins(char b) {
    int indiceB = b - 'a';
    return insertar[indiceB];  
}

/*
 // Calcula el costo de eliminar el carácter ’a ’.
 // Parámetros:
 //−a: carácter a eliminar
 // Return: costo de eliminar ’a’
*/
int costo_del(char a) {
    int indiceA = a - 'a';
    return eliminar[indiceA];
}

/*
 // Calcula el costo de transponer los caracteres ’a’ y ’b’.
 // Parámetros:
 //−a: primer carácter a transponer
 //−b: segundo carácter a transponer
 // Return: costo de transponer ’a’ y ’b’
*/
int costo_trans(char a, char b) {
    int indiceA = a - 'a';
    int indiceB = b - 'a';
    return transponer[indiceA][indiceB];
}

vector<string> reconstruirCamino(string &S1, string &S2, vector<vector<int>> &Cache) {
    vector<string> camino;
    int i = 0, j = 0;

    while (i < S1.size() || j < S2.size()) {
        if (i == S1.size()) {
            // Resta insertar el resto de los caracteres de S2
            camino.push_back("Insertar '" + string(1, S2[j]) + "' en posición " + to_string(j));
            j++;
        } else if (j == S2.size()) {
            // Resta eliminar el resto de los caracteres de S1
            camino.push_back("Eliminar '" + string(1, S1[i]) + "' de posición " + to_string(i));
            i++;
        } else {
            int elim = costo_del(S1[i]) + Cache[i + 1][j];
            int ins = costo_ins(S2[j]) + Cache[i][j + 1];
            int remp = costo_sub(S1[i], S2[j]) + Cache[i + 1][j + 1];
            int transp = INT_MAX;

            if (i + 1 < S1.size() && j + 1 < S2.size() && S1[i] == S2[j + 1] && S1[i + 1] == S2[j]) {
                transp = costo_trans(S1[i], S1[i + 1]) + Cache[i + 2][j + 2];
            }

            int minimo = Cache[i][j];
            if (minimo == elim) {
                camino.push_back("Eliminar " + string(1, S1[i])); //+ "' de posición " + to_string(i)
                i++;
            } else if (minimo == ins) {
                camino.push_back("Insertar " + string(1, S2[j])); //+ "' en posición " + to_string(j)
                j++;
            } else if (minimo == remp) {
                camino.push_back("Reemplazar " + string(1, S1[i]) + " por " + string(1, S2[j])); //+ "' en posición " + to_string(i)
                i++;
                j++;
            } else if (minimo == transp) {
                camino.push_back("Transponer " + string(1, S1[i]) + " y " + string(1, S1[i + 1])); //+ "' en posiciones " + to_string(i) + " y " + to_string(i + 1)
                i += 2;
                j += 2;
            }
        }
    }

    return camino;
}

/*
*   Memoria calcula el espacio utilizado por la matriz de cache
*/
size_t Memoria(const vector<vector<int>>& matriz) {
    size_t memoria = 0;
    
    memoria += sizeof(matriz);  
    memoria += sizeof(vector<int>) * matriz.capacity();
    
    for (const auto& fila : matriz) {
        memoria += sizeof(vector<int>);
        memoria += sizeof(int) * fila.capacity();
    }
    
    return memoria;
}