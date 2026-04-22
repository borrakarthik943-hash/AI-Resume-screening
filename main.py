from chains.extraction_chain import extract_data   # ✅ ADD THIS

resume = """
Python developer with 2 years experience in machine learning,
worked with TensorFlow, Pandas, SQL.
"""

result = extract_data(resume)
print(result.content)

