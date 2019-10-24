
#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time

import numpy as np
import pandas as pd
from pandas import Series, DataFrame


def get_all_motiftxt_path(dirpath):
    """
    get motif --> sample_output --> knownResults.txt

    return all motif_abs_path

    """

    motif_file_path_list = []

    # 改变工作目录到 path
    os.chdir(dirpath)
    # 一级目录下的所有文件
    all_file = os.listdir(dirpath)

    for file in all_file:
        # 判断是不是目录
        if os.path.isdir(file):
            # 是目录 就 拼接 成二级目录
            path_2nd = os.path.join(dirpath, file)
            # print(path_2nd,"是目录")
            # 进入二级目录
            os.chdir(path_2nd)
            all_file_path_2nd = os.listdir(path_2nd)
            for motif_file in all_file_path_2nd:
                ##  找到 需要的motif文件
                if 'knownResults.txt' in motif_file:
                    abs_path_motif = os.path.join(path_2nd, motif_file)
                    motif_file_path_list.append(abs_path_motif)

                    ## 回到上级目录
                os.chdir(dirpath)
    print("#### already get all motif file path...")
    print(motif_file_path_list)
    print(len(motif_file_path_list))


    return motif_file_path_list


def get_motif_file(abspath_list, out_put):
    """

    Klf4(Zf)/mES-Klf4-ChIP-Seq(GSE11431)/Homer  -->>  Klf4(Zf)

    output  file to out_put

    """
    motif_file_nunber = len(abspath_list)
    save_motif_path_list = []
    for motif_path in abspath_list:

        sample_name = motif_path.split("/")[-2].replace("output", "motif.txt")
        ## read table
        known_results = pd.read_csv("%s" % motif_path, sep='\t')

        motif_name = known_results["Motif Name"].str.split("/", 1).str[0]  # 名字，取/前面的


        ## p_value的值（1e-28）有时候读进pandas 会是str，或者 float64
        p_value = []
        if type(known_results.iloc[:, 2][0]) != str:
            p_value_lie = -np.log10(known_results.iloc[:, 2])
            # 若 p_value > 1e-323 ,取 np.log10 后值会溢出，变成 inf
            for i in p_value_lie:
                if str(i)== "inf":
                    p_value.append(324)
                else:
                    p_value.append(i)
        else:
            for i in known_results.iloc[:, 2]:
                p_value.append(i.split("e")[-1].replace("-", ""))

        ##p_value = -np.log10(known_results.iloc[:, 2])  # P-value 取-log10
        target_persent = known_results.iloc[:, 6].str.split("%").str[0]  # 目标 百分比  去掉%
        background_persent = known_results.iloc[:, 8].str.split("%").str[0]  # 背景 百分比  去掉%

        ## 筛选   %Target  /  % Background  >= 1.5 的，输出P-value
        ##       %Target  /  % Background  < 1.5 的，输出 0
        ##      如果 P-value = 1e0 , 把P-value改成300
        ##      if % Background==0 ，输出0

        p_value_list = []
        x = 0
        for i in range(known_results.shape[0]):
            ## 判断 除数是否为 0
            if float(background_persent[i]) != 0:
                persent = float(target_persent[i]) / float(background_persent[i])
                # print(persent)
                if persent >= enrich_percent:
                    x += 1

                    pppp = int(p_value[i])
                    if pppp == 0:
                        p_value_list.append(300)
                    else:
                        p_value_list.append(pppp)
                else:
                    p_value_list.append(0)
            else:
                p_value_list.append(0)
        # print(p_value_list)
        # print(len(p_value_list))
        # print(x)

        # 新建dataframe 保存 输出数据
        df_motif = DataFrame(data=motif_name)
        df_motif["P-value"] = p_value_list
        # save
        save_path = os.path.join(out_put, sample_name)
        save_motif_path_list.append(save_path)

        df_motif.to_csv("%s" % save_path, index=False, header=False, sep="\t")
        print("%s" % sample_name, "have done ...")

    ## 已经输出的motif 的路径
    return save_motif_path_list
    print("all_____%s_____ motiffile have done ..." % motif_file_nunber)


def join_output_motif_file(motif_path_list):
    """

    将所有的motif表拼接在一起

    输出 main_motif.txt ， 保存在 motif_table_only/目录下

    """
    ## 读取第一个motif文件为主表


    aaaa = motif_path_list[0]
    file_name = "main_motif.txt"
    main_path = os.path.join(os.path.dirname(aaaa), file_name)
    first_motif_name = aaaa.split("/")[-1].replace("_motif.txt", "")
    ## names 是 列名
    main = pd.read_csv("%s" % aaaa, names=["motif", "%s" % first_motif_name], header=None, sep="\t")

    ## 第二个之后表 拼接到第一张表上
    for i in motif_path_list[1:]:
        print(i)
        columns_name = i.split("/")[-1].replace("_motif.txt", "")
        dfx = pd.read_csv("%s" % i, header=None, sep="\t")

        value_list = []
        dict1 = {}  # 用字典存储，key=motif，value=P-value的值
        for i in range(dfx.shape[0]):
            dict1[dfx.iloc[:, 0][i]] = dfx.iloc[:, 1][i]

        for i in main.iloc[:, 0]:
            value_list.append(dict1[i])

        ## 拼接到第一张表上
        main[columns_name] = value_list
        print(columns_name, "已经拼接完成...")

    # 总表保存

    main.to_csv("%s" % main_path, index=False, sep="\t")
    print("已经生成motif总表")

if __name__ == '__main__':
    # 提取所有 ${out}_output文件夹内的 knownResults.txt文件，筛选target/background > 1.2
    # 简化motif名字 ， 输出到指定的文件夹
    #

    # 输入文件位置
    dirpath = "/public/home/yuliu_gibh/DNA-seq/mouce_ATAC/190830_ATAC/motif_genome"
    # 输出文件位置
    out_put = "/public/home/yuliu_gibh/DNA-seq/mouce_ATAC/190830_ATAC/motif_genome/motif_table_only"
    # enrich_percent = target %  / background %  
    enrich_percent = 1.1
    all_motif_path_list = get_all_motiftxt_path(dirpath)
    
    motif_get_2columns = get_motif_file(all_motif_path_list,out_put)
    #time.sleep(3)
    join_output_motif_file(motif_get_2columns)
    
    


