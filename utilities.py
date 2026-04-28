import pandas as pd
import numpy as np

# --------------------
#  Data Transormation 
# --------------------

def correct_name(df):
    # We create the correct form of the sintax
    # It works for bad column names with '\n'
    new_column_names = [i.replace('\n', ' ') for i in df.columns.get_levels_values(1)]

    df.columns = pd.multiIndex.from_array([
        df.columns.get_levels_values(0)
        , new_column_names
    ])

    return df

def union_dataframes_by_different_key_name(df1, df2
,column_to_merge_of_df1 ,column_to_merge_of_df2):
    # merge two dataframes by columns
    # works for MultiIndex
    result = pd.merge(df1, df2, left_on=[column_to_merge_of_df1]
             ,right_on=[column_to_merge_of_df2])
    
    return result

def same_column_name(df_reference, df_changed_column_names):
    # Works for MultiIndex with 2 levels
    lvl_0 = df_reference.columns.get_level_values(0)
    lvl_1 = df_reference.columns.get_level_values(1)
    
    df_changed_column_names.columns = pd.MultiIndex.from_arrays([
            lvl_0
            ,lvl_1
        ])

    return df_changed_column_names

def add_zero_level_column(df, name_lvl_0):
    df.columns = pd.MultiIndex.from_arrays([
        np.resize(np.array(name_lvl_0), df.shape[1])
        , df.columns.to_list()
    ])

    return df


