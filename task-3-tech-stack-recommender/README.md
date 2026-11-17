# Tech Stack Recommender

Project 3 — DecodeLabs AI Engineering Internship (2026 Batch)

A content-based recommendation engine that matches a user's skills to the closest career/job role, using TF-IDF weighting and cosine similarity — built entirely from scratch with no external libraries (no scikit-learn, no numpy).

## What it does

You give it a list of skills (e.g. `python`, `docker`, `kubernetes`), and it ranks a set of job roles by how closely their required skill sets match yours — returning the top matches with a similarity score between 0 and 1.

This follows the classic recommendation system **Input → Process → Output** pipeline:

1. **Ingestion** — collect the user's skills (minimum 3)
2. **Scoring** — convert skills and roles into TF-IDF vectors, then compute cosine similarity between the user and every role
3. **Sorting** — rank roles by similarity score, highest first
4. **Filtering** — return only the top N results

## Files

| File | Purpose |
|---|---|
| `tech_stack_recommender.py` | Main script — loads data, builds vectors, runs the recommender |
| `raw_skills.csv` | Dataset of job roles and their associated skills (`role,skill` pairs) |
| `screenshots/` | Example runs |
| `README.md` | This file |

## How it works

### 1. TF-IDF (Term Frequency – Inverse Document Frequency)
Machines can't understand words like "Python" or "Docker" directly — everything gets converted into numbers.

- **TF (Term Frequency)** — how often a skill appears within one role's skill set
- **IDF (Inverse Document Frequency)** — penalizes skills that appear across *many* roles (generic, less useful for distinguishing) and rewards skills that are rare/specific

Multiplying TF × IDF gives each skill a weight — generic skills contribute less, specific ones contribute more.

### 2. Cosine Similarity
Once the user's skills and every role's skills are turned into TF-IDF vectors, cosine similarity measures the *angle* between them rather than raw distance. This means it doesn't matter if one role has a longer skill list than another — what matters is how closely aligned the two vectors are.

- **Score of 1** → perfect match
- **Score of 0** → no overlap at all
- Scores in between → partial match

### 3. Cold Start Handling
If a user's skills share zero vocabulary overlap with any role in the dataset, all similarity scores come out as 0 (rather than crashing) — this is the classic "cold start" problem in recommendation systems.

## Running it

```bash
python3 tech_stack_recommender.py
```

You'll be prompted to enter your skills one at a time:

```
Enter your skills one at a time (type 'done' when finished).
You must enter at least 3 skills.

Skill 1: python
Skill 2: aws
Skill 3: automation
Skill 4: done

Based on your skills ['python', 'aws', 'automation'], top career matches:

1. Cloud Architect — match score: 0.495
2. Data Scientist — match score: 0.091
3. ML Engineer — match score: 0.091
```

## Customizing

- **Add more roles/skills** — open `raw_skills.csv` and add new `role,skill` rows
- **Change how many results are shown** — edit `top_n` in the `recommend_careers()` call
- **Try the cold-start case** — enter skills that don't exist anywhere in the CSV (e.g. `photoshop`) and watch every score drop to 0

## Key concepts demonstrated

- Content-based filtering (as opposed to collaborative filtering)
- Vector space modeling of text data
- TF-IDF feature weighting
- Cosine similarity for measuring alignment between vectors
- Basic recommendation pipeline: ingest → score → sort → filter
- Handling the cold start problem

## Author

Khadija — AI Engineering Intern, DecodeLabs (2026 Batch)
