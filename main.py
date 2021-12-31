from phrase_similarity import dedup_by_embedding, dedup_by_stemming

print(dedup_by_stemming(['civilization', 'civil', 'computer']))

print(dedup_by_stemming(["computational", "computer", "machine", "compute"]))

print(dedup_by_stemming(["institutional", "institute", "thisworddoesnotexist"]))

print(dedup_by_embedding(["database technique", "database techniques",

                          "cloud network", "cloud networks",

                          "machine learning",

                          "supervised learning",

                          "semi supervised learning",

                          "un supervised learning",

                          "data mining",

                          "data mining technique", "data mining techniques", "data mining strategy"]))

print(dedup_by_embedding(["Linear Neural network",

                          "Convolutional Neural Network",

                          "Database system", "Database systems", "database system",

                          "data mining techniques", "Data mining methods",

                          "programming language", "program languages",

                          "cloud storage",

                          "cloud network", "cloud networks"]))

print(dedup_by_embedding(["machine learning", "machine-learning", "machine learn",

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
                          ]))

print(dedup_by_embedding([
    "data mining",

    "data mining algorithm", "data mining technique",

    "data structure", "data structures",

    "database design",

    "data stream", "data streams",

    "database", "databases",

    "data analysis", "data analytics", "big data analytics",

    "data visualization",

    "database system",

    "data privacy", "data security",

    "image database",

    "graph database",
]))

print(dedup_by_embedding(["helloworld", "world", "network"]))
