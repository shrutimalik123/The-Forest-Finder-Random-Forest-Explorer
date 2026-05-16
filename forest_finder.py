import random

def random_forest_game():
    # 1. Scenario: Wildlife Tracking
    print("--- 🌲 THE FOREST FINDER: RANDOM FOREST SIM 🌲 ---")
    print("Mission: Predict if a rare animal will visit the trail today.")
    print("Goal: Combine multiple weak Decision Trees to make one strong prediction.")

    # 2. Environmental Conditions (The Inputs)
    # 0 = Rainy/Night, 1 = Sunny/Day
    weather = random.choice([0, 1])
    time_of_day = random.choice([0, 1])
    
    weather_str = "Sunny" if weather == 1 else "Rainy"
    time_str = "Daytime" if time_of_day == 1 else "Nighttime"
    
    print(f"\nTrail Conditions today: {weather_str} & {time_str}")

    # 3. Hyperparameter: Number of Trees (Estimators)
    print("\n--- STEP 1: GROW YOUR FOREST ---")
    print("How many Decision Trees do you want in your Random Forest ensemble?")
    try:
        num_trees = int(input("Enter number of trees (e.g., 3, 5, or 7): "))
        if num_trees % 2 == 0:
            print("💡 Tip: An odd number of trees prevents tie votes! Adding 1.")
            num_trees += 1
    except ValueError:
        num_trees = 3

    # 4. The Ensemble Logic (Simulating Bootstrapped Trees)
    print(f"\n--- 🖥️ BOOTSTRAPPING AND TRAINING {num_trees} TREES... ---")
    votes = []
    
    for i in range(1, num_trees + 1):
        # In a real Random Forest, each tree gets a random subset of data/features[span_2](start_span)[span_2](end_span).
        # We simulate this by giving each tree a slightly randomized internal bias.
        tree_bias = random.choice(["weather_heavy", "time_heavy", "balanced"])
        
        if tree_bias == "weather_heavy":
            prediction = 1 if weather == 1 else 0
        elif tree_bias == "time_heavy":
            prediction = 1 if time_of_day == 1 else 0
        else:
            prediction = 1 if (weather + time_of_day) >= 1 else 0
            
        votes.append(prediction)
        pred_str = "🐾 WILL VISIT" if prediction == 1 else "❌ WILL NOT VISIT"
        print(f"🌲 Tree {i} focuses on {tree_bias.replace('_', ' ')} -> Prediction: {pred_str}")

    # 5. Aggregation: Majority Voting
    visit_votes = votes.count(1)
    no_visit_votes = votes.count(0)
    
    final_prediction = 1 if visit_votes > no_visit_votes else 0
    final_pred_str = "🐾 WILL VISIT" if final_prediction == 1 else "❌ WILL NOT VISIT"

    print("\n--- 🗳️ ENSEMBLE AGGREGATION (MAJORITY VOTING) ---")
    print(f"Votes for 'Will Visit': {visit_votes}")
    print(f"Votes for 'Will Not Visit': {no_visit_votes}")
    print(f"Final Forest Prediction: {final_pred_str}")

    # 6. Evaluation (Ground Truth comparison)
    # Let's say the animal actually loves Sunny Days, but hates Rain unless it's Night
    actual_truth = 1 if (weather == 1 and time_of_day == 1) or (weather == 0 and time_of_day == 0) else 0
    actual_str = "🐾 DID VISIT" if actual_truth == 1 else "❌ DID NOT VISIT"
    
    print(f"\n--- 📊 GROUND TRUTH ---")
    print(f"What actually happened: {actual_str}")
    
    if final_prediction == actual_truth:
        print("🏆 SUCCESS: Your Random Forest accurately predicted the animal's behavior!")
    else:
        print("⚠️ MISCLASSIFICATION: The forest got it wrong. Try expanding the forest next time.")

if __name__ == "__main__":
    random_forest_game()
