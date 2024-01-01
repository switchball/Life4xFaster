# coding=utf8

import datetime
import streamlit as st


def render_page():
    st.set_page_config(page_title="人生4倍速", page_icon=":wave:")
    st.title("人生4倍速")
    st.markdown("“人生四倍速”旨在使用一套不同的历法体系，把一个自然年看作“4年”。"
                "这样，现实生活中每一周都对应新历法中的一个月，每个小时皆重要。"
                "这个页面可以帮助快速换算，以此提醒自己时间宝贵。")
    st.markdown("---")


def render_guide():
    pass


def pick_date():
    col_date, col_time = st.columns(2)
    with col_date:
        d1 = st.date_input("请选择日期", datetime.datetime.now())
    with col_time:
        d2 = st.time_input("请选择时间", datetime.datetime.now(), step=datetime.timedelta(minutes=60))
    # 获取datetime1的日期部分，并保留时间为00:00:00
    # date_only = d1.replace(hour=0, minute=0, second=0, microsecond=0)

    # 将datetime2的时间部分与date_only的日期部分合并
    new_datetime = datetime.datetime.combine(d1, d2)
    st.write("选择的日期是：", new_datetime.strftime("%Y-%m-%d %H:%M:%S"))
    return new_datetime

# get today datetime
def get_today_datetime():
    today = datetime.datetime.today()
    # get today month
    today_month = today.month
    st.write('week_day() Monday == 0 ... Sunday == 6', today.weekday())
    # get week index of today
    week_idx = today.isocalendar()
    st.write('week_idx', week_idx, today.isocalendar)
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    render_page()
    render_guide()
    date = pick_date()
    x = get_today_datetime()
    st.write(x)
