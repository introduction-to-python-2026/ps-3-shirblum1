def approximate_pi(n_terms):
    appro_pi = 0
    for i in range (n_terms):
        appro_pi += 4 * ((-1) ** i /(2 * i +1))
    return appro_pi

    
