# CSV based - streamlit
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="IPL Analytics App", layout="wide")

# --------------------------------
# Load Dataset Automatically
# --------------------------------

@st.cache_data
def load_local_data(data_path):
    try:
        return pd.read_csv(data_path)
    except Exception as e:
        st.error(f"Could not load dataset: {e}")
        return None
    
def over_viz(bin_sums1, bin_sums2, bin_wkts_sums1, bin_wkts_sums2, cum_sum1, cum_sum2, bat_team, bow_team):
   
    # 1st Interactive Bar Chart: Runs per over
    fig1 = go.Figure()

    # Bar chart for 1st inning
    fig1.add_trace(go.Bar(
        x=np.arange(1, len(bin_sums1) + 1),
        y=bin_sums1,
        name=f'{bat_team} - 1st Inn',
        marker=dict(color='skyblue'),
        text=[f"Runs: {bin_sums1[i]}<br>Wickets: {bin_wkts_sums1[i]}" for i in range(len(bin_sums1))],  # Wickets count as hover text        
        hoverinfo='text'  # Show run and wicket count in hover
    ))

    # Bar chart for 2nd inning
    fig1.add_trace(go.Bar(
        x=np.arange(1, len(bin_sums2) + 1),
        y=bin_sums2,
        name=f'{bow_team} - 2nd Inn',
        marker=dict(color='lightgreen'),
        text=[f"Runs: {bin_sums2[i]}<br>Wickets: {bin_wkts_sums2[i]}" for i in range(len(bin_sums2))],  # Wickets count as hover text
        hoverinfo='text'
    ))

    fig1.update_layout(
        barmode='group',
        title='Runs per Over',
        xaxis_title='Overs',
        yaxis_title='Runs',
        xaxis=dict(tickmode='array', tickvals=np.arange(1, 21)),
        template='plotly_dark',
        showlegend=True
    )


    # 2nd Interactive Line Chart: Runs per over
    fig2 = go.Figure()

    # Line plot for 1st inning
    fig2.add_trace(go.Scatter(
        x=np.arange(1, len(bin_sums1) + 1),
        y=bin_sums1,
        mode='lines+markers',
        name=f'{bat_team} - 1st Inn',
        marker=dict(color='red'),
        line=dict(color='green'),
        text=[f"Runs: {bin_sums1[i]}" for i in range(len(bin_sums1))],
        hoverinfo='text'
    ))

    # Line plot for 2nd inning
    fig2.add_trace(go.Scatter(
        x=np.arange(1, len(bin_sums2) + 1),
        y=bin_sums2,
        mode='lines+markers',
        name=f'{bow_team} - 2nd Inn',
        marker=dict(color='yellow'),
        line=dict(color='blue'),
        text=[f"Runs: {bin_sums2[i]}" for i in range(len(bin_sums2))],
        hoverinfo='text'
    ))

    fig2.update_layout(
        title='Runs per Over',
        xaxis_title='Overs',
        yaxis_title='Runs',
        xaxis=dict(tickmode='array', tickvals=np.arange(1, 21)),
        template='plotly_dark',
        showlegend=True
    )

    # 3rd Interactive Cumulative Run Chart
    # Create a Plotly Figure for interactive chart
    fig3 = go.Figure()

    # Cumulative runs plot for 1st inning
    fig3.add_trace(go.Scatter(
        x=np.arange(1, len(cum_sum1) + 1),
        y=cum_sum1,
        mode='lines+markers',
        name=f'{bat_team} - 1st Inn',
        marker=dict(color='red'),
        line=dict(color='green'),
        text=[f"Runs: {cum_sum1[i]}" for i in range(len(cum_sum1))],
        hoverinfo='text'
    ))

    # Cumulative runs plot for 2nd inning
    fig3.add_trace(go.Scatter(
        x=np.arange(1, len(cum_sum2) + 1),
        y=cum_sum2,
        mode='lines+markers',
        name=f'{bow_team} - 2nd Inn',
        marker=dict(color='yellow'),
        line=dict(color='blue'),
        text=[f"Runs: {cum_sum2[i]}" for i in range(len(cum_sum2))],
        hoverinfo='text'
    ))

    fig3.update_layout(
        title='Worm graph - Score comparison',
        xaxis_title='Overs',
        yaxis_title='Cumulative Runs',
        xaxis=dict(tickmode='array', tickvals=np.arange(1, 21)),
        template='plotly_dark',
        showlegend=True
    )

    return fig1, fig2, fig3

