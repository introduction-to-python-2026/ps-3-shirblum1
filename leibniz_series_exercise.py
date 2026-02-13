def approximate_pi(n_terms):
    appro_pi = 0
    sign = 1
    for i in range(n_terms):
        appro_pi += sign / (2 * i + 1)
        sign *= -1
    return appro_pi * 4
    
