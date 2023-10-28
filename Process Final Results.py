import io


# luceneAnswers = [5, 6, 10, 4, 7, 1, 19]
# realAnswers = [6, 8, 10]


# calculate precision
def calculate_precision(realAnswers, luceneAnswers):
    TP = 0
    for ans in luceneAnswers:
        if ans in realAnswers:
            TP += 1
    FP = len(luceneAnswers) - TP
    P = TP / (FP + TP)
    return P


# calculate recall
def calculate_recall(realAnswers, luceneAnswers):
    TP = 0
    for ans in luceneAnswers:
        if ans in realAnswers:
            TP += 1
    FN = len(realAnswers) - TP
    R = TP / (FN + TP)
    return R


# calculate F_measure
def calculate_F_measure(P, R):
    if P != 0 and R != 0:
        F_measure = (2 * P * R) / (P + R)
    else:
        F_measure = 0
    return F_measure


# calculate MAP
def calculate_MAP(realAnswers, luceneAnswers):
    k = len(realAnswers)
    similar = 0
    precisionAt = []
    counter = 0
    for i in luceneAnswers:
        counter += 1
        if i in realAnswers:
            similar += 1
            precisionAt.append(similar / counter)
    MAP = sum(precisionAt) / k
    return MAP


# process relavence assesments
f = io.open('RelevanceAssesment/RelevanceAssesment.txt', mode="r", encoding="utf-8")
relevanceAssesments = []
queryCounter = 0
while queryCounter < 47:
    line = f.readline()
    results = []
    if "persian_query" in line:
        queryCounter += 1
        line = f.readline()
        raw_results = line.split(" ")
        results = []
        for result in raw_results:
            if "\n" in result:
                result = result.replace('\n', '')
                results.append(result)
            else:
                if result != None:
                    results.append(result)
        relevanceAssesments.append(results)

# process NT_hazm
f = io.open('results/NT_hazm.txt', mode="r", encoding="utf-8")
NT_hazm = []
queryCounter = 0
while queryCounter < 47:
    line = f.readline()
    results = []
    if "total matching documents" in line:
        queryCounter += 1
        line = f.readline()
        raw_results = line.split(" ")
        results = []
        for result in raw_results:
            if "\n" in result:
                result = result.replace('\n', '')
                results.append(result)
            else:
                if result != None:
                    results.append(result)
        NT_hazm.append(results)

# process NT_parsivar
f = io.open('results/NT_parsivar.txt', mode="r", encoding="utf-8")
NT_parsivar = []
queryCounter = 0
while queryCounter < 47:
    line = f.readline()
    results = []
    if "total matching documents" in line:
        queryCounter += 1
        line = f.readline()
        raw_results = line.split(" ")
        results = []
        for result in raw_results:
            if "\n" in result:
                result = result.replace('\n', '')
                results.append(result)
            else:
                if result != None:
                    results.append(result)
        NT_parsivar.append(results)

# process NTR_hazm
f = io.open('results/NTR_hazm.txt', mode="r", encoding="utf-8")
NTR_hazm = []
queryCounter = 0
while queryCounter < 47:
    line = f.readline()
    results = []
    if "total matching documents" in line:
        queryCounter += 1
        line = f.readline()
        raw_results = line.split(" ")
        results = []
        for result in raw_results:
            if "\n" in result:
                result = result.replace('\n', '')
                results.append(result)
            else:
                if result != None:
                    results.append(result)
        NTR_hazm.append(results)

# process NTR_parsivar
f = io.open('results/NTR_parsivar.txt', mode="r", encoding="utf-8")
NTR_parsivar = []
queryCounter = 0
while queryCounter < 47:
    line = f.readline()
    results = []
    if "total matching documents" in line:
        queryCounter += 1
        line = f.readline()
        raw_results = line.split(" ")
        results = []
        for result in raw_results:
            if "\n" in result:
                result = result.replace('\n', '')
                results.append(result)
            else:
                if result != None:
                    results.append(result)
        NTR_parsivar.append(results)

