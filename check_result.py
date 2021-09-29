## 推定結果の正解判定を行う関数

import pandas as pd
import numpy as np

def check_result(dat_e : pd.DataFrame, target_team_id : str) -> pd.DataFrame:
  '''check_result
  推定結果と正解データを突合して、メンバシップ推定/再識別の結果を付与する関数

  Args:
    dat_e(pd.DataFrame) : CTの行ごとに推定結果を記入したデータ(100行x3列)
    target_team_id(str) : 攻撃対象のチームID (ex: "01"))
  Return:
    dat_e(pd.DataFrame) : 推定結果に、正解行番号(非メンバなら-1)と、推定結果の正解不正解を付与したデータ(100行x6列)
  '''

  ## 正解の読み込み
  ea_file = "./PWSCUP2021_attack/Share/pre_attack_result/Team03_E_Ea_X/EA/pre_anony_03_for_03_ea.csv"
  dat_ea = pd.read_csv(ea_file, header = None)


  if(dat_e.shape[0] != dat_ea.shape[0]):
    print("推定ファイルの行数はCTファイルと同じ100行にする必要があります")
    return dat_e
  
  if(dat_e.shape[1] != 3):
    print("推定ファイルの列数は3にする必要があります")
    return dat_e

  dat_e.columns = ["E1", "E2", "E3"]

  dat_ea.columns = ["EA"]

  dat_e = pd.concat([dat_e, dat_ea], axis = 1)

  ## 推定結果を付与
  dat_e["MEMBERSHIP_ESTIMATION"] = -1;
  dat_e["REID_ESTIMATION"] = np.nan

  for i in range(dat_e.shape[0]):
    e1 = dat_e["E1"][i]
    e2 = dat_e["E2"][i]
    e3 = dat_e["E3"][i]
    ea = dat_e["EA"][i]

    ## メンバシップ推定結果を付与
    if e1 == -1 and ea == -1:
      dat_e["MEMBERSHIP_ESTIMATION"][i] = 1;
    elif e1 != -1 and ea != -1:
      dat_e["MEMBERSHIP_ESTIMATION"][i] = 1;
    else:
      dat_e["MEMBERSHIP_ESTIMATION"][i] = 0;

    tmp = dat_e["MEMBERSHIP_ESTIMATION"][i]
    if ea != -1 and tmp == 1:
      if e1 == ea or e2 == ea or e3 == ea:
        dat_e["REID_ESTIMATION"] = 1
      else:
        dat_e["REID_ESTIMATION"] = 0

  return(dat_e)


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


