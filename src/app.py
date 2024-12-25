import streamlit as st
import pandas as pd
from formulas import *

# Set page to wide mode
st.set_page_config(layout="wide")

st.title("劉倢瑜 - Discrete Mathematics - Programming Assignment 1")

# Initialize session state for results if not exists
if 'results' not in st.session_state:
    st.session_state.results = ["" for _ in range(4)]
if 'sequences' not in st.session_state:
    st.session_state.sequences = {
        'catalan': "", 'triangular': "", 'harmonic': "",
        'fibonacci': "", 'lucas': ""
    }
if 'advanced' not in st.session_state:
    st.session_state.advanced = {'eulerian': "", 'stirling': ""}

# Basic Formulas Section
st.subheader("Basic Combinatorial Formulas")

# Input controls for basic formulas
col1, col2, col3, col4 = st.columns(4)
with col1:
    n = st.number_input("**n** =", min_value=0, value=7, key="basic_n")
with col2:
    r = st.number_input("**r** =", min_value=0, value=3, key="basic_r")
    

col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("Compute All Basic", key="compute_basic"):
        st.session_state.results[0] = P(n, r)
        st.session_state.results[1] = C(n, r)
        st.session_state.results[2] = arrangement_with_rep(n, r)
        st.session_state.results[3] = selection_with_rep(n, r)
        st.rerun()
with col2:
    if st.button("Reset Basic", key="reset_basic"):
        st.session_state.results = ["" for _ in range(4)]
        st.rerun()

# Create the main calculation table
data = {
    "Formula": [f"P({n}, {r})", f"C({n}, {r})", f"{n}^{r}", f"C({r}+{n}-1, {r})"],
    "Result": st.session_state.results,
    "Compute": ["Permutation", "Combination", "Arrangement with repetition", "Selection with repetition"],
    "Order relevant": ["yes", "no", "yes", "no"],
    "Repetition": ["no", "no", "yes", "yes"],
    "Memo": [
        "Permutations of size r from n distinct objects",
        "Selections/Combinations of size r from n distinct objects",
        "Arrangements with repetition of size r from n distinct objects",
        "Selections with repetition of size r from n distinct objects"
    ]
}

df = pd.DataFrame(data)

# Create column headers with adjusted widths
cols = st.columns([2, 4, 2, 0.5, 0.5, 3])
cols[0].write("**Formula**")
cols[1].write("**Result**")
cols[2].write("**Compute**")
cols[3].write("**Ord**")
cols[4].write("**Rep**")
cols[5].write("**Memo**")

# Display the table with buttons
for idx, row in df.iterrows():
    cols = st.columns([2, 4, 2, 0.5, 0.5, 3])
    
    cols[0].write(row["Formula"])
    cols[1].write(str(st.session_state.results[idx]))
    
    if cols[2].button(row["Compute"], key=f"btn_{idx}"):
        if row["Formula"] == "P(n, r)":
            st.session_state.results[idx] = P(n, r)
        elif row["Formula"] == "C(n, r)":
            st.session_state.results[idx] = C(n, r)
        elif row["Formula"] == "n^r":
            st.session_state.results[idx] = arrangement_with_rep(n, r)
        elif row["Formula"] == "C(r+n-1, r)":
            st.session_state.results[idx] = selection_with_rep(n, r)
        st.rerun()
    
    cols[3].write(row["Order relevant"])
    cols[4].write(row["Repetition"])
    cols[5].write(row["Memo"])

# Special sequences section
st.subheader("Special Sequences (first n terms)")

col1, col2, col3, col4 = st.columns(4)
with col1:
    seq_n = st.number_input("n = ", min_value=0, value=7, key="seq_n")

col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("Compute All Sequences", key="compute_seq"):
        st.session_state.sequences['catalan'] = [catalan(i) for i in range(seq_n)]
        st.session_state.sequences['triangular'] = [triangular(i) for i in range(1, seq_n+1)]
        st.session_state.sequences['harmonic'] = [round(harmonic(i), 4) for i in range(1, seq_n+1)]
        st.session_state.sequences['fibonacci'] = [fibonacci(i) for i in range(seq_n)]
        st.session_state.sequences['lucas'] = [lucas(i) for i in range(seq_n)]
        st.rerun()
