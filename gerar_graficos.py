import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def processar_avaliacoes(diretorio_base):
    dados = []
    
    for avaliador in os.listdir(diretorio_base):
        caminho_avaliador = os.path.join(diretorio_base, avaliador)
        
        if not os.path.isdir(caminho_avaliador):
            continue
            
        for arquivo in os.listdir(caminho_avaliador):
            if arquivo.endswith('.json'):
                partes = arquivo.replace('.json', '').split('_')
                if len(partes) != 2:
                    continue
                    
                gerador = partes[0]
                estrategia = partes[1].upper()
                
                with open(os.path.join(caminho_avaliador, arquivo), 'r', encoding='utf-8') as f:
                    conteudo = json.load(f)
                    
                    p = conteudo.get('pontuacao_precisao', 0)
                    c = conteudo.get('pontuacao_clareza', 0)
                    co = conteudo.get('pontuacao_completude', 0)
                    a = conteudo.get('pontuacao_aderencia', 0)
                    
                    nota_final = ((p * 3) + (a * 2) + (c * 2) + (co * 1)) / 8
                    
                    dados.append({
                        'Avaliador': avaliador,
                        'Gerador': gerador,
                        'Estrategia': estrategia,
                        'Nota_Final': nota_final
                    })
                    
    return pd.DataFrame(dados)

def gerar_graficos(df):
    sns.set_theme(style="whitegrid")
    
    # Gráfico 1: Impacto Geral da Estruturação
    plt.figure(figsize=(8, 6))
    sns.barplot(data=df, x='Estrategia', y='Nota_Final', errorbar=None, palette='viridis')
    plt.title('Impacto da Estruturação de Prompts na Qualidade (Média Geral)', fontsize=14)
    plt.xlabel('Estratégia de Prompt')
    plt.ylabel('Nota Final Ponderada')
    plt.ylim(0, 5)
    plt.tight_layout()
    plt.savefig('grafico1_impacto_geral.png', dpi=300)
    plt.close()
    
    # Gráfico 2: Sensibilidade por Modelo
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='Gerador', y='Nota_Final', hue='Estrategia', palette='mako')
    plt.title('Sensibilidade à Estruturação de Prompts por Modelo', fontsize=14)
    plt.xlabel('Modelo Gerador')
    plt.ylabel('Nota Final Ponderada')
    plt.ylim(0, 5)
    plt.legend(title='Estratégia')
    plt.tight_layout()
    plt.savefig('grafico2_sensibilidade_modelo.png', dpi=300)
    plt.close()
    
    # Gráfico 3: Matriz de Avaliação Cruzada (Heatmap)
    pivot_df = df.pivot_table(index='Avaliador', columns='Gerador', values='Nota_Final', aggfunc='mean')
    plt.figure(figsize=(8, 6))
    sns.heatmap(pivot_df, annot=True, cmap='YlGnBu', vmin=1, vmax=5, fmt='.2f', cbar_kws={'label': 'Nota Final Média'})
    plt.title('Matriz de Avaliação Cruzada (Viés Egocêntrico)', fontsize=14)
    plt.xlabel('Modelo Gerador')
    plt.ylabel('Modelo Avaliador')
    plt.tight_layout()
    plt.savefig('grafico3_avaliacao_cruzada.png', dpi=300)
    plt.close()

if __name__ == '__main__':
    pasta_avaliacoes = 'Avaliacoes' 
    df_resultados = processar_avaliacoes(pasta_avaliacoes)
    
    if not df_resultados.empty:
        gerar_graficos(df_resultados)
        df_resultados.to_csv('matriz_resultados_consolidados.csv', index=False)