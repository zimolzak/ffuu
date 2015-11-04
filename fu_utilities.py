def matrix2csv(matrix):
    return '\n'.join(map(lambda x: ','.join(map(str, x)), matrix))