with col2:
    if st.button("Reset Sequences", key="reset_seq"):
        st.session_state.sequences = {k: "" for k in st.session_state.sequences}
        st.rerun()

cols = st.columns([2, 5, 2, 3])
cols[0].write("**Sequence**")
cols[1].write("**Result**")
cols[2].write("**Compute**")
cols[3].write("**Description**")

sequences = [
    ("Catalan", "catalan", "Numbers related to various counting problems"),
    ("Triangular", "triangular", "Sum of first n positive integers"),
    ("Harmonic", "harmonic", "Sum of reciprocals of first n positive integers"),
    ("Fibonacci", "fibonacci", "Each number is sum of two preceding ones"),
    ("Lucas", "lucas", "Similar to Fibonacci but starts with 2,1")
]

for name, key, desc in sequences:
    cols = st.columns([2, 5, 2, 3])
    cols[0].write(f"{name} numbers")
    cols[1].write(str(st.session_state.sequences[key]))
    if cols[2].button(f"Compute {name}", key=f"btn_{key}"):
        if key == 'catalan':
            st.session_state.sequences[key] = [catalan(i) for i in range(seq_n)]
        elif key == 'triangular':
            st.session_state.sequences[key] = [triangular(i) for i in range(1, seq_n+1)]
        elif key == 'harmonic':
            st.session_state.sequences[key] = [round(harmonic(i), 4) for i in range(1, seq_n+1)]
        elif key == 'fibonacci':
            st.session_state.sequences[key] = [fibonacci(i) for i in range(seq_n)]
        elif key == 'lucas':
            st.session_state.sequences[key] = [lucas(i) for i in range(seq_n)]
        st.rerun()
    cols[3].write(desc)

# Advanced numbers section
st.subheader("Advanced Numbers")
col1, col2, col3, col4 = st.columns(4)
with col1:
    adv_m = st.number_input("m = ", min_value=0, value=7, key="adv_m")
with col2:
    adv_k = st.number_input("k = ", min_value=0, value=3, key="adv_k")

col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("Compute All Advanced", key="compute_adv"):
        st.session_state.advanced['eulerian'] = eulerian(adv_m, adv_k)
        st.session_state.advanced['stirling'] = stirling2(adv_m, min(adv_m, adv_k))
        st.rerun()
with col2:
    if st.button("Reset Advanced", key="reset_adv"):
        st.session_state.advanced = {k: "" for k in st.session_state.advanced}
        st.rerun()

cols = st.columns([2, 5, 2, 3])
cols[0].write("**Formula**")
cols[1].write("**Result**")
cols[2].write("**Compute**")
cols[3].write("**Description**")

advanced_numbers = [
    (f"A({adv_m},{adv_k})", "eulerian", "Eulerian number", "Number of permutations with k ascents"),
    (f"S({adv_m},{min(adv_m,adv_k)})", "stirling", "Stirling number", "Number of ways to partition m objects into n non-empty subsets")
]

for formula, key, name, desc in advanced_numbers:
    cols = st.columns([2, 5, 2, 3])
    cols[0].write(formula)
    cols[1].write(str(st.session_state.advanced[key]))
    if cols[2].button(f"Compute {name}", key=f"btn_{key}"):
        if key == 'eulerian':
            st.session_state.advanced[key] = eulerian(adv_m, adv_k)
        elif key == 'stirling':
            st.session_state.advanced[key] = stirling2(adv_m, min(adv_m, adv_k))
        st.rerun()
    cols[3].write(desc)

# Bonus section
st.subheader("Bonus: Distribution Problems")

# Initialize session state for bonus results if not exists
if 'bonus' not in st.session_state:
    st.session_state.bonus = ["" for _ in range(8)]

col1, col2, col3, col4 = st.columns(4)
with col1:
    bonus_m = st.number_input("m = ", min_value=0, value=7, key="bonus_m")
with col2:
    bonus_n = st.number_input("n = ", min_value=0, value=3, key="bonus_n")

