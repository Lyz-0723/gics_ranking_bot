import pickle

from utils import *


def get_all_data():
    # 修改方向: 第一次先抓所有人(935)的資訊，然後與自己組比較
    # 1. 剩餘題數多 + 土地多的 (打爛他)
    # 2. 剩餘題數少 + 土地多的 (待觀察)
    # 3. 剩餘題數多 + 土地少的 (待觀察)
    # 4. 剩餘題數少 + 土地少的 (安全)

    first_user_id = 7641031  # put first user id
    last_user_id = 7641978  # put last user id

    print("開始爬取資料：")
    groups = {}
    get_group_information(groups, first_user_id, last_user_id)

    print('\n')

    # 存檔
    with open('gics_winner.pickle', 'wb') as f:
        pickle.dump(groups, f)
    return


def scoreboard(limit: int = None):
    with open('gics_winner.pickle', 'rb') as f:
        loaded_data = pickle.load(f)

    # 按小組總分排名
    sorted_ranking = sorted(loaded_data.items(), key=lambda x: x[1]['group_score'], reverse=True)
    if limit:
        sorted_ranking = sorted_ranking[:limit]

    # 輸出排名結果
    print("目前分數排行")
    for rank, (index, info) in enumerate(sorted_ranking, start=1):
        print("第{:03d}隊: {:04d}分 - 第{}名".format(index, info['group_score'], rank))


if __name__ == '__main__':
    user = get_account()
    login(user)
    get_all_data()
    scoreboard()