if __name__ == '__main__':
    df = pd.read_excel(r'..\src\accidents_per_comunity_2017-2024\Grupo-1.-Tablas-Generales-2018.xlsx', sheet_name='TABLA 1.1.C.A.', header=[2, 3])
    df2 = pd.read_excel(r'..\src\accidents_per_comunity_2017-2024\Grupo-1.-Tablas-Generales-2019.xlsx', sheet_name='TABLA 1.1.C.A.', header=[2, 3])
    df3 = pd.read_excel(r'..\src\accidents_per_comunity_2017-2024\Accidentes_con_victimas_Tablas_estadisticas_2020.xlsx', sheet_name='TABLA 1.1.C.A.', header=[2, 3])
    df4 = pd.read_excel(r'..\src\accidents_per_comunity_2017-2024\Accidentes_con_victimas_Tablas_estadisticas_2021.xlsx', sheet_name='TABLA 1.1.C.A.', header=[2, 3])
    df5 = pd.read_excel(r'..\src\accidents_per_comunity_2017-2024\Accidentes_con_victimas_Tablas_estadisticas_2022.xlsx', sheet_name='TABLA 1.1.C.A.', header=[2, 3])
    df6 = pd.read_excel(r'..\src\accidents_per_comunity_2017-2024\Accidentes-con-victimas-Tablas-estadisticas-2023.xlsx', sheet_name='TABLA 1.1.C.A.', header=[2, 3])
    df7 = pd.read_excel(r'..\src\accidents_per_comunity_2017-2024\Accidentes-con-victimas-Tablas-estadisticas-2024.xlsx', sheet_name='TABLA 1.1.C.A.', header=[2, 3])

    population_2018 = pd.read_csv(r'..\src\population\poblacion_comunidad_2018.csv', sep=';', encoding='latin-1')
    population_2019 = pd.read_csv(r'..\src\population\poblacion_comunidad_2019.csv', sep=';', encoding='latin-1')
    population_2020 = pd.read_csv(r'..\src\population\poblacion_comunidad_2020.csv', sep=';', encoding='latin-1')
    population_2021 = pd.read_csv(r'..\src\population\poblacion_comunidad_2021.csv', sep=';', encoding='latin-1')
    population_2022 = pd.read_csv(r'..\src\population\poblacion_comunidad_2022.csv', sep=';', encoding='latin-1')
    population_2023 = pd.read_csv(r'..\src\population\poblacion_comunidad_2023.csv', sep=';', encoding='latin-1')
    population_2024 = pd.read_csv(r'..\src\population\poblacion_comunidad_2024.csv', sep=';', encoding='latin-1')

    df = same_column_name(df2, df)
    df3 = same_column_name(df2, df3)
    df4 = same_column_name(df2, df4)
    df5 = same_column_name(df2, df5)
    df6 = same_column_name(df2, df6)
    df7 = same_column_name(df2, df7)
    
    population_2018['Comunidades y Ciudades Autónomas'] = population_2018['Comunidades y Ciudades Autónomas'].str[3:]
    population_2018 = add_zero_level_column(population_2018, 'Población')
    population_2019['Comunidades y Ciudades Autónomas'] = population_2019['Comunidades y Ciudades Autónomas'].str[3:]
    population_2019 = add_zero_level_column(population_2019, 'Población')
    population_2020['Comunidades y Ciudades Autónomas'] = population_2020['Comunidades y Ciudades Autónomas'].str[3:]
    population_2020 = add_zero_level_column(population_2020, 'Población')
    population_2021['Comunidades y Ciudades Autónomas'] = population_2021['Comunidades y Ciudades Autónomas'].str[3:]
    population_2021 = add_zero_level_column(population_2021, 'Población')
    population_2022['Comunidades y Ciudades Autónomas'] = population_2022['Comunidades y Ciudades Autónomas'].str[3:]
    population_2022 = add_zero_level_column(population_2022, 'Población')
    population_2023['Comunidades y Ciudades Autónomas'] = population_2023['Comunidades y Ciudades Autónomas'].str[3:]
    population_2023 = add_zero_level_column(population_2023, 'Población')
    population_2024['Comunidades y Ciudades Autónomas'] = population_2024['Comunidades y Ciudades Autónomas'].str[3:]
    population_2024 = add_zero_level_column(population_2024, 'Población')

    population_2018['Población', 'Comunidades y Ciudades Autónomas'] = population_2018['Población', 'Comunidades y Ciudades Autónomas'].str.strip()
    df['COMUNIDAD AUTÓNOMA', 'Unnamed: 0_level_1'] = df['COMUNIDAD AUTÓNOMA', 'Unnamed: 0_level_1'].str.strip()

    accidents_and_population_2018 = union_dataframes_by_different_key_name(df, population_2018, ('COMUNIDAD AUTÓNOMA', 'Unnamed: 0_level_1'), ('Población', 'Comunidades y Ciudades Autónomas')) 
    accidents_and_population_2019 = union_dataframes_by_different_key_name(df2, population_2019, ('COMUNIDAD AUTÓNOMA', 'Unnamed: 0_level_1'), ('Población', 'Comunidades y Ciudades Autónomas'))
    accidents_and_population_2020 = union_dataframes_by_different_key_name(df3, population_2020, ('COMUNIDAD AUTÓNOMA', 'Unnamed: 0_level_1'), ('Población', 'Comunidades y Ciudades Autónomas'))
    accidents_and_population_2021 = union_dataframes_by_different_key_name(df3, population_2020, ('COMUNIDAD AUTÓNOMA', 'Unnamed: 0_level_1'), ('Población', 'Comunidades y Ciudades Autónomas'))
    accidents_and_population_2022 = union_dataframes_by_different_key_name(df3, population_2020, ('COMUNIDAD AUTÓNOMA', 'Unnamed: 0_level_1'), ('Población', 'Comunidades y Ciudades Autónomas'))
    accidents_and_population_2023 = union_dataframes_by_different_key_name(df3, population_2020, ('COMUNIDAD AUTÓNOMA', 'Unnamed: 0_level_1'), ('Población', 'Comunidades y Ciudades Autónomas'))
    accidents_and_population_2024 = union_dataframes_by_different_key_name(df3, population_2020, ('COMUNIDAD AUTÓNOMA', 'Unnamed: 0_level_1'), ('Población', 'Comunidades y Ciudades Autónomas'))
    
    print(accidents_and_population_2018.shape)
    print(accidents_and_population_2019.shape)
    print(accidents_and_population_2020.shape)
    print(accidents_and_population_2021.shape)
    print(accidents_and_population_2022.shape)
    print(accidents_and_population_2023.shape)
    print(accidents_and_population_2024.shape)

    accidents_and_population_2018_2014 = pd.concat([accidents_and_population_2018, accidents_and_population_2019, accidents_and_population_2020
                                                    , accidents_and_population_2021, accidents_and_population_2022, accidents_and_population_2023
                                                    , accidents_and_population_2024])
    
    accidents_and_population_2018_2014.to_csv('accidents_and_population_2018_2014.csv')
    