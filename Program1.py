from flask import Flask, render_template, request
import pandas as pd
import pickle as pkl

app = Flask(__name__)


@app.route("/")
def Home():
    return render_template("Home.html")


@app.route("/Car-Price-Prediction")
def CarPricePrediction():

    dataset = pd.read_csv("cleaned_Data8.csv")

    companies = sorted(dataset["company"].dropna().unique())
    names = sorted(dataset["name"].dropna().unique())

    return render_template(
        "CarPricePrediction.html",
        companies=companies,
        names=names
    )


@app.route("/Car-Price-Prediction-Result")
def CarPricePredictionResult():

    company = request.args.get("company")
    name = request.args.get("name")
    year = request.args.get("year")
    kms_driven = request.args.get("kms_driven")
    fuel_type = request.args.get("fuel_type")

    # Convert numeric inputs from strings to integers
    try:
        year = int(year)
        kms_driven = int(kms_driven)
    except (TypeError, ValueError):
        return "Invalid year or kilometers driven value.", 400

    # Load trained pipeline
    with open("LinearRegressionModel.pkl", "rb") as file:
        pipe = pkl.load(file)

    # IMPORTANT:
    # Create DataFrame directly instead of using np.array()
    myinput = pd.DataFrame({
        "name": [name],
        "company": [company],
        "year": [year],
        "kms_driven": [kms_driven],
        "fuel_type": [fuel_type]
    })

    # Make prediction
    result = pipe.predict(myinput)

    # Get single prediction value
    predicted_price = float(result[0])

    return render_template(
        "CarPricePredictionResult.html",
        company=company,
        name=name,
        year=year,
        kms_driven=kms_driven,
        fuel_type=fuel_type,
        result=predicted_price
    )


if __name__ == "__main__":
    app.run(debug=True)