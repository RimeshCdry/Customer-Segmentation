# K-Means Clustering Project 🌟

## Overview 📄

This project applies **K-Means Clustering** to identify patterns in data through **unsupervised learning**. The pipeline includes data collection, **Exploratory Data Analysis (EDA)**, choosing the optimal number of clusters using the **Within-Cluster Sum of Squares (WCSS)** method, model training, and results visualization. Additionally, a **UI** for the K-Means model has been developed, making API calls to interact with the model hosted on a local server.

---

## Project Workflow 🔄

### 1. Data Collection 📂
- The dataset was collected from **Kaggle**.
- Performed data pre-processing, including:
  - Handling missing values.
  - Feature scaling.
  - Removing duplicates.

### 2. Exploratory Data Analysis (EDA) 🔍
- Generated summary statistics to understand data distribution.
- Checked for missing values and handled them appropriately.

### 3. Within-Cluster Sum of Squares (WCSS) 📊
- Calculated WCSS for different cluster values.
- Used the **Elbow Method** to determine the optimal number of clusters.

### 4. Plotting the Elbow Graph 📈
- The Elbow Graph was plotted using **Matplotlib** to visualize the WCSS values.
- The optimal number of clusters was selected based on the **elbow point**.

### 5. Choosing the Optimum Number of Clusters 🔢
- Based on the Elbow Method, the best number of clusters was determined.
- Applied domain knowledge to validate the choice.

### 6. Training the Model 🤖
- The **K-Means clustering model** was trained using **Scikit-Learn**.
- The dataset was divided into clusters based on selected features.

### 7. Visualizing the Clusters 🎨
- **Scatter plots** were used to display the clustered data.
- Cluster centroids were marked for better visualization.
- **2D plots** were generated for better insights.

### 8. Prediction 🔮
- The model can predict the cluster for new data points.
- Users can provide input via the UI to get predictions.

---

## UI Development 🖥️
- A **Graphical User Interface** was developed using **Streamlit**.

---

## API Development 🌐
- A **Flask API** was built to serve the K-Means model.
- **Endpoints**:
  - `/predict` – Accepts user data and returns cluster predictions.

---

## Technologies Used 💻
- **Python** (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn)
- **Streamlit** (for UI)
- **Flask** (for API)
- **Jupyter Notebook** (for EDA and model training)

---

## Installation Guide 🛠️

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/kmeans-clustering-ui.git
   cd kmeans-clustering-ui
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask API:
  ```bash
  python server.py
  ```
4. Run the Streamlit UI:
  ```bash
  streamlit run app.py
  ```

## Usage 🚀
### 1. Open the Streamlit UI in a browser.
### 2. Enter data points for prediction.
### 3. The API processes the request and returns cluster information.
### 4. View visualizations of the clustered data.

---

## Results & Insights 📊
### 1. The clustering model successfully identified meaningful patterns in the dataset.
### 2. The UI provides an interactive way to explore clusters and predictions.
### 3. Cluster distribution insights can help in business segmentation and data-driven decision-making.

---

## Future Enhancements 🚧
### 1. Enable real-time data processing in the UI.
### 2. Deploy the model on a cloud server for wider accessibility.
### 3. Compare with other clustering algorithms for improved performance.

---

## 👥 Contact
For questions or feedback, feel free to reach out:

- GitHub: [@RimeshCdry](https://github.com/RimeshCdry)
- Email: rimeshcdry45@gmail.com
- Linkedin: https://www.linkedin.com/in/rimesh-chaudhary-09a25a30a
