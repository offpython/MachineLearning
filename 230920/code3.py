# 가까운 K중에 가장 많이 등장한 y값 구하기

# np.argmax : 최대값의 인덱스
uniques, cnts = np.unique(closest_classes, return_counts=True)
pred = uniques[np.argmax(cnts)]
print(f"{test_data} is classified as {pred}\n")

'''
closest_classes -> [0. 0. 0. 1. 1.]
uniques -> [0. 1.]
cnts -> [3 2]
=> 0이 3번, 1이 2번 나왔음, cnts가 가장 큰 0을 가져와야함 = argmax(counts)
'''