def match_info(match):
    # match_df = deliveries[deliveries['match_id'] == id]
    bat_team = match['batting_team'].iloc[0]
    bow_team = match['bowling_team'].iloc[0]
    inn1 = match[match['inning'] == 1]
    inn2 = match[match['inning'] == 2]
    runs1 = inn1[['over','total_runs', 'is_wicket']]
    runs2 = inn2[['over','total_runs', 'is_wicket']]

    # Define the range intervals
    start = 0
    end = 20
    step = 1  # Define the step size for the ranges (0 to 1, 1 to 2, etc.)

    # Create bins based on the defined ranges
    bins = np.arange(start, end+step, step)  # Bin edges

    # Initialize a list to hold the sum of values in each bin for both data sets
    bin_sums1 = []
    bin_sums2 = []
    bin_wkts_sums1 = []
    bin_wkts_sums2 = []

    # For each bin, sum the values that fall within it for both data sets
    for i in range(len(bins) - 1):
        bin_values1 = runs1[(runs1.over >= bins[i]) & (runs1.over < bins[i+1])]
        bin_values2 = runs2[(runs2.over >= bins[i]) & (runs2.over < bins[i+1])]
        
        if len(bin_values1) != 0:
            bin_sums1.append(bin_values1['total_runs'].sum())  # Sum of values for data1 in the bin
            bin_wkts_sums1.append(bin_values1['is_wicket'].sum())

        if len(bin_values2) != 0:
            bin_sums2.append(bin_values2['total_runs'].sum())  # Sum of values for data2 in the bin
            bin_wkts_sums2.append(bin_values2['is_wicket'].sum())  

    # Calculate cumulative sum using numpy
    cum_sum1 = np.cumsum(bin_sums1)
    cum_sum2 = np.cumsum(bin_sums2)

    return over_viz(bin_sums1, bin_sums2, bin_wkts_sums1, bin_wkts_sums2, cum_sum1, cum_sum2, bat_team, bow_team)

    
    
def team_records():
    wins = matches['winner'].value_counts().sort_index()
    tot = matches['team1'].value_counts() + matches['team2'].value_counts()  # Total matches each team has played
    losses = tot - wins
    teams = pd.concat([tot.index.to_series().reset_index(drop=True), tot.reset_index(drop=True), wins.reset_index(drop=True), losses.reset_index(drop=True)], axis=1, ignore_index=True)
    teams.columns = ['Teams', 'Matches', 'Wins', 'Loss']
    teams['Win percentage'] = np.round((teams['Wins']/teams['Matches'])*100, 2)
    return teams.sort_values('Win percentage', ascending=False).head(10).reset_index(drop=True)
    
players = load_local_data("./IPL_Analytics_App/data/players_clean.csv")
matches = load_local_data('./IPL_Analytics_App/data/matches_clean.csv')
deliveries = load_local_data('./IPL_Analytics_App/data/deliveries_clean.csv')
df_matches = load_local_data('./IPL_Analytics_App/data/match_info.csv')


if players is not None and matches is not None and df_matches is not None and deliveries is not None:
    st.success("Local dataset loaded successfully!")

# --------------------------------
# Main App
# --------------------------------
st.title("📊 IPL Analytics App")

