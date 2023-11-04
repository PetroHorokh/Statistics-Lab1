import random
import math
from const import n, a, v, max_v, min_v
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


def random_variable():
    r_v = sum([random.uniform(0, 1) for _ in range(12)])
    result = (r_v - 6) * a + v

    return result


def data_collector(i):
    data = [random_variable() for _ in range(i)]
    data.sort()
    return data


def intervals(rounder):
    count_intervals = int(1 + 1.44 * math.log(n)) + 1
    step = (max_v - min_v) / count_intervals
    interval_list = [round(min_v + step * i, rounder) for i in range(count_intervals + 1)]
    interval_list.sort()
    return interval_list


def labels(intervals):
    labels = [f"[{intervals[i]};{intervals[i + 1]}]" for i in range(len(intervals) - 1)]
    return labels


def interval_diagram(data):
    df = pd.DataFrame(data, columns=['Grades'])

    bins = intervals(2)
    labels_list = labels(bins)

    df['Grade Interval'] = pd.cut(df['Grades'], bins=bins, labels=labels_list)

    frequency_table = df['Grade Interval'].value_counts()

    return frequency_table


def histogram(data):
    bins = intervals(2)
    hist, _ = np.histogram(data, bins=bins)
    relative_frequencies = hist / np.sum(hist)

    plt.bar(range(len(relative_frequencies)), relative_frequencies,
            tick_label=[f"{i}-{j}" for i, j in zip(bins[:-1], bins[1:])])

    plt.xlabel('Інтервали')
    plt.ylabel('Відносна частота')
    plt.xticks(rotation=30)

    plt.show()


def valuation(data):
    xv = sum(data) / len(data)
    s2 = sum([(data[i] - xv) ** 2 for i in range(len(data))]) / len(data) - 1
    s = math.sqrt(s2)
    print(f"Xv = {xv}")
    print(f"s^2 = {s2}")
    print(f"s = {s}")


def approximation(data):
    bins = np.linspace(min(data), max(data), 10)

    mean = np.mean(data)
    std = np.std(data)

    x = np.linspace(min(data), max(data), 100)
    pdf = norm.pdf(x, mean, std)

    plt.hist(data, bins, density=True, alpha=0.6, label='Гістограма відносних частот')
    plt.plot(x, pdf, '-o', label='Нормальний розподіл')

    plt.xlabel('Значення')
    plt.ylabel('Відносна частота')
    plt.legend()

    plt.show()
