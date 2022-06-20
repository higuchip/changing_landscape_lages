# importar pacotes
import collections
import ee
import leafmap.foliumap as leafmap
from geobr import read_municipality
import json
import streamlit as st
import geemap.foliumap as geemap

collections.Callable = collections.abc.Callable


original_title = '<h1 style="color:Blue"> Mudanças na ocupação territorial de Lages no período de 1985 a 2020  </h1>'
st.markdown(original_title, unsafe_allow_html=True)
subtitle = "<h3> Aplicação do MapBiomas para a visualização de mudanças na cobertura e uso do solo</h3>"
st.markdown(subtitle, unsafe_allow_html=True)
st.caption(
    "Powered by  MapBiomas, Google Earth Engine and Python | Developed by Pedro Higuchi ([@pe_hi](https://twitter.com/pe_hi))"
)
st.caption("Contato: higuchip@gmail.com")
st.warning("Atenção: Desenvolvimento experimental, com o propósito didático.")
st.markdown("___")

###########################


Map = geemap.Map()
Map.add_basemap("SATELLITE")


#  Seleção da área de interesse (Município de Lages)

# Importar de geobr
lages = read_municipality(code_muni=4209300, year=2020)

# Converter formato para json
lages_feature = lages.to_json()

# Carregar o arquivo json
lages_feature = json.loads(lages_feature)

# Selecionar as features
lages_feature = lages_feature["features"]

# Construir Feature Collection
roi_lages = ee.FeatureCollection(lages_feature)


# Importar MapBiomas

mapbiomas = ee.Image(
    "projects/mapbiomas-workspace/public/collection6/mapbiomas_collection60_integration_v1"
).clip(roi_lages)


st.subheader("Escolha o período de interesse:")
# Seleção de anos

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Antes")
    antes = st.selectbox(
        "Escolha o primeiro ano",
        [
            1985,
            1986,
            1987,
            1988,
            1989,
            1990,
            1991,
            1992,
            1993,
            1994,
            1995,
            1996,
            1997,
            1998,
            1999,
            2000,
            2001,
            2002,
            2003,
            2004,
            2005,
            2006,
            2007,
            2008,
            2009,
            2010,
            2011,
            2012,
            2013,
            2014,
            2015,
            2016,
            2017,
            2018,
            2019,
            2020,
        ],
        index=0,
    )


with col2:
    st.markdown("#### Depois")
    depois = st.selectbox(
        "Escolha o segundo ano",
        [
            1985,
            1986,
            1987,
            1988,
            1989,
            1990,
            1991,
            1992,
            1993,
            1994,
            1995,
            1996,
            1997,
            1998,
            1999,
            2000,
            2001,
            2002,
            2003,
            2004,
            2005,
            2006,
            2007,
            2008,
            2009,
            2010,
            2011,
            2012,
            2013,
            2014,
            2015,
            2016,
            2017,
            2018,
            2019,
            2020,
        ],
        index=35,
    )


mbyr_antes = mapbiomas.select(f"classification_{antes}")
mbyr_depois = mapbiomas.select(f"classification_{depois}")

# Legenda

legend_colors = [
    "ffffff",  # 0
    "006400",  # 1 1. Forest
    "1f4423",  # 2
    "006400",  # 3 1.1. Forest Formation
    "006400",  # 4 1.2. Savanna Formation
    "006400",  # 5 1.2. Mangrove
    "76a5af",  # 6
    "29eee4",  # 7
    "77a605",  # 8
    "ad4413",  # 9 3.2. Forest Plantation
    "b8af4f",  # 10  Non Forest Natural Formation
    "45c2a5",  # 11 Wetlands
    "b8af4f",  # 12 Grassland
    "b8af4f",  # 13 2.5. Other non Forest Formations
    "ffffb2",  # 14 3. Farming
    "ffd966",  # 15 3.1. Pasture
    "f6b26b",  # 16
    "f99f40",  # 17
    "e974ed",  # 18 3.2. Agriculture
    "e974ed",  # 19 3.2.1. Temporary Crop
    "e974ed",  # 20  3.2.1.2. Sugar cane
    "fff3bf",  # 21 3.4. Mosaic Agriculture and Pasture
    "ea9999",  # 22 4. Non vegetated Area
    "ea9999",  # 23 4.1. Beach, Dune and Sand Spot
    "aa0000",  # 24 4.2. Urban Area
    "ea9999",  # 25 4.4. Other non Vegetaded Areas
    "0000ff",  # 26 5. Water
    "d5d5e5",  # 27 6. Non Observed
    "dd497f",  # 28
    "b8af4f",  # 29 2.4. Rocky Outcrop
    "af2a2a",  # 30 4.3. Mining
    "0000ff",  # 31 5.2. Aquaculture
    "b8af4f",  # 32  2.3. Salt Flat
    "0000ff",  # 33 5.1. River,Lake and Ocean
    "4fd3ff",  # 34
    "645617",  # 35
    "f3b4f1",  # 36 3.2.2. Perennial Corp
    "02106f",  # 37
    "02106f",  # 38
    "e974ed",  # 39 3.2.1.1. Soybean
    "e974ed",  # 40 3.2.1.3. Rice
    "e974ed",  # 41 3.2.1.4. Other temporary Crops
    "cca0d4",  # 42
    "d082de",  # 43
    "cd49e4",  # 44
    "e04cfa",  # 45
    "f3b4f1",  # 46 3.2.2.1. Coffee
    "f3b4f1",  # 47 3.2.2.2. Citrus
    "f3b4f1",  # 48 3.2.2.3. Other Perennial Crop
    "006400",
]  # 49 1.4. Wooded Restinga


