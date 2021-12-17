# Import Library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Import Dataset
df = pd.read_csv('df_minyak_negara_merged.csv')
df['prod_kumulatif'] = df['produksi'].cumsum()

# Create Title
st.write('# UAS - Create a GUI with Streamlit')

# Section 1
st.write('## Line Chart Amount of Oil per Year')
negara1 = st.selectbox('Choose Country', tuple(np.sort(df['name'].unique())), key = 1)
st.write('You selected:', negara1)
df_negara1_choose = df[df['name'] == negara1]
df_negara1_choose = df_negara1_choose[['name', 'tahun', 'produksi', 'prod_kumulatif']]

fig1 = plt.figure(figsize = (10, 5))
plt.plot(df_negara1_choose['tahun'], df_negara1_choose['produksi'])
plt.xlabel("Tahun")
plt.ylabel("Produksi Minyak")
plt.title("Jumlah Produksi Minyak Berdasarkan Tahun")
st.pyplot(fig1)

# Section 2
st.write('## Amount of Oil per Year Line Chart with Point Customization')
negara2 = st.selectbox('Choose Country', tuple(np.sort(df['name'].unique())), key = 2)
tahun2 = st.slider('Choose Year', 1971, 2015, key = 3)
st.write('You selected:', negara2)
st.write('You selected:', tahun2)
df_negara2_choose = df[df['name'] == negara2]

negara_choose = df['name'] == negara2
tahun_choose = df['tahun'] == tahun2

df_negara2 = df[negara_choose & tahun_choose]
df_negara2_choose = df_negara2_choose[['name', 'tahun', 'produksi', 'prod_kumulatif']]

fig2, ax2 = plt.subplots()
ax2.plot(df_negara2_choose['tahun'], df_negara2_choose['produksi'])
ax2.scatter(df_negara2['tahun'], df_negara2['produksi'], s = 25, marker = 'x', color = 'red')
ax2.set_xlabel("Tahun")
ax2.set_ylabel("Produksi Minyak")
ax2.set_title("Jumlah Produksi Minyak Berdasarkan Tahun")
ax2.ticklabel_format(useOffset=False, style='plain')
st.pyplot(fig2)

# Section 3
st.write('## Line Chart Cumulative Oil Production Amount per Year')
negara3 = st.selectbox('Choose Country', tuple(np.sort(df['name'].unique())), key = 4)
st.write('You selected:', negara3)
df_negara3_choose = df[df['name'] == negara3]
df_negara3_choose = df_negara3_choose[['name', 'tahun', 'produksi', 'prod_kumulatif']]

fig3, ax3 = plt.subplots()
ax3.plot(df_negara3_choose['tahun'], df_negara3_choose['prod_kumulatif'])
ax3.set_xlabel("Tahun")
ax3.set_ylabel("Produksi Minyak")
ax3.set_title("Jumlah Produksi Minyak Kumulatif Berdasarkan Tahun")
ax3.ticklabel_format(useOffset=False, style='plain')
st.pyplot(fig3)

# Section 4
st.write('## Table Information')
dti = df[['name', 'kode_negara', 'region', 'sub-region', 'tahun', 'produksi']]
tahun4 = st.slider('Choose Year', 1971, 2015, key = 5)
dti = dti[dti['tahun'] == tahun4]
max4 = dti['produksi'] == dti['produksi'].max()
min4 = dti['produksi'] == dti['produksi'].min()
zero4 = dti['produksi'] == 0
dti = dti[max4 | min4 | zero4]
dti['tahun'] = dti['tahun'].astype('int')
dti = dti.sort_values(by='produksi', ascending=False)
st.write(dti)

# Section 5
st.write('## Bar Chart of 10 Countries with the Largest Total Oil Production')
dt = pd.DataFrame(df.groupby('name')['produksi'].sum()).sort_values(by='produksi', ascending=False)
dt = dt.iloc[0:10]
fig4, ax4 = plt.subplots()
ax4.bar(dt.index, dt['produksi'])
ax4.set_xlabel("Negara")
ax4.set_ylabel("Total Produksi Minyak")
ax4.set_title("10 Negara dengan Total Produksi Minyak Terbesar")
ax4.ticklabel_format(useOffset=False, style='plain',axis='y')
ax4.set_xticklabels(dt.index, rotation = 90)
st.pyplot(fig4)