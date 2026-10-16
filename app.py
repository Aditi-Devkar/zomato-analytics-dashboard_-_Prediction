import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Zomato Analytics Dashboard",
    page_icon="🍽",
    layout="wide"
)

# =====================================================
# 🎨 BASIC STYLE (OPTIONAL CLEAN LOOK)
# =====================================================
st.markdown("""
<style>
body {background-color:#0e1117;}

.kpi {
    background: linear-gradient(135deg,#1f1f2e,#2c2c3e);
    padding:15px;
    border-radius:12px;
    text-align:center;
    color:white;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv(r"C:\Users\Pallavi Devkar\OneDrive\Desktop\Data Analyst Project\rest project\zomato.csv")
df.columns = df.columns.str.strip()

df.rename(columns={'approx_cost(for two people)': 'cost'}, inplace=True)

df = df[['name','location','rate','votes','cost',
         'cuisines','online_order','book_table']]

# -------------------------------
# CLEANING
# -------------------------------
df['rate'] = df['rate'].astype(str).str.replace('/5','')
df['rate'] = df['rate'].replace(['NEW','-'], None)
df['rate'] = pd.to_numeric(df['rate'], errors='coerce')

df['cost'] = df['cost'].astype(str).str.replace(',', '')
df['cost'] = pd.to_numeric(df['cost'], errors='coerce')

df.dropna(inplace=True)

# =====================================================
# 🟦 SIDEBAR FILTERS
# =====================================================
st.sidebar.title("🔍 Filters Panel")

location_filter = st.sidebar.multiselect(
    "📍 Location",
    options=sorted(df['location'].unique()),
    default=sorted(df['location'].unique())[:3]
)

top_cuisines = df['cuisines'].value_counts().head(20).index

cuisine_filter = st.sidebar.multiselect(
    "🍽 Cuisine",
    options=top_cuisines,
    default=list(top_cuisines[:3])
)

cost_min, cost_max = st.sidebar.slider(
    "💰 Cost Range",
    int(df['cost'].min()),
    int(df['cost'].max()),
    (200, 1000)
)

rating_min, rating_max = st.sidebar.slider(
    "⭐ Rating Range",
    float(df['rate'].min()),
    float(df['rate'].max()),
    (3.0, 5.0)
)

online_filter = st.sidebar.selectbox("📦 Online Order", df['online_order'].unique())
table_filter = st.sidebar.selectbox("🍽 Table Booking", df['book_table'].unique())

# -------------------------------
# FILTER DATA
# -------------------------------
filtered_df = df[
    (df['location'].isin(location_filter)) &
    (df['cuisines'].isin(cuisine_filter)) &
    (df['cost'].between(cost_min, cost_max)) &
    (df['rate'].between(rating_min, rating_max)) &
    (df['online_order'] == online_filter) &
    (df['book_table'] == table_filter)
]

if filtered_df.empty:
    st.warning("No data found for selected filters")
    st.stop()

# =====================================================
# 🔴 TITLE (RED BOX + WHITE TEXT)
# =====================================================
st.markdown("""
<div style="
    background-color:#ff0000;
    padding:15px;
    border-radius:12px;
    text-align:center;
    font-size:32px;
    font-weight:bold;
    color:white;
">
🍽 Zomato Analytics Dashboard
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =====================================================
# KPI CARDS
# =====================================================
col1, col2, col3 = st.columns(3)

col1.markdown(f"""
<div class="kpi">
<h2 style="color:#ffcc00;">🍴 {len(filtered_df)}</h2>
<p>Restaurants</p>
</div>
""", unsafe_allow_html=True)

col2.markdown(f"""
<div class="kpi">
<h2 style="color:#00ff99;">⭐ {round(filtered_df['rate'].mean(),2)}</h2>
<p>Avg Rating</p>
</div>
""", unsafe_allow_html=True)

col3.markdown(f"""
<div class="kpi">
<h2 style="color:#66b3ff;">💰 {round(filtered_df['cost'].mean(),0)}</h2>
<p>Avg Cost</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =====================================================
# 📊 CHARTS
# =====================================================
col1, col2 = st.columns(2)

with col1:
    st.subheader("⭐ Top Restaurants")

    top_rest = filtered_df.sort_values('rate', ascending=False).head(8)

    fig1 = px.bar(
        top_rest,
        x='name',
        y='rate',
        color='rate',
        color_continuous_scale='Viridis',
        height=300
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("📍 Location Distribution")

    loc_counts = filtered_df['location'].value_counts().reset_index()
    loc_counts.columns = ['location','count']

    fig2 = px.pie(
        loc_counts,
        names='location',
        values='count',
        hole=0.4,
        height=300
    )
    st.plotly_chart(fig2, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    st.subheader("📈 Votes vs Rating")

    trend = filtered_df.groupby('rate')['votes'].mean().reset_index()

    fig3 = px.line(
        trend,
        x='rate',
        y='votes',
        markers=True,
        height=300
    )
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.subheader("📉 Rating Distribution")

    fig4 = px.histogram(
        filtered_df,
        x='rate',
        nbins=15,
        height=300
    )
    st.plotly_chart(fig4, use_container_width=True)

# =====================================================
# 🤖 ML MODEL
# =====================================================
le_location = LabelEncoder()
le_online = LabelEncoder()
le_table = LabelEncoder()

df['location_enc'] = le_location.fit_transform(df['location'])
df['online_enc'] = le_online.fit_transform(df['online_order'])
df['table_enc'] = le_table.fit_transform(df['book_table'])

X = df[['location_enc','cost','votes','online_enc','table_enc']]
y = df['rate']

model = RandomForestRegressor()
model.fit(X, y)

# =====================================================
# 🔮 PREDICTION
# =====================================================
st.markdown("---")
st.subheader("🔮 Predict Rating")

col1, col2, col3 = st.columns(3)

loc_input = col1.selectbox("Location", le_location.classes_)
cost_input = col2.number_input("Cost", 100, 5000, 500)
votes_input = col3.number_input("Votes", 0, 10000, 100)

col4, col5 = st.columns(2)

online_input = col4.selectbox("Online Order", le_online.classes_)
table_input = col5.selectbox("Table Booking", le_table.classes_)

if st.button("Predict Rating ⭐"):

    input_df = pd.DataFrame([{
        'location_enc': le_location.transform([loc_input])[0],
        'cost': cost_input,
        'votes': votes_input,
        'online_enc': le_online.transform([online_input])[0],
        'table_enc': le_table.transform([table_input])[0]
    }])

    pred = model.predict(input_df)[0]
    st.success(f"⭐ Predicted Rating: {round(pred,2)}")