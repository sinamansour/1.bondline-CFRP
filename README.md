
## User Guidance

### Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/sinamansour/1.bondline-CFRP
    ```
    Replace `YOUR-GITHUB-USERNAME` and `YOUR-REPOSITORY-NAME` with the actual GitHub username and repository name.

2. **Navigate to the Project Directory**:
    ```bash
    cd YOUR-REPOSITORY-NAME
    ```

3. **Create and Activate a Virtual Environment**:

    **On macOS/Linux**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    **On Windows**:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

4. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Prediction Script

1. **Run the Script**:
    ```bash
    python run_models.py
    ```

2. **Follow the Input Prompts**:
    - **Choose the type of prediction**:
        - Enter `1` for predicting ultimate force (regression).
        - Enter `2` for predicting failure mode (classification).
    - **Enter the feature values**:
        - `Total Defect Area/Bond Area (%)`
        - `Measured Adhesive Thickness (ta)`
        - `Type of defect`

### Example Interaction

```plaintext
Choose the type of prediction you want to make:
1. Ultimate Force
2. Failure Mode
Enter 1 or 2: 1
Enter value for Total Defect Area/Bond Area (%): 0.5
Enter value for Measured Adhesive Thickness (ta): 0.3
Enter value for Type of Defect: 1
Predicted Ultimate Force: sth based on KN
