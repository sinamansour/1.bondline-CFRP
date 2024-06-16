import joblib
import pandas as pd

# Load the saved models
regression_model = joblib.load('best_random_forest_model_regression.pkl')
classification_model = joblib.load('best_random_forest_model_classification.pkl')
label_encoder = joblib.load('label_encoder.pkl')

def get_user_input():
    """Function to get user input for the features."""
    total_defect_area = float(input("Enter value for Total Defect Area/Bond Area (%): "))
    adhesive_thickness = float(input("Enter value for Measured Adhesive Thickness (ta): "))
    type_of_defect = input("Enter value for Type of Defect: ")
    return total_defect_area, adhesive_thickness, type_of_defect

def make_prediction(model, features, is_classification=False):
    """Function to make a prediction based on the model and features."""
    input_data = {
        'Total Defect Area/Bond Area (%)': [features[0]],
        'Measured Adhesive Thickness (ta)': [features[1]],
        'Type of defect': [features[2]]
    }
    X_input = pd.DataFrame(input_data)
    if is_classification:
        prediction = model.predict(X_input)
        return label_encoder.inverse_transform(prediction)[0]
    else:
        prediction = model.predict(X_input)[0]
        return prediction

def main():
    """Main function to run the script."""
    print("Choose the type of prediction you want to make:")
    print("1. Ultimate Force")
    print("2. Failure Mode")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        features = get_user_input()
        result = make_prediction(regression_model, features)
        print(f"Predicted Ultimate Force: {result}")
    elif choice == '2':
        features = get_user_input()
        result = make_prediction(classification_model, features, is_classification=True)
        print(f"Predicted Failure Mode: {result}")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
