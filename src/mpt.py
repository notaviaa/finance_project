import pandas as pd
import numpy as np
import sys

def mpt_sim(p:pd.DataFrame, sims: int):
    mu_m, var_m, tickers = mpt_vectorize(p)

    simulations = []

    for i in range(sims):
        sim = mpt_simulate(mu_m, var_m, tickers)
        row = {
            'Return': sim['return'],
            'Volatility': sim['volatility'],
            'Weight': sim['weights'],
        }
        simulations.append(row)

    final = pd.DataFrame(simulations, columns=['Return', 'Volatility', 'Weight'])
    return final.sort_values(['Return', 'Volatility'], ascending=[False, True])


def mpt_vectorize(p:pd.DataFrame):
    '''
    Docstring for mpt_vectorize
    Takes in a an aggregate vector (of mean, std, var) and output mean, std, var vector
    :param p: Description
    :type p: pd.DataFrame
    
    '''
    # mu return
    aggregate = p.groupby('ticker')['ret'].agg(['mean', 'std','var'])  
    var_m, tickers = mpt_sigma(p)

    # Ensure the order of the mean/variance vectors matches the covariance matrix
    mu_m = aggregate.loc[tickers, 'mean'].to_numpy(dtype=float)
    var_m_test = aggregate.loc[tickers, 'var'].to_numpy(dtype=float)


    if mpt_vector_validation(var_m_test, var_m) == 1:
        return mu_m, var_m, tickers
    # sigma calculation
    return ValueError("Vector is incorrect")

def mpt_sigma(p:pd.DataFrame):
    p['time'] = pd.to_datetime(p['time'])

    R_df = (p.dropna(subset=['ret']))
    R_df = R_df.pivot(index='time', columns='ticker', values='ret')
    R_df = (R_df.dropna()).sort_index()
    print(R_df.columns) 
    r = np.cov(R_df, rowvar=False, ddof=1)
    tickers = list(R_df.columns)
    return r, tickers

def mpt_vector_validation(mu_m, var_m):
    for i in range(len(var_m)):
        if (np.round(var_m[i][i],5) == np.round(mu_m[i], 5)):
            continue
        else:
            return 0
        
    return 1

def mpt_simulate(mu_m: np.array, var_m: np.array, tickers):
    n = len(mu_m)
    w = np.random.dirichlet(alpha = np.ones(n))
    weights = dict(zip(tickers, w))
    portfolio_return = float(np.dot(w, mu_m))
    portfolio_variance = float(w @ var_m @ w)
    portfolio_volatility = float(np.sqrt(portfolio_variance))

    return {
        'return': portfolio_return,
        'volatility': portfolio_volatility,
        f'weights': dict(weights),
    }