# process NTRL_hazm
f = io.open('results/NTRL_hazm.txt', mode="r", encoding="utf-8")
NTRL_hazm = []
queryCounter = 0
while queryCounter < 47:
    line = f.readline()
    results = []
    if "total matching documents" in line:
        queryCounter += 1
        line = f.readline()
        raw_results = line.split(" ")
        results = []
        for result in raw_results:
            if "\n" in result:
                result = result.replace('\n', '')
                results.append(result)
            else:
                if result != None:
                    results.append(result)
        NTRL_hazm.append(results)

# process NTRL_parsivar
f = io.open('results/NTRL_parsivar.txt', mode="r", encoding="utf-8")
NTRL_parsivar = []
queryCounter = 0
while queryCounter < 47:
    line = f.readline()
    results = []
    if "total matching documents" in line:
        queryCounter += 1
        line = f.readline()
        raw_results = line.split(" ")
        results = []
        for result in raw_results:
            if "\n" in result:
                result = result.replace('\n', '')
                results.append(result)
            else:
                if result != None:
                    results.append(result)
        NTRL_parsivar.append(results)

# process NTRS_hazm
f = io.open('results/NTRS_hazm.txt', mode="r", encoding="utf-8")
NTRS_hazm = []
queryCounter = 0
while queryCounter < 47:
    line = f.readline()
    results = []
    if "total matching documents" in line:
        queryCounter += 1
        line = f.readline()
        raw_results = line.split(" ")
        results = []
        for result in raw_results:
            if "\n" in result:
                result = result.replace('\n', '')
                results.append(result)
            else:
                if result != None:
                    results.append(result)
        NTRS_hazm.append(results)

# process raw
f = io.open('results/raw.txt', mode="r", encoding="utf-8")
raw = []
queryCounter = 0
while queryCounter < 47:
    line = f.readline()
    results = []
    if "total matching documents" in line:
        queryCounter += 1
        line = f.readline()
        raw_results = line.split(" ")
        results = []
        for result in raw_results:
            if "\n" in result:
                result = result.replace('\n', '')
                results.append(result)
            else:
                if result != None:
                    results.append(result)
        raw.append(results)

# calculations NT_hazm
i = 0
NT_hazm_precision = []
NT_hazm_recall = []
NT_hazm_F = []
NT_hazm_Map = []

for result in NT_hazm:
    P = calculate_precision(relevanceAssesments[i], result)
    R = calculate_recall(relevanceAssesments[i], result)
    NT_hazm_precision.append(P)
    NT_hazm_recall.append(R)
    NT_hazm_F.append(calculate_F_measure(P,R))
    NT_hazm_Map.append(calculate_MAP(relevanceAssesments[i], result))
    i += 1
avg_presicion_NT_hazm = sum(NT_hazm_precision) / len(NT_hazm_precision)
avg_recall_NT_hazm = sum(NT_hazm_recall) / len(NT_hazm_recall)
avg_f_NT_hazm = sum(NT_hazm_F) / len(NT_hazm_F)
avg_Map_NT_hazm = sum(NT_hazm_Map) / len(NT_hazm_Map)

# calculations NT_parsivar
i = 0
NT_parsivar_precision = []
NT_parsivar_recall = []
NT_parsivar_F = []
NT_parsivar_Map = []
for result in NT_parsivar:
    P = calculate_precision(relevanceAssesments[i], result)
    R = calculate_recall(relevanceAssesments[i], result)
    NT_parsivar_precision.append(P)
    NT_parsivar_recall.append(R)
    NT_parsivar_F.append(calculate_F_measure(P, R))
    NT_parsivar_Map.append(calculate_MAP(relevanceAssesments[i], result))
    i += 1
avg_presicion_NT_parsivar = sum(NT_parsivar_precision) / len(NT_parsivar_precision)
avg_recall_NT_parsivar = sum(NT_parsivar_recall) / len(NT_parsivar_recall)
avg_f_NT_parsivar = sum(NT_parsivar_F) / len(NT_parsivar_F)
avg_Map_NT_parsivar = sum(NT_parsivar_Map) / len(NT_parsivar_Map)

