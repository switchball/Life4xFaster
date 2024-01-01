# coding=utf8

from datetime import datetime, timedelta
import streamlit as st


def render_page():
    st.set_page_config(page_title="人生 4 倍速", page_icon=":wave:")
    st.title("人生 4 倍速")
    st.markdown(
        "“人生四倍速”旨在使用一套不同的历法体系，把一个自然年看作“4年”。"
        "这样，现实生活中每一周都对应新历法中的一个月，每个小时皆重要。"
        "这个页面可以帮助快速换算，以此提醒自己时间宝贵。"
    )


def render_guide():
    pass


def pick_date():
    col_date, col_time = st.columns(2)
    with col_date:
        d1 = st.date_input("请选择日期", datetime.now())
    with col_time:
        d2 = st.time_input("请选择时间", datetime.now(), step=timedelta(minutes=60))

    # 将d2的时间部分与d1的日期部分合并
    new_datetime = datetime.combine(d1, d2)

    return new_datetime


def convert_to_new(date: datetime):
    # get month
    today_hour = date.time().hour
    # st.write('week_day() Monday == 0 ... Sunday == 6', date.weekday())
    # get year. week index, weekday in ISO calendar
    year, week_num, weekday = date.isocalendar()

    # divide into four "years"
    new_year = (week_num - 1) // 13 + 1
    new_year = new_year if new_year <= 4 else 4

    # 计算是第多少天的 counter (从 0 开始)
    counter = (week_num - 1) * 7 + (weekday - 1)

    # 人生 4 倍速！
    counter = counter * 4
    # 按照每 6 小时/天 的差量增加
    counter += today_hour // 6
    # 这个天数周期为 28 * (12 + 1) = 364
    counter = counter % 364

    # 重新计算新历法下的第几周和第几天
    new_week_num = counter // 7 + 1
    new_week_day = counter % 7 + 1

    # 再转换成可读性强的X月Y日
    new_month = counter // 28 + 1
    new_day = counter % 28 + 1

    st.markdown("---")
    st.subheader(f"第{new_year}年度")
    st.header(f"{new_month} 月 {new_day} 日")
    if new_month == 13:
        st.success("每年度的第 13 个月为休息月，记得复盘“这一年”的成果哦！")
    # st.write('week_idx', week_idx, today.isocalendar)

    with st.expander("这是如何计算的？查看转换过程"):
        LINK = "https://zh.wikipedia.org/zh-cn/ISO%E9%80%B1%E6%97%A5%E6%9B%86"
        st.write("- 选择的日期是：", date.strftime("%Y-%m-%d %H:%M:%S"))
        st.write(f"- 根据 [ISO周日历]({LINK})，这是 {year} 年的第 {week_num} 周第 {weekday} 天")
        st.write(f"- 每个季度视作一个年度，这是第 {new_year} 年度的第 {counter+1} 天")
        st.write(f"- 转换为新历法，即为：{new_month} 月 {new_day} 日")

    return new_year, new_month, new_day


if __name__ == "__main__":
    render_page()
    render_guide()
    date = pick_date()
    _ = convert_to_new(date)
