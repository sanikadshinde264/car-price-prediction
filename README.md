# 🚗 Car Price Prediction

Predicts the resale price of a used car based on its company, model, manufacturing year, kilometers driven, and fuel type. Built with Flask and a scikit-learn Linear Regression pipeline.

## 📌 Overview
This project trains a regression model on a used-car dataset and serves predictions through a simple Flask web app. Users select a car's company, model, year, kms driven, and fuel type from a form and get an estimated resale price back instantly.

## ❓ Problem Statement
Used car pricing varies a lot and is hard to estimate consistently by hand — it depends on brand, model, age, mileage, and fuel type. This project builds a data-driven model that learns from past listings to give a quick, consistent price estimate for a given set of car details.

## ✨ Features
- Select car company, model, year, kms driven, and fuel type from a simple web form
- Instant resale price prediction using a trained Linear Regression model
- Dropdown lists dynamically populated from the dataset (companies, model names)
- Lightweight Flask app with separate pages for home, input form, and result

## 📊 Dataset
- **File:** `cleaned_Data8.csv`
- **Rows:** 816 cleaned used-car listings
- **Columns:**

  | Column | Description |
  |---|---|
  | `name` | Car model name (463 unique) |
  | `company` | Manufacturer/brand (25 unique) |
  | `year` | Manufacturing year |
  | `kms_driven` | Kilometers driven |
  | `fuel_type` | Petrol / Diesel / LPG |
  | `Price` | Target — resale price |

## 🛠️ Tools & Technologies
- **Python 3**, **Flask** — backend & routing
- **pandas / numpy** — data handling
- **scikit-learn** — `OneHotEncoder` + `LinearRegression` pipeline
- **HTML / Bootstrap** — front-end templates

## ⚙️ Methods / Methodology
1. Load and clean the dataset (`cleaned_Data8.csv`)
2. One-hot encode categorical features (`name`, `company`, `fuel_type`); pass numeric features (`year`, `kms_driven`) through
3. Fit a `LinearRegression` pipeline on the encoded data
4. Save the trained pipeline as `LinearRegressionModel.pkl`
5. Load the pickle in Flask (`Program1.py`) and use `pipe.predict()` on user input to return a price

## 🗂️ Project Directory Structure
```
Car-Price-Prediction/
├── Program1.py                     # Flask app
├── cleaned_Data8.csv               # Dataset
├── LinearRegressionModel.pkl       # Trained model
├── README.md
└── templates/
    ├── Home.html
    ├── CarPricePrediction.html
    └── CarPricePredictionResult.html
```

## 🖥️ Dashboard / Model / Output
- **Home page** → link to the prediction tool
- **Prediction form** → select company, model, year, kms driven, fuel type
- **Result page** → shows the predicted price

## 💡 Key Insights
- Brand and model are the strongest price drivers — luxury brands (BMW, Audi, Mercedes) price far above mass-market ones (Maruti, Hyundai, Tata)
- Higher `kms_driven` and older `year` generally push price down
- Fuel type (Petrol/Diesel) also shifts price depending on brand
- Prices range widely (₹30,000 to ₹85 lakh), which limits accuracy of a simple linear model at the extremes

## ✅ Results & Conclusion
The Linear Regression pipeline gives a fast, interpretable baseline for used-car price estimation and captures broad trends well (brand, age, mileage effects). Accuracy is limited on a small dataset (816 rows) with a wide price range, so this is best treated as a learning/demo project rather than a production pricing tool.

## ▶️ How to Run the Project
```bash
# 1. Install dependencies
pip install flask pandas numpy scikit-learn

# 2. Run the app
python Program1.py

# 3. Open in browser
http://127.0.0.1:5000/
```

## 🚀 Future Work
- Try non-linear models (Random Forest, XGBoost) for better accuracy
- Expand dataset with more listings and features (transmission, owner count, engine size, location)
- Add input validation for unseen categories

## 👤 Author and Contact
**Sanika Shinde** <br>
📧 sanikadshinde264@gmail.com | 🔗 [linkedin.com/in/sanikadshinde264](https://www.linkedin.com/in/sanikadshinde264)
