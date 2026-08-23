from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle as pkl
import os

app = Flask(__name__)


@app.route("/")
def Home():
    return render_template("Home.html")


@app.route("/Car-Price-Prediction")
def CarPricePrediction():

    dataset = pd.read_csv("cleaned_Data8.csv")

    companies = sorted(dataset["company"].unique())
    names = sorted(dataset["name"].unique())

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

    model_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "LinearRegressionModel.pkl"
    )

    with open(model_path, "rb") as file:
        pipe = pkl.load(file)

    columns = [
        "name",
        "company",
        "year",
        "kms_driven",
        "fuel_type"
    ]

    data = np.array(
        [name, company, year, kms_driven, fuel_type],
        dtype=object
    ).reshape(1, 5)

    myinput = pd.DataFrame(
        columns=columns,
        data=data
    )

    result = pipe.predict(myinput)

    return render_template(
        "CarPricePredictionResult.html",
        company=company,
        name=name,
        year=year,
        kms_driven=kms_driven,
        fuel_type=fuel_type,
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)