# calculations NTR_hazm
i = 0
NTR_hazm_precision = []
NTR_hazm_recall = []
NTR_hazm_F = []
NTR_hazm_Map = []
for result in NTR_hazm:
    P = calculate_precision(relevanceAssesments[i], result)
    R = calculate_recall(relevanceAssesments[i], result)
    NTR_hazm_precision.append(P)
    NTR_hazm_recall.append(R)
    NTR_hazm_F.append(calculate_F_measure(P, R))
    NTR_hazm_Map.append(calculate_MAP(relevanceAssesments[i], result))
    i += 1
avg_presicion_NTR_hazm = sum(NTR_hazm_precision) / len(NTR_hazm_precision)
avg_recall_NTR_hazm = sum(NTR_hazm_recall) / len(NTR_hazm_recall)
avg_f_NTR_hazm = sum(NTR_hazm_F) / len(NTR_hazm_F)
avg_Map_NTR_hazm = sum(NTR_hazm_Map) / len(NTR_hazm_Map)

# calculations NTR_parsivar
i = 0
NTR_parsivar_precision = []
NTR_parsivar_recall = []
NTR_parsivar_F = []
NTR_parsivar_Map = []
for result in NTR_parsivar:
    P = calculate_precision(relevanceAssesments[i], result)
    R = calculate_recall(relevanceAssesments[i], result)
    NTR_parsivar_precision.append(P)
    NTR_parsivar_recall.append(R)
    NTR_parsivar_F.append(calculate_F_measure(P, R))
    NTR_parsivar_Map.append(calculate_MAP(relevanceAssesments[i], result))
    i += 1
avg_presicion_NTR_parsivar = sum(NTR_parsivar_precision) / len(NTR_parsivar_precision)
avg_recall_NTR_parsivar = sum(NTR_parsivar_recall) / len(NTR_parsivar_recall)
avg_f_NTR_parsivar = sum(NTR_parsivar_F) / len(NTR_parsivar_F)
avg_Map_NTR_parsivar = sum(NTR_parsivar_Map) / len(NTR_parsivar_Map)

# calculations NTRL_hazm
i = 0
NTRL_hazm_precision = []
NTRL_hazm_recall = []
NTRL_hazm_F = []
NTRL_hazm_Map = []
for result in NTRL_hazm:
    P = calculate_precision(relevanceAssesments[i], result)
    R = calculate_recall(relevanceAssesments[i], result)
    NTRL_hazm_precision.append(P)
    NTRL_hazm_recall.append(R)
    NTRL_hazm_F.append(calculate_F_measure(P, R))
    NTRL_hazm_Map.append(calculate_MAP(relevanceAssesments[i], result))
    i += 1
avg_presicion_NTRL_hazm = sum(NTRL_hazm_precision) / len(NTRL_hazm_precision)
avg_recall_NTRL_hazm = sum(NTRL_hazm_recall) / len(NTRL_hazm_recall)
avg_f_NTRL_hazm = sum(NTRL_hazm_F) / len(NTRL_hazm_F)
avg_Map_NTRL_hazm = sum(NTRL_hazm_Map) / len(NTRL_hazm_Map)

# calculations NTRL_parsivar
i = 0
NTRL_parsivar_precision = []
NTRL_parsivar_recall = []
NTRL_parsivar_F = []
NTRL_parsivar_Map = []
for result in NTRL_parsivar:
    P = calculate_precision(relevanceAssesments[i], result)
    R = calculate_recall(relevanceAssesments[i], result)
    NTRL_parsivar_precision.append(P)
    NTRL_parsivar_recall.append(R)
    NTRL_parsivar_F.append(calculate_F_measure(P, R))
    NTRL_parsivar_Map.append(calculate_MAP(relevanceAssesments[i], result))
    i += 1
avg_presicion_NTRL_parsivar = sum(NTRL_parsivar_precision) / len(NTRL_parsivar_precision)
avg_recall_NTRL_parsivar = sum(NTRL_parsivar_recall) / len(NTRL_parsivar_recall)
avg_f_NTRL_parsivar = sum(NTRL_parsivar_F) / len(NTRL_parsivar_F)
avg_Map_NTRL_parsivar = sum(NTRL_parsivar_Map) / len(NTRL_parsivar_Map)

