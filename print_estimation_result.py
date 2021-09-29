import numpy as np
import pandas as pd

## 推定結果を読み込み、membership, precision, reacallを表示するだけ

def print_estimation_result(dat_e_a: pd.DataFrame):
  '''print_estimation_result
    推定結果を表示する membership, precision, recall
  '''

  
  recall     = 0 
  recall_member = 0;
  recall_member_estimated = 0
  precision  = 0 
  precision_member = 0;
  precision_member_estimated = 0;
  topk = 0
  topk_member = 0
  topk_member_estimated = 0

  ## 行ごとに計算する
  for row in list(range(dat_e_a.shape[0])):
    ## recallの計算
    ## Membership != -1 な行のうち、何割がメンバーシップと推定されたか
    ## EAが-1でない行の中で、E1が-1で無いものの割合
    if dat_e_a.iat[row,3] != -1:
      recall_member += 1
      if dat_e_a.iat[row,0] != -1:
        recall_member_estimated += 1  

    ## precicionの計算
    ## メンバーシップだと推定した行のうち、何割がメンバーシップだったか
    ## E1が-1でない行の中で、EAが-1で無いものの割合
    if dat_e_a.iat[row,0] != -1:
      precision_member += 1
      if dat_e_a.iat[row,3] != -1:
        precision_member_estimated += 1

    ## topkの計算
    ## EAが-1でない行の中で、E1E2E3で推定が成功しているものの割合
    if dat_e_a.iat[row,3] != -1:
      topk_member += 1;
      s = set(dat_e_a.iloc[row, 0:2])
      if dat_e_a.iat[row,3] in s:
        topk_member_estimated += 1

    
  recall = recall_member_estimated / recall_member
  precision = precision_member_estimated / precision_member
  topk = topk_member_estimated / topk_member


  print("")
  print("----- attack result ------")
  print("Precision: " + str(precision))
  print("Recall: " + str(recall))
  print("topk: " + str(topk))
  return [recall,precision,topk]


