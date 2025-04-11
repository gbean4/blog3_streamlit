import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def load_name_data():
    # Load the dataset from a CSV file
    df = pd.read_csv('https://raw.githubusercontent.com/gbean4/Post_2/9b874da1c45720f3196d7f1bd7edc4a60ee30484/fast_food_analysis.csv')    
    return df

df = load_name_data()

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


st.title("Fast Food Analysis")
st.write("This is a Streamlit app for analyzing economic data versus various fast food items.")

tab1, tab2, tab3 = st.tabs(['Overall Correlation', 'Correlation by Region', 'State vs Food'])

with tab1:
    st.subheader("Overall Correlation")
    st.write("Correlation matrix for all states:")
    overall_df = df.drop(columns=['region'])
    matrix = overall_df.set_index("state").corr()
    fig = plt.figure(figsize=(10,6))
    sns.heatmap(matrix, annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title("Correlation Between Economic Factors and Restaurant Prices")
    st.pyplot(fig)

#expander with more info
    with st.expander("See explanation"):
        st.write('''
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        ''')
        #st.image("https://static.streamlit.io/examples/dice.jpg")


with tab2:
    st.subheader("Correlation by Region")
    region = st.selectbox("Select a region:", df['region'].unique())

    region_data = df[df['region'] == region]
    numeric_region_data = region_data.select_dtypes(include='number')
    corr_matrix = numeric_region_data.corr()


    fig = plt.figure(figsize=(10,6))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title(f"Correlation Between Economic Factors and Restaurant Prices in {region}")
    st.pyplot(fig)
    st.write("This chart shows the correlation between economic factors and restaurant prices in the selected region.")
    



    
#     state_df = df[df['state'] == state]
#     numeric_data = state_df.select_dtypes(include='number')

# if numeric_data.shape[0] >= 2:
#     corr_matrix = numeric_data.corr()
#     fig = plt.figure(figsize=(10, 6))
#     sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
#     plt.title(f"Correlation Between Economic Factors and Restaurant Prices in {state}")
#     st.pyplot(fig)
#     st.write("This chart shows the correlation between economic factors and restaurant prices in the selected state.")
# else:
#     st.warning("Not enough data to compute correlation for this state.")



  