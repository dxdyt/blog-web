from datetime import datetime, timezone, timedelta

def get_time_now():
    # 获取当前时间
    now = datetime.now(timezone(timedelta(hours=8)))

    # 将当前时间格式化为 ISO 8601 格式
    iso_time = now.strftime('%Y-%m-%dT%H:%M:%S%z')

    # 将时区偏移量格式化为正确的格式（+08:00）
    iso_time = iso_time[:-2] + ':' + iso_time[-2:]

    return iso_time