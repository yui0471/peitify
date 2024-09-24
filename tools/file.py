#!/usr/bin/env python3
# -*- coding : utf-8 -*-
#
# 【Peitify - DiscordBot】
# peitify.tools.file.py
#

import traceback

import yaml


def load_yaml(file_path):
    """
    yamlファイルを読み込み、辞書型で返す

    Parameters
    ----------
    file_path: str
        読み込むYAMLファイルのパスを指定

    Returns
    -------
    yaml_dict: dictionary
        YAMLファイルを変換した辞書型オブジェクト

    """
    try:
        with open(file_path, "r", encoding="utf-8")as file:
            yaml_dict = yaml.safe_load(file)
        
        return yaml_dict
    
    except Exception as e:
        traceback.print_exc()
        print(e)
        return False


def validation_config(config_dict):
    """
    必須データが存在するか、データ型が合っているかチェックする

    Parameters
    ----------
    config_dict: dictionary
        config.yamlをload_yaml関数を通した辞書型オブジェクト

    Returns
    -------
    return: bool
        バリデーションチェックに成功したらTrue、失敗したらFalseを返す

    """
    check_dict = {
        "TOKEN" : "str"
    }

    set_check_elements = set(check_dict.keys())
    set_config_elements = set(config_dict.keys())
    
    # 指定されたkeyのみが存在しているか確認
    if set_check_elements != set_config_elements:
        return False
    
    # check_dictと実際の型が合っているか確認
    for key in config_dict.keys():
        if "str" == check_dict[key]:
            if type(config_dict[key]) is not str:
                return False

        elif "int" == check_dict[key]:
            if type(config_dict[key]) is not int:
                return False
            
        elif "list" == check_dict[key]:
            if type(config_dict[key]) is not list:
                return False
            
        elif "dict" == check_dict[key]:
            if type(config_dict[key]) is not dict:
                return False

        else:
            return False

    return True