if players is not None:
    tabs = st.tabs(["Players", "Matches", "Match Info"])

    # -------------------------------
    # Tab 1: Player data
    # -------------------------------
    with tabs[0]:
        st.header("📁 Data Overview")
        st.write(players.head())
        csv = players.to_csv(index=False).encode("utf-8")
        st.download_button("Download Cleaned CSV", csv, "data.csv")

        st.header("Top 10 players")
        # Creating a dropdown (selectbox)
        option = st.selectbox(
            'Choose option:',
            ['Runs_Scored', 'Batting_Average', 'Batting_Strike_Rate', 'Wickets_Taken']
        )

        # Display the selected option
        #st.write('Top 10:')
        if option not in ['Wickets_Taken']:
            st.subheader("Top Batters")
            st.write(players[['Player_Name', 'Matches', 'Runs_Scored', 'Batting_Average', 'Batting_Strike_Rate']].sort_values(option, ascending=False).head(10).reset_index(drop=True))
        else:
            st.subheader("Top Bowlers")
            st.write(players[['Player_Name', 'Matches', 'Wickets_Taken', 'Bowling_Average', 'Economy_Rate', 'Bowling_Strike_Rate', 'Best_Bowling_Match']].sort_values(option, ascending=False).head(10).reset_index(drop=True))

    # -------------------------------
    # Tab 2: Matches
    # -------------------------------
    with tabs[1]:
        st.header("Matches")
        st.subheader("Matches Data overview")
        st.write(matches.head())

        st.subheader("Team Records")
        st.write(team_records())

        # Biggest win margins
        st.subheader("Biggest win margins")
        st.write(matches.sort_values(by='result_margin', ascending=False).head(10).reset_index(drop=True))


        # Highest 1st innings score
        st.subheader("Highest 1st inning scores")
        st.write(matches[matches['result'] == 'runs'].sort_values('target_runs', ascending=False).head(10).reset_index(drop=True))

        # Highest successful chases
        st.subheader("Highest successful chases")
        st.write(matches[matches['result'] == 'wickets'].sort_values('target_runs', ascending=False).head(10).reset_index(drop=True))

        st.subheader("Super Over Matches")
        st.write(matches[matches['super_over'] == 'Y'].reset_index(drop=True))

        st.subheader("Top 10")
        # Creating a dropdown (selectbox)
        option = st.selectbox(
            'Choose option:',
            ['Player of match', 'Toss winners', 'Toss decisions', 'City']
        )

        # Display the selected option
        st.subheader(f'Top {option}')
        opt_dict = {'Player of match':{'player_of_match':'Player','count':'Number of MoM\'s'},
                    'Toss winners':{'toss_winner':'Teams','count':'Number of Toss wins'},
                    'Toss decisions':{'toss_decision':'Toss','count':'Teams chose'},
                    'City':{'city':'City','count':'Number of Times'}}
        
        col = list(opt_dict.get(option).keys())[0]
        top10 = matches[col].value_counts().reset_index()
        top10.rename(columns=opt_dict.get(option), inplace=True)
        st.write(top10.head(10))


    # -------------------------------
    # Tab 3: Visualizations
    # -------------------------------
    with tabs[2]:
        st.header("Match Info")
        st.write(df_matches.head())

        ip = st.slider("Select id:", 1, 1095)
        # st.write(deliveries.match_id == ip)
        match = deliveries[deliveries.match_id == ip]
        bat_team = match['batting_team'].iloc[0]
        bow_team = match['bowling_team'].iloc[0]

        fig1, fig2, fig3 = match_info(match)

        st.subheader(f"Over by over - 2 innings - {bat_team} vs {bow_team}")
        st.plotly_chart(fig1, width='stretch', key="fig1")
        st.markdown("---")  # Horizontal line separator

        st.subheader(f"Line graph with two innings - {bat_team} vs {bow_team}")
        st.plotly_chart(fig2, width='stretch', key="fig2")
        st.markdown("---")  # Horizontal line separator

        st.subheader(f"Run graph to compare 2 innings - {bat_team} vs {bow_team}")
        st.plotly_chart(fig3, width='stretch', key="fig3")
        

        



   