import pandas as pd
from pyecharts.charts import Line, Radar
# 通过学号获取其他学生信息，join

# 1,成绩分析+雷达图

# 展示一段时间内排名分布的走势
# 如果需要计算总成绩的排名，需要先统计所有学生的成绩，并进行排名计算
def score_analyse_series(chengji, stu, date, subject):         #date应该是一个学期列表
    score = pd.read_csv(chengji)

    stu_score = score[(score["mes_StudentID"] == stu)
                      & (score["mes_sub_name"].isin(subject))
                      & (score["exam_term"].isin(date))
                      & (~score["exam_type"].isin([5]))]

    print(stu_score[['mes_StudentID', "mes_Score", "mes_sub_name","exam_numname","mes_T_Score","exam_type"]])

    # 处理考试时间的时刻
    df_exam_date = stu_score["exam_sdate"].tolist()
    exam_date = []
    # print(df_exam_date)
    for date in df_exam_date:
        date = date.split()
        exam_date.append(date[0])
    print(exam_date)

    line =(
        Line()
        .add_xaxis(xaxis_data=exam_date)
        .add_yaxis(
            series_name='成绩分数',
            y_axis=stu_score["mes_Score"].tolist()
        )
    )
    line.render('score.html')

# 分析某个学生某次考试的雷达图，用他的T-score
def score_analyse_radar(chengji, stu, subject):
    score = pd.read_csv(chengji)
    radar = Radar()
    radar.render()
    pass

# 2，消费分析


if __name__ == '__main__':
    # 查询成绩
    chengji = 'data/5_chengji.csv'
    stu = 12669
    date =["2016-2017-1","2016-2017-2"]
    subject = ["数学"]
    score_analyse_series(chengji, stu, date, subject)

    #