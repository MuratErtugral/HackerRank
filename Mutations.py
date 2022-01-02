def mutate_string(string, position, character):
    m = string[:position]+character+string[(position+1):]
    return (m)