# calculations NTRS_hazm
i = 0
NTRS_hazm_precision = []
NTRS_hazm_recall = []
NTRS_hazm_F = []
NTRS_hazm_Map = []
for result in NTRS_hazm:
    P = calculate_precision(relevanceAssesments[i], result)
    R = calculate_recall(relevanceAssesments[i], result)
    NTRS_hazm_precision.append(P)
    NTRS_hazm_recall.append(R)
    NTRS_hazm_F.append(calculate_F_measure(P, R))
    NTRS_hazm_Map.append(calculate_MAP(relevanceAssesments[i], result))
    i += 1
avg_presicion_NTRS_hazm = sum(NTRS_hazm_precision) / len(NTRS_hazm_precision)
avg_recall_NTRS_hazm = sum(NTRS_hazm_recall) / len(NTRS_hazm_recall)
avg_f_NTRS_hazm = sum(NTRS_hazm_F) / len(NTRS_hazm_F)
avg_Map_NTRS_hazm = sum(NTRS_hazm_Map) / len(NTRS_hazm_Map)

# calculations raw
i = 0
raw_precision = []
raw_recall = []
raw_F = []
raw_Map = []
for result in raw:
    P = calculate_precision(relevanceAssesments[i], result)
    R = calculate_recall(relevanceAssesments[i], result)
    raw_precision.append(P)
    raw_recall.append(R)
    raw_F.append(calculate_F_measure(P, R))
    raw_Map.append(calculate_MAP(relevanceAssesments[i], result))
    i += 1
avg_presicion_raw = sum(raw_precision) / len(raw_precision)
avg_recall_raw = sum(raw_recall) / len(raw_recall)
avg_f_raw = sum(raw_F) / len(raw_F)
avg_Map_raw = sum(raw_Map) / len(raw_Map)


print("avg_presicion_NT_hazm:", avg_presicion_NT_hazm)
print("avg_recall_NT_hazm:", avg_recall_NT_hazm)
print("avg_F_NT_hazm:", avg_f_NT_hazm)
print("avg_Map_NT_hazm:", avg_Map_NT_hazm)

print("avg_presicion_NT_parsivar:", avg_presicion_NT_parsivar)
print("avg_recall_NT_parsivar:", avg_recall_NT_parsivar)
print("avg_F_NT_parsivar:", avg_f_NT_parsivar)
print("avg_Map_NT_parsivar:", avg_Map_NT_parsivar)

print("avg_presicion_NTR_hazm:", avg_presicion_NTR_hazm)
print("avg_recall_NTR_hazm:", avg_recall_NTR_hazm)
print("avg_F_NTR_hazm:", avg_f_NTR_hazm)
print("avg_Map_NTR_hazm:", avg_Map_NTR_hazm)

print("avg_presicion_NTR_parsivar:", avg_presicion_NTR_parsivar)
print("avg_recall_NTR_parsivar:", avg_recall_NTR_parsivar)
print("avg_F_NTR_parsivar:", avg_f_NTR_parsivar)
print("avg_Map_NTR_parsivar:", avg_Map_NTR_parsivar)

print("avg_presicion_NTRL_hazm:", avg_presicion_NTRL_hazm)
print("avg_recall_NTRL_hazm:", avg_recall_NTRL_hazm)
print("avg_F_NTRL_hazm:", avg_f_NTRL_hazm)
print("avg_Map_NTRL_hazm:", avg_Map_NTRL_hazm)

print("avg_presicion_NTRL_parsivar:", avg_presicion_NTRL_parsivar)
print("avg_recall_NTRL_parsivar:", avg_recall_NTRL_parsivar)
print("avg_F_NTRL_parsivar:", avg_f_NTRL_parsivar)
print("avg_Map_NTRL_parsivar:", avg_Map_NTRL_parsivar)

print("avg_presicion_NTRS_hazm:", avg_presicion_NTRS_hazm)
print("avg_recall_NTRS_hazm:", avg_recall_NTRS_hazm)
print("avg_F_NTRS_hazm:", avg_f_NTRS_hazm)
print("avg_Map_NTRS_hazm:", avg_Map_NTRS_hazm)

print("avg_presicion_raw:", avg_presicion_raw)
print("avg_recall_raw:", avg_recall_raw)
print("avg_F_raw:", avg_f_raw)
print("avg_Map_raw:", avg_Map_raw)