col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("Compute All Distributions", key="compute_bonus"):
        # Calculate all distribution results
        st.session_state.bonus[0] = arrangement_with_rep(bonus_n, bonus_m)  # n^m
        st.session_state.bonus[1] = onto(bonus_m, bonus_n)  # n!S(m,n)
        st.session_state.bonus[2] = sum_stirling2_to_n(bonus_m, bonus_n)  # Sum of S(m,k)
        st.session_state.bonus[3] = stirling2(bonus_m, bonus_n)  # S(m,n)
        st.session_state.bonus[4] = C(bonus_m + bonus_n - 1, bonus_m)  # C(m+n-1,m)
        st.session_state.bonus[5] = C(bonus_m - 1, bonus_m - bonus_n)  # C(m-1,m-n)
        st.session_state.bonus[6] = partition_with_zeros(bonus_m, bonus_n)  # p(m,≤n)
        st.session_state.bonus[7] = partition(bonus_m, bonus_n)  # p(m,n)
        st.rerun()
with col2:
    if st.button("Reset Distributions", key="reset_bonus"):
        st.session_state.bonus = ["" for _ in range(8)]
        st.rerun()

# Create column headers
cols = st.columns([2, 4, 2, 0.5, 0.5, 3])
cols[0].write("**Formula**")
cols[1].write("**Result**")
cols[2].write("**Compute**")
cols[3].write("**Dist**")
cols[4].write("**Empty**")
cols[5].write("**Interpretation**")

# Distribution problems data
distributions = [
    ("n^m", 0, "Power", "yes", "yes", 
     "Each of the m distinct objects may be distributed into any of the n distinct containers"),
    ("n!S(m,n)", 1, "Onto", "yes", "no", 
     "Each of the m distinct objects may be distributed onto any of the n distinct containers with no containers empty"),
    ("S(m,1)+...+S(m,n)", 2, "Sum S", "no", "yes", 
     "m distinct objects onto 1, 2, ..., n identical containers, leaving no container empty"),
    ("S(m,n)", 3, "Stirling2", "no", "no", 
     "m distinct objects onto n identical containers, leaving no container empty"),
    ("C(m+n-1,m)", 4, "Stars&Bars1", "no", "yes", 
     "Ordering food from the view of kitchen (m kids (identical), n foods (distinct))"),
    ("C(m-1,m-n)", 5, "Stars&Bars2", "no", "no", 
     "Deliver one object to each of the n distinct containers first, then distribute m-n objects"),
    ("p(m,≤n)", 6, "Partition1", "no", "yes", 
     "Partition integer m into at most n summands (with some 0 summands)"),
    ("p(m,n)", 7, "Partition2", "no", "no", 
     "Partition integer m into exactly n summands (with no container empty)")
]

# Display the distribution problems
for formula, idx, name, dist, empty, interp in distributions:
    cols = st.columns([2, 4, 2, 0.5, 0.5, 3])
    cols[0].write(formula)
    cols[1].write(str(st.session_state.bonus[idx]))
    
    if cols[2].button(name, key=f"btn_bonus_{idx}"):
        if idx == 0:
            st.session_state.bonus[idx] = arrangement_with_rep(bonus_n, bonus_m)
        elif idx == 1:
            st.session_state.bonus[idx] = onto(bonus_m, bonus_n)
        elif idx == 2:
            st.session_state.bonus[idx] = sum_stirling2_to_n(bonus_m, bonus_n)
        elif idx == 3:
            st.session_state.bonus[idx] = stirling2(bonus_m, bonus_n)
        elif idx == 4:
            st.session_state.bonus[idx] = C(bonus_m + bonus_n - 1, bonus_m)
        elif idx == 5:
            st.session_state.bonus[idx] = C(bonus_m - 1, bonus_m - bonus_n)
        elif idx == 6:
            st.session_state.bonus[idx] = partition_with_zeros(bonus_m, bonus_n)
        elif idx == 7:
            st.session_state.bonus[idx] = partition(bonus_m, bonus_n)
        st.rerun()
    
    cols[3].write(dist)
    cols[4].write(empty)
    cols[5].write(interp)
