# 🎬 Movie Recommendation System

A Machine Learning based Movie Recommendation System built using Python, Pandas, Scikit-Learn, and Streamlit.

This project recommends movies similar to the selected movie using:
- genres
- keywords
- cast
- director
- movie overview

The recommendation engine is based on:
- CountVectorizer
- Cosine Similarity

---

# 🚀 Live Demo

🔗 Add your deployed Streamlit app link here


---

# 📂 Dataset

Dataset used:

🔗 TMDB 5000 Movie Dataset

Add dataset link here:

```text
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
```

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Pickle

---

# 📊 Machine Learning Workflow

1. Load datasets
2. Merge movie and credits datasets
3. Data preprocessing
4. Feature engineering
5. Convert text into vectors using CountVectorizer
6. Compute cosine similarity
7. Recommend similar movies

---

# ✨ Features

✅ Content-Based Recommendation System  
✅ Recommends 5 Similar Movies  
✅ Interactive Streamlit Web App  
✅ Clean and User-Friendly UI  
✅ Case-Insensitive Movie Search  

---

# 📁 Project Structure

```text
Movie-Recommendation-System/

│
├── data/
├── movie-recommendation.ipynb
├── app.py
├── movie_dict.pkl
├── similarity.pkl
├── requirements.txt
└── README.md
```

---

# ▶️ Run Locally

Clone repository:

```bash
git clone https://github.com/your-username/Movie-Recommendation-System.git
```

Go to project folder:

```bash
cd Movie-Recommendation-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit app:

```bash
python3 -m streamlit run app.py
```

---

# 🎥 Example Recommendation

Input:

```text
Batman Begins
```

Output:
- The Dark Knight
- Batman
- Superman Returns
- Man of Steel
- The Dark Knight Rises

---

# 📸 Screenshots

(Add screenshots of your web app here)

---

# 🌐 Future Improvements

- Add movie posters using TMDB API
- Add fuzzy search support
- Add genre-based recommendations
- Improve UI design
- Add collaborative filtering

---

# 👩‍💻 Author

Vanshika Sharma

Machine Learning Enthusiast 🚀
