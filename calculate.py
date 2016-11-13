import process
import sentanalysis
import sys

ticker = 'AAPL'


def total(ticker):
    score = sentanalysis.getScore(ticker)
    return score

total(ticker)
