import pandas as pd
import numpy as np

## 推定結果を読み込み、membership, precision, reacallを表示するだけ

def print_estimation_result(dat_e_a: pd.DataFrame):
  '''print_estimation_result
    推定結果を表示する membership, precision, recall
  '''

  membership = np.mean(dat_e_a["MEMBERSHIP_ESTIMATION"])
  precision = 0; ## TODO
  recall = 0; ## TODO

  print("Membership: " + str(membership))
  print("Precision: " + str(precision))
  print("Recall: " + str(recall))



