import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt


# @st.cache_data
# def load_name_data():
#     # Load the dataset from a CSV file
#     df = pd.read_csv('https://raw.githubusercontent.com/gbean4/Post_2/9b874da1c45720f3196d7f1bd7edc4a60ee30484/fast_food_analysis.csv')    
#     return df

df = pd.read_csv("fast_food_analysis.csv")

@st.cache_data
def load_region():
    state_region_map = {
    # Northeast
    'Connecticut': 'Northeast', 'Maine': 'Northeast', 'Massachusetts': 'Northeast',
    'New Hampshire': 'Northeast', 'Rhode Island': 'Northeast', 'Vermont': 'Northeast',
    'New Jersey': 'Northeast', 'New York': 'Northeast', 'Pennsylvania': 'Northeast',

    # Midwest
    'Illinois': 'Midwest', 'Indiana': 'Midwest', 'Michigan': 'Midwest',
    'Ohio': 'Midwest', 'Wisconsin': 'Midwest', 'Iowa': 'Midwest',
    'Kansas': 'Midwest', 'Minnesota': 'Midwest', 'Missouri': 'Midwest',
    'Nebraska': 'Midwest', 'North Dakota': 'Midwest', 'South Dakota': 'Midwest',

    # South
    'Delaware': 'South', 'Florida': 'South', 'Georgia': 'South',
    'Maryland': 'South', 'North Carolina': 'South', 'South Carolina': 'South',
    'Virginia': 'South', 'District of Columbia': 'South', 'West Virginia': 'South',
    'Alabama': 'South', 'Kentucky': 'South', 'Mississippi': 'South',
    'Tennessee': 'South', 'Arkansas': 'South', 'Louisiana': 'South',
    'Oklahoma': 'South', 'Texas': 'South',

    # West
    'Arizona': 'West', 'Colorado': 'West', 'Idaho': 'West', 'Montana': 'West',
    'Nevada': 'West', 'New Mexico': 'West', 'Utah': 'West', 'Wyoming': 'West',
    'Alaska': 'West', 'California': 'West', 'Hawaii': 'West', 'Oregon': 'West',
    'Washington': 'West'
}

    df['region'] = df['state'].map(state_region_map)
    return df
region_df = load_region()

@st.cache_data
def load_abbreviations():
    us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "Virgin Islands, U.S.": "VI",
}
    df['abbreviation'] = df['state'].map(us_state_to_abbrev)
    return df
abbrev_df = load_abbreviations()
new_abbrev_df = load_abbreviations()

st.title("Fast Food Analysis")
st.write("This is a Streamlit app for analyzing economic data against the prices of various fast food items.")

tab1, tab2, tab3, tab4 = st.tabs(['Overall Correlation', 'Correlation by Region', 'State vs Fast Food vs Economic Factor', 'Economic Factors vs Fast Food'])

