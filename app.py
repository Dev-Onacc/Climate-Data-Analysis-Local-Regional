import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Charger les données depuis un fichier Excel
@st.cache_data
def load_data(file):
    return pd.read_excel(file, sheet_name='mnocc_forecasts_dekadal')

# Interface utilisateur pour choisir le fichier
st.image("logo.png", width=80)  # Remplacez "logo.png" par le chemin de votre logo
st.title("Analyse des données climatiques")
uploaded_file = st.file_uploader("Choisissez un fichier Excel", type="xlsx")

if uploaded_file is not None:
    data = load_data(uploaded_file)
    
    # Afficher les premières lignes du dataframe
    st.write(data.head())
    
    # Sélectionner la région
    region = st.selectbox("Choisissez une région", data['region'].unique())
    
    # Filtrer les données pour la région choisie
    filtered_data = data[data['region'] == region]
    
    # Sélectionner la localité
    locality = st.selectbox("Choisissez une localité", filtered_data['location'].unique())
    
    # Filtrer les données pour la localité choisie
    locality_data = filtered_data[filtered_data['location'] == locality]
    
    # Convertir la colonne datetime en format datetime
    locality_data['datetime'] = pd.to_datetime(locality_data['datetime'])
    
    # Graphique des températures et des précipitations avec Plotly
    st.subheader(f"Températures et Précipitations pour {locality} dans la région {region}")
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(x=locality_data['datetime'], y=locality_data['temp_max'],
                             mode='lines+markers', name='Température Max (°C)', line=dict(color='red')))
    
    fig.add_trace(go.Scatter(x=locality_data['datetime'], y=locality_data['temp_min'],
                             mode='lines+markers', name='Température Min (°C)', line=dict(color='blue')))
    
    fig.add_trace(go.Bar(x=locality_data['datetime'], y=locality_data['precip'],
                         name='Précipitation (mm)', opacity=0.5, marker_color='green'))
    
    fig.update_layout(title=f'Températures Max, Min et Précipitations à {locality}',
                      xaxis_title='Date',
                      yaxis_title='Valeurs',
                      hovermode='x unified')
    
    st.plotly_chart(fig)

    # Saisie de la température seuil par l'utilisateur
    temp_threshold = st.number_input("Entrez la température seuil (°C) :", value=32.0)

    # Nombre de jours avec température supérieure à la valeur entrée par l'utilisateur
    hot_days_count = (locality_data['temp_max'] > temp_threshold).sum()
    
    st.subheader(f"Nombre de jours avec température supérieure à {temp_threshold} °C: {hot_days_count}")

    # Graphique du nombre de jours avec température supérieure à la valeur entrée par l'utilisateur
    days_above_threshold = locality_data[locality_data['temp_max'] > temp_threshold].groupby(locality_data['datetime'].dt.date).size()
    
    hot_days_fig = go.Figure()
    hot_days_fig.add_trace(go.Bar(x=days_above_threshold.index, y=days_above_threshold.values,
                                   name=f'Jours > {temp_threshold} °C', marker_color='orange'))
    
    hot_days_fig.update_layout(title=f'Nombre de Jours avec Température max > {temp_threshold} °C à {locality}',
                                xaxis_title='Date',
                                yaxis_title='Nombre de Jours',
                                hovermode='x unified')
    
    st.plotly_chart(hot_days_fig)

    # Graphique du nombre de jours de pluie
    rainy_days_count = (locality_data['precip'] > 0).sum()
    
    st.subheader(f"Nombre de jours de pluie à {locality}: {rainy_days_count}")
    
    rain_fig = go.Figure()
    rain_fig.add_trace(go.Bar(x=['Jours de pluie', 'Autres jours'], 
                               y=[rainy_days_count, len(locality_data) - rainy_days_count],
                               marker_color=['blue', 'orange']))
    
    rain_fig.update_layout(title=f'Répartition des jours de pluie à {locality}',
                           xaxis_title='Type de jour',
                           yaxis_title='Nombre de jours')
    
    st.plotly_chart(rain_fig)

    # Résumé pour toutes les localités dans la région choisie
    st.subheader(f"Résumé pour toutes les localités dans la région {region}")

    # Calculer le nombre de jours avec température supérieure au seuil pour chaque localité
    hot_days_summary = filtered_data.groupby('location').apply(lambda x: (x['temp_max'] > temp_threshold).sum()).reset_index(name='Jours > {}'.format(temp_threshold))

    # Graphique du nombre de jours avec température supérieure au seuil pour chaque localité
    hot_days_summary_fig = go.Figure()
    hot_days_summary_fig.add_trace(go.Bar(x=hot_days_summary['location'], y=hot_days_summary['Jours > {}'.format(temp_threshold)],
                                           marker_color='orange'))
    
    hot_days_summary_fig.update_layout(title=f'Nombre de Jours avec Température max > {temp_threshold} °C par Localité',
                                        xaxis_title='Localité',
                                        yaxis_title='Nombre de Jours',
                                        hovermode='x unified')
    
    st.plotly_chart(hot_days_summary_fig)

    # Calculer le nombre total de jours de pluie pour chaque localité
    rainy_days_summary = filtered_data.groupby('location').apply(lambda x: (x['precip'] > 0).sum()).reset_index(name='Jours de pluie')

    # Graphique du nombre total de jours de pluie pour chaque localité
    rainy_days_summary_fig = go.Figure()
    rainy_days_summary_fig.add_trace(go.Bar(x=rainy_days_summary['location'], y=rainy_days_summary['Jours de pluie'],
                                             marker_color='blue'))
    
    rainy_days_summary_fig.update_layout(title=f'Nombre Total de Jours de Pluie par Localité',
                                          xaxis_title='Localité',
                                          yaxis_title='Nombre de Jours',
                                          hovermode='x unified')
    
    st.plotly_chart(rainy_days_summary_fig)
