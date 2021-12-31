from phrase_similarity import dedup_by_embedding, dedup_by_stemming

# Test1
result1 = dedup_by_stemming(['civilization', 'civil', 'computer'])
sol1 = ['civilization', 'computer']
if result1 == sol1:
    print("Test 1 Passed")
else:
    print("Test 1 Failed")
    print(result1)
    exit()


#Test 2
result2 = dedup_by_embedding(["database technique", "database techniques",

                          "cloud network", "cloud networks",

                          "machine learning",

                          "supervised learning",

                          "un supervised learning",

                          "data mining",

                          "data mining technique", "data mining techniques"])
sol2 = ['database technique', 
        'cloud network', 
        'machine learning', 
        'supervised learning', 
        'un supervised learning', 
        'data mining', 
        'data mining technique'
        ]
if result2 == sol2:
    print("Test 2 Passed")
else:
    print("Test 2 Failed")
    print(result2)
    exit()



#Test 3
result3 = dedup_by_embedding(["Linear Neural network",

                          "Convolutional Neural Network",

                          "Database system", "Database systems", "database system",

                          "data mining techniques", "Data mining methods",

                          "programming language", "program languages",

                          "cloud storage",

                          "cloud network", "cloud networks"])

sol3 = ['linear neural network', 
    'convolutional neural network', 
    'database system', 
    'data mining techniques', 
    'programming language', 
    'cloud storage', 
    'cloud network']

if result3 == sol3:
    print("Test 3 Passed")
else:
    print("Test 3 Failed")
    print(result3)
    exit()



#Test 4
result4 = dedup_by_embedding(["machine learning", "machine-learning", "machine learn",

                          "machine translation",

                          "machine translation system",

                          "machine translation evaluation",

                          "machine vision",

                          "machine vision system",

                          "machine vision application",

                          "machine intelligence", "machine consciousness", "machine perception",

                          "machine learning algorithm", "machine learning algorithms", "machine learn algorithm",

                          "machine learning techniques", "machine learning technique", "machine learn technique",
                          "machine learn method", "machine learning methods", "machine learning method",

                          "machine learning approach", "machine learn approach",

                          "machine learning classifiers", "machine learning classifier",

                          "machine-type communications", "machine type communications",
                          "machine-type communication", "machine type communication",

                          "machine structure", "machine structures"
                          ])

sol4 = ['machine learning', 
    'machine translation', 
    'machine translation system', 
    'machine translation evaluation', 
    'machine vision', 
    'machine vision system', 
    'machine vision application', 
    'machine consciousness', 
    'machine learning algorithm', 
    'machine learning techniques', 
    'machine learning approach', 
    'machine learning classifiers', 
    'machine type communications', 
    'machine structure']
if result4 == sol4:
    print("Test 4 Passed")
else:
    print("Test 4 Failed")
    print(result4)
    exit()



#Test 5
result5 = dedup_by_embedding([
    "data mining",

    "data mining algorithm", "data mining technique",

    "data structure", "data structures",

    "database design",

    "data stream", "data streams",

    "database", "databases",

    "data analysis", "data analytics", 
    
    "big data analytics",

    "data visualization",

    "database system",

    "data privacy", "data security",

    "image database",

    "graph database",
])

sol5 = ['data mining', 
    'data mining algorithm', 
    'data mining technique', 
    'data structure', 
    'database design', 
    'data stream', 
    'database', 
    'data analysis', 
    'big data analytics', 
    'data visualization', 
    'database system', 
    'data privacy', 
    'image database', 
    'graph database']


if result5 == sol5:
    print("Test 5 Passed")
else:
    print("Test 5 Failed")
    print(result5)
    exit()


#Test 6
result6 = dedup_by_embedding(["helloworld", "world", "network"])
sol6 = ["helloworld", "world", "network"]
if result6 == sol6:
    print("Test 6 Passed")
else:
    print("Test 6 Failed")
    print(result6)
    exit()
