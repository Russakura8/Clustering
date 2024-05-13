import openpyxl


methods = ["dbscan", "spectral", "kmeans", "gmm", "agglomerative"]


def create_txt(method):
    workbook = openpyxl.load_workbook(f"{method}.xlsx")
    with open(f"{method}.txt", 'w') as f:
        f.write('')
    mink = 0
    if method == "dbscan":
        mink = -1

    for i in range(mink, 5):
        sheet = workbook[str(i)]
        res = dict()
        for column in sheet.iter_cols(values_only=False):
            for cell in column:
                if cell.row == 1:
                    res[cell.value] = dict()

                else:
                    tmp = res[sheet[cell.column_letter + '1'].value]
                    if cell.value not in tmp:
                        tmp[cell.value] = 1

                    else:
                        tmp[cell.value] += 1

        with open(f"{method}.txt", 'a') as f:
            f.write(str(i))
            f.write("\n")
            for key, value in res.items():
                f.write(key)
                f.write('\n')
                for k, v in value.items():
                    f.write(k)
                    f.write(' — ')
                    f.write(str(v))
                    f.write('\n')
                f.write("\n\n")
            f.write("\n\n")

for method in methods:
    create_txt(method)