with tab1:
    st.subheader("Overall Correlation")
    st.write("Correlation matrix for all states:")
    numeric_df = df.select_dtypes(include=["number"])
    matrix = numeric_df.corr()

    fig = plt.figure(figsize=(10,6))
    sns.heatmap(matrix, annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title("Correlation Between Economic Factors and Restaurant Prices")
    st.pyplot(fig)

#expander with more info
    with st.expander("See explanation"):
        st.write('''
            This heatmap illustrates the correlations between various economic factors and fast food prices across U.S. states. Several clear trends emerge:

- Strong Relationships Among Fast Food Prices: Fast food items are highly correlated with each other, suggesting that when one item's price increases in a state, others tend to rise as well.

- Income and Cost of Living Matter: There is a strong positive correlation between fast food prices and both average/median income and cost of living. States with higher income levels and living costs generally have more expensive fast food.

- Weaker Links with Broader Economic Indicators: Factors like GDP growth and unemployment rate show minimal correlation with fast food prices, indicating that these broader metrics may not directly impact everyday food costs.

Overall, the analysis suggests that local affordability and purchasing power are more predictive of fast food pricing than general economic performance.


        ''')

with tab2:
    st.subheader("Correlation by Region")
    region = st.selectbox("Select a region:", region_df['region'].unique())

    region_data = region_df[region_df['region'] == region]
    numeric_region_data = region_data.select_dtypes(include='number')
    corr_matrix = numeric_region_data.corr()


    fig = plt.figure(figsize=(10,6))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title(f"Correlation Between Economic Factors and Restaurant Prices in {region}")
    st.pyplot(fig)
    st.write("This chart shows the correlation between economic factors and restaurant prices in the selected region.")


with tab3:
    st.subheader("State vs Food vs Economic Factors")

    food_label_map = {
    "Domino's Medium Cheese": "DominosMedCheese",
    "McDonald's Happy Meal": "McDonaldsHappyMeal",
    "McDonald's Big Mac": "McDonaldsBigMac",
    "Chick-fil-A Chicken Sandwich": "ChickfilAChickenSandwich",
    "Taco Bell Combo Meal": "TacoBellComboMeal"
}
    factors = ['AverageIncome','MedianIncome','CostOfLiving','MinimumWage',	'GDP','GDPGrowth',	'UnemploymentRate']

    fast_food = st.selectbox("Select a fast food item:", list(food_label_map.keys()))
    factor = st.selectbox("Select an economic factor:", factors, key="economic_factor")

    food_col = food_label_map[fast_food]
    abbrev_df = abbrev_df[['abbreviation', food_col]].rename(columns={food_col: 'price'})


        # Plotly choropleth
    fig = px.choropleth(
        abbrev_df,
        locations='abbreviation',
        locationmode="USA-states",
        color='price',
        scope="usa",
        color_continuous_scale="reds",
        labels={'price': f'{fast_food} Price'},
        title=f"Fast Food Prices by State: {fast_food}",
    )

    st.plotly_chart(fig)

    factor_df = new_abbrev_df[['abbreviation', factor]].rename(columns={factor: 'value'})

    fig2 = px.choropleth(
            factor_df,
            locations='abbreviation',
            locationmode="USA-states",
            color='value',
            scope="usa",
            color_continuous_scale="reds",
            labels={'value': f'{factor} value'},
            title=f"Economic Factor by State: {factor}",
        )
    
    st.plotly_chart(fig2)
    with st.expander("See explanation"):
        st.write('Compare the maps above and observe any similarities or differences. ' \
    'These observations can be used to draw conclusions about what factors most impact particular fast foods.')



with tab4:
    food_label_map = {
    "Domino's Medium Cheese": "DominosMedCheese",
    "McDonald's Happy Meal": "McDonaldsHappyMeal",
    "McDonald's Big Mac": "McDonaldsBigMac",
    "Chick-fil-A Chicken Sandwich": "ChickfilAChickenSandwich",
    "Taco Bell Combo Meal": "TacoBellComboMeal"
}
    st.subheader("Economic Factors vs Fast Food")
    factors = ['AverageIncome','MedianIncome','CostOfLiving','MinimumWage',	'GDP','GDPGrowth',	'UnemploymentRate']
    x = st.selectbox("Select an economic factor:", factors)
    y = st.selectbox("Select a fast food item:", list(food_label_map.keys()), key="fast_food_select")

    y = food_label_map[y]

    chart_df = df[[x, y,'state']].dropna()

    scatter = (
    alt.Chart(chart_df)
    .mark_circle(size=80)
    .encode(
        x=alt.X(x, title=x),
        y=alt.Y(y, title=y),
        tooltip=["state", x, y] 
    )
    .properties(
        width=600,
        height=400,
        title=f"{x} vs {y}"
    )
    .interactive()
)

    st.altair_chart(scatter, use_container_width=True)
    with st.expander("See explanation"):
        st.write('''
            This scatter plot illustrates the relationship between the selected economic factor and fast food prices. The x-axis represents the economic factor, while the y-axis shows the price of the selected fast food item.
            As each point is a state, note any outliers or linear trends. Linear trends indicate higher correlation values.''')