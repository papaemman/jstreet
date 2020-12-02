**Project Steps**


1. **EDA** 
    
    * Load and understand data, define datatypes

    * Create visualizations, calculate statistics, reveal interesting relationships between features and targets
    
    * Data preprocessing (NAs, categorical encoding, text data)
    
    * Identify and remove features with data leakage 
    

2. Create a **full ML pipeline** with baseline model (from test, to prediction)

3. Create **cross-validation procedure**, using AUCROC evaluation metric

4. **Feature engineering** based on supplementary dataset

5. Define **feature preprocessing** steps

6. Using train data and cross validation, **experiment** with all algorithms from the course.

7. **Submit** the top 3 algorithms, based on CV results

----

**More advanced steps**

1. Create more features and apply feature selection 

2. Test more advanced algorithms (eg xgboost, lightgbm)

3. Define a structure to track every experiment (custom solution, or ready-to-use servise like Neptune)



For categorical encoding, it's use bot train and test set,
in order to avoid problems with new categories in test set.