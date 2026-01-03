import pandas as pd

# Function to calculate scores for each team
def calculate_scores(df):
    """
    Calculates a fairness score for each team based on:
    - attendance (more people → higher score)
    - priority (higher → higher score)
    - past usage (more past usage → lower score)
    """
    df["score"] = (
        0.6 * df["attendance"] + 
        0.3 * df["priority"] - 
        0.4 * df["past_usage"]
    )
    # Sort descending, highest score first
    df_sorted = df.sort_values("score", ascending=False).reset_index(drop=True)
    return df_sorted


if __name__ == "__main__":
    # Read the sample CSV
    df = pd.read_csv("data/requests.csv")
    
    # Calculate scores
    scored_df = calculate_scores(df)
    
    # Print results
    print("=== Team Scores ===")
    print(scored_df)
    
    # Show which team wins
    winner = scored_df.iloc[0]
    print(f"\n✅ Resource allocated to {winner['group']} with score {winner['score']:.2f}")
