import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

def read_data():
    """Lee los archivos de datos y los prepara para el análisis"""
    columnas = ['dataset', 'distancia_minima', 'largo_s1', 'largo_s2', 
                'tiempo_ms', 'memoria_bytes']
    
    # Leer archivos
    df_bf = pd.read_csv('BF.txt', names=columnas)
    df_dp = pd.read_csv('DP.txt', names=columnas)
    
    return df_bf, df_dp

def configurar_estilo():
    """Configura el estilo general de los gráficos"""
    plt.style.use('seaborn-v0_8-paper')
    plt.rcParams['figure.figsize'] = [12, 7]
    plt.rcParams['font.size'] = 12
    plt.rcParams['axes.labelsize'] = 12
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['legend.fontsize'] = 10
    plt.rcParams['figure.titlesize'] = 16

def generar_graficos_rendimiento(df_bf, df_dp, output_dir):
    """Genera gráficos de rendimiento para cada dataset"""
    datasets_principales = ['IgualLargo', 'LetrasRepetidas', 'Transposiciones', 'VacioS1', 'VacioS2']
    
    # 1. Gráficos individuales por dataset
    for dataset in datasets_principales:
        bf_data = df_bf[df_bf['dataset'] == dataset]
        dp_data = df_dp[df_dp['dataset'] == dataset]
        largo = 'largo_s2'
        if dataset == "VacioS2":
            largo = 'largo_s1'
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        fig.suptitle(f'Análisis de Rendimiento - Dataset: {dataset}', fontsize=16, y=1.05)
        
        # Gráfico de tiempo
        ax1.semilogy(bf_data[largo], bf_data['tiempo_ms'], 'o-', 
                    label='Fuerza Bruta', color='#e74c3c', linewidth=2)
        ax1.semilogy(dp_data[largo], dp_data['tiempo_ms'], 's-', 
                    label='Prog. Dinámica', color='#2ecc71', linewidth=2)
        ax1.set_xlabel('Largo de entrada')
        ax1.set_ylabel('Tiempo (ms)')
        ax1.set_title('Tiempo de ejecución')
        ax1.grid(True, which="both", ls="-", alpha=0.2)
        ax1.legend()
        
        # Gráfico de memoria
        ax2.plot(dp_data[largo], dp_data['memoria_bytes'], 's-', 
                color='#2ecc71', linewidth=2, label='Prog. Dinámica')
        ax2.plot(bf_data[largo], bf_data['memoria_bytes'], 's-', 
            color='#2f3aba', label='Brute Force')
        ax2.set_xlabel('Largo de entrada')
        ax2.set_ylabel('Memoria (bytes)')
        ax2.set_title('Uso de memoria')
        ax2.grid(True, alpha=0.2)
        ax2.legend()
        
        plt.tight_layout()
        plt.savefig(f'{output_dir}/{dataset}_analisis.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    # 2. Gráfico comparativo general de tiempos
    plt.figure(figsize=(12, 7))
    for dataset in datasets_principales:
        bf_data = df_bf[df_bf['dataset'] == dataset]
        dp_data = df_dp[df_dp['dataset'] == dataset]
        
        largo = 'largo_s2'
        if dataset == "VacioS2":
            largo = 'largo_s1'
        plt.semilogy(bf_data[largo], bf_data['tiempo_ms'], 'o-', 
                    label=f'BF - {dataset}', alpha=0.7)
        plt.semilogy(dp_data[largo], dp_data['tiempo_ms'], 's--', 
                    label=f'DP - {dataset}', alpha=0.7)
    
    plt.title('Comparación General de Tiempos de Ejecución')
    plt.xlabel('Largo de entrada')
    plt.ylabel('Tiempo (ms)')
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/comparacion_general_tiempos.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 3. Análisis de casos especiales (VacioS1 y VacioS2)
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Análisis de Casos Cadenas Vacias', fontsize=16, y=1.02)
    
    # VacioS1 - Tiempo
    bf_data = df_bf[df_bf['dataset'] == 'VacioS1']
    dp_data = df_dp[df_dp['dataset'] == 'VacioS1']
    
    ax1.plot(bf_data['largo_s2'], bf_data['tiempo_ms'], 'o-', 
            label='Fuerza Bruta', color='#e74c3c')
    ax1.plot(dp_data['largo_s2'], dp_data['tiempo_ms'], 's-', 
            label='Prog. Dinámica', color='#2ecc71')
    ax1.set_title('Tiempo de ejecución - VacioS1')
    ax1.set_xlabel('Largo de S2')
    ax1.set_ylabel('Tiempo (ms)')
    ax1.legend()
    ax1.grid(True, alpha=0.2)
    
    # VacioS1 - Memoria
    ax2.plot(dp_data['largo_s2'], dp_data['memoria_bytes'], 's-', 
            color='#2ecc71', label='Prog. Dinámica')
    ax2.plot(bf_data['largo_s2'], bf_data['memoria_bytes'], 's-', 
            color='#2f3aba', label='Brute Force')
    ax2.set_title('Uso de memoria - VacioS1')
    ax2.set_xlabel('Largo de S2')
    ax2.set_ylabel('Memoria (bytes)')
    ax2.legend()
    ax2.grid(True, alpha=0.2)
    
    # VacioS2 - Tiempo
    bf_data = df_bf[df_bf['dataset'] == 'VacioS2']
    dp_data = df_dp[df_dp['dataset'] == 'VacioS2']
    
    ax3.plot(bf_data['largo_s1'], bf_data['tiempo_ms'], 'o-', 
            label='Fuerza Bruta', color='#e74c3c')
    ax3.plot(dp_data['largo_s1'], dp_data['tiempo_ms'], 's-', 
            label='Prog. Dinámica', color='#2ecc71')
    ax3.set_title('Tiempo de ejecución - VacioS2')
    ax3.set_xlabel('Largo de S1')
    ax3.set_ylabel('Tiempo (ms)')
    ax3.legend()
    ax3.grid(True, alpha=0.2)
    
    # VacioS2 - Memoria
    ax4.plot(dp_data['largo_s1'], dp_data['memoria_bytes'], 's-', 
            color='#2ecc71', label='Prog. Dinámica')
    ax4.plot(bf_data['largo_s1'], bf_data['memoria_bytes'], 's-', 
            color='#2f3aba', label='Brute Force')
    ax4.set_title('Uso de memoria - VacioS2')
    ax4.set_xlabel('Largo de S1')
    ax4.set_ylabel('Memoria (bytes)')
    ax4.legend()
    ax4.grid(True, alpha=0.2)
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/casos_especiales.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 4. Gráfico de eficiencia relativa
    """
    plt.figure(figsize=(12, 7))
    for dataset in datasets_principales:
        bf_data = df_bf[df_bf['dataset'] == dataset]
        dp_data = df_dp[df_dp['dataset'] == dataset]
        
        ratio = bf_data['tiempo_ms'] / dp_data['tiempo_ms']
        plt.semilogy(bf_data['largo_s1'], ratio, 'o-', label=dataset)
    
    plt.title('Eficiencia Relativa (Tiempo BF / Tiempo DP)')
    plt.xlabel('Largo de entrada')
    plt.ylabel('Factor de mejora (escala log)')
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'{output_dir}/eficiencia_relativa.png', dpi=300, bbox_inches='tight')
    plt.close()
    """

def generar_grafico_costos(df_bf, df_dp, output_dir):
    """
    Genera un gráfico de costos (tiempo y memoria combinados) por dataset.
    """
    datasets_principales = ['IgualLargo', 'LetrasRepetidas', 'Transposiciones', 'VacioS1', 'VacioS2']
    
    # Crear DataFrame con métricas normalizadas
    costos = []
    for dataset in datasets_principales:
        bf_data = df_bf[df_bf['dataset'] == dataset]
        dp_data = df_dp[df_dp['dataset'] == dataset]
        
        # Normalización (suma total por dataset)
        bf_tiempo_total = bf_data['distancia_minima'].sum()
        dp_tiempo_total = dp_data['distancia_minima'].sum()
        
        costos.append({
            'dataset': dataset,
            'metodo': 'BF',
            'costo_total': bf_tiempo_total
        })
        costos.append({
            'dataset': dataset,
            'metodo': 'DP',
            'costo_total': dp_tiempo_total
        })
    
    df_costos = pd.DataFrame(costos)
    
    # Graficar
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_costos, x='dataset', y='costo_total', hue='metodo', palette=['#2f3aba', '#2ecc71'])
    plt.title('Comparación de Costos por Dataset', fontsize=14)
    plt.xlabel('Dataset')
    plt.ylabel('Costo Total')
    plt.grid(axis='y', alpha=0.3)
    plt.legend(title='Método')
    plt.tight_layout()
    
    # Guardar gráfico
    plt.savefig(f'{output_dir}/costos_por_dataset.png', dpi=300, bbox_inches='tight')
    plt.close()

def main():
    # Crear directorio de salida
    Path("Graficos").mkdir(parents=True, exist_ok=True)
    
    # Configurar estilo de los gráficos
    configurar_estilo()
    
    # Leer datos
    df_bf, df_dp = read_data()
    
    # Generar gráficos
    generar_graficos_rendimiento(df_bf, df_dp, "Graficos")

    generar_grafico_costos(df_bf, df_dp, "Graficos")

    # Imprimir estadísticas relevantes
    print("\nEstadísticas de rendimiento:")
    for dataset in df_bf['dataset'].unique():
        bf_time = df_bf[df_bf['dataset'] == dataset]['tiempo_ms'].max()
        dp_time = df_dp[df_dp['dataset'] == dataset]['tiempo_ms'].max()
        print(f"\n{dataset}:")
        print(f"Tiempo máximo BF: {bf_time:.6f} ms")
        print(f"Tiempo máximo DP: {dp_time:.6f} ms")
        if bf_time > 0 and dp_time > 0:
            print(f"Factor de mejora: {bf_time/dp_time:.2f}x")

if __name__ == "__main__":
    main()