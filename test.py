import pkgutil

data = pkgutil.get_data('restidy.db', "gene_db_mapping.tsv")

print(data)
