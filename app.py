from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import random
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load dataset
df = pd.read_csv("disney-characters.csv")

# ---- Existing Routes ----

@app.route("/characters", methods=["GET"])
def all_characters():
    return jsonify(df.dropna().to_dict(orient="records"))

@app.route("/random", methods=["GET"])
def random_character():
    return jsonify(df.dropna().sample(1).iloc[0].to_dict())

@app.route("/hero/<name>", methods=["GET"])
def get_hero(name):
    result = df[df["hero"].str.lower() == name.lower()]
    if result.empty:
        return jsonify({"error": "Hero not found"}), 404
    return jsonify(result.iloc[0].to_dict())

# ---- New ML-like Endpoint ----

def get_embedding(text):
    # Dummy embedding: ASCII-based fallback
    return np.array([ord(c) for c in text.lower()[:10]]).reshape(1, -1)

@app.route("/similar/<name>", methods=["GET"])
def similar_characters(name):
    try:
        if name.lower() not in df["hero"].str.lower().values:
            return jsonify([])

        base_embed = get_embedding(name)
        df["similarity"] = df["hero"].apply(lambda h: cosine_similarity(base_embed, get_embedding(h))[0][0])
        filtered_df = df[df["hero"].str.lower() != name.lower()]
        top_similar = filtered_df.sort_values(by="similarity", ascending=False).head(5)

        return jsonify(top_similar[["hero", "movie_title", "release_date", "villian", "song"]].to_dict(orient="records"))

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---- Run App ----
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
