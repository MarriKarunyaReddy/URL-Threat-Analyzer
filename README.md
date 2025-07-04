# 🛡️ Malicious URL Detector

A beginner-friendly machine learning-based web application that detects whether a given URL is **malicious (phishing)** or **safe**, based on simple URL features. Built using Python, trained on a real-world phishing dataset, and deployed using Streamlit.

---

## 🔍 Project Overview

This project demonstrates how to apply basic data science techniques to a cybersecurity problem: **detecting harmful URLs**. The model is trained using handcrafted features extracted from the URL itself (e.g., length, presence of suspicious words or characters).

---

## ✅ Features

- 🚀 Classifies input URLs as **malicious** or **benign**
- 🧠 Trained with a lightweight ML model (Random Forest or Logistic Regression)
- 🔍 Uses real-world phishing datasets for training
- 🧪 Feature engineering based purely on URL string analysis
- 🌐 Streamlit-powered web app UI for real-time predictions
- 📦 Deployable on Streamlit Cloud and shareable via link

---

## 🧠 Tech Stack

| Area         | Tools Used                             |
|--------------|----------------------------------------|
| Language     | Python                                 |
| Libraries    | scikit-learn, pandas, joblib, streamlit |
| UI           | Streamlit                              |
| Deployment   | Streamlit Cloud                        |
| Versioning   | Git + GitHub                           |

---

## 📊 Dataset

- **Source**: [Kaggle - Malicious URLs Dataset](https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset)
- **Format**: `.csv` with `url` and `label` columns
- **Classes**:
  - `bad` – Phishing or malicious
  - `good` – Safe / benign

---