legend_keys = [
    " ",  # 0
    "Floresta",  # 1 1. Forest
    " ",  # 2
    "Floresta",  # 3 1.1. Forest Formation
    "Floresta",  # 4 1.2. Savanna Formation
    "Floresta",  # 5 1.2. Mangrove
    " ",  # 6
    " ",  # 7
    " ",  # 8
    "Silvicultura",  # 9 3.2. Forest Plantation
    "Formacao Campestre",  # 10  Non Forest Natural Formation
    "Campo Alagado e Area Pantanosa",  # 11 Wetlands
    "Formacao Campestre",  # 12 Grassland
    "Formacao Campestre",  # 13 2.5. Other non Forest Formations
    "Agropecuaria",  # 14 3. Farming
    "Pastagem",  # 15 3.1. Pasture
    " ",  # 16
    " ",  # 17
    "Agropecuaria",  # 18 3.2. Agriculture
    "Agropecuaria",  # 19 3.2.1. Temporary Crop
    "Agropecuaria",  # 20  3.2.1.2. Sugar cane
    "Mosaico de Agricultura e Pastagem",  # 21 3.4. Mosaic Agriculture and Pasture
    "Area nao Vegetada",  # 22 4. Non vegetated Area
    "Area nao Vegetada",  # 23 4.1. Beach, Dune and Sand Spot
    "Area Urbanizada",  # 24 4.2. Urban Area
    "Area nao Vegetada",  # 25 4.4. Other non Vegetaded Areas
    "Corpo Dagua",  # 26 5. Water
    "Nao Observado",  # 27 6. Non Observed
    " ",  # 28
    "Formacao Natural nao Florestal",  # 29 2.4. Rocky Outcrop
    "Mineracao",  # 30 4.3. Mining
    "Corpo Dagua",  # 31 5.2. Aquaculture
    "Formacao Natural nao Florestal",  # 32  2.3. Salt Flat
    "Corpo Dagua",  # 33 5.1. River,Lake and Ocean
    " ",  # 34
    " ",  # 35
    "Lavoura Perene",  # 36 3.2.2. Perennial Corp
    " ",  # 37
    " ",  # 38
    "Agropecuaria",  # 39 3.2.1.1. Soybean
    "Agropecuaria",  # 40 3.2.1.3. Rice
    "Agropecuaria",  # 41 3.2.1.4. Other temporary Crops
    " ",  # 42
    " ",  # 43
    " ",  # 44
    " ",  # 45
    "Lavoura Perene",  # 46 3.2.2.1. Coffee
    "Lavoura Perene",  # 47 3.2.2.2. Citrus
    "Lavoura Perene",  # 48 3.2.2.3. Other Perennial Crop
    "Floresta",
]  # 49 1.4. Wooded Restinga

legend_dict = {legend_keys[i]: legend_colors[i] for i in range(len(legend_keys))}
legend_dict.pop(" ")


# Mapa
left_layer = geemap.ee_tile_layer(
    mbyr_antes, {"min": 0, "max": 49, "palette": legend_colors}, name=f"Lages {antes}"
)
right_layer = geemap.ee_tile_layer(
    mbyr_depois, {"min": 0, "max": 49, "palette": legend_colors}, name=f"Lages {depois}"
)

Map.split_map(left_layer, right_layer)
Map.add_legend(legend_title="Classes", legend_dict=legend_dict)
Map.centerObject(roi_lages, zoom=10)
Map.to_streamlit(height=600)
###########################

st.subheader("Referências:")
st.markdown(
    "Souza at. al. (2020) - Reconstructing Three Decades of Land Use and Land Cover Changes in Brazilian Biomes with Landsat Archive and Earth Engine - Remote Sensing, Volume 12, Issue 17, 10.3390/rs12172735."
)
st.markdown(
    "Wu, Q., (2020). geemap: A Python package for interactive mapping with Google Earth Engine. The Journal of Open Source Software, 5(51), 2305. https://doi.org/10.21105/joss.02305"
)
st.markdown(
    "Wu, Q., Lane, C. R., Li, X., Zhao, K., Zhou, Y., Clinton, N., DeVries, B., Golden, H. E., & Lang, M. W. (2019). Integrating LiDAR data and multi-temporal aerial imagery to map wetland inundation dynamics using Google Earth Engine. Remote Sensing of Environment, 228, 1-13. https://doi.org/10.1016/j.rse.2019.04.015 (pdf | source code)"
)

st.markdown(
    'Projeto MapBiomas - é uma iniciativa multi-institucional para gerar mapas anuais de uso e cobertura da terra a partir de processos de classificação automática aplicada a imagens de satélite. A descrição completa do projeto encontra-se em http://mapbiomas.org".'
)

st.markdown("___")
