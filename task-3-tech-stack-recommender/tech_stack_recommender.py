import csv
import math

# ---------- Step 1: Load dataset from CSV ----------
def load_job_roles(csv_path):
    """Reads role,skill rows and groups them into {role: [skills]}"""
    job_roles = {}
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            role = row["role"].strip()
            skill = row["skill"].strip().lower()
            job_roles.setdefault(role, []).append(skill)
    return job_roles

# ---------- Step 2: Build vocabulary ----------
def build_vocab(docs):
    vocab = set()
    for doc in docs:
        vocab.update(doc)
    return sorted(vocab)

# ---------- Step 3: TF ----------
def term_freq(doc):
    tf = {}
    for term in doc:
        tf[term] = tf.get(term, 0) + 1
    total = len(doc)
    return {term: count / total for term, count in tf.items()}

# ---------- Step 4: IDF ----------
def inverse_doc_freq(docs, vocab):
    N = len(docs)
    idf = {}
    for term in vocab:
        containing = sum(1 for doc in docs if term in doc)
        idf[term] = math.log(N / containing) if containing else 0
    return idf

# ---------- Step 5: TF-IDF vector ----------
def tfidf_vector(doc, vocab, idf):
    tf = term_freq(doc)
    return [tf.get(term, 0) * idf[term] for term in vocab]

# ---------- Step 6: Cosine similarity ----------
def cosine_similarity(vec_a, vec_b):
    dot = sum(a * b for a, b in zip(vec_a, vec_b))
    norm_a = math.sqrt(sum(a * a for a in vec_a))
    norm_b = math.sqrt(sum(b * b for b in vec_b))
    if norm_a == 0 or norm_b == 0:
        return 0
    return dot / (norm_a * norm_b)

# ---------- Step 7: Recommender pipeline ----------
def recommend_careers(user_skills, job_roles, top_n=3):
    user_skills = [s.lower() for s in user_skills]
    roles = list(job_roles.keys())
    docs = list(job_roles.values())

    all_docs = docs + [user_skills]
    vocab = build_vocab(all_docs)
    idf = inverse_doc_freq(all_docs, vocab)

    user_vec = tfidf_vector(user_skills, vocab, idf)

    scores = []
    for role, doc in zip(roles, docs):
        role_vec = tfidf_vector(doc, vocab, idf)
        score = cosine_similarity(user_vec, role_vec)
        scores.append((role, round(score, 3)))

    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:top_n]

# ---------- Interactive mode ----------
def get_user_skills():
    """Asks the user to type in skills, one at a time, minimum 3."""
    print("Enter your skills one at a time (type 'done' when finished).")
    print("You must enter at least 3 skills.\n")

    skills = []
    while True:
        skill = input(f"Skill {len(skills) + 1}: ").strip()
        if skill.lower() == "done":
            if len(skills) < 3:
                print(f"Need at least 3 skills, you've entered {len(skills)}. Keep going.")
                continue
            break
        if skill:
            skills.append(skill)
    return skills

# ---------- Run ----------
if __name__ == "__main__":
    job_roles = load_job_roles("raw_skills.csv")

    user_input = get_user_skills()
    top_matches = recommend_careers(user_input, job_roles)

    print(f"\nBased on your skills {user_input}, top career matches:\n")
    for i, (role, score) in enumerate(top_matches, 1):
        print(f"{i}. {role} — match score: {score}")
