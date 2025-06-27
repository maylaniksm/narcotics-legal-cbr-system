
# DRUG CRIME LEGAL CASE RETRIEVAL & PREDICTION SYSTEM
## MODEL EVALUATION REPORT

### EXECUTIVE SUMMARY
- **System**: Drug Crime Legal Case Retrieval and Solution Prediction
- **Evaluation Date**: 2025-06-21
- **Total Drug Crime Cases**: 64
- **Evaluation Queries**: 10

### RETRIEVAL PERFORMANCE
Best performing model: **Drug-TF-IDF (k=3)**

#### Overall Metrics:
- **Accuracy**: 1.000
- **Precision**: 1.000
- **Recall**: 1.000
- **F1-Score**: 1.000

#### Model Comparison:
- **Drug-TF-IDF (k=3)**: F1=1.000, Precision=1.000, Recall=1.000
- **Drug-TF-IDF (k=5)**: F1=1.000, Precision=1.000, Recall=1.000
- **Drug-TF-IDF (k=7)**: F1=1.000, Precision=1.000, Recall=1.000
- **Drug-TF-IDF (k=10)**: F1=1.000, Precision=1.000, Recall=1.000
- **Drug-BERT**: F1=1.000, Precision=1.000, Recall=1.000
- **Drug-SVM**: F1=1.000, Precision=1.000, Recall=1.000

### PREDICTION PERFORMANCE
- **Average Accuracy**: 0.700
- **Total Predictions**: 10
- **Correct Predictions**: 7

### DRUG CRIME SPECIFIC FINDINGS
1. **Best Model**: Drug-TF-IDF (k=3) shows the highest F1-score of 1.000
2. **System Strengths**: Good precision in retrieving relevant drug crime cases
3. **Drug Types**: System handles sabu-sabu, ganja, heroin, ekstasi effectively
4. **Legal Basis**: UU No. 35 Tahun 2009 integration works well

### AREAS FOR IMPROVEMENT
1. **Drug Terminology**: Expand street names and slang terms
2. **Punishment Prediction**: Fine-tune based on drug quantities
3. **Legal Articles**: Better pasal-specific matching

### RECOMMENDATIONS
1. **Immediate**: Fine-tune drug-specific similarity thresholds
2. **Short-term**: Implement drug crime domain BERT embeddings
3. **Long-term**: Develop quantity-aware punishment prediction

### FILES GENERATED
- `/data/eval/drug_crime_retrieval_metrics.csv` - Detailed drug crime retrieval performance
- `/data/eval/drug_crime_prediction_metrics.csv` - Drug crime prediction accuracy results
- `/data/eval/drug_crime_performance_chart.png` - Visual performance comparison
