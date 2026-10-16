# 🍽 Zomato Restaurant Analytics & Rating Prediction

## 📌 Project Overview

The **Zomato Restaurant Analytics & Rating Prediction Dashboard** is an interactive web application developed using Python and Streamlit. It analyzes restaurant data to provide insights into restaurant ratings, locations, cuisines, costs, customer votes, online ordering, and table booking.

The dashboard includes interactive visualizations and a Machine Learning model that predicts restaurant ratings based on selected restaurant details.

## 🎯 Objectives

- Analyze restaurant ratings and customer votes.
- Explore restaurant distribution across different locations.
- Compare restaurant costs and ratings.
- Understand customer preferences and restaurant services.
- Predict restaurant ratings using a Random Forest Regression model.

## 🛠️ Technologies Used

- **Python** – Programming language
- **Pandas** – Data cleaning and manipulation
- **Plotly** – Interactive data visualization
- **Streamlit** – Web dashboard development
- **Scikit-learn** – Machine Learning and data preprocessing

## ✨ Key Features

### 📊 Interactive Dashboard
- Displays the total number of restaurants, average rating, and average cost.
- Provides interactive charts for restaurant analysis.
- Presents restaurant insights through a simple interface.

### 🔍 Sidebar Filters
- Filter restaurants by location and cuisine.
- Select a cost range and rating range.
- Filter by online ordering and table booking availability.

### 📈 Data Visualizations
- **Top Restaurants:** Displays highly rated restaurants.
- **Location Distribution:** Shows the distribution of restaurants across locations.
- **Votes vs Rating:** Visualizes the relationship between ratings and average customer votes.
- **Rating Distribution:** Displays the distribution of restaurant ratings.

### 🤖 Machine Learning
Uses a **Random Forest Regressor** to predict restaurant ratings based on:
- Restaurant location
- Cost for two people
- Number of customer votes
- Online ordering availability
- Table booking availability

Users can enter restaurant details and generate a predicted rating through the dashboard.

## 📂 Project Structure

```text
zomato-analytics-dashboard/
│
├── app.py
├── zomato.csv
├── requirements.txt
└── README.md
```

**Note:** The `zomato.csv` dataset must be available locally or provided through an appropriate data source.

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### Step 2: Open the Project Folder

```bash
cd your-repository-name
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure the Dataset

Place `zomato.csv` in the project folder.

Update the CSV file path in `app.py` to use a relative path:

```python
df = pd.read_csv("zomato.csv")
```

### Step 5: Run the Application

```bash
python -m streamlit run app.py
```

The dashboard will open in your browser, usually at:

`http://localhost:8501`

## 📦 Requirements

The project dependencies are listed in `requirements.txt`:

```text
streamlit
pandas
plotly
scikit-learn
```

## 📌 Machine Learning Approach

The project uses the **Random Forest Regression** algorithm to estimate restaurant ratings from selected features.

The model is trained on the available dataset and generates predictions based on user inputs.

**Note:** The predicted rating is an estimate, not a guaranteed actual restaurant rating. Model performance should be evaluated using appropriate metrics on unseen test data.

## 🚀 Future Enhancements

- Deploy the dashboard online using Streamlit Community Cloud.
- Add more advanced restaurant comparison features.
- Evaluate model performance using MAE, RMSE, and R².
- Improve model accuracy through feature engineering and hyperparameter tuning.
- Add additional interactive visualizations.

## 👩‍💻 Author

**Aditi Devkar**

- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/aditi-devkar-7766a7292/)

---

⭐ If you find this project useful, consider giving the repository a star!